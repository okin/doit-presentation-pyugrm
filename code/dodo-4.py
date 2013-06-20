def task_hello_pyugrm():
    return {
        'actions': ['echo "Hallo Trollhoehle" > greeting'],
        'targets': ['greeting']
    }


def task_show_greeting():
    return {
        'actions': ['cat greeting'],
        'verbosity': 2,
        'file_dep': ['greeting'],
    }
