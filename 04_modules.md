## Exceptions revisited
The biggest power of python lies in its simplicity, we have already seen how to define and handle exceptions the way exceptions are handled in other traditional programming languages.
Before we get into wrapping up the code into modules, I want to add the last two touches to exceptions, firsly that a well defined module, just like a well defined object hierarchy should include at least one higher level exception that can be used to catch exception thrown by the module. At this point, you can see how it all ties in toghether.
Secondly, a pythonic way to write code is to write it in simple and concise manner, that is easy to read, and thats why python provides another mechanism for exception handling, lets have a look.

## The with block
`With` block wraps code in a context block, and can be used with objects that provide context. When we had a look at objects, we mentioned special dunder methods, which can be used to define special properties of an object, and in this case the two methods that have to be defined in object to use the `with` are __enter__ and __exit__. We will have a look at defining these later, for now lets just note they have to be there to be able to use a with block.
Lets first see how the block is used and how does it differ from tradional approach. Lets look at two ways of opening and printing out the contents of a file.

```
try:
   filehandle = open("myfile.txt", "r")
   print(filehandle.read())
except FileNotFoundError as e:
   print(f"File not found, errorno: {e.errno}")
else:
   filehandle.close()

with open("myfile.txt", "r") as f:
   print(f.read())

```

As we can see its much simpler, nicer and cleaner to read a file, when opening it using the `with` block. But as I mentioned, python requires object to be written correctly in order to be able to use it with this block.
Lets dive a little bit deeper into how thats defined. The __enter__ method must return object that will be assigned as some variable, in the above example, that variable is f. 
The __exit__ method is a bit more complicated, it takes 3 arguments which are, exception type, exception value and a traceback. If there was no exception inside the block, all three values will be None,
otherwise they will contain the exception caught by the block. When exception is passed, we can choose to surpress it or re-raise it depending on the return value of this method.
If we want the with block to surpress the exception, __exit__ method must return True, if we want the exception to be raised, it must return False. Lets have a look at an example.

```
class RangeException(Exception):
   pass

class MyRange:
   def __init__(self, start, stop, step):
       self.start = start
       self.stop = stop
       self.step = step

   def __enter__(self):
       return self.next_value

   def next_value(self):
      while self.start + self.step < self.stop:
          self.start += self.step
          yield self.start
      else:
          raise RangeException

   def __exit__(self, exc_type, exc_value, traceback):
      if exc_type is None:
         # here we can handle normal exit conditions such as closing a file
         pass
      if exc_type == RangeException:
         # in this case we can assume that range terminated correctly unless values were incorrectly assigned by the user
         # and we dont want to raise the error
         return True
      else:
         return False

with MyRange(1, 10, 6) as f:
   for i in r():
      print(i)
```
As we can see this mechanism, still allows for handling exceptions, and dealing with them, just they are deffered into the object itself.

## Python modules
To import a module we use import statement. Its simple we can import specific objects, entire module, all objects or rename objects or modules. Lets have a quick look at example.
```
import random
random.random()

import random as r
r.random()

from random import random
random()

from random import random as r
r()
```
Any standalone python file an be treated as a module. All it takes is an `import filename`. Python first searches for modules in its standard library, then in PYTHONPATH, then in path where python was executed.
This works for small files, but when module gets bigger, it would be nice to have some kind of structure to it. This is achived by using packages.
Packages are defined by creating a folder, with a file __init__.py inside. This file initialises the package and defines its contents. The most important variable of that file is __all__, this is a list, that contains strings, with names of functions, objects and variables we want to make public.
By default if this is not defined, all objects visible in this file would be exported. How are objects visible in the __init__.py file? We import them from other files in the same directory (package). Lets have a look at some example.

Lets imagine, we have a directory called MyRange, and inside we have following files with following contents:
- myrange.py -> MyRange, NegativeRange
- myrangegenerator.py -> MyRangeGenerator
- exceptions.py -> MyRangeException, InvalidRangeError
- __init__.py

Lets have a look at a sample implementation of __init__.py, that creates MyRange module with all the objects defined except MyRange, and NegativeRange name changed to NegRange.
```
from myrange import NegativeRange as NegRange
from myrangegenerator import MyRangeGenerator
from exceptions import *

__all__ = [
   "NegRange",
   "MyRangeGenerator",
   "MyRangeException",
   "InvalidRangeError"
]
```

Lastly, since we already have a module, we might want to make it installable using pip. To do this we need to place setup.py file above our package folder, and inside setup.py we need to place following:
```
from setuptools import setup
setup(
    name="MyRange",
    version="1.0",
    description="Range module",
    packages=["MyRange"],
    author="hero24"
)
```

And thats all!
