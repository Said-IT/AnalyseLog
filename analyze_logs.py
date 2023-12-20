import re

def analyze_logs(file_path):
    # Define regex patterns for unusual activities
    alert_pattern = re.compile(r'ERROR|ALERT|CRITICAL', re.IGNORECASE)
    suspicious_ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')  # Example pattern to detect suspicious IP addresses

    with open(file_path, 'r') as log_file:
        lines = log_file.readlines()

        for line_number, line in enumerate(lines, start=1):
            # Analyze unusual activities with regex patterns
            if alert_pattern.search(line):
                print(f"Alert detected at line {line_number}: {line.strip()}")
            if suspicious_ip_pattern.search(line):
                suspicious_ip = suspicious_ip_pattern.search(line).group()
                print(f"Suspicious IP address detected at line {line_number}: {suspicious_ip}")

if __name__ == "__main__":
    log_file_path = "path/to/your/file/logs.txt"
    analyze_logs(log_file_path)
