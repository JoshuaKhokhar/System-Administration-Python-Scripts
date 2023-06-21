"""
Script Name: findAndTerminateProcess.py
Author: Joshua Khokhar
Creation Date: 6/21/2023
Purpose: This script finds the process it is provided with and terminates it.
Instructions: To test this script, open up the Notepad application and run this script.
If the Notepad application terminates after runnning this script, it is functioning properly.
To terminate any process using this script, replace the "Notepad.exe" parameter for Name with the process you would like to terminate and run the script.
"""

import wmi
c = wmi.WMI()

for process in c.Win32_Process(Name="Notepad.exe"):
    print(process.Name, process.ProcessId, process.VirtualSize)
    process.terminate
