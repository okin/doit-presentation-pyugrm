def task_setup_environment():
    return {
        'actions': ['echo "Done"'],
        'task_dep': ['install_tools']
    }


def task_install_tools():
    return {
        'actions': ['pip install --upgrade flake8']
    }
