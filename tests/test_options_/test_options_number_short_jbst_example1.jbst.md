     1	[94m<%@[39;49;00m[37m [39;49;00mControl[37m [39;49;00mName=[33m"MyApp.MyJbstControl"[39;49;00m[37m [39;49;00mLanguage=[33m"JavaScript"[39;49;00m[37m [39;49;00m[94m%>[39;49;00m
     2
     3	<[94mscript[39;49;00m [36mtype[39;49;00m=[33m"text/javascript"[39;49;00m>[37m[39;49;00m
     4	[37m[39;49;00m
     5	[37m	[39;49;00m[37m/* initialization code block, executed only once as control is loaded */[39;49;00m[37m[39;49;00m
     6	[37m	[39;49;00m[34mthis[39;49;00m.generateValue[37m [39;49;00m=[37m [39;49;00m[34mfunction[39;49;00m()[37m [39;49;00m{[37m[39;49;00m
     7	[37m		[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[35mnew[39;49;00m[37m [39;49;00m[36mDate[39;49;00m().toString();[37m[39;49;00m
     8	[37m	[39;49;00m};[37m[39;49;00m
     9	[37m[39;49;00m
    10	</[94mscript[39;49;00m>
    11
    12	[94m<%![39;49;00m[37m[39;49;00m
    13	[37m	[39;49;00m[37m/* initialization code block, executed only once as control is loaded */[39;49;00m[37m[39;49;00m
    14	[37m	[39;49;00m[37m/* alternate syntax to script block above */[39;49;00m[37m[39;49;00m
    15	[37m	[39;49;00m[34mthis[39;49;00m.myInitTime[37m [39;49;00m=[37m [39;49;00m[34mthis[39;49;00m.generateValue();[37m[39;49;00m
    16	[94m%>[39;49;00m
    17
    18	[94m<%[39;49;00m[37m[39;49;00m
    19	[37m	[39;49;00m[37m/* data binding code block, executed each time as control is data bound */[39;49;00m[37m[39;49;00m
    20	[37m	[39;49;00m[34mthis[39;49;00m.myBindTime[37m [39;49;00m=[37m [39;49;00m[34mthis[39;49;00m.generateValue();[37m[39;49;00m
    21	[94m%>[39;49;00m
    22
    23	[94m<%[39;49;00m--[37m [39;49;00mJBST[37m [39;49;00mComment[37m [39;49;00m--[94m%>[39;49;00m
    24	<[94mspan[39;49;00m [36mstyle[39;49;00m=[33m"color:red"[39;49;00m>[94m<%=[39;49;00m[37m [39;49;00m[34mthis[39;49;00m.myBindTime[37m [39;49;00m[37m/* data binding expression */[39;49;00m[37m [39;49;00m[94m%>[39;49;00m</[94mspan[39;49;00m>
    25	<[94mspan[39;49;00m [36mstyle[39;49;00m=[33m"color:green"[39;49;00m>[94m<%=[39;49;00m[37m [39;49;00m[34mthis[39;49;00m.myInitTime[37m [39;49;00m[37m/* data binding expression */[39;49;00m[37m [39;49;00m[94m%>[39;49;00m</[94mspan[39;49;00m>
    26
    27	[37m<!-- HTML Comment -->[39;49;00m
    28	<[94mspan[39;49;00m [36mstyle[39;49;00m=[33m"color:blue"[39;49;00m>[94m<%[39;49;00m$[37m [39;49;00mResources:[37m [39;49;00mlocalizationKey[37m [39;49;00m[94m%>[39;49;00m[94m<%[39;49;00m--[37m [39;49;00mJBST[37m [39;49;00mglobalization--[94m%>[39;49;00m</[94mspan[39;49;00m>
