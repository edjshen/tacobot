# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:52:35 2022

@author: edjsh
"""


import os
import json
import requests
import pandas
from pandas import read_csv
import datetime
from datetime import date





csv_filepath = os.path.join(os.path.dirname(__file__), "board bday.csv")

#reads the csv file into products variable
f = read_csv(csv_filepath)
#pandas transforms the data into a list of dictionaries
file = f.to_dict('records')


jsonString = """

 {
    "token": "d279ea60-cf19-11ec-8f1f-f3a7959f03f6",
    "uid": "U03CET7481X",
    "amount": 1,
    "message": "test"
  }

"""  

if __name__ == "__main__":
    i = 0
    while(i<len(file)):
        if(date.today() == file[i]["bday"]):
            url = "https://www.heytaco.chat/api/app.giveTaco"
            jsonString = """

             {
                "token": "d279ea60-cf19-11ec-8f1f-f3a7959f03f6",
                "uid": "{}",
                "amount": 5,
                "message": "Happy Birthday! Here's some tacos to celebrate!!"
              }

            """.format(file[i]["id"])
            
            give = requests.post(url, data = jsonString)
            print(give.status_code)
        i = i+1