"""
Author: Joshua Khokhar
Created: 6/17/2023
Purpose: Retrives current system information and writes it to a CSV file
"""

import csv
import subprocess
import socket
from datetime import datetime

def get_system_info():
    # Run the systeminfo command and capture the output
    result = subprocess.run('systeminfo', capture_output=True, text=True)

    # Extract relevant system information
    lines = result.stdout.split('\n')
    info = []
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            info.append([key.strip(), value.strip()])

    return info

def write_to_csv(info, filename):
    # Write the system info to the CSV file
    with open(filename, 'w', newline='', encoding='utf-16') as file:
        writer = csv.writer(file)
        for row in info:
            writer.writerow(row)

# Retrieve system information
system_info = get_system_info()

# Get the hostname
hostname = socket.gethostname()

# Get the current timestamp
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Construct the CSV filename using hostname and timestamp
filename = f'{hostname}_{timestamp}.csv'

# Write system information to the CSV file
write_to_csv(system_info, filename)
print(f"System information has been written to {filename}.")
