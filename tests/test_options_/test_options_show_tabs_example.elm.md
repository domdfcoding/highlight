[34mimport[39;49;00m[37m [39;49;00m[04m[32mMath.Vector3[39;49;00m[37m [39;49;00m[32m(..)[39;49;00m[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[32mMath.Matrix4[39;49;00m[37m [39;49;00m[32m(..)[39;49;00m[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[32mGraphics.WebGL[39;49;00m[37m [39;49;00m[32m(..)[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m-- Create a mesh with two triangles[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mtype[39;49;00m[37m [39;49;00m[36mVertex[39;49;00m[37m [39;49;00m[32m=[39;49;00m[37m [39;49;00m{[37m [39;49;00m[31mposition[39;49;00m[32m:[39;49;00m[36mVec3[39;49;00m,[37m [39;49;00m[31mcolor[39;49;00m[32m:[39;49;00m[36mVec3[39;49;00m[37m [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[31mmesh[39;49;00m[37m [39;49;00m[32m:[39;49;00m[37m [39;49;00m[[36mTriangle[39;49;00m[37m [39;49;00m[36mVertex[39;49;00m][37m[39;49;00m
[31mmesh[39;49;00m[37m [39;49;00m[32m=[39;49;00m[37m [39;49;00m[[37m [39;49;00m([37m [39;49;00m[36mVertex[39;49;00m[37m [39;49;00m([31mvec3[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mvec3[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
[37m         [39;49;00m,[37m [39;49;00m[36mVertex[39;49;00m[37m [39;49;00m([31mvec3[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m  [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mvec3[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
[37m         [39;49;00m,[37m [39;49;00m[36mVertex[39;49;00m[37m [39;49;00m([31mvec3[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[32m-[39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mvec3[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
[37m         [39;49;00m)[37m[39;49;00m
[37m       [39;49;00m][37m[39;49;00m
[37m[39;49;00m
[37m-- Create the scene[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mmain [39;49;00m[32m:[39;49;00m[37m [39;49;00m[36mSignal[39;49;00m[37m [39;49;00m[36mElement[39;49;00m[37m[39;49;00m
[34mmain [39;49;00m[32m=[39;49;00m[37m [39;49;00m[31mscene[39;49;00m[37m [39;49;00m[32m<~[39;49;00m[37m [39;49;00m[31mfoldp[39;49;00m[37m [39;49;00m[32m(+)[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mfps[39;49;00m[37m [39;49;00m[34m30[39;49;00m)[37m[39;49;00m
[37m[39;49;00m
[31mscene[39;49;00m[37m [39;49;00m[32m:[39;49;00m[37m [39;49;00m[36mFloat[39;49;00m[37m [39;49;00m[32m->[39;49;00m[37m [39;49;00m[36mElement[39;49;00m[37m[39;49;00m
[31mscene[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[32m=[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[31mwebgl[39;49;00m[37m [39;49;00m([34m400[39;49;00m,[34m400[39;49;00m)[37m[39;49;00m
[37m    [39;49;00m[[37m [39;49;00m[31mentity[39;49;00m[37m [39;49;00m[31mvertexShader[39;49;00m[37m [39;49;00m[31mfragmentShader[39;49;00m[37m [39;49;00m[31mmesh[39;49;00m[37m [39;49;00m{[37m [39;49;00m[31mview[39;49;00m[37m [39;49;00m[32m=[39;49;00m[37m [39;49;00m[31mview[39;49;00m[37m [39;49;00m([31mt[39;49;00m[37m [39;49;00m[32m/[39;49;00m[37m [39;49;00m[34m1000[39;49;00m)[37m [39;49;00m}[37m [39;49;00m][37m[39;49;00m
[37m[39;49;00m
[31mview[39;49;00m[37m [39;49;00m[32m:[39;49;00m[37m [39;49;00m[36mFloat[39;49;00m[37m [39;49;00m[32m->[39;49;00m[37m [39;49;00m[36mMat4[39;49;00m[37m[39;49;00m
[31mview[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[32m=[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[31mmul[39;49;00m[37m [39;49;00m([31mmakePerspective[39;49;00m[37m [39;49;00m[34m45[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m0.[39;49;00m[34m01[39;49;00m[37m [39;49;00m[34m100[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m([31mmakeLookAt[39;49;00m[37m [39;49;00m([31mvec3[39;49;00m[37m [39;49;00m([34m4[39;49;00m[37m [39;49;00m[32m*[39;49;00m[37m [39;49;00m[31mcos[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([34m4[39;49;00m[37m [39;49;00m[32m*[39;49;00m[37m [39;49;00m[31msin[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m [39;49;00m([31mvec3[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mvec3[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
[37m[39;49;00m
[37m-- Shaders[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[31mvertexShader[39;49;00m[37m [39;49;00m[32m:[39;49;00m[37m [39;49;00m[36mShader[39;49;00m[37m [39;49;00m{[37m [39;49;00m[31mattr[39;49;00m[37m [39;49;00m[32m|[39;49;00m[37m [39;49;00m[31mposition[39;49;00m[32m:[39;49;00m[36mVec3[39;49;00m,[37m [39;49;00m[31mcolor[39;49;00m[32m:[39;49;00m[36mVec3[39;49;00m[37m [39;49;00m}[37m [39;49;00m{[37m [39;49;00m[31munif[39;49;00m[37m [39;49;00m[32m|[39;49;00m[37m [39;49;00m[31mview[39;49;00m[32m:[39;49;00m[36mMat4[39;49;00m[37m [39;49;00m}[37m [39;49;00m{[37m [39;49;00m[31mvcolor[39;49;00m[32m:[39;49;00m[36mVec3[39;49;00m[37m [39;49;00m}[37m[39;49;00m
[31mvertexShader[39;49;00m[37m [39;49;00m[32m=[39;49;00m[37m [39;49;00m[glsl|[37m[39;49;00m
[37m[39;49;00m
attribute vec3 position;[37m[39;49;00m
attribute vec3 color;[37m[39;49;00m
uniform mat4 view;[37m[39;49;00m
varying vec3 vcolor;[37m[39;49;00m
[37m[39;49;00m
void main () {[37m[39;49;00m
    gl_Position = view * vec4(position, 1.0);[37m[39;49;00m
    vcolor = color;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
|][37m[39;49;00m
[37m[39;49;00m
[31mfragmentShader[39;49;00m[37m [39;49;00m[32m:[39;49;00m[37m [39;49;00m[36mShader[39;49;00m[37m [39;49;00m{}[37m [39;49;00m[31mu[39;49;00m[37m [39;49;00m{[37m [39;49;00m[31mvcolor[39;49;00m[32m:[39;49;00m[36mVec3[39;49;00m[37m [39;49;00m}[37m[39;49;00m
[31mfragmentShader[39;49;00m[37m [39;49;00m[32m=[39;49;00m[37m [39;49;00m[glsl|[37m[39;49;00m
[37m[39;49;00m
precision mediump float;[37m[39;49;00m
varying vec3 vcolor;[37m[39;49;00m
[37m[39;49;00m
void main () {[37m[39;49;00m
    gl_FragColor = vec4(vcolor, 1.0);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
|]
