     1^I[36mproject[39;49;00m([33m'pygments'[39;49;00m,[37m [39;49;00m[33m'c'[39;49;00m,[37m[39;49;00m$
     2^I[37m  [39;49;00mversion[37m [39;49;00m:[37m [39;49;00m[33m'0.1'[39;49;00m,[37m[39;49;00m$
     3^I[37m  [39;49;00mdefault_options[37m [39;49;00m:[37m [39;49;00m[[33m'warning_level=3'[39;49;00m][37m[39;49;00m$
     4^I)[37m[39;49;00m$
     5^I[04m[36mimport[39;49;00m([33m'fs'[39;49;00m)[37m[39;49;00m$
     6^Ibuilder[37m [39;49;00m=[37m [39;49;00m[31mbuild_machine[39;49;00m[37m[39;49;00m$
     7^Itarget[37m [39;49;00m=[37m [39;49;00m[31mtarget_machine[39;49;00m[37m[39;49;00m$
     8^Ihost[37m [39;49;00m=[37m [39;49;00m[31mhost_machine[39;49;00m[37m[39;49;00m$
     9^I[37m[39;49;00m$
    10^I[37m# This is a comment[39;49;00m[37m[39;49;00m$
    11^Icc[37m [39;49;00m=[37m [39;49;00m[31mmeson[39;49;00m.get_compiler([33m'c'[39;49;00m)[37m[39;49;00m$
    12^Icc.compiles([37m[39;49;00m$
    13^I[33m'''[39;49;00m$
    14^I[33m/*This[39;49;00m$
    15^I[33m''[39;49;00m$
    16^I[33mis a multiline string[39;49;00m$
    17^I[33m[39;49;00m$
    18^I[33m# with an embedded line that looks like a comment[39;49;00m$
    19^I[33m[39;49;00m$
    20^I[33mand some other elements like[39;49;00m$
    21^I[33m[39;49;00m$
    22^I[33mtrue false[39;49;00m$
    23^I[33m0 1[39;49;00m$
    24^I[33mproject()[39;49;00m$
    25^I[33m*/[39;49;00m$
    26^I[33m#include <stdio.h>[39;49;00m$
    27^I[33mint main(void) {[39;49;00m$
    28^I[33m  printf("hello\n");[39;49;00m$
    29^I[33m}[39;49;00m$
    30^I[33m'''[39;49;00m[37m[39;49;00m$
    31^I)[37m[39;49;00m$
    32^Iexe[37m [39;49;00m=[37m [39;49;00m[36mexecutable[39;49;00m([33m'pygments'[39;49;00m,[37m [39;49;00m[33m'pygments.c'[39;49;00m,[37m [39;49;00minstall[37m [39;49;00m:[37m [39;49;00m[34mtrue[39;49;00m)[37m[39;49;00m$
    33^Idep[37m [39;49;00m=[37m [39;49;00mcc.find_library([33m'foo'[39;49;00m,[37m [39;49;00m[36mdisabler[39;49;00m:[37m [39;49;00m[34mtrue[39;49;00m)[37m[39;49;00m$
    34^I[37m[39;49;00m$
    35^I[34mforeach[39;49;00m[37m [39;49;00mx[37m [39;49;00m:[37m [39;49;00m[[34m42[39;49;00m,[37m [39;49;00m[34m0x55000[39;49;00m,[37m [39;49;00m[34m0o6[39;49;00m,[37m [39;49;00mexe][37m[39;49;00m$
    36^I[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m[35mnot[39;49;00m[37m [39;49;00m[36mis_disabler[39;49;00m(dep)[37m[39;49;00m$
    37^I[37m    [39;49;00m[36mlibrary[39;49;00m([33m'lib'[39;49;00m,[37m [39;49;00m[33m'lib.c'[39;49;00m,[37m [39;49;00m[36minclude_directories[39;49;00m:[37m [39;49;00m[],[37m [39;49;00mdependencies:[37m [39;49;00mdep)[37m[39;49;00m$
    38^I[37m  [39;49;00m[34melif[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m[39;49;00m$
    39^I[37m    [39;49;00m[36mboth_libraries[39;49;00m([33m'lib'[39;49;00m,[37m [39;49;00m[33m'lib2.c'[39;49;00m)[37m[39;49;00m$
    40^I[37m  [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
    41^I[37m    [39;49;00m[36mmessage[39;49;00m([33m'failed'[39;49;00m)[37m[39;49;00m$
    42^I[37m    [39;49;00m[34mcontinue[39;49;00m[37m[39;49;00m$
    43^I[37m  [39;49;00m[34mendif[39;49;00m[37m[39;49;00m$
    44^I[37m  [39;49;00m[34mbreak[39;49;00m[37m[39;49;00m$
    45^I[34mendforeach[39;49;00m[37m[39;49;00m$
    46^I[37m[39;49;00m$
    47^I[36mtest[39;49;00m([33m'basic'[39;49;00m,[37m [39;49;00mexe)[37m[39;49;00m$
    48^I[36msubdir[39;49;00m([33m'dir'[39;49;00m)[37m[39;49;00m$
    49^I[34mif[39;49;00m[37m [39;49;00m[35mnot[39;49;00m[37m [39;49;00m[36mget_option[39;49;00m([33m'build-docs'[39;49;00m)[37m[39;49;00m$
    50^I[37m  [39;49;00m[36msummary[39;49;00m({[33m'docs'[39;49;00m:[37m [39;49;00m[[34mfalse[39;49;00m,[37m [39;49;00m[33m'(disabled by config)'[39;49;00m]},[37m [39;49;00msection:[37m [39;49;00m[33m'Configuration'[39;49;00m)[37m[39;49;00m$
    51^I[37m  [39;49;00m[36msubdir_done[39;49;00m()[37m[39;49;00m$
    52^I[34mendif[39;49;00m$
