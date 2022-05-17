     1^I[01mFunctional Programming HOWTO[39;49;00m$
     2^I[01m================================[39;49;00m$
     3^I$
     4^I**Version 0.30**$
     5^I$
     6^I(This is a first draft.  Please send comments/error$
     7^Ireports/suggestions to amk@amk.ca.  This URL is probably not going to$
     8^Ibe the final location of the document, so be careful about linking to$
     9^Iit -- you may want to add a disclaimer.)$
    10^I$
    11^IIn this document, we'll take a tour of Python's features suitable for$
    12^Iimplementing programs in a functional style.  After an introduction to$
    13^Ithe concepts of functional programming, we'll look at language$
    14^Ifeatures such as iterators and generators and relevant library modules$
    15^Isuch as [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfunctools[39;49;00m[33m``[39;49;00m.$
    16^I$
    17^I$
    18^I.. [35mcontents[39;49;00m::$
    19^I$
    20^I[01mIntroduction[39;49;00m$
    21^I[01m----------------------[39;49;00m$
    22^I$
    23^IThis section explains the basic concept of functional programming; if$
    24^Iyou're just interested in learning about Python language features,$
    25^Iskip to the next section.$
    26^I$
    27^IProgramming languages support decomposing problems in several different $
    28^Iways:$
    29^I$
    30^I[34m*[39;49;00m Most programming languages are **procedural**: $
    31^I  programs are lists of instructions that tell the computer what to$
    32^I  do with the program's input.$
    33^I  C, Pascal, and even Unix shells are procedural languages.$
    34^I$
    35^I[34m*[39;49;00m In **declarative** languages, you write a specification that describes $
    36^I  the problem to be solved, and the language implementation figures out $
    37^I  how to perform the computation efficiently.  SQL is the declarative $
    38^I  language you're most likely to be familiar with; a SQL query describes$
    39^I  the data set you want to retrieve, and the SQL engine decides whether to $
    40^I  scan tables or use indexes, which subclauses should be performed first,$
    41^I  etc.$
    42^I$
    43^I[34m*[39;49;00m **Object-oriented** programs manipulate  collections of objects.$
    44^I  Objects have internal state and support methods that query or modify$
    45^I  this internal state in some way. Smalltalk and Java are$
    46^I  object-oriented languages.  C++ and Python are languages that$
    47^I  support object-oriented programming, but don't force the use $
    48^I  of object-oriented features.$
    49^I$
    50^I[34m*[39;49;00m **Functional** programming decomposes a problem into a set of functions.$
    51^I  Ideally, functions only take inputs and produce outputs, and don't have any $
    52^I  internal state that affects the output produced for a given input.$
    53^I  Well-known functional languages include the ML family (Standard ML,$
    54^I  OCaml, and other variants) and Haskell.$
    55^I$
    56^IThe designers of some computer languages have chosen one approach to $
    57^Iprogramming that's emphasized.  This often makes it difficult to$
    58^Iwrite programs that use a different approach.  Other languages are$
    59^Imulti-paradigm languages that support several different approaches.  Lisp,$
    60^IC++, and Python are multi-paradigm; you can write programs or$
    61^Ilibraries that are largely procedural, object-oriented, or functional$
    62^Iin all of these languages.  In a large program, different sections$
    63^Imight be written using different approaches; the GUI might be object-oriented$
    64^Iwhile the processing logic is procedural or functional, for example.$
    65^I$
    66^IIn a functional program, input flows through a set of functions. Each$
    67^Ifunction operates on its input and produces some output.  Functional$
    68^Istyle frowns upon functions with side effects that modify internal$
    69^Istate or make other changes that aren't visible in the function's$
    70^Ireturn value.  Functions that have no side effects at all are $
    71^Icalled **purely functional**.$
    72^IAvoiding side effects means not using data structures$
    73^Ithat get updated as a program runs; every function's output $
    74^Imust only depend on its input.$
    75^I$
    76^ISome languages are very strict about purity and don't even have$
    77^Iassignment statements such as [33m``[39;49;00m[33ma=3[39;49;00m[33m``[39;49;00m or [33m``[39;49;00m[33mc = a + b[39;49;00m[33m``[39;49;00m, but it's$
    78^Idifficult to avoid all side effects.  Printing to the screen or$
    79^Iwriting to a disk file are side effects, for example.  For example, in$
    80^IPython a [33m``[39;49;00m[33mprint[39;49;00m[33m``[39;49;00m statement or a [33m``[39;49;00m[33mtime.sleep(1)[39;49;00m[33m``[39;49;00m both return no$
    81^Iuseful value; they're only called for their side effects of sending$
    82^Isome text to the screen or pausing execution for a second.$
    83^I$
    84^IPython programs written in functional style usually won't go to the$
    85^Iextreme of avoiding all I/O or all assignments; instead, they'll$
    86^Iprovide a functional-appearing interface but will use non-functional$
    87^Ifeatures internally.  For example, the implementation of a function$
    88^Iwill still use assignments to local variables, but won't modify global$
    89^Ivariables or have other side effects.$
    90^I$
    91^IFunctional programming can be considered the opposite of$
    92^Iobject-oriented programming.  Objects are little capsules containing$
    93^Isome internal state along with a collection of method calls that let$
    94^Iyou modify this state, and programs consist of making the right set of$
    95^Istate changes.  Functional programming wants to avoid state changes as$
    96^Imuch as possible and works with data flowing between functions.  In$
    97^IPython you might combine the two approaches by writing functions that$
    98^Itake and return instances representing objects in your application$
    99^I(e-mail messages, transactions, etc.).$
   100^I$
   101^IFunctional design may seem like an odd constraint to work under.  Why$
   102^Ishould you avoid objects and side effects?  There are theoretical and$
   103^Ipractical advantages to the functional style:$
   104^I$
   105^I[34m*[39;49;00m Formal provability.$
   106^I[34m*[39;49;00m Modularity.$
   107^I[34m*[39;49;00m Composability.$
   108^I[34m*[39;49;00m Ease of debugging and testing.$
   109^I$
   110^I[01mFormal provability[39;49;00m$
   111^I[01m''''''''''''''''''''''[39;49;00m$
   112^I$
   113^IA theoretical benefit is that it's easier to construct a mathematical proof$
   114^Ithat a functional program is correct.$
   115^I$
   116^IFor a long time researchers have been interested in finding ways to$
   117^Imathematically prove programs correct.  This is different from testing$
   118^Ia program on numerous inputs and concluding that its output is usually$
   119^Icorrect, or reading a program's source code and concluding that the$
   120^Icode looks right; the goal is instead a rigorous proof that a program$
   121^Iproduces the right result for all possible inputs.$
   122^I$
   123^IThe technique used to prove programs correct is to write down $
   124^I**invariants**, properties of the input data and of the program's $
   125^Ivariables that are always true.  For each line of code, you then show $
   126^Ithat if invariants X and Y are true **before** the line is executed, $
   127^Ithe slightly different invariants X' and Y' are true **after**$
   128^Ithe line is executed.  This continues until you reach the end of the$
   129^Iprogram, at which point the invariants should match the desired $
   130^Iconditions on the program's output.$
   131^I$
   132^IFunctional programming's avoidance of assignments arose because $
   133^Iassignments are difficult to handle with this technique; $
   134^Iassignments can break invariants that were true before the assignment$
   135^Iwithout producing any new invariants that can be propagated onward.$
   136^I$
   137^IUnfortunately, proving programs correct is largely impractical and not$
   138^Irelevant to Python software. Even trivial programs require proofs that$
   139^Iare several pages long; the proof of correctness for a moderately$
   140^Icomplicated program would be enormous, and few or none of the programs$
   141^Iyou use daily (the Python interpreter, your XML parser, your web$
   142^Ibrowser) could be proven correct.  Even if you wrote down or generated$
   143^Ia proof, there would then be the question of verifying the proof;$
   144^Imaybe there's an error in it, and you wrongly believe you've proved$
   145^Ithe program correct.$
   146^I$
   147^I[01mModularity[39;49;00m$
   148^I[01m''''''''''''''''''''''[39;49;00m$
   149^I$
   150^IA more practical benefit of functional programming is that it forces$
   151^Iyou to break apart your problem into small pieces.  Programs are more$
   152^Imodular as a result.  It's easier to specify and write a small$
   153^Ifunction that does one thing than a large function that performs a$
   154^Icomplicated transformation.  Small functions are also easier to read$
   155^Iand to check for errors.$
   156^I$
   157^I$
   158^I[01mEase of debugging and testing [39;49;00m$
   159^I[01m''''''''''''''''''''''''''''''''''[39;49;00m$
   160^I$
   161^ITesting and debugging a functional-style program is easier.$
   162^I$
   163^IDebugging is simplified because functions are generally small and$
   164^Iclearly specified.  When a program doesn't work, each function is an$
   165^Iinterface point where you can check that the data are correct.  You$
   166^Ican look at the intermediate inputs and outputs to quickly isolate the$
   167^Ifunction that's responsible for a bug.$
   168^I$
   169^ITesting is easier because each function is a potential subject for a$
   170^Iunit test.  Functions don't depend on system state that needs to be$
   171^Ireplicated before running a test; instead you only have to synthesize$
   172^Ithe right input and then check that the output matches expectations.$
   173^I$
   174^I$
   175^I$
   176^I[01mComposability[39;49;00m$
   177^I[01m''''''''''''''''''''''[39;49;00m$
   178^I$
   179^IAs you work on a functional-style program, you'll write a number of$
   180^Ifunctions with varying inputs and outputs.  Some of these functions$
   181^Iwill be unavoidably specialized to a particular application, but$
   182^Iothers will be useful in a wide variety of programs.  For example, a$
   183^Ifunction that takes a directory path and returns all the XML files in$
   184^Ithe directory, or a function that takes a filename and returns its$
   185^Icontents, can be applied to many different situations.$
   186^I$
   187^IOver time you'll form a personal library of utilities.  Often you'll$
   188^Iassemble new programs by arranging existing functions in a new$
   189^Iconfiguration and writing a few functions specialized for the current$
   190^Itask.$
   191^I$
   192^I$
   193^I$
   194^I[01mIterators[39;49;00m$
   195^I[01m-----------------------[39;49;00m$
   196^I$
   197^II'll start by looking at a Python language feature that's an important$
   198^Ifoundation for writing functional-style programs: iterators.$
   199^I$
   200^IAn iterator is an object representing a stream of data; this object$
   201^Ireturns the data one element at a time.  A Python iterator must$
   202^Isupport a method called [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m that takes no arguments and always$
   203^Ireturns the next element of the stream.  If there are no more elements$
   204^Iin the stream, [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m must raise the [33m``[39;49;00m[33mStopIteration[39;49;00m[33m``[39;49;00m exception.$
   205^IIterators don't have to be finite, though; it's perfectly reasonable$
   206^Ito write an iterator that produces an infinite stream of data.$
   207^I$
   208^IThe built-in [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m function takes an arbitrary object and tries$
   209^Ito return an iterator that will return the object's contents or$
   210^Ielements, raising [33m``[39;49;00m[33mTypeError[39;49;00m[33m``[39;49;00m if the object doesn't support$
   211^Iiteration.  Several of Python's built-in data types support iteration,$
   212^Ithe most common being lists and dictionaries.  An object is called $
   213^Ian **iterable** object if you can get an iterator for it.$
   214^I$
   215^IYou can experiment with the iteration interface manually[33m::[39;49;00m$
   216^I$
   217^I[33m    [39;49;00m[33m>>> L = [1,2,3][39;49;00m$
   218^I[33m    >>> it = iter(L)[39;49;00m$
   219^I[33m    >>> print it[39;49;00m$
   220^I[33m    <iterator object at 0x8116870>[39;49;00m$
   221^I[33m    >>> it.next()[39;49;00m$
   222^I[33m    1[39;49;00m$
   223^I[33m    >>> it.next()[39;49;00m$
   224^I[33m    2[39;49;00m$
   225^I[33m    >>> it.next()[39;49;00m$
   226^I[33m    3[39;49;00m$
   227^I[33m    >>> it.next()[39;49;00m$
   228^I[33m    Traceback (most recent call last):[39;49;00m$
   229^I[33m      File "<stdin>", line 1, in ?[39;49;00m$
   230^I[33m    StopIteration[39;49;00m$
   231^I[33m    >>>      [39;49;00m$
   232^I[33m[39;49;00m$
   233^IPython expects iterable objects in several different contexts, the $
   234^Imost important being the [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m statement.  In the statement [33m``[39;49;00m[33mfor X in Y[39;49;00m[33m``[39;49;00m,$
   235^IY must be an iterator or some object for which [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m can create $
   236^Ian iterator.  These two statements are equivalent[33m::[39;49;00m$
   237^I$
   238^I[33m        [39;49;00m[33mfor i in iter(obj):[39;49;00m$
   239^I[33m            print i[39;49;00m$
   240^I[33m[39;49;00m$
   241^I[33m        for i in obj:[39;49;00m$
   242^I[33m            print i[39;49;00m$
   243^I[33m[39;49;00m$
   244^IIterators can be materialized as lists or tuples by using the$
   245^I[33m``[39;49;00m[33mlist()[39;49;00m[33m``[39;49;00m or [33m``[39;49;00m[33mtuple()[39;49;00m[33m``[39;49;00m constructor functions[33m::[39;49;00m$
   246^I$
   247^I[33m    [39;49;00m[33m>>> L = [1,2,3][39;49;00m$
   248^I[33m    >>> iterator = iter(L)[39;49;00m$
   249^I[33m    >>> t = tuple(iterator)[39;49;00m$
   250^I[33m    >>> t[39;49;00m$
   251^I[33m    (1, 2, 3)[39;49;00m$
   252^I[33m[39;49;00m$
   253^ISequence unpacking also supports iterators: if you know an iterator $
   254^Iwill return N elements, you can unpack them into an N-tuple[33m::[39;49;00m$
   255^I$
   256^I[33m    [39;49;00m[33m>>> L = [1,2,3][39;49;00m$
   257^I[33m    >>> iterator = iter(L)[39;49;00m$
   258^I[33m    >>> a,b,c = iterator[39;49;00m$
   259^I[33m    >>> a,b,c[39;49;00m$
   260^I[33m    (1, 2, 3)[39;49;00m$
   261^I[33m[39;49;00m$
   262^IBuilt-in functions such as [33m``[39;49;00m[33mmax()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mmin()[39;49;00m[33m``[39;49;00m can take a single$
   263^Iiterator argument and will return the largest or smallest element.$
   264^IThe [33m``[39;49;00m[33m"in"[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33m"not in"[39;49;00m[33m``[39;49;00m operators also support iterators: [33m``[39;49;00m[33mX in[39;49;00m$
   265^I[33miterator[39;49;00m[33m``[39;49;00m is true if X is found in the stream returned by the$
   266^Iiterator.  You'll run into obvious problems if the iterator is$
   267^Iinfinite; [33m``[39;49;00m[33mmax()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mmin()[39;49;00m[33m``[39;49;00m, and [33m``[39;49;00m[33m"not in"[39;49;00m[33m``[39;49;00m will never return, and$
   268^Iif the element X never appears in the stream, the [33m``[39;49;00m[33m"in"[39;49;00m[33m``[39;49;00m operator$
   269^Iwon't return either.$
   270^I$
   271^INote that you can only go forward in an iterator; there's no way to$
   272^Iget the previous element, reset the iterator, or make a copy of it.$
   273^IIterator objects can optionally provide these additional capabilities,$
   274^Ibut the iterator protocol only specifies the [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m method.$
   275^IFunctions may therefore consume all of the iterator's output, and if$
   276^Iyou need to do something different with the same stream, you'll have$
   277^Ito create a new iterator.$
   278^I$
   279^I$
   280^I$
   281^I[01mData Types That Support Iterators[39;49;00m$
   282^I[01m'''''''''''''''''''''''''''''''''''[39;49;00m$
   283^I$
   284^IWe've already seen how lists and tuples support iterators.  In fact,$
   285^Iany Python sequence type, such as strings, will automatically support$
   286^Icreation of an iterator.$
   287^I$
   288^ICalling [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m on a dictionary returns an iterator that will loop$
   289^Iover the dictionary's keys[33m::[39;49;00m$
   290^I$
   291^I[33m    [39;49;00m[33m>>> m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,[39;49;00m$
   292^I[33m    ...      'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}[39;49;00m$
   293^I[33m    >>> for key in m:[39;49;00m$
   294^I[33m    ...     print key, m[key][39;49;00m$
   295^I[33m    Mar 3[39;49;00m$
   296^I[33m    Feb 2[39;49;00m$
   297^I[33m    Aug 8[39;49;00m$
   298^I[33m    Sep 9[39;49;00m$
   299^I[33m    May 5[39;49;00m$
   300^I[33m    Jun 6[39;49;00m$
   301^I[33m    Jul 7[39;49;00m$
   302^I[33m    Jan 1[39;49;00m$
   303^I[33m    Apr 4[39;49;00m$
   304^I[33m    Nov 11[39;49;00m$
   305^I[33m    Dec 12[39;49;00m$
   306^I[33m    Oct 10[39;49;00m$
   307^I[33m[39;49;00m$
   308^INote that the order is essentially random, because it's based on the$
   309^Ihash ordering of the objects in the dictionary.$
   310^I$
   311^IApplying [33m``[39;49;00m[33miter()[39;49;00m[33m``[39;49;00m to a dictionary always loops over the keys, but$
   312^Idictionaries have methods that return other iterators.  If you want to$
   313^Iiterate over keys, values, or key/value pairs, you can explicitly call$
   314^Ithe [33m``[39;49;00m[33miterkeys()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mitervalues()[39;49;00m[33m``[39;49;00m, or [33m``[39;49;00m[33miteritems()[39;49;00m[33m``[39;49;00m methods to$
   315^Iget an appropriate iterator.$
   316^I$
   317^IThe [33m``[39;49;00m[33mdict()[39;49;00m[33m``[39;49;00m constructor can accept an iterator that returns a$
   318^Ifinite stream of [33m``[39;49;00m[33m(key, value)[39;49;00m[33m``[39;49;00m tuples[33m::[39;49;00m$
   319^I$
   320^I[33m    [39;49;00m[33m>>> L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')][39;49;00m$
   321^I[33m    >>> dict(iter(L))[39;49;00m$
   322^I[33m    {'Italy': 'Rome', 'US': 'Washington DC', 'France': 'Paris'}[39;49;00m$
   323^I[33m[39;49;00m$
   324^IFiles also support iteration by calling the [33m``[39;49;00m[33mreadline()[39;49;00m[33m``[39;49;00m$
   325^Imethod until there are no more lines in the file.  This means you can$
   326^Iread each line of a file like this[33m::[39;49;00m$
   327^I$
   328^I[33m    [39;49;00m[33mfor line in file:[39;49;00m$
   329^I[33m        # do something for each line[39;49;00m$
   330^I[33m        ...[39;49;00m$
   331^I[33m[39;49;00m$
   332^ISets can take their contents from an iterable and let you iterate over$
   333^Ithe set's elements[33m::[39;49;00m$
   334^I$
   335^I[33m    [39;49;00m[33mS = set((2, 3, 5, 7, 11, 13))[39;49;00m$
   336^I[33m    for i in S:[39;49;00m$
   337^I[33m        print i[39;49;00m$
   338^I[33m[39;49;00m$
   339^I[33m[39;49;00m$
   340^I[33m[39;49;00m$
   341^I[01mGenerator expressions and list comprehensions[39;49;00m$
   342^I[01m----------------------------------------------------[39;49;00m$
   343^I$
   344^ITwo common operations on an iterator's output are 1) performing some$
   345^Ioperation for every element, 2) selecting a subset of elements that$
   346^Imeet some condition.  For example, given a list of strings, you might$
   347^Iwant to strip off trailing whitespace from each line or extract all$
   348^Ithe strings containing a given substring.$
   349^I$
   350^IList comprehensions and generator expressions (short form: "listcomps"$
   351^Iand "genexps") are a concise notation for such operations, borrowed$
   352^Ifrom the functional programming language Haskell$
   353^I(http://www.haskell.org).  You can strip all the whitespace from a$
   354^Istream of strings with the following code[33m::[39;49;00m$
   355^I$
   356^I[33m        [39;49;00m[33mline_list = ['  line 1\n', 'line 2  \n', ...][39;49;00m$
   357^I[33m[39;49;00m$
   358^I[33m        # Generator expression -- returns iterator[39;49;00m$
   359^I[33m        stripped_iter = (line.strip() for line in line_list)[39;49;00m$
   360^I[33m[39;49;00m$
   361^I[33m        # List comprehension -- returns list[39;49;00m$
   362^I[33m        stripped_list = [line.strip() for line in line_list][39;49;00m$
   363^I[33m[39;49;00m$
   364^IYou can select only certain elements by adding an [33m``[39;49;00m[33m"if"[39;49;00m[33m``[39;49;00m condition[33m::[39;49;00m$
   365^I$
   366^I[33m        [39;49;00m[33mstripped_list = [line.strip() for line in line_list[39;49;00m$
   367^I[33m                         if line != ""][39;49;00m$
   368^I[33m[39;49;00m$
   369^IWith a list comprehension, you get back a Python list;$
   370^I[33m``[39;49;00m[33mstripped_list[39;49;00m[33m``[39;49;00m is a list containing the resulting lines, not an$
   371^Iiterator.  Generator expressions return an iterator that computes the$
   372^Ivalues as necessary, not needing to materialize all the values at$
   373^Ionce.  This means that list comprehensions aren't useful if you're$
   374^Iworking with iterators that return an infinite stream or a very large$
   375^Iamount of data.  Generator expressions are preferable in these$
   376^Isituations.$
   377^I$
   378^IGenerator expressions are surrounded by parentheses ("()") and list$
   379^Icomprehensions are surrounded by square brackets ("[]").  Generator$
   380^Iexpressions have the form[33m::[39;49;00m$
   381^I$
   382^I[33m    [39;49;00m[33m( expression for expr in sequence1 [39;49;00m$
   383^I[33m                 if condition1[39;49;00m$
   384^I[33m                 for expr2 in sequence2[39;49;00m$
   385^I[33m                 if condition2[39;49;00m$
   386^I[33m                 for expr3 in sequence3 ...[39;49;00m$
   387^I[33m                 if condition3[39;49;00m$
   388^I[33m                 for exprN in sequenceN[39;49;00m$
   389^I[33m                 if conditionN )[39;49;00m$
   390^I[33m[39;49;00m$
   391^IAgain, for a list comprehension only the outside brackets are$
   392^Idifferent (square brackets instead of parentheses).$
   393^I$
   394^IThe elements of the generated output will be the successive values of$
   395^I[33m``[39;49;00m[33mexpression[39;49;00m[33m``[39;49;00m.  The [33m``[39;49;00m[33mif[39;49;00m[33m``[39;49;00m clauses are all optional; if present,$
   396^I[33m``[39;49;00m[33mexpression[39;49;00m[33m``[39;49;00m is only evaluated and added to the result when$
   397^I[33m``[39;49;00m[33mcondition[39;49;00m[33m``[39;49;00m is true.$
   398^I$
   399^IGenerator expressions always have to be written inside parentheses,$
   400^Ibut the parentheses signalling a function call also count.  If you$
   401^Iwant to create an iterator that will be immediately passed to a$
   402^Ifunction you can write[33m::[39;49;00m$
   403^I$
   404^I[33m        [39;49;00m[33mobj_total = sum(obj.count for obj in list_all_objects())[39;49;00m$
   405^I[33m[39;49;00m$
   406^IThe [33m``[39;49;00m[33mfor...in[39;49;00m[33m``[39;49;00m clauses contain the sequences to be iterated over.$
   407^IThe sequences do not have to be the same length, because they are$
   408^Iiterated over from left to right, **not** in parallel.  For each$
   409^Ielement in [33m``[39;49;00m[33msequence1[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33msequence2[39;49;00m[33m``[39;49;00m is looped over from the$
   410^Ibeginning.  [33m``[39;49;00m[33msequence3[39;49;00m[33m``[39;49;00m  is then looped over for each $
   411^Iresulting pair of elements from [33m``[39;49;00m[33msequence1[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33msequence2[39;49;00m[33m``[39;49;00m.$
   412^I$
   413^ITo put it another way, a list comprehension or generator expression is$
   414^Iequivalent to the following Python code[33m::[39;49;00m$
   415^I$
   416^I[33m    [39;49;00m[33mfor expr1 in sequence1:[39;49;00m$
   417^I[33m        if not (condition1):[39;49;00m$
   418^I[33m            continue   # Skip this element[39;49;00m$
   419^I[33m        for expr2 in sequence2:[39;49;00m$
   420^I[33m            if not (condition2):[39;49;00m$
   421^I[33m                continue    # Skip this element[39;49;00m$
   422^I[33m            ...[39;49;00m$
   423^I[33m            for exprN in sequenceN:[39;49;00m$
   424^I[33m                 if not (conditionN):[39;49;00m$
   425^I[33m                     continue   # Skip this element[39;49;00m$
   426^I[33m[39;49;00m$
   427^I[33m                 # Output the value of [39;49;00m$
   428^I[33m                 # the expression.[39;49;00m$
   429^I[33m[39;49;00m$
   430^IThis means that when there are multiple [33m``[39;49;00m[33mfor...in[39;49;00m[33m``[39;49;00m clauses but no$
   431^I[33m``[39;49;00m[33mif[39;49;00m[33m``[39;49;00m clauses, the length of the resulting output will be equal to$
   432^Ithe product of the lengths of all the sequences.  If you have two$
   433^Ilists of length 3, the output list is 9 elements long[33m::[39;49;00m$
   434^I$
   435^I[33m    [39;49;00m[33mseq1 = 'abc'[39;49;00m$
   436^I[33m    seq2 = (1,2,3)[39;49;00m$
   437^I[33m    >>> [ (x,y) for x in seq1 for y in seq2][39;49;00m$
   438^I[33m    [('a', 1), ('a', 2), ('a', 3), [39;49;00m$
   439^I[33m     ('b', 1), ('b', 2), ('b', 3), [39;49;00m$
   440^I[33m     ('c', 1), ('c', 2), ('c', 3)][39;49;00m$
   441^I[33m[39;49;00m$
   442^ITo avoid introducing an ambiguity into Python's grammar, if$
   443^I[33m``[39;49;00m[33mexpression[39;49;00m[33m``[39;49;00m is creating a tuple, it must be surrounded with$
   444^Iparentheses.  The first list comprehension below is a syntax error,$
   445^Iwhile the second one is correct[33m::[39;49;00m$
   446^I$
   447^I[33m    [39;49;00m[33m# Syntax error[39;49;00m$
   448^I[33m    [ x,y for x in seq1 for y in seq2][39;49;00m$
   449^I[33m    # Correct[39;49;00m$
   450^I[33m    [ (x,y) for x in seq1 for y in seq2][39;49;00m$
   451^I[33m[39;49;00m$
   452^I[33m[39;49;00m$
   453^I[01mGenerators[39;49;00m$
   454^I[01m-----------------------[39;49;00m$
   455^I$
   456^IGenerators are a special class of functions that simplify the task of$
   457^Iwriting iterators.  Regular functions compute a value and return it,$
   458^Ibut generators return an iterator that returns a stream of values.$
   459^I$
   460^IYou're doubtless familiar with how regular function calls work in$
   461^IPython or C.  When you call a function, it gets a private namespace$
   462^Iwhere its local variables are created.  When the function reaches a$
   463^I[33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m statement, the local variables are destroyed and the$
   464^Ivalue is returned to the caller.  A later call to the same function$
   465^Icreates a new private namespace and a fresh set of local$
   466^Ivariables. But, what if the local variables weren't thrown away on$
   467^Iexiting a function?  What if you could later resume the function where$
   468^Iit left off?  This is what generators provide; they can be thought of$
   469^Ias resumable functions.$
   470^I$
   471^IHere's the simplest example of a generator function[33m::[39;49;00m$
   472^I$
   473^I[33m    [39;49;00m[33mdef generate_ints(N):[39;49;00m$
   474^I[33m        for i in range(N):[39;49;00m$
   475^I[33m            yield i[39;49;00m$
   476^I[33m[39;49;00m$
   477^IAny function containing a [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m keyword is a generator function;$
   478^Ithis is detected by Python's bytecode compiler which compiles the$
   479^Ifunction specially as a result.$
   480^I$
   481^IWhen you call a generator function, it doesn't return a single value;$
   482^Iinstead it returns a generator object that supports the iterator$
   483^Iprotocol.  On executing the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m expression, the generator$
   484^Ioutputs the value of [33m``[39;49;00m[33mi[39;49;00m[33m``[39;49;00m, similar to a [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m$
   485^Istatement.  The big difference between [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m and a$
   486^I[33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m statement is that on reaching a [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m the$
   487^Igenerator's state of execution is suspended and local variables are$
   488^Ipreserved.  On the next call to the generator's [33m``[39;49;00m[33m.next()[39;49;00m[33m``[39;49;00m method,$
   489^Ithe function will resume executing.  $
   490^I$
   491^IHere's a sample usage of the [33m``[39;49;00m[33mgenerate_ints()[39;49;00m[33m``[39;49;00m generator[33m::[39;49;00m$
   492^I$
   493^I[33m    [39;49;00m[33m>>> gen = generate_ints(3)[39;49;00m$
   494^I[33m    >>> gen[39;49;00m$
   495^I[33m    <generator object at 0x8117f90>[39;49;00m$
   496^I[33m    >>> gen.next()[39;49;00m$
   497^I[33m    0[39;49;00m$
   498^I[33m    >>> gen.next()[39;49;00m$
   499^I[33m    1[39;49;00m$
   500^I[33m    >>> gen.next()[39;49;00m$
   501^I[33m    2[39;49;00m$
   502^I[33m    >>> gen.next()[39;49;00m$
   503^I[33m    Traceback (most recent call last):[39;49;00m$
   504^I[33m      File "stdin", line 1, in ?[39;49;00m$
   505^I[33m      File "stdin", line 2, in generate_ints[39;49;00m$
   506^I[33m    StopIteration[39;49;00m$
   507^I[33m[39;49;00m$
   508^IYou could equally write [33m``[39;49;00m[33mfor i in generate_ints(5)[39;49;00m[33m``[39;49;00m, or$
   509^I[33m``[39;49;00m[33ma,b,c = generate_ints(3)[39;49;00m[33m``[39;49;00m.$
   510^I$
   511^IInside a generator function, the [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m statement can only be used$
   512^Iwithout a value, and signals the end of the procession of values;$
   513^Iafter executing a [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m the generator cannot return any further$
   514^Ivalues.  [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m with a value, such as [33m``[39;49;00m[33mreturn 5[39;49;00m[33m``[39;49;00m, is a syntax$
   515^Ierror inside a generator function.  The end of the generator's results$
   516^Ican also be indicated by raising [33m``[39;49;00m[33mStopIteration[39;49;00m[33m``[39;49;00m manually, or by$
   517^Ijust letting the flow of execution fall off the bottom of the$
   518^Ifunction.$
   519^I$
   520^IYou could achieve the effect of generators manually by writing your$
   521^Iown class and storing all the local variables of the generator as$
   522^Iinstance variables.  For example, returning a list of integers could$
   523^Ibe done by setting [33m``[39;49;00m[33mself.count[39;49;00m[33m``[39;49;00m to 0, and having the$
   524^I[33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m method increment [33m``[39;49;00m[33mself.count[39;49;00m[33m``[39;49;00m and return it.$
   525^IHowever, for a moderately complicated generator, writing a$
   526^Icorresponding class can be much messier.$
   527^I$
   528^IThe test suite included with Python's library, [33m``[39;49;00m[33mtest_generators.py[39;49;00m[33m``[39;49;00m,$
   529^Icontains a number of more interesting examples.  Here's one generator$
   530^Ithat implements an in-order traversal of a tree using generators$
   531^Irecursively.$
   532^I$
   533^I[33m::[39;49;00m$
   534^I$
   535^I[33m    [39;49;00m[33m# A recursive generator that generates Tree leaves in in-order.[39;49;00m$
   536^I[33m    def inorder(t):[39;49;00m$
   537^I[33m        if t:[39;49;00m$
   538^I[33m            for x in inorder(t.left):[39;49;00m$
   539^I[33m                yield x[39;49;00m$
   540^I[33m[39;49;00m$
   541^I[33m            yield t.label[39;49;00m$
   542^I[33m[39;49;00m$
   543^I[33m            for x in inorder(t.right):[39;49;00m$
   544^I[33m                yield x[39;49;00m$
   545^I[33m[39;49;00m$
   546^ITwo other examples in [33m``[39;49;00m[33mtest_generators.py[39;49;00m[33m``[39;49;00m produce$
   547^Isolutions for the N-Queens problem (placing N queens on an NxN$
   548^Ichess board so that no queen threatens another) and the Knight's Tour$
   549^I(finding a route that takes a knight to every square of an NxN chessboard$
   550^Iwithout visiting any square twice).$
   551^I$
   552^I$
   553^I$
   554^I[01mPassing values into a generator[39;49;00m$
   555^I[01m''''''''''''''''''''''''''''''''''''''''''''''[39;49;00m$
   556^I$
   557^IIn Python 2.4 and earlier, generators only produced output.  Once a$
   558^Igenerator's code was invoked to create an iterator, there was no way to$
   559^Ipass any new information into the function when its execution is$
   560^Iresumed.  You could hack together this ability by making the$
   561^Igenerator look at a global variable or by passing in some mutable object$
   562^Ithat callers then modify, but these approaches are messy.$
   563^I$
   564^IIn Python 2.5 there's a simple way to pass values into a generator.$
   565^I[33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m became an expression, returning a value that can be assigned$
   566^Ito a variable or otherwise operated on[33m::[39;49;00m$
   567^I$
   568^I[33m    [39;49;00m[33mval = (yield i)[39;49;00m$
   569^I[33m[39;49;00m$
   570^II recommend that you **always** put parentheses around a [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m$
   571^Iexpression when you're doing something with the returned value, as in$
   572^Ithe above example.  The parentheses aren't always necessary, but it's$
   573^Ieasier to always add them instead of having to remember when they're$
   574^Ineeded.$
   575^I$
   576^I(PEP 342 explains the exact rules, which are that a$
   577^I[33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m-expression must always be parenthesized except when it$
   578^Ioccurs at the top-level expression on the right-hand side of an$
   579^Iassignment.  This means you can write [33m``[39;49;00m[33mval = yield i[39;49;00m[33m``[39;49;00m but have to$
   580^Iuse parentheses when there's an operation, as in [33m``[39;49;00m[33mval = (yield i)[39;49;00m$
   581^I[33m+ 12[39;49;00m[33m``[39;49;00m.)$
   582^I$
   583^IValues are sent into a generator by calling its$
   584^I[33m``[39;49;00m[33msend(value)[39;49;00m[33m``[39;49;00m method.  This method resumes the $
   585^Igenerator's code and the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m expression returns the specified$
   586^Ivalue.  If the regular [33m``[39;49;00m[33mnext()[39;49;00m[33m``[39;49;00m method is called, the$
   587^I[33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m returns [33m``[39;49;00m[33mNone[39;49;00m[33m``[39;49;00m.$
   588^I$
   589^IHere's a simple counter that increments by 1 and allows changing the$
   590^Ivalue of the internal counter.$
   591^I$
   592^I[33m::[39;49;00m$
   593^I$
   594^I[33m    [39;49;00m[33mdef counter (maximum):[39;49;00m$
   595^I[33m        i = 0[39;49;00m$
   596^I[33m        while i < maximum:[39;49;00m$
   597^I[33m            val = (yield i)[39;49;00m$
   598^I[33m            # If value provided, change counter[39;49;00m$
   599^I[33m            if val is not None:[39;49;00m$
   600^I[33m                i = val[39;49;00m$
   601^I[33m            else:[39;49;00m$
   602^I[33m                i += 1[39;49;00m$
   603^I[33m[39;49;00m$
   604^IAnd here's an example of changing the counter:$
   605^I$
   606^I    >>> it = counter(10)$
   607^I    >>> print it.next()$
   608^I    0$
   609^I    >>> print it.next()$
   610^I    1$
   611^I    >>> print it.send(8)$
   612^I    8$
   613^I    >>> print it.next()$
   614^I    9$
   615^I    >>> print it.next()$
   616^I    Traceback (most recent call last):$
   617^I      File [33m``[39;49;00m[33mt.py'', line 15, in ?[39;49;00m$
   618^I[33m        print it.next()[39;49;00m$
   619^I[33m    StopIteration[39;49;00m$
   620^I[33m[39;49;00m$
   621^I[33mBecause [39;49;00m[33m`[39;49;00m[33m`[39;49;00m[33myield[39;49;00m[33m``[39;49;00m will often be returning [33m``[39;49;00m[33mNone[39;49;00m[33m``[39;49;00m, you$
   622^Ishould always check for this case.  Don't just use its value in$
   623^Iexpressions unless you're sure that the [33m``[39;49;00m[33msend()[39;49;00m[33m``[39;49;00m method$
   624^Iwill be the only method used resume your generator function.$
   625^I$
   626^IIn addition to [33m``[39;49;00m[33msend()[39;49;00m[33m``[39;49;00m, there are two other new methods on$
   627^Igenerators:$
   628^I$
   629^I[34m*[39;49;00m [33m``[39;49;00m[33mthrow(type, value=None, traceback=None)[39;49;00m[33m``[39;49;00m is used to raise an exception inside the$
   630^I  generator; the exception is raised by the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m expression$
   631^I  where the generator's execution is paused.$
   632^I$
   633^I[34m*[39;49;00m [33m``[39;49;00m[33mclose()[39;49;00m[33m``[39;49;00m raises a [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m$
   634^I  exception inside the generator to terminate the iteration.  $
   635^I  On receiving this$
   636^I  exception, the generator's code must either raise$
   637^I  [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m or [33m``[39;49;00m[33mStopIteration[39;49;00m[33m``[39;49;00m; catching the $
   638^I  exception and doing anything else is illegal and will trigger$
   639^I  a [33m``[39;49;00m[33mRuntimeError[39;49;00m[33m``[39;49;00m.  [33m``[39;49;00m[33mclose()[39;49;00m[33m``[39;49;00m will also be called by $
   640^I  Python's garbage collector when the generator is garbage-collected.$
   641^I$
   642^I  If you need to run cleanup code when a [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m occurs,$
   643^I  I suggest using a [33m``[39;49;00m[33mtry: ... finally:[39;49;00m[33m``[39;49;00m suite instead of $
   644^I  catching [33m``[39;49;00m[33mGeneratorExit[39;49;00m[33m``[39;49;00m.$
   645^I$
   646^IThe cumulative effect of these changes is to turn generators from$
   647^Ione-way producers of information into both producers and consumers.$
   648^I$
   649^IGenerators also become **coroutines**, a more generalized form of$
   650^Isubroutines.  Subroutines are entered at one point and exited at$
   651^Ianother point (the top of the function, and a [33m``[39;49;00m[33mreturn[39;49;00m[33m``[39;49;00m$
   652^Istatement), but coroutines can be entered, exited, and resumed at$
   653^Imany different points (the [33m``[39;49;00m[33myield[39;49;00m[33m``[39;49;00m statements).  $
   654^I$
   655^I$
   656^I[01mBuilt-in functions[39;49;00m$
   657^I[01m----------------------------------------------[39;49;00m$
   658^I$
   659^ILet's look in more detail at built-in functions often used with iterators.$
   660^I$
   661^ITwo Python's built-in functions, [33m``[39;49;00m[33mmap()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfilter()[39;49;00m[33m``[39;49;00m, are$
   662^Isomewhat obsolete; they duplicate the features of list comprehensions$
   663^Ibut return actual lists instead of iterators.  $
   664^I$
   665^I[33m``[39;49;00m[33mmap(f, iterA, iterB, ...)[39;49;00m[33m``[39;49;00m returns a list containing [33m``[39;49;00m[33mf(iterA[0],[39;49;00m$
   666^I[33miterB[0]), f(iterA[1], iterB[1]), f(iterA[2], iterB[2]), ...[39;49;00m[33m``[39;49;00m.  $
   667^I$
   668^I[33m::[39;49;00m$
   669^I$
   670^I[33m    [39;49;00m[33mdef upper(s):[39;49;00m$
   671^I[33m        return s.upper()[39;49;00m$
   672^I[33m    map(upper, ['sentence', 'fragment']) =>[39;49;00m$
   673^I[33m      ['SENTENCE', 'FRAGMENT'][39;49;00m$
   674^I[33m[39;49;00m$
   675^I[33m    [upper(s) for s in ['sentence', 'fragment']] =>[39;49;00m$
   676^I[33m      ['SENTENCE', 'FRAGMENT'][39;49;00m$
   677^I[33m[39;49;00m$
   678^IAs shown above, you can achieve the same effect with a list$
   679^Icomprehension.  The [33m``[39;49;00m[33mitertools.imap()[39;49;00m[33m``[39;49;00m function does the same thing$
   680^Ibut can handle infinite iterators; it'll be discussed later, in the section on $
   681^Ithe [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module.$
   682^I$
   683^I[33m``[39;49;00m[33mfilter(predicate, iter)[39;49;00m[33m``[39;49;00m returns a list $
   684^Ithat contains all the sequence elements that meet a certain condition,$
   685^Iand is similarly duplicated by list comprehensions.$
   686^IA **predicate** is a function that returns the truth value of$
   687^Isome condition; for use with [33m``[39;49;00m[33mfilter()[39;49;00m[33m``[39;49;00m, the predicate must take a $
   688^Isingle value.  $
   689^I$
   690^I[33m::[39;49;00m$
   691^I$
   692^I[33m    [39;49;00m[33mdef is_even(x):[39;49;00m$
   693^I[33m        return (x % 2) == 0[39;49;00m$
   694^I[33m[39;49;00m$
   695^I[33m    filter(is_even, range(10)) =>[39;49;00m$
   696^I[33m      [0, 2, 4, 6, 8][39;49;00m$
   697^I[33m[39;49;00m$
   698^IThis can also be written as a list comprehension[33m::[39;49;00m$
   699^I$
   700^I[33m    [39;49;00m[33m>>> [x for x in range(10) if is_even(x)][39;49;00m$
   701^I[33m    [0, 2, 4, 6, 8][39;49;00m$
   702^I[33m[39;49;00m$
   703^I[33m``[39;49;00m[33mfilter()[39;49;00m[33m``[39;49;00m also has a counterpart in the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module,$
   704^I[33m``[39;49;00m[33mitertools.ifilter()[39;49;00m[33m``[39;49;00m, that returns an iterator and $
   705^Ican therefore handle infinite sequences just as [33m``[39;49;00m[33mitertools.imap()[39;49;00m[33m``[39;49;00m can.$
   706^I$
   707^I[33m``[39;49;00m[33mreduce(func, iter, [initial_value])[39;49;00m[33m``[39;49;00m doesn't have a counterpart in$
   708^Ithe [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module because it cumulatively performs an operation$
   709^Ion all the iterable's elements and therefore can't be applied to$
   710^Iinfinite iterables.  [33m``[39;49;00m[33mfunc[39;49;00m[33m``[39;49;00m must be a function that takes two elements$
   711^Iand returns a single value.  [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m takes the first two elements$
   712^IA and B returned by the iterator and calculates [33m``[39;49;00m[33mfunc(A, B)[39;49;00m[33m``[39;49;00m.  It$
   713^Ithen requests the third element, C, calculates [33m``[39;49;00m[33mfunc(func(A, B),[39;49;00m$
   714^I[33mC)[39;49;00m[33m``[39;49;00m, combines this result with the fourth element returned, and$
   715^Icontinues until the iterable is exhausted.  If the iterable returns no$
   716^Ivalues at all, a [33m``[39;49;00m[33mTypeError[39;49;00m[33m``[39;49;00m exception is raised.  If the initial$
   717^Ivalue is supplied, it's used as a starting point and$
   718^I[33m``[39;49;00m[33mfunc(initial_value, A)[39;49;00m[33m``[39;49;00m is the first calculation.$
   719^I$
   720^I[33m::[39;49;00m$
   721^I$
   722^I[33m    [39;49;00m[33mimport operator[39;49;00m$
   723^I[33m    reduce(operator.concat, ['A', 'BB', 'C']) =>[39;49;00m$
   724^I[33m      'ABBC'[39;49;00m$
   725^I[33m    reduce(operator.concat, []) =>[39;49;00m$
   726^I[33m      TypeError: reduce() of empty sequence with no initial value[39;49;00m$
   727^I[33m    reduce(operator.mul, [1,2,3], 1) =>[39;49;00m$
   728^I[33m      6[39;49;00m$
   729^I[33m    reduce(operator.mul, [], 1) =>[39;49;00m$
   730^I[33m      1[39;49;00m$
   731^I[33m[39;49;00m$
   732^IIf you use [33m``[39;49;00m[33moperator.add[39;49;00m[33m``[39;49;00m with [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m, you'll add up all the $
   733^Ielements of the iterable.  This case is so common that there's a special$
   734^Ibuilt-in called [33m``[39;49;00m[33msum()[39;49;00m[33m``[39;49;00m to compute it[33m::[39;49;00m$
   735^I$
   736^I[33m    [39;49;00m[33mreduce(operator.add, [1,2,3,4], 0) =>[39;49;00m$
   737^I[33m      10[39;49;00m$
   738^I[33m    sum([1,2,3,4]) =>[39;49;00m$
   739^I[33m      10[39;49;00m$
   740^I[33m    sum([]) =>[39;49;00m$
   741^I[33m      0[39;49;00m$
   742^I[33m[39;49;00m$
   743^IFor many uses of [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m, though, it can be clearer to just write$
   744^Ithe obvious [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m loop[33m::[39;49;00m$
   745^I$
   746^I[33m    [39;49;00m[33m# Instead of:[39;49;00m$
   747^I[33m    product = reduce(operator.mul, [1,2,3], 1)[39;49;00m$
   748^I[33m[39;49;00m$
   749^I[33m    # You can write:[39;49;00m$
   750^I[33m    product = 1[39;49;00m$
   751^I[33m    for i in [1,2,3]:[39;49;00m$
   752^I[33m        product *= i[39;49;00m$
   753^I[33m[39;49;00m$
   754^I[33m[39;49;00m$
   755^I[33m``[39;49;00m[33menumerate(iter)[39;49;00m[33m``[39;49;00m counts off the elements in the iterable, returning$
   756^I2-tuples containing the count and each element.$
   757^I$
   758^I[33m::[39;49;00m$
   759^I$
   760^I[33m    [39;49;00m[33menumerate(['subject', 'verb', 'object']) =>[39;49;00m$
   761^I[33m      (0, 'subject'), (1, 'verb'), (2, 'object')[39;49;00m$
   762^I[33m[39;49;00m$
   763^I[33m``[39;49;00m[33menumerate()[39;49;00m[33m``[39;49;00m is often used when looping through a list $
   764^Iand recording the indexes at which certain conditions are met[33m::[39;49;00m$
   765^I$
   766^I[33m    [39;49;00m[33mf = open('data.txt', 'r')[39;49;00m$
   767^I[33m    for i, line in enumerate(f):[39;49;00m$
   768^I[33m        if line.strip() == '':[39;49;00m$
   769^I[33m            print 'Blank line at line #%i' % i[39;49;00m$
   770^I[33m[39;49;00m$
   771^I[33m``[39;49;00m[33msorted(iterable, [cmp=None], [key=None], [reverse=False)[39;49;00m[33m``[39;49;00m $
   772^Icollects all the elements of the iterable into a list, sorts $
   773^Ithe list, and returns the sorted result.  The [33m``[39;49;00m[33mcmp[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mkey[39;49;00m[33m``[39;49;00m, $
   774^Iand [33m``[39;49;00m[33mreverse[39;49;00m[33m``[39;49;00m arguments are passed through to the $
   775^Iconstructed list's [33m``[39;49;00m[33m.sort()[39;49;00m[33m``[39;49;00m method.$
   776^I$
   777^I[33m::[39;49;00m$
   778^I$
   779^I[33m    [39;49;00m[33mimport random[39;49;00m$
   780^I[33m    # Generate 8 random numbers between [0, 10000)[39;49;00m$
   781^I[33m    rand_list = random.sample(range(10000), 8)[39;49;00m$
   782^I[33m    rand_list =>[39;49;00m$
   783^I[33m      [769, 7953, 9828, 6431, 8442, 9878, 6213, 2207][39;49;00m$
   784^I[33m    sorted(rand_list) =>[39;49;00m$
   785^I[33m      [769, 2207, 6213, 6431, 7953, 8442, 9828, 9878][39;49;00m$
   786^I[33m    sorted(rand_list, reverse=True) =>[39;49;00m$
   787^I[33m      [9878, 9828, 8442, 7953, 6431, 6213, 2207, 769][39;49;00m$
   788^I[33m[39;49;00m$
   789^I(For a more detailed discussion of sorting, see the Sorting mini-HOWTO$
   790^Iin the Python wiki at http://wiki.python.org/moin/HowTo/Sorting.)$
   791^I$
   792^IThe [33m``[39;49;00m[33many(iter)[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mall(iter)[39;49;00m[33m``[39;49;00m built-ins look at $
   793^Ithe truth values of an iterable's contents.  [33m``[39;49;00m[33many()[39;49;00m[33m``[39;49;00m returns $
   794^ITrue if any element in the iterable is a true value, and [33m``[39;49;00m[33mall()[39;49;00m[33m``[39;49;00m $
   795^Ireturns True if all of the elements are true values[33m::[39;49;00m$
   796^I$
   797^I[33m    [39;49;00m[33many([0,1,0]) =>[39;49;00m$
   798^I[33m      True[39;49;00m$
   799^I[33m    any([0,0,0]) =>[39;49;00m$
   800^I[33m      False[39;49;00m$
   801^I[33m    any([1,1,1]) =>[39;49;00m$
   802^I[33m      True[39;49;00m$
   803^I[33m    all([0,1,0]) =>[39;49;00m$
   804^I[33m      False[39;49;00m$
   805^I[33m    all([0,0,0]) => [39;49;00m$
   806^I[33m      False[39;49;00m$
   807^I[33m    all([1,1,1]) =>[39;49;00m$
   808^I[33m      True[39;49;00m$
   809^I[33m[39;49;00m$
   810^I[33m[39;49;00m$
   811^I[01mSmall functions and the lambda statement[39;49;00m$
   812^I[01m----------------------------------------------[39;49;00m$
   813^I$
   814^IWhen writing functional-style programs, you'll often need little$
   815^Ifunctions that act as predicates or that combine elements in some way.$
   816^I$
   817^IIf there's a Python built-in or a module function that's suitable, you$
   818^Idon't need to define a new function at all[33m::[39;49;00m$
   819^I$
   820^I[33m        [39;49;00m[33mstripped_lines = [line.strip() for line in lines][39;49;00m$
   821^I[33m        existing_files = filter(os.path.exists, file_list)[39;49;00m$
   822^I[33m[39;49;00m$
   823^IIf the function you need doesn't exist, you need to write it.  One way$
   824^Ito write small functions is to use the [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m statement.  [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m$
   825^Itakes a number of parameters and an expression combining these parameters,$
   826^Iand creates a small function that returns the value of the expression[33m::[39;49;00m$
   827^I$
   828^I[33m        [39;49;00m[33mlowercase = lambda x: x.lower()[39;49;00m$
   829^I[33m[39;49;00m$
   830^I[33m        print_assign = lambda name, value: name + '=' + str(value)[39;49;00m$
   831^I[33m[39;49;00m$
   832^I[33m        adder = lambda x, y: x+y[39;49;00m$
   833^I[33m[39;49;00m$
   834^IAn alternative is to just use the [33m``[39;49;00m[33mdef[39;49;00m[33m``[39;49;00m statement and define a$
   835^Ifunction in the usual way[33m::[39;49;00m$
   836^I$
   837^I[33m        [39;49;00m[33mdef lowercase(x):[39;49;00m$
   838^I[33m            return x.lower()[39;49;00m$
   839^I[33m[39;49;00m$
   840^I[33m        def print_assign(name, value):[39;49;00m$
   841^I[33m            return name + '=' + str(value)[39;49;00m$
   842^I[33m[39;49;00m$
   843^I[33m        def adder(x,y):[39;49;00m$
   844^I[33m            return x + y[39;49;00m$
   845^I[33m[39;49;00m$
   846^IWhich alternative is preferable?  That's a style question; my usual$
   847^Icourse is to avoid using [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m.$
   848^I$
   849^IOne reason for my preference is that [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m is quite limited in$
   850^Ithe functions it can define.  The result has to be computable as a$
   851^Isingle expression, which means you can't have multiway$
   852^I[33m``[39;49;00m[33mif... elif... else[39;49;00m[33m``[39;49;00m comparisons or [33m``[39;49;00m[33mtry... except[39;49;00m[33m``[39;49;00m statements.$
   853^IIf you try to do too much in a [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m statement, you'll end up$
   854^Iwith an overly complicated expression that's hard to read.  Quick,$
   855^Iwhat's the following code doing?$
   856^I$
   857^I[33m::[39;49;00m$
   858^I$
   859^I[33m    [39;49;00m[33mtotal = reduce(lambda a, b: (0, a[1] + b[1]), items)[1][39;49;00m$
   860^I[33m[39;49;00m$
   861^IYou can figure it out, but it takes time to disentangle the expression$
   862^Ito figure out what's going on.  Using a short nested$
   863^I[33m``[39;49;00m[33mdef[39;49;00m[33m``[39;49;00m statements makes things a little bit better[33m::[39;49;00m$
   864^I$
   865^I[33m    [39;49;00m[33mdef combine (a, b):[39;49;00m$
   866^I[33m        return 0, a[1] + b[1][39;49;00m$
   867^I[33m[39;49;00m$
   868^I[33m    total = reduce(combine, items)[1][39;49;00m$
   869^I[33m[39;49;00m$
   870^IBut it would be best of all if I had simply used a [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m loop[33m::[39;49;00m$
   871^I$
   872^I[33m     [39;49;00m[33mtotal = 0[39;49;00m$
   873^I[33m     for a, b in items:[39;49;00m$
   874^I[33m         total += b[39;49;00m$
   875^I[33m[39;49;00m$
   876^IOr the [33m``[39;49;00m[33msum()[39;49;00m[33m``[39;49;00m built-in and a generator expression[33m::[39;49;00m$
   877^I$
   878^I[33m     [39;49;00m[33mtotal = sum(b for a,b in items)[39;49;00m$
   879^I[33m[39;49;00m$
   880^IMany uses of [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m are clearer when written as [33m``[39;49;00m[33mfor[39;49;00m[33m``[39;49;00m loops.$
   881^I$
   882^IFredrik Lundh once suggested the following set of rules for refactoring $
   883^Iuses of [33m``[39;49;00m[33mlambda[39;49;00m[33m``[39;49;00m:$
   884^I$
   885^I[34m1)[39;49;00m Write a lambda function.$
   886^I[34m2)[39;49;00m Write a comment explaining what the heck that lambda does.$
   887^I[34m3)[39;49;00m Study the comment for a while, and think of a name that captures$
   888^I   the essence of the comment.$
   889^I[34m4)[39;49;00m Convert the lambda to a def statement, using that name.$
   890^I[34m5)[39;49;00m Remove the comment.$
   891^I$
   892^II really like these rules, but you're free to disagree that this $
   893^Ilambda-free style is better.$
   894^I$
   895^I$
   896^I[01mThe itertools module[39;49;00m$
   897^I[01m-----------------------[39;49;00m$
   898^I$
   899^IThe [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module contains a number of commonly-used iterators$
   900^Ias well as functions for combining several iterators.  This section$
   901^Iwill introduce the module's contents by showing small examples.$
   902^I$
   903^IThe module's functions fall into a few broad classes:$
   904^I$
   905^I[34m*[39;49;00m Functions that create a new iterator based on an existing iterator.$
   906^I[34m*[39;49;00m Functions for treating an iterator's elements as function arguments.$
   907^I[34m*[39;49;00m Functions for selecting portions of an iterator's output.$
   908^I[34m*[39;49;00m A function for grouping an iterator's output.$
   909^I$
   910^I[01mCreating new iterators[39;49;00m$
   911^I[01m''''''''''''''''''''''[39;49;00m$
   912^I$
   913^I[33m``[39;49;00m[33mitertools.count(n)[39;49;00m[33m``[39;49;00m returns an infinite stream of$
   914^Iintegers, increasing by 1 each time.  You can optionally supply the$
   915^Istarting number, which defaults to 0[33m::[39;49;00m$
   916^I$
   917^I[33m        [39;49;00m[33mitertools.count() =>[39;49;00m$
   918^I[33m          0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...[39;49;00m$
   919^I[33m        itertools.count(10) =>[39;49;00m$
   920^I[33m          10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...[39;49;00m$
   921^I[33m[39;49;00m$
   922^I[33m``[39;49;00m[33mitertools.cycle(iter)[39;49;00m[33m``[39;49;00m saves a copy of the contents of a provided$
   923^Iiterable and returns a new iterator that returns its elements from$
   924^Ifirst to last.  The new iterator will repeat these elements infinitely.$
   925^I$
   926^I[33m::[39;49;00m$
   927^I$
   928^I[33m        [39;49;00m[33mitertools.cycle([1,2,3,4,5]) =>[39;49;00m$
   929^I[33m          1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...[39;49;00m$
   930^I[33m[39;49;00m$
   931^I[33m``[39;49;00m[33mitertools.repeat(elem, [n])[39;49;00m[33m``[39;49;00m returns the provided element [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m$
   932^Itimes, or returns the element endlessly if [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m is not provided.$
   933^I$
   934^I[33m::[39;49;00m$
   935^I$
   936^I[33m    [39;49;00m[33mitertools.repeat('abc') =>[39;49;00m$
   937^I[33m      abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, ...[39;49;00m$
   938^I[33m    itertools.repeat('abc', 5) =>[39;49;00m$
   939^I[33m      abc, abc, abc, abc, abc[39;49;00m$
   940^I[33m[39;49;00m$
   941^I[33m``[39;49;00m[33mitertools.chain(iterA, iterB, ...)[39;49;00m[33m``[39;49;00m takes an arbitrary number of$
   942^Iiterables as input, and returns all the elements of the first$
   943^Iiterator, then all the elements of the second, and so on, until all of$
   944^Ithe iterables have been exhausted.$
   945^I$
   946^I[33m::[39;49;00m$
   947^I$
   948^I[33m    [39;49;00m[33mitertools.chain(['a', 'b', 'c'], (1, 2, 3)) =>[39;49;00m$
   949^I[33m      a, b, c, 1, 2, 3[39;49;00m$
   950^I[33m[39;49;00m$
   951^I[33m``[39;49;00m[33mitertools.izip(iterA, iterB, ...)[39;49;00m[33m``[39;49;00m takes one element from each iterable$
   952^Iand returns them in a tuple[33m::[39;49;00m$
   953^I$
   954^I[33m    [39;49;00m[33mitertools.izip(['a', 'b', 'c'], (1, 2, 3)) =>[39;49;00m$
   955^I[33m      ('a', 1), ('b', 2), ('c', 3)[39;49;00m$
   956^I[33m[39;49;00m$
   957^IIt's similiar to the built-in [33m``[39;49;00m[33mzip()[39;49;00m[33m``[39;49;00m function, but doesn't$
   958^Iconstruct an in-memory list and exhaust all the input iterators before$
   959^Ireturning; instead tuples are constructed and returned only if they're$
   960^Irequested.  (The technical term for this behaviour is $
   961^I[33m`lazy evaluation [39;49;00m[33m<http://en.wikipedia.org/wiki/Lazy_evaluation>[39;49;00m[33m`__[39;49;00m.)$
   962^I$
   963^IThis iterator is intended to be used with iterables that are all of$
   964^Ithe same length.  If the iterables are of different lengths, the$
   965^Iresulting stream will be the same length as the shortest iterable.$
   966^I$
   967^I[33m::[39;49;00m$
   968^I$
   969^I[33m    [39;49;00m[33mitertools.izip(['a', 'b'], (1, 2, 3)) =>[39;49;00m$
   970^I[33m      ('a', 1), ('b', 2)[39;49;00m$
   971^I[33m[39;49;00m$
   972^IYou should avoid doing this, though, because an element may be taken$
   973^Ifrom the longer iterators and discarded.  This means you can't go on$
   974^Ito use the iterators further because you risk skipping a discarded$
   975^Ielement.$
   976^I$
   977^I[33m``[39;49;00m[33mitertools.islice(iter, [start], stop, [step])[39;49;00m[33m``[39;49;00m returns a stream$
   978^Ithat's a slice of the iterator.  With a single [33m``[39;49;00m[33mstop[39;49;00m[33m``[39;49;00m argument, $
   979^Iit will return the first [33m``[39;49;00m[33mstop[39;49;00m[33m``[39;49;00m$
   980^Ielements.  If you supply a starting index, you'll get [33m``[39;49;00m[33mstop-start[39;49;00m[33m``[39;49;00m$
   981^Ielements, and if you supply a value for [33m``[39;49;00m[33mstep[39;49;00m[33m``[39;49;00m, elements will be$
   982^Iskipped accordingly.  Unlike Python's string and list slicing, you$
   983^Ican't use negative values for [33m``[39;49;00m[33mstart[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mstop[39;49;00m[33m``[39;49;00m, or [33m``[39;49;00m[33mstep[39;49;00m[33m``[39;49;00m.$
   984^I$
   985^I[33m::[39;49;00m$
   986^I$
   987^I[33m    [39;49;00m[33mitertools.islice(range(10), 8) =>[39;49;00m$
   988^I[33m      0, 1, 2, 3, 4, 5, 6, 7[39;49;00m$
   989^I[33m    itertools.islice(range(10), 2, 8) =>[39;49;00m$
   990^I[33m      2, 3, 4, 5, 6, 7[39;49;00m$
   991^I[33m    itertools.islice(range(10), 2, 8, 2) =>[39;49;00m$
   992^I[33m      2, 4, 6[39;49;00m$
   993^I[33m[39;49;00m$
   994^I[33m``[39;49;00m[33mitertools.tee(iter, [n])[39;49;00m[33m``[39;49;00m replicates an iterator; it returns [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m$
   995^Iindependent iterators that will all return the contents of the source$
   996^Iiterator.  If you don't supply a value for [33m``[39;49;00m[33mn[39;49;00m[33m``[39;49;00m, the default is 2.$
   997^IReplicating iterators requires saving some of the contents of the source$
   998^Iiterator, so this can consume significant memory if the iterator is large$
   999^Iand one of the new iterators is consumed more than the others.$
  1000^I$
  1001^I[33m::[39;49;00m$
  1002^I$
  1003^I[33m        [39;49;00m[33mitertools.tee( itertools.count() ) =>[39;49;00m$
  1004^I[33m           iterA, iterB[39;49;00m$
  1005^I[33m[39;49;00m$
  1006^I[33m        where iterA ->[39;49;00m$
  1007^I[33m           0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...[39;49;00m$
  1008^I[33m[39;49;00m$
  1009^I[33m        and   iterB ->[39;49;00m$
  1010^I[33m           0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...[39;49;00m$
  1011^I[33m[39;49;00m$
  1012^I[33m[39;49;00m$
  1013^I[01mCalling functions on elements[39;49;00m$
  1014^I[01m'''''''''''''''''''''''''''''[39;49;00m$
  1015^I$
  1016^ITwo functions are used for calling other functions on the contents of an$
  1017^Iiterable.$
  1018^I$
  1019^I[33m``[39;49;00m[33mitertools.imap(f, iterA, iterB, ...)[39;49;00m[33m``[39;49;00m returns $
  1020^Ia stream containing [33m``[39;49;00m[33mf(iterA[0], iterB[0]), f(iterA[1], iterB[1]),[39;49;00m$
  1021^I[33mf(iterA[2], iterB[2]), ...[39;49;00m[33m``[39;49;00m[33m::[39;49;00m$
  1022^I$
  1023^I[33m    [39;49;00m[33mitertools.imap(operator.add, [5, 6, 5], [1, 2, 3]) =>[39;49;00m$
  1024^I[33m      6, 8, 8[39;49;00m$
  1025^I[33m[39;49;00m$
  1026^IThe [33m``[39;49;00m[33moperator[39;49;00m[33m``[39;49;00m module contains a set of functions $
  1027^Icorresponding to Python's operators.  Some examples are $
  1028^I[33m``[39;49;00m[33moperator.add(a, b)[39;49;00m[33m``[39;49;00m (adds two values), $
  1029^I[33m``[39;49;00m[33moperator.ne(a, b)[39;49;00m[33m``[39;49;00m (same as [33m``[39;49;00m[33ma!=b[39;49;00m[33m``[39;49;00m),$
  1030^Iand $
  1031^I[33m``[39;49;00m[33moperator.attrgetter('id')[39;49;00m[33m``[39;49;00m (returns a callable that$
  1032^Ifetches the [33m``[39;49;00m[33m"id"[39;49;00m[33m``[39;49;00m attribute).$
  1033^I$
  1034^I[33m``[39;49;00m[33mitertools.starmap(func, iter)[39;49;00m[33m``[39;49;00m assumes that the iterable will $
  1035^Ireturn a stream of tuples, and calls [33m``[39;49;00m[33mf()[39;49;00m[33m``[39;49;00m using these tuples as the $
  1036^Iarguments[33m::[39;49;00m$
  1037^I$
  1038^I[33m    [39;49;00m[33mitertools.starmap(os.path.join, [39;49;00m$
  1039^I[33m                      [('/usr', 'bin', 'java'), ('/bin', 'python'),[39;49;00m$
  1040^I[33m                       ('/usr', 'bin', 'perl'),('/usr', 'bin', 'ruby')])[39;49;00m$
  1041^I[33m    =>[39;49;00m$
  1042^I[33m      /usr/bin/java, /bin/python, /usr/bin/perl, /usr/bin/ruby[39;49;00m$
  1043^I[33m[39;49;00m$
  1044^I[33m[39;49;00m$
  1045^I[01mSelecting elements[39;49;00m$
  1046^I[01m''''''''''''''''''[39;49;00m$
  1047^I$
  1048^IAnother group of functions chooses a subset of an iterator's elements$
  1049^Ibased on a predicate.$
  1050^I$
  1051^I[33m``[39;49;00m[33mitertools.ifilter(predicate, iter)[39;49;00m[33m``[39;49;00m returns all the elements for$
  1052^Iwhich the predicate returns true[33m::[39;49;00m$
  1053^I$
  1054^I[33m    [39;49;00m[33mdef is_even(x):[39;49;00m$
  1055^I[33m        return (x % 2) == 0[39;49;00m$
  1056^I[33m[39;49;00m$
  1057^I[33m    itertools.ifilter(is_even, itertools.count()) =>[39;49;00m$
  1058^I[33m      0, 2, 4, 6, 8, 10, 12, 14, ...[39;49;00m$
  1059^I[33m[39;49;00m$
  1060^I[33m``[39;49;00m[33mitertools.ifilterfalse(predicate, iter)[39;49;00m[33m``[39;49;00m is the opposite, $
  1061^Ireturning all elements for which the predicate returns false[33m::[39;49;00m$
  1062^I$
  1063^I[33m    [39;49;00m[33mitertools.ifilterfalse(is_even, itertools.count()) =>[39;49;00m$
  1064^I[33m      1, 3, 5, 7, 9, 11, 13, 15, ...[39;49;00m$
  1065^I[33m[39;49;00m$
  1066^I[33m``[39;49;00m[33mitertools.takewhile(predicate, iter)[39;49;00m[33m``[39;49;00m returns elements for as long$
  1067^Ias the predicate returns true.  Once the predicate returns false, $
  1068^Ithe iterator will signal the end of its results.$
  1069^I$
  1070^I[33m::[39;49;00m$
  1071^I$
  1072^I[33m    [39;49;00m[33mdef less_than_10(x):[39;49;00m$
  1073^I[33m        return (x < 10)[39;49;00m$
  1074^I[33m[39;49;00m$
  1075^I[33m    itertools.takewhile(less_than_10, itertools.count()) =>[39;49;00m$
  1076^I[33m      0, 1, 2, 3, 4, 5, 6, 7, 8, 9[39;49;00m$
  1077^I[33m[39;49;00m$
  1078^I[33m    itertools.takewhile(is_even, itertools.count()) =>[39;49;00m$
  1079^I[33m      0[39;49;00m$
  1080^I[33m[39;49;00m$
  1081^I[33m``[39;49;00m[33mitertools.dropwhile(predicate, iter)[39;49;00m[33m``[39;49;00m discards elements while the$
  1082^Ipredicate returns true, and then returns the rest of the iterable's$
  1083^Iresults.$
  1084^I$
  1085^I[33m::[39;49;00m$
  1086^I$
  1087^I[33m    [39;49;00m[33mitertools.dropwhile(less_than_10, itertools.count()) =>[39;49;00m$
  1088^I[33m      10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...[39;49;00m$
  1089^I[33m[39;49;00m$
  1090^I[33m    itertools.dropwhile(is_even, itertools.count()) =>[39;49;00m$
  1091^I[33m      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...[39;49;00m$
  1092^I[33m[39;49;00m$
  1093^I[33m[39;49;00m$
  1094^I[01mGrouping elements[39;49;00m$
  1095^I[01m'''''''''''''''''[39;49;00m$
  1096^I$
  1097^IThe last function I'll discuss, [33m``[39;49;00m[33mitertools.groupby(iter,[39;49;00m$
  1098^I[33mkey_func=None)[39;49;00m[33m``[39;49;00m, is the most complicated.  [33m``[39;49;00m[33mkey_func(elem)[39;49;00m[33m``[39;49;00m is a$
  1099^Ifunction that can compute a key value for each element returned by the$
  1100^Iiterable.  If you don't supply a key function, the key is simply each$
  1101^Ielement itself.$
  1102^I$
  1103^I[33m``[39;49;00m[33mgroupby()[39;49;00m[33m``[39;49;00m collects all the consecutive elements from the$
  1104^Iunderlying iterable that have the same key value, and returns a stream$
  1105^Iof 2-tuples containing a key value and an iterator for the elements$
  1106^Iwith that key.  $
  1107^I$
  1108^I[33m::[39;49;00m$
  1109^I$
  1110^I[33m    [39;49;00m[33mcity_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'), [39;49;00m$
  1111^I[33m                 ('Anchorage', 'AK'), ('Nome', 'AK'),[39;49;00m$
  1112^I[33m                 ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'), [39;49;00m$
  1113^I[33m                 ...[39;49;00m$
  1114^I[33m                ][39;49;00m$
  1115^I[33m[39;49;00m$
  1116^I[33m    def get_state ((city, state)):[39;49;00m$
  1117^I[33m        return state[39;49;00m$
  1118^I[33m[39;49;00m$
  1119^I[33m    itertools.groupby(city_list, get_state) =>[39;49;00m$
  1120^I[33m      ('AL', iterator-1),[39;49;00m$
  1121^I[33m      ('AK', iterator-2),[39;49;00m$
  1122^I[33m      ('AZ', iterator-3), ...[39;49;00m$
  1123^I[33m[39;49;00m$
  1124^I[33m    where[39;49;00m$
  1125^I[33m    iterator-1 =>[39;49;00m$
  1126^I[33m      ('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')[39;49;00m$
  1127^I[33m    iterator-2 => [39;49;00m$
  1128^I[33m      ('Anchorage', 'AK'), ('Nome', 'AK')[39;49;00m$
  1129^I[33m    iterator-3 =>[39;49;00m$
  1130^I[33m      ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')[39;49;00m$
  1131^I[33m[39;49;00m$
  1132^I[33m``[39;49;00m[33mgroupby()[39;49;00m[33m``[39;49;00m assumes that the underlying iterable's contents will$
  1133^Ialready be sorted based on the key.  Note that the returned iterators$
  1134^Ialso use the underlying iterable, so you have to consume the results$
  1135^Iof iterator-1 before requesting iterator-2 and its corresponding key.$
  1136^I$
  1137^I$
  1138^I[01mThe functools module[39;49;00m$
  1139^I[01m----------------------------------------------[39;49;00m$
  1140^I$
  1141^IThe [33m``[39;49;00m[33mfunctools[39;49;00m[33m``[39;49;00m module in Python 2.5 contains some higher-order$
  1142^Ifunctions.  A **higher-order function** takes one or more functions as$
  1143^Iinput and returns a new function.  The most useful tool in this module$
  1144^Iis the [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m function.$
  1145^I$
  1146^IFor programs written in a functional style, you'll sometimes want to$
  1147^Iconstruct variants of existing functions that have some of the$
  1148^Iparameters filled in.  Consider a Python function [33m``[39;49;00m[33mf(a, b, c)[39;49;00m[33m``[39;49;00m; you$
  1149^Imay wish to create a new function [33m``[39;49;00m[33mg(b, c)[39;49;00m[33m``[39;49;00m that's equivalent to$
  1150^I[33m``[39;49;00m[33mf(1, b, c)[39;49;00m[33m``[39;49;00m; you're filling in a value for one of [33m``[39;49;00m[33mf()[39;49;00m[33m``[39;49;00m's parameters.  $
  1151^IThis is called "partial function application".$
  1152^I$
  1153^IThe constructor for [33m``[39;49;00m[33mpartial[39;49;00m[33m``[39;49;00m takes the arguments [33m``[39;49;00m[33m(function, arg1,[39;49;00m$
  1154^I[33marg2, ... kwarg1=value1, kwarg2=value2)[39;49;00m[33m``[39;49;00m.  The resulting object is$
  1155^Icallable, so you can just call it to invoke [33m``[39;49;00m[33mfunction[39;49;00m[33m``[39;49;00m with the$
  1156^Ifilled-in arguments.$
  1157^I$
  1158^IHere's a small but realistic example[33m::[39;49;00m$
  1159^I$
  1160^I[33m    [39;49;00m[33mimport functools[39;49;00m$
  1161^I[33m[39;49;00m$
  1162^I[33m    def log (message, subsystem):[39;49;00m$
  1163^I[33m        "Write the contents of 'message' to the specified subsystem."[39;49;00m$
  1164^I[33m        print '%s: %s' % (subsystem, message)[39;49;00m$
  1165^I[33m        ...[39;49;00m$
  1166^I[33m[39;49;00m$
  1167^I[33m    server_log = functools.partial(log, subsystem='server')[39;49;00m$
  1168^I[33m    server_log('Unable to open socket')[39;49;00m$
  1169^I[33m[39;49;00m$
  1170^I[33m[39;49;00m$
  1171^I[01mThe operator module[39;49;00m$
  1172^I[01m-------------------[39;49;00m$
  1173^I$
  1174^IThe [33m``[39;49;00m[33moperator[39;49;00m[33m``[39;49;00m module was mentioned earlier.  It contains a set of$
  1175^Ifunctions corresponding to Python's operators.  These functions $
  1176^Iare often useful in functional-style code because they save you $
  1177^Ifrom writing trivial functions that perform a single operation.$
  1178^I$
  1179^ISome of the functions in this module are:$
  1180^I$
  1181^I[34m*[39;49;00m Math operations: [33m``[39;49;00m[33madd()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33msub()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mmul()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mdiv()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mfloordiv()[39;49;00m[33m``[39;49;00m,$
  1182^I  [33m``[39;49;00m[33mabs()[39;49;00m[33m``[39;49;00m, ...$
  1183^I[34m*[39;49;00m Logical operations: [33m``[39;49;00m[33mnot_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mtruth()[39;49;00m[33m``[39;49;00m.$
  1184^I[34m*[39;49;00m Bitwise operations: [33m``[39;49;00m[33mand_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mor_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33minvert()[39;49;00m[33m``[39;49;00m.$
  1185^I[34m*[39;49;00m Comparisons: [33m``[39;49;00m[33meq()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mne()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mlt()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mle()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mgt()[39;49;00m[33m``[39;49;00m, and [33m``[39;49;00m[33mge()[39;49;00m[33m``[39;49;00m.$
  1186^I[34m*[39;49;00m Object identity: [33m``[39;49;00m[33mis_()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mis_not()[39;49;00m[33m``[39;49;00m.$
  1187^I$
  1188^IConsult [33m`the operator module's documentation [39;49;00m[33m<http://docs.python.org/lib/module-operator.html>[39;49;00m[33m`__[39;49;00m for a complete$
  1189^Ilist.$
  1190^I$
  1191^I$
  1192^I$
  1193^I[01mThe functional module[39;49;00m$
  1194^I[01m---------------------[39;49;00m$
  1195^I$
  1196^ICollin Winter's [33m`functional module [39;49;00m[33m<http://oakwinter.com/code/functional/>[39;49;00m[33m`__[39;49;00m $
  1197^Iprovides a number of more$
  1198^Iadvanced tools for functional programming. It also reimplements$
  1199^Iseveral Python built-ins, trying to make them more intuitive to those$
  1200^Iused to functional programming in other languages.$
  1201^I$
  1202^IThis section contains an introduction to some of the most important$
  1203^Ifunctions in [33m``[39;49;00m[33mfunctional[39;49;00m[33m``[39;49;00m; full documentation can be found at `the$
  1204^Iproject's website <http://oakwinter.com/code/functional/documentation/>`__.$
  1205^I$
  1206^I[33m``[39;49;00m[33mcompose(outer, inner, unpack=False)[39;49;00m[33m``[39;49;00m$
  1207^I$
  1208^IThe [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m function implements function composition.$
  1209^IIn other words, it returns a wrapper around the [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m callables, such$
  1210^Ithat the return value from [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m is fed directly to [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m.  That is,$
  1211^I$
  1212^I[33m::[39;49;00m$
  1213^I$
  1214^I[33m        [39;49;00m[33m>>> def add(a, b):[39;49;00m$
  1215^I[33m        ...     return a + b[39;49;00m$
  1216^I[33m        ...[39;49;00m$
  1217^I[33m        >>> def double(a):[39;49;00m$
  1218^I[33m        ...     return 2 * a[39;49;00m$
  1219^I[33m        ...[39;49;00m$
  1220^I[33m        >>> compose(double, add)(5, 6)[39;49;00m$
  1221^I[33m        22[39;49;00m$
  1222^I[33m[39;49;00m$
  1223^Iis equivalent to$
  1224^I$
  1225^I[33m::[39;49;00m$
  1226^I$
  1227^I[33m        [39;49;00m[33m>>> double(add(5, 6))[39;49;00m$
  1228^I[33m        22[39;49;00m$
  1229^I[33m                    [39;49;00m$
  1230^IThe [33m``[39;49;00m[33munpack[39;49;00m[33m``[39;49;00m keyword is provided to work around the fact that Python functions are not always$
  1231^I[33m`fully curried [39;49;00m[33m<http://en.wikipedia.org/wiki/Currying>[39;49;00m[33m`__[39;49;00m.$
  1232^IBy default, it is expected that the [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m function will return a single object and that the [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m$
  1233^Ifunction will take a single argument. Setting the [33m``[39;49;00m[33munpack[39;49;00m[33m``[39;49;00m argument causes [33m``[39;49;00m[33mcompose[39;49;00m[33m``[39;49;00m to expect a$
  1234^Ituple from [33m``[39;49;00m[33minner[39;49;00m[33m``[39;49;00m which will be expanded before being passed to [33m``[39;49;00m[33mouter[39;49;00m[33m``[39;49;00m. Put simply,$
  1235^I$
  1236^I[33m::[39;49;00m$
  1237^I$
  1238^I[33m        [39;49;00m[33mcompose(f, g)(5, 6)[39;49;00m$
  1239^I[33m                    [39;49;00m$
  1240^Iis equivalent to[33m::[39;49;00m$
  1241^I$
  1242^I[33m        [39;49;00m[33mf(g(5, 6))[39;49;00m$
  1243^I[33m                    [39;49;00m$
  1244^Iwhile$
  1245^I$
  1246^I[33m::[39;49;00m$
  1247^I$
  1248^I[33m        [39;49;00m[33mcompose(f, g, unpack=True)(5, 6)[39;49;00m$
  1249^I[33m                    [39;49;00m$
  1250^Iis equivalent to[33m::[39;49;00m$
  1251^I$
  1252^I[33m        [39;49;00m[33mf(*g(5, 6))[39;49;00m$
  1253^I[33m[39;49;00m$
  1254^IEven though [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m only accepts two functions, it's trivial to$
  1255^Ibuild up a version that will compose any number of functions. We'll$
  1256^Iuse [33m``[39;49;00m[33mreduce()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m (the last of which$
  1257^Iis provided by both [33m``[39;49;00m[33mfunctional[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfunctools[39;49;00m[33m``[39;49;00m).$
  1258^I$
  1259^I[33m::[39;49;00m$
  1260^I$
  1261^I[33m        [39;49;00m[33mfrom functional import compose, partial[39;49;00m$
  1262^I[33m        [39;49;00m$
  1263^I[33m        multi_compose = partial(reduce, compose)[39;49;00m$
  1264^I[33m        [39;49;00m$
  1265^I    $
  1266^IWe can also use [33m``[39;49;00m[33mmap()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33mcompose()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m to craft a$
  1267^Iversion of [33m``[39;49;00m[33m"".join(...)[39;49;00m[33m``[39;49;00m that converts its arguments to string[33m::[39;49;00m$
  1268^I$
  1269^I[33m        [39;49;00m[33mfrom functional import compose, partial[39;49;00m$
  1270^I[33m        [39;49;00m$
  1271^I[33m        join = compose("".join, partial(map, str))[39;49;00m$
  1272^I[33m[39;49;00m$
  1273^I[33m[39;49;00m$
  1274^I[33m``[39;49;00m[33mflip(func)[39;49;00m[33m``[39;49;00m$
  1275^I                    $
  1276^I[33m``[39;49;00m[33mflip()[39;49;00m[33m``[39;49;00m wraps the callable in [33m``[39;49;00m[33mfunc[39;49;00m[33m``[39;49;00m and  $
  1277^Icauses it to receive its non-keyword arguments in reverse order.$
  1278^I$
  1279^I[33m::[39;49;00m$
  1280^I$
  1281^I[33m        [39;49;00m[33m>>> def triple(a, b, c):[39;49;00m$
  1282^I[33m        ...     return (a, b, c)[39;49;00m$
  1283^I[33m        ...[39;49;00m$
  1284^I[33m        >>> triple(5, 6, 7)[39;49;00m$
  1285^I[33m        (5, 6, 7)[39;49;00m$
  1286^I[33m        >>>[39;49;00m$
  1287^I[33m        >>> flipped_triple = flip(triple)[39;49;00m$
  1288^I[33m        >>> flipped_triple(5, 6, 7)[39;49;00m$
  1289^I[33m        (7, 6, 5)[39;49;00m$
  1290^I[33m[39;49;00m$
  1291^I[33m``[39;49;00m[33mfoldl(func, start, iterable)[39;49;00m[33m``[39;49;00m$
  1292^I                    $
  1293^I[33m``[39;49;00m[33mfoldl()[39;49;00m[33m``[39;49;00m takes a binary function, a starting value (usually some kind of 'zero'), and an iterable.$
  1294^IThe function is applied to the starting value and the first element of the list, then the result of$
  1295^Ithat and the second element of the list, then the result of that and the third element of the list,$
  1296^Iand so on.$
  1297^I$
  1298^IThis means that a call such as[33m::[39;49;00m$
  1299^I$
  1300^I[33m        [39;49;00m[33mfoldl(f, 0, [1, 2, 3])[39;49;00m$
  1301^I[33m[39;49;00m$
  1302^Iis equivalent to[33m::[39;49;00m$
  1303^I$
  1304^I[33m        [39;49;00m[33mf(f(f(0, 1), 2), 3)[39;49;00m$
  1305^I[33m[39;49;00m$
  1306^I    $
  1307^I[33m``[39;49;00m[33mfoldl()[39;49;00m[33m``[39;49;00m is roughly equivalent to the following recursive function[33m::[39;49;00m$
  1308^I$
  1309^I[33m        [39;49;00m[33mdef foldl(func, start, seq):[39;49;00m$
  1310^I[33m            if len(seq) == 0:[39;49;00m$
  1311^I[33m                return start[39;49;00m$
  1312^I[33m[39;49;00m$
  1313^I[33m            return foldl(func, func(start, seq[0]), seq[1:])[39;49;00m$
  1314^I[33m[39;49;00m$
  1315^ISpeaking of equivalence, the above [33m``[39;49;00m[33mfoldl[39;49;00m[33m``[39;49;00m call can be expressed in terms of the built-in [33m``[39;49;00m[33mreduce[39;49;00m[33m``[39;49;00m like$
  1316^Iso[33m::[39;49;00m$
  1317^I$
  1318^I[33m        [39;49;00m[33mreduce(f, [1, 2, 3], 0)[39;49;00m$
  1319^I[33m[39;49;00m$
  1320^I[33m[39;49;00m$
  1321^IWe can use [33m``[39;49;00m[33mfoldl()[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33moperator.concat()[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mpartial()[39;49;00m[33m``[39;49;00m to$
  1322^Iwrite a cleaner, more aesthetically-pleasing version of Python's$
  1323^I[33m``[39;49;00m[33m"".join(...)[39;49;00m[33m``[39;49;00m idiom[33m::[39;49;00m$
  1324^I$
  1325^I[33m        [39;49;00m[33mfrom functional import foldl, partial[39;49;00m$
  1326^I[33m        from operator import concat[39;49;00m$
  1327^I[33m        [39;49;00m$
  1328^I[33m        join = partial(foldl, concat, "")[39;49;00m$
  1329^I[33m[39;49;00m$
  1330^I[33m[39;49;00m$
  1331^I[01mRevision History and Acknowledgements[39;49;00m$
  1332^I[01m------------------------------------------------[39;49;00m$
  1333^I$
  1334^IThe author would like to thank the following people for offering$
  1335^Isuggestions, corrections and assistance with various drafts of this$
  1336^Iarticle: Ian Bicking, Nick Coghlan, Nick Efford, Raymond Hettinger,$
  1337^IJim Jewett, Mike Krell, Leandro Lameiro, Jussi Salmela, $
  1338^ICollin Winter, Blake Winton.$
  1339^I$
  1340^IVersion 0.1: posted June 30 2006.$
  1341^I$
  1342^IVersion 0.11: posted July 1 2006.  Typo fixes.$
  1343^I$
  1344^IVersion 0.2: posted July 10 2006.  Merged genexp and listcomp$
  1345^Isections into one.  Typo fixes.$
  1346^I$
  1347^IVersion 0.21: Added more references suggested on the tutor mailing list.$
  1348^I$
  1349^IVersion 0.30: Adds a section on the [33m``[39;49;00m[33mfunctional[39;49;00m[33m``[39;49;00m module written by$
  1350^ICollin Winter; adds short section on the operator module; a few other$
  1351^Iedits.$
  1352^I$
  1353^I$
  1354^I[01mReferences[39;49;00m$
  1355^I[01m--------------------[39;49;00m$
  1356^I$
  1357^I[01mGeneral[39;49;00m$
  1358^I[01m'''''''''''''''[39;49;00m$
  1359^I$
  1360^I**Structure and Interpretation of Computer Programs**, by $
  1361^IHarold Abelson and Gerald Jay Sussman with Julie Sussman.$
  1362^IFull text at http://mitpress.mit.edu/sicp/.$
  1363^IIn this classic textbook of computer science,  chapters 2 and 3 discuss the$
  1364^Iuse of sequences and streams to organize the data flow inside a$
  1365^Iprogram.  The book uses Scheme for its examples, but many of the$
  1366^Idesign approaches described in these chapters are applicable to$
  1367^Ifunctional-style Python code.$
  1368^I$
  1369^Ihttp://www.defmacro.org/ramblings/fp.html: A general $
  1370^Iintroduction to functional programming that uses Java examples$
  1371^Iand has a lengthy historical introduction.$
  1372^I$
  1373^Ihttp://en.wikipedia.org/wiki/Functional_programming:$
  1374^IGeneral Wikipedia entry describing functional programming.$
  1375^I$
  1376^Ihttp://en.wikipedia.org/wiki/Coroutine:$
  1377^IEntry for coroutines.$
  1378^I$
  1379^Ihttp://en.wikipedia.org/wiki/Currying:$
  1380^IEntry for the concept of currying.$
  1381^I$
  1382^I[01mPython-specific[39;49;00m$
  1383^I[01m'''''''''''''''''''''''''''[39;49;00m$
  1384^I$
  1385^Ihttp://gnosis.cx/TPiP/:$
  1386^IThe first chapter of David Mertz's book [36m:title-reference:[39;49;00m[31m`Text Processing in Python`[39;49;00m $
  1387^Idiscusses functional programming for text processing, in the section titled$
  1388^I"Utilizing Higher-Order Functions in Text Processing".$
  1389^I$
  1390^IMertz also wrote a 3-part series of articles on functional programming$
  1391^Ifor IBM's DeveloperWorks site; see $
  1392^I[33m`part 1 [39;49;00m[33m<http://www-128.ibm.com/developerworks/library/l-prog.html>[39;49;00m[33m`__[39;49;00m,$
  1393^I[33m`part 2 [39;49;00m[33m<http://www-128.ibm.com/developerworks/library/l-prog2.html>[39;49;00m[33m`__[39;49;00m, and$
  1394^I[33m`part 3 [39;49;00m[33m<http://www-128.ibm.com/developerworks/linux/library/l-prog3.html>[39;49;00m[33m`__[39;49;00m,$
  1395^I$
  1396^I$
  1397^I[01mPython documentation[39;49;00m$
  1398^I[01m'''''''''''''''''''''''''''[39;49;00m$
  1399^I$
  1400^Ihttp://docs.python.org/lib/module-itertools.html:$
  1401^IDocumentation for the [33m``[39;49;00m[33mitertools[39;49;00m[33m``[39;49;00m module.$
  1402^I$
  1403^Ihttp://docs.python.org/lib/module-operator.html:$
  1404^IDocumentation for the [33m``[39;49;00m[33moperator[39;49;00m[33m``[39;49;00m module.$
  1405^I$
  1406^Ihttp://www.python.org/dev/peps/pep-0289/:$
  1407^IPEP 289: "Generator Expressions"$
  1408^I$
  1409^Ihttp://www.python.org/dev/peps/pep-0342/$
  1410^IPEP 342: "Coroutines via Enhanced Generators" describes the new generator$
  1411^Ifeatures in Python 2.5.$
  1412^I$
  1413^I[36m.. comment[39;49;00m$
  1414^I[36m[39;49;00m$
  1415^I[36m    Topics to place[39;49;00m$
  1416^I[36m    -----------------------------[39;49;00m$
  1417^I[36m[39;49;00m$
  1418^I[36m    XXX os.walk()[39;49;00m$
  1419^I[36m[39;49;00m$
  1420^I[36m    XXX Need a large example.[39;49;00m$
  1421^I[36m[39;49;00m$
  1422^I[36m    But will an example add much?  I'll post a first draft and see[39;49;00m$
  1423^I[36m    what the comments say.[39;49;00m$
  1424^I[36m[39;49;00m$
  1425^I[36m.. comment[39;49;00m$
  1426^I[36m[39;49;00m$
  1427^I[36m    Original outline:[39;49;00m$
  1428^I[36m    Introduction[39;49;00m$
  1429^I[36m            Idea of FP[39;49;00m$
  1430^I[36m                    Programs built out of functions[39;49;00m$
  1431^I[36m                    Functions are strictly input-output, no internal state[39;49;00m$
  1432^I[36m            Opposed to OO programming, where objects have state[39;49;00m$
  1433^I[36m[39;49;00m$
  1434^I[36m            Why FP?[39;49;00m$
  1435^I[36m                    Formal provability[39;49;00m$
  1436^I[36m                            Assignment is difficult to reason about[39;49;00m$
  1437^I[36m                            Not very relevant to Python[39;49;00m$
  1438^I[36m                    Modularity[39;49;00m$
  1439^I[36m                            Small functions that do one thing[39;49;00m$
  1440^I[36m                    Debuggability:[39;49;00m$
  1441^I[36m                            Easy to test due to lack of state[39;49;00m$
  1442^I[36m                            Easy to verify output from intermediate steps[39;49;00m$
  1443^I[36m                    Composability[39;49;00m$
  1444^I[36m                            You assemble a toolbox of functions that can be mixed[39;49;00m$
  1445^I[36m[39;49;00m$
  1446^I[36m    Tackling a problem[39;49;00m$
  1447^I[36m            Need a significant example[39;49;00m$
  1448^I[36m[39;49;00m$
  1449^I[36m    Iterators[39;49;00m$
  1450^I[36m    Generators[39;49;00m$
  1451^I[36m    The itertools module[39;49;00m$
  1452^I[36m    List comprehensions[39;49;00m$
  1453^I[36m    Small functions and the lambda statement[39;49;00m$
  1454^I[36m    Built-in functions[39;49;00m$
  1455^I[36m            map[39;49;00m$
  1456^I[36m            filter[39;49;00m$
  1457^I[36m            reduce[39;49;00m$
  1458^I[36m[39;49;00m$
  1459^I[36m.. comment[39;49;00m$
  1460^I[36m[39;49;00m$
  1461^I[36m    Handy little function for printing part of an iterator -- used[39;49;00m$
  1462^I[36m    while writing this document.[39;49;00m$
  1463^I[36m[39;49;00m$
  1464^I[36m    import itertools[39;49;00m$
  1465^I[36m    def print_iter(it):[39;49;00m$
  1466^I[36m         slice = itertools.islice(it, 10)[39;49;00m$
  1467^I[36m         for elem in slice[:-1]:[39;49;00m$
  1468^I[36m             sys.stdout.write(str(elem))[39;49;00m$
  1469^I[36m             sys.stdout.write(', ')[39;49;00m$
  1470^I        print elem[-1]$
