# Object oriented programming

What is object oriented programming? It's a very good question.

We can start with the fact that "object oriented programming" is a phrase.

We can think of language as a map. Let L be a function that takes a word or a phrase, and outputs an idea.

What is L(object oriented programming)?

Since L is a function, it has to output one idea for every word or phrase it accepts as an argument.

You might say, "We should allow object oriented programming to correspond to many ideas."

We can do that, but would that make our language efficient?

If the word orange corresponds to the colors orange, red, blue, and violet, does that make our language efficient?

What idea does object oriented programming refer to?

# Defining the phrase "object oriented programming"

We can start with the definition of an object. What is an object?

An object is exactly what we know it to be. An object is a person place or thing.

We describe objects using nouns. An object can be a dictionary, a function, a number, a set, a chair, a table.

In computer science we have something called data objects.

In computer science a function is an object. In computer science an integer is an object. 

In computer science a boolean is an object. In computer science a data structure is an object.

And what you realize is... these are different kinds of data objects.

In computer science there are many kinds of data objects.

How do we organize all the different kinds of data objects we have in computer science?

We can organize objects by giving each object a class.

Thus a boolean belongs to the class boolean. The value True or False belongs to the class bool.

Thus an integer belongs to the class integer. The value 10 or 20 belongs to the class int.

Thus a string belongs to the class string. The character sequence "hello world" belongs to the class str.

Thus a dictionary belongs to the class dictionary. (There are many brands of English dictionaries sold in bookstores,
and all of these brands of dictionaries belong to the class dictionary.)

In Python, a dictionary belongs to class dict.

Python has built-in classes that help us organize objects and create objects.

Instead of writing our own class for creating a dictionary, we can use the built-in dict class to create a dictionary.

# The premise of object oriented programming

The beautiful premise of object-oriented programming is that everything is an object, and every object has a class.

We get this idea from mathematics. In mathematics there is a way of thinking about numbers, sets, and functions. 

What do they all have in common? Numbers, sets, and functions are all objects.

A number belongs to class number, a set belongs to class set, and a function belongs to class function.

In mathematics we have different classes (types) of objects: number, set, function, point, line, plane.

In computer science we have different classes (types) of objects: modules, functions, ints, strs, dicts, bools, lists, and more.

The premise of object-oriented programming is that everything is an object, and that every object has a class. 

It is a way of organizing the ideas and technologies that make up computer science.

# How did we come up with this definition of object oriented programming?

We came up with this definition of object oriented programming by referring to the field of mathematics.

In mathematics, we can think of everything as an object. We can think of numbers, sets, and functions as objects.

Just like the objects all around us have behavior, objects in the field of mathematics have behavior.

Just like the objects all around us have attributes, objects in the field of mathematics have attributes.

A computer can have the behavior of playing music, and the attributes of a laptop.

We are using a definition of the word object that harmonizes with its usage in the English language and the field of mathematics.

# Does object oriented programming slow a program down, or cause it to use too much memory?

Object oriented programming does not slow a program down or cause it to use too much memory.

The efficiency of a program is connected to the efficiency of the source code and the efficiency of the compiler or interpreter.

The efficiency of a program is not connected to object oriented programming.

Object oriented programming actually makes it easier to write compilers and interpreters, 
because it organizes different data objects according to their class.

Object oriented programming makes it easier to add new features to a programming language, 
because we can add new features by defining a new class of object.

# Is a Python module an object?

A Python module is in fact an object. We can verify this by opening up the interactive Python environment.

    % python
    >>> type(math)
    <class 'module'>
    >>> type(math.pi)
    <class 'float'>
    >>> type(math.factorial)
    <class 'builtin_function_or_method'>

We can see from the above example how everything in Python is an object. 

A module is an object. A function is an object. A float is an object. 

These objects belong to three different classes: the module class, the function class, and the float class.

# We can use built-in classes, and we can create our own    

In Python we can use built-in classes, and we can create our own classes.

