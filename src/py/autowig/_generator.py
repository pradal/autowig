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
# File authors: Pierre Fernique <pfernique@gmail.com> (3)                        #
#                                                                                #
##################################################################################

from .plugin import PluginManager

generator = PluginManager('autowig.generator', brief="AutoWIG back-end plugin_managers",
        details="""AutoWIG back-end plugin_managers are responsible for C/C++ code generation from an Abstract Semantic Graph (ASG) interpretation.

.. seealso:: :class:`autowig.AbstractSemanticGraph` for more details on ASGs""")
