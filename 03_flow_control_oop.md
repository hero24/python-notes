## Flow control
Python supports two types of loops, mainly a while loop which works based on a condition and a for loop, that works based on iterators and their conditions. This matters because both loops support an else clause, and the correct way to think about the else part of the loops is that it gets triggered when the condition of the loop turns into false. Lets have a look at an example.

```
while x < 10:
   x += 1
   if x > 5:
       break
else:
    print("the else here will never happen, because x will never be incremented above 5 (x is always lower than 10)")

while x < 10:
   x += 1
   if x > 15:
       break
else:
    print("the else here will always happen, because x will never reach 15 and break will not happen thus the loop finishes with condition x < 10 evaluating to true")
```

This concept is also alive in for loops, here it gets executed when a for loop reaches a moment where an iterator or generator has no more values and raises a StopIteration exception.
```
for i in range(0, 10, 3):
    if i == 9:
        break
else:
    print("loop finished early, else is never executed")

for i in range(0, 8, 3):
    if i == 9:
        break
else:
    print("loop completed, else gets executed")
```
## Generators
While we are here, and before we jump into Object-oriented programming, I will briefly explain a different concept of generator, a one that can be used to writing a bit more complex functions that generate values.
In completly normal scenarios, where we have a function that computes a value, we use `return` statement to exit function and return a value, but python allows us to somewhat "save" the state of a function, and get the next computed value the next time we execute it, by using a `yield` keyword instead of return.
(it saves states by it self, and its only possible because at the end of a day a function is just and object in python).
```
def negative_range(start, stop, step):
    while start > stop:
        yield start
        start -= step

for i in negative_range(10, 5, -1):
    print(i)
```

## Object orientatied programming
Objects are structs that contain data which can represent a state, and methods that can be used to manipulate that data. They have been coming up here and there because in python everything is an object, that said not all objects are the same. Some more primitive types are objects that have only one instance,
but most objects can have multiple instances, hence there are two important operators to compare objects, it is the equality (==) operator, which answers a question do objects have the same value and the `is` keyword, which answers the question is this the same object. Lets see an example.

```
x = []
y = []
print(x is y)
print(x == y)
```

Objects are defined using a `class` keyword, and in python, they can inherit from multiple objects, although it is generally adviced to inherit from at most one object. Internally all objects inherit from `object` object, and similarly exceptions should inherit from Exception at lowest lever of hierarchy, although some built-in exceptions inherit from BaseException.
Its worth to note that, there is also a Warning exception class, which is designed in such a way that python interpreter can be configured at runtime to ignore these and not interrupt a program, but we will look more into exceptions at a later stage.

### Defining a class

Each class, at the least should have a class keyword, and this matters mostly for exceptions but for an object to be somewhat functional, it should be able to save states, and for that to happen it should be initialised. In python we initialise objects using a dunder method called __init__, and unlike most languages it needs to take the instance of the object as a parameter,
by convention pythonistas call this variable self, but as long as the reference is always the same within a given class defnintion, it could even be called cookie, then we take whatever parameters we want. An init function parameter list can finish with *args, **kwargs.

```
class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = self.start

```

So we have defined and object, this object has its state, and now we would like to iterate through it like through list or a range generator. To implement an iterator, the object has to return the iterator itself from the __iter__ dunder method and the next value in __next__ method. It also needs to raise StopIteration exception, when it exhausts values.
The iteration object can be it self, and for simple example like this it is fine. Lets look at an example.

```
    def __next__(self):
        current = self.current
        if current > self.stop:
            raise StopIteration
        self.current += 1
        return current

    def __iter__(self):
        retrun self

myrange = MyRange(10, 15)
for i in myrange:
    print(i)
```

At the current implementation, this range is only usable once, but we can implement a reset method, we might also want to implement a __str__ method for converting the range to string to print it out, (yes python calls this when we try printing object out),
we could compare ranges by overwritting __eq__, __lt__, __gt__ (equal, less than, greater than). Im only going to show __eq__ and string, and leave the rest as an excersise. 

```
    def __str__(self):
        return [x for x in range(self.start, self.stop)].join(" ")

    def __eq__(self, other):
        return self.start == other.start and self.stop == other.stop

```

Lets have a look at inheritance, well written inheritance, does not change the base class but uses the base class as much as possible, lets extend the range with step.
```
class ExtendedRange(MyRange):
   def __init__(self, start, stop, step):
      super().__init__(start, stop)
      self.step = step

    def __next__(self):
        current = self.current
        if current > self.stop:
            raise StopIteration
        self.current += self.step
        return current

    def __str__(self):
        return [x for x in range(self.start, self.stop, self.step)].join(" ")

    def __eq__(self, other):
        return super() == super() and self.step == other.step
```
## Exceptions

Python provides a lot of dunder methods, and their list can be found in python docs, for example there is an overload for not equal to operator or function call to make the object callable.
I have mentioned that class definition can be empty, and that its used for exceptions mostly, for estabilishing the exception hierarchy. Lets have a look at how exceptions work.
```
class MyException(Exception):
    pass

class OtherEx(MyException):
    pass

try:
   raise MyException()
except OtherEx:
   print("Not hit")
except MyException:
   print("Hit)
except:
   print("Not hit, this is generic, and equals to except Exception, and will catch any other exception that is not explicitly caucht above it")
else:
   print("Not hit, this is only hit if there was no exception")
finally:
   print("Hit, this is always hit, regardless if exception has or hasnt occoured")

```

Lets go through a couple things here, the pass keyword exists so that it can be used as a placeholder when implementing code, where syntax requires an indentation but we have no code yet, we can use pass, so that we dont get IndentationError.
Although it was specifically designed for that reason, its commonly used for extending Exception class, it bears no action and surpresses IndentationError. Extending Exception allows us to catch them later, some more sophisticated Exception sometimes overwrite __str__, or implement error codes.

We catch exceptions by using try/except block. We always want to catch the most specific exception, and so, we need to catch OtherEx first, then, less specific otherwise we wouldnt be able to catch the less specific. The exception type is optional, and the keyword itself by default catches Exception class and anything that inherits from it.
Python also provides else block, just like in the for/while loop, and that gets executed if no exception gets called. Lastly the finally block gets always executed.
