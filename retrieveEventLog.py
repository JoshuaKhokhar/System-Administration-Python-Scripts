"""
Script Name: retrieveEventLog.py
Author: Joshua Khokhar
Creation Date: 6/22/2023
Purpose: This script retrieves information from the Application section of the Windows Logs in the Event Viewer and writes it to a csv file.
"""

import csv
import win32evtlog
import win32evtlogutil
import socket
from datetime import datetime

log_source = "Application"
event_src = win32evtlog.OpenEventLog(None, log_source)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
events = win32evtlog.ReadEventLog(event_src, flags, 0)

# Get the hostname
hostname = socket.gethostname()

# Get the current timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Create a CSV file name based on the hostname and timestamp
csv_file = f"{hostname}_{timestamp}_event_log_output.csv"

# Open the CSV file to write the output
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["EventID", "TimeGenerated", "Message"])  # Write header row

    for event in events:
        event_id = event.EventID
        time_generated = event.TimeGenerated.Format()
        message = win32evtlogutil.SafeFormatMessage(event, log_source)

        # Write the event details to the CSV file
        writer.writerow([event_id, time_generated, message])

print("Output has been written to", csv_file)
