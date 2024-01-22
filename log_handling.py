def process_log_file(input_file, output_file):
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
    
    answers = []
    answers.append(f"Login OK: {ok_count}")
    answers.append(f"Login Incorrect: {err_count}")

    # Write answers to the output file
    with open(output_file, 'a') as answers_file:
        answers_file.write('\n'.join(answers))

# Example usage:
input_log_file = "kursain.log"
output_answers_file = "answers.txt"
process_log_file(input_log_file, output_answers_file)
