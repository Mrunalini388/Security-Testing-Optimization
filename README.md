# AI-Based Log Anomaly Detector

This tool automates security log analysis by combining traditional scanners (Nmap, Nikto) with AI-based anomaly detection using Python.

 Features
•	Uses Nmap and Nikto log files
•	Extracts key features (line length, keywords, IPs, etc.)
•	Applies Isolation Forest to detect abnormal patterns
•	Outputs a clear report of anomalies vs. normal entries

 Tech Stack
•	Python 3.x
•	Numpy
•	scikit-learn (IsolationForest)
