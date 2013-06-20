import sys, os;

def someone_likes_semicolons(                             foo  = None            ,\
bar='bar'):


    """Hello; bye."""; print( 'A'<>foo)            #<> is a deprecated form of !=
    return 0;
def func11():
    a=(   1,2, 3,"a"  );
    ####This is a long comment. This should be wrapped to fit within 72 characters.
    x = [a,[100,200,300,9876543210,'This is a long string that goes on and on']]
def func22(): return {True: True}.has_key({'foo': 2}.has_key('foo'));
class UselessClass(   object ):
    def __init__    ( self, bar ):
     #Comments should have a space after the hash.
     if bar : bar+=1;  bar=bar* bar   ; return bar
     else:
                    indentation_in_strings_should_not_be_touched = """
                       hello
world
"""
                    raise ValueError, indentation_in_strings_should_not_be_touched
    def my_method(self):
                                              print(self);