Let's give some examples.

    % python
    >>> import math
    >>> type(math.factorial)
    <class 'builtin_function_or_method'>
    >>> math.factorial(5)
    120
    >>> type(math.pi)
    <class 'float'>
    >>> math.pi
    3.141592653589793

In the examples above, we use some built-in functions and variables: the factorial function and the variable pi.

We can also create our own functions and variables.

    % python
    >>> def inc(n):
    ...     return n+1
    ... 
    >>> type(inc)
    <class 'function'>
    >>> x = inc(5)
    >>> x
    6

In code above, we created a function called inc using the def keyword, and we assigned the variable x to the number returned by the function.

The object inc belongs to class function. 

Now let's create a class. We can create a class using the class keyword.

    % python
    >>> class Person:
    ...     def __init__(self, name, age, occupation, nationality):
    ...             self.name = name
    ...             self.age = age
    ...             self.occupation = occupation
    ...             self.nationality = nationality
    ...     def __str__(self):
    ...             return "Name: %s\nAge: %s\nOccupation: %s\nNationality: %s" %(self.name, self.age, self.occupation, self.nationality)
    ... 
    >>> Mosheh = Person("Mosheh", 50, "Rabbi", "Israel")
    >>> print(Mosheh)
    Name: Mosheh
    Age: 50
    Occupation: Rabbi
    Nationality: Israel
    >>> type(Mosheh)
    <class '__main__.Person'>

We have created a new class of data object called Person. 

We used this data type to create a data object containing information about Moses.

So you see how we can easily create a new data structure by creating a new class of objects.

In this example we created a data structure for storing information about a person.

# How do we store data objects in memory?

Since objects are dynamically allocated, we often store object data on the heap.

It is also a good strategy to store object data on a stack, which we see done in C and assembly.

When we store memory on the stack, it's also dynamic. 

What's the difference between storing data on the stack and storing data on the heap?

The difference is the algorithm for memory allocation. 

When we store data on the stack, we use a different algorithm for memory allocation.

When we store data on the stack, we don't have to bother looking for unused portions of memory.

It takes time to scan the heap and find unused portions of memory.

