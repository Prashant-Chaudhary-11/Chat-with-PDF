# 📄 Chat with PDF using Gemini AI

A full-stack web app where users can upload a PDF, ask questions about it, and receive answers based on the document's content using vector search and Gemini Pro.

---

## 🌐 Live Demo

🔗 [https://chattingwithpdf.netlify.app/](https://chattingwithpdf.netlify.app/)

---

## 🔧 Features

- 🗂 Upload a PDF and preview it on the left side.
- 💬 Chat interface on the right for asking questions.
- 📚 Text chunks are vectorized using TF-IDF for semantic search.
- 🤖 Gemini API is used to generate responses based on matched content.

---

## 🖼 Interface Overview

- **Left Pane**: PDF viewer with scroll and optional highlight support.
- **Right Pane**: Chat input/output with Gemini-generated answers.

---

## 🚀 Tech Stack

- **Frontend**: HTML, JavaScript (Vanilla), PDF.js
- **Backend**: Python (FastAPI), Gemini Pro (via `google.generativeai`)
- **Vector Search**: TF-IDF + Cosine Similarity (via `scikit-learn`)
- **PDF Parsing**: PyMuPDF (`fitz`)

---

## 📁 Project Structure

```
ChatWithPdf/
├── backend/
│   ├── app.py              # FastAPI backend logic
│   └── utils.py            # PDF processing and chunking
├── frontend/
│   └── index.html          # Frontend interface
├── .env                    # API keys and config
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🛠 Setup Instructions

### 1. Clone the repository
```bash
git clone git@github.com:Prashant-Chaudhary-11/Chat-with-PDF.git
cd Chat-with-PDF
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key
Create a `.env` file in the `backend` folder:
```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the backend
```bash
cd backend
uvicorn app:app --reload --port 8000
```

### 5. Open the frontend
Open `frontend/index.html` in your browser directly or serve it via a local HTTP server.

---

## 🌐 Deployment Notes

- Use **Render**, **Railway**, or **Deta Space** for Python backend hosting.
- Serve the frontend on **Netlify**, **Vercel**, or any static host.
- Make sure CORS is enabled in FastAPI if deploying separately.

---

## 🤝 Contributions

Pull requests and issues are welcome. Please ensure code is well-commented and clean.

---

## 🧠 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Prashant Chaudhary**  
📧 [prashantchaudhary1106@gmail.com](mailto:prashantchaudhary1106@gmail.com)  
🌐 [GitHub Profile](https://github.com/Prashant-Chaudhary-11)
