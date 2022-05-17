     1	   ## a comment
     2
     3	\## not a comment
     4
     5	#if foo
     6	  [36m${[39;49;00mbar[36m}[39;49;00m
     7	#endif
     8
     9	The answer is:
    10	#choose
    11	  #when 0 == 1
    12	    0
    13	  #end
    14	  #when 1 == 1
    15	    1
    16	  #end
    17	  #otherwise
    18	    2
    19	  #end
    20	#end -- comment about choose
    21
    22	#for item in items
    23	  * [36m${[39;49;00mitem[36m}[39;49;00m
    24	#end
    25
    26	#def greeting(name)
    27	  Hello, [36m${[39;49;00mname[36m}[39;49;00m!
    28	#end
    29	[36m${[39;49;00mgreeting([33m'[39;49;00m[33mworld[39;49;00m[33m'[39;49;00m)[36m}[39;49;00m
    30
    31	#with y=7; z=x+10
    32	  [31m$x[39;49;00m [31m$y[39;49;00m [31m$z[39;49;00m
    33	#end
