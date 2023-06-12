# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:30:01 2023
Beautify TAP Static Report Output
@author: tiwashima
"""
import json

fileName='C:\\Users\\tiwashima\\Downloads\\report_2023-06-06T17_33_47Z.json'

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