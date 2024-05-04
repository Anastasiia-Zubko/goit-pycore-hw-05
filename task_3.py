def parse_log_line(line: str) -> dict:
    date, time, level, *msg = line.split() # split the line into variables date time level and message
    return { 
        'date': date,
        'timestamp': time,
        'level': level.upper(), 
        'message': ' '.join(msg) } # assign the variebles to corresponding keys in a dict 

def load_logs(file_path: str) -> list:
    logs = [] # create an empty list
    with open(file_path, "r") as file: # open the file 
        for line in file: # iterate through each line of the file
            logs.append(parse_log_line(line)) # # parse each line with parse_log_line function and append to the earlier created list
    return logs 


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level, logs)) # filter through levels


def count_logs_by_level(logs: list) -> dict:
    counts = {} # create an empty dict
    for log in logs: # iterate through each entry in logs
        level = log["level"] # check for level match
        counts[level] = counts.get(level, 0) + 1 # add 1 for each level repetition found 
    return counts


def display_log_counts(counts: dict):
    print("Logging level    | Quantity") # print header of the display message 
    print("-----------------|----------") # print header of the display message 
    for level, count in counts.items(): # iterate through level and counts in the counts dict
        print(f"{level.upper():<17}| {count}") # print the level and the corressponding count (number of times it was found)


def display_log_details(logs: list):
    print("\nLogs:") # print header of the display message 
    for log in logs: # iterate through each entry in the logs list
        print(f"{log['timestamp']} - {log['message']}") # print the timestamp and the message of each log


def main():
    file_path = "logfile.log" # path to the log file
    try:
        logs = load_logs(file_path) # loading the file using the function load_logs
    except FileNotFoundError: # processing error in case the file is not found
        print("File is not found")
        return
    
    display_log_details(logs) 
    count = count_logs_by_level(logs)
    filter = filter_logs_by_level(logs, "INFO")
    display_log_counts(count)
    display_log_details(filter)
    

if __name__ == "__main__":
    main()