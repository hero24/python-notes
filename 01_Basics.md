## Comments
Comments in Python are denoted by a # at the start of the line. This is inline with most scripting languages, because it allows for usage of shebang.
Shebang is important part of any script as it tells the shell which interpreter to use, which is why most python programs start with a shebang.
```
#!/usr/bin/env python3
```
Because putting a hashtag in front of every line of multiline comments, a lot of programmers use the docstring mechanism for multiline comments.
This involves using `"""` to wrap the comment. For the string to become a docstring it has to be a first statement of a module, function or object,
this docstring gets assigned to `__doc__` variable.

## Coding conventions
Correct coding covnetions for Python are defined in PEP8. https://peps.python.org/pep-0008/ 
PEPs are pythons enhancment proposals, they unlike documentation, provide guidelines on how to use python and new features, they also provide extra details on how certain features work.
If there is one PEP that every python programmer should read, its PEP8.
Python also provides an easter egg, called The Zen of Python, which in form of a poem summarises python conentions. To access it run python interpreter and execute following:
```
import this
```

## Safeguarding scripts

When Python interpreter executes the script it does so in the same way when its executed as a standalone script or a module. In order to stop execution of code when module is imported, we can use the following to wrap the code that should only be executed as standalone code
```
if __name__ == "__main__":
    # Code to be executed
```
Unless script is executed as script the __name__ variable stores the modules name.

## Double underscores
By now you have already seen a few of dunder (double underscore) variables, python uses dunder variables for metadata and variables it uses for proper execution of the code. Dunder methods also exists and are used for special cases such as operator overloading. 
Python doesnt support encapsulation, and as such all functions, methods are public, but it allows by convention to mimic private attributes, by adding a double underscore in front of the variable or method. By convention python programmers however use a single underscore to denote a function, method or attribute that should not be accessed by other programmers or classes.
One of the commonly used dunder variables is __file__ which contains the name and path to the executed file. Its often used in the help/usage function, which is often defined in scripts to tell the user how to use a script.

## Function definitions
Python functions can be defined without type hints or with type hints just like this, but types are not enforced regardless if the typing module is used, but it can be used by third-party software to check the code.
```
def hello(name):
   # Without type hinting
   return "Hello World" + name

def hello(name: str) -> str:
   # With type hinting
   return "Hello World" + name
```

Python has four types of function arguments, which are as follows:
 - positional arguments
 - default arguments
 - non-keyword arguments
 - keyword arguments
and these must follow this order. Furthermore positional arguments are required to pass.
Non-keyword arguments can be passed as a list or tuple, and expanded using a star, similarly Keyword arguments can be passed as a dict and expanded by **.
Lets look at some examples.

```
def func(positional, default="World", *args, **kwargs):
    print(positional, default)
    for arg in args:
        print(arg, end=" ")
    print()
    for key in kwargs:
        print(key, "=", kwargs[key])

func("Hello", default="to", "this", awsome="world")

lst = ["Hey", "whats", "up?"]
kwargs = {"World":"bright"}

func(*lst, **kwargs)

```
In python functions are objects, and as such can be assigned to variables once they are defined, they can also be defined anonymously as lambda functions, or be defined within a function and returned by a function.
```
def double(x):
   def f():
      return x * 2
   return f

square = double(2)
print(square())

triple = lambda x : x * 3
print(triple(5))

lst = [double(2), double(3), double(4)]
for f in lst:
    print(f())
```
