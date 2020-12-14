import json
from data import data_

def convertToJSON():
    with open(r'C:\Users\krask\Вступ до КН\ICS_18_09_2020\Individual_Project\data.json', 'w') as write_file:
        json.dump(data_, write_file)


       