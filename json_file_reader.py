# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:07:14 2019
@author: creddersen
"""
"""JSON FILE READER"""
# This is the code I used to read a log from a tenable scan ran 
# against a router. I wanted to know what commands the scan ran 
# on the router. 
import json 
with open("C:/ssh_command.json", 'r') as json_file:
    data = json_file.readlines()
    for line in data:
        obj = json.loads(line)
        #I only wanted the commands listed in the file so..
        print(str(obj['command']))
