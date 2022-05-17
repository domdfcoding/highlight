[34mdomain[39;49;00m Option__Node {
    [34munique[39;49;00m [34mfunction[39;49;00m Option__Node__Some(): Option__Node
    [34munique[39;49;00m [34mfunction[39;49;00m Option__Node__None(): Option__Node

    [34mfunction[39;49;00m variantOfOptionNode(self: [36mRef[39;49;00m): Option__Node

    [34mfunction[39;49;00m isOptionNode(self: [36mRef[39;49;00m): [36mBool[39;49;00m

    [34maxiom[39;49;00m ax_variantOfOptionNodeChoices {
        [34mforall[39;49;00m x: [36mRef[39;49;00m :: { variantOfOptionNode(x) }
            (variantOfOptionNode(x) == Option__Node__Some() || variantOfOptionNode(x) == Option__Node__None())
    }

    [34maxiom[39;49;00m ax_isCounterState {
        [34mforall[39;49;00m x: [36mRef[39;49;00m ::  { variantOfOptionNode(x) }
            isOptionNode(x) == (variantOfOptionNode(x) == Option__Node__Some() ||
                variantOfOptionNode(x) == Option__Node__None())
    }
}

[34mpredicate[39;49;00m validOption(this: [36mRef[39;49;00m) {
    isOptionNode(this) &&
    variantOfOptionNode(this) == Option__Node__Some() ==> (
        [34macc[39;49;00m(this.Option__Node__Some__1, [34mwrite[39;49;00m) &&
        [34macc[39;49;00m(validNode(this.Option__Node__Some__1))
    )
}

[34mfield[39;49;00m Option__Node__Some__1: [36mRef[39;49;00m

[34mfield[39;49;00m Node__v: [36mInt[39;49;00m
[34mfield[39;49;00m Node__next: [36mRef[39;49;00m

[34mpredicate[39;49;00m validNode(this: [36mRef[39;49;00m) {
    [34macc[39;49;00m(this.Node__v) &&
    [34macc[39;49;00m(this.Node__next) &&
    [34macc[39;49;00m(validOption(this.Node__next))
}


[34mfunction[39;49;00m length(this: [36mRef[39;49;00m): [36mInt[39;49;00m
    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
    [90mensures[39;49;00m [34mresult[39;49;00m >= [34m1[39;49;00m
{
    ([34munfolding[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m) [34min[39;49;00m
        [34munfolding[39;49;00m [34macc[39;49;00m(validOption(this.Node__next)) [34min[39;49;00m
        (variantOfOptionNode(this.Node__next) == Option__Node__None()) ?
            [34m1[39;49;00m : [34m1[39;49;00m + length(this.Node__next.Option__Node__Some__1)
    )
}

[34mfunction[39;49;00m itemAt(this: [36mRef[39;49;00m, i: [36mInt[39;49;00m): [36mInt[39;49;00m
    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
    [90mrequires[39;49;00m [34m0[39;49;00m <= i && i < length(this)
{
    [34munfolding[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m) [34min[39;49;00m [34munfolding[39;49;00m [34macc[39;49;00m(validOption(this.Node__next)) [34min[39;49;00m (
        (i == [34m0[39;49;00m) ?
            this.Node__v:
            (variantOfOptionNode(this.Node__next) == Option__Node__Some()) ?
                itemAt(this.Node__next.Option__Node__Some__1, i-[34m1[39;49;00m) : this.Node__v
    )
}

[34mfunction[39;49;00m sum(this$1: [36mRef[39;49;00m): [36mInt[39;49;00m
    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this$1), [34mwrite[39;49;00m)
{
    ([34munfolding[39;49;00m [34macc[39;49;00m(validNode(this$1), [34mwrite[39;49;00m) [34min[39;49;00m [34munfolding[39;49;00m [34macc[39;49;00m(validOption(this$1.Node__next)) [34min[39;49;00m
        (variantOfOptionNode(this$1.Node__next) == Option__Node__None()) ? this$1.Node__v : this$1.Node__v + sum(this$1.Node__next.Option__Node__Some__1))
}

[34mmethod[39;49;00m append(this: [36mRef[39;49;00m, val: [36mInt[39;49;00m)
    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
    [90mensures[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m) [37m/*[39;49;00m[37m POST1 [39;49;00m[37m*/[39;49;00m
    [90mensures[39;49;00m length(this) == ([34mold[39;49;00m(length(this)) + [34m1[39;49;00m) [37m/*[39;49;00m[37m POST2 [39;49;00m[37m*/[39;49;00m
    [90mensures[39;49;00m ([34mforall[39;49;00m i: [36mInt[39;49;00m :: ([34m0[39;49;00m <= i && i < [34mold[39;49;00m(length(this))) ==> (itemAt(this, i) == [34mold[39;49;00m(itemAt(this, i)))) [37m/*[39;49;00m[37m POST3 [39;49;00m[37m*/[39;49;00m
    [90mensures[39;49;00m itemAt(this, length(this) - [34m1[39;49;00m) == val [37m/*[39;49;00m[37m POST4 [39;49;00m[37m*/[39;49;00m
    [90mensures[39;49;00m [34mtrue[39;49;00m ==> [34mtrue[39;49;00m
{
    [34mvar[39;49;00m tmp_node: [36mRef[39;49;00m
    [34mvar[39;49;00m tmp_option: [36mRef[39;49;00m

    [34munfold[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
    [34munfold[39;49;00m [34macc[39;49;00m(validOption(this.Node__next), [34mwrite[39;49;00m)

    [34mif[39;49;00m (variantOfOptionNode(this.Node__next) == Option__Node__None()) {
        tmp_node := [34mnew[39;49;00m(Node__next, Node__v)
        tmp_node.Node__next := [34mnull[39;49;00m
        tmp_node.Node__v := val

        [34massume[39;49;00m variantOfOptionNode(tmp_node.Node__next) == Option__Node__None()
        [34mfold[39;49;00m [34macc[39;49;00m(validOption(tmp_node.Node__next))
        [34mfold[39;49;00m [34macc[39;49;00m(validNode(tmp_node), [34mwrite[39;49;00m)

        tmp_option := [34mnew[39;49;00m(Option__Node__Some__1)
        tmp_option.Option__Node__Some__1 := tmp_node
        [34massume[39;49;00m variantOfOptionNode(tmp_option) == Option__Node__Some()
        [34mfold[39;49;00m [34macc[39;49;00m(validOption(tmp_option))

        this.Node__next := tmp_option


        [34munfold[39;49;00m validOption(tmp_option)
        [34massert[39;49;00m length(tmp_node) == [34m1[39;49;00m [37m/*[39;49;00m[37m TODO: Required by Silicon, POST2 fails otherwise [39;49;00m[37m*/[39;49;00m
        [34massert[39;49;00m itemAt(tmp_node, [34m0[39;49;00m) == val [37m/*[39;49;00m[37m TODO: Required by Silicon, POST4 fails otherwise [39;49;00m[37m*/[39;49;00m
        [34mfold[39;49;00m validOption(tmp_option)
    } [34melse[39;49;00m {
        append(this.Node__next.Option__Node__Some__1, val)
        [34mfold[39;49;00m [34macc[39;49;00m(validOption(this.Node__next), [34mwrite[39;49;00m)
    }

    [34mfold[39;49;00m [34macc[39;49;00m(validNode(this), [34mwrite[39;49;00m)
}

[34mmethod[39;49;00m prepend(tail: [36mRef[39;49;00m, val: [36mInt[39;49;00m) [34mreturns[39;49;00m (res: [36mRef[39;49;00m)
    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(tail))
    [90mensures[39;49;00m [34macc[39;49;00m(validNode(res))
    [37m//ensures acc(validNode(tail))[39;49;00m
    [90mensures[39;49;00m length(res) == [34mold[39;49;00m(length(tail)) + [34m1[39;49;00m

    [90mensures[39;49;00m ([34mforall[39;49;00m i: [36mInt[39;49;00m :: ([34m1[39;49;00m <= i && i < length(res)) ==> (itemAt(res, i) == [34mold[39;49;00m(itemAt(tail, i-[34m1[39;49;00m)))) [37m/*[39;49;00m[37m POST3 [39;49;00m[37m*/[39;49;00m
    [90mensures[39;49;00m itemAt(res, [34m0[39;49;00m) == val
{
    [34mvar[39;49;00m tmp_option: [36mRef[39;49;00m

    res := [34mnew[39;49;00m(Node__v, Node__next)
    res.Node__v := val

    tmp_option := [34mnew[39;49;00m(Option__Node__Some__1)
    tmp_option.Option__Node__Some__1 := tail
    [34massume[39;49;00m variantOfOptionNode(tmp_option) == Option__Node__Some()

    res.Node__next := tmp_option

    [34massert[39;49;00m [34macc[39;49;00m(validNode(tail))
    [34mfold[39;49;00m [34macc[39;49;00m(validOption(res.Node__next))
    [34mfold[39;49;00m [34macc[39;49;00m(validNode(res))
}

[34mmethod[39;49;00m length_iter(list: [36mRef[39;49;00m) [34mreturns[39;49;00m (len: [36mInt[39;49;00m)
    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(list), [34mwrite[39;49;00m)
    [90mensures[39;49;00m [34mold[39;49;00m(length(list)) == len
    [37m// TODO we have to preserve this property[39;49;00m
    [37m// ensures acc(validNode(list))[39;49;00m
{
    [34mvar[39;49;00m curr: [36mRef[39;49;00m := list
    [34mvar[39;49;00m tmp: [36mRef[39;49;00m := list

    len := [34m1[39;49;00m

    [34munfold[39;49;00m [34macc[39;49;00m(validNode(curr))
    [34munfold[39;49;00m [34macc[39;49;00m(validOption(curr.Node__next))
    [34mwhile[39;49;00m(variantOfOptionNode(curr.Node__next) == Option__Node__Some())
        [90minvariant[39;49;00m [34macc[39;49;00m(curr.Node__v)
        [90minvariant[39;49;00m [34macc[39;49;00m(curr.Node__next)
        [90minvariant[39;49;00m (variantOfOptionNode(curr.Node__next) == Option__Node__Some() ==> (
            [34macc[39;49;00m(curr.Node__next.Option__Node__Some__1, [34mwrite[39;49;00m) &&
            [34macc[39;49;00m(validNode(curr.Node__next.Option__Node__Some__1))
        ))
        [90minvariant[39;49;00m (variantOfOptionNode(curr.Node__next) == Option__Node__Some() ==> len + length(curr.Node__next.Option__Node__Some__1) == [34mold[39;49;00m(length(list)))
        [90minvariant[39;49;00m (variantOfOptionNode(curr.Node__next) == Option__Node__None() ==> len == [34mold[39;49;00m(length(list)))
    {
        [34massert[39;49;00m [34macc[39;49;00m(validNode(curr.Node__next.Option__Node__Some__1))
        len := len + [34m1[39;49;00m
        tmp := curr
        curr := curr.Node__next.Option__Node__Some__1
        [34munfold[39;49;00m [34macc[39;49;00m(validNode(curr))
        [34munfold[39;49;00m [34macc[39;49;00m(validOption(curr.Node__next))
    }
}

[34mmethod[39;49;00m t1()
{
    [34mvar[39;49;00m l: [36mRef[39;49;00m

    l := [34mnew[39;49;00m(Node__v, Node__next)
    l.Node__next := [34mnull[39;49;00m
    l.Node__v := [34m1[39;49;00m
    [34massume[39;49;00m variantOfOptionNode(l.Node__next) == Option__Node__None()

    [34mfold[39;49;00m validOption(l.Node__next)
    [34mfold[39;49;00m validNode(l)

    [34massert[39;49;00m length(l) == [34m1[39;49;00m
    [34massert[39;49;00m itemAt(l, [34m0[39;49;00m) == [34m1[39;49;00m

    append(l, [34m7[39;49;00m)
    [34massert[39;49;00m itemAt(l, [34m1[39;49;00m) == [34m7[39;49;00m
    [34massert[39;49;00m itemAt(l, [34m0[39;49;00m) == [34m1[39;49;00m
    [34massert[39;49;00m length(l) == [34m2[39;49;00m

    l := prepend(l, [34m10[39;49;00m)
    [34massert[39;49;00m itemAt(l, [34m2[39;49;00m) == [34m7[39;49;00m
    [34massert[39;49;00m itemAt(l, [34m1[39;49;00m) == [34m1[39;49;00m
    [34massert[39;49;00m itemAt(l, [34m0[39;49;00m) == [34m10[39;49;00m
    [34massert[39;49;00m length(l) == [34m3[39;49;00m

    [37m//assert sum(l) == 18[39;49;00m
}

[34mmethod[39;49;00m t2(l: [36mRef[39;49;00m) [34mreturns[39;49;00m (res: [36mRef[39;49;00m)
    [90mrequires[39;49;00m [34macc[39;49;00m(validNode(l), [34mwrite[39;49;00m)
    [90mensures[39;49;00m [34macc[39;49;00m(validNode(res), [34mwrite[39;49;00m)
    [90mensures[39;49;00m length(res) > [34mold[39;49;00m(length(l))
{
    res := prepend(l, [34m10[39;49;00m)
}
