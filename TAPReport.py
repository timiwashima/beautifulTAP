# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:43:57 2023
Beautify TAP Report Output
@author: tiwashima
"""
import json

file='DRIVE:\\Directory\\to\\the\\file.json'

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
                if k=='os':
                    print('    ' + 'OS: ' + str(v))
                else:
                    print('    ' + str(k.title()) + ': ' + str(v))
        else:
            print('  ' + str(keys.title()) + ': ' + str(report[keys]))

confirmSave=input("\nWould you like to save to a file (y/n)?").lower()
if confirmSave=='y' or 'yes':
    filename='TAPReport.txt'
    with open(filename,'w') as file:
        for forensics in range(0,len(fileData)):
            report=(fileData[forensics])
            file.write('\nReport ' + str(forensics+1))
            for keys in report:
                if keys=='what':
                    what=(report[keys])
                    file.write('\n  What:')
                    for k,v in what.items():
                        file.write('\n    ' + str(k.title()) + ': ' + str(v))
                elif keys=='platforms':
                    platforms=(report[keys])
                    for platformItems in range(0,len(platforms)):
                        platformDict=platforms[platformItems]
                    file.write('\n  Platforms:')
                    for k,v in platformDict.items():
                        if k=='os':
                            file.write('\n    ' + 'OS: ' + str(v))
                        else:
                            file.write('\n    ' + str(k.title()) + ': ' + str(v))
                else:
                    file.write('\n  ' + str(keys.title()) + ': ' + str(report[keys]))
