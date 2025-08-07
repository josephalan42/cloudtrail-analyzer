# 🔍 CloudTrail Event Analyzer

This Flask-based tool helps visualize and analyze AWS CloudTrail log files (JSON format). It parses CloudTrail logs to identify security-relevant actions and presents the data in a web interface.

---

## 📌 Features

- Upload and parse CloudTrail `.json` log files
- Highlight suspicious or sensitive API calls (e.g., `StopLogging`, `PutUserPolicy`)
- Web interface built with Flask
- Easily extendable for custom detection rules

---

## ⚙️ Stack

- Python 3
- Flask
- Boto3 (for optional future AWS integrations)

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/cloudtrail-analyzer.git
cd cloudtrail-analyzer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
