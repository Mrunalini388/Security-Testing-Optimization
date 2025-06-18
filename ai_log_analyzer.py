import re
import numpy as np
from sklearn.ensemble import IsolationForest

# Load logs from file
def load_logs(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Extract features: line length, keyword count, IP presence, URL, status code
def extract_features(log_lines):
    keywords = ['vulnerability', 'error', 'warning', 'outdated', 'critical', 'phpinfo']
    features = []

    for line in log_lines:
        length = len(line)
        keyword_count = sum(1 for k in keywords if k in line.lower())
        ip_presence = 1 if re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line) else 0
        url_presence = 1 if 'http' in line.lower() else 0
        status_code = 1 if re.search(r'\b\d{3}\b', line) else 0
        features.append([length, keyword_count, ip_presence, url_presence, status_code])
    
    return np.array(features)

# Load logs
nmap_logs = load_logs('example_nmap.txt')
nikto_logs = load_logs('example_nikto.txt')
combined_logs = nmap_logs + nikto_logs
sources = ['[Nmap]'] * len(nmap_logs) + ['[Nikto]'] * len(nikto_logs)

# Extract features and train model
features = extract_features(combined_logs)
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(features)
predictions = model.predict(features)

# Display and save results
print("\n--- Anomaly Detection Results ---")
with open("anomaly_detection_results.txt", "w") as out:
    for i, line in enumerate(combined_logs):
        status = "Anomaly" if predictions[i] == -1 else "Normal"
        result = f"[{status}] {sources[i]} {line.strip()}"
        print(result)
        out.write(result + "\n")

print("\nResults saved to anomaly_detection_results.txt")

