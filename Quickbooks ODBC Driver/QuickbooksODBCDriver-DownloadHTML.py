#!/usr/bin/env python

from autopkglib import Processor, ProcessorError
from autopkglib import URLGetter

__all__ = ["GetQuickbooksHTML"]


class GetQuickbooksHTML(Processor):
    """This processor gets the latest version of the download page for the QuickBooks ODBC Drivers for Mac. This is used because AutoPKGr struggles with processing URLs with the 'and' symbol."""

    description = __doc__
    input_variables = {}
    output_variables = {}

    def main(self):
        # Use curl to download a file to disk.
        # Ideal for zipped or archived files that contain information you need, 
        # such as versions or URLs of other downloads
        url = 'http://www.cdata.com/download/getfile.aspx?file=demo/RQDG-M/setup.dmg&name=QuickBooks ODBC Driver for Mac'
        url = url.replace(" ", "%20")
        my_url = self.env["url"]
        filename = os.path.join(self.env["RECIPE_CACHE_DIR"], "Quickbooks ODBC Driver.html")
        self.download_to_file(url, filename)
        # Now we can do something with the file, such as read it, rename it, store it in an output variable, etc.

if __name__ == "__main__":
    PROCESSOR = GetQuickbooksHTML()
    PROCESSOR.execute_shell()