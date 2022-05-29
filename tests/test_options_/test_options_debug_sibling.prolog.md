Using lexer <pygments.lexers.PrologLexer with {'ensurenl': False, 'tabsize': 0}>
[37m/*[39;49;00m[37m Comments [39;49;00m[37m/*[39;49;00m[37m can nest [39;49;00m[37m*/[39;49;00m[37m[39;49;00m
[37mstill a comment[39;49;00m
[37m*/[39;49;00m

:- [32mmodule[39;49;00m([33mmaplist[39;49;00m, [33mmaplist[39;49;00m/[34m3[39;49;00m)

[32massert[39;49;00m([04m[36mworld[39;49;00m:[33mdone[39;49;00m). [37m% asserts[39;49;00m

[32msibling[39;49;00m([31mX[39;49;00m, [31mY[39;49;00m)      :- [32mparent_child[39;49;00m([31mZ[39;49;00m, [31mX[39;49;00m), [32mparent_child[39;49;00m([31mZ[39;49;00m, [31mY[39;49;00m).

[32mparent_child[39;49;00m([31mX[39;49;00m, [31mY[39;49;00m) :- [32mfather_child[39;49;00m([31mX[39;49;00m, [31mY[39;49;00m).
[32mparent_child[39;49;00m([31mX[39;49;00m, [31mY[39;49;00m) :- [32mmother_child[39;49;00m([31mX[39;49;00m, [31mY[39;49;00m).

[32mmother_child[39;49;00m([33mtrude[39;49;00m, [33msally[39;49;00m).

[32mfather_child[39;49;00m([33mtom[39;49;00m, [33msally[39;49;00m).
[32mfather_child[39;49;00m([33mtom[39;49;00m, [33merica[39;49;00m).
[32mfather_child[39;49;00m([33mmike[39;49;00m, [33mtom[39;49;00m).
