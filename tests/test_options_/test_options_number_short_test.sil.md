     1	[34mdomain[39;49;00m Option__Node {
     2	    [34munique[39;49;00m [34mfunction[39;49;00m Option__Node__Some(): Option__Node
     3	    [34munique[39;49;00m [34mfunction[39;49;00m Option__Node__None(): Option__Node
     4
     5	    [34mfunction[39;49;00m variantOfOptionNode(self: [36mRef[39;49;00m): Option__Node
     6
     7	    [34mfunction[39;49;00m isOptionNode(self: [36mRef[39;49;00m): [36mBool[39;49;00m
     8
     9	    [34maxiom[39;49;00m ax_variantOfOptionNodeChoices {
    10	        [34mforall[39;49;00m x: [36mRef[39;49;00m :: { variantOfOptionNode(x) }
    11	            (variantOfOptionNode(x) == Option__Node__Some() || variantOfOptionNode(x) == Option__Node__None())
    12	    }
    13
    14	    [34maxiom[39;49;00m ax_isCounterState {
    15	        [34mforall[39;49;00m x: [36mRef[39;49;00m ::  { variantOfOptionNode(x) }
    16	            isOptionNode(x) == (variantOfOptionNode(x) == Option__Node__Some() ||
    17	                variantOfOptionNode(x) == Option__Node__None())
    18	    }
    19	}
    20
    21	[34mpredicate[39;49;00m validOption(this: [36mRef[39;49;00m) {
    22	    isOptionNode(this) &&
    23	    variantOfOptionNode(this) == Option__Node__Some() ==> (
    24	        [34macc[39;49;00m(this.Option__Node__Some__1, [34mwrite[39;49;00m) &&
    25	        [34macc[39;49;00m(validNode(this.Option__Node__Some__1))
    26	    )
    27	}
    28
    29	[34mfield[39;49;00m Option__Node__Some__1: [36mRef[39;49;00m
    30
    31	[34mfield[39;49;00m Node__v: [36mInt[39;49;00m
    32	[34mfield[39;49;00m Node__next: [36mRef[39;49;00m
    33
    34	[34mpredicate[39;49;00m validNode(this: [36mRef[39;49;00m) {
    35	    [34macc[39;49;00m(this.Node__v) &&
    36	    [34macc[39;49;00m(this.Node__next) &&
    37	    [34macc[39;49;00m(validOption(this.Node__next))
    38	}
    39
    40
    41	[34mfunction[39;49;00m length(this: [36mRef[39;49;00m): [36mInt[39;49;00m
    42	    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
    43	    [90mensures[39;49;00m [34mresult[39;49;00m >= [34m1[39;49;00m
    44	{
    45	    ([34munfolding[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m) [34min[39;49;00m
    46	        [34munfolding[39;49;00m [34macc[39;49;00m(validOption(this.Node__next)) [34min[39;49;00m
    47	        (variantOfOptionNode(this.Node__next) == Option__Node__None()) ?
    48	            [34m1[39;49;00m : [34m1[39;49;00m + length(this.Node__next.Option__Node__Some__1)
    49	    )
    50	}
    51
    52	[34mfunction[39;49;00m itemAt(this: [36mRef[39;49;00m, i: [36mInt[39;49;00m): [36mInt[39;49;00m
    53	    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
    54	    [90mrequires[39;49;00m [34m0[39;49;00m <= i && i < length(this)
    55	{
    56	    [34munfolding[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m) [34min[39;49;00m [34munfolding[39;49;00m [34macc[39;49;00m(validOption(this.Node__next)) [34min[39;49;00m (
    57	        (i == [34m0[39;49;00m) ?
    58	            this.Node__v:
    59	            (variantOfOptionNode(this.Node__next) == Option__Node__Some()) ?
    60	                itemAt(this.Node__next.Option__Node__Some__1, i-[34m1[39;49;00m) : this.Node__v
    61	    )
    62	}
    63
    64	[34mfunction[39;49;00m sum(this$1: [36mRef[39;49;00m): [36mInt[39;49;00m
    65	    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this$1), [34mwrite[39;49;00m)
    66	{
    67	    ([34munfolding[39;49;00m [34macc[39;49;00m(validNode(this$1), [34mwrite[39;49;00m) [34min[39;49;00m [34munfolding[39;49;00m [34macc[39;49;00m(validOption(this$1.Node__next)) [34min[39;49;00m
    68	        (variantOfOptionNode(this$1.Node__next) == Option__Node__None()) ? this$1.Node__v : this$1.Node__v + sum(this$1.Node__next.Option__Node__Some__1))
    69	}
    70
    71	[34mmethod[39;49;00m append(this: [36mRef[39;49;00m, val: [36mInt[39;49;00m)
    72	    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
    73	    [90mensures[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m) [37m/*[39;49;00m[37m POST1 [39;49;00m[37m*/[39;49;00m
    74	    [90mensures[39;49;00m length(this) == ([34mold[39;49;00m(length(this)) + [34m1[39;49;00m) [37m/*[39;49;00m[37m POST2 [39;49;00m[37m*/[39;49;00m
    75	    [90mensures[39;49;00m ([34mforall[39;49;00m i: [36mInt[39;49;00m :: ([34m0[39;49;00m <= i && i < [34mold[39;49;00m(length(this))) ==> (itemAt(this, i) == [34mold[39;49;00m(itemAt(this, i)))) [37m/*[39;49;00m[37m POST3 [39;49;00m[37m*/[39;49;00m
    76	    [90mensures[39;49;00m itemAt(this, length(this) - [34m1[39;49;00m) == val [37m/*[39;49;00m[37m POST4 [39;49;00m[37m*/[39;49;00m
    77	    [90mensures[39;49;00m [34mtrue[39;49;00m ==> [34mtrue[39;49;00m
    78	{
    79	    [34mvar[39;49;00m tmp_node: [36mRef[39;49;00m
    80	    [34mvar[39;49;00m tmp_option: [36mRef[39;49;00m
    81
    82	    [34munfold[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
    83	    [34munfold[39;49;00m [34macc[39;49;00m(validOption(this.Node__next), [34mwrite[39;49;00m)
    84
    85	    [34mif[39;49;00m (variantOfOptionNode(this.Node__next) == Option__Node__None()) {
    86	        tmp_node := [34mnew[39;49;00m(Node__next, Node__v)
    87	        tmp_node.Node__next := [34mnull[39;49;00m
    88	        tmp_node.Node__v := val
    89
    90	        [34massume[39;49;00m variantOfOptionNode(tmp_node.Node__next) == Option__Node__None()
    91	        [34mfold[39;49;00m [34macc[39;49;00m(validOption(tmp_node.Node__next))
    92	        [34mfold[39;49;00m [34macc[39;49;00m(validNode(tmp_node), [34mwrite[39;49;00m)
    93
    94	        tmp_option := [34mnew[39;49;00m(Option__Node__Some__1)
    95	        tmp_option.Option__Node__Some__1 := tmp_node
    96	        [34massume[39;49;00m variantOfOptionNode(tmp_option) == Option__Node__Some()
    97	        [34mfold[39;49;00m [34macc[39;49;00m(validOption(tmp_option))
    98
    99	        this.Node__next := tmp_option
   100
   101
   102	        [34munfold[39;49;00m validOption(tmp_option)
   103	        [34massert[39;49;00m length(tmp_node) == [34m1[39;49;00m [37m/*[39;49;00m[37m TODO: Required by Silicon, POST2 fails otherwise [39;49;00m[37m*/[39;49;00m
   104	        [34massert[39;49;00m itemAt(tmp_node, [34m0[39;49;00m) == val [37m/*[39;49;00m[37m TODO: Required by Silicon, POST4 fails otherwise [39;49;00m[37m*/[39;49;00m
   105	        [34mfold[39;49;00m validOption(tmp_option)
   106	    } [34melse[39;49;00m {
   107	        append(this.Node__next.Option__Node__Some__1, val)
   108	        [34mfold[39;49;00m [34macc[39;49;00m(validOption(this.Node__next), [34mwrite[39;49;00m)
   109	    }
   110
   111	    [34mfold[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
   112	}
   113
   114	[34mmethod[39;49;00m prepend(tail: [36mRef[39;49;00m, val: [36mInt[39;49;00m) [34mreturns[39;49;00m (res: [36mRef[39;49;00m)
   115	    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(tail))
   116	    [90mensures[39;49;00m [34macc[39;49;00m(validNode(res))
   117	    [37m//ensures acc(validNode(tail))[39;49;00m
   118	    [90mensures[39;49;00m length(res) == [34mold[39;49;00m(length(tail)) + [34m1[39;49;00m
   119
   120	    [90mensures[39;49;00m ([34mforall[39;49;00m i: [36mInt[39;49;00m :: ([34m1[39;49;00m <= i && i < length(res)) ==> (itemAt(res, i) == [34mold[39;49;00m(itemAt(tail, i-[34m1[39;49;00m)))) [37m/*[39;49;00m[37m POST3 [39;49;00m[37m*/[39;49;00m
   121	    [90mensures[39;49;00m itemAt(res, [34m0[39;49;00m) == val
   122	{
   123	    [34mvar[39;49;00m tmp_option: [36mRef[39;49;00m
   124
   125	    res := [34mnew[39;49;00m(Node__v, Node__next)
   126	    res.Node__v := val
   127
   128	    tmp_option := [34mnew[39;49;00m(Option__Node__Some__1)
   129	    tmp_option.Option__Node__Some__1 := tail
   130	    [34massume[39;49;00m variantOfOptionNode(tmp_option) == Option__Node__Some()
   131
   132	    res.Node__next := tmp_option
   133
   134	    [34massert[39;49;00m [34macc[39;49;00m(validNode(tail))
   135	    [34mfold[39;49;00m [34macc[39;49;00m(validOption(res.Node__next))
   136	    [34mfold[39;49;00m [34macc[39;49;00m(validNode(res))
   137	}
   138
   139	[34mmethod[39;49;00m length_iter(list: [36mRef[39;49;00m) [34mreturns[39;49;00m (len: [36mInt[39;49;00m)
   140	    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(list), [34mwrite[39;49;00m)
   141	    [90mensures[39;49;00m [34mold[39;49;00m(length(list)) == len
   142	    [37m// TODO we have to preserve this property[39;49;00m
   143	    [37m// ensures acc(validNode(list))[39;49;00m
   144	{
   145	    [34mvar[39;49;00m curr: [36mRef[39;49;00m := list
   146	    [34mvar[39;49;00m tmp: [36mRef[39;49;00m := list
   147
   148	    len := [34m1[39;49;00m
   149
   150	    [34munfold[39;49;00m [34macc[39;49;00m(validNode(curr))
   151	    [34munfold[39;49;00m [34macc[39;49;00m(validOption(curr.Node__next))
   152	    [34mwhile[39;49;00m(variantOfOptionNode(curr.Node__next) == Option__Node__Some())
   153	        [90minvariant[39;49;00m [34macc[39;49;00m(curr.Node__v)
   154	        [90minvariant[39;49;00m [34macc[39;49;00m(curr.Node__next)
   155	        [90minvariant[39;49;00m (variantOfOptionNode(curr.Node__next) == Option__Node__Some() ==> (
   156	            [34macc[39;49;00m(curr.Node__next.Option__Node__Some__1, [34mwrite[39;49;00m) &&
   157	            [34macc[39;49;00m(validNode(curr.Node__next.Option__Node__Some__1))
   158	        ))
   159	        [90minvariant[39;49;00m (variantOfOptionNode(curr.Node__next) == Option__Node__Some() ==> len + length(curr.Node__next.Option__Node__Some__1) == [34mold[39;49;00m(length(list)))
   160	        [90minvariant[39;49;00m (variantOfOptionNode(curr.Node__next) == Option__Node__None() ==> len == [34mold[39;49;00m(length(list)))
   161	    {
   162	        [34massert[39;49;00m [34macc[39;49;00m(validNode(curr.Node__next.Option__Node__Some__1))
   163	        len := len + [34m1[39;49;00m
   164	        tmp := curr
   165	        curr := curr.Node__next.Option__Node__Some__1
   166	        [34munfold[39;49;00m [34macc[39;49;00m(validNode(curr))
   167	        [34munfold[39;49;00m [34macc[39;49;00m(validOption(curr.Node__next))
   168	    }
   169	}
   170
   171	[34mmethod[39;49;00m t1()
   172	{
   173	    [34mvar[39;49;00m l: [36mRef[39;49;00m
   174
   175	    l := [34mnew[39;49;00m(Node__v, Node__next)
   176	    l.Node__next := [34mnull[39;49;00m
   177	    l.Node__v := [34m1[39;49;00m
   178	    [34massume[39;49;00m variantOfOptionNode(l.Node__next) == Option__Node__None()
   179
   180	    [34mfold[39;49;00m validOption(l.Node__next)
   181	    [34mfold[39;49;00m validNode(l)
   182
   183	    [34massert[39;49;00m length(l) == [34m1[39;49;00m
   184	    [34massert[39;49;00m itemAt(l, [34m0[39;49;00m) == [34m1[39;49;00m
   185
   186	    append(l, [34m7[39;49;00m)
   187	    [34massert[39;49;00m itemAt(l, [34m1[39;49;00m) == [34m7[39;49;00m
   188	    [34massert[39;49;00m itemAt(l, [34m0[39;49;00m) == [34m1[39;49;00m
   189	    [34massert[39;49;00m length(l) == [34m2[39;49;00m
   190
   191	    l := prepend(l, [34m10[39;49;00m)
   192	    [34massert[39;49;00m itemAt(l, [34m2[39;49;00m) == [34m7[39;49;00m
   193	    [34massert[39;49;00m itemAt(l, [34m1[39;49;00m) == [34m1[39;49;00m
   194	    [34massert[39;49;00m itemAt(l, [34m0[39;49;00m) == [34m10[39;49;00m
   195	    [34massert[39;49;00m length(l) == [34m3[39;49;00m
   196
   197	    [37m//assert sum(l) == 18[39;49;00m
   198	}
   199
   200	[34mmethod[39;49;00m t2(l: [36mRef[39;49;00m) [34mreturns[39;49;00m (res: [36mRef[39;49;00m)
   201	    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(l), [34mwrite[39;49;00m)
   202	    [90mensures[39;49;00m [34macc[39;49;00m(validNode(res), [34mwrite[39;49;00m)
   203	    [90mensures[39;49;00m length(res) > [34mold[39;49;00m(length(l))
   204	{
   205	    res := prepend(l, [34m10[39;49;00m)
   206	}
