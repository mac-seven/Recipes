#!/usr/bin/python3
# QuickbooksODBCDriver-DownloadHTML.py

import urllib.request, urllib.error, urllib.parse

def getQuickbooksHTML():
    url = 'http://www.cdata.com/download/getfile.aspx?file=demo/RQDG-M/setup.dmg&name=QuickBooks ODBC Driver for Mac'
    url = url.replace(" ", "%20")

    response = urllib.request.urlopen(url)
    webContent = response.read().decode('UTF-8')

    f = open('Quickbooks ODBC Driver.html', 'w')
    f.write(webContent)
    f.close
    
PROCESSOR = getQuickbooksHTML()