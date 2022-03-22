#!/usr/bin/env python

import urllib.request, urllib.error, urllib.parse

class getQuickbooksHTML(Processor):
    """This processor gets the latest version of the download page for the QuickBooks ODBC Drivers for Mac. This is used because AutoPKGr struggles with processing URLs with the & symbol.
    """
    
    input_variables = {}
    output_variables = {}
    description = __doc__
    
    def main(self):
        self.url = 'http://www.cdata.com/download/getfile.aspx?file=demo/RQDG-M/setup.dmg&name=QuickBooks ODBC Driver for Mac'
        self.url = self.url.replace(" ", "%20")

        self.response = urllib.request.urlopen(self.url)
        self.webContent = response.read().decode('UTF-8')

        self.f = open('Quickbooks ODBC Driver.html', 'w')
        self.f.write(webContent)
        self.f.close
    
if __name__ == "__main__":
    processor = getQuickbooksHTML()
    processor.excecute_shell()