(It's hard to predict when memory on the heap will be allocated and released.)

When we store data on the stack, we just push an object onto the stack, and it takes no time at all.

Thus storing data on the stack can save time. But we also have to remember the order of every variable on the stack.

If we store the numbers 5, 10, and 15 on the stack, we have to remember the order of the stack in order to retrieve each of the three variables.

    push 5
    push 10
    push 15
    pop eax 
    pop ebx
    pop ecx

In the example above, we have to remember the order of the stack. 

In the example above, eax = 15, ebx = 10, and ecx = 5.

Storing data on the stack saves time, but we have to remember the order of the stack.

These are some reasons why dynamic memory allocation uses both a stack and a heap for data storage and retrieval.

The stack and the heap are simply two different algorithms for memory allocation.

As we have pointed out, data is often allocated dynamically, because it's hard to predict what the data will be at compiletime.

But some data gets allocated statically (once and only once). 

Since classes are static (they can only be defined once) the code in a class only gets loaded into memory once.

What happens when a function gets replaced? For example

    def f(n):
        return n+1

    def clock(f):
        def inner(*args, **kwargs):
            start = time.time()
            ret_value = f(*args, **kwargs)
            end = time.time()
            print("Function %s took %f seconds" %(f.__name__, end-time))
            return ret_value
        return inner
    
    f = clock(f)

We see here an example of a function being replaced.

We are adding a benchmark to function f to measure how much time it takes.

Can we allocate function f statically? We can. But what if we do not know, at compiletime, whether function f will be replaced?

This is one reason why it's good to be flexible about memory allocation.

The code inside a function can often be allocated in the static code segment of virtual memory. But it can also be alocated on the heap in cases like this where the code of a function can be replaced at runtime.

What we're getting at is this:

The stack and the heap are two algorithms for memory allocation.

But in this vast cosmos of planets and stars and galaxies... there are more than two algorithms for memory allocation.

In many programming languages (like C and Python) we can inspect objects and see what they look like in memory.

Here is one way of doing this in Python. We will see how our data object Mosheh is stored.

    >>> import ctypes
    >>> import sys
    >>> ctypes.string_at(id(Mosheh), sys.getsizeof(Mosheh))
    b'\x01\x00\x00\x00\x00\x00\x00\x00(\xd8\xda\x12\xee\x7f\x00\x000\xef\x07h\xee\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00p\x8f\xc4\n\x01\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00'

Now let's see how a string and an integer are stored.

    >>> import ctypes
    >>> import sys
    >>> s = "Hello world!"
    >>> n = 5
    >>> ctypes.string_at(id(s), sys.getsizeof(s))
    b'\x01\x00\x00\x00\x00\x00\x00\x00p\x8f\xc4\n\x01\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\xd8\xbf~\xc8^\xecvM\xe4x\x04h\xee\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Hello world!\x00'
    >>> ctypes.string_at(id(n), sys.getsizeof(n))
    b'\x0f\x02\x00\x00\x00\x00\x00\x00\xa0\xcc\xc3\n\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00'

We can see that the string "Hello world!" is stored at the very end of the byte array.

We can also see that the integer value 5 is stored in the last four bytes of the byte array.

To review this subject of static and dynamic memory allocation, it's important to make one point clear.

When we define a function, we create variables. And there's a lot we do not know at compiletime.

We do not know if the function will even be called. We do not know what data the variables will hold. And we even do not know the size of the data referred to by each variable. (For example, will a string be five characters or five hundred?)

When a function defines a data object, the data object often gets allocated dynamically, on the stack or the heap.

The word dynamic means that it does not happen at the beginning, but it happens over time.

It also means that it does not happen once and only once, it happens a variable number of times.

A lot of data can be allocated statically (at the very beginning, when the program is loaded into memory.)

A lot of data has to be allocated dynamically (during the runtime of the program).

There are strategies and algorithms for allocating a program's memory. 

Sometimes memory gets allocated at the beginning (statically) and sometimes memory gets allocated over time (dynamically).

Python is dynamically typed, and it gives a programmer the ability to replace and redefine functions at runtime.

Thus in Python it is common to allocate memory dynamically.

It is the responsibility of the compiler or interpreter to be efficient with memory requests and memory allocation.

The compiler or interpreter can use many algorithms for memory requests and memory allocation.

The concepts of static memory allocation, dynamic memory allocation, stack memory allocation, and heap memory allocation are really just four algorithms for allocating memory.

We can always refer to mathematics when we talk about concepts in computer science.

In mathematics we have the concepts of a constant and a variable.

Data that is constant can be allocated statically (at the beginning).

Data that is variable can sometimes be allocated statically (if it has a fixed size).

But when data has a variable size, it is often allocated dynamically.

When we are sure we need a data object, we can often allocate the data statically. (It is constant in the sense that we constantly need it at runtime.)

But when we are not sure we need a data object, we often allocate the data dynamically. (It is variable in the sense that we may or may not need it at runtime.)

The computer science terms static and dynamic have a lot in common with the mathematical terms constant and variable.

Is helpful to give a formal definition of static memory and dynamic memory.

Static memory refers to memory blocks that are constant in some way. Either the data does not change, or the size of the data does not change (like the integer five, or a 32-bit integer of any value.)

Dynamic memory refers to memory blocks that change over time. The memory blocks can be claimed and marked as used. The memory blocks can be freed and marked as unused. The memory blocks can store any class of data object.

Static memory refers to memory blocks that are constant in some way, and dynamic memory refers to memory blocks that are not constant, because theoretically they could be used or unused, and theoretically they could hold any class of data object.

This vocabulary for memory allocation probably comes from the C programming language. The C programming language has been very successful and its vocabulary has been widely adopted. 

We can use the concepts of static and dynamic memory to talk about memory allocation. We can use the concepts of a stack and a heap to talk about memory allocation.

But it's important to keep in mind what is really happening. 

A program gives instructions to a procesor.

A program tells a processor to load code and data into memory, so that it can be used when it is needed.

A program stores the addresses of functions and data objects in a symbol table.

A program can organize memory however it wants.

That's what the operating system does... it organizes memory however it wants.

These concepts of static memory, dynamic memory, stacks and heaps are only one way of organizing memory.

When we talk about static memory allocation, dynamic memory allocation, stacks and heaps, we are often using the vocabulary of an operating system, a compiler, or an interpreter.

The operating system is able to modify the memory at any address.

A program is given virtual memory so that it does not modify the memory of other programs.

The compiler or interpreter that translates Python into bytecode or machine code makes decisions about how to organize the virtual memory it is given.

This is because a compiler or interpreter translates source code into a low-level language that allows it to make these decisions.

We see that there are many ways of organizing memory, and there are many ways of organizing virtual memory. 

The familiar algorithms of static memory allocation, dynamic memory allocation, stacks, heaps, and shared libraries are algorithms used by compilers and interpreters and operating systems.

These algorithms do a good job of organizing virtual memory. But there are other strategies and algorithms for organizing virtual memory. We see how C and Python take different approaches to memory allocation. C might make more use of stack memory allocation, and Python might make more use of heap memory allocation.

# Conclusion

Object-oriented programming is a phrase that is often used. But what does it mean?

There are many ways of defining this phrase. It's important to have a clear definition.

We can form a clear definition of "object oriented programming" by drawing from the field of mathematics.

In mathematics, everything is an object. A number is an object, a set is an object, a function is an object.

We can translate this to computer science, and say that, in computer science, everything is an object.

In computer science, everything is an object. A module is an object, a function is an object, an int is an object, a str is an object, a bool is an object, a dict is an object, a list is an object, et cetera.

Every object has a class. 

In mathematics, a number belongs to class number, a set belongs to class set, and a function belongs to class function.

In Python, a module belongs to class module, a function belongs to class function, an integer belongs to class int, a string belongs to class str, a boolean belongs to class bool, a dictionary belongs to class dict, and a list belongs to class list.

Thus everything is an object, and every object has a class.

When we pass an object to a function, what we are really doing is passing a reference to an object.

When we assign a variable to an object, what we are really doing is storing a reference to an object.

When we assign a variable to an object, we are updating our symbol table.

The name of a variable gets stored in the symbol table as a symbol name.

The address of the object referred to by the variable gets stored in the symbol table as a value, next to the symbol name.

When we define a function, we are updating our symbol table.

The name of the function gets stored in the symbol table as a symbol name.

The address of the function gets stored in the symbol table as a value (a memory address).

So behind the scenes we are updating our symbol table.

By creating classes of data objects, we are able to create scopes and namespaces that have a level of privacy between global and local.

Without classes and objects, there is a risk of there being two namespaces, and only two namespaces: global and local.

With classes and objects, we can create many namespaces for code and data.

This is because every object has its own namespace. Every object has its own symbol table.

It is easy to go on and on about this subject, because there is so much to write and think about.

The basic premise of object-oriented programming is that everything is an object, and every object has a class.

When we run the Python interpreter, we create an environment (the Python environment) and we fill it with objects,
like functions, modules, numbers, strings, dictionaries, lists, and so on.

We create a space (the Python runtime environment) and we fill it with objects.

You can see how we have drawn from the physical universe to create an analogy.

When we start the Python runtime environment, we have a space filled with objects. Some objects are already built-in (like the print function and the type function), and some objects we have yet to create.

This is object oriented programming. 

Objects in mathematics and computer science are analogous to objects in the physical universe.

The objects exist in a space. The objects have state and behavior.

When we start the Python runtime environment, we create a space and we fill it with objects. 

You can see how easy it is to go on and on about this subject.

The basic premise of object-oriented programming is that everything is an object and every object has a class.

This understanding of object-oriented programming makes an analogy with the physical universe.

We can use this thinking to create a formal definition for object oriented programming.

Object oriented programming is a paradigm that says, everything is an object, and all objects have a class.