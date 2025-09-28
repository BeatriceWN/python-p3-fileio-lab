def write_file(file_name, file_content):
    full_file_name = f"{file_name}.txt"
    
    with open(full_file_name, 'w') as file:
        file.write(file_content)
    
    print(f"Content written to {full_file_name}")


def append_file(file_name, append_content):
    full_file_name = f"{file_name}.txt"
    
    with open(full_file_name, 'a') as file:
        file.write(append_content) 
    
    print(f"Content appended to {full_file_name}")

def read_file(file_name):
    full_file_name = f"{file_name}.txt"
    
    try:
        with open(full_file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: {full_file_name} does not exist.")
        return None




from lib.file_io import write_file, append_file, read_file

#create a new log file
write_file(file_name="logfile", file_content="Log 1: 5 bananas added") #output: Log 1: 5 bananas added

#append new logs
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted") #output: Log 2: 3 bananas subtracted
append_file(file_name="logfile", append_content="Log 3: 10 bananas sold") #output: Log 3: 10 bananas sold

#read the log file
content = read_file(file_name="logfile")
print(content)