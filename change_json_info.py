#!/usr/bin/env python

import os
import json

"""
#CNS LAB#
This is a simple tool used to change information in JSON files
"""

def change_file(json_path, key_to_change, value_to_change):
    with open(json_path, 'r') as f:
        data = json.load(f)
        data[key_to_change] = value_to_change
    

    with open(json_path, 'w') as out_f:
        json.dump(data, out_f, indent=8)
        
    print('updated the file {json_path}')
    
    