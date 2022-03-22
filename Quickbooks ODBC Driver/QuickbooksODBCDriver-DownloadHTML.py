#!/usr/bin/python3
# QuickbooksODBCDriver-DownloadHTML.py

import urllib.request, urllib.error, urllib.parse

class getQuickbooksHTML(Processor):
    """This processor gets the latest version of the download page for the QuickBooks ODBC Drivers for Mac. This is used because AutoPKGr struggles with processing URLs with the & symbol.
    """
    
    input_variables = {}
    output_variables = {}
    description = __doc__
    
    def getQuickbooksHTML():
        url = 'http://www.cdata.com/download/getfile.aspx?file=demo/RQDG-M/setup.dmg&name=QuickBooks ODBC Driver for Mac'
        url = url.replace(" ", "%20")

        response = urllib.request.urlopen(url)
        webContent = response.read().decode('UTF-8')

        f = open('Quickbooks ODBC Driver.html', 'w')
        f.write(webContent)
        f.close
    
if __name__ == "__main__":
    processor = getQuickbooksHTML()
    processor.excecute_shell()