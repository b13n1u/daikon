#
#   Copyright [2012] [Patrick Ancillotti]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

# ---------------------
# Imports
# ---------------------

import os
import types
import logging

# ---------------------
# Logging
# ---------------------

formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
logging.basicConfig(level=logging.INFO, formatter=formatter)
log = logging.getLogger('daikon')


# ---------------------
# Classes
# ---------------------

class Display():

    def print_dict(output, level=0):
        for key, value in output.iteritems():
            if isinstance(value, types.DictType):
                Display.print_output(key, level=level)
                Display.print_dict(value, level=level + 1)
            else:
                Display.print_output('%s: %s' % (key, value), level=level)

    def print_output(output, vars=None, level=0):
        if isinstance(output, types.ListType):
            output = os.linesep.join(output)
        elif isinstance(output, types.DictType):
            return Display.print_dict(output, level=level)
        if vars is not None:
            output = output % vars
        prefix = ''
        if level > 0:
            prefix = '\t' * level
        print prefix + output
