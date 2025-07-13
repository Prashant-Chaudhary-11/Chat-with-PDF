from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os, fitz
from dotenv import load_dotenv
import google.generativeai as genai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()
chunks = []
vectorizer = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    dir_path = "temp"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)  # create 'temp' folder if not present

    path = f"{dir_path}/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    global chunks, vectorizer
    chunks = extract_chunks(path)
    texts = [c["text"] for c in chunks]
    vectorizer = TfidfVectorizer().fit(texts)
    return {"message": "PDF processed", "pages": len(chunks)}

@app.post("/ask")
def ask_question(query: Query):
    if not chunks or not vectorizer:
        return {"error": "No PDF uploaded"}

    vectors = vectorizer.transform([c["text"] for c in chunks] + [query.question])
    similarities = cosine_similarity(vectors[-1], vectors[:-1])
    best_idx = similarities.argmax()
    matched = chunks[best_idx]

    prompt = f"""The user asked: {query.question}

Here is a relevant passage from a PDF:
\"\"\"
{matched['text']}
\"\"\"

Please answer the question based on the content.
"""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    return {
        "answer": response.text,
        "page": matched["page"],
        "highlight": query.question,
        "chunk": matched["text"]
    }

def extract_chunks(path, chunk_size=800):
    doc = fitz.open(path)
    result = []
    for i, page in enumerate(doc):
        text = page.get_text()
        for start in range(0, len(text), chunk_size):
            result.append({"page": i + 1, "text": text[start:start + chunk_size]})
    return result

@app.get("/health")
def health():
    return {"message": "OK"}