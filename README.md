## Features

- Processes raw scan logs from Nmap and Nikto  
- Extracts simple features such as line length and presence of security-related keywords  
- Applies Isolation Forest, an unsupervised AI algorithm, to detect anomalous log lines  
- Labels log entries as Normal or Anomaly to help identify suspicious events  
- Saves detailed results to a report file for review and further analysis  

---

## Prerequisites

- Python 3.7+  
- Required packages: numpy, scikit-learn  

---

## Setup & Usage

### Clone the repository

```bash
git clone https://github.com/Mrunalini388/Security-Testing-Optimization.git
cd Security-Testing-Optimization

Create and activate virtual environment
macOS/Linux:
python -m venv venv
source venv/bin/activate
Windows:
python -m venv venv
venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Add your Nmap and Nikto scan logs
Place these files in the root directory:
example_nmap.txt
example_nikto.txt

Run anomaly detection
python ai_log_analyzer.py




