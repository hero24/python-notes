## If-elif-else
For compleness, a simple example of if statement

```
x = 30
if x < 3:
    print("<3")
elif x > 10:
    print("E>")
else:
    print("Will this ever be printed?)
```

Because python is indentation based language it aids clarity, but even though its indentation based language it still supports a single line if statement, when using it in assigment.

```
x = 10
y = 15
result = "x is greater" if x > y else "y is greater"

# nested if statement
z = 20
result = x if x > y else y if y > z else z
``` 

## Comprahensions
Single line if statements are perfect opporunity to introduce list, set and dict comprahensions. Lists in python are ordered collections just like arrays in other languages except they have no upper limit.
Dicts are just like hash maps in other languages, these are unordered and referenced by keys to retrieve their values. Sets in python are unordered and contain single values. Comprahensions in python are simple and elegant ways to create lists, sets and dicts within one line,
they are probably the most commonly used functional programming constructs in python. The basic way to think about comprahension is result for variable in function call.
```
# List comprahension
# doubles numbers 0-10
lst = [x*2 for x in range(10)]
# populates list with None values, in python the convention says that if we dont use the value of a variable directly,
# we call the variable with single underscore
lst = [None for _ in range(5)]

# set comprahension
myset = {x*2 for x in range(15)}

# dict comprahension
mydict = { key: value for key, value in zip("abcde", [1,2,3,4,5])}
```
Comprahensions can also be nested, but that is rarely used, and it makes them difficult to understand, however, sometimes we want to use conditions in comprahensions, as you can guess this is where the single line if statement becomes most useful and is used most commonly.
```
lst = [ x for x in range(10) if x % 2 == 0]
myset = { x if x % 2 == 0 else x * 2 for x in range(10)}
```

## Tuples
Tuples are immutable, ordered collections, that are often used in python to pass arguments. For completness of comprahensions, its worth mentioning that at some point you might come across a construct that looks like a list comprahension but is wrapped in () instead of [].
That construct is called tuple generator, and its power lies in its lazy evaluation, we use it when we want to optimize the programs memory usage. The main difference lies in the fact that when we use list comprahension, list comprahension is generated in that moment in the memory of the program, for tuple generator the actual generation of data is deferred to when the data is actually needed.
There is a drawback to using tuple generations, because they are generated, they cant be indexed like a normal tuple or list.
```
# simple tuples can be indexed but generators cant, and indexing generator would raise TypeError
simple_tuple = (1,2,3)
print(simple_tuple[1])
tpl = ( x for x in range(1000))
```
As mentioned before tuples are used mostly to pass arguments so python has some syntactic sugar to ease manipulation of arguments, you have seen this already on the previous page, but I will dive into this a bit deeper. In python when we are returning multiple values from a function we are essentially creating a tuple. When we are using a zip function to zip two different collections just like I have done in a dict comprahension above, we are essentially creating a tuple, there are certain syntactic and conventional behaviours around them.
Firstly, when using a function that reutrns two values, but we only want to use one value, we denote the second value as underscore. This is called tuple unpacking.
```
_, y = zip([1,2])
simple_tuple = (1,2,3)
_, y, _ = simple_tuple
```
We can also use a * to unpack tuples, or other iterables, this is useful when passing lists or tuples as arguments to functions. Lets look at what a star does when unpacking a tuple, is creates a new iterable, in the example below we are dropping the value, but we could assiging it to some value.
Lastly when we print out y, it will print out an iterable, containing numbers 2-4, however is we print out *y, it will print out each element separately.
```
_, *y = simple_tuple = (1,2,3,4)
first, *rest, last = simple_tuple
print(y)
print(*y)
```
Lastly there are certain functions that become useful when using these constructs, these mainly are 
- zip, which zips two iterables together,
- enumerate, which enumerates a single iterable
- range, which gives a range of numbers, where the args are start, stop, step, with start and step defaulting to 1 when not used
- filter, which filters an iterable, takes in a filter function as an argument or a lambda
```
for x,y in zip([1,2,3], [4,5,6]):
   print(x,y)
for idx, val in enumerate([4,3,2,1]):
   print(idx, val)
for i in range(0,10,2):
   print(i)
for elem in filter(lambda x: x<3, [1,2,3]):
   print(elem)
```
