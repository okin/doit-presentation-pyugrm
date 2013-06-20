# -*- coding: utf-8 -*-

import os
from doit.tools import run_once

DOIT_CONFIG = {
    'continue': True
}


def task_run_flake8():
    for filename in os.listdir('.'):
        if filename.endswith('.py'):
            yield {
                'name': filename,
                'actions': ['flake8 {}'.format(filename)],
                'file_dep': [filename],
                'verbosity': 1,
                'task_dep': ['install_flake8']
            }


def task_install_flake8():
    return {
        'actions': ['pip install flake8'],
        'uptodate': [run_once]
    }
