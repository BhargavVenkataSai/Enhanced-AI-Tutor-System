# Enhanced AI Learning Tutor

An advanced AI-powered learning assistant that helps users research topics, personalize their learning journey, and generate insightful reports with interactive learning features.

---

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8+
- OpenAI API key

### Using Docker (Recommended):

```bash
docker build -t ai-tutor .
docker run -p 8501:8501 -e OPENAI_API_KEY=your_api_key ai-tutor
```

### Manual (Local Environment):

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

4. Run the application:

```bash
streamlit run app.py
```

---

## 🧠 System Architecture

```
User Input → Research (Web, Papers, Videos)
           → Personalization Questions
           → Interactive Learning (AI Tutor)
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

Users are presented with categorized questions (single/multi-select, text input). These responses shape the structure and focus of the final report and learning experience.

---

## 🤖 AI Tutor Features

The enhanced AI tutor provides:

1. **Concept Explorer**: Detailed explanations of key concepts with examples and analogies
2. **Interactive Quizzes**: AI-generated quizzes with instant feedback
3. **Practice Problems**: Step-by-step solutions to reinforce learning
4. **Personalized Learning Path**: Custom curriculum based on user knowledge and goals
5. **Q&A Interface**: Ask questions and get detailed answers
6. **Progress Tracking**: Monitor learning progress and identify areas for improvement

---

## 📄 Report Generation

A structured report is generated using:

- Topic summary
- Merged findings
- Custom feedback integration

---

## ⚠️ Limitations & Future Improvements

- Add real API integration (Semantic Scholar, YouTube)
- Improve summarization with more advanced LLM techniques
- Add multilingual support
- Better feedback-to-report logic
- Implement user accounts and progress saving
- Add collaborative learning features

---

## 📁 Sample I/O

See `/samples/` for:

- Sample topic input
- Generated HTML report

---

## 👨‍💻 Author Notes

This project showcases:

- Streamlit UI
- OpenAI API integration
- Modular AI agents
- Good system design and documentation
