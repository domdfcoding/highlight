Using lexer <pygments.lexers.ArduinoLexer with {'ensurenl': False, 'tabsize': 0}>
[37m/*[39;49;00m
[37m  Blink[39;49;00m
[37m  Turns on an LED on for one second, then off for one second, repeatedly.[39;49;00m
[37m [39;49;00m
[37m  This example code is in the public domain.[39;49;00m
[37m */[39;49;00m[37m[39;49;00m
[37m [39;49;00m[37m[39;49;00m
[37m// Pin 13 has an LED connected on most Arduino boards.[39;49;00m
[37m// give it a name:[39;49;00m
[34mint[39;49;00m[37m [39;49;00mled[37m [39;49;00m=[37m [39;49;00m[34m13[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[37m// the setup routine runs once when you press reset:[39;49;00m
[34mvoid[39;49;00m[37m [39;49;00m[36msetup[39;49;00m()[37m [39;49;00m{[37m[39;49;00m
[37m  [39;49;00m[37m// initialize the digital pin as an output.[39;49;00m
[37m  [39;49;00m[32mpinMode[39;49;00m(led,[37m [39;49;00m[34mOUTPUT[39;49;00m);[37m     [39;49;00m[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m// the loop routine runs over and over again forever:[39;49;00m
[34mvoid[39;49;00m[37m [39;49;00m[36mloop[39;49;00m()[37m [39;49;00m{[37m[39;49;00m
[37m  [39;49;00m[32mdigitalWrite[39;49;00m(led,[37m [39;49;00m[34mHIGH[39;49;00m);[37m   [39;49;00m[37m// turn the LED on (HIGH is the voltage level)[39;49;00m
[37m  [39;49;00m[32mdelay[39;49;00m([34m1000[39;49;00m);[37m               [39;49;00m[37m// wait for a second[39;49;00m
[37m  [39;49;00m[32mdigitalWrite[39;49;00m(led,[37m [39;49;00m[34mLOW[39;49;00m);[37m    [39;49;00m[37m// turn the LED off by making the voltage LOW[39;49;00m
[37m  [39;49;00m[32mdelay[39;49;00m([34m1000[39;49;00m);[37m               [39;49;00m[37m// wait for a second[39;49;00m
}
