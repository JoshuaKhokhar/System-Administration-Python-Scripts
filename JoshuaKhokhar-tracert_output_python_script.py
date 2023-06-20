"""
Script Name: JoshuaKhokhar-tracert_output_python_script.py
Author: Joshua Khokhar
Creation Date: 6/20/2023
Purpose: Retreives the number and duration of hops encountered by the packet
on its way to its destination and writes it to a text file.
"""

import subprocess
import datetime
import socket

# Get the current timestamp
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

website = input("What website would you like to go to? ")

# Run tracert command and capture the output
command = ['tracert', website]
output = subprocess.run(command, capture_output=True, text=True)

# Get the hostname
hostname = socket.gethostname()

# Generate the output file name
output_file = f"tracert_{hostname}_{timestamp}.txt"

# Write the output to the text file
with open(output_file, 'w') as file:
    file.write(hostname)
    file.write('\n')
    file.write(timestamp)
    file.write(output.stdout)

print(f"Tracert output has been written to {output_file}")
