[36mmodule[39;49;00m:[37m [39;49;00m[33mnanomsg[39;49;00m[37m[39;49;00m$
[36msynopsis[39;49;00m:[37m [39;49;00m[33mgenerated bindings for the nanomsg library[39;49;00m[37m[39;49;00m$
[36mauthor[39;49;00m:[37m [39;49;00m[33mBruce Mitchener, Jr.[39;49;00m[37m[39;49;00m$
[36mcopyright[39;49;00m:[37m [39;49;00m[33mSee LICENSE file in this distribution.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[34mdefine[39;49;00m[37m [39;49;00msimple-C-mapped-subtype[37m [39;49;00m[04m[32m<C-buffer-offset>[39;49;00m[37m [39;49;00m([04m[32m<C-char*>[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00mexport-map[37m [39;49;00m[04m[32m<machine-word>[39;49;00m,[37m [39;49;00m[34mexport-function:[39;49;00m[37m [39;49;00m[36midentity[39;49;00m;[37m[39;49;00m$
[34mend[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[34mdefine[39;49;00m[37m [39;49;00m[36minterface[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[34m#include[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/sp.h[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/fanin.h[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/inproc.h[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/pair.h[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/reqrep.h[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/survey.h[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/fanout.h[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/ipc.h[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/pubsub.h[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp/tcp.h[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m},[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mexclude:[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33mSP_HAUSNUMERO[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33mSP_PAIR_ID[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33mSP_PUBSUB_ID[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33mSP_REQREP_ID[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33mSP_FANIN_ID[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33mSP_FANOUT_ID[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33mSP_SURVEY_ID[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m},[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mequate:[39;49;00m[37m [39;49;00m{[33m"[39;49;00m[33mchar *[39;49;00m[33m"[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[04m[32m<c-string>[39;49;00m},[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mrename:[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp_recv[39;49;00m[33m"[39;49;00m[37m [39;49;00m=>[37m [39;49;00m%sp-recv,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp_send[39;49;00m[33m"[39;49;00m[37m [39;49;00m=>[37m [39;49;00m%sp-send,[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33msp_setsockopt[39;49;00m[33m"[39;49;00m[37m [39;49;00m=>[37m [39;49;00m%sp-setsockopt[37m[39;49;00m$
[37m    [39;49;00m};[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36mfunction[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33msp_version[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[34moutput-argument:[39;49;00m[37m [39;49;00m[34m1[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[34moutput-argument:[39;49;00m[37m [39;49;00m[34m2[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[34moutput-argument:[39;49;00m[37m [39;49;00m[34m3[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36mfunction[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33msp_send[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[34mmap-argument:[39;49;00m[37m [39;49;00m{[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[04m[32m<C-buffer-offset>[39;49;00m[37m [39;49;00m};[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36mfunction[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33msp_recv[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m      [39;49;00m[34mmap-argument:[39;49;00m[37m [39;49;00m{[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[04m[32m<C-buffer-offset>[39;49;00m[37m [39;49;00m};[37m[39;49;00m$
[37m[39;49;00m$
[34mend[39;49;00m[37m [39;49;00m[36minterface[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m// Function for adding the base address of the repeated slots of a <buffer>[39;49;00m[37m[39;49;00m$
[37m// to an offset and returning the result as a <machine-word>.  This is[39;49;00m[37m[39;49;00m$
[37m// necessary for passing <buffer> contents across the FFI.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[34mdefine[39;49;00m[37m [39;49;00m[36mfunction[39;49;00m[37m [39;49;00mbuffer-offset[37m[39;49;00m$
[37m    [39;49;00m(the-buffer[37m [39;49;00m::[37m [39;49;00m[04m[32m<buffer>[39;49;00m,[37m [39;49;00mdata-offset[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m)[37m[39;49;00m$
[37m [39;49;00m=>[37m [39;49;00m(result-offset[37m [39;49;00m::[37m [39;49;00m[04m[32m<machine-word>[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00mu%+(data-offset,[37m[39;49;00m$
[37m      [39;49;00mprimitive-wrap-machine-word[37m[39;49;00m$
[37m        [39;49;00m(primitive-repeated-slot-as-raw[37m[39;49;00m$
[37m           [39;49;00m(the-buffer,[37m [39;49;00mprimitive-repeated-slot-offset(the-buffer))))[37m[39;49;00m$
[34mend[39;49;00m[37m [39;49;00m[36mfunction[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[34mdefine[39;49;00m[37m [39;49;00m[36minline[39;49;00m[37m [39;49;00m[36mfunction[39;49;00m[37m [39;49;00msp-send[37m [39;49;00m(socket[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m,[37m [39;49;00mdata[37m [39;49;00m::[37m [39;49;00m[04m[32m<buffer>[39;49;00m,[37m [39;49;00mflags[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m)[37m [39;49;00m=>[37m [39;49;00m(res[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m%sp-send(socket,[37m [39;49;00mbuffer-offset(data,[37m [39;49;00m[34m0[39;49;00m),[37m [39;49;00mdata.[36msize[39;49;00m,[37m [39;49;00mflags)[37m[39;49;00m$
[34mend[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[34mdefine[39;49;00m[37m [39;49;00m[36minline[39;49;00m[37m [39;49;00m[36mfunction[39;49;00m[37m [39;49;00msp-recv[37m [39;49;00m(socket[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m,[37m [39;49;00mdata[37m [39;49;00m::[37m [39;49;00m[04m[32m<buffer>[39;49;00m,[37m [39;49;00mflags[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m)[37m [39;49;00m=>[37m [39;49;00m(res[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m%sp-recv(socket,[37m [39;49;00mbuffer-offset(data,[37m [39;49;00m[34m0[39;49;00m),[37m [39;49;00mdata.[36msize[39;49;00m,[37m [39;49;00mflags);[37m[39;49;00m$
[34mend[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[34mdefine[39;49;00m[37m [39;49;00m[36minline[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m[37m [39;49;00msp-setsockopt[37m [39;49;00m(socket[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m,[37m [39;49;00mlevel[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m,[37m [39;49;00moption[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m,[37m [39;49;00mvalue[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00mwith-stack-structure[37m [39;49;00m(int[37m [39;49;00m::[37m [39;49;00m[04m[32m<C-int*>[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00mpointer-value(int)[37m [39;49;00m:=[37m [39;49;00mvalue;[37m[39;49;00m$
[37m    [39;49;00m[34mlet[39;49;00m[37m [39;49;00msetsockopt-result[37m [39;49;00m=[37m[39;49;00m$
[37m      [39;49;00m%sp-setsockopt(socket,[37m [39;49;00mlevel,[37m [39;49;00moption,[37m [39;49;00mint,[37m [39;49;00msize-of([04m[32m<C-int*>[39;49;00m));[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(setsockopt-result[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[37m// Check error![39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[34mend[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00msetsockopt-result[37m[39;49;00m$
[37m  [39;49;00m[34mend[39;49;00m;[37m[39;49;00m$
[34mend[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[34mdefine[39;49;00m[37m [39;49;00m[36minline[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m[37m [39;49;00msp-setsockopt[37m [39;49;00m(socket[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m,[37m [39;49;00mlevel[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m,[37m [39;49;00moption[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m,[37m [39;49;00mdata[37m [39;49;00m::[37m [39;49;00m[04m[32m<byte-string>[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[34mlet[39;49;00m[37m [39;49;00msetsockopt-result[37m [39;49;00m=[37m[39;49;00m$
[37m    [39;49;00m%sp-setsockopt(socket,[37m [39;49;00mlevel,[37m [39;49;00moption,[37m [39;49;00m[36mas[39;49;00m([04m[32m<c-string>[39;49;00m,[37m [39;49;00mdata),[37m [39;49;00mdata.[36msize[39;49;00m);[37m[39;49;00m$
[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(setsockopt-result[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[37m// Check error![39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[34mend[39;49;00m;[37m[39;49;00m$
[37m  [39;49;00msetsockopt-result[37m[39;49;00m$
[34mend[39;49;00m;$
