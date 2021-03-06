##################################################################################
#                                                                                #
# AutoWIG: Automatic Wrapper and Interface Generator                             #
#                                                                                #
# Homepage: http://autowig.readthedocs.io                                        #
#                                                                                #
# Copyright (c) 2016 Pierre Fernique                                             #
#                                                                                #
# This software is distributed under the CeCILL license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (2)                        #
#                                                                                #
##################################################################################

import os
import parse
from path import Path

from .plugin import PluginManager

feedback = PluginManager('autowig.feedback', brief="",
        details="""""")

def parse_errors(err, directory, asg, **kwargs):
    if not isinstance(err, basestring):
        raise TypeError('\'err\' parameter')
    if not isinstance(directory, Path):
        directory = Path(directory)
    variant_dir = kwargs.pop('variant_dir', None)
    if variant_dir:
        variant_dir = directory/variant_dir
    else:
        variant_dir = directory
    src_dir = kwargs.pop('src_dir', None)
    if src_dir:
        src_dir = directory/src_dir
    else:
        src_dir = directory
    indent = kwargs.pop('indent', 0)
    src_dir = str(src_dir.abspath()) + os.sep
    variant_dir = str(variant_dir.relpath(directory))
    if variant_dir == '.':
        variant_dir = ''
    else:
        variant_dir += os.sep
    wrappers = dict()
    for line in err.splitlines():
        parsed = parse.parse(variant_dir+'{filename}:{row}:{column}:{message}', line)
        if parsed:
            try:
                row = int(parsed['row'])
                node = src_dir + parsed['filename']
                if node in asg:
                    if node not in wrappers:
                        wrappers[node] = [row]
                    else:
                        wrappers[node].append(row)
            except:
                pass
    return wrappers