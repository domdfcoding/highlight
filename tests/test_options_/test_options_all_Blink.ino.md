     1^I[37m/*[39;49;00m$
     2^I[37m  Blink[39;49;00m$
     3^I[37m  Turns on an LED on for one second, then off for one second, repeatedly.[39;49;00m$
     4^I[37m [39;49;00m$
     5^I[37m  This example code is in the public domain.[39;49;00m$
     6^I[37m */[39;49;00m[37m[39;49;00m$
     7^I[37m [39;49;00m[37m[39;49;00m$
     8^I[37m// Pin 13 has an LED connected on most Arduino boards.[39;49;00m$
     9^I[37m// give it a name:[39;49;00m$
    10^I[34mint[39;49;00m[37m [39;49;00mled[37m [39;49;00m=[37m [39;49;00m[34m13[39;49;00m;[37m[39;49;00m$
    11^I[37m[39;49;00m$
    12^I[37m// the setup routine runs once when you press reset:[39;49;00m$
    13^I[34mvoid[39;49;00m[37m [39;49;00m[36msetup[39;49;00m()[37m [39;49;00m{[37m[39;49;00m$
    14^I[37m  [39;49;00m[37m// initialize the digital pin as an output.[39;49;00m$
    15^I[37m  [39;49;00m[32mpinMode[39;49;00m(led,[37m [39;49;00m[34mOUTPUT[39;49;00m);[37m     [39;49;00m[37m[39;49;00m$
    16^I}[37m[39;49;00m$
    17^I[37m[39;49;00m$
    18^I[37m// the loop routine runs over and over again forever:[39;49;00m$
    19^I[34mvoid[39;49;00m[37m [39;49;00m[36mloop[39;49;00m()[37m [39;49;00m{[37m[39;49;00m$
    20^I[37m  [39;49;00m[32mdigitalWrite[39;49;00m(led,[37m [39;49;00m[34mHIGH[39;49;00m);[37m   [39;49;00m[37m// turn the LED on (HIGH is the voltage level)[39;49;00m$
    21^I[37m  [39;49;00m[32mdelay[39;49;00m([34m1000[39;49;00m);[37m               [39;49;00m[37m// wait for a second[39;49;00m$
    22^I[37m  [39;49;00m[32mdigitalWrite[39;49;00m(led,[37m [39;49;00m[34mLOW[39;49;00m);[37m    [39;49;00m[37m// turn the LED off by making the voltage LOW[39;49;00m$
    23^I[37m  [39;49;00m[32mdelay[39;49;00m([34m1000[39;49;00m);[37m               [39;49;00m[37m// wait for a second[39;49;00m$
    24^I}$
