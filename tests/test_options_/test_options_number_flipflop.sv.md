     1	[34mmodule[39;49;00m[37m [39;49;00mtoplevel(clock,reset);[37m[39;49;00m
     2	[37m [39;49;00m[34minput[39;49;00m[37m [39;49;00mclock;[37m[39;49;00m
     3	[37m [39;49;00m[34minput[39;49;00m[37m [39;49;00mreset;[37m[39;49;00m
     4	[37m [39;49;00m
     5	[37m [39;49;00m[36mreg[39;49;00m[37m [39;49;00mflop1;[37m[39;49;00m
     6	[37m [39;49;00m[36mreg[39;49;00m[37m [39;49;00mflop2;[37m[39;49;00m
     7	[37m [39;49;00m
     8	[37m [39;49;00m[34malways[39;49;00m[37m [39;49;00m@[37m [39;49;00m([34mposedge[39;49;00m[37m [39;49;00mreset[37m [39;49;00m[34mor[39;49;00m[37m [39;49;00m[34mposedge[39;49;00m[37m [39;49;00mclock)[37m[39;49;00m
     9	[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(reset)[37m[39;49;00m
    10	[37m   [39;49;00m[34mbegin[39;49;00m[37m[39;49;00m
    11	[37m     [39;49;00mflop1[37m [39;49;00m<=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m
    12	[37m     [39;49;00mflop2[37m [39;49;00m<=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m
    13	[37m   [39;49;00m[34mend[39;49;00m[37m[39;49;00m
    14	[37m [39;49;00m[34melse[39;49;00m[37m[39;49;00m
    15	[37m   [39;49;00m[34mbegin[39;49;00m[37m[39;49;00m
    16	[37m     [39;49;00mflop1[37m [39;49;00m<=[37m [39;49;00mflop2;[37m[39;49;00m
    17	[37m     [39;49;00mflop2[37m [39;49;00m<=[37m [39;49;00mflop1;[37m[39;49;00m
    18	[37m   [39;49;00m[34mend[39;49;00m[37m[39;49;00m
    19	[34mendmodule[39;49;00m
