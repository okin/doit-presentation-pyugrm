from doit.tools import InteractiveAction


def task_connect_ssh():
    return {
        'actions': [InteractiveAction('ssh %(username)s@%(host)s')],
        'params': [{'name': 'username',
                    'long': 'username',
                    'short': 'u',
                    'default': 'niko',
                    'help': 'The username to use.'},
                   {'name': 'host',
                    'long': 'server',
                    'short': 's',
                    'default': 'localhost'}
                   ]
    }
