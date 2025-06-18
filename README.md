## 📝 Sample Logs Required

This tool expects two log files in the project directory:

- `example_nmap.txt` — Nmap scan logs
- `example_nikto.txt` — Nikto scan logs

> ⚠️ **Important:** These files should contain raw scan results from Nmap and Nikto respectively.  
> If these files are missing or empty, the script will throw a `FileNotFoundError`.

---

## ⚙️ Setup and Usage

# 1. Clone the repository
git clone https://github.com/hni388/Security-Testing-Optimization.git
cd Security-Testing-Optimization

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate         # Linux/macOS
# OR
venv\Scripts\activate            # Windows

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Provide your actual Nmap and Nikto scan log files named:
#    - example_nmap.txt
#    - example_nikto.txt
#    in the root project directory

# 5. Run the anomaly detection script
python ai_log_analyzer.py


