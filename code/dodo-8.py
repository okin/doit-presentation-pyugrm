from doit.tools import InteractiveAction


def task_connect_ssh():
    return {
        'actions': [InteractiveAction('ssh niko@localhost')]
    }
