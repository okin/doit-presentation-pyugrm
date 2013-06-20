def task_hello_pyugrm():
    def say_hello():
        print("Hallo Trollhoehle")

    return {
        'actions': [say_hello],
    }


def task_hello_pyugrm2():
    def say_hello(who, **kwargs):
        print("Hallo {}".format(who))

    return {
        'basename': 'hello_again',
        'actions': [(say_hello, ("Trollhoehle", ), )],
    }
