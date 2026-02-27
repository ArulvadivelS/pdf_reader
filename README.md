# WASDE Commodity Report Summarizer

An AI-powered Streamlit application that processes official USDA WASDE PDF reports and generates structured summaries by commodity (Wheat, Rice, Oilseeds, Cotton, Sugar, Livestock, etc.).

The application extracts commodity-specific commentary from WASDE reports and produces concise analytical summaries using a configurable Large Language Model (LLM).

---

## Key Features

- Upload official USDA WASDE PDF reports
- Automatic detection of commodity sections
- AI-generated summaries for each commodity
- Support for multiple LLM providers
- Configurable models and token settings
- Clean, interactive Streamlit user interface
- Environment-based API key management

---
## Project Structure

pdf_reader/
├── app.py
├── packages.txt
├── .env.example
├── README.md
├── src/
│   ├── core/
│   │   ├── config.py
│   │   └── constants.py
│   ├── services/
│   │   ├── pdf_service.py
│   │   └── summary_service.py
│   ├── utils/
│   │   └── file_utils.py
│   └── ui/
│       └── theme.py

## 🛠 Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd pdf_reader
```
### Create virtual environmet and activate

```bash
python -m venv venv

venv\Scripts\activate.bat
```

### Install Required Dependencies

```bash
pip install -r requirements.txt
```

Generate an API key: https://console.groq.com/keys

Create a .env file in the project root and configure:

GROQ_API_KEY=your_key_here

### Run the app

```bash
streamlit run app.py
```