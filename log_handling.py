import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

def process_log_file(input_file):
    log_file = open(input_file, 'r')
    # Read lines from the log file
    ok_count = 0
    err_count = 0
    for line in log_file:
        if "Login OK" in line:
            ok_count += 1
        elif "Login incorrect" in line:
            err_count += 1
    
    log_file.close()
    
    print(f"Login OK: {ok_count}")
    print(f"Login Incorrect: {err_count}")

    
# Example usage:
input_log_file = sys.argv[1]
process_log_file(input_log_file)
