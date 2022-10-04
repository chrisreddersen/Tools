# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:19:27 2022

@author: chris
"""

#script will use VirusTotal to query data for the sha256 hash of a binary using its banned md5 hash.
# the md5 hashes are in a text file. the list was curated from CB banned hashes data. 

import requests
import json


# API information. 

api_url = 'https://www.virustotal.com/api/v3/search?query='
headers = {'x-apikey': 'fc69d15e41443a043f4d5c7c427b2ecd67c1161f31b1cd867953ce7ea40375fa'}

# the function reads the list of md5 hashes, then couples them with the query to form a complete GET request.
def get_sha256():
    with open('banned_md5.txt', 'r') as md5_file:
        lines = md5_file.readlines()
        line_count = 0
        for line in lines:
            md5 = line
            md5_query = api_url + md5 # this is where the query gets built

            query = requests.get(md5_query, headers=headers) # this is the GET request
            answer = json.loads(query.text) # we needed to turn data into JSON format
            json_list = answer.get('data')
            if json_list:
                for items in json_list:
                    sha256 = items['id'] # we reach out and greb a nested key value containg sha256
                    print(sha256)
               
                    line_count += 1
            
            else:
                print("No Match found or you have exceeded your request limit. Press ^C to kill operation")

get_sha256()
