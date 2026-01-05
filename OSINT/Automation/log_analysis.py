# Simple log analysis script
# Created for learning basic security automation

def analyze_log(file_name):
    try:
        with open(file_name, "r") as file:
            for line in file:
                if "error" in line.lower():
                    print("Error found:", line.strip())
    except FileNotFoundError:
        print("Log file not found")

# Example usage
analyze_log("sample.log")
