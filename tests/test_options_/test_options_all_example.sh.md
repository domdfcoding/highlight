     1^I[37m#!/bin/bash[39;49;00m$
     2^I$
     3^I[36mprintf[39;49;00m [33m"%d %s\n"[39;49;00m [34m10[39;49;00m [33m"foo"[39;49;00m$
     4^I[36mprintf[39;49;00m [33m"%d %s\n"[39;49;00m [34m$(([39;49;00m[34m10#1[39;49;00m[34m))[39;49;00m [33m"bar"[39;49;00m$
     5^I$
     6^I[36mlet[39;49;00m [33m"[39;49;00m[33mm = 10#[39;49;00m[33m${[39;49;00m[31m1[39;49;00m:[31m1[39;49;00m:[31m2[39;49;00m[33m}[39;49;00m[33m"[39;49;00m$
     7^I[36mecho[39;49;00m [31m$m[39;49;00m$
     8^I$
     9^I[31mm[39;49;00m=[34m$(([39;49;00m[34m10#[39;49;00m[33m${[39;49;00m[31m1[39;49;00m:[31m4[39;49;00m:[31m3[39;49;00m[33m}[39;49;00m + [34m10#[39;49;00m[33m${[39;49;00m[31m1[39;49;00m:[31m1[39;49;00m:[31m3[39;49;00m[33m}[39;49;00m[34m))[39;49;00m$
    10^I[36mecho[39;49;00m [31m$m[39;49;00m$
    11^I$
    12^I[31mm[39;49;00m=[34m$(([39;49;00m[34m10#[39;49;00m[33m${[39;49;00m[31m1[39;49;00m:[31m4[39;49;00m:[31m3[39;49;00m[33m}[39;49;00m[34m))[39;49;00m$
    13^I[36mecho[39;49;00m [31m$m[39;49;00m$
    14^I$
    15^I[31mm[39;49;00m=[34m$(([39;49;00m[34m10#[39;49;00m[31m$1[39;49;00m[34m))[39;49;00m$
    16^I[36mecho[39;49;00m [31m$m[39;49;00m$
    17^I$
    18^I[31mm[39;49;00m=[34m$(([39;49;00m[34m10#1[39;49;00m[34m))[39;49;00m$
    19^I[36mecho[39;49;00m [31m$m[39;49;00m$
    20^I$
    21^I[31mm[39;49;00m=[34m$(([39;49;00m[34m10[39;49;00m[34m))[39;49;00m$
    22^I[36mecho[39;49;00m [31m$m[39;49;00m$
