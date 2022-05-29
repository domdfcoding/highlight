Using lexer <pygments.lexers.GLShaderLexer with {'ensurenl': False, 'tabsize': 0}>
[37m/* Vertex shader */[39;49;00m[37m[39;49;00m
[34muniform[39;49;00m[37m [39;49;00m[36mfloat[39;49;00m[37m [39;49;00mwaveTime;[37m[39;49;00m
[34muniform[39;49;00m[37m [39;49;00m[36mfloat[39;49;00m[37m [39;49;00mwaveWidth;[37m[39;49;00m
[34muniform[39;49;00m[37m [39;49;00m[36mfloat[39;49;00m[37m [39;49;00mwaveHeight;[37m[39;49;00m
[37m [39;49;00m
[36mvoid[39;49;00m[37m [39;49;00mmain([36mvoid[39;49;00m)[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[36mvec4[39;49;00m[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mvec4[39;49;00m([36mgl_Vertex[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mv.z[37m [39;49;00m=[37m [39;49;00msin(waveWidth[37m [39;49;00m*[37m [39;49;00mv.x[37m [39;49;00m+[37m [39;49;00mwaveTime)[37m [39;49;00m*[37m [39;49;00mcos(waveWidth[37m [39;49;00m*[37m [39;49;00mv.y[37m [39;49;00m+[37m [39;49;00mwaveTime)[37m [39;49;00m*[37m [39;49;00mwaveHeight;[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[36mgl_Position[39;49;00m[37m [39;49;00m=[37m [39;49;00m[36mgl_ModelViewProjectionMatrix[39;49;00m[37m [39;49;00m*[37m [39;49;00mv;[37m[39;49;00m
}
