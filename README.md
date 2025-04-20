
# Enhanced AI Tutor System

An AI-powered learning assistant that helps users research topics, personalize their learning journey, and generate insightful reports.

---

## 🚀 Setup Instructions

### Using Docker (Recommended):
```bash
docker build -t ai-tutor .
docker run -p 8501:8501 ai-tutor
```

### Manual (Local Environment):
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧠 System Architecture

```
User Input → Research (Web, Papers, Videos)
           → Personalization Questions
           → Report Generation
           → Feedback-based Regeneration
```

---

## 🔍 Research Methodology

The system pulls research from:
- 🌐 Web Articles
- 📚 Academic Papers (simulated)
- 🎥 YouTube Video Transcripts

It summarizes and consolidates the content using pre-trained transformers.

---

## 🎯 Personalization Approach

Users are presented with categorized questions (single/multi-select, text input). These responses shape the structure and focus of the final report.

---

## 📄 Report Generation

A structured report is generated using:
- Topic summary
- Merged findings
- Custom feedback integration

---

## ⚠️ Limitations & Future Improvements

- Add real API integration (Semantic Scholar, YouTube)
- Improve summarization with LLM integration (OpenAI or open-source)
- Add multilingual support
- Better feedback-to-report logic

---

## 📁 Sample I/O

See `/samples/` for:
- Sample topic input
- Generated HTML report

---

## 👨‍💻 Author Notes

This project showcases:
- Streamlit UI
- Modular AI agents
- Good system design and documentation

