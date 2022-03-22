from autopkglib.URLGetter import URLGetter

__all__ = ["SampleSharedProcessor"]


class SampleSharedProcessor(Processor):
    """This processor doesn't do anything useful. It is a demonstration of using
    a shared processor via a recipe repo."""

    description = __doc__
    input_variables = {}
    output_variables = {}

    def main(self):
        # Use curl to download a file to disk.
        # Ideal for zipped or archived files that contain information you need, 
        # such as versions or URLs of other downloads
        my_url = 'http://www.cdata.com/download/getfile.aspx?file=demo/RQDG-M/setup.dmg&name=QuickBooks%20ODBC%20Driver%20for%20Mac'
        filename = os.path.join(self.env["RECIPE_CACHE_DIR"], "QuickbooksODBCDriver.html")
        self.download_to_file(url, filename)
        # Now we can do something with the file, such as read it, rename it, store it in an output variable, etc.

if __name__ == "__main__":
    PROCESSOR = SampleSharedProcessor()
    PROCESSOR.execute_shell()
