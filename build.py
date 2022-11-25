#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pycharm')

name = "Face Recognition"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on('cv2')
    project.depends_on('numpy')
    project.depends_on('face_recognition')
    project.depends_on('datetime')
