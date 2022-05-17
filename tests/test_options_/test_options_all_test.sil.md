     1^I[34mdomain[39;49;00m Option__Node {$
     2^I    [34munique[39;49;00m [34mfunction[39;49;00m Option__Node__Some(): Option__Node$
     3^I    [34munique[39;49;00m [34mfunction[39;49;00m Option__Node__None(): Option__Node$
     4^I$
     5^I    [34mfunction[39;49;00m variantOfOptionNode(self: [36mRef[39;49;00m): Option__Node$
     6^I$
     7^I    [34mfunction[39;49;00m isOptionNode(self: [36mRef[39;49;00m): [36mBool[39;49;00m$
     8^I$
     9^I    [34maxiom[39;49;00m ax_variantOfOptionNodeChoices {$
    10^I        [34mforall[39;49;00m x: [36mRef[39;49;00m :: { variantOfOptionNode(x) }$
    11^I            (variantOfOptionNode(x) == Option__Node__Some() || variantOfOptionNode(x) == Option__Node__None())$
    12^I    }$
    13^I$
    14^I    [34maxiom[39;49;00m ax_isCounterState {$
    15^I        [34mforall[39;49;00m x: [36mRef[39;49;00m ::  { variantOfOptionNode(x) }$
    16^I            isOptionNode(x) == (variantOfOptionNode(x) == Option__Node__Some() ||$
    17^I                variantOfOptionNode(x) == Option__Node__None())$
    18^I    }$
    19^I}$
    20^I$
    21^I[34mpredicate[39;49;00m validOption(this: [36mRef[39;49;00m) {$
    22^I    isOptionNode(this) &&$
    23^I    variantOfOptionNode(this) == Option__Node__Some() ==> ($
    24^I        [34macc[39;49;00m(this.Option__Node__Some__1, [34mwrite[39;49;00m) &&$
    25^I        [34macc[39;49;00m(validNode(this.Option__Node__Some__1))$
    26^I    )$
    27^I}$
    28^I$
    29^I[34mfield[39;49;00m Option__Node__Some__1: [36mRef[39;49;00m$
    30^I$
    31^I[34mfield[39;49;00m Node__v: [36mInt[39;49;00m$
    32^I[34mfield[39;49;00m Node__next: [36mRef[39;49;00m$
    33^I$
    34^I[34mpredicate[39;49;00m validNode(this: [36mRef[39;49;00m) {$
    35^I    [34macc[39;49;00m(this.Node__v) &&$
    36^I    [34macc[39;49;00m(this.Node__next) &&$
    37^I    [34macc[39;49;00m(validOption(this.Node__next))$
    38^I}$
    39^I$
    40^I$
    41^I[34mfunction[39;49;00m length(this: [36mRef[39;49;00m): [36mInt[39;49;00m$
    42^I    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)$
    43^I    [90mensures[39;49;00m [34mresult[39;49;00m >= [34m1[39;49;00m$
    44^I{$
    45^I    ([34munfolding[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m) [34min[39;49;00m$
    46^I        [34munfolding[39;49;00m [34macc[39;49;00m(validOption(this.Node__next)) [34min[39;49;00m$
    47^I        (variantOfOptionNode(this.Node__next) == Option__Node__None()) ? $
    48^I            [34m1[39;49;00m : [34m1[39;49;00m + length(this.Node__next.Option__Node__Some__1)$
    49^I    )$
    50^I}$
    51^I$
    52^I[34mfunction[39;49;00m itemAt(this: [36mRef[39;49;00m, i: [36mInt[39;49;00m): [36mInt[39;49;00m$
    53^I    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)$
    54^I    [90mrequires[39;49;00m [34m0[39;49;00m <= i && i < length(this)$
    55^I{$
    56^I    [34munfolding[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m) [34min[39;49;00m [34munfolding[39;49;00m [34macc[39;49;00m(validOption(this.Node__next)) [34min[39;49;00m ($
    57^I        (i == [34m0[39;49;00m) ?$
    58^I            this.Node__v:$
    59^I            (variantOfOptionNode(this.Node__next) == Option__Node__Some()) ? $
    60^I                itemAt(this.Node__next.Option__Node__Some__1, i-[34m1[39;49;00m) : this.Node__v$
    61^I    )$
    62^I}$
    63^I$
    64^I[34mfunction[39;49;00m sum(this$1: [36mRef[39;49;00m): [36mInt[39;49;00m$
    65^I    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this$1), [34mwrite[39;49;00m)$
    66^I{$
    67^I    ([34munfolding[39;49;00m [34macc[39;49;00m(validNode(this$1), [34mwrite[39;49;00m) [34min[39;49;00m [34munfolding[39;49;00m [34macc[39;49;00m(validOption(this$1.Node__next)) [34min[39;49;00m $
    68^I        (variantOfOptionNode(this$1.Node__next) == Option__Node__None()) ? this$1.Node__v : this$1.Node__v + sum(this$1.Node__next.Option__Node__Some__1))$
    69^I}$
    70^I$
    71^I[34mmethod[39;49;00m append(this: [36mRef[39;49;00m, val: [36mInt[39;49;00m)$
    72^I    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)$
    73^I    [90mensures[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m) [37m/*[39;49;00m[37m POST1 [39;49;00m[37m*/[39;49;00m$
    74^I    [90mensures[39;49;00m length(this) == ([34mold[39;49;00m(length(this)) + [34m1[39;49;00m) [37m/*[39;49;00m[37m POST2 [39;49;00m[37m*/[39;49;00m$
    75^I    [90mensures[39;49;00m ([34mforall[39;49;00m i: [36mInt[39;49;00m :: ([34m0[39;49;00m <= i && i < [34mold[39;49;00m(length(this))) ==> (itemAt(this, i) == [34mold[39;49;00m(itemAt(this, i)))) [37m/*[39;49;00m[37m POST3 [39;49;00m[37m*/[39;49;00m$
    76^I    [90mensures[39;49;00m itemAt(this, length(this) - [34m1[39;49;00m) == val [37m/*[39;49;00m[37m POST4 [39;49;00m[37m*/[39;49;00m$
    77^I    [90mensures[39;49;00m [34mtrue[39;49;00m ==> [34mtrue[39;49;00m$
    78^I{$
    79^I    [34mvar[39;49;00m tmp_node: [36mRef[39;49;00m$
    80^I    [34mvar[39;49;00m tmp_option: [36mRef[39;49;00m$
    81^I$
    82^I    [34munfold[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)$
    83^I    [34munfold[39;49;00m [34macc[39;49;00m(validOption(this.Node__next), [34mwrite[39;49;00m)$
    84^I$
    85^I    [34mif[39;49;00m (variantOfOptionNode(this.Node__next) == Option__Node__None()) {$
    86^I        tmp_node := [34mnew[39;49;00m(Node__next, Node__v)$
    87^I        tmp_node.Node__next := [34mnull[39;49;00m$
    88^I        tmp_node.Node__v := val$
    89^I$
    90^I        [34massume[39;49;00m variantOfOptionNode(tmp_node.Node__next) == Option__Node__None()$
    91^I        [34mfold[39;49;00m [34macc[39;49;00m(validOption(tmp_node.Node__next))$
    92^I        [34mfold[39;49;00m [34macc[39;49;00m(validNode(tmp_node), [34mwrite[39;49;00m)$
    93^I$
    94^I        tmp_option := [34mnew[39;49;00m(Option__Node__Some__1)$
    95^I        tmp_option.Option__Node__Some__1 := tmp_node$
    96^I        [34massume[39;49;00m variantOfOptionNode(tmp_option) == Option__Node__Some()$
    97^I        [34mfold[39;49;00m [34macc[39;49;00m(validOption(tmp_option))$
    98^I$
    99^I        this.Node__next := tmp_option$
   100^I$
   101^I $
   102^I        [34munfold[39;49;00m validOption(tmp_option)$
   103^I        [34massert[39;49;00m length(tmp_node) == [34m1[39;49;00m [37m/*[39;49;00m[37m TODO: Required by Silicon, POST2 fails otherwise [39;49;00m[37m*/[39;49;00m$
   104^I        [34massert[39;49;00m itemAt(tmp_node, [34m0[39;49;00m) == val [37m/*[39;49;00m[37m TODO: Required by Silicon, POST4 fails otherwise [39;49;00m[37m*/[39;49;00m$
   105^I        [34mfold[39;49;00m validOption(tmp_option)$
   106^I    } [34melse[39;49;00m {$
   107^I        append(this.Node__next.Option__Node__Some__1, val)$
   108^I        [34mfold[39;49;00m [34macc[39;49;00m(validOption(this.Node__next), [34mwrite[39;49;00m)$
   109^I    }$
   110^I$
   111^I    [34mfold[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)$
   112^I}$
   113^I$
   114^I[34mmethod[39;49;00m prepend(tail: [36mRef[39;49;00m, val: [36mInt[39;49;00m) [34mreturns[39;49;00m (res: [36mRef[39;49;00m)$
   115^I    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(tail))$
   116^I    [90mensures[39;49;00m [34macc[39;49;00m(validNode(res))$
   117^I    [37m//ensures acc(validNode(tail))[39;49;00m$
   118^I    [90mensures[39;49;00m length(res) == [34mold[39;49;00m(length(tail)) + [34m1[39;49;00m$
   119^I$
   120^I    [90mensures[39;49;00m ([34mforall[39;49;00m i: [36mInt[39;49;00m :: ([34m1[39;49;00m <= i && i < length(res)) ==> (itemAt(res, i) == [34mold[39;49;00m(itemAt(tail, i-[34m1[39;49;00m)))) [37m/*[39;49;00m[37m POST3 [39;49;00m[37m*/[39;49;00m$
   121^I    [90mensures[39;49;00m itemAt(res, [34m0[39;49;00m) == val$
   122^I{$
   123^I    [34mvar[39;49;00m tmp_option: [36mRef[39;49;00m$
   124^I$
   125^I    res := [34mnew[39;49;00m(Node__v, Node__next)$
   126^I    res.Node__v := val$
   127^I$
   128^I    tmp_option := [34mnew[39;49;00m(Option__Node__Some__1)$
   129^I    tmp_option.Option__Node__Some__1 := tail$
   130^I    [34massume[39;49;00m variantOfOptionNode(tmp_option) == Option__Node__Some()$
   131^I$
   132^I    res.Node__next := tmp_option$
   133^I$
   134^I    [34massert[39;49;00m [34macc[39;49;00m(validNode(tail))$
   135^I    [34mfold[39;49;00m [34macc[39;49;00m(validOption(res.Node__next))$
   136^I    [34mfold[39;49;00m [34macc[39;49;00m(validNode(res))$
   137^I}$
   138^I$
   139^I[34mmethod[39;49;00m length_iter(list: [36mRef[39;49;00m) [34mreturns[39;49;00m (len: [36mInt[39;49;00m)$
   140^I    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(list), [34mwrite[39;49;00m)$
   141^I    [90mensures[39;49;00m [34mold[39;49;00m(length(list)) == len$
   142^I    [37m// TODO we have to preserve this property[39;49;00m$
   143^I    [37m// ensures acc(validNode(list))[39;49;00m$
   144^I{$
   145^I    [34mvar[39;49;00m curr: [36mRef[39;49;00m := list$
   146^I    [34mvar[39;49;00m tmp: [36mRef[39;49;00m := list$
   147^I$
   148^I    len := [34m1[39;49;00m$
   149^I$
   150^I    [34munfold[39;49;00m [34macc[39;49;00m(validNode(curr))$
   151^I    [34munfold[39;49;00m [34macc[39;49;00m(validOption(curr.Node__next))$
   152^I    [34mwhile[39;49;00m(variantOfOptionNode(curr.Node__next) == Option__Node__Some())$
   153^I        [90minvariant[39;49;00m [34macc[39;49;00m(curr.Node__v)$
   154^I        [90minvariant[39;49;00m [34macc[39;49;00m(curr.Node__next)$
   155^I        [90minvariant[39;49;00m (variantOfOptionNode(curr.Node__next) == Option__Node__Some() ==> ($
   156^I            [34macc[39;49;00m(curr.Node__next.Option__Node__Some__1, [34mwrite[39;49;00m) &&$
   157^I            [34macc[39;49;00m(validNode(curr.Node__next.Option__Node__Some__1))$
   158^I        ))$
   159^I        [90minvariant[39;49;00m (variantOfOptionNode(curr.Node__next) == Option__Node__Some() ==> len + length(curr.Node__next.Option__Node__Some__1) == [34mold[39;49;00m(length(list)))$
   160^I        [90minvariant[39;49;00m (variantOfOptionNode(curr.Node__next) == Option__Node__None() ==> len == [34mold[39;49;00m(length(list)))$
   161^I    {$
   162^I        [34massert[39;49;00m [34macc[39;49;00m(validNode(curr.Node__next.Option__Node__Some__1))$
   163^I        len := len + [34m1[39;49;00m$
   164^I        tmp := curr$
   165^I        curr := curr.Node__next.Option__Node__Some__1$
   166^I        [34munfold[39;49;00m [34macc[39;49;00m(validNode(curr))$
   167^I        [34munfold[39;49;00m [34macc[39;49;00m(validOption(curr.Node__next))$
   168^I    }$
   169^I}$
   170^I$
   171^I[34mmethod[39;49;00m t1()$
   172^I{$
   173^I    [34mvar[39;49;00m l: [36mRef[39;49;00m$
   174^I$
   175^I    l := [34mnew[39;49;00m(Node__v, Node__next)$
   176^I    l.Node__next := [34mnull[39;49;00m$
   177^I    l.Node__v := [34m1[39;49;00m$
   178^I    [34massume[39;49;00m variantOfOptionNode(l.Node__next) == Option__Node__None()$
   179^I$
   180^I    [34mfold[39;49;00m validOption(l.Node__next)$
   181^I    [34mfold[39;49;00m validNode(l)$
   182^I$
   183^I    [34massert[39;49;00m length(l) == [34m1[39;49;00m$
   184^I    [34massert[39;49;00m itemAt(l, [34m0[39;49;00m) == [34m1[39;49;00m$
   185^I$
   186^I    append(l, [34m7[39;49;00m)$
   187^I    [34massert[39;49;00m itemAt(l, [34m1[39;49;00m) == [34m7[39;49;00m$
   188^I    [34massert[39;49;00m itemAt(l, [34m0[39;49;00m) == [34m1[39;49;00m$
   189^I    [34massert[39;49;00m length(l) == [34m2[39;49;00m$
   190^I$
   191^I    l := prepend(l, [34m10[39;49;00m)$
   192^I    [34massert[39;49;00m itemAt(l, [34m2[39;49;00m) == [34m7[39;49;00m$
   193^I    [34massert[39;49;00m itemAt(l, [34m1[39;49;00m) == [34m1[39;49;00m$
   194^I    [34massert[39;49;00m itemAt(l, [34m0[39;49;00m) == [34m10[39;49;00m$
   195^I    [34massert[39;49;00m length(l) == [34m3[39;49;00m$
   196^I$
   197^I    [37m//assert sum(l) == 18[39;49;00m$
   198^I}$
   199^I$
   200^I[34mmethod[39;49;00m t2(l: [36mRef[39;49;00m) [34mreturns[39;49;00m (res: [36mRef[39;49;00m)$
   201^I    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(l), [34mwrite[39;49;00m)$
   202^I    [90mensures[39;49;00m [34macc[39;49;00m(validNode(res), [34mwrite[39;49;00m)$
   203^I    [90mensures[39;49;00m length(res) > [34mold[39;49;00m(length(l))$
   204^I{$
   205^I    res := prepend(l, [34m10[39;49;00m)$
   206^I}$
