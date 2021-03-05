#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Special Processor to deal with a blank space in the redirect URL"""

from autopkglib import Processor, ProcessorError, URLGetter
import subprocess

try:
    from urllib.parse import quote  # For Python 3
except ImportError:
    from urllib2 import quote  # For Python 2

__all__ = ["URLRedirect"]


class URLRedirect(URLGetter):
    """Follows link to final redirect and encodes URL ready for download"""

    description = __doc__
    input_variables = {
        "url": {"required": True, "description": "The URL to follow and encode.",},
    }
    output_variables = {
        "redirect_url": {"description": "The final encoded URL.",},
    }

    def main(self):
        """Follows link to final redirect and encodes URL ready for download"""

        test_var = subprocess.run(['/usr/bin/curl', '-Ls', '-o', '/dev/null', '-w', '%{url_effective}', self.env["url"]], stdout=subprocess.PIPE)
        self.env["redirect_url"]=quote(test_var.stdout.decode("UTF-8"), safe=":/")

if __name__ == "__main__":
    PROCESSOR = URLRedirect()
    PROCESSOR.execute_shell()
