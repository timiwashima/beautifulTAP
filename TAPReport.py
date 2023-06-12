# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:43:57 2023
Beautify TAP Report Output
@author: tiwashima
"""
import json

file='C:\\users\\tiwashima\\downloads\\forensics_reports_2023-06-07T16_27_34Z.json'

with open(file) as f:
    fileData=json.load(f)

#Print the raw data
#print(fileData)

for forensics in range(0,len(fileData)):
    report=(fileData[forensics])
    print('Report ' + str(forensics+1))
    for keys in report:
        if keys=='what':
            what=(report[keys])
            print('  What:')
            for k,v in what.items():
                print('    ' + str(k.title()) + ': ' + str(v))
        elif keys=='platforms':
            platforms=(report[keys])
            for platformItems in range(0,len(platforms)):
                platformDict=platforms[platformItems]
            print('  Platforms:')
            for k,v in platformDict.items():
                print('    ' + str(k.title()) + ': ' + str(v))
        else:
            print('  ' + str(keys.title()) + ': ' + str(report[keys]))