def task_show_greeting():
    return {
        'actions': ['cat greeting'],
        'verbosity': 2,
        'file_dep': ['greeting'],
    }
