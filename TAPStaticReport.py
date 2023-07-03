# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:30:01 2023
Beautify TAP Static Report Output
@author: tiwashima
"""
import json

fileName='DRIVE:\\Directory\\to\\the\\file.json'

with open(fileName) as f:
    data=json.load(f)

#Print the Raw Data
#print(data)

for keys in data:
    if keys=='id':
        print('ID: ' + str(data[keys]))
    elif keys=='threatId':
        print('Threat ID: ' + str(data[keys]))
    elif keys=='displaySource':
        print('Display Source: ' + str(data[keys]))
    elif keys=='forensicsId':
        print('Forensics ID: ' + str(data[keys]))
    elif keys=='platformName':
        print('Platform Name: ' + str(data[keys]))
    elif keys=='platformOS':
        print('Platform OS: ' + str(data[keys]))
    elif keys=='platformOSVersion':
        print('Platform OS Version: ' + str(data[keys]))
    elif keys=='condemnationSource':
        print('Condemnation Source: ' + str(data[keys]))
    elif keys=='threatStatus':
        print('Threat Status: ' + str(data[keys]))
    elif keys=='isAnalystScan':
        print('Analyst Scan: ' + str(data[keys]))
    elif keys=='createdAt':
        print('Created at: ' + str(data[keys]))
    elif keys=='reports':
        print('Reports:')
        reportDataLists=(data[keys])
        totalReports=len(reportDataLists)
        for report in range (0, totalReports):
            print('  Report ' + str(report+1))
            reportDictionary=reportDataLists[report]
            for reportKeys in reportDictionary:
                if reportKeys=='isAnalystReport':
                    print('    Analyst Report: ' + str(reportDictionary[reportKeys]))
                else:
                    print('    ' + reportKeys.title() + ': ' + str(reportDictionary[reportKeys]))
    elif keys=='url':
        print('URL:')
        urlDict=(data[keys])
        for urlKeys in urlDict:
            if urlKeys=='domainname':
                print('  Domain Name: ' + urlDict[urlKeys])
            elif urlKeys=='fullurl':
                print('  Full URL: ' + urlDict[urlKeys])
            else: 
                print('  ' + urlKeys.title() + ': ' + urlDict[urlKeys])
    else:
        print(keys.title() + ": " + str(data[keys]))
        
confirmSave=input("Would you like to save to a file (y/n)?").lower()
if confirmSave=='y' or 'yes':
    filename='TAPReport.txt'
    with open(filename, 'w') as file:
        for keys in data:
            if keys=='id':
                file.write('ID: ' + str(data[keys]))
            elif keys=='threatId':
                file.write('\nThreat ID: ' + str(data[keys]))
            elif keys=='displaySource':
                file.write('\nDisplay Source: ' + str(data[keys]))
            elif keys=='forensicsId':
                file.write('\nForensics ID: ' + str(data[keys]))
            elif keys=='platformName':
                file.write('\nPlatform Name: ' + str(data[keys]))
            elif keys=='platformOS':
                file.write('\nPlatform OS: ' + str(data[keys]))
            elif keys=='platformOSVersion':
                file.write('\nPlatform OS Version: ' + str(data[keys]))
            elif keys=='condemnationSource':
                file.write('\nCondemnation Source: ' + str(data[keys]))
            elif keys=='threatStatus':
                file.write('\nThreat Status: ' + str(data[keys]))
            elif keys=='isAnalystScan':
                file.write('\nAnalyst Scan: ' + str(data[keys]))
            elif keys=='createdAt':
                file.write('\nCreated at: ' + str(data[keys]))
            elif keys=='reports':
                file.write('\nReports:')
                reportDataLists=(data[keys])
                totalReports=len(reportDataLists)
                for report in range (0, totalReports):
                    file.write('\n  Report ' + str(report+1))
                    reportDictionary=reportDataLists[report]
                    for reportKeys in reportDictionary:
                        if reportKeys=='isAnalystReport':
                            file.write('\n    Analyst Report: ' + str(reportDictionary[reportKeys]))
                        else:
                            file.write('\n    ' + reportKeys.title() + ': ' + str(reportDictionary[reportKeys]))
            elif keys=='url':
                file.write('\nURL:')
                urlDict=(data[keys])
                for urlKeys in urlDict:
                    if urlKeys=='domainname':
                        file.write('\n  Domain Name: ' + urlDict[urlKeys])
                    elif urlKeys=='fullurl':
                        file.write('\n  Full URL: ' + urlDict[urlKeys])
                    else: 
                        file.write('\n  ' + urlKeys.title() + ': ' + urlDict[urlKeys])
