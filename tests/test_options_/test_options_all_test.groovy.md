     1^I[37m// This source code comes from http://www.odelia-technologies.com/node/200[39;49;00m[37m[39;49;00m$
     2^I[37m[39;49;00m$
     3^I[34mpackage[39;49;00m[37m [39;49;00mcom.[36modelia[39;49;00m.[36mgroovy[39;49;00m.[36msimpleworkflow[39;49;00m[37m[39;49;00m$
     4^I[37m[39;49;00m$
     5^I[37m[39;49;00m$
     6^I[34mclass[39;49;00m[37m [39;49;00m[04m[32mSimpleWorkflowEngine[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
     7^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00mworkflowMap[37m [39;49;00m=[37m [39;49;00m[:][37m[39;49;00m$
     8^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00mcontext[37m [39;49;00m=[37m [39;49;00m[:][37m[39;49;00m$
     9^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00mbeforeActivityName[37m [39;49;00m=[37m [39;49;00m[33m'beforeActivity'[39;49;00m[37m[39;49;00m$
    10^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00mafterActivityName[37m [39;49;00m=[37m [39;49;00m[33m'afterActivity'[39;49;00m[37m[39;49;00m$
    11^I[37m[39;49;00m$
    12^I[37m    [39;49;00mSimpleWorkflowEngine(workflow,[37m [39;49;00mcontext[37m [39;49;00m=[37m [39;49;00m[:])[37m [39;49;00m{[37m[39;49;00m$
    13^I[37m        [39;49;00m[34mthis[39;49;00m.[36mcontext[39;49;00m[37m [39;49;00m=[37m [39;49;00mcontext[37m[39;49;00m$
    14^I[37m        [39;49;00mparseWorkflow(workflow)[37m[39;49;00m$
    15^I[37m    [39;49;00m}[37m[39;49;00m$
    16^I[37m[39;49;00m$
    17^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00m[32mparseWorkflow[39;49;00m(workflow)[37m [39;49;00m{[37m[39;49;00m$
    18^I[37m        [39;49;00mworkflowMap[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mWorkflowParser().[36mparse[39;49;00m(workflow)[37m[39;49;00m$
    19^I[37m    [39;49;00m}[37m[39;49;00m$
    20^I[37m[39;49;00m$
    21^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00m[32mgetActivityValue[39;49;00m(activity)[37m [39;49;00m{[37m[39;49;00m$
    22^I[37m        [39;49;00m[34massert[39;49;00m[37m [39;49;00mactivity[37m [39;49;00m[34minstanceof[39;49;00m[37m [39;49;00mString[37m[39;49;00m$
    23^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!workflowMap[activity])[37m[39;49;00m$
    24^I[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mRuntimeException([33m"$activity activity doesn't exist"[39;49;00m)[37m[39;49;00m$
    25^I[37m        [39;49;00mworkflowMap[activity][37m[39;49;00m$
    26^I[37m    [39;49;00m}[37m[39;49;00m$
    27^I[37m[39;49;00m$
    28^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00m[32mexecute[39;49;00m(activity,[37m [39;49;00mpause)[37m [39;49;00m{[37m[39;49;00m$
    29^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(workflowMap[beforeActivityName])[37m [39;49;00m{[37m[39;49;00m$
    30^I[37m            [39;49;00mgetActivityValue(beforeActivityName)(context,[37m [39;49;00mactivity)[37m[39;49;00m$
    31^I[37m        [39;49;00m}[37m[39;49;00m$
    32^I[37m[39;49;00m$
    33^I[37m        [39;49;00m[36mdef[39;49;00m[37m [39;49;00mactivityValue[37m [39;49;00m=[37m [39;49;00mgetActivityValue(activity)[37m[39;49;00m$
    34^I[37m[39;49;00m$
    35^I[37m        [39;49;00m[37m// Determine the next activity to execute[39;49;00m[37m[39;49;00m$
    36^I[37m        [39;49;00m[36mdef[39;49;00m[37m [39;49;00mnextActivity[37m[39;49;00m$
    37^I[37m        [39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(activityValue)[37m [39;49;00m{[37m[39;49;00m$
    38^I[37m            [39;49;00m[34mcase[39;49;00m[37m [39;49;00mString:[37m [39;49;00mnextActivity[37m [39;49;00m=[37m [39;49;00mactivityValue;[37m [39;49;00m[34mbreak[39;49;00m[37m[39;49;00m$
    39^I[37m            [39;49;00m[34mcase[39;49;00m[37m [39;49;00mClosure:[37m [39;49;00mnextActivity[37m [39;49;00m=[37m [39;49;00mactivityValue(context);[37m [39;49;00m[34mbreak[39;49;00m[37m[39;49;00m$
    40^I[37m            [39;49;00m[34mcase[39;49;00m[37m [39;49;00mClass:[37m [39;49;00mnextActivity[37m [39;49;00m=[37m [39;49;00mactivityValue.[36mnewInstance[39;49;00m()(context)[37m[39;49;00m$
    41^I[37m        [39;49;00m}[37m[39;49;00m$
    42^I[37m[39;49;00m$
    43^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(workflowMap[afterActivityName])[37m [39;49;00m{[37m[39;49;00m$
    44^I[37m            [39;49;00mgetActivityValue(afterActivityName)(context,[37m [39;49;00mactivity,[37m [39;49;00mnextActivity)[37m[39;49;00m$
    45^I[37m        [39;49;00m}[37m[39;49;00m$
    46^I[37m[39;49;00m$
    47^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!pause[37m [39;49;00m&&[37m [39;49;00mnextActivity)[37m[39;49;00m$
    48^I[37m            [39;49;00mcall(nextActivity)[37m[39;49;00m$
    49^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
    50^I[37m            [39;49;00mnextActivity[37m[39;49;00m$
    51^I[37m    [39;49;00m}[37m[39;49;00m$
    52^I[37m[39;49;00m$
    53^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00m[32mcall[39;49;00m(activity)[37m [39;49;00m{[37m[39;49;00m$
    54^I[37m        [39;49;00mexecute(activity,[37m [39;49;00m[34mfalse[39;49;00m)[37m[39;49;00m$
    55^I[37m    [39;49;00m}[37m[39;49;00m$
    56^I[37m[39;49;00m$
    57^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00m[32mnextActivity[39;49;00m(activity)[37m [39;49;00m{[37m[39;49;00m$
    58^I[37m        [39;49;00mexecute(activity,[37m [39;49;00m[34mtrue[39;49;00m)[37m[39;49;00m$
    59^I[37m    [39;49;00m}[37m[39;49;00m$
    60^I[37m[39;49;00m$
    61^I[37m    [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mmain[39;49;00m(String[][37m [39;49;00margs)[37m [39;49;00m{[37m[39;49;00m$
    62^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(args.[36msize[39;49;00m()[37m [39;49;00m!=[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
    63^I[37m            [39;49;00mprintln[37m [39;49;00m[33m'Usage: com.odelia.groovy.simpleworkflow.SimpleWorkflowEngine <dsl_filename> <activity_name>'[39;49;00m[37m[39;49;00m$
    64^I[37m            [39;49;00m[34mreturn[39;49;00m[37m[39;49;00m$
    65^I[37m        [39;49;00m}[37m[39;49;00m$
    66^I[37m        [39;49;00mSimpleWorkflowEngine.[36mnewInstance[39;49;00m([34mnew[39;49;00m[37m [39;49;00mFile(args[[34m0[39;49;00m]))(args[[34m1[39;49;00m])[37m[39;49;00m$
    67^I[37m    [39;49;00m}[37m[39;49;00m$
    68^I[37m[39;49;00m$
    69^I}[37m[39;49;00m$
    70^I[37m[39;49;00m$
    71^I[34mprivate[39;49;00m[37m [39;49;00m[34mclass[39;49;00m[37m [39;49;00m[04m[32mWorkflowParser[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
    72^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00mmap[37m [39;49;00m=[37m [39;49;00m[:][37m[39;49;00m$
    73^I[37m[39;49;00m$
    74^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00m[32mmethodMissing[39;49;00m(String[37m [39;49;00mname,[37m [39;49;00margs)[37m [39;49;00m{[37m[39;49;00m$
    75^I[37m        [39;49;00mmap[name][37m [39;49;00m=[37m [39;49;00margs[[34m0[39;49;00m][37m[39;49;00m$
    76^I[37m    [39;49;00m}[37m[39;49;00m$
    77^I[37m[39;49;00m$
    78^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00m[32mparse[39;49;00m(Closure[37m [39;49;00mwf)[37m [39;49;00m{[37m[39;49;00m$
    79^I[37m        [39;49;00mwf.[36mdelegate[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
    80^I[37m        [39;49;00mwf.[36mresolveStrategy[39;49;00m[37m [39;49;00m=[37m [39;49;00mClosure.[36mDELEGATE_FIRST[39;49;00m[37m[39;49;00m$
    81^I[37m        [39;49;00mwf()[37m[39;49;00m$
    82^I[37m        [39;49;00mmap[37m[39;49;00m$
    83^I[37m    [39;49;00m}[37m[39;49;00m$
    84^I[37m[39;49;00m$
    85^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00mworkflow[37m [39;49;00m=[37m [39;49;00m{[37m [39;49;00mit[37m [39;49;00m->[37m[39;49;00m$
    86^I[37m        [39;49;00mit.[36mdelegate[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
    87^I[37m        [39;49;00mit.[36mresolveStrategy[39;49;00m[37m [39;49;00m=[37m [39;49;00mClosure.[36mDELEGATE_FIRST[39;49;00m[37m[39;49;00m$
    88^I[37m        [39;49;00mit()[37m[39;49;00m$
    89^I[37m    [39;49;00m}[37m[39;49;00m$
    90^I[37m[39;49;00m$
    91^I[37m    [39;49;00m[36mdef[39;49;00m[37m [39;49;00m[32mparse[39;49;00m(File[37m [39;49;00mworkflowDef)[37m [39;49;00m{[37m[39;49;00m$
    92^I[37m        [39;49;00m[36mdef[39;49;00m[37m [39;49;00mbinding[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBinding([workflow:[37m [39;49;00mworkflow])[37m[39;49;00m$
    93^I[37m        [39;49;00m[36mdef[39;49;00m[37m [39;49;00mshell[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mGroovyShell(binding)[37m[39;49;00m$
    94^I[37m        [39;49;00mshell.[36mevaluate[39;49;00m(workflowDef)[37m[39;49;00m$
    95^I[37m        [39;49;00mmap[37m[39;49;00m$
    96^I[37m    [39;49;00m}[37m[39;49;00m$
    97^I}$
