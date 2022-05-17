     1	[34mif[39;49;00m ([31mthis[39;49;00m.running)
     2	  [31mplayer[39;49;00m:[32mtell[39;49;00m([33m"[Train] Error: already a jump in progress"[39;49;00m);
     3	  [34mreturn[39;49;00m;
     4	[34mendif[39;49;00m
     5	[31mthis[39;49;00m.running = [34m1[39;49;00m;
     6	[31mthis[39;49;00m.aborted = [34m0[39;49;00m;
     7	[31mthis[39;49;00m:[32mannounce_all[39;49;00m([33m"[Train] departure in 20 seconds"[39;49;00m);
     8	dest = [31mthis[39;49;00m.targets[[36mrandom[39;49;00m([36mlength[39;49;00m([31mthis[39;49;00m.targets))];
     9	[31mthis[39;49;00m:[32mannounce_all[39;49;00m([33m"[Train] Next stop is '"[39;49;00m, dest:[32mtitle[39;49;00m(), [33m"'"[39;49;00m);
    10	[31mthis[39;49;00m:[32mannounce_all[39;49;00m([33m"You hear the engines starting up"[39;49;00m);
    11	[31mthis[39;49;00m.location:[32mannounce[39;49;00m([33m"The MOOTrain starts up his engines"[39;49;00m);
    12	[32msuspend[39;49;00m([34m20[39;49;00m);
    13	[34mif[39;49;00m ([31mthis[39;49;00m.aborted)
    14	  [31mthis[39;49;00m.running = [34m0[39;49;00m;
    15	  [31mthis[39;49;00m.aborted = [34m0[39;49;00m;
    16	  [34mreturn[39;49;00m;
    17	[34mendif[39;49;00m
    18	[31mthis[39;49;00m:[32mannounce_all[39;49;00m([33m"[Train] Departure!"[39;49;00m);
    19	[31mthis[39;49;00m.location:[32mannounce_all[39;49;00m([33m"The MOOTrain leaves into the 42th dimension!"[39;49;00m);
    20	[31mthis[39;49;00m:[32mannounce_all[39;49;00m([33m"Outside you see the lights of the 42th dimension"[39;49;00m);
    21	[31mthis[39;49;00m:[32mmoveto[39;49;00m(dest);
    22	[32msuspend[39;49;00m([34m4[39;49;00m);
    23	[31mthis[39;49;00m:[32mannounce_all[39;49;00m([33m"The glowing gets less, until you can see the clear shape of the room, the MOOTrain has landed in"[39;49;00m);
    24	[31mthis[39;49;00m.location:[32mannounce_all[39;49;00m([33m"The MOOTrain arrives out of the 42th dimension!"[39;49;00m);
    25	[31mthis[39;49;00m:[32mannounce_all[39;49;00m([33m"[Train] arrived in '"[39;49;00m, dest:[32mtitle[39;49;00m(), [33m"'"[39;49;00m);
    26	[31mthis[39;49;00m.running = [34m0[39;49;00m;
