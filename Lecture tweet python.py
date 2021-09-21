#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:43:09 2021

@author: Aname
"""

import json

with open('Donnees/corpus_ter_2021_Suicide/always getting bullied/tweet_1236362661383811075.json') as json_data:
    data_dict = json.load(json_data)
    print(data_dict)
    
    
import os
import pandas as pd

path_to_json = 'Donnees/corpus_ter_2021_Suicide/always getting bullied'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
 
jsons_data = pd.DataFrame(columns=['text'])

# we need both the json and an index number so use enumerate()
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

        # here you need to know the layout of your json and each json has to have
        # the same structure (obviously not the structure I have here)
        text = json_text['text']
        city = json_text['user_information']

        # here I push a list of data into a pandas DataFrame at row given by 'index'
        jsons_data.loc[index] = [text]

# now that we have the pertinent json data in our DataFrame let's look at it
print(jsons_data)