     1^I[37m// A few random snippets of HLSL shader code I gathered...[39;49;00m[37m[39;49;00m$
     2^I[37m[39;49;00m$
     3^I[[90mnumthreads[39;49;00m([34m256[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m)][37m[39;49;00m$
     4^I[36mvoid[39;49;00m[37m [39;49;00mcs_main([36muint3[39;49;00m[37m [39;49;00mthreadId[37m [39;49;00m:[37m [39;49;00m[90mSV_DispatchThreadID[39;49;00m)[37m[39;49;00m$
     5^I{[37m[39;49;00m$
     6^I[37m^I[39;49;00m[37m// Seed the PRNG using the thread ID[39;49;00m[37m[39;49;00m$
     7^I[37m^I[39;49;00mrng_state[37m [39;49;00m=[37m [39;49;00mthreadId.x;[37m[39;49;00m$
     8^I[37m[39;49;00m$
     9^I[37m^I[39;49;00m[37m// Generate a few numbers...[39;49;00m[37m[39;49;00m$
    10^I[37m^I[39;49;00m[36muint[39;49;00m[37m [39;49;00mr0[37m [39;49;00m=[37m [39;49;00mrand_xorshift();[37m[39;49;00m$
    11^I[37m^I[39;49;00m[36muint[39;49;00m[37m [39;49;00mr1[37m [39;49;00m=[37m [39;49;00mrand_xorshift();[37m[39;49;00m$
    12^I[37m^I[39;49;00m[37m// Do some stuff with them...[39;49;00m[37m[39;49;00m$
    13^I[37m[39;49;00m$
    14^I[37m^I[39;49;00m[37m// Generate a random float in [0, 1)...[39;49;00m[37m[39;49;00m$
    15^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m [39;49;00mf0[37m [39;49;00m=[37m [39;49;00m[36mfloat[39;49;00m(rand_xorshift())[37m [39;49;00m*[37m [39;49;00m([34m1.0[39;49;00m[37m [39;49;00m/[37m [39;49;00m[34m4294967296.0[39;49;00m);[37m[39;49;00m$
    16^I[37m[39;49;00m$
    17^I[37m^I[39;49;00m[37m// ...etc.[39;49;00m[37m[39;49;00m$
    18^I}[37m[39;49;00m$
    19^I[37m[39;49;00m$
    20^I[37m// Constant buffer of parameters[39;49;00m[37m[39;49;00m$
    21^I[34mcbuffer[39;49;00m[37m [39;49;00mIntegratorParams[37m [39;49;00m:[37m [39;49;00m[34mregister[39;49;00m(b0)[37m[39;49;00m$
    22^I{[37m[39;49;00m$
    23^I[37m^I[39;49;00m[36mfloat2[39;49;00m[37m [39;49;00mspecPow;[37m^I^I[39;49;00m[37m// Spec powers in XY directions (equal for isotropic BRDFs)[39;49;00m[37m[39;49;00m$
    24^I[37m^I[39;49;00m[36mfloat3[39;49;00m[37m [39;49;00mL;[37m^I^I^I[39;49;00m[37m// Unit vector toward light [39;49;00m[37m[39;49;00m$
    25^I[37m^I[39;49;00m[36mint2[39;49;00m[37m [39;49;00mcThread;[37m^I^I[39;49;00m[37m// Total threads launched in XY dimensions[39;49;00m[37m[39;49;00m$
    26^I[37m^I[39;49;00m[36mint2[39;49;00m[37m [39;49;00mxyOutput;[37m^I^I[39;49;00m[37m// Where in the output buffer to store the result[39;49;00m[37m[39;49;00m$
    27^I}[37m[39;49;00m$
    28^I[37m[39;49;00m$
    29^I[34mstatic[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00m[36mfloat[39;49;00m[37m [39;49;00mpi[37m [39;49;00m=[37m [39;49;00m[34m3.141592654[39;49;00m;[37m[39;49;00m$
    30^I[37m[39;49;00m$
    31^I[36mfloat[39;49;00m[37m [39;49;00mAshikhminShirleyNDF([36mfloat3[39;49;00m[37m [39;49;00mH)[37m[39;49;00m$
    32^I{[37m[39;49;00m$
    33^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m [39;49;00mnormFactor[37m [39;49;00m=[37m [39;49;00m[36msqrt[39;49;00m((specPow.x[37m [39;49;00m+[37m [39;49;00m[34m2.0f[39;49;00m)[37m [39;49;00m*[37m [39;49;00m(specPow.y[37m [39;49;00m+[37m [39;49;00m[34m2.0[39;49;00m))[37m [39;49;00m*[37m [39;49;00m([34m0.5f[39;49;00m[37m [39;49;00m/[37m [39;49;00mpi);[37m[39;49;00m$
    34^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m [39;49;00mNdotH[37m [39;49;00m=[37m [39;49;00mH.z;[37m[39;49;00m$
    35^I[37m^I[39;49;00m[36mfloat2[39;49;00m[37m [39;49;00mHxy[37m [39;49;00m=[37m [39;49;00m[36mnormalize[39;49;00m(H.xy);[37m[39;49;00m$
    36^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mnormFactor[37m [39;49;00m*[37m [39;49;00m[36mpow[39;49;00m(NdotH,[37m [39;49;00m[36mdot[39;49;00m(specPow,[37m [39;49;00mHxy[37m [39;49;00m*[37m [39;49;00mHxy));[37m[39;49;00m$
    37^I}[37m[39;49;00m$
    38^I[37m[39;49;00m$
    39^I[36mfloat[39;49;00m[37m [39;49;00mBeckmannNDF([36mfloat3[39;49;00m[37m [39;49;00mH)[37m[39;49;00m$
    40^I{[37m[39;49;00m$
    41^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m [39;49;00mglossFactor[37m [39;49;00m=[37m [39;49;00mspecPow.x[37m [39;49;00m*[37m [39;49;00m[34m0.5f[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1.0f[39;49;00m;[37m^I[39;49;00m[37m// This is 1/m^2 in the usual Beckmann formula[39;49;00m[37m[39;49;00m$
    42^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m [39;49;00mnormFactor[37m [39;49;00m=[37m [39;49;00mglossFactor[37m [39;49;00m*[37m [39;49;00m([34m1.0f[39;49;00m[37m [39;49;00m/[37m [39;49;00mpi);[37m[39;49;00m$
    43^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m [39;49;00mNdotHSq[37m [39;49;00m=[37m [39;49;00mH.z[37m [39;49;00m*[37m [39;49;00mH.z;[37m[39;49;00m$
    44^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mnormFactor[37m [39;49;00m/[37m [39;49;00m(NdotHSq[37m [39;49;00m*[37m [39;49;00mNdotHSq)[37m [39;49;00m*[37m [39;49;00m[36mexp[39;49;00m(glossFactor[37m [39;49;00m*[37m [39;49;00m([34m1.0f[39;49;00m[37m [39;49;00m-[37m [39;49;00m[34m1.0f[39;49;00m[37m [39;49;00m/[37m [39;49;00mNdotHSq));[37m[39;49;00m$
    45^I}[37m[39;49;00m$
    46^I[37m[39;49;00m$
    47^I[37m// Output buffer for compute shader (actually float, but must be declared as uint[39;49;00m[37m[39;49;00m$
    48^I[37m// for atomic operations to work)[39;49;00m[37m[39;49;00m$
    49^I[34mgloballycoherent[39;49;00m[37m [39;49;00m[36mRWTexture2D[39;49;00m<[36muint[39;49;00m>[37m [39;49;00mo_data[37m [39;49;00m:[37m [39;49;00m[34mregister[39;49;00m(u0);[37m[39;49;00m$
    50^I[37m[39;49;00m$
    51^I[37m// Sum up the outputs of all threads and store to the output location[39;49;00m[37m[39;49;00m$
    52^I[34mstatic[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00m[36muint[39;49;00m[37m [39;49;00mthreadGroupSize2D[37m [39;49;00m=[37m [39;49;00m[34m16[39;49;00m;[37m[39;49;00m$
    53^I[34mstatic[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00m[36muint[39;49;00m[37m [39;49;00mthreadGroupSize1D[37m [39;49;00m=[37m [39;49;00mthreadGroupSize2D[37m [39;49;00m*[37m [39;49;00mthreadGroupSize2D;[37m[39;49;00m$
    54^I[34mgroupshared[39;49;00m[37m [39;49;00m[36mfloat[39;49;00m[37m [39;49;00mg_partialSums[threadGroupSize1D];[37m[39;49;00m$
    55^I[36mvoid[39;49;00m[37m [39;49;00mSumAcrossThreadsAndStore([36mfloat[39;49;00m[37m [39;49;00mvalue,[37m [39;49;00m[36muint[39;49;00m[37m [39;49;00miThreadInGroup)[37m[39;49;00m$
    56^I{[37m[39;49;00m$
    57^I[37m^I[39;49;00m[37m// First reduce within the threadgroup: partial sums of 2, 4, 8... elements[39;49;00m[37m[39;49;00m$
    58^I[37m^I[39;49;00m[37m// are calculated by 1/2, 1/4, 1/8... of the threads, always keeping the[39;49;00m[37m[39;49;00m$
    59^I[37m^I[39;49;00m[37m// active threads at the front of the group to minimize divergence.[39;49;00m[37m[39;49;00m$
    60^I[37m[39;49;00m$
    61^I[37m^I[39;49;00m[37m// NOTE: there are faster ways of doing this...but this is simple to code[39;49;00m[37m[39;49;00m$
    62^I[37m^I[39;49;00m[37m// and good enough.[39;49;00m[37m[39;49;00m$
    63^I[37m[39;49;00m$
    64^I[37m^I[39;49;00mg_partialSums[iThreadInGroup][37m [39;49;00m=[37m [39;49;00mvalue;[37m[39;49;00m$
    65^I[37m^I[39;49;00m[36mGroupMemoryBarrierWithGroupSync[39;49;00m();[37m[39;49;00m$
    66^I[37m[39;49;00m$
    67^I[37m^I[39;49;00m[[90munroll[39;49;00m][37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36muint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00mthreadGroupSize1D[37m [39;49;00m/[37m [39;49;00m[34m2[39;49;00m;[37m [39;49;00mi[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m/=[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
    68^I[37m^I[39;49;00m{[37m[39;49;00m$
    69^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(iThreadInGroup[37m [39;49;00m<[37m [39;49;00mi)[37m[39;49;00m$
    70^I[37m^I^I[39;49;00m{[37m[39;49;00m$
    71^I[37m^I^I^I[39;49;00mg_partialSums[iThreadInGroup][37m [39;49;00m+=[37m [39;49;00mg_partialSums[iThreadInGroup[37m [39;49;00m+[37m [39;49;00mi];[37m[39;49;00m$
    72^I[37m^I^I[39;49;00m}[37m[39;49;00m$
    73^I[37m^I^I[39;49;00m[36mGroupMemoryBarrierWithGroupSync[39;49;00m();[37m[39;49;00m$
    74^I[37m^I[39;49;00m}[37m[39;49;00m$
    75^I[37m[39;49;00m$
    76^I[37m^I[39;49;00m[37m// Then reduce across threadgroups: one thread from each group adds the group[39;49;00m[37m[39;49;00m$
    77^I[37m^I[39;49;00m[37m// total to the final output location, using a software transactional memory[39;49;00m[37m[39;49;00m$
    78^I[37m^I[39;49;00m[37m// style since D3D11 doesn't support atomic add on floats.[39;49;00m[37m[39;49;00m$
    79^I[37m^I[39;49;00m[37m// (Assumes the output value has been cleared to zero beforehand.)[39;49;00m[37m[39;49;00m$
    80^I[37m[39;49;00m$
    81^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(iThreadInGroup[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
    82^I[37m^I[39;49;00m{[37m[39;49;00m$
    83^I[37m^I^I[39;49;00m[36mfloat[39;49;00m[37m [39;49;00mthreadGroupSum[37m [39;49;00m=[37m [39;49;00mg_partialSums[[34m0[39;49;00m];[37m[39;49;00m$
    84^I[37m^I^I[39;49;00m[36muint[39;49;00m[37m [39;49;00moutputValueRead[37m [39;49;00m=[37m [39;49;00mo_data[xyOutput];[37m[39;49;00m$
    85^I[37m^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m([34mtrue[39;49;00m)[37m[39;49;00m$
    86^I[37m^I^I[39;49;00m{[37m[39;49;00m$
    87^I[37m^I^I^I[39;49;00m[36muint[39;49;00m[37m [39;49;00mnewOutputValue[37m [39;49;00m=[37m [39;49;00m[36masuint[39;49;00m([36masfloat[39;49;00m(outputValueRead)[37m [39;49;00m+[37m [39;49;00mthreadGroupSum);[37m[39;49;00m$
    88^I[37m^I^I^I[39;49;00m[36muint[39;49;00m[37m [39;49;00mpreviousOutputValue;[37m[39;49;00m$
    89^I[37m^I^I^I[39;49;00m[36mInterlockedCompareExchange[39;49;00m([37m[39;49;00m$
    90^I[37m^I^I^I^I[39;49;00mo_data[xyOutput],[37m [39;49;00moutputValueRead,[37m [39;49;00mnewOutputValue,[37m [39;49;00mpreviousOutputValue);[37m[39;49;00m$
    91^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(previousOutputValue[37m [39;49;00m==[37m [39;49;00moutputValueRead)[37m[39;49;00m$
    92^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
    93^I[37m^I^I^I[39;49;00moutputValueRead[37m [39;49;00m=[37m [39;49;00mpreviousOutputValue;[37m[39;49;00m$
    94^I[37m^I^I[39;49;00m}[37m[39;49;00m$
    95^I[37m^I[39;49;00m}[37m[39;49;00m$
    96^I}[37m[39;49;00m$
    97^I[37m[39;49;00m$
    98^I[36mvoid[39;49;00m[37m [39;49;00mmain([37m[39;49;00m$
    99^I[37m^I[39;49;00m[34min[39;49;00m[37m [39;49;00mVertex[37m [39;49;00mi_vtx,[37m[39;49;00m$
   100^I[37m^I[39;49;00m[34mout[39;49;00m[37m [39;49;00mVertex[37m [39;49;00mo_vtx,[37m[39;49;00m$
   101^I[37m^I[39;49;00m[34mout[39;49;00m[37m [39;49;00m[36mfloat3[39;49;00m[37m [39;49;00mo_vecCamera[37m [39;49;00m:[37m [39;49;00mCAMERA,[37m[39;49;00m$
   102^I[37m^I[39;49;00m[34mout[39;49;00m[37m [39;49;00m[36mfloat4[39;49;00m[37m [39;49;00mo_uvzwShadow[37m [39;49;00m:[37m [39;49;00mUVZW_SHADOW,[37m[39;49;00m$
   103^I[37m^I[39;49;00m[34mout[39;49;00m[37m [39;49;00m[36mfloat4[39;49;00m[37m [39;49;00mo_posClip[37m [39;49;00m:[37m [39;49;00m[90mSV_Position[39;49;00m)[37m[39;49;00m$
   104^I{[37m[39;49;00m$
   105^I[37m^I[39;49;00mo_vtx[37m [39;49;00m=[37m [39;49;00mi_vtx;[37m[39;49;00m$
   106^I[37m^I[39;49;00mo_vecCamera[37m [39;49;00m=[37m [39;49;00mg_posCamera[37m [39;49;00m-[37m [39;49;00mi_vtx.m_pos;[37m[39;49;00m$
   107^I[37m^I[39;49;00mo_uvzwShadow[37m [39;49;00m=[37m [39;49;00m[36mmul[39;49;00m([36mfloat4[39;49;00m(i_vtx.m_pos,[37m [39;49;00m[34m1.0[39;49;00m),[37m [39;49;00mg_matWorldToUvzwShadow);[37m[39;49;00m$
   108^I[37m^I[39;49;00mo_posClip[37m [39;49;00m=[37m [39;49;00m[36mmul[39;49;00m([36mfloat4[39;49;00m(i_vtx.m_pos,[37m [39;49;00m[34m1.0[39;49;00m),[37m [39;49;00mg_matWorldToClip);[37m[39;49;00m$
   109^I}[37m[39;49;00m$
   110^I[37m[39;49;00m$
   111^I[36m#pragma pack_matrix(row_major)[39;49;00m[37m[39;49;00m$
   112^I[37m[39;49;00m$
   113^I[34mstruct[39;49;00m[37m [39;49;00mVertex[37m[39;49;00m$
   114^I{[37m[39;49;00m$
   115^I[37m^I[39;49;00m[36mfloat3[39;49;00m[37m^I^I[39;49;00mm_pos[37m^I^I[39;49;00m:[37m [39;49;00mPOSITION;[37m[39;49;00m$
   116^I[37m^I[39;49;00m[36mfloat3[39;49;00m[37m^I^I[39;49;00mm_normal[37m^I[39;49;00m:[37m [39;49;00mNORMAL;[37m[39;49;00m$
   117^I[37m^I[39;49;00m[36mfloat2[39;49;00m[37m^I^I[39;49;00mm_uv[37m^I^I[39;49;00m:[37m [39;49;00mUV;[37m[39;49;00m$
   118^I};[37m[39;49;00m$
   119^I[37m[39;49;00m$
   120^I[34mcbuffer[39;49;00m[37m [39;49;00mCBFrame[37m [39;49;00m:[37m [39;49;00mCB_FRAME[37m^I^I^I^I^I[39;49;00m[37m// matches struct CBFrame in test.cpp[39;49;00m[37m[39;49;00m$
   121^I{[37m[39;49;00m$
   122^I[37m^I[39;49;00m[36mfloat4x4[39;49;00m[37m^I[39;49;00mg_matWorldToClip;[37m[39;49;00m$
   123^I[37m^I[39;49;00m[36mfloat4x4[39;49;00m[37m^I[39;49;00mg_matWorldToUvzwShadow;[37m[39;49;00m$
   124^I[37m^I[39;49;00m[36mfloat3x3[39;49;00m[37m^I[39;49;00mg_matWorldToUvzShadowNormal;[37m[39;49;00m$
   125^I[37m^I[39;49;00m[36mfloat3[39;49;00m[37m^I^I[39;49;00mg_posCamera;[37m[39;49;00m$
   126^I[37m[39;49;00m$
   127^I[37m^I[39;49;00m[36mfloat3[39;49;00m[37m^I^I[39;49;00mg_vecDirectionalLight;[37m[39;49;00m$
   128^I[37m^I[39;49;00m[36mfloat3[39;49;00m[37m^I^I[39;49;00mg_rgbDirectionalLight;[37m[39;49;00m$
   129^I[37m[39;49;00m$
   130^I[37m^I[39;49;00m[36mfloat2[39;49;00m[37m^I^I[39;49;00mg_dimsShadowMap;[37m[39;49;00m$
   131^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m^I^I[39;49;00mg_normalOffsetShadow;[37m[39;49;00m$
   132^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m^I^I[39;49;00mg_shadowSharpening;[37m[39;49;00m$
   133^I[37m[39;49;00m$
   134^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m^I^I[39;49;00mg_exposure;[37m^I^I^I^I^I[39;49;00m[37m// Exposure multiplier[39;49;00m[37m[39;49;00m$
   135^I}[37m[39;49;00m$
   136^I[37m[39;49;00m$
   137^I[36mTexture2D[39;49;00m<[36mfloat3[39;49;00m>[37m [39;49;00mg_texDiffuse[37m [39;49;00m:[37m [39;49;00m[34mregister[39;49;00m(t0);[37m[39;49;00m$
   138^I[36mSamplerState[39;49;00m[37m [39;49;00mg_ss[37m [39;49;00m:[37m [39;49;00m[34mregister[39;49;00m(s0);[37m[39;49;00m$
   139^I[37m[39;49;00m$
   140^I[36mvoid[39;49;00m[37m [39;49;00mmain([37m[39;49;00m$
   141^I[37m^I[39;49;00m[34min[39;49;00m[37m [39;49;00mVertex[37m [39;49;00mi_vtx,[37m[39;49;00m$
   142^I[37m^I[39;49;00m[34min[39;49;00m[37m [39;49;00m[36mfloat3[39;49;00m[37m [39;49;00mi_vecCamera[37m [39;49;00m:[37m [39;49;00mCAMERA,[37m[39;49;00m$
   143^I[37m^I[39;49;00m[34min[39;49;00m[37m [39;49;00m[36mfloat4[39;49;00m[37m [39;49;00mi_uvzwShadow[37m [39;49;00m:[37m [39;49;00mUVZW_SHADOW,[37m[39;49;00m$
   144^I[37m^I[39;49;00m[34mout[39;49;00m[37m [39;49;00m[36mfloat3[39;49;00m[37m [39;49;00mo_rgb[37m [39;49;00m:[37m [39;49;00m[90mSV_Target[39;49;00m)[37m[39;49;00m$
   145^I{[37m[39;49;00m$
   146^I[37m^I[39;49;00m[36mfloat3[39;49;00m[37m [39;49;00mnormal[37m [39;49;00m=[37m [39;49;00m[36mnormalize[39;49;00m(i_vtx.m_normal);[37m[39;49;00m$
   147^I[37m[39;49;00m$
   148^I[37m^I[39;49;00m[37m// Sample shadow map[39;49;00m[37m[39;49;00m$
   149^I[37m^I[39;49;00m[36mfloat[39;49;00m[37m [39;49;00mshadow[37m [39;49;00m=[37m [39;49;00mEvaluateShadow(i_uvzwShadow,[37m [39;49;00mnormal);[37m[39;49;00m$
   150^I[37m[39;49;00m$
   151^I[37m^I[39;49;00m[37m// Evaluate diffuse lighting[39;49;00m[37m[39;49;00m$
   152^I[37m^I[39;49;00m[36mfloat3[39;49;00m[37m [39;49;00mdiffuseColor[37m [39;49;00m=[37m [39;49;00mg_texDiffuse.Sample(g_ss,[37m [39;49;00mi_vtx.m_uv);[37m[39;49;00m$
   153^I[37m^I[39;49;00m[36mfloat3[39;49;00m[37m [39;49;00mdiffuseLight[37m [39;49;00m=[37m [39;49;00mg_rgbDirectionalLight[37m [39;49;00m*[37m [39;49;00m(shadow[37m [39;49;00m*[37m [39;49;00m[36msaturate[39;49;00m([36mdot[39;49;00m(normal,[37m [39;49;00mg_vecDirectionalLight)));[37m[39;49;00m$
   154^I[37m^I[39;49;00mdiffuseLight[37m [39;49;00m+=[37m [39;49;00mSimpleAmbient(normal);[37m[39;49;00m$
   155^I[37m[39;49;00m$
   156^I[37m^I[39;49;00mo_rgb[37m [39;49;00m=[37m [39;49;00mdiffuseColor[37m [39;49;00m*[37m [39;49;00mdiffuseLight;[37m[39;49;00m$
   157^I}[37m[39;49;00m$
   158^I[37m[39;49;00m$
   159^I[[90mdomain[39;49;00m([33m"[39;49;00m[33mquad[39;49;00m[33m"[39;49;00m)][37m[39;49;00m$
   160^I[36mvoid[39;49;00m[37m [39;49;00mds([37m[39;49;00m$
   161^I[37m^I[39;49;00m[34min[39;49;00m[37m [39;49;00m[36mfloat[39;49;00m[37m [39;49;00medgeFactors[[34m4[39;49;00m][37m [39;49;00m:[37m [39;49;00m[90mSV_TessFactor[39;49;00m,[37m[39;49;00m$
   162^I[37m^I[39;49;00m[34min[39;49;00m[37m [39;49;00m[36mfloat[39;49;00m[37m [39;49;00minsideFactors[[34m2[39;49;00m][37m [39;49;00m:[37m [39;49;00m[90mSV_InsideTessFactor[39;49;00m,[37m[39;49;00m$
   163^I[37m^I[39;49;00m[34min[39;49;00m[37m [39;49;00m[36mOutputPatch[39;49;00m<VData,[37m [39;49;00m[34m4[39;49;00m>[37m [39;49;00minp,[37m[39;49;00m$
   164^I[37m^I[39;49;00m[34min[39;49;00m[37m [39;49;00m[36mfloat2[39;49;00m[37m [39;49;00muv[37m [39;49;00m:[37m [39;49;00m[90mSV_DomainLocation[39;49;00m,[37m[39;49;00m$
   165^I[37m^I[39;49;00m[34mout[39;49;00m[37m [39;49;00m[36mfloat4[39;49;00m[37m [39;49;00mo_pos[37m [39;49;00m:[37m [39;49;00m[90mSV_Position[39;49;00m)[37m[39;49;00m$
   166^I{[37m[39;49;00m$
   167^I[37m^I[39;49;00mo_pos[37m [39;49;00m=[37m [39;49;00m[36mlerp[39;49;00m([36mlerp[39;49;00m(inp[[34m0[39;49;00m].pos,[37m [39;49;00minp[[34m1[39;49;00m].pos,[37m [39;49;00muv.x),[37m [39;49;00m[36mlerp[39;49;00m(inp[[34m2[39;49;00m].pos,[37m [39;49;00minp[[34m3[39;49;00m].pos,[37m [39;49;00muv.x),[37m [39;49;00muv.y);[37m[39;49;00m$
   168^I}$
