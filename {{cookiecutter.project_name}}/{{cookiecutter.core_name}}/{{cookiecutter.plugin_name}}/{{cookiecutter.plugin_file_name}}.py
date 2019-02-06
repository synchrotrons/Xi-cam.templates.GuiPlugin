from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
from qtpy import uic 
import pyqtgraph as pg

from xicam.core import msg
from xicam.plugins import GUIPlugin, GUILayout

class {{cookiecutter.plugin_name}}(GUIPlugin):
    name = '{{cookiecutter.plugin_name}}'

    # insert GUI plugin generation
{{cookiecutter.plugin_code}}

    def __init__(self, *args, **kwargs):
        # insert auto generation
        self.stages = {{cookiecutter.stages_code}}
        super({{cookiecutter.plugin_name}}, self).__init__(*args,**kwargs)



