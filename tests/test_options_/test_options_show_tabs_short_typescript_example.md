[34mclass[39;49;00m[37m [39;49;00mAnimal[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00mconstructor(public[37m [39;49;00mname)[37m [39;49;00m{[37m [39;49;00m}[37m[39;49;00m
[37m    [39;49;00mmove(meters)[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00malert(this.name[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m moved [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mmeters[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33mm.[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34mclass[39;49;00m[37m [39;49;00mSnake[37m [39;49;00m[34mextends[39;49;00m[37m [39;49;00mAnimal[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00mconstructor(name)[37m [39;49;00m{[37m [39;49;00msuper(name);[37m [39;49;00m}[37m[39;49;00m
[37m    [39;49;00mmove()[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00malert([33m"[39;49;00m[33mSlithering...[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m        [39;49;00msuper.move([34m5[39;49;00m);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34mclass[39;49;00m[37m [39;49;00mHorse[37m [39;49;00m[34mextends[39;49;00m[37m [39;49;00mAnimal[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00mconstructor(name)[37m [39;49;00m{[37m [39;49;00msuper(name);[37m [39;49;00m}[37m[39;49;00m
[37m    [39;49;00mmove()[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00malert([33m"[39;49;00m[33mGalloping...[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m        [39;49;00msuper.move([34m45[39;49;00m);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[04m[91m@[39;49;00mView({[37m[39;49;00m
[37m    [39;49;00mtemplateUrl:[37m [39;49;00m[33m"[39;49;00m[33mapp/components/LoginForm.html[39;49;00m[33m"[39;49;00m,[37m[39;49;00m
[37m    [39;49;00mdirectives:[37m [39;49;00m[FORM_DIRECTIVES,[37m [39;49;00mNgIf][37m[39;49;00m
})[37m[39;49;00m
[04m[91m@[39;49;00mComponent({[37m[39;49;00m
[37m    [39;49;00mselector:[37m [39;49;00m[33m"[39;49;00m[33mlogin-form[39;49;00m[33m"[39;49;00m[37m[39;49;00m
})[37m[39;49;00m
[34mclass[39;49;00m[37m [39;49;00mLoginForm[37m [39;49;00m{[37m[39;49;00m
[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34mvar[39;49;00m[37m [39;49;00msam[37m [39;49;00m=[37m [39;49;00mnew[37m [39;49;00mSnake([33m"[39;49;00m[33mSammy the Python[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
[34mvar[39;49;00m[37m [39;49;00mtom:[37m [39;49;00mAnimal[37m [39;49;00m=[37m [39;49;00mnew[37m [39;49;00mHorse([33m"[39;49;00m[33mTommy the Palomino[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
[37m[39;49;00m
sam.move()[37m[39;49;00m
tom.move([34m34[39;49;00m)
