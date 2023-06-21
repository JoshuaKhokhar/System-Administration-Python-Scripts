"""
Script Name: managingWindowsServices.py
Author: Joshua Khokhar
Creation Date: 6/21/2023
Purpose: This script finds the service it is provided with to start or stop it and prints a response to the IDE.
Instructions: To start or stop any service using this script, replace the "BITS" argument for the Name parameter with the service you would like to start or stop, and run the script.
"""

import wmi

c = wmi.WMI()

for service in c.Win32_Service(Name="BITS"):
    if service.State == "Stopped":
        service.StartService()
        print(service.Name + " is " + service.State)
    if service.State == "Running":
        service.StopService()
        print(service.Name + " is " + service.State)
    
    
