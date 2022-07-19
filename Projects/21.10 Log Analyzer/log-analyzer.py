from pathlib import Path

"""
Goes through the file line by line
Saves error lines from file to list
returns list and count of errors
"""
def analyze_file(filePath):
    count = 0
    error_list = []
    phrase = ' ERROR - '

    with open(filePath) as file:
        for line in file:
            if phrase in line:
                error_list.append(line.rstrip('\n'))
                count = count + 1
    
    return count, error_list


total_errors = 0
log_errors = []

log_path = '/home/dakota/airflow/airflowhome/logs/dag_id=market_vol'
path_list = Path(log_path).rglob('*.log')


"""
Takes a list of file paths
Goes though each file path and finds errors
"""
for filePath in path_list:
    count = 0
    cur_list = []

    count, cur_list = analyze_file(filePath)
    total_errors = total_errors + count
    log_errors.extend(cur_list)


"""
Prints out errors
"""
print(f'Total number of errors: {total_errors}')
print('Here are all the errors:')

for error in log_errors:
    print(error)