     1	[01mFunctional Programming HOWTO[39;49;00m
     2	[01m================================[39;49;00m
     3
     4	**Version 0.30**
     5
     6	(This is a first draft.  Please send comments/error
     7	reports/suggestions to amk@amk.ca.  This URL is probably not going to
     8	be the final location of the document, so be careful about linking to
     9	it -- you may want to add a disclaimer.)
    10
    11	In this document, we'll take a tour of Python's features suitable for
    12	implementing programs in a functional style.  After an introduction to
    13	the concepts of functional programming, we'll look at language
    14	features such as iterators and generators and relevant library modules
    15	such as [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfunctools[39;49;00m[33m``[39;49;00m.
    16
    17
    18	.. [35mcontents[39;49;00m::
    19
    20	[01mIntroduction[39;49;00m
    21	[01m----------------------[39;49;00m
    22
    23	This section explains the basic concept of functional programming; if
    24	you're just interested in learning about Python language features,
    25	skip to the next section.
    26
    27	Programming languages support decomposing problems in several different
    28	ways:
    29
    30	[34m*[39;49;00m Most programming languages are **procedural**:
    31	  programs are lists of instructions that tell the computer what to
    32	  do with the program's input.
    33	  C, Pascal, and even Unix shells are procedural languages.
    34
    35	[34m*[39;49;00m In **declarative** languages, you write a specification that describes
    36	  the problem to be solved, and the language implementation figures out
    37	  how to perform the computation efficiently.  SQL is the declarative
    38	  language you're most likely to be familiar with; a SQL query describes
    39	  the data set you want to retrieve, and the SQL engine decides whether to
    40	  scan tables or use indexes, which subclauses should be performed first,
    41	  etc.
    42
    43	[34m*[39;49;00m **Object-oriented** programs manipulate  collections of objects.
    44	  Objects have internal state and support methods that query or modify
    45	  this internal state in some way. Smalltalk and Java are
    46	  object-oriented languages.  C++ and Python are languages that
    47	  support object-oriented programming, but don't force the use
    48	  of object-oriented features.
    49
    50	[34m*[39;49;00m **Functional** programming decomposes a problem into a set of functions.
    51	  Ideally, functions only take inputs and produce outputs, and don't have any
    52	  internal state that affects the output produced for a given input.
    53	  Well-known functional languages include the ML family (Standard ML,
    54	  OCaml, and other variants) and Haskell.
    55
    56	The designers of some computer languages have chosen one approach to
    57	programming that's emphasized.  This often makes it difficult to
    58	write programs that use a different approach.  Other languages are
    59	multi-paradigm languages that support several different approaches.  Lisp,
    60	C++, and Python are multi-paradigm; you can write programs or
    61	libraries that are largely procedural, object-oriented, or functional
    62	in all of these languages.  In a large program, different sections
    63	might be written using different approaches; the GUI might be object-oriented
    64	while the processing logic is procedural or functional, for example.
    65
    66	In a functional program, input flows through a set of functions. Each
    67	function operates on its input and produces some output.  Functional
    68	style frowns upon functions with side effects that modify internal
    69	state or make other changes that aren't visible in the function's
    70	return value.  Functions that have no side effects at all are
    71	called **purely functional**.
    72	Avoiding side effects means not using data structures
    73	that get updated as a program runs; every function's output
    74	must only depend on its input.
    75
    76	Some languages are very strict about purity and don't even have
    77	assignment statements such as [33m``[39;49;00m[33ma=3[39;49;00m[33m``[39;49;00m or [33m``[39;49;00m[33mc = a + b[39;49;00m[33m``[39;49;00m, but it's
    78	difficult to avoid all side effects.  Printing to the screen or
    79	writing to a disk file are side effects, for example.  For example, in
    80	Python a [33m``[39;49;00m[33mprint[39;49;00m[33m``[39;49;00m statement or a [33m``[39;49;00m[33mtime.sleep(1)[39;49;00m[33m``[39;49;00m both return no
    81	useful value; they're only called for their side effects of sending
    82	some text to the screen or pausing execution for a second.
    83
    84	Python programs written in functional style usually won't go to the
    85	extreme of avoiding all I/O or all assignments; instead, they'll
    86	provide a functional-appearing interface but will use non-functional
    87	features internally.  For example, the implementation of a function
    88	will still use assignments to local variables, but won't modify global
    89	variables or have other side effects.
    90
    91	Functional programming can be considered the opposite of
    92	object-oriented programming.  Objects are little capsules containing
    93	some internal state along with a collection of method calls that let
    94	you modify this state, and programs consist of making the right set of
    95	state changes.  Functional programming wants to avoid state changes as
    96	much as possible and works with data flowing between functions.  In
    97	Python you might combine the two approaches by writing functions that
    98	take and return instances representing objects in your application
    99	(e-mail messages, transactions, etc.).
   100
   101	Functional design may seem like an odd constraint to work under.  Why
   102	should you avoid objects and side effects?  There are theoretical and
   103	practical advantages to the functional style:
   104
   105	[34m*[39;49;00m Formal provability.
   106	[34m*[39;49;00m Modularity.
   107	[34m*[39;49;00m Composability.
   108	[34m*[39;49;00m Ease of debugging and testing.
   109
   110	[01mFormal provability[39;49;00m
   111	[01m''''''''''''''''''''''[39;49;00m
   112
   113	A theoretical benefit is that it's easier to construct a mathematical proof
   114	that a functional program is correct.
   115
   116	For a long time researchers have been interested in finding ways to
   117	mathematically prove programs correct.  This is different from testing
   118	a program on numerous inputs and concluding that its output is usually
   119	correct, or reading a program's source code and concluding that the
   120	code looks right; the goal is instead a rigorous proof that a program
   121	produces the right result for all possible inputs.
   122
   123	The technique used to prove programs correct is to write down
   124	**invariants**, properties of the input data and of the program's
   125	variables that are always true.  For each line of code, you then show
   126	that if invariants X and Y are true **before** the line is executed,
   127	the slightly different invariants X' and Y' are true **after**
   128	the line is executed.  This continues until you reach the end of the
   129	program, at which point the invariants should match the desired
   130	conditions on the program's output.
   131
   132	Functional programming's avoidance of assignments arose because
   133	assignments are difficult to handle with this technique;
   134	assignments can break invariants that were true before the assignment
   135	without producing any new invariants that can be propagated onward.
   136
   137	Unfortunately, proving programs correct is largely impractical and not
   138	relevant to Python software. Even trivial programs require proofs that
   139	are several pages long; the proof of correctness for a moderately
   140	complicated program would be enormous, and few or none of the programs
   141	you use daily (the Python interpreter, your XML parser, your web
   142	browser) could be proven correct.  Even if you wrote down or generated
   143	a proof, there would then be the question of verifying the proof;
   144	maybe there's an error in it, and you wrongly believe you've proved
   145	the program correct.
   146
   147	[01mModularity[39;49;00m
   148	[01m''''''''''''''''''''''[39;49;00m
   149
   150	A more practical benefit of functional programming is that it forces
   151	you to break apart your problem into small pieces.  Programs are more
   152	modular as a result.  It's easier to specify and write a small
   153	function that does one thing than a large function that performs a
   154	complicated transformation.  Small functions are also easier to read
   155	and to check for errors.
   156
   157
   158	[01mEase of debugging and testing [39;49;00m
   159	[01m''''''''''''''''''''''''''''''''''[39;49;00m
   160
   161	Testing and debugging a functional-style program is easier.
   162
   163	Debugging is simplified because functions are generally small and
   164	clearly specified.  When a program doesn't work, each function is an
   165	interface point where you can check that the data are correct.  You
   166	can look at the intermediate inputs and outputs to quickly isolate the
   167	function that's responsible for a bug.
   168
   169	Testing is easier because each function is a potential subject for a
   170	unit test.  Functions don't depend on system state that needs to be
   171	replicated before running a test; instead you only have to synthesize
   172	the right input and then check that the output matches expectations.
   173
   174
   175
   176	[01mComposability[39;49;00m
   177	[01m''''''''''''''''''''''[39;49;00m
   178
   179	As you work on a functional-style program, you'll write a number of
   180	functions with varying inputs and outputs.  Some of these functions
   181	will be unavoidably specialized to a particular application, but
   182	others will be useful in a wide variety of programs.  For example, a
   183	function that takes a directory path and returns all the XML files in
   184	the directory, or a function that takes a filename and returns its
   185	contents, can be applied to many different situations.
   186
   187	Over time you'll form a personal library of utilities.  Often you'll
   188	assemble new programs by arranging existing functions in a new
   189	configuration and writing a few functions specialized for the current
   190	task.
   191
   192
   193
   194	[01mIterators[39;49;00m
   195	[01m-----------------------[39;49;00m
   196
   197	I'll start by looking at a Python language feature that's an important
   198	foundation for writing functional-style programs: iterators.
   199
   200	An iterator is an object representing a stream of data; this object
   201	returns the data one element at a time.  A Python iterator must
   202	support a method called [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m that takes no arguments and always
   203	returns the next element of the stream.  If there are no more elements
   204	in the stream, [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m must raise the [33m``[39;49;00m[33mStopIteration[39;49;00m[33m``[39;49;00m exception.
   205	Iterators don't have to be finite, though; it's perfectly reasonable
   206	to write an iterator that produces an infinite stream of data.
   207
   208	The built-in [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m function takes an arbitrary object and tries
   209	to return an iterator that will return the object's contents or
   210	elements, raising [33m``[39;49;00m[33mTypeError[39;49;00m[33m``[39;49;00m if the object doesn't support
   211	iteration.  Several of Python's built-in data types support iteration,
   212	the most common being lists and dictionaries.  An object is called
   213	an **iterable** object if you can get an iterator for it.
   214
   215	You can experiment with the iteration interface manually[33m::[39;49;00m
   216
   217	[33m    [39;49;00m[33m>>> L = [1,2,3][39;49;00m
   218	[33m    >>> it = iter(L)[39;49;00m
   219	[33m    >>> print it[39;49;00m
   220	[33m    <iterator object at 0x8116870>[39;49;00m
   221	[33m    >>> it.next()[39;49;00m
   222	[33m    1[39;49;00m
   223	[33m    >>> it.next()[39;49;00m
   224	[33m    2[39;49;00m
   225	[33m    >>> it.next()[39;49;00m
   226	[33m    3[39;49;00m
   227	[33m    >>> it.next()[39;49;00m
   228	[33m    Traceback (most recent call last):[39;49;00m
   229	[33m      File "<stdin>", line 1, in ?[39;49;00m
   230	[33m    StopIteration[39;49;00m
   231	[33m    >>>      [39;49;00m
   232	[33m[39;49;00m
   233	Python expects iterable objects in several different contexts, the
   234	most important being the [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m statement.  In the statement [33m``[39;49;00m[33mfor X in Y[39;49;00m[33m``[39;49;00m,
   235	Y must be an iterator or some object for which [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m can create
   236	an iterator.  These two statements are equivalent[33m::[39;49;00m
   237
   238	[33m        [39;49;00m[33mfor i in iter(obj):[39;49;00m
   239	[33m            print i[39;49;00m
   240	[33m[39;49;00m
   241	[33m        for i in obj:[39;49;00m
   242	[33m            print i[39;49;00m
   243	[33m[39;49;00m
   244	Iterators can be materialized as lists or tuples by using the
   245	[33m``[39;49;00m[33mlist()[39;49;00m[33m``[39;49;00m or [33m``[39;49;00m[33mtuple()[39;49;00m[33m``[39;49;00m constructor functions[33m::[39;49;00m
   246
   247	[33m    [39;49;00m[33m>>> L = [1,2,3][39;49;00m
   248	[33m    >>> iterator = iter(L)[39;49;00m
   249	[33m    >>> t = tuple(iterator)[39;49;00m
   250	[33m    >>> t[39;49;00m
   251	[33m    (1, 2, 3)[39;49;00m
   252	[33m[39;49;00m
   253	Sequence unpacking also supports iterators: if you know an iterator
   254	will return N elements, you can unpack them into an N-tuple[33m::[39;49;00m
   255
   256	[33m    [39;49;00m[33m>>> L = [1,2,3][39;49;00m
   257	[33m    >>> iterator = iter(L)[39;49;00m
   258	[33m    >>> a,b,c = iterator[39;49;00m
   259	[33m    >>> a,b,c[39;49;00m
   260	[33m    (1, 2, 3)[39;49;00m
   261	[33m[39;49;00m
   262	Built-in functions such as [33m``[39;49;00m[33mmax()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mmin()[39;49;00m[33m``[39;49;00m can take a single
   263	iterator argument and will return the largest or smallest element.
   264	The [33m``[39;49;00m[33m"in"[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33m"not in"[39;49;00m[33m``[39;49;00m operators also support iterators: [33m``[39;49;00m[33mX in[39;49;00m
   265	[33miterator[39;49;00m[33m``[39;49;00m is true if X is found in the stream returned by the
   266	iterator.  You'll run into obvious problems if the iterator is
   267	infinite; [33m``[39;49;00m[33mmax()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mmin()[39;49;00m[33m``[39;49;00m, and [33m``[39;49;00m[33m"not in"[39;49;00m[33m``[39;49;00m will never return, and
   268	if the element X never appears in the stream, the [33m``[39;49;00m[33m"in"[39;49;00m[33m``[39;49;00m operator
   269	won't return either.
   270
   271	Note that you can only go forward in an iterator; there's no way to
   272	get the previous element, reset the iterator, or make a copy of it.
   273	Iterator objects can optionally provide these additional capabilities,
   274	but the iterator protocol only specifies the [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m method.
   275	Functions may therefore consume all of the iterator's output, and if
   276	you need to do something different with the same stream, you'll have
   277	to create a new iterator.
   278
   279
   280
   281	[01mData Types That Support Iterators[39;49;00m
   282	[01m'''''''''''''''''''''''''''''''''''[39;49;00m
   283
   284	We've already seen how lists and tuples support iterators.  In fact,
   285	any Python sequence type, such as strings, will automatically support
   286	creation of an iterator.
   287
   288	Calling [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m on a dictionary returns an iterator that will loop
   289	over the dictionary's keys[33m::[39;49;00m
   290
   291	[33m    [39;49;00m[33m>>> m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,[39;49;00m
   292	[33m    ...      'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}[39;49;00m
   293	[33m    >>> for key in m:[39;49;00m
   294	[33m    ...     print key, m[key][39;49;00m
   295	[33m    Mar 3[39;49;00m
   296	[33m    Feb 2[39;49;00m
   297	[33m    Aug 8[39;49;00m
   298	[33m    Sep 9[39;49;00m
   299	[33m    May 5[39;49;00m
   300	[33m    Jun 6[39;49;00m
   301	[33m    Jul 7[39;49;00m
   302	[33m    Jan 1[39;49;00m
   303	[33m    Apr 4[39;49;00m
   304	[33m    Nov 11[39;49;00m
   305	[33m    Dec 12[39;49;00m
   306	[33m    Oct 10[39;49;00m
   307	[33m[39;49;00m
   308	Note that the order is essentially random, because it's based on the
   309	hash ordering of the objects in the dictionary.
   310
   311	Applying [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m to a dictionary always loops over the keys, but
   312	dictionaries have methods that return other iterators.  If you want to
   313	iterate over keys, values, or key/value pairs, you can explicitly call
   314	the [33m``[39;49;00m[33miterkeys()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mitervalues()[39;49;00m[33m``[39;49;00m, or [33m``[39;49;00m[33miteritems()[39;49;00m[33m``[39;49;00m methods to
   315	get an appropriate iterator.
   316
   317	The [33m``[39;49;00m[33mdict()[39;49;00m[33m``[39;49;00m constructor can accept an iterator that returns a
   318	finite stream of [33m``[39;49;00m[33m(key, value)[39;49;00m[33m``[39;49;00m tuples[33m::[39;49;00m
   319
   320	[33m    [39;49;00m[33m>>> L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')][39;49;00m
   321	[33m    >>> dict(iter(L))[39;49;00m
   322	[33m    {'Italy': 'Rome', 'US': 'Washington DC', 'France': 'Paris'}[39;49;00m
   323	[33m[39;49;00m
   324	Files also support iteration by calling the [33m``[39;49;00m[33mreadline()[39;49;00m[33m``[39;49;00m
   325	method until there are no more lines in the file.  This means you can
   326	read each line of a file like this[33m::[39;49;00m
   327
   328	[33m    [39;49;00m[33mfor line in file:[39;49;00m
   329	[33m        # do something for each line[39;49;00m
   330	[33m        ...[39;49;00m
   331	[33m[39;49;00m
   332	Sets can take their contents from an iterable and let you iterate over
   333	the set's elements[33m::[39;49;00m
   334
   335	[33m    [39;49;00m[33mS = set((2, 3, 5, 7, 11, 13))[39;49;00m
   336	[33m    for i in S:[39;49;00m
   337	[33m        print i[39;49;00m
   338	[33m[39;49;00m
   339	[33m[39;49;00m
   340	[33m[39;49;00m
   341	[01mGenerator expressions and list comprehensions[39;49;00m
   342	[01m----------------------------------------------------[39;49;00m
   343
   344	Two common operations on an iterator's output are 1) performing some
   345	operation for every element, 2) selecting a subset of elements that
   346	meet some condition.  For example, given a list of strings, you might
   347	want to strip off trailing whitespace from each line or extract all
   348	the strings containing a given substring.
   349
   350	List comprehensions and generator expressions (short form: "listcomps"
   351	and "genexps") are a concise notation for such operations, borrowed
   352	from the functional programming language Haskell
   353	(http://www.haskell.org).  You can strip all the whitespace from a
   354	stream of strings with the following code[33m::[39;49;00m
   355
   356	[33m        [39;49;00m[33mline_list = ['  line 1\n', 'line 2  \n', ...][39;49;00m
   357	[33m[39;49;00m
   358	[33m        # Generator expression -- returns iterator[39;49;00m
   359	[33m        stripped_iter = (line.strip() for line in line_list)[39;49;00m
   360	[33m[39;49;00m
   361	[33m        # List comprehension -- returns list[39;49;00m
   362	[33m        stripped_list = [line.strip() for line in line_list][39;49;00m
   363	[33m[39;49;00m
   364	You can select only certain elements by adding an [33m``[39;49;00m[33m"if"[39;49;00m[33m``[39;49;00m condition[33m::[39;49;00m
   365
   366	[33m        [39;49;00m[33mstripped_list = [line.strip() for line in line_list[39;49;00m
   367	[33m                         if line != ""][39;49;00m
   368	[33m[39;49;00m
   369	With a list comprehension, you get back a Python list;
   370	[33m``[39;49;00m[33mstripped_list[39;49;00m[33m``[39;49;00m is a list containing the resulting lines, not an
   371	iterator.  Generator expressions return an iterator that computes the
   372	values as necessary, not needing to materialize all the values at
   373	once.  This means that list comprehensions aren't useful if you're
   374	working with iterators that return an infinite stream or a very large
   375	amount of data.  Generator expressions are preferable in these
   376	situations.
   377
   378	Generator expressions are surrounded by parentheses ("()") and list
   379	comprehensions are surrounded by square brackets ("[]").  Generator
   380	expressions have the form[33m::[39;49;00m
   381
   382	[33m    [39;49;00m[33m( expression for expr in sequence1 [39;49;00m
   383	[33m                 if condition1[39;49;00m
   384	[33m                 for expr2 in sequence2[39;49;00m
   385	[33m                 if condition2[39;49;00m
   386	[33m                 for expr3 in sequence3 ...[39;49;00m
   387	[33m                 if condition3[39;49;00m
   388	[33m                 for exprN in sequenceN[39;49;00m
   389	[33m                 if conditionN )[39;49;00m
   390	[33m[39;49;00m
   391	Again, for a list comprehension only the outside brackets are
   392	different (square brackets instead of parentheses).
   393
   394	The elements of the generated output will be the successive values of
   395	[33m``[39;49;00m[33mexpression[39;49;00m[33m``[39;49;00m.  The [33m``[39;49;00m[33mif[39;49;00m[33m``[39;49;00m clauses are all optional; if present,
   396	[33m``[39;49;00m[33mexpression[39;49;00m[33m``[39;49;00m is only evaluated and added to the result when
   397	[33m``[39;49;00m[33mcondition[39;49;00m[33m``[39;49;00m is true.
   398
   399	Generator expressions always have to be written inside parentheses,
   400	but the parentheses signalling a function call also count.  If you
   401	want to create an iterator that will be immediately passed to a
   402	function you can write[33m::[39;49;00m
   403
   404	[33m        [39;49;00m[33mobj_total = sum(obj.count for obj in list_all_objects())[39;49;00m
   405	[33m[39;49;00m
   406	The [33m``[39;49;00m[33mfor...in[39;49;00m[33m``[39;49;00m clauses contain the sequences to be iterated over.
   407	The sequences do not have to be the same length, because they are
   408	iterated over from left to right, **not** in parallel.  For each
   409	element in [33m``[39;49;00m[33msequence1[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33msequence2[39;49;00m[33m``[39;49;00m is looped over from the
   410	beginning.  [33m``[39;49;00m[33msequence3[39;49;00m[33m``[39;49;00m  is then looped over for each
   411	resulting pair of elements from [33m``[39;49;00m[33msequence1[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33msequence2[39;49;00m[33m``[39;49;00m.
   412
   413	To put it another way, a list comprehension or generator expression is
   414	equivalent to the following Python code[33m::[39;49;00m
   415
   416	[33m    [39;49;00m[33mfor expr1 in sequence1:[39;49;00m
   417	[33m        if not (condition1):[39;49;00m
   418	[33m            continue   # Skip this element[39;49;00m
   419	[33m        for expr2 in sequence2:[39;49;00m
   420	[33m            if not (condition2):[39;49;00m
   421	[33m                continue    # Skip this element[39;49;00m
   422	[33m            ...[39;49;00m
   423	[33m            for exprN in sequenceN:[39;49;00m
   424	[33m                 if not (conditionN):[39;49;00m
   425	[33m                     continue   # Skip this element[39;49;00m
   426	[33m[39;49;00m
   427	[33m                 # Output the value of [39;49;00m
   428	[33m                 # the expression.[39;49;00m
   429	[33m[39;49;00m
   430	This means that when there are multiple [33m``[39;49;00m[33mfor...in[39;49;00m[33m``[39;49;00m clauses but no
   431	[33m``[39;49;00m[33mif[39;49;00m[33m``[39;49;00m clauses, the length of the resulting output will be equal to
   432	the product of the lengths of all the sequences.  If you have two
   433	lists of length 3, the output list is 9 elements long[33m::[39;49;00m
   434
   435	[33m    [39;49;00m[33mseq1 = 'abc'[39;49;00m
   436	[33m    seq2 = (1,2,3)[39;49;00m
   437	[33m    >>> [ (x,y) for x in seq1 for y in seq2][39;49;00m
   438	[33m    [('a', 1), ('a', 2), ('a', 3), [39;49;00m
   439	[33m     ('b', 1), ('b', 2), ('b', 3), [39;49;00m
   440	[33m     ('c', 1), ('c', 2), ('c', 3)][39;49;00m
   441	[33m[39;49;00m
   442	To avoid introducing an ambiguity into Python's grammar, if
   443	[33m``[39;49;00m[33mexpression[39;49;00m[33m``[39;49;00m is creating a tuple, it must be surrounded with
   444	parentheses.  The first list comprehension below is a syntax error,
   445	while the second one is correct[33m::[39;49;00m
   446
   447	[33m    [39;49;00m[33m# Syntax error[39;49;00m
   448	[33m    [ x,y for x in seq1 for y in seq2][39;49;00m
   449	[33m    # Correct[39;49;00m
   450	[33m    [ (x,y) for x in seq1 for y in seq2][39;49;00m
   451	[33m[39;49;00m
   452	[33m[39;49;00m
   453	[01mGenerators[39;49;00m
   454	[01m-----------------------[39;49;00m
   455
   456	Generators are a special class of functions that simplify the task of
   457	writing iterators.  Regular functions compute a value and return it,
   458	but generators return an iterator that returns a stream of values.
   459
   460	You're doubtless familiar with how regular function calls work in
   461	Python or C.  When you call a function, it gets a private namespace
   462	where its local variables are created.  When the function reaches a
   463	[33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m statement, the local variables are destroyed and the
   464	value is returned to the caller.  A later call to the same function
   465	creates a new private namespace and a fresh set of local
   466	variables. But, what if the local variables weren't thrown away on
   467	exiting a function?  What if you could later resume the function where
   468	it left off?  This is what generators provide; they can be thought of
   469	as resumable functions.
   470
   471	Here's the simplest example of a generator function[33m::[39;49;00m
   472
   473	[33m    [39;49;00m[33mdef generate_ints(N):[39;49;00m
   474	[33m        for i in range(N):[39;49;00m
   475	[33m            yield i[39;49;00m
   476	[33m[39;49;00m
   477	Any function containing a [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m keyword is a generator function;
   478	this is detected by Python's bytecode compiler which compiles the
   479	function specially as a result.
   480
   481	When you call a generator function, it doesn't return a single value;
   482	instead it returns a generator object that supports the iterator
   483	protocol.  On executing the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m expression, the generator
   484	outputs the value of [33m``[39;49;00m[33mi[39;49;00m[33m``[39;49;00m, similar to a [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m
   485	statement.  The big difference between [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m and a
   486	[33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m statement is that on reaching a [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m the
   487	generator's state of execution is suspended and local variables are
   488	preserved.  On the next call to the generator's [33m``[39;49;00m[33m.next()[39;49;00m[33m``[39;49;00m method,
   489	the function will resume executing.
   490
   491	Here's a sample usage of the [33m``[39;49;00m[33mgenerate_ints()[39;49;00m[33m``[39;49;00m generator[33m::[39;49;00m
   492
   493	[33m    [39;49;00m[33m>>> gen = generate_ints(3)[39;49;00m
   494	[33m    >>> gen[39;49;00m
   495	[33m    <generator object at 0x8117f90>[39;49;00m
   496	[33m    >>> gen.next()[39;49;00m
   497	[33m    0[39;49;00m
   498	[33m    >>> gen.next()[39;49;00m
   499	[33m    1[39;49;00m
   500	[33m    >>> gen.next()[39;49;00m
   501	[33m    2[39;49;00m
   502	[33m    >>> gen.next()[39;49;00m
   503	[33m    Traceback (most recent call last):[39;49;00m
   504	[33m      File "stdin", line 1, in ?[39;49;00m
   505	[33m      File "stdin", line 2, in generate_ints[39;49;00m
   506	[33m    StopIteration[39;49;00m
   507	[33m[39;49;00m
   508	You could equally write [33m``[39;49;00m[33mfor i in generate_ints(5)[39;49;00m[33m``[39;49;00m, or
   509	[33m``[39;49;00m[33ma,b,c = generate_ints(3)[39;49;00m[33m``[39;49;00m.
   510
   511	Inside a generator function, the [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m statement can only be used
   512	without a value, and signals the end of the procession of values;
   513	after executing a [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m the generator cannot return any further
   514	values.  [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m with a value, such as [33m``[39;49;00m[33mreturn 5[39;49;00m[33m``[39;49;00m, is a syntax
   515	error inside a generator function.  The end of the generator's results
   516	can also be indicated by raising [33m``[39;49;00m[33mStopIteration[39;49;00m[33m``[39;49;00m manually, or by
   517	just letting the flow of execution fall off the bottom of the
   518	function.
   519
   520	You could achieve the effect of generators manually by writing your
   521	own class and storing all the local variables of the generator as
   522	instance variables.  For example, returning a list of integers could
   523	be done by setting [33m``[39;49;00m[33mself.count[39;49;00m[33m``[39;49;00m to 0, and having the
   524	[33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m method increment [33m``[39;49;00m[33mself.count[39;49;00m[33m``[39;49;00m and return it.
   525	However, for a moderately complicated generator, writing a
   526	corresponding class can be much messier.
   527
   528	The test suite included with Python's library, [33m``[39;49;00m[33mtest_generators.py[39;49;00m[33m``[39;49;00m,
   529	contains a number of more interesting examples.  Here's one generator
   530	that implements an in-order traversal of a tree using generators
   531	recursively.
   532
   533	[33m::[39;49;00m
   534
   535	[33m    [39;49;00m[33m# A recursive generator that generates Tree leaves in in-order.[39;49;00m
   536	[33m    def inorder(t):[39;49;00m
   537	[33m        if t:[39;49;00m
   538	[33m            for x in inorder(t.left):[39;49;00m
   539	[33m                yield x[39;49;00m
   540	[33m[39;49;00m
   541	[33m            yield t.label[39;49;00m
   542	[33m[39;49;00m
   543	[33m            for x in inorder(t.right):[39;49;00m
   544	[33m                yield x[39;49;00m
   545	[33m[39;49;00m
   546	Two other examples in [33m``[39;49;00m[33mtest_generators.py[39;49;00m[33m``[39;49;00m produce
   547	solutions for the N-Queens problem (placing N queens on an NxN
   548	chess board so that no queen threatens another) and the Knight's Tour
   549	(finding a route that takes a knight to every square of an NxN chessboard
   550	without visiting any square twice).
   551
   552
   553
   554	[01mPassing values into a generator[39;49;00m
   555	[01m''''''''''''''''''''''''''''''''''''''''''''''[39;49;00m
   556
   557	In Python 2.4 and earlier, generators only produced output.  Once a
   558	generator's code was invoked to create an iterator, there was no way to
   559	pass any new information into the function when its execution is
   560	resumed.  You could hack together this ability by making the
   561	generator look at a global variable or by passing in some mutable object
   562	that callers then modify, but these approaches are messy.
   563
   564	In Python 2.5 there's a simple way to pass values into a generator.
   565	[33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m became an expression, returning a value that can be assigned
   566	to a variable or otherwise operated on[33m::[39;49;00m
   567
   568	[33m    [39;49;00m[33mval = (yield i)[39;49;00m
   569	[33m[39;49;00m
   570	I recommend that you **always** put parentheses around a [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m
   571	expression when you're doing something with the returned value, as in
   572	the above example.  The parentheses aren't always necessary, but it's
   573	easier to always add them instead of having to remember when they're
   574	needed.
   575
   576	(PEP 342 explains the exact rules, which are that a
   577	[33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m-expression must always be parenthesized except when it
   578	occurs at the top-level expression on the right-hand side of an
   579	assignment.  This means you can write [33m``[39;49;00m[33mval = yield i[39;49;00m[33m``[39;49;00m but have to
   580	use parentheses when there's an operation, as in [33m``[39;49;00m[33mval = (yield i)[39;49;00m
   581	[33m+ 12[39;49;00m[33m``[39;49;00m.)
   582
   583	Values are sent into a generator by calling its
   584	[33m``[39;49;00m[33msend(value)[39;49;00m[33m``[39;49;00m method.  This method resumes the
   585	generator's code and the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m expression returns the specified
   586	value.  If the regular [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m method is called, the
   587	[33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m returns [33m``[39;49;00m[33mNone[39;49;00m[33m``[39;49;00m.
   588
   589	Here's a simple counter that increments by 1 and allows changing the
   590	value of the internal counter.
   591
   592	[33m::[39;49;00m
   593
   594	[33m    [39;49;00m[33mdef counter (maximum):[39;49;00m
   595	[33m        i = 0[39;49;00m
   596	[33m        while i < maximum:[39;49;00m
   597	[33m            val = (yield i)[39;49;00m
   598	[33m            # If value provided, change counter[39;49;00m
   599	[33m            if val is not None:[39;49;00m
   600	[33m                i = val[39;49;00m
   601	[33m            else:[39;49;00m
   602	[33m                i += 1[39;49;00m
   603	[33m[39;49;00m
   604	And here's an example of changing the counter:
   605
   606	    >>> it = counter(10)
   607	    >>> print it.next()
   608	    0
   609	    >>> print it.next()
   610	    1
   611	    >>> print it.send(8)
   612	    8
   613	    >>> print it.next()
   614	    9
   615	    >>> print it.next()
   616	    Traceback (most recent call last):
   617	      File [33m``[39;49;00m[33mt.py'', line 15, in ?[39;49;00m
   618	[33m        print it.next()[39;49;00m
   619	[33m    StopIteration[39;49;00m
   620	[33m[39;49;00m
   621	[33mBecause [39;49;00m[33m`[39;49;00m[33m`[39;49;00m[33myield[39;49;00m[33m``[39;49;00m will often be returning [33m``[39;49;00m[33mNone[39;49;00m[33m``[39;49;00m, you
   622	should always check for this case.  Don't just use its value in
   623	expressions unless you're sure that the [33m``[39;49;00m[33msend()[39;49;00m[33m``[39;49;00m method
   624	will be the only method used resume your generator function.
   625
   626	In addition to [33m``[39;49;00m[33msend()[39;49;00m[33m``[39;49;00m, there are two other new methods on
   627	generators:
   628
   629	[34m*[39;49;00m [33m``[39;49;00m[33mthrow(type, value=None, traceback=None)[39;49;00m[33m``[39;49;00m is used to raise an exception inside the
   630	  generator; the exception is raised by the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m expression
   631	  where the generator's execution is paused.
   632
   633	[34m*[39;49;00m [33m``[39;49;00m[33mclose()[39;49;00m[33m``[39;49;00m raises a [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m
   634	  exception inside the generator to terminate the iteration.
   635	  On receiving this
   636	  exception, the generator's code must either raise
   637	  [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m or [33m``[39;49;00m[33mStopIteration[39;49;00m[33m``[39;49;00m; catching the
   638	  exception and doing anything else is illegal and will trigger
   639	  a [33m``[39;49;00m[33mRuntimeError[39;49;00m[33m``[39;49;00m.  [33m``[39;49;00m[33mclose()[39;49;00m[33m``[39;49;00m will also be called by
   640	  Python's garbage collector when the generator is garbage-collected.
   641
   642	  If you need to run cleanup code when a [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m occurs,
   643	  I suggest using a [33m``[39;49;00m[33mtry: ... finally:[39;49;00m[33m``[39;49;00m suite instead of
   644	  catching [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m.
   645
   646	The cumulative effect of these changes is to turn generators from
   647	one-way producers of information into both producers and consumers.
   648
   649	Generators also become **coroutines**, a more generalized form of
   650	subroutines.  Subroutines are entered at one point and exited at
   651	another point (the top of the function, and a [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m
   652	statement), but coroutines can be entered, exited, and resumed at
   653	many different points (the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m statements).
   654
   655
   656	[01mBuilt-in functions[39;49;00m
   657	[01m----------------------------------------------[39;49;00m
   658
   659	Let's look in more detail at built-in functions often used with iterators.
   660
   661	Two Python's built-in functions, [33m``[39;49;00m[33mmap()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfilter()[39;49;00m[33m``[39;49;00m, are
   662	somewhat obsolete; they duplicate the features of list comprehensions
   663	but return actual lists instead of iterators.
   664
   665	[33m``[39;49;00m[33mmap(f, iterA, iterB, ...)[39;49;00m[33m``[39;49;00m returns a list containing [33m``[39;49;00m[33mf(iterA[0],[39;49;00m
   666	[33miterB[0]), f(iterA[1], iterB[1]), f(iterA[2], iterB[2]), ...[39;49;00m[33m``[39;49;00m.
   667
   668	[33m::[39;49;00m
   669
   670	[33m    [39;49;00m[33mdef upper(s):[39;49;00m
   671	[33m        return s.upper()[39;49;00m
   672	[33m    map(upper, ['sentence', 'fragment']) =>[39;49;00m
   673	[33m      ['SENTENCE', 'FRAGMENT'][39;49;00m
   674	[33m[39;49;00m
   675	[33m    [upper(s) for s in ['sentence', 'fragment']] =>[39;49;00m
   676	[33m      ['SENTENCE', 'FRAGMENT'][39;49;00m
   677	[33m[39;49;00m
   678	As shown above, you can achieve the same effect with a list
   679	comprehension.  The [33m``[39;49;00m[33mitertools.imap()[39;49;00m[33m``[39;49;00m function does the same thing
   680	but can handle infinite iterators; it'll be discussed later, in the section on
   681	the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module.
   682
   683	[33m``[39;49;00m[33mfilter(predicate, iter)[39;49;00m[33m``[39;49;00m returns a list
   684	that contains all the sequence elements that meet a certain condition,
   685	and is similarly duplicated by list comprehensions.
   686	A **predicate** is a function that returns the truth value of
   687	some condition; for use with [33m``[39;49;00m[33mfilter()[39;49;00m[33m``[39;49;00m, the predicate must take a
   688	single value.
   689
   690	[33m::[39;49;00m
   691
   692	[33m    [39;49;00m[33mdef is_even(x):[39;49;00m
   693	[33m        return (x % 2) == 0[39;49;00m
   694	[33m[39;49;00m
   695	[33m    filter(is_even, range(10)) =>[39;49;00m
   696	[33m      [0, 2, 4, 6, 8][39;49;00m
   697	[33m[39;49;00m
   698	This can also be written as a list comprehension[33m::[39;49;00m
   699
   700	[33m    [39;49;00m[33m>>> [x for x in range(10) if is_even(x)][39;49;00m
   701	[33m    [0, 2, 4, 6, 8][39;49;00m
   702	[33m[39;49;00m
   703	[33m``[39;49;00m[33mfilter()[39;49;00m[33m``[39;49;00m also has a counterpart in the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module,
   704	[33m``[39;49;00m[33mitertools.ifilter()[39;49;00m[33m``[39;49;00m, that returns an iterator and
   705	can therefore handle infinite sequences just as [33m``[39;49;00m[33mitertools.imap()[39;49;00m[33m``[39;49;00m can.
   706
   707	[33m``[39;49;00m[33mreduce(func, iter, [initial_value])[39;49;00m[33m``[39;49;00m doesn't have a counterpart in
   708	the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module because it cumulatively performs an operation
   709	on all the iterable's elements and therefore can't be applied to
   710	infinite iterables.  [33m``[39;49;00m[33mfunc[39;49;00m[33m``[39;49;00m must be a function that takes two elements
   711	and returns a single value.  [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m takes the first two elements
   712	A and B returned by the iterator and calculates [33m``[39;49;00m[33mfunc(A, B)[39;49;00m[33m``[39;49;00m.  It
   713	then requests the third element, C, calculates [33m``[39;49;00m[33mfunc(func(A, B),[39;49;00m
   714	[33mC)[39;49;00m[33m``[39;49;00m, combines this result with the fourth element returned, and
   715	continues until the iterable is exhausted.  If the iterable returns no
   716	values at all, a [33m``[39;49;00m[33mTypeError[39;49;00m[33m``[39;49;00m exception is raised.  If the initial
   717	value is supplied, it's used as a starting point and
   718	[33m``[39;49;00m[33mfunc(initial_value, A)[39;49;00m[33m``[39;49;00m is the first calculation.
   719
   720	[33m::[39;49;00m
   721
   722	[33m    [39;49;00m[33mimport operator[39;49;00m
   723	[33m    reduce(operator.concat, ['A', 'BB', 'C']) =>[39;49;00m
   724	[33m      'ABBC'[39;49;00m
   725	[33m    reduce(operator.concat, []) =>[39;49;00m
   726	[33m      TypeError: reduce() of empty sequence with no initial value[39;49;00m
   727	[33m    reduce(operator.mul, [1,2,3], 1) =>[39;49;00m
   728	[33m      6[39;49;00m
   729	[33m    reduce(operator.mul, [], 1) =>[39;49;00m
   730	[33m      1[39;49;00m
   731	[33m[39;49;00m
   732	If you use [33m``[39;49;00m[33moperator.add[39;49;00m[33m``[39;49;00m with [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m, you'll add up all the
   733	elements of the iterable.  This case is so common that there's a special
   734	built-in called [33m``[39;49;00m[33msum()[39;49;00m[33m``[39;49;00m to compute it[33m::[39;49;00m
   735
   736	[33m    [39;49;00m[33mreduce(operator.add, [1,2,3,4], 0) =>[39;49;00m
   737	[33m      10[39;49;00m
   738	[33m    sum([1,2,3,4]) =>[39;49;00m
   739	[33m      10[39;49;00m
   740	[33m    sum([]) =>[39;49;00m
   741	[33m      0[39;49;00m
   742	[33m[39;49;00m
   743	For many uses of [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m, though, it can be clearer to just write
   744	the obvious [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m loop[33m::[39;49;00m
   745
   746	[33m    [39;49;00m[33m# Instead of:[39;49;00m
   747	[33m    product = reduce(operator.mul, [1,2,3], 1)[39;49;00m
   748	[33m[39;49;00m
   749	[33m    # You can write:[39;49;00m
   750	[33m    product = 1[39;49;00m
   751	[33m    for i in [1,2,3]:[39;49;00m
   752	[33m        product *= i[39;49;00m
   753	[33m[39;49;00m
   754	[33m[39;49;00m
   755	[33m``[39;49;00m[33menumerate(iter)[39;49;00m[33m``[39;49;00m counts off the elements in the iterable, returning
   756	2-tuples containing the count and each element.
   757
   758	[33m::[39;49;00m
   759
   760	[33m    [39;49;00m[33menumerate(['subject', 'verb', 'object']) =>[39;49;00m
   761	[33m      (0, 'subject'), (1, 'verb'), (2, 'object')[39;49;00m
   762	[33m[39;49;00m
   763	[33m``[39;49;00m[33menumerate()[39;49;00m[33m``[39;49;00m is often used when looping through a list
   764	and recording the indexes at which certain conditions are met[33m::[39;49;00m
   765
   766	[33m    [39;49;00m[33mf = open('data.txt', 'r')[39;49;00m
   767	[33m    for i, line in enumerate(f):[39;49;00m
   768	[33m        if line.strip() == '':[39;49;00m
   769	[33m            print 'Blank line at line #%i' % i[39;49;00m
   770	[33m[39;49;00m
   771	[33m``[39;49;00m[33msorted(iterable, [cmp=None], [key=None], [reverse=False)[39;49;00m[33m``[39;49;00m
   772	collects all the elements of the iterable into a list, sorts
   773	the list, and returns the sorted result.  The [33m``[39;49;00m[33mcmp[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mkey[39;49;00m[33m``[39;49;00m,
   774	and [33m``[39;49;00m[33mreverse[39;49;00m[33m``[39;49;00m arguments are passed through to the
   775	constructed list's [33m``[39;49;00m[33m.sort()[39;49;00m[33m``[39;49;00m method.
   776
   777	[33m::[39;49;00m
   778
   779	[33m    [39;49;00m[33mimport random[39;49;00m
   780	[33m    # Generate 8 random numbers between [0, 10000)[39;49;00m
   781	[33m    rand_list = random.sample(range(10000), 8)[39;49;00m
   782	[33m    rand_list =>[39;49;00m
   783	[33m      [769, 7953, 9828, 6431, 8442, 9878, 6213, 2207][39;49;00m
   784	[33m    sorted(rand_list) =>[39;49;00m
   785	[33m      [769, 2207, 6213, 6431, 7953, 8442, 9828, 9878][39;49;00m
   786	[33m    sorted(rand_list, reverse=True) =>[39;49;00m
   787	[33m      [9878, 9828, 8442, 7953, 6431, 6213, 2207, 769][39;49;00m
   788	[33m[39;49;00m
   789	(For a more detailed discussion of sorting, see the Sorting mini-HOWTO
   790	in the Python wiki at http://wiki.python.org/moin/HowTo/Sorting.)
   791
   792	The [33m``[39;49;00m[33many(iter)[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mall(iter)[39;49;00m[33m``[39;49;00m built-ins look at
   793	the truth values of an iterable's contents.  [33m``[39;49;00m[33many()[39;49;00m[33m``[39;49;00m returns
   794	True if any element in the iterable is a true value, and [33m``[39;49;00m[33mall()[39;49;00m[33m``[39;49;00m
   795	returns True if all of the elements are true values[33m::[39;49;00m
   796
   797	[33m    [39;49;00m[33many([0,1,0]) =>[39;49;00m
   798	[33m      True[39;49;00m
   799	[33m    any([0,0,0]) =>[39;49;00m
   800	[33m      False[39;49;00m
   801	[33m    any([1,1,1]) =>[39;49;00m
   802	[33m      True[39;49;00m
   803	[33m    all([0,1,0]) =>[39;49;00m
   804	[33m      False[39;49;00m
   805	[33m    all([0,0,0]) => [39;49;00m
   806	[33m      False[39;49;00m
   807	[33m    all([1,1,1]) =>[39;49;00m
   808	[33m      True[39;49;00m
   809	[33m[39;49;00m
   810	[33m[39;49;00m
   811	[01mSmall functions and the lambda statement[39;49;00m
   812	[01m----------------------------------------------[39;49;00m
   813
   814	When writing functional-style programs, you'll often need little
   815	functions that act as predicates or that combine elements in some way.
   816
   817	If there's a Python built-in or a module function that's suitable, you
   818	don't need to define a new function at all[33m::[39;49;00m
   819
   820	[33m        [39;49;00m[33mstripped_lines = [line.strip() for line in lines][39;49;00m
   821	[33m        existing_files = filter(os.path.exists, file_list)[39;49;00m
   822	[33m[39;49;00m
   823	If the function you need doesn't exist, you need to write it.  One way
   824	to write small functions is to use the [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m statement.  [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m
   825	takes a number of parameters and an expression combining these parameters,
   826	and creates a small function that returns the value of the expression[33m::[39;49;00m
   827
   828	[33m        [39;49;00m[33mlowercase = lambda x: x.lower()[39;49;00m
   829	[33m[39;49;00m
   830	[33m        print_assign = lambda name, value: name + '=' + str(value)[39;49;00m
   831	[33m[39;49;00m
   832	[33m        adder = lambda x, y: x+y[39;49;00m
   833	[33m[39;49;00m
   834	An alternative is to just use the [33m``[39;49;00m[33mdef[39;49;00m[33m``[39;49;00m statement and define a
   835	function in the usual way[33m::[39;49;00m
   836
   837	[33m        [39;49;00m[33mdef lowercase(x):[39;49;00m
   838	[33m            return x.lower()[39;49;00m
   839	[33m[39;49;00m
   840	[33m        def print_assign(name, value):[39;49;00m
   841	[33m            return name + '=' + str(value)[39;49;00m
   842	[33m[39;49;00m
   843	[33m        def adder(x,y):[39;49;00m
   844	[33m            return x + y[39;49;00m
   845	[33m[39;49;00m
   846	Which alternative is preferable?  That's a style question; my usual
   847	course is to avoid using [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m.
   848
   849	One reason for my preference is that [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m is quite limited in
   850	the functions it can define.  The result has to be computable as a
   851	single expression, which means you can't have multiway
   852	[33m``[39;49;00m[33mif... elif... else[39;49;00m[33m``[39;49;00m comparisons or [33m``[39;49;00m[33mtry... except[39;49;00m[33m``[39;49;00m statements.
   853	If you try to do too much in a [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m statement, you'll end up
   854	with an overly complicated expression that's hard to read.  Quick,
   855	what's the following code doing?
   856
   857	[33m::[39;49;00m
   858
   859	[33m    [39;49;00m[33mtotal = reduce(lambda a, b: (0, a[1] + b[1]), items)[1][39;49;00m
   860	[33m[39;49;00m
   861	You can figure it out, but it takes time to disentangle the expression
   862	to figure out what's going on.  Using a short nested
   863	[33m``[39;49;00m[33mdef[39;49;00m[33m``[39;49;00m statements makes things a little bit better[33m::[39;49;00m
   864
   865	[33m    [39;49;00m[33mdef combine (a, b):[39;49;00m
   866	[33m        return 0, a[1] + b[1][39;49;00m
   867	[33m[39;49;00m
   868	[33m    total = reduce(combine, items)[1][39;49;00m
   869	[33m[39;49;00m
   870	But it would be best of all if I had simply used a [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m loop[33m::[39;49;00m
   871
   872	[33m     [39;49;00m[33mtotal = 0[39;49;00m
   873	[33m     for a, b in items:[39;49;00m
   874	[33m         total += b[39;49;00m
   875	[33m[39;49;00m
   876	Or the [33m``[39;49;00m[33msum()[39;49;00m[33m``[39;49;00m built-in and a generator expression[33m::[39;49;00m
   877
   878	[33m     [39;49;00m[33mtotal = sum(b for a,b in items)[39;49;00m
   879	[33m[39;49;00m
   880	Many uses of [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m are clearer when written as [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m loops.
   881
   882	Fredrik Lundh once suggested the following set of rules for refactoring
   883	uses of [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m:
   884
   885	[34m1)[39;49;00m Write a lambda function.
   886	[34m2)[39;49;00m Write a comment explaining what the heck that lambda does.
   887	[34m3)[39;49;00m Study the comment for a while, and think of a name that captures
   888	   the essence of the comment.
   889	[34m4)[39;49;00m Convert the lambda to a def statement, using that name.
   890	[34m5)[39;49;00m Remove the comment.
   891
   892	I really like these rules, but you're free to disagree that this
   893	lambda-free style is better.
   894
   895
   896	[01mThe itertools module[39;49;00m
   897	[01m-----------------------[39;49;00m
   898
   899	The [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module contains a number of commonly-used iterators
   900	as well as functions for combining several iterators.  This section
   901	will introduce the module's contents by showing small examples.
   902
   903	The module's functions fall into a few broad classes:
   904
   905	[34m*[39;49;00m Functions that create a new iterator based on an existing iterator.
   906	[34m*[39;49;00m Functions for treating an iterator's elements as function arguments.
   907	[34m*[39;49;00m Functions for selecting portions of an iterator's output.
   908	[34m*[39;49;00m A function for grouping an iterator's output.
   909
   910	[01mCreating new iterators[39;49;00m
   911	[01m''''''''''''''''''''''[39;49;00m
   912
   913	[33m``[39;49;00m[33mitertools.count(n)[39;49;00m[33m``[39;49;00m returns an infinite stream of
   914	integers, increasing by 1 each time.  You can optionally supply the
   915	starting number, which defaults to 0[33m::[39;49;00m
   916
   917	[33m        [39;49;00m[33mitertools.count() =>[39;49;00m
   918	[33m          0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...[39;49;00m
   919	[33m        itertools.count(10) =>[39;49;00m
   920	[33m          10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...[39;49;00m
   921	[33m[39;49;00m
   922	[33m``[39;49;00m[33mitertools.cycle(iter)[39;49;00m[33m``[39;49;00m saves a copy of the contents of a provided
   923	iterable and returns a new iterator that returns its elements from
   924	first to last.  The new iterator will repeat these elements infinitely.
   925
   926	[33m::[39;49;00m
   927
   928	[33m        [39;49;00m[33mitertools.cycle([1,2,3,4,5]) =>[39;49;00m
   929	[33m          1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...[39;49;00m
   930	[33m[39;49;00m
   931	[33m``[39;49;00m[33mitertools.repeat(elem, [n])[39;49;00m[33m``[39;49;00m returns the provided element [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m
   932	times, or returns the element endlessly if [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m is not provided.
   933
   934	[33m::[39;49;00m
   935
   936	[33m    [39;49;00m[33mitertools.repeat('abc') =>[39;49;00m
   937	[33m      abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, ...[39;49;00m
   938	[33m    itertools.repeat('abc', 5) =>[39;49;00m
   939	[33m      abc, abc, abc, abc, abc[39;49;00m
   940	[33m[39;49;00m
   941	[33m``[39;49;00m[33mitertools.chain(iterA, iterB, ...)[39;49;00m[33m``[39;49;00m takes an arbitrary number of
   942	iterables as input, and returns all the elements of the first
   943	iterator, then all the elements of the second, and so on, until all of
   944	the iterables have been exhausted.
   945
   946	[33m::[39;49;00m
   947
   948	[33m    [39;49;00m[33mitertools.chain(['a', 'b', 'c'], (1, 2, 3)) =>[39;49;00m
   949	[33m      a, b, c, 1, 2, 3[39;49;00m
   950	[33m[39;49;00m
   951	[33m``[39;49;00m[33mitertools.izip(iterA, iterB, ...)[39;49;00m[33m``[39;49;00m takes one element from each iterable
   952	and returns them in a tuple[33m::[39;49;00m
   953
   954	[33m    [39;49;00m[33mitertools.izip(['a', 'b', 'c'], (1, 2, 3)) =>[39;49;00m
   955	[33m      ('a', 1), ('b', 2), ('c', 3)[39;49;00m
   956	[33m[39;49;00m
   957	It's similiar to the built-in [33m``[39;49;00m[33mzip()[39;49;00m[33m``[39;49;00m function, but doesn't
   958	construct an in-memory list and exhaust all the input iterators before
   959	returning; instead tuples are constructed and returned only if they're
   960	requested.  (The technical term for this behaviour is
   961	[33m`lazy evaluation [39;49;00m[33m<http://en.wikipedia.org/wiki/Lazy_evaluation>[39;49;00m[33m`__[39;49;00m.)
   962
   963	This iterator is intended to be used with iterables that are all of
   964	the same length.  If the iterables are of different lengths, the
   965	resulting stream will be the same length as the shortest iterable.
   966
   967	[33m::[39;49;00m
   968
   969	[33m    [39;49;00m[33mitertools.izip(['a', 'b'], (1, 2, 3)) =>[39;49;00m
   970	[33m      ('a', 1), ('b', 2)[39;49;00m
   971	[33m[39;49;00m
   972	You should avoid doing this, though, because an element may be taken
   973	from the longer iterators and discarded.  This means you can't go on
   974	to use the iterators further because you risk skipping a discarded
   975	element.
   976
   977	[33m``[39;49;00m[33mitertools.islice(iter, [start], stop, [step])[39;49;00m[33m``[39;49;00m returns a stream
   978	that's a slice of the iterator.  With a single [33m``[39;49;00m[33mstop[39;49;00m[33m``[39;49;00m argument,
   979	it will return the first [33m``[39;49;00m[33mstop[39;49;00m[33m``[39;49;00m
   980	elements.  If you supply a starting index, you'll get [33m``[39;49;00m[33mstop-start[39;49;00m[33m``[39;49;00m
   981	elements, and if you supply a value for [33m``[39;49;00m[33mstep[39;49;00m[33m``[39;49;00m, elements will be
   982	skipped accordingly.  Unlike Python's string and list slicing, you
   983	can't use negative values for [33m``[39;49;00m[33mstart[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mstop[39;49;00m[33m``[39;49;00m, or [33m``[39;49;00m[33mstep[39;49;00m[33m``[39;49;00m.
   984
   985	[33m::[39;49;00m
   986
   987	[33m    [39;49;00m[33mitertools.islice(range(10), 8) =>[39;49;00m
   988	[33m      0, 1, 2, 3, 4, 5, 6, 7[39;49;00m
   989	[33m    itertools.islice(range(10), 2, 8) =>[39;49;00m
   990	[33m      2, 3, 4, 5, 6, 7[39;49;00m
   991	[33m    itertools.islice(range(10), 2, 8, 2) =>[39;49;00m
   992	[33m      2, 4, 6[39;49;00m
   993	[33m[39;49;00m
   994	[33m``[39;49;00m[33mitertools.tee(iter, [n])[39;49;00m[33m``[39;49;00m replicates an iterator; it returns [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m
   995	independent iterators that will all return the contents of the source
   996	iterator.  If you don't supply a value for [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m, the default is 2.
   997	Replicating iterators requires saving some of the contents of the source
   998	iterator, so this can consume significant memory if the iterator is large
   999	and one of the new iterators is consumed more than the others.
  1000
  1001	[33m::[39;49;00m
  1002
  1003	[33m        [39;49;00m[33mitertools.tee( itertools.count() ) =>[39;49;00m
  1004	[33m           iterA, iterB[39;49;00m
  1005	[33m[39;49;00m
  1006	[33m        where iterA ->[39;49;00m
  1007	[33m           0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...[39;49;00m
  1008	[33m[39;49;00m
  1009	[33m        and   iterB ->[39;49;00m
  1010	[33m           0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...[39;49;00m
  1011	[33m[39;49;00m
  1012	[33m[39;49;00m
  1013	[01mCalling functions on elements[39;49;00m
  1014	[01m'''''''''''''''''''''''''''''[39;49;00m
  1015
  1016	Two functions are used for calling other functions on the contents of an
  1017	iterable.
  1018
  1019	[33m``[39;49;00m[33mitertools.imap(f, iterA, iterB, ...)[39;49;00m[33m``[39;49;00m returns
  1020	a stream containing [33m``[39;49;00m[33mf(iterA[0], iterB[0]), f(iterA[1], iterB[1]),[39;49;00m
  1021	[33mf(iterA[2], iterB[2]), ...[39;49;00m[33m``[39;49;00m[33m::[39;49;00m
  1022
  1023	[33m    [39;49;00m[33mitertools.imap(operator.add, [5, 6, 5], [1, 2, 3]) =>[39;49;00m
  1024	[33m      6, 8, 8[39;49;00m
  1025	[33m[39;49;00m
  1026	The [33m``[39;49;00m[33moperator[39;49;00m[33m``[39;49;00m module contains a set of functions
  1027	corresponding to Python's operators.  Some examples are
  1028	[33m``[39;49;00m[33moperator.add(a, b)[39;49;00m[33m``[39;49;00m (adds two values),
  1029	[33m``[39;49;00m[33moperator.ne(a, b)[39;49;00m[33m``[39;49;00m (same as [33m``[39;49;00m[33ma!=b[39;49;00m[33m``[39;49;00m),
  1030	and
  1031	[33m``[39;49;00m[33moperator.attrgetter('id')[39;49;00m[33m``[39;49;00m (returns a callable that
  1032	fetches the [33m``[39;49;00m[33m"id"[39;49;00m[33m``[39;49;00m attribute).
  1033
  1034	[33m``[39;49;00m[33mitertools.starmap(func, iter)[39;49;00m[33m``[39;49;00m assumes that the iterable will
  1035	return a stream of tuples, and calls [33m``[39;49;00m[33mf()[39;49;00m[33m``[39;49;00m using these tuples as the
  1036	arguments[33m::[39;49;00m
  1037
  1038	[33m    [39;49;00m[33mitertools.starmap(os.path.join, [39;49;00m
  1039	[33m                      [('/usr', 'bin', 'java'), ('/bin', 'python'),[39;49;00m
  1040	[33m                       ('/usr', 'bin', 'perl'),('/usr', 'bin', 'ruby')])[39;49;00m
  1041	[33m    =>[39;49;00m
  1042	[33m      /usr/bin/java, /bin/python, /usr/bin/perl, /usr/bin/ruby[39;49;00m
  1043	[33m[39;49;00m
  1044	[33m[39;49;00m
  1045	[01mSelecting elements[39;49;00m
  1046	[01m''''''''''''''''''[39;49;00m
  1047
  1048	Another group of functions chooses a subset of an iterator's elements
  1049	based on a predicate.
  1050
  1051	[33m``[39;49;00m[33mitertools.ifilter(predicate, iter)[39;49;00m[33m``[39;49;00m returns all the elements for
  1052	which the predicate returns true[33m::[39;49;00m
  1053
  1054	[33m    [39;49;00m[33mdef is_even(x):[39;49;00m
  1055	[33m        return (x % 2) == 0[39;49;00m
  1056	[33m[39;49;00m
  1057	[33m    itertools.ifilter(is_even, itertools.count()) =>[39;49;00m
  1058	[33m      0, 2, 4, 6, 8, 10, 12, 14, ...[39;49;00m
  1059	[33m[39;49;00m
  1060	[33m``[39;49;00m[33mitertools.ifilterfalse(predicate, iter)[39;49;00m[33m``[39;49;00m is the opposite,
  1061	returning all elements for which the predicate returns false[33m::[39;49;00m
  1062
  1063	[33m    [39;49;00m[33mitertools.ifilterfalse(is_even, itertools.count()) =>[39;49;00m
  1064	[33m      1, 3, 5, 7, 9, 11, 13, 15, ...[39;49;00m
  1065	[33m[39;49;00m
  1066	[33m``[39;49;00m[33mitertools.takewhile(predicate, iter)[39;49;00m[33m``[39;49;00m returns elements for as long
  1067	as the predicate returns true.  Once the predicate returns false,
  1068	the iterator will signal the end of its results.
  1069
  1070	[33m::[39;49;00m
  1071
  1072	[33m    [39;49;00m[33mdef less_than_10(x):[39;49;00m
  1073	[33m        return (x < 10)[39;49;00m
  1074	[33m[39;49;00m
  1075	[33m    itertools.takewhile(less_than_10, itertools.count()) =>[39;49;00m
  1076	[33m      0, 1, 2, 3, 4, 5, 6, 7, 8, 9[39;49;00m
  1077	[33m[39;49;00m
  1078	[33m    itertools.takewhile(is_even, itertools.count()) =>[39;49;00m
  1079	[33m      0[39;49;00m
  1080	[33m[39;49;00m
  1081	[33m``[39;49;00m[33mitertools.dropwhile(predicate, iter)[39;49;00m[33m``[39;49;00m discards elements while the
  1082	predicate returns true, and then returns the rest of the iterable's
  1083	results.
  1084
  1085	[33m::[39;49;00m
  1086
  1087	[33m    [39;49;00m[33mitertools.dropwhile(less_than_10, itertools.count()) =>[39;49;00m
  1088	[33m      10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...[39;49;00m
  1089	[33m[39;49;00m
  1090	[33m    itertools.dropwhile(is_even, itertools.count()) =>[39;49;00m
  1091	[33m      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...[39;49;00m
  1092	[33m[39;49;00m
  1093	[33m[39;49;00m
  1094	[01mGrouping elements[39;49;00m
  1095	[01m'''''''''''''''''[39;49;00m
  1096
  1097	The last function I'll discuss, [33m``[39;49;00m[33mitertools.groupby(iter,[39;49;00m
  1098	[33mkey_func=None)[39;49;00m[33m``[39;49;00m, is the most complicated.  [33m``[39;49;00m[33mkey_func(elem)[39;49;00m[33m``[39;49;00m is a
  1099	function that can compute a key value for each element returned by the
  1100	iterable.  If you don't supply a key function, the key is simply each
  1101	element itself.
  1102
  1103	[33m``[39;49;00m[33mgroupby()[39;49;00m[33m``[39;49;00m collects all the consecutive elements from the
  1104	underlying iterable that have the same key value, and returns a stream
  1105	of 2-tuples containing a key value and an iterator for the elements
  1106	with that key.
  1107
  1108	[33m::[39;49;00m
  1109
  1110	[33m    [39;49;00m[33mcity_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'), [39;49;00m
  1111	[33m                 ('Anchorage', 'AK'), ('Nome', 'AK'),[39;49;00m
  1112	[33m                 ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'), [39;49;00m
  1113	[33m                 ...[39;49;00m
  1114	[33m                ][39;49;00m
  1115	[33m[39;49;00m
  1116	[33m    def get_state ((city, state)):[39;49;00m
  1117	[33m        return state[39;49;00m
  1118	[33m[39;49;00m
  1119	[33m    itertools.groupby(city_list, get_state) =>[39;49;00m
  1120	[33m      ('AL', iterator-1),[39;49;00m
  1121	[33m      ('AK', iterator-2),[39;49;00m
  1122	[33m      ('AZ', iterator-3), ...[39;49;00m
  1123	[33m[39;49;00m
  1124	[33m    where[39;49;00m
  1125	[33m    iterator-1 =>[39;49;00m
  1126	[33m      ('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')[39;49;00m
  1127	[33m    iterator-2 => [39;49;00m
  1128	[33m      ('Anchorage', 'AK'), ('Nome', 'AK')[39;49;00m
  1129	[33m    iterator-3 =>[39;49;00m
  1130	[33m      ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')[39;49;00m
  1131	[33m[39;49;00m
  1132	[33m``[39;49;00m[33mgroupby()[39;49;00m[33m``[39;49;00m assumes that the underlying iterable's contents will
  1133	already be sorted based on the key.  Note that the returned iterators
  1134	also use the underlying iterable, so you have to consume the results
  1135	of iterator-1 before requesting iterator-2 and its corresponding key.
  1136
  1137
  1138	[01mThe functools module[39;49;00m
  1139	[01m----------------------------------------------[39;49;00m
  1140
  1141	The [33m``[39;49;00m[33mfunctools[39;49;00m[33m``[39;49;00m module in Python 2.5 contains some higher-order
  1142	functions.  A **higher-order function** takes one or more functions as
  1143	input and returns a new function.  The most useful tool in this module
  1144	is the [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m function.
  1145
  1146	For programs written in a functional style, you'll sometimes want to
  1147	construct variants of existing functions that have some of the
  1148	parameters filled in.  Consider a Python function [33m``[39;49;00m[33mf(a, b, c)[39;49;00m[33m``[39;49;00m; you
  1149	may wish to create a new function [33m``[39;49;00m[33mg(b, c)[39;49;00m[33m``[39;49;00m that's equivalent to
  1150	[33m``[39;49;00m[33mf(1, b, c)[39;49;00m[33m``[39;49;00m; you're filling in a value for one of [33m``[39;49;00m[33mf()[39;49;00m[33m``[39;49;00m's parameters.
  1151	This is called "partial function application".
  1152
  1153	The constructor for [33m``[39;49;00m[33mpartial[39;49;00m[33m``[39;49;00m takes the arguments [33m``[39;49;00m[33m(function, arg1,[39;49;00m
  1154	[33marg2, ... kwarg1=value1, kwarg2=value2)[39;49;00m[33m``[39;49;00m.  The resulting object is
  1155	callable, so you can just call it to invoke [33m``[39;49;00m[33mfunction[39;49;00m[33m``[39;49;00m with the
  1156	filled-in arguments.
  1157
  1158	Here's a small but realistic example[33m::[39;49;00m
  1159
  1160	[33m    [39;49;00m[33mimport functools[39;49;00m
  1161	[33m[39;49;00m
  1162	[33m    def log (message, subsystem):[39;49;00m
  1163	[33m        "Write the contents of 'message' to the specified subsystem."[39;49;00m
  1164	[33m        print '%s: %s' % (subsystem, message)[39;49;00m
  1165	[33m        ...[39;49;00m
  1166	[33m[39;49;00m
  1167	[33m    server_log = functools.partial(log, subsystem='server')[39;49;00m
  1168	[33m    server_log('Unable to open socket')[39;49;00m
  1169	[33m[39;49;00m
  1170	[33m[39;49;00m
  1171	[01mThe operator module[39;49;00m
  1172	[01m-------------------[39;49;00m
  1173
  1174	The [33m``[39;49;00m[33moperator[39;49;00m[33m``[39;49;00m module was mentioned earlier.  It contains a set of
  1175	functions corresponding to Python's operators.  These functions
  1176	are often useful in functional-style code because they save you
  1177	from writing trivial functions that perform a single operation.
  1178
  1179	Some of the functions in this module are:
  1180
  1181	[34m*[39;49;00m Math operations: [33m``[39;49;00m[33madd()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33msub()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mmul()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mdiv()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mfloordiv()[39;49;00m[33m``[39;49;00m,
  1182	  [33m``[39;49;00m[33mabs()[39;49;00m[33m``[39;49;00m, ...
  1183	[34m*[39;49;00m Logical operations: [33m``[39;49;00m[33mnot_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mtruth()[39;49;00m[33m``[39;49;00m.
  1184	[34m*[39;49;00m Bitwise operations: [33m``[39;49;00m[33mand_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mor_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33minvert()[39;49;00m[33m``[39;49;00m.
  1185	[34m*[39;49;00m Comparisons: [33m``[39;49;00m[33meq()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mne()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mlt()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mle()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mgt()[39;49;00m[33m``[39;49;00m, and [33m``[39;49;00m[33mge()[39;49;00m[33m``[39;49;00m.
  1186	[34m*[39;49;00m Object identity: [33m``[39;49;00m[33mis_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mis_not()[39;49;00m[33m``[39;49;00m.
  1187
  1188	Consult [33m`the operator module's documentation [39;49;00m[33m<http://docs.python.org/lib/module-operator.html>[39;49;00m[33m`__[39;49;00m for a complete
  1189	list.
  1190
  1191
  1192
  1193	[01mThe functional module[39;49;00m
  1194	[01m---------------------[39;49;00m
  1195
  1196	Collin Winter's [33m`functional module [39;49;00m[33m<http://oakwinter.com/code/functional/>[39;49;00m[33m`__[39;49;00m
  1197	provides a number of more
  1198	advanced tools for functional programming. It also reimplements
  1199	several Python built-ins, trying to make them more intuitive to those
  1200	used to functional programming in other languages.
  1201
  1202	This section contains an introduction to some of the most important
  1203	functions in [33m``[39;49;00m[33mfunctional[39;49;00m[33m``[39;49;00m; full documentation can be found at `the
  1204	project's website <http://oakwinter.com/code/functional/documentation/>`__.
  1205
  1206	[33m``[39;49;00m[33mcompose(outer, inner, unpack=False)[39;49;00m[33m``[39;49;00m
  1207
  1208	The [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m function implements function composition.
  1209	In other words, it returns a wrapper around the [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m callables, such
  1210	that the return value from [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m is fed directly to [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m.  That is,
  1211
  1212	[33m::[39;49;00m
  1213
  1214	[33m        [39;49;00m[33m>>> def add(a, b):[39;49;00m
  1215	[33m        ...     return a + b[39;49;00m
  1216	[33m        ...[39;49;00m
  1217	[33m        >>> def double(a):[39;49;00m
  1218	[33m        ...     return 2 * a[39;49;00m
  1219	[33m        ...[39;49;00m
  1220	[33m        >>> compose(double, add)(5, 6)[39;49;00m
  1221	[33m        22[39;49;00m
  1222	[33m[39;49;00m
  1223	is equivalent to
  1224
  1225	[33m::[39;49;00m
  1226
  1227	[33m        [39;49;00m[33m>>> double(add(5, 6))[39;49;00m
  1228	[33m        22[39;49;00m
  1229	[33m                    [39;49;00m
  1230	The [33m``[39;49;00m[33munpack[39;49;00m[33m``[39;49;00m keyword is provided to work around the fact that Python functions are not always
  1231	[33m`fully curried [39;49;00m[33m<http://en.wikipedia.org/wiki/Currying>[39;49;00m[33m`__[39;49;00m.
  1232	By default, it is expected that the [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m function will return a single object and that the [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m
  1233	function will take a single argument. Setting the [33m``[39;49;00m[33munpack[39;49;00m[33m``[39;49;00m argument causes [33m``[39;49;00m[33mcompose[39;49;00m[33m``[39;49;00m to expect a
  1234	tuple from [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m which will be expanded before being passed to [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m. Put simply,
  1235
  1236	[33m::[39;49;00m
  1237
  1238	[33m        [39;49;00m[33mcompose(f, g)(5, 6)[39;49;00m
  1239	[33m                    [39;49;00m
  1240	is equivalent to[33m::[39;49;00m
  1241
  1242	[33m        [39;49;00m[33mf(g(5, 6))[39;49;00m
  1243	[33m                    [39;49;00m
  1244	while
  1245
  1246	[33m::[39;49;00m
  1247
  1248	[33m        [39;49;00m[33mcompose(f, g, unpack=True)(5, 6)[39;49;00m
  1249	[33m                    [39;49;00m
  1250	is equivalent to[33m::[39;49;00m
  1251
  1252	[33m        [39;49;00m[33mf(*g(5, 6))[39;49;00m
  1253	[33m[39;49;00m
  1254	Even though [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m only accepts two functions, it's trivial to
  1255	build up a version that will compose any number of functions. We'll
  1256	use [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m (the last of which
  1257	is provided by both [33m``[39;49;00m[33mfunctional[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfunctools[39;49;00m[33m``[39;49;00m).
  1258
  1259	[33m::[39;49;00m
  1260
  1261	[33m        [39;49;00m[33mfrom functional import compose, partial[39;49;00m
  1262	[33m        [39;49;00m
  1263	[33m        multi_compose = partial(reduce, compose)[39;49;00m
  1264	[33m        [39;49;00m
  1265
  1266	We can also use [33m``[39;49;00m[33mmap()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m to craft a
  1267	version of [33m``[39;49;00m[33m"".join(...)[39;49;00m[33m``[39;49;00m that converts its arguments to string[33m::[39;49;00m
  1268
  1269	[33m        [39;49;00m[33mfrom functional import compose, partial[39;49;00m
  1270	[33m        [39;49;00m
  1271	[33m        join = compose("".join, partial(map, str))[39;49;00m
  1272	[33m[39;49;00m
  1273	[33m[39;49;00m
  1274	[33m``[39;49;00m[33mflip(func)[39;49;00m[33m``[39;49;00m
  1275
  1276	[33m``[39;49;00m[33mflip()[39;49;00m[33m``[39;49;00m wraps the callable in [33m``[39;49;00m[33mfunc[39;49;00m[33m``[39;49;00m and
  1277	causes it to receive its non-keyword arguments in reverse order.
  1278
  1279	[33m::[39;49;00m
  1280
  1281	[33m        [39;49;00m[33m>>> def triple(a, b, c):[39;49;00m
  1282	[33m        ...     return (a, b, c)[39;49;00m
  1283	[33m        ...[39;49;00m
  1284	[33m        >>> triple(5, 6, 7)[39;49;00m
  1285	[33m        (5, 6, 7)[39;49;00m
  1286	[33m        >>>[39;49;00m
  1287	[33m        >>> flipped_triple = flip(triple)[39;49;00m
  1288	[33m        >>> flipped_triple(5, 6, 7)[39;49;00m
  1289	[33m        (7, 6, 5)[39;49;00m
  1290	[33m[39;49;00m
  1291	[33m``[39;49;00m[33mfoldl(func, start, iterable)[39;49;00m[33m``[39;49;00m
  1292
  1293	[33m``[39;49;00m[33mfoldl()[39;49;00m[33m``[39;49;00m takes a binary function, a starting value (usually some kind of 'zero'), and an iterable.
  1294	The function is applied to the starting value and the first element of the list, then the result of
  1295	that and the second element of the list, then the result of that and the third element of the list,
  1296	and so on.
  1297
  1298	This means that a call such as[33m::[39;49;00m
  1299
  1300	[33m        [39;49;00m[33mfoldl(f, 0, [1, 2, 3])[39;49;00m
  1301	[33m[39;49;00m
  1302	is equivalent to[33m::[39;49;00m
  1303
  1304	[33m        [39;49;00m[33mf(f(f(0, 1), 2), 3)[39;49;00m
  1305	[33m[39;49;00m
  1306
  1307	[33m``[39;49;00m[33mfoldl()[39;49;00m[33m``[39;49;00m is roughly equivalent to the following recursive function[33m::[39;49;00m
  1308
  1309	[33m        [39;49;00m[33mdef foldl(func, start, seq):[39;49;00m
  1310	[33m            if len(seq) == 0:[39;49;00m
  1311	[33m                return start[39;49;00m
  1312	[33m[39;49;00m
  1313	[33m            return foldl(func, func(start, seq[0]), seq[1:])[39;49;00m
  1314	[33m[39;49;00m
  1315	Speaking of equivalence, the above [33m``[39;49;00m[33mfoldl[39;49;00m[33m``[39;49;00m call can be expressed in terms of the built-in [33m``[39;49;00m[33mreduce[39;49;00m[33m``[39;49;00m like
  1316	so[33m::[39;49;00m
  1317
  1318	[33m        [39;49;00m[33mreduce(f, [1, 2, 3], 0)[39;49;00m
  1319	[33m[39;49;00m
  1320	[33m[39;49;00m
  1321	We can use [33m``[39;49;00m[33mfoldl()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33moperator.concat()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m to
  1322	write a cleaner, more aesthetically-pleasing version of Python's
  1323	[33m``[39;49;00m[33m"".join(...)[39;49;00m[33m``[39;49;00m idiom[33m::[39;49;00m
  1324
  1325	[33m        [39;49;00m[33mfrom functional import foldl, partial[39;49;00m
  1326	[33m        from operator import concat[39;49;00m
  1327	[33m        [39;49;00m
  1328	[33m        join = partial(foldl, concat, "")[39;49;00m
  1329	[33m[39;49;00m
  1330	[33m[39;49;00m
  1331	[01mRevision History and Acknowledgements[39;49;00m
  1332	[01m------------------------------------------------[39;49;00m
  1333
  1334	The author would like to thank the following people for offering
  1335	suggestions, corrections and assistance with various drafts of this
  1336	article: Ian Bicking, Nick Coghlan, Nick Efford, Raymond Hettinger,
  1337	Jim Jewett, Mike Krell, Leandro Lameiro, Jussi Salmela,
  1338	Collin Winter, Blake Winton.
  1339
  1340	Version 0.1: posted June 30 2006.
  1341
  1342	Version 0.11: posted July 1 2006.  Typo fixes.
  1343
  1344	Version 0.2: posted July 10 2006.  Merged genexp and listcomp
  1345	sections into one.  Typo fixes.
  1346
  1347	Version 0.21: Added more references suggested on the tutor mailing list.
  1348
  1349	Version 0.30: Adds a section on the [33m``[39;49;00m[33mfunctional[39;49;00m[33m``[39;49;00m module written by
  1350	Collin Winter; adds short section on the operator module; a few other
  1351	edits.
  1352
  1353
  1354	[01mReferences[39;49;00m
  1355	[01m--------------------[39;49;00m
  1356
  1357	[01mGeneral[39;49;00m
  1358	[01m'''''''''''''''[39;49;00m
  1359
  1360	**Structure and Interpretation of Computer Programs**, by
  1361	Harold Abelson and Gerald Jay Sussman with Julie Sussman.
  1362	Full text at http://mitpress.mit.edu/sicp/.
  1363	In this classic textbook of computer science,  chapters 2 and 3 discuss the
  1364	use of sequences and streams to organize the data flow inside a
  1365	program.  The book uses Scheme for its examples, but many of the
  1366	design approaches described in these chapters are applicable to
  1367	functional-style Python code.
  1368
  1369	http://www.defmacro.org/ramblings/fp.html: A general
  1370	introduction to functional programming that uses Java examples
  1371	and has a lengthy historical introduction.
  1372
  1373	http://en.wikipedia.org/wiki/Functional_programming:
  1374	General Wikipedia entry describing functional programming.
  1375
  1376	http://en.wikipedia.org/wiki/Coroutine:
  1377	Entry for coroutines.
  1378
  1379	http://en.wikipedia.org/wiki/Currying:
  1380	Entry for the concept of currying.
  1381
  1382	[01mPython-specific[39;49;00m
  1383	[01m'''''''''''''''''''''''''''[39;49;00m
  1384
  1385	http://gnosis.cx/TPiP/:
  1386	The first chapter of David Mertz's book [36m:title-reference:[39;49;00m[31m`Text Processing in Python`[39;49;00m
  1387	discusses functional programming for text processing, in the section titled
  1388	"Utilizing Higher-Order Functions in Text Processing".
  1389
  1390	Mertz also wrote a 3-part series of articles on functional programming
  1391	for IBM's DeveloperWorks site; see
  1392	[33m`part 1 [39;49;00m[33m<http://www-128.ibm.com/developerworks/library/l-prog.html>[39;49;00m[33m`__[39;49;00m,
  1393	[33m`part 2 [39;49;00m[33m<http://www-128.ibm.com/developerworks/library/l-prog2.html>[39;49;00m[33m`__[39;49;00m, and
  1394	[33m`part 3 [39;49;00m[33m<http://www-128.ibm.com/developerworks/linux/library/l-prog3.html>[39;49;00m[33m`__[39;49;00m,
  1395
  1396
  1397	[01mPython documentation[39;49;00m
  1398	[01m'''''''''''''''''''''''''''[39;49;00m
  1399
  1400	http://docs.python.org/lib/module-itertools.html:
  1401	Documentation for the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module.
  1402
  1403	http://docs.python.org/lib/module-operator.html:
  1404	Documentation for the [33m``[39;49;00m[33moperator[39;49;00m[33m``[39;49;00m module.
  1405
  1406	http://www.python.org/dev/peps/pep-0289/:
  1407	PEP 289: "Generator Expressions"
  1408
  1409	http://www.python.org/dev/peps/pep-0342/
  1410	PEP 342: "Coroutines via Enhanced Generators" describes the new generator
  1411	features in Python 2.5.
  1412
  1413	[36m.. comment[39;49;00m
  1414	[36m[39;49;00m
  1415	[36m    Topics to place[39;49;00m
  1416	[36m    -----------------------------[39;49;00m
  1417	[36m[39;49;00m
  1418	[36m    XXX os.walk()[39;49;00m
  1419	[36m[39;49;00m
  1420	[36m    XXX Need a large example.[39;49;00m
  1421	[36m[39;49;00m
  1422	[36m    But will an example add much?  I'll post a first draft and see[39;49;00m
  1423	[36m    what the comments say.[39;49;00m
  1424	[36m[39;49;00m
  1425	[36m.. comment[39;49;00m
  1426	[36m[39;49;00m
  1427	[36m    Original outline:[39;49;00m
  1428	[36m    Introduction[39;49;00m
  1429	[36m            Idea of FP[39;49;00m
  1430	[36m                    Programs built out of functions[39;49;00m
  1431	[36m                    Functions are strictly input-output, no internal state[39;49;00m
  1432	[36m            Opposed to OO programming, where objects have state[39;49;00m
  1433	[36m[39;49;00m
  1434	[36m            Why FP?[39;49;00m
  1435	[36m                    Formal provability[39;49;00m
  1436	[36m                            Assignment is difficult to reason about[39;49;00m
  1437	[36m                            Not very relevant to Python[39;49;00m
  1438	[36m                    Modularity[39;49;00m
  1439	[36m                            Small functions that do one thing[39;49;00m
  1440	[36m                    Debuggability:[39;49;00m
  1441	[36m                            Easy to test due to lack of state[39;49;00m
  1442	[36m                            Easy to verify output from intermediate steps[39;49;00m
  1443	[36m                    Composability[39;49;00m
  1444	[36m                            You assemble a toolbox of functions that can be mixed[39;49;00m
  1445	[36m[39;49;00m
  1446	[36m    Tackling a problem[39;49;00m
  1447	[36m            Need a significant example[39;49;00m
  1448	[36m[39;49;00m
  1449	[36m    Iterators[39;49;00m
  1450	[36m    Generators[39;49;00m
  1451	[36m    The itertools module[39;49;00m
  1452	[36m    List comprehensions[39;49;00m
  1453	[36m    Small functions and the lambda statement[39;49;00m
  1454	[36m    Built-in functions[39;49;00m
  1455	[36m            map[39;49;00m
  1456	[36m            filter[39;49;00m
  1457	[36m            reduce[39;49;00m
  1458	[36m[39;49;00m
  1459	[36m.. comment[39;49;00m
  1460	[36m[39;49;00m
  1461	[36m    Handy little function for printing part of an iterator -- used[39;49;00m
  1462	[36m    while writing this document.[39;49;00m
  1463	[36m[39;49;00m
  1464	[36m    import itertools[39;49;00m
  1465	[36m    def print_iter(it):[39;49;00m
  1466	[36m         slice = itertools.islice(it, 10)[39;49;00m
  1467	[36m         for elem in slice[:-1]:[39;49;00m
  1468	[36m             sys.stdout.write(str(elem))[39;49;00m
  1469	[36m             sys.stdout.write(', ')[39;49;00m
  1470	        print elem[-1]
