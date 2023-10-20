import colorama, os
from colorama import Fore, Style

# Specify the directory where you want to search for .log files
log_directory = 'log'

# List all files ending with .log in the directory
log_files = [file for file in os.listdir(log_directory) if file.endswith('.log')]

# Display the list of log files with corresponding numbers
print("List of .log files:")
for index, file in enumerate(log_files, start=1):
    print(f"{Fore.YELLOW}[{index}]{Style.RESET_ALL} {file}")

# Prompt the user to select a file by its corresponding number
while True:
    try:
        choice = int(input("Enter the number of the file you want to view: "))
        if 1 <= choice <= len(log_files):
            selected_file = log_files[choice - 1]
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Read and print the contents of the selected file
selected_file_path = os.path.join(log_directory, selected_file)
with open(selected_file_path, 'r') as file:
    file_contents = file.read()


def find_state_changes(log_file_path):
    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()

    state_changes = []

    current_state = None
    current_time = None

    for line in lines:
        parts = line.split(' | ')
        if len(parts) == 2:
            time, status = parts
            if 'Online' in status:
                if current_state == 'Offline':
                    state_changes.append((current_time, time, f'{Fore.GREEN}Online{Style.RESET_ALL}'))
                current_state = 'Online'
            else:
                if current_state == 'Online':
                    state_changes.append((current_time, time, f'{Fore.RED}Offline{Style.RESET_ALL}'))
                current_state = 'Offline'
            current_time = time

    return state_changes

log_file_path = f'log/{selected_file}'
changes = find_state_changes(log_file_path)

print("")

for change in changes:
    print(f"{change[1]} | {selected_file.replace('.log', '')} went {change[2]}")
