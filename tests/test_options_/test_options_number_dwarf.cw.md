     1	[37m;redcode[39;49;00m[37m[39;49;00m
     2	[37m;name          Dwarf[39;49;00m[37m[39;49;00m
     3	[37m;author        A. K. Dewdney[39;49;00m[37m[39;49;00m
     4	[37m;version       94.1[39;49;00m[37m[39;49;00m
     5	[37m;date          April 29, 1993[39;49;00m[37m[39;49;00m
     6	[37m;strategy      Bombs every fourth instruction.[39;49;00m[37m[39;49;00m
     7	[37m        [39;49;00m[32mORG[39;49;00m[37m     [39;49;00mstart[37m              [39;49;00m[37m; Indicates the instruction with[39;49;00m[37m[39;49;00m
     8	[37m                                   [39;49;00m[37m; the label "start" should be the[39;49;00m[37m[39;49;00m
     9	[37m                                   [39;49;00m[37m; first to execute.[39;49;00m[37m[39;49;00m
    10	step[37m    [39;49;00m[32mEQU[39;49;00m[37m      [39;49;00m[34m4[39;49;00m[37m                 [39;49;00m[37m; Replaces all occurrences of "step"[39;49;00m[37m[39;49;00m
    11	[37m                                   [39;49;00m[37m; with the character "4".[39;49;00m[37m[39;49;00m
    12	target[37m  [39;49;00m[32mDAT[39;49;00m.[90mF[39;49;00m[37m   [39;49;00m#[34m0[39;49;00m,[37m     [39;49;00m#[34m0[39;49;00m[37m         [39;49;00m[37m; Pointer to target instruction.[39;49;00m[37m[39;49;00m
    13	start[37m   [39;49;00m[32mADD[39;49;00m.[90mAB[39;49;00m[37m  [39;49;00m#step,[37m   [39;49;00mtarget[37m    [39;49;00m[37m; Increments pointer by step.[39;49;00m[37m[39;49;00m
    14	[37m        [39;49;00m[32mMOV[39;49;00m.[90mAB[39;49;00m[37m  [39;49;00m#[34m0[39;49;00m,[37m     [39;49;00m@target[37m    [39;49;00m[37m; Bombs target instruction.[39;49;00m[37m[39;49;00m
    15	[37m        [39;49;00m[32mJMP[39;49;00m.[90mA[39;49;00m[37m    [39;49;00mstart[37m             [39;49;00m[37m; Same as JMP.A -2.  Loops back to[39;49;00m[37m[39;49;00m
    16	[37m                                   [39;49;00m[37m; the instruction labelled "start".[39;49;00m[37m[39;49;00m
    17	[37m        [39;49;00m[32mEND[39;49;00m
