     1	[37m-SOME RANDOM DIRECTIVE WOULD GO HERE[39;49;00m
     2	[37m*[39;49;00m
     3	[37m* SNOBOL4 example file for lexer[39;49;00m
     4	[37m*[39;49;00m
     5	 SOME.THING_OR_OTHER32 = [34m1[39;49;00m + [34m1.0[39;49;00m - [34m1E3[39;49;00m * [34m1E-3[39;49;00m ** [34m2.718284590E0[39;49;00m
     6	+ :[34mF[39;49;00m(END)[34mS[39;49;00m(IN_LOOP)
     7	 PATTERN = [36mLEN[39;49;00m([34m3[39;49;00m) ([33m"GAR"[39;49;00m | [33m"BAR"[39;49;00m)
     8	IN_LOOP THING = [36mINPUT[39;49;00m :[34mF[39;49;00m(END)
     9	 THING [36mLEN[39;49;00m([34m3[39;49;00m) ([33m"GAR"[39;49;00m | [33m"BAR"[39;49;00m) :[34mS[39;49;00m(OK)
    10	 [36mOUTPUT[39;49;00m = THING [33m" : Failure!"[39;49;00m :(IN_LOOP)
    11	OK [36mOUTPUT[39;49;00m = THING [33m' : "Success"!'[39;49;00m :(IN_LOOP)
    12	END
    13	[33mFOOBAR[39;49;00m
    14	[33mFOOGAR[39;49;00m
    15	[04m[91mT[39;49;00m[04m[91mH[39;49;00m[04m[91mi[39;49;00m[04m[91mN[39;49;00m[04m[91mI[39;49;00m[04m[91mg[39;49;00m
