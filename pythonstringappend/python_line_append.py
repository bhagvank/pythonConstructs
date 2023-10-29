with open('log.txt') as file:
    log_file = file.readlines()

new_log_lines = ''
for line in log_file:
    if line[:6] == 'ERROR:':
        new_log_lines = new_log_lines + line
        
print(new_log_lines)        