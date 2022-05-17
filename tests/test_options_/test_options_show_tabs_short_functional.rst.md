[01mFunctional Programming HOWTO[39;49;00m
[01m================================[39;49;00m

**Version 0.30**

(This is a first draft.  Please send comments/error
reports/suggestions to amk@amk.ca.  This URL is probably not going to
be the final location of the document, so be careful about linking to
it -- you may want to add a disclaimer.)

In this document, we'll take a tour of Python's features suitable for
implementing programs in a functional style.  After an introduction to
the concepts of functional programming, we'll look at language
features such as iterators and generators and relevant library modules
such as [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfunctools[39;49;00m[33m``[39;49;00m.


.. [35mcontents[39;49;00m::

[01mIntroduction[39;49;00m
[01m----------------------[39;49;00m

This section explains the basic concept of functional programming; if
you're just interested in learning about Python language features,
skip to the next section.

Programming languages support decomposing problems in several different
ways:

[34m*[39;49;00m Most programming languages are **procedural**:
  programs are lists of instructions that tell the computer what to
  do with the program's input.
  C, Pascal, and even Unix shells are procedural languages.

[34m*[39;49;00m In **declarative** languages, you write a specification that describes
  the problem to be solved, and the language implementation figures out
  how to perform the computation efficiently.  SQL is the declarative
  language you're most likely to be familiar with; a SQL query describes
  the data set you want to retrieve, and the SQL engine decides whether to
  scan tables or use indexes, which subclauses should be performed first,
  etc.

[34m*[39;49;00m **Object-oriented** programs manipulate  collections of objects.
  Objects have internal state and support methods that query or modify
  this internal state in some way. Smalltalk and Java are
  object-oriented languages.  C++ and Python are languages that
  support object-oriented programming, but don't force the use
  of object-oriented features.

[34m*[39;49;00m **Functional** programming decomposes a problem into a set of functions.
  Ideally, functions only take inputs and produce outputs, and don't have any
  internal state that affects the output produced for a given input.
  Well-known functional languages include the ML family (Standard ML,
  OCaml, and other variants) and Haskell.

The designers of some computer languages have chosen one approach to
programming that's emphasized.  This often makes it difficult to
write programs that use a different approach.  Other languages are
multi-paradigm languages that support several different approaches.  Lisp,
C++, and Python are multi-paradigm; you can write programs or
libraries that are largely procedural, object-oriented, or functional
in all of these languages.  In a large program, different sections
might be written using different approaches; the GUI might be object-oriented
while the processing logic is procedural or functional, for example.

In a functional program, input flows through a set of functions. Each
function operates on its input and produces some output.  Functional
style frowns upon functions with side effects that modify internal
state or make other changes that aren't visible in the function's
return value.  Functions that have no side effects at all are
called **purely functional**.
Avoiding side effects means not using data structures
that get updated as a program runs; every function's output
must only depend on its input.

Some languages are very strict about purity and don't even have
assignment statements such as [33m``[39;49;00m[33ma=3[39;49;00m[33m``[39;49;00m or [33m``[39;49;00m[33mc = a + b[39;49;00m[33m``[39;49;00m, but it's
difficult to avoid all side effects.  Printing to the screen or
writing to a disk file are side effects, for example.  For example, in
Python a [33m``[39;49;00m[33mprint[39;49;00m[33m``[39;49;00m statement or a [33m``[39;49;00m[33mtime.sleep(1)[39;49;00m[33m``[39;49;00m both return no
useful value; they're only called for their side effects of sending
some text to the screen or pausing execution for a second.

Python programs written in functional style usually won't go to the
extreme of avoiding all I/O or all assignments; instead, they'll
provide a functional-appearing interface but will use non-functional
features internally.  For example, the implementation of a function
will still use assignments to local variables, but won't modify global
variables or have other side effects.

Functional programming can be considered the opposite of
object-oriented programming.  Objects are little capsules containing
some internal state along with a collection of method calls that let
you modify this state, and programs consist of making the right set of
state changes.  Functional programming wants to avoid state changes as
much as possible and works with data flowing between functions.  In
Python you might combine the two approaches by writing functions that
take and return instances representing objects in your application
(e-mail messages, transactions, etc.).

Functional design may seem like an odd constraint to work under.  Why
should you avoid objects and side effects?  There are theoretical and
practical advantages to the functional style:

[34m*[39;49;00m Formal provability.
[34m*[39;49;00m Modularity.
[34m*[39;49;00m Composability.
[34m*[39;49;00m Ease of debugging and testing.

[01mFormal provability[39;49;00m
[01m''''''''''''''''''''''[39;49;00m

A theoretical benefit is that it's easier to construct a mathematical proof
that a functional program is correct.

For a long time researchers have been interested in finding ways to
mathematically prove programs correct.  This is different from testing
a program on numerous inputs and concluding that its output is usually
correct, or reading a program's source code and concluding that the
code looks right; the goal is instead a rigorous proof that a program
produces the right result for all possible inputs.

The technique used to prove programs correct is to write down
**invariants**, properties of the input data and of the program's
variables that are always true.  For each line of code, you then show
that if invariants X and Y are true **before** the line is executed,
the slightly different invariants X' and Y' are true **after**
the line is executed.  This continues until you reach the end of the
program, at which point the invariants should match the desired
conditions on the program's output.

Functional programming's avoidance of assignments arose because
assignments are difficult to handle with this technique;
assignments can break invariants that were true before the assignment
without producing any new invariants that can be propagated onward.

Unfortunately, proving programs correct is largely impractical and not
relevant to Python software. Even trivial programs require proofs that
are several pages long; the proof of correctness for a moderately
complicated program would be enormous, and few or none of the programs
you use daily (the Python interpreter, your XML parser, your web
browser) could be proven correct.  Even if you wrote down or generated
a proof, there would then be the question of verifying the proof;
maybe there's an error in it, and you wrongly believe you've proved
the program correct.

[01mModularity[39;49;00m
[01m''''''''''''''''''''''[39;49;00m

A more practical benefit of functional programming is that it forces
you to break apart your problem into small pieces.  Programs are more
modular as a result.  It's easier to specify and write a small
function that does one thing than a large function that performs a
complicated transformation.  Small functions are also easier to read
and to check for errors.


[01mEase of debugging and testing [39;49;00m
[01m''''''''''''''''''''''''''''''''''[39;49;00m

Testing and debugging a functional-style program is easier.

Debugging is simplified because functions are generally small and
clearly specified.  When a program doesn't work, each function is an
interface point where you can check that the data are correct.  You
can look at the intermediate inputs and outputs to quickly isolate the
function that's responsible for a bug.

Testing is easier because each function is a potential subject for a
unit test.  Functions don't depend on system state that needs to be
replicated before running a test; instead you only have to synthesize
the right input and then check that the output matches expectations.



[01mComposability[39;49;00m
[01m''''''''''''''''''''''[39;49;00m

As you work on a functional-style program, you'll write a number of
functions with varying inputs and outputs.  Some of these functions
will be unavoidably specialized to a particular application, but
others will be useful in a wide variety of programs.  For example, a
function that takes a directory path and returns all the XML files in
the directory, or a function that takes a filename and returns its
contents, can be applied to many different situations.

Over time you'll form a personal library of utilities.  Often you'll
assemble new programs by arranging existing functions in a new
configuration and writing a few functions specialized for the current
task.



[01mIterators[39;49;00m
[01m-----------------------[39;49;00m

I'll start by looking at a Python language feature that's an important
foundation for writing functional-style programs: iterators.

An iterator is an object representing a stream of data; this object
returns the data one element at a time.  A Python iterator must
support a method called [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m that takes no arguments and always
returns the next element of the stream.  If there are no more elements
in the stream, [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m must raise the [33m``[39;49;00m[33mStopIteration[39;49;00m[33m``[39;49;00m exception.
Iterators don't have to be finite, though; it's perfectly reasonable
to write an iterator that produces an infinite stream of data.

The built-in [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m function takes an arbitrary object and tries
to return an iterator that will return the object's contents or
elements, raising [33m``[39;49;00m[33mTypeError[39;49;00m[33m``[39;49;00m if the object doesn't support
iteration.  Several of Python's built-in data types support iteration,
the most common being lists and dictionaries.  An object is called
an **iterable** object if you can get an iterator for it.

You can experiment with the iteration interface manually[33m::[39;49;00m

[33m    [39;49;00m[33m>>> L = [1,2,3][39;49;00m
[33m    >>> it = iter(L)[39;49;00m
[33m    >>> print it[39;49;00m
[33m    <iterator object at 0x8116870>[39;49;00m
[33m    >>> it.next()[39;49;00m
[33m    1[39;49;00m
[33m    >>> it.next()[39;49;00m
[33m    2[39;49;00m
[33m    >>> it.next()[39;49;00m
[33m    3[39;49;00m
[33m    >>> it.next()[39;49;00m
[33m    Traceback (most recent call last):[39;49;00m
[33m      File "<stdin>", line 1, in ?[39;49;00m
[33m    StopIteration[39;49;00m
[33m    >>>      [39;49;00m
[33m[39;49;00m
Python expects iterable objects in several different contexts, the
most important being the [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m statement.  In the statement [33m``[39;49;00m[33mfor X in Y[39;49;00m[33m``[39;49;00m,
Y must be an iterator or some object for which [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m can create
an iterator.  These two statements are equivalent[33m::[39;49;00m

[33m        [39;49;00m[33mfor i in iter(obj):[39;49;00m
[33m            print i[39;49;00m
[33m[39;49;00m
[33m        for i in obj:[39;49;00m
[33m            print i[39;49;00m
[33m[39;49;00m
Iterators can be materialized as lists or tuples by using the
[33m``[39;49;00m[33mlist()[39;49;00m[33m``[39;49;00m or [33m``[39;49;00m[33mtuple()[39;49;00m[33m``[39;49;00m constructor functions[33m::[39;49;00m

[33m    [39;49;00m[33m>>> L = [1,2,3][39;49;00m
[33m    >>> iterator = iter(L)[39;49;00m
[33m    >>> t = tuple(iterator)[39;49;00m
[33m    >>> t[39;49;00m
[33m    (1, 2, 3)[39;49;00m
[33m[39;49;00m
Sequence unpacking also supports iterators: if you know an iterator
will return N elements, you can unpack them into an N-tuple[33m::[39;49;00m

[33m    [39;49;00m[33m>>> L = [1,2,3][39;49;00m
[33m    >>> iterator = iter(L)[39;49;00m
[33m    >>> a,b,c = iterator[39;49;00m
[33m    >>> a,b,c[39;49;00m
[33m    (1, 2, 3)[39;49;00m
[33m[39;49;00m
Built-in functions such as [33m``[39;49;00m[33mmax()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mmin()[39;49;00m[33m``[39;49;00m can take a single
iterator argument and will return the largest or smallest element.
The [33m``[39;49;00m[33m"in"[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33m"not in"[39;49;00m[33m``[39;49;00m operators also support iterators: [33m``[39;49;00m[33mX in[39;49;00m
[33miterator[39;49;00m[33m``[39;49;00m is true if X is found in the stream returned by the
iterator.  You'll run into obvious problems if the iterator is
infinite; [33m``[39;49;00m[33mmax()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mmin()[39;49;00m[33m``[39;49;00m, and [33m``[39;49;00m[33m"not in"[39;49;00m[33m``[39;49;00m will never return, and
if the element X never appears in the stream, the [33m``[39;49;00m[33m"in"[39;49;00m[33m``[39;49;00m operator
won't return either.

Note that you can only go forward in an iterator; there's no way to
get the previous element, reset the iterator, or make a copy of it.
Iterator objects can optionally provide these additional capabilities,
but the iterator protocol only specifies the [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m method.
Functions may therefore consume all of the iterator's output, and if
you need to do something different with the same stream, you'll have
to create a new iterator.



[01mData Types That Support Iterators[39;49;00m
[01m'''''''''''''''''''''''''''''''''''[39;49;00m

We've already seen how lists and tuples support iterators.  In fact,
any Python sequence type, such as strings, will automatically support
creation of an iterator.

Calling [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m on a dictionary returns an iterator that will loop
over the dictionary's keys[33m::[39;49;00m

[33m    [39;49;00m[33m>>> m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,[39;49;00m
[33m    ...      'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}[39;49;00m
[33m    >>> for key in m:[39;49;00m
[33m    ...     print key, m[key][39;49;00m
[33m    Mar 3[39;49;00m
[33m    Feb 2[39;49;00m
[33m    Aug 8[39;49;00m
[33m    Sep 9[39;49;00m
[33m    May 5[39;49;00m
[33m    Jun 6[39;49;00m
[33m    Jul 7[39;49;00m
[33m    Jan 1[39;49;00m
[33m    Apr 4[39;49;00m
[33m    Nov 11[39;49;00m
[33m    Dec 12[39;49;00m
[33m    Oct 10[39;49;00m
[33m[39;49;00m
Note that the order is essentially random, because it's based on the
hash ordering of the objects in the dictionary.

Applying [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m to a dictionary always loops over the keys, but
dictionaries have methods that return other iterators.  If you want to
iterate over keys, values, or key/value pairs, you can explicitly call
the [33m``[39;49;00m[33miterkeys()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mitervalues()[39;49;00m[33m``[39;49;00m, or [33m``[39;49;00m[33miteritems()[39;49;00m[33m``[39;49;00m methods to
get an appropriate iterator.

The [33m``[39;49;00m[33mdict()[39;49;00m[33m``[39;49;00m constructor can accept an iterator that returns a
finite stream of [33m``[39;49;00m[33m(key, value)[39;49;00m[33m``[39;49;00m tuples[33m::[39;49;00m

[33m    [39;49;00m[33m>>> L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')][39;49;00m
[33m    >>> dict(iter(L))[39;49;00m
[33m    {'Italy': 'Rome', 'US': 'Washington DC', 'France': 'Paris'}[39;49;00m
[33m[39;49;00m
Files also support iteration by calling the [33m``[39;49;00m[33mreadline()[39;49;00m[33m``[39;49;00m
method until there are no more lines in the file.  This means you can
read each line of a file like this[33m::[39;49;00m

[33m    [39;49;00m[33mfor line in file:[39;49;00m
[33m        # do something for each line[39;49;00m
[33m        ...[39;49;00m
[33m[39;49;00m
Sets can take their contents from an iterable and let you iterate over
the set's elements[33m::[39;49;00m

[33m    [39;49;00m[33mS = set((2, 3, 5, 7, 11, 13))[39;49;00m
[33m    for i in S:[39;49;00m
[33m        print i[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[01mGenerator expressions and list comprehensions[39;49;00m
[01m----------------------------------------------------[39;49;00m

Two common operations on an iterator's output are 1) performing some
operation for every element, 2) selecting a subset of elements that
meet some condition.  For example, given a list of strings, you might
want to strip off trailing whitespace from each line or extract all
the strings containing a given substring.

List comprehensions and generator expressions (short form: "listcomps"
and "genexps") are a concise notation for such operations, borrowed
from the functional programming language Haskell
(http://www.haskell.org).  You can strip all the whitespace from a
stream of strings with the following code[33m::[39;49;00m

[33m        [39;49;00m[33mline_list = ['  line 1\n', 'line 2  \n', ...][39;49;00m
[33m[39;49;00m
[33m        # Generator expression -- returns iterator[39;49;00m
[33m        stripped_iter = (line.strip() for line in line_list)[39;49;00m
[33m[39;49;00m
[33m        # List comprehension -- returns list[39;49;00m
[33m        stripped_list = [line.strip() for line in line_list][39;49;00m
[33m[39;49;00m
You can select only certain elements by adding an [33m``[39;49;00m[33m"if"[39;49;00m[33m``[39;49;00m condition[33m::[39;49;00m

[33m        [39;49;00m[33mstripped_list = [line.strip() for line in line_list[39;49;00m
[33m                         if line != ""][39;49;00m
[33m[39;49;00m
With a list comprehension, you get back a Python list;
[33m``[39;49;00m[33mstripped_list[39;49;00m[33m``[39;49;00m is a list containing the resulting lines, not an
iterator.  Generator expressions return an iterator that computes the
values as necessary, not needing to materialize all the values at
once.  This means that list comprehensions aren't useful if you're
working with iterators that return an infinite stream or a very large
amount of data.  Generator expressions are preferable in these
situations.

Generator expressions are surrounded by parentheses ("()") and list
comprehensions are surrounded by square brackets ("[]").  Generator
expressions have the form[33m::[39;49;00m

[33m    [39;49;00m[33m( expression for expr in sequence1 [39;49;00m
[33m                 if condition1[39;49;00m
[33m                 for expr2 in sequence2[39;49;00m
[33m                 if condition2[39;49;00m
[33m                 for expr3 in sequence3 ...[39;49;00m
[33m                 if condition3[39;49;00m
[33m                 for exprN in sequenceN[39;49;00m
[33m                 if conditionN )[39;49;00m
[33m[39;49;00m
Again, for a list comprehension only the outside brackets are
different (square brackets instead of parentheses).

The elements of the generated output will be the successive values of
[33m``[39;49;00m[33mexpression[39;49;00m[33m``[39;49;00m.  The [33m``[39;49;00m[33mif[39;49;00m[33m``[39;49;00m clauses are all optional; if present,
[33m``[39;49;00m[33mexpression[39;49;00m[33m``[39;49;00m is only evaluated and added to the result when
[33m``[39;49;00m[33mcondition[39;49;00m[33m``[39;49;00m is true.

Generator expressions always have to be written inside parentheses,
but the parentheses signalling a function call also count.  If you
want to create an iterator that will be immediately passed to a
function you can write[33m::[39;49;00m

[33m        [39;49;00m[33mobj_total = sum(obj.count for obj in list_all_objects())[39;49;00m
[33m[39;49;00m
The [33m``[39;49;00m[33mfor...in[39;49;00m[33m``[39;49;00m clauses contain the sequences to be iterated over.
The sequences do not have to be the same length, because they are
iterated over from left to right, **not** in parallel.  For each
element in [33m``[39;49;00m[33msequence1[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33msequence2[39;49;00m[33m``[39;49;00m is looped over from the
beginning.  [33m``[39;49;00m[33msequence3[39;49;00m[33m``[39;49;00m  is then looped over for each
resulting pair of elements from [33m``[39;49;00m[33msequence1[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33msequence2[39;49;00m[33m``[39;49;00m.

To put it another way, a list comprehension or generator expression is
equivalent to the following Python code[33m::[39;49;00m

[33m    [39;49;00m[33mfor expr1 in sequence1:[39;49;00m
[33m        if not (condition1):[39;49;00m
[33m            continue   # Skip this element[39;49;00m
[33m        for expr2 in sequence2:[39;49;00m
[33m            if not (condition2):[39;49;00m
[33m                continue    # Skip this element[39;49;00m
[33m            ...[39;49;00m
[33m            for exprN in sequenceN:[39;49;00m
[33m                 if not (conditionN):[39;49;00m
[33m                     continue   # Skip this element[39;49;00m
[33m[39;49;00m
[33m                 # Output the value of [39;49;00m
[33m                 # the expression.[39;49;00m
[33m[39;49;00m
This means that when there are multiple [33m``[39;49;00m[33mfor...in[39;49;00m[33m``[39;49;00m clauses but no
[33m``[39;49;00m[33mif[39;49;00m[33m``[39;49;00m clauses, the length of the resulting output will be equal to
the product of the lengths of all the sequences.  If you have two
lists of length 3, the output list is 9 elements long[33m::[39;49;00m

[33m    [39;49;00m[33mseq1 = 'abc'[39;49;00m
[33m    seq2 = (1,2,3)[39;49;00m
[33m    >>> [ (x,y) for x in seq1 for y in seq2][39;49;00m
[33m    [('a', 1), ('a', 2), ('a', 3), [39;49;00m
[33m     ('b', 1), ('b', 2), ('b', 3), [39;49;00m
[33m     ('c', 1), ('c', 2), ('c', 3)][39;49;00m
[33m[39;49;00m
To avoid introducing an ambiguity into Python's grammar, if
[33m``[39;49;00m[33mexpression[39;49;00m[33m``[39;49;00m is creating a tuple, it must be surrounded with
parentheses.  The first list comprehension below is a syntax error,
while the second one is correct[33m::[39;49;00m

[33m    [39;49;00m[33m# Syntax error[39;49;00m
[33m    [ x,y for x in seq1 for y in seq2][39;49;00m
[33m    # Correct[39;49;00m
[33m    [ (x,y) for x in seq1 for y in seq2][39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[01mGenerators[39;49;00m
[01m-----------------------[39;49;00m

Generators are a special class of functions that simplify the task of
writing iterators.  Regular functions compute a value and return it,
but generators return an iterator that returns a stream of values.

You're doubtless familiar with how regular function calls work in
Python or C.  When you call a function, it gets a private namespace
where its local variables are created.  When the function reaches a
[33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m statement, the local variables are destroyed and the
value is returned to the caller.  A later call to the same function
creates a new private namespace and a fresh set of local
variables. But, what if the local variables weren't thrown away on
exiting a function?  What if you could later resume the function where
it left off?  This is what generators provide; they can be thought of
as resumable functions.

Here's the simplest example of a generator function[33m::[39;49;00m

[33m    [39;49;00m[33mdef generate_ints(N):[39;49;00m
[33m        for i in range(N):[39;49;00m
[33m            yield i[39;49;00m
[33m[39;49;00m
Any function containing a [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m keyword is a generator function;
this is detected by Python's bytecode compiler which compiles the
function specially as a result.

When you call a generator function, it doesn't return a single value;
instead it returns a generator object that supports the iterator
protocol.  On executing the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m expression, the generator
outputs the value of [33m``[39;49;00m[33mi[39;49;00m[33m``[39;49;00m, similar to a [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m
statement.  The big difference between [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m and a
[33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m statement is that on reaching a [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m the
generator's state of execution is suspended and local variables are
preserved.  On the next call to the generator's [33m``[39;49;00m[33m.next()[39;49;00m[33m``[39;49;00m method,
the function will resume executing.

Here's a sample usage of the [33m``[39;49;00m[33mgenerate_ints()[39;49;00m[33m``[39;49;00m generator[33m::[39;49;00m

[33m    [39;49;00m[33m>>> gen = generate_ints(3)[39;49;00m
[33m    >>> gen[39;49;00m
[33m    <generator object at 0x8117f90>[39;49;00m
[33m    >>> gen.next()[39;49;00m
[33m    0[39;49;00m
[33m    >>> gen.next()[39;49;00m
[33m    1[39;49;00m
[33m    >>> gen.next()[39;49;00m
[33m    2[39;49;00m
[33m    >>> gen.next()[39;49;00m
[33m    Traceback (most recent call last):[39;49;00m
[33m      File "stdin", line 1, in ?[39;49;00m
[33m      File "stdin", line 2, in generate_ints[39;49;00m
[33m    StopIteration[39;49;00m
[33m[39;49;00m
You could equally write [33m``[39;49;00m[33mfor i in generate_ints(5)[39;49;00m[33m``[39;49;00m, or
[33m``[39;49;00m[33ma,b,c = generate_ints(3)[39;49;00m[33m``[39;49;00m.

Inside a generator function, the [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m statement can only be used
without a value, and signals the end of the procession of values;
after executing a [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m the generator cannot return any further
values.  [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m with a value, such as [33m``[39;49;00m[33mreturn 5[39;49;00m[33m``[39;49;00m, is a syntax
error inside a generator function.  The end of the generator's results
can also be indicated by raising [33m``[39;49;00m[33mStopIteration[39;49;00m[33m``[39;49;00m manually, or by
just letting the flow of execution fall off the bottom of the
function.

You could achieve the effect of generators manually by writing your
own class and storing all the local variables of the generator as
instance variables.  For example, returning a list of integers could
be done by setting [33m``[39;49;00m[33mself.count[39;49;00m[33m``[39;49;00m to 0, and having the
[33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m method increment [33m``[39;49;00m[33mself.count[39;49;00m[33m``[39;49;00m and return it.
However, for a moderately complicated generator, writing a
corresponding class can be much messier.

The test suite included with Python's library, [33m``[39;49;00m[33mtest_generators.py[39;49;00m[33m``[39;49;00m,
contains a number of more interesting examples.  Here's one generator
that implements an in-order traversal of a tree using generators
recursively.

[33m::[39;49;00m

[33m    [39;49;00m[33m# A recursive generator that generates Tree leaves in in-order.[39;49;00m
[33m    def inorder(t):[39;49;00m
[33m        if t:[39;49;00m
[33m            for x in inorder(t.left):[39;49;00m
[33m                yield x[39;49;00m
[33m[39;49;00m
[33m            yield t.label[39;49;00m
[33m[39;49;00m
[33m            for x in inorder(t.right):[39;49;00m
[33m                yield x[39;49;00m
[33m[39;49;00m
Two other examples in [33m``[39;49;00m[33mtest_generators.py[39;49;00m[33m``[39;49;00m produce
solutions for the N-Queens problem (placing N queens on an NxN
chess board so that no queen threatens another) and the Knight's Tour
(finding a route that takes a knight to every square of an NxN chessboard
without visiting any square twice).



[01mPassing values into a generator[39;49;00m
[01m''''''''''''''''''''''''''''''''''''''''''''''[39;49;00m

In Python 2.4 and earlier, generators only produced output.  Once a
generator's code was invoked to create an iterator, there was no way to
pass any new information into the function when its execution is
resumed.  You could hack together this ability by making the
generator look at a global variable or by passing in some mutable object
that callers then modify, but these approaches are messy.

In Python 2.5 there's a simple way to pass values into a generator.
[33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m became an expression, returning a value that can be assigned
to a variable or otherwise operated on[33m::[39;49;00m

[33m    [39;49;00m[33mval = (yield i)[39;49;00m
[33m[39;49;00m
I recommend that you **always** put parentheses around a [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m
expression when you're doing something with the returned value, as in
the above example.  The parentheses aren't always necessary, but it's
easier to always add them instead of having to remember when they're
needed.

(PEP 342 explains the exact rules, which are that a
[33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m-expression must always be parenthesized except when it
occurs at the top-level expression on the right-hand side of an
assignment.  This means you can write [33m``[39;49;00m[33mval = yield i[39;49;00m[33m``[39;49;00m but have to
use parentheses when there's an operation, as in [33m``[39;49;00m[33mval = (yield i)[39;49;00m
[33m+ 12[39;49;00m[33m``[39;49;00m.)

Values are sent into a generator by calling its
[33m``[39;49;00m[33msend(value)[39;49;00m[33m``[39;49;00m method.  This method resumes the
generator's code and the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m expression returns the specified
value.  If the regular [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m method is called, the
[33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m returns [33m``[39;49;00m[33mNone[39;49;00m[33m``[39;49;00m.

Here's a simple counter that increments by 1 and allows changing the
value of the internal counter.

[33m::[39;49;00m

[33m    [39;49;00m[33mdef counter (maximum):[39;49;00m
[33m        i = 0[39;49;00m
[33m        while i < maximum:[39;49;00m
[33m            val = (yield i)[39;49;00m
[33m            # If value provided, change counter[39;49;00m
[33m            if val is not None:[39;49;00m
[33m                i = val[39;49;00m
[33m            else:[39;49;00m
[33m                i += 1[39;49;00m
[33m[39;49;00m
And here's an example of changing the counter:

    >>> it = counter(10)
    >>> print it.next()
    0
    >>> print it.next()
    1
    >>> print it.send(8)
    8
    >>> print it.next()
    9
    >>> print it.next()
    Traceback (most recent call last):
      File [33m``[39;49;00m[33mt.py'', line 15, in ?[39;49;00m
[33m        print it.next()[39;49;00m
[33m    StopIteration[39;49;00m
[33m[39;49;00m
[33mBecause [39;49;00m[33m`[39;49;00m[33m`[39;49;00m[33myield[39;49;00m[33m``[39;49;00m will often be returning [33m``[39;49;00m[33mNone[39;49;00m[33m``[39;49;00m, you
should always check for this case.  Don't just use its value in
expressions unless you're sure that the [33m``[39;49;00m[33msend()[39;49;00m[33m``[39;49;00m method
will be the only method used resume your generator function.

In addition to [33m``[39;49;00m[33msend()[39;49;00m[33m``[39;49;00m, there are two other new methods on
generators:

[34m*[39;49;00m [33m``[39;49;00m[33mthrow(type, value=None, traceback=None)[39;49;00m[33m``[39;49;00m is used to raise an exception inside the
  generator; the exception is raised by the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m expression
  where the generator's execution is paused.

[34m*[39;49;00m [33m``[39;49;00m[33mclose()[39;49;00m[33m``[39;49;00m raises a [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m
  exception inside the generator to terminate the iteration.
  On receiving this
  exception, the generator's code must either raise
  [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m or [33m``[39;49;00m[33mStopIteration[39;49;00m[33m``[39;49;00m; catching the
  exception and doing anything else is illegal and will trigger
  a [33m``[39;49;00m[33mRuntimeError[39;49;00m[33m``[39;49;00m.  [33m``[39;49;00m[33mclose()[39;49;00m[33m``[39;49;00m will also be called by
  Python's garbage collector when the generator is garbage-collected.

  If you need to run cleanup code when a [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m occurs,
  I suggest using a [33m``[39;49;00m[33mtry: ... finally:[39;49;00m[33m``[39;49;00m suite instead of
  catching [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m.

The cumulative effect of these changes is to turn generators from
one-way producers of information into both producers and consumers.

Generators also become **coroutines**, a more generalized form of
subroutines.  Subroutines are entered at one point and exited at
another point (the top of the function, and a [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m
statement), but coroutines can be entered, exited, and resumed at
many different points (the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m statements).


[01mBuilt-in functions[39;49;00m
[01m----------------------------------------------[39;49;00m

Let's look in more detail at built-in functions often used with iterators.

Two Python's built-in functions, [33m``[39;49;00m[33mmap()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfilter()[39;49;00m[33m``[39;49;00m, are
somewhat obsolete; they duplicate the features of list comprehensions
but return actual lists instead of iterators.

[33m``[39;49;00m[33mmap(f, iterA, iterB, ...)[39;49;00m[33m``[39;49;00m returns a list containing [33m``[39;49;00m[33mf(iterA[0],[39;49;00m
[33miterB[0]), f(iterA[1], iterB[1]), f(iterA[2], iterB[2]), ...[39;49;00m[33m``[39;49;00m.

[33m::[39;49;00m

[33m    [39;49;00m[33mdef upper(s):[39;49;00m
[33m        return s.upper()[39;49;00m
[33m    map(upper, ['sentence', 'fragment']) =>[39;49;00m
[33m      ['SENTENCE', 'FRAGMENT'][39;49;00m
[33m[39;49;00m
[33m    [upper(s) for s in ['sentence', 'fragment']] =>[39;49;00m
[33m      ['SENTENCE', 'FRAGMENT'][39;49;00m
[33m[39;49;00m
As shown above, you can achieve the same effect with a list
comprehension.  The [33m``[39;49;00m[33mitertools.imap()[39;49;00m[33m``[39;49;00m function does the same thing
but can handle infinite iterators; it'll be discussed later, in the section on
the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module.

[33m``[39;49;00m[33mfilter(predicate, iter)[39;49;00m[33m``[39;49;00m returns a list
that contains all the sequence elements that meet a certain condition,
and is similarly duplicated by list comprehensions.
A **predicate** is a function that returns the truth value of
some condition; for use with [33m``[39;49;00m[33mfilter()[39;49;00m[33m``[39;49;00m, the predicate must take a
single value.

[33m::[39;49;00m

[33m    [39;49;00m[33mdef is_even(x):[39;49;00m
[33m        return (x % 2) == 0[39;49;00m
[33m[39;49;00m
[33m    filter(is_even, range(10)) =>[39;49;00m
[33m      [0, 2, 4, 6, 8][39;49;00m
[33m[39;49;00m
This can also be written as a list comprehension[33m::[39;49;00m

[33m    [39;49;00m[33m>>> [x for x in range(10) if is_even(x)][39;49;00m
[33m    [0, 2, 4, 6, 8][39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mfilter()[39;49;00m[33m``[39;49;00m also has a counterpart in the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module,
[33m``[39;49;00m[33mitertools.ifilter()[39;49;00m[33m``[39;49;00m, that returns an iterator and
can therefore handle infinite sequences just as [33m``[39;49;00m[33mitertools.imap()[39;49;00m[33m``[39;49;00m can.

[33m``[39;49;00m[33mreduce(func, iter, [initial_value])[39;49;00m[33m``[39;49;00m doesn't have a counterpart in
the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module because it cumulatively performs an operation
on all the iterable's elements and therefore can't be applied to
infinite iterables.  [33m``[39;49;00m[33mfunc[39;49;00m[33m``[39;49;00m must be a function that takes two elements
and returns a single value.  [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m takes the first two elements
A and B returned by the iterator and calculates [33m``[39;49;00m[33mfunc(A, B)[39;49;00m[33m``[39;49;00m.  It
then requests the third element, C, calculates [33m``[39;49;00m[33mfunc(func(A, B),[39;49;00m
[33mC)[39;49;00m[33m``[39;49;00m, combines this result with the fourth element returned, and
continues until the iterable is exhausted.  If the iterable returns no
values at all, a [33m``[39;49;00m[33mTypeError[39;49;00m[33m``[39;49;00m exception is raised.  If the initial
value is supplied, it's used as a starting point and
[33m``[39;49;00m[33mfunc(initial_value, A)[39;49;00m[33m``[39;49;00m is the first calculation.

[33m::[39;49;00m

[33m    [39;49;00m[33mimport operator[39;49;00m
[33m    reduce(operator.concat, ['A', 'BB', 'C']) =>[39;49;00m
[33m      'ABBC'[39;49;00m
[33m    reduce(operator.concat, []) =>[39;49;00m
[33m      TypeError: reduce() of empty sequence with no initial value[39;49;00m
[33m    reduce(operator.mul, [1,2,3], 1) =>[39;49;00m
[33m      6[39;49;00m
[33m    reduce(operator.mul, [], 1) =>[39;49;00m
[33m      1[39;49;00m
[33m[39;49;00m
If you use [33m``[39;49;00m[33moperator.add[39;49;00m[33m``[39;49;00m with [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m, you'll add up all the
elements of the iterable.  This case is so common that there's a special
built-in called [33m``[39;49;00m[33msum()[39;49;00m[33m``[39;49;00m to compute it[33m::[39;49;00m

[33m    [39;49;00m[33mreduce(operator.add, [1,2,3,4], 0) =>[39;49;00m
[33m      10[39;49;00m
[33m    sum([1,2,3,4]) =>[39;49;00m
[33m      10[39;49;00m
[33m    sum([]) =>[39;49;00m
[33m      0[39;49;00m
[33m[39;49;00m
For many uses of [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m, though, it can be clearer to just write
the obvious [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m loop[33m::[39;49;00m

[33m    [39;49;00m[33m# Instead of:[39;49;00m
[33m    product = reduce(operator.mul, [1,2,3], 1)[39;49;00m
[33m[39;49;00m
[33m    # You can write:[39;49;00m
[33m    product = 1[39;49;00m
[33m    for i in [1,2,3]:[39;49;00m
[33m        product *= i[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33menumerate(iter)[39;49;00m[33m``[39;49;00m counts off the elements in the iterable, returning
2-tuples containing the count and each element.

[33m::[39;49;00m

[33m    [39;49;00m[33menumerate(['subject', 'verb', 'object']) =>[39;49;00m
[33m      (0, 'subject'), (1, 'verb'), (2, 'object')[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33menumerate()[39;49;00m[33m``[39;49;00m is often used when looping through a list
and recording the indexes at which certain conditions are met[33m::[39;49;00m

[33m    [39;49;00m[33mf = open('data.txt', 'r')[39;49;00m
[33m    for i, line in enumerate(f):[39;49;00m
[33m        if line.strip() == '':[39;49;00m
[33m            print 'Blank line at line #%i' % i[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33msorted(iterable, [cmp=None], [key=None], [reverse=False)[39;49;00m[33m``[39;49;00m
collects all the elements of the iterable into a list, sorts
the list, and returns the sorted result.  The [33m``[39;49;00m[33mcmp[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mkey[39;49;00m[33m``[39;49;00m,
and [33m``[39;49;00m[33mreverse[39;49;00m[33m``[39;49;00m arguments are passed through to the
constructed list's [33m``[39;49;00m[33m.sort()[39;49;00m[33m``[39;49;00m method.

[33m::[39;49;00m

[33m    [39;49;00m[33mimport random[39;49;00m
[33m    # Generate 8 random numbers between [0, 10000)[39;49;00m
[33m    rand_list = random.sample(range(10000), 8)[39;49;00m
[33m    rand_list =>[39;49;00m
[33m      [769, 7953, 9828, 6431, 8442, 9878, 6213, 2207][39;49;00m
[33m    sorted(rand_list) =>[39;49;00m
[33m      [769, 2207, 6213, 6431, 7953, 8442, 9828, 9878][39;49;00m
[33m    sorted(rand_list, reverse=True) =>[39;49;00m
[33m      [9878, 9828, 8442, 7953, 6431, 6213, 2207, 769][39;49;00m
[33m[39;49;00m
(For a more detailed discussion of sorting, see the Sorting mini-HOWTO
in the Python wiki at http://wiki.python.org/moin/HowTo/Sorting.)

The [33m``[39;49;00m[33many(iter)[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mall(iter)[39;49;00m[33m``[39;49;00m built-ins look at
the truth values of an iterable's contents.  [33m``[39;49;00m[33many()[39;49;00m[33m``[39;49;00m returns
True if any element in the iterable is a true value, and [33m``[39;49;00m[33mall()[39;49;00m[33m``[39;49;00m
returns True if all of the elements are true values[33m::[39;49;00m

[33m    [39;49;00m[33many([0,1,0]) =>[39;49;00m
[33m      True[39;49;00m
[33m    any([0,0,0]) =>[39;49;00m
[33m      False[39;49;00m
[33m    any([1,1,1]) =>[39;49;00m
[33m      True[39;49;00m
[33m    all([0,1,0]) =>[39;49;00m
[33m      False[39;49;00m
[33m    all([0,0,0]) => [39;49;00m
[33m      False[39;49;00m
[33m    all([1,1,1]) =>[39;49;00m
[33m      True[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[01mSmall functions and the lambda statement[39;49;00m
[01m----------------------------------------------[39;49;00m

When writing functional-style programs, you'll often need little
functions that act as predicates or that combine elements in some way.

If there's a Python built-in or a module function that's suitable, you
don't need to define a new function at all[33m::[39;49;00m

[33m        [39;49;00m[33mstripped_lines = [line.strip() for line in lines][39;49;00m
[33m        existing_files = filter(os.path.exists, file_list)[39;49;00m
[33m[39;49;00m
If the function you need doesn't exist, you need to write it.  One way
to write small functions is to use the [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m statement.  [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m
takes a number of parameters and an expression combining these parameters,
and creates a small function that returns the value of the expression[33m::[39;49;00m

[33m        [39;49;00m[33mlowercase = lambda x: x.lower()[39;49;00m
[33m[39;49;00m
[33m        print_assign = lambda name, value: name + '=' + str(value)[39;49;00m
[33m[39;49;00m
[33m        adder = lambda x, y: x+y[39;49;00m
[33m[39;49;00m
An alternative is to just use the [33m``[39;49;00m[33mdef[39;49;00m[33m``[39;49;00m statement and define a
function in the usual way[33m::[39;49;00m

[33m        [39;49;00m[33mdef lowercase(x):[39;49;00m
[33m            return x.lower()[39;49;00m
[33m[39;49;00m
[33m        def print_assign(name, value):[39;49;00m
[33m            return name + '=' + str(value)[39;49;00m
[33m[39;49;00m
[33m        def adder(x,y):[39;49;00m
[33m            return x + y[39;49;00m
[33m[39;49;00m
Which alternative is preferable?  That's a style question; my usual
course is to avoid using [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m.

One reason for my preference is that [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m is quite limited in
the functions it can define.  The result has to be computable as a
single expression, which means you can't have multiway
[33m``[39;49;00m[33mif... elif... else[39;49;00m[33m``[39;49;00m comparisons or [33m``[39;49;00m[33mtry... except[39;49;00m[33m``[39;49;00m statements.
If you try to do too much in a [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m statement, you'll end up
with an overly complicated expression that's hard to read.  Quick,
what's the following code doing?

[33m::[39;49;00m

[33m    [39;49;00m[33mtotal = reduce(lambda a, b: (0, a[1] + b[1]), items)[1][39;49;00m
[33m[39;49;00m
You can figure it out, but it takes time to disentangle the expression
to figure out what's going on.  Using a short nested
[33m``[39;49;00m[33mdef[39;49;00m[33m``[39;49;00m statements makes things a little bit better[33m::[39;49;00m

[33m    [39;49;00m[33mdef combine (a, b):[39;49;00m
[33m        return 0, a[1] + b[1][39;49;00m
[33m[39;49;00m
[33m    total = reduce(combine, items)[1][39;49;00m
[33m[39;49;00m
But it would be best of all if I had simply used a [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m loop[33m::[39;49;00m

[33m     [39;49;00m[33mtotal = 0[39;49;00m
[33m     for a, b in items:[39;49;00m
[33m         total += b[39;49;00m
[33m[39;49;00m
Or the [33m``[39;49;00m[33msum()[39;49;00m[33m``[39;49;00m built-in and a generator expression[33m::[39;49;00m

[33m     [39;49;00m[33mtotal = sum(b for a,b in items)[39;49;00m
[33m[39;49;00m
Many uses of [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m are clearer when written as [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m loops.

Fredrik Lundh once suggested the following set of rules for refactoring
uses of [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m:

[34m1)[39;49;00m Write a lambda function.
[34m2)[39;49;00m Write a comment explaining what the heck that lambda does.
[34m3)[39;49;00m Study the comment for a while, and think of a name that captures
   the essence of the comment.
[34m4)[39;49;00m Convert the lambda to a def statement, using that name.
[34m5)[39;49;00m Remove the comment.

I really like these rules, but you're free to disagree that this
lambda-free style is better.


[01mThe itertools module[39;49;00m
[01m-----------------------[39;49;00m

The [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module contains a number of commonly-used iterators
as well as functions for combining several iterators.  This section
will introduce the module's contents by showing small examples.

The module's functions fall into a few broad classes:

[34m*[39;49;00m Functions that create a new iterator based on an existing iterator.
[34m*[39;49;00m Functions for treating an iterator's elements as function arguments.
[34m*[39;49;00m Functions for selecting portions of an iterator's output.
[34m*[39;49;00m A function for grouping an iterator's output.

[01mCreating new iterators[39;49;00m
[01m''''''''''''''''''''''[39;49;00m

[33m``[39;49;00m[33mitertools.count(n)[39;49;00m[33m``[39;49;00m returns an infinite stream of
integers, increasing by 1 each time.  You can optionally supply the
starting number, which defaults to 0[33m::[39;49;00m

[33m        [39;49;00m[33mitertools.count() =>[39;49;00m
[33m          0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...[39;49;00m
[33m        itertools.count(10) =>[39;49;00m
[33m          10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mitertools.cycle(iter)[39;49;00m[33m``[39;49;00m saves a copy of the contents of a provided
iterable and returns a new iterator that returns its elements from
first to last.  The new iterator will repeat these elements infinitely.

[33m::[39;49;00m

[33m        [39;49;00m[33mitertools.cycle([1,2,3,4,5]) =>[39;49;00m
[33m          1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mitertools.repeat(elem, [n])[39;49;00m[33m``[39;49;00m returns the provided element [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m
times, or returns the element endlessly if [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m is not provided.

[33m::[39;49;00m

[33m    [39;49;00m[33mitertools.repeat('abc') =>[39;49;00m
[33m      abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, ...[39;49;00m
[33m    itertools.repeat('abc', 5) =>[39;49;00m
[33m      abc, abc, abc, abc, abc[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mitertools.chain(iterA, iterB, ...)[39;49;00m[33m``[39;49;00m takes an arbitrary number of
iterables as input, and returns all the elements of the first
iterator, then all the elements of the second, and so on, until all of
the iterables have been exhausted.

[33m::[39;49;00m

[33m    [39;49;00m[33mitertools.chain(['a', 'b', 'c'], (1, 2, 3)) =>[39;49;00m
[33m      a, b, c, 1, 2, 3[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mitertools.izip(iterA, iterB, ...)[39;49;00m[33m``[39;49;00m takes one element from each iterable
and returns them in a tuple[33m::[39;49;00m

[33m    [39;49;00m[33mitertools.izip(['a', 'b', 'c'], (1, 2, 3)) =>[39;49;00m
[33m      ('a', 1), ('b', 2), ('c', 3)[39;49;00m
[33m[39;49;00m
It's similiar to the built-in [33m``[39;49;00m[33mzip()[39;49;00m[33m``[39;49;00m function, but doesn't
construct an in-memory list and exhaust all the input iterators before
returning; instead tuples are constructed and returned only if they're
requested.  (The technical term for this behaviour is
[33m`lazy evaluation [39;49;00m[33m<http://en.wikipedia.org/wiki/Lazy_evaluation>[39;49;00m[33m`__[39;49;00m.)

This iterator is intended to be used with iterables that are all of
the same length.  If the iterables are of different lengths, the
resulting stream will be the same length as the shortest iterable.

[33m::[39;49;00m

[33m    [39;49;00m[33mitertools.izip(['a', 'b'], (1, 2, 3)) =>[39;49;00m
[33m      ('a', 1), ('b', 2)[39;49;00m
[33m[39;49;00m
You should avoid doing this, though, because an element may be taken
from the longer iterators and discarded.  This means you can't go on
to use the iterators further because you risk skipping a discarded
element.

[33m``[39;49;00m[33mitertools.islice(iter, [start], stop, [step])[39;49;00m[33m``[39;49;00m returns a stream
that's a slice of the iterator.  With a single [33m``[39;49;00m[33mstop[39;49;00m[33m``[39;49;00m argument,
it will return the first [33m``[39;49;00m[33mstop[39;49;00m[33m``[39;49;00m
elements.  If you supply a starting index, you'll get [33m``[39;49;00m[33mstop-start[39;49;00m[33m``[39;49;00m
elements, and if you supply a value for [33m``[39;49;00m[33mstep[39;49;00m[33m``[39;49;00m, elements will be
skipped accordingly.  Unlike Python's string and list slicing, you
can't use negative values for [33m``[39;49;00m[33mstart[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mstop[39;49;00m[33m``[39;49;00m, or [33m``[39;49;00m[33mstep[39;49;00m[33m``[39;49;00m.

[33m::[39;49;00m

[33m    [39;49;00m[33mitertools.islice(range(10), 8) =>[39;49;00m
[33m      0, 1, 2, 3, 4, 5, 6, 7[39;49;00m
[33m    itertools.islice(range(10), 2, 8) =>[39;49;00m
[33m      2, 3, 4, 5, 6, 7[39;49;00m
[33m    itertools.islice(range(10), 2, 8, 2) =>[39;49;00m
[33m      2, 4, 6[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mitertools.tee(iter, [n])[39;49;00m[33m``[39;49;00m replicates an iterator; it returns [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m
independent iterators that will all return the contents of the source
iterator.  If you don't supply a value for [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m, the default is 2.
Replicating iterators requires saving some of the contents of the source
iterator, so this can consume significant memory if the iterator is large
and one of the new iterators is consumed more than the others.

[33m::[39;49;00m

[33m        [39;49;00m[33mitertools.tee( itertools.count() ) =>[39;49;00m
[33m           iterA, iterB[39;49;00m
[33m[39;49;00m
[33m        where iterA ->[39;49;00m
[33m           0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...[39;49;00m
[33m[39;49;00m
[33m        and   iterB ->[39;49;00m
[33m           0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[01mCalling functions on elements[39;49;00m
[01m'''''''''''''''''''''''''''''[39;49;00m

Two functions are used for calling other functions on the contents of an
iterable.

[33m``[39;49;00m[33mitertools.imap(f, iterA, iterB, ...)[39;49;00m[33m``[39;49;00m returns
a stream containing [33m``[39;49;00m[33mf(iterA[0], iterB[0]), f(iterA[1], iterB[1]),[39;49;00m
[33mf(iterA[2], iterB[2]), ...[39;49;00m[33m``[39;49;00m[33m::[39;49;00m

[33m    [39;49;00m[33mitertools.imap(operator.add, [5, 6, 5], [1, 2, 3]) =>[39;49;00m
[33m      6, 8, 8[39;49;00m
[33m[39;49;00m
The [33m``[39;49;00m[33moperator[39;49;00m[33m``[39;49;00m module contains a set of functions
corresponding to Python's operators.  Some examples are
[33m``[39;49;00m[33moperator.add(a, b)[39;49;00m[33m``[39;49;00m (adds two values),
[33m``[39;49;00m[33moperator.ne(a, b)[39;49;00m[33m``[39;49;00m (same as [33m``[39;49;00m[33ma!=b[39;49;00m[33m``[39;49;00m),
and
[33m``[39;49;00m[33moperator.attrgetter('id')[39;49;00m[33m``[39;49;00m (returns a callable that
fetches the [33m``[39;49;00m[33m"id"[39;49;00m[33m``[39;49;00m attribute).

[33m``[39;49;00m[33mitertools.starmap(func, iter)[39;49;00m[33m``[39;49;00m assumes that the iterable will
return a stream of tuples, and calls [33m``[39;49;00m[33mf()[39;49;00m[33m``[39;49;00m using these tuples as the
arguments[33m::[39;49;00m

[33m    [39;49;00m[33mitertools.starmap(os.path.join, [39;49;00m
[33m                      [('/usr', 'bin', 'java'), ('/bin', 'python'),[39;49;00m
[33m                       ('/usr', 'bin', 'perl'),('/usr', 'bin', 'ruby')])[39;49;00m
[33m    =>[39;49;00m
[33m      /usr/bin/java, /bin/python, /usr/bin/perl, /usr/bin/ruby[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[01mSelecting elements[39;49;00m
[01m''''''''''''''''''[39;49;00m

Another group of functions chooses a subset of an iterator's elements
based on a predicate.

[33m``[39;49;00m[33mitertools.ifilter(predicate, iter)[39;49;00m[33m``[39;49;00m returns all the elements for
which the predicate returns true[33m::[39;49;00m

[33m    [39;49;00m[33mdef is_even(x):[39;49;00m
[33m        return (x % 2) == 0[39;49;00m
[33m[39;49;00m
[33m    itertools.ifilter(is_even, itertools.count()) =>[39;49;00m
[33m      0, 2, 4, 6, 8, 10, 12, 14, ...[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mitertools.ifilterfalse(predicate, iter)[39;49;00m[33m``[39;49;00m is the opposite,
returning all elements for which the predicate returns false[33m::[39;49;00m

[33m    [39;49;00m[33mitertools.ifilterfalse(is_even, itertools.count()) =>[39;49;00m
[33m      1, 3, 5, 7, 9, 11, 13, 15, ...[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mitertools.takewhile(predicate, iter)[39;49;00m[33m``[39;49;00m returns elements for as long
as the predicate returns true.  Once the predicate returns false,
the iterator will signal the end of its results.

[33m::[39;49;00m

[33m    [39;49;00m[33mdef less_than_10(x):[39;49;00m
[33m        return (x < 10)[39;49;00m
[33m[39;49;00m
[33m    itertools.takewhile(less_than_10, itertools.count()) =>[39;49;00m
[33m      0, 1, 2, 3, 4, 5, 6, 7, 8, 9[39;49;00m
[33m[39;49;00m
[33m    itertools.takewhile(is_even, itertools.count()) =>[39;49;00m
[33m      0[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mitertools.dropwhile(predicate, iter)[39;49;00m[33m``[39;49;00m discards elements while the
predicate returns true, and then returns the rest of the iterable's
results.

[33m::[39;49;00m

[33m    [39;49;00m[33mitertools.dropwhile(less_than_10, itertools.count()) =>[39;49;00m
[33m      10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...[39;49;00m
[33m[39;49;00m
[33m    itertools.dropwhile(is_even, itertools.count()) =>[39;49;00m
[33m      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[01mGrouping elements[39;49;00m
[01m'''''''''''''''''[39;49;00m

The last function I'll discuss, [33m``[39;49;00m[33mitertools.groupby(iter,[39;49;00m
[33mkey_func=None)[39;49;00m[33m``[39;49;00m, is the most complicated.  [33m``[39;49;00m[33mkey_func(elem)[39;49;00m[33m``[39;49;00m is a
function that can compute a key value for each element returned by the
iterable.  If you don't supply a key function, the key is simply each
element itself.

[33m``[39;49;00m[33mgroupby()[39;49;00m[33m``[39;49;00m collects all the consecutive elements from the
underlying iterable that have the same key value, and returns a stream
of 2-tuples containing a key value and an iterator for the elements
with that key.

[33m::[39;49;00m

[33m    [39;49;00m[33mcity_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'), [39;49;00m
[33m                 ('Anchorage', 'AK'), ('Nome', 'AK'),[39;49;00m
[33m                 ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'), [39;49;00m
[33m                 ...[39;49;00m
[33m                ][39;49;00m
[33m[39;49;00m
[33m    def get_state ((city, state)):[39;49;00m
[33m        return state[39;49;00m
[33m[39;49;00m
[33m    itertools.groupby(city_list, get_state) =>[39;49;00m
[33m      ('AL', iterator-1),[39;49;00m
[33m      ('AK', iterator-2),[39;49;00m
[33m      ('AZ', iterator-3), ...[39;49;00m
[33m[39;49;00m
[33m    where[39;49;00m
[33m    iterator-1 =>[39;49;00m
[33m      ('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')[39;49;00m
[33m    iterator-2 => [39;49;00m
[33m      ('Anchorage', 'AK'), ('Nome', 'AK')[39;49;00m
[33m    iterator-3 =>[39;49;00m
[33m      ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mgroupby()[39;49;00m[33m``[39;49;00m assumes that the underlying iterable's contents will
already be sorted based on the key.  Note that the returned iterators
also use the underlying iterable, so you have to consume the results
of iterator-1 before requesting iterator-2 and its corresponding key.


[01mThe functools module[39;49;00m
[01m----------------------------------------------[39;49;00m

The [33m``[39;49;00m[33mfunctools[39;49;00m[33m``[39;49;00m module in Python 2.5 contains some higher-order
functions.  A **higher-order function** takes one or more functions as
input and returns a new function.  The most useful tool in this module
is the [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m function.

For programs written in a functional style, you'll sometimes want to
construct variants of existing functions that have some of the
parameters filled in.  Consider a Python function [33m``[39;49;00m[33mf(a, b, c)[39;49;00m[33m``[39;49;00m; you
may wish to create a new function [33m``[39;49;00m[33mg(b, c)[39;49;00m[33m``[39;49;00m that's equivalent to
[33m``[39;49;00m[33mf(1, b, c)[39;49;00m[33m``[39;49;00m; you're filling in a value for one of [33m``[39;49;00m[33mf()[39;49;00m[33m``[39;49;00m's parameters.
This is called "partial function application".

The constructor for [33m``[39;49;00m[33mpartial[39;49;00m[33m``[39;49;00m takes the arguments [33m``[39;49;00m[33m(function, arg1,[39;49;00m
[33marg2, ... kwarg1=value1, kwarg2=value2)[39;49;00m[33m``[39;49;00m.  The resulting object is
callable, so you can just call it to invoke [33m``[39;49;00m[33mfunction[39;49;00m[33m``[39;49;00m with the
filled-in arguments.

Here's a small but realistic example[33m::[39;49;00m

[33m    [39;49;00m[33mimport functools[39;49;00m
[33m[39;49;00m
[33m    def log (message, subsystem):[39;49;00m
[33m        "Write the contents of 'message' to the specified subsystem."[39;49;00m
[33m        print '%s: %s' % (subsystem, message)[39;49;00m
[33m        ...[39;49;00m
[33m[39;49;00m
[33m    server_log = functools.partial(log, subsystem='server')[39;49;00m
[33m    server_log('Unable to open socket')[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[01mThe operator module[39;49;00m
[01m-------------------[39;49;00m

The [33m``[39;49;00m[33moperator[39;49;00m[33m``[39;49;00m module was mentioned earlier.  It contains a set of
functions corresponding to Python's operators.  These functions
are often useful in functional-style code because they save you
from writing trivial functions that perform a single operation.

Some of the functions in this module are:

[34m*[39;49;00m Math operations: [33m``[39;49;00m[33madd()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33msub()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mmul()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mdiv()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mfloordiv()[39;49;00m[33m``[39;49;00m,
  [33m``[39;49;00m[33mabs()[39;49;00m[33m``[39;49;00m, ...
[34m*[39;49;00m Logical operations: [33m``[39;49;00m[33mnot_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mtruth()[39;49;00m[33m``[39;49;00m.
[34m*[39;49;00m Bitwise operations: [33m``[39;49;00m[33mand_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mor_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33minvert()[39;49;00m[33m``[39;49;00m.
[34m*[39;49;00m Comparisons: [33m``[39;49;00m[33meq()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mne()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mlt()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mle()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mgt()[39;49;00m[33m``[39;49;00m, and [33m``[39;49;00m[33mge()[39;49;00m[33m``[39;49;00m.
[34m*[39;49;00m Object identity: [33m``[39;49;00m[33mis_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mis_not()[39;49;00m[33m``[39;49;00m.

Consult [33m`the operator module's documentation [39;49;00m[33m<http://docs.python.org/lib/module-operator.html>[39;49;00m[33m`__[39;49;00m for a complete
list.



[01mThe functional module[39;49;00m
[01m---------------------[39;49;00m

Collin Winter's [33m`functional module [39;49;00m[33m<http://oakwinter.com/code/functional/>[39;49;00m[33m`__[39;49;00m
provides a number of more
advanced tools for functional programming. It also reimplements
several Python built-ins, trying to make them more intuitive to those
used to functional programming in other languages.

This section contains an introduction to some of the most important
functions in [33m``[39;49;00m[33mfunctional[39;49;00m[33m``[39;49;00m; full documentation can be found at `the
project's website <http://oakwinter.com/code/functional/documentation/>`__.

[33m``[39;49;00m[33mcompose(outer, inner, unpack=False)[39;49;00m[33m``[39;49;00m

The [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m function implements function composition.
In other words, it returns a wrapper around the [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m callables, such
that the return value from [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m is fed directly to [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m.  That is,

[33m::[39;49;00m

[33m        [39;49;00m[33m>>> def add(a, b):[39;49;00m
[33m        ...     return a + b[39;49;00m
[33m        ...[39;49;00m
[33m        >>> def double(a):[39;49;00m
[33m        ...     return 2 * a[39;49;00m
[33m        ...[39;49;00m
[33m        >>> compose(double, add)(5, 6)[39;49;00m
[33m        22[39;49;00m
[33m[39;49;00m
is equivalent to

[33m::[39;49;00m

[33m        [39;49;00m[33m>>> double(add(5, 6))[39;49;00m
[33m        22[39;49;00m
[33m                    [39;49;00m
The [33m``[39;49;00m[33munpack[39;49;00m[33m``[39;49;00m keyword is provided to work around the fact that Python functions are not always
[33m`fully curried [39;49;00m[33m<http://en.wikipedia.org/wiki/Currying>[39;49;00m[33m`__[39;49;00m.
By default, it is expected that the [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m function will return a single object and that the [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m
function will take a single argument. Setting the [33m``[39;49;00m[33munpack[39;49;00m[33m``[39;49;00m argument causes [33m``[39;49;00m[33mcompose[39;49;00m[33m``[39;49;00m to expect a
tuple from [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m which will be expanded before being passed to [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m. Put simply,

[33m::[39;49;00m

[33m        [39;49;00m[33mcompose(f, g)(5, 6)[39;49;00m
[33m                    [39;49;00m
is equivalent to[33m::[39;49;00m

[33m        [39;49;00m[33mf(g(5, 6))[39;49;00m
[33m                    [39;49;00m
while

[33m::[39;49;00m

[33m        [39;49;00m[33mcompose(f, g, unpack=True)(5, 6)[39;49;00m
[33m                    [39;49;00m
is equivalent to[33m::[39;49;00m

[33m        [39;49;00m[33mf(*g(5, 6))[39;49;00m
[33m[39;49;00m
Even though [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m only accepts two functions, it's trivial to
build up a version that will compose any number of functions. We'll
use [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m (the last of which
is provided by both [33m``[39;49;00m[33mfunctional[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfunctools[39;49;00m[33m``[39;49;00m).

[33m::[39;49;00m

[33m        [39;49;00m[33mfrom functional import compose, partial[39;49;00m
[33m        [39;49;00m
[33m        multi_compose = partial(reduce, compose)[39;49;00m
[33m        [39;49;00m

We can also use [33m``[39;49;00m[33mmap()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m to craft a
version of [33m``[39;49;00m[33m"".join(...)[39;49;00m[33m``[39;49;00m that converts its arguments to string[33m::[39;49;00m

[33m        [39;49;00m[33mfrom functional import compose, partial[39;49;00m
[33m        [39;49;00m
[33m        join = compose("".join, partial(map, str))[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mflip(func)[39;49;00m[33m``[39;49;00m

[33m``[39;49;00m[33mflip()[39;49;00m[33m``[39;49;00m wraps the callable in [33m``[39;49;00m[33mfunc[39;49;00m[33m``[39;49;00m and
causes it to receive its non-keyword arguments in reverse order.

[33m::[39;49;00m

[33m        [39;49;00m[33m>>> def triple(a, b, c):[39;49;00m
[33m        ...     return (a, b, c)[39;49;00m
[33m        ...[39;49;00m
[33m        >>> triple(5, 6, 7)[39;49;00m
[33m        (5, 6, 7)[39;49;00m
[33m        >>>[39;49;00m
[33m        >>> flipped_triple = flip(triple)[39;49;00m
[33m        >>> flipped_triple(5, 6, 7)[39;49;00m
[33m        (7, 6, 5)[39;49;00m
[33m[39;49;00m
[33m``[39;49;00m[33mfoldl(func, start, iterable)[39;49;00m[33m``[39;49;00m

[33m``[39;49;00m[33mfoldl()[39;49;00m[33m``[39;49;00m takes a binary function, a starting value (usually some kind of 'zero'), and an iterable.
The function is applied to the starting value and the first element of the list, then the result of
that and the second element of the list, then the result of that and the third element of the list,
and so on.

This means that a call such as[33m::[39;49;00m

[33m        [39;49;00m[33mfoldl(f, 0, [1, 2, 3])[39;49;00m
[33m[39;49;00m
is equivalent to[33m::[39;49;00m

[33m        [39;49;00m[33mf(f(f(0, 1), 2), 3)[39;49;00m
[33m[39;49;00m

[33m``[39;49;00m[33mfoldl()[39;49;00m[33m``[39;49;00m is roughly equivalent to the following recursive function[33m::[39;49;00m

[33m        [39;49;00m[33mdef foldl(func, start, seq):[39;49;00m
[33m            if len(seq) == 0:[39;49;00m
[33m                return start[39;49;00m
[33m[39;49;00m
[33m            return foldl(func, func(start, seq[0]), seq[1:])[39;49;00m
[33m[39;49;00m
Speaking of equivalence, the above [33m``[39;49;00m[33mfoldl[39;49;00m[33m``[39;49;00m call can be expressed in terms of the built-in [33m``[39;49;00m[33mreduce[39;49;00m[33m``[39;49;00m like
so[33m::[39;49;00m

[33m        [39;49;00m[33mreduce(f, [1, 2, 3], 0)[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
We can use [33m``[39;49;00m[33mfoldl()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33moperator.concat()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m to
write a cleaner, more aesthetically-pleasing version of Python's
[33m``[39;49;00m[33m"".join(...)[39;49;00m[33m``[39;49;00m idiom[33m::[39;49;00m

[33m        [39;49;00m[33mfrom functional import foldl, partial[39;49;00m
[33m        from operator import concat[39;49;00m
[33m        [39;49;00m
[33m        join = partial(foldl, concat, "")[39;49;00m
[33m[39;49;00m
[33m[39;49;00m
[01mRevision History and Acknowledgements[39;49;00m
[01m------------------------------------------------[39;49;00m

The author would like to thank the following people for offering
suggestions, corrections and assistance with various drafts of this
article: Ian Bicking, Nick Coghlan, Nick Efford, Raymond Hettinger,
Jim Jewett, Mike Krell, Leandro Lameiro, Jussi Salmela,
Collin Winter, Blake Winton.

Version 0.1: posted June 30 2006.

Version 0.11: posted July 1 2006.  Typo fixes.

Version 0.2: posted July 10 2006.  Merged genexp and listcomp
sections into one.  Typo fixes.

Version 0.21: Added more references suggested on the tutor mailing list.

Version 0.30: Adds a section on the [33m``[39;49;00m[33mfunctional[39;49;00m[33m``[39;49;00m module written by
Collin Winter; adds short section on the operator module; a few other
edits.


[01mReferences[39;49;00m
[01m--------------------[39;49;00m

[01mGeneral[39;49;00m
[01m'''''''''''''''[39;49;00m

**Structure and Interpretation of Computer Programs**, by
Harold Abelson and Gerald Jay Sussman with Julie Sussman.
Full text at http://mitpress.mit.edu/sicp/.
In this classic textbook of computer science,  chapters 2 and 3 discuss the
use of sequences and streams to organize the data flow inside a
program.  The book uses Scheme for its examples, but many of the
design approaches described in these chapters are applicable to
functional-style Python code.

http://www.defmacro.org/ramblings/fp.html: A general
introduction to functional programming that uses Java examples
and has a lengthy historical introduction.

http://en.wikipedia.org/wiki/Functional_programming:
General Wikipedia entry describing functional programming.

http://en.wikipedia.org/wiki/Coroutine:
Entry for coroutines.

http://en.wikipedia.org/wiki/Currying:
Entry for the concept of currying.

[01mPython-specific[39;49;00m
[01m'''''''''''''''''''''''''''[39;49;00m

http://gnosis.cx/TPiP/:
The first chapter of David Mertz's book [36m:title-reference:[39;49;00m[31m`Text Processing in Python`[39;49;00m
discusses functional programming for text processing, in the section titled
"Utilizing Higher-Order Functions in Text Processing".

Mertz also wrote a 3-part series of articles on functional programming
for IBM's DeveloperWorks site; see
[33m`part 1 [39;49;00m[33m<http://www-128.ibm.com/developerworks/library/l-prog.html>[39;49;00m[33m`__[39;49;00m,
[33m`part 2 [39;49;00m[33m<http://www-128.ibm.com/developerworks/library/l-prog2.html>[39;49;00m[33m`__[39;49;00m, and
[33m`part 3 [39;49;00m[33m<http://www-128.ibm.com/developerworks/linux/library/l-prog3.html>[39;49;00m[33m`__[39;49;00m,


[01mPython documentation[39;49;00m
[01m'''''''''''''''''''''''''''[39;49;00m

http://docs.python.org/lib/module-itertools.html:
Documentation for the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module.

http://docs.python.org/lib/module-operator.html:
Documentation for the [33m``[39;49;00m[33moperator[39;49;00m[33m``[39;49;00m module.

http://www.python.org/dev/peps/pep-0289/:
PEP 289: "Generator Expressions"

http://www.python.org/dev/peps/pep-0342/
PEP 342: "Coroutines via Enhanced Generators" describes the new generator
features in Python 2.5.

[36m.. comment[39;49;00m
[36m[39;49;00m
[36m    Topics to place[39;49;00m
[36m    -----------------------------[39;49;00m
[36m[39;49;00m
[36m    XXX os.walk()[39;49;00m
[36m[39;49;00m
[36m    XXX Need a large example.[39;49;00m
[36m[39;49;00m
[36m    But will an example add much?  I'll post a first draft and see[39;49;00m
[36m    what the comments say.[39;49;00m
[36m[39;49;00m
[36m.. comment[39;49;00m
[36m[39;49;00m
[36m    Original outline:[39;49;00m
[36m    Introduction[39;49;00m
[36m            Idea of FP[39;49;00m
[36m                    Programs built out of functions[39;49;00m
[36m                    Functions are strictly input-output, no internal state[39;49;00m
[36m            Opposed to OO programming, where objects have state[39;49;00m
[36m[39;49;00m
[36m            Why FP?[39;49;00m
[36m                    Formal provability[39;49;00m
[36m                            Assignment is difficult to reason about[39;49;00m
[36m                            Not very relevant to Python[39;49;00m
[36m                    Modularity[39;49;00m
[36m                            Small functions that do one thing[39;49;00m
[36m                    Debuggability:[39;49;00m
[36m                            Easy to test due to lack of state[39;49;00m
[36m                            Easy to verify output from intermediate steps[39;49;00m
[36m                    Composability[39;49;00m
[36m                            You assemble a toolbox of functions that can be mixed[39;49;00m
[36m[39;49;00m
[36m    Tackling a problem[39;49;00m
[36m            Need a significant example[39;49;00m
[36m[39;49;00m
[36m    Iterators[39;49;00m
[36m    Generators[39;49;00m
[36m    The itertools module[39;49;00m
[36m    List comprehensions[39;49;00m
[36m    Small functions and the lambda statement[39;49;00m
[36m    Built-in functions[39;49;00m
[36m            map[39;49;00m
[36m            filter[39;49;00m
[36m            reduce[39;49;00m
[36m[39;49;00m
[36m.. comment[39;49;00m
[36m[39;49;00m
[36m    Handy little function for printing part of an iterator -- used[39;49;00m
[36m    while writing this document.[39;49;00m
[36m[39;49;00m
[36m    import itertools[39;49;00m
[36m    def print_iter(it):[39;49;00m
[36m         slice = itertools.islice(it, 10)[39;49;00m
[36m         for elem in slice[:-1]:[39;49;00m
[36m             sys.stdout.write(str(elem))[39;49;00m
[36m             sys.stdout.write(', ')[39;49;00m
        print elem[-1]
