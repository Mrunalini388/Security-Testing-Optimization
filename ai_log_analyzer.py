import re
import numpy as np
from sklearn.ensemble import IsolationForest
import pyfiglet
import os

def print_logo():
    logo = pyfiglet.figlet_format("LOGIQ")
    print(logo)
    print("🔍 Smart AI intelligence for detecting anomalies in your security logs.")
    print("🔐 Developed by Mrunalini\n")

# Function to load and preprocess scan logs
def load_logs(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found. Please ensure it exists.")
        return []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# Extract simple features from log lines (length and keyword matches)
def extract_features(log_lines):
    features = []
    keywords = ['vulnerability', 'error', 'warning', 'outdated', 'critical', 'phpinfo']
    
    for line in log_lines:
        # Feature 1: Length of the line
        line_length = len(line)
        
        # Feature 2: Count of keyword matches in the line
        keyword_count = sum(1 for keyword in keywords if keyword.lower() in line.lower())
        
        features.append([line_length, keyword_count])
    
    return np.array(features)

def main():
    print_logo()

    # Load logs from Nmap and Nikto
    nmap_logs = load_logs('example_nmap.txt')
    nikto_logs = load_logs('example_nikto.txt')

    # Combine logs for analysis
    combined_logs = nmap_logs + nikto_logs

    if not combined_logs:
        print("No logs loaded. Exiting...")
        return

    # Extract features for the AI model
    features = extract_features(combined_logs)

    # Fit the Isolation Forest for anomaly detection
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(features)

    # Predict anomalies (-1 means anomaly, 1 means normal)
    predictions = model.predict(features)

    print("\n--- Anomaly Detection Results ---")
    for i, line in enumerate(combined_logs):
        status = "Anomaly" if predictions[i] == -1 else "Normal"
        print(f"[{status}] {line.strip()}")

    # Save results to a file
    with open("anomaly_detection_results.txt", "w") as result_file:
        for i, line in enumerate(combined_logs):
            status = "Anomaly" if predictions[i] == -1 else "Normal"
            result_file.write(f"[{status}] {line.strip()}\n")

    print("\nResults saved to anomaly_detection_results.txt")

if __name__ == "__main__":
    main()


