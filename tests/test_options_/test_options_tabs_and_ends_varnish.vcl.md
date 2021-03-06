[37m# This is the VCL configuration Varnish will automatically append to your VCL[39;49;00m$
[37m# file during compilation/loading. See the vcl(7) man page for details on syntax[39;49;00m$
[37m# and semantics.[39;49;00m$
[37m# New users is recommended to use the example.vcl file as a starting point.[39;49;00m$
$
[34mvcl [39;49;00m[31m4.0[39;49;00m;$
$
[34mbackend[39;49;00m[31m foo[39;49;00m { [36m.host[39;49;00m = [33m"[39;49;00m[33m192.168.1.1[39;49;00m[33m"[39;49;00m; }$
$
[34mprobe [39;49;00m[31mblatti [39;49;00m{ [36m.url[39;49;00m = [33m"[39;49;00m[33mfoo[39;49;00m[33m"[39;49;00m; }$
[34mprobe [39;49;00m[31mfooy [39;49;00m{$
^I[36m.url[39;49;00m = [33m"[39;49;00m[33mbeh[39;49;00m[33m"[39;49;00m;$
$
}$
$
[34macl [39;49;00m[31mfoo [39;49;00m{$
^I[33m"[39;49;00m[33m192.168.1.1[39;49;00m[33m"[39;49;00m;$
^I[33m"[39;49;00m[33m192.168.0.0[39;49;00m[33m"[39;49;00m/[34m24[39;49;00m;$
^I! [33m"[39;49;00m[33m192.168.0.1[39;49;00m[33m"[39;49;00m;$
}$
$
[34minclude[39;49;00m [33m"[39;49;00m[33mfoo.vcl[39;49;00m[33m"[39;49;00m;$
$
[34mimport[39;49;00m std;$
$
[34msub [39;49;00m[32mvcl_init[39;49;00m {$
^I[34mnew[39;49;00m b = [32mdirector[39;49;00m.[32mfoo[39;49;00m();$
}$
$
[34msub [39;49;00m[32mvcl_recv[39;49;00m {$
^I[34mban[39;49;00m([31mreq.url[39;49;00m ~ [33m"[39;49;00m[33mfoo[39;49;00m[33m"[39;49;00m);$
^I[34mrollback[39;49;00m();$
}$
[34msub [39;49;00m[32mvcl_recv[39;49;00m {$
    [34mif[39;49;00m ([31mreq.method[39;49;00m == [33m"[39;49;00m[33mPRI[39;49;00m[33m"[39;49;00m) {$
^I[37m/*[39;49;00m[37m We do not support SPDY or HTTP[39;49;00m[37m/[39;49;00m[37m2.0 [39;49;00m[37m*/[39;49;00m$
^I[34mreturn[39;49;00m ([31msynth[39;49;00m([34m405[39;49;00m));$
    }$
    [34mif[39;49;00m ([31mreq.method[39;49;00m != [33m"[39;49;00m[33mGET[39;49;00m[33m"[39;49;00m &&$
      [31mreq.method[39;49;00m != [33m"[39;49;00m[33mHEAD[39;49;00m[33m"[39;49;00m &&$
      [31mreq.method[39;49;00m != [33m"[39;49;00m[33mPUT[39;49;00m[33m"[39;49;00m &&$
      [31mreq.method[39;49;00m != [33m"[39;49;00m[33mPOST[39;49;00m[33m"[39;49;00m &&$
      [31mreq.method[39;49;00m != [33m"[39;49;00m[33mTRACE[39;49;00m[33m"[39;49;00m &&$
      [31mreq.method[39;49;00m != [33m"[39;49;00m[33mOPTIONS[39;49;00m[33m"[39;49;00m &&$
      [31mreq.method[39;49;00m != [33m"[39;49;00m[33mDELETE[39;49;00m[33m"[39;49;00m) {$
        [37m/*[39;49;00m[37m Non-RFC2616 or CONNECT which is weird. [39;49;00m[37m*/[39;49;00m$
        [34mreturn[39;49;00m ([31mpipe[39;49;00m);$
    }$
$
    [34mif[39;49;00m ([31mreq.method[39;49;00m != [33m"[39;49;00m[33mGET[39;49;00m[33m"[39;49;00m && [31mreq.method[39;49;00m != [33m"[39;49;00m[33mHEAD[39;49;00m[33m"[39;49;00m) {$
        [37m/*[39;49;00m[37m We only deal with GET and HEAD by default [39;49;00m[37m*/[39;49;00m$
        [34mreturn[39;49;00m ([31mpass[39;49;00m);$
    }$
    [34mif[39;49;00m ([31mreq.http.Authorization[39;49;00m || [31mreq.http.Cookie[39;49;00m) {$
        [37m/*[39;49;00m[37m Not cacheable by default [39;49;00m[37m*/[39;49;00m$
        [34mreturn[39;49;00m ([31mpass[39;49;00m);$
    }$
    [34mreturn[39;49;00m ([31mhash[39;49;00m);$
}$
$
[34msub [39;49;00m[32mvcl_pipe[39;49;00m {$
    [37m# By default Connection: close is set on all piped requests, to stop[39;49;00m$
    [37m# connection reuse from sending future requests directly to the[39;49;00m$
    [37m# (potentially) wrong backend. If you do want this to happen, you can undo[39;49;00m$
    [37m# it here.[39;49;00m$
    [37m# unset bereq.http.connection;[39;49;00m$
    [34mreturn[39;49;00m ([31mpipe[39;49;00m);$
}$
$
[34msub [39;49;00m[32mvcl_pass[39;49;00m {$
    [34mreturn[39;49;00m ([31mfetch[39;49;00m);$
}$
$
[34msub [39;49;00m[32mvcl_hash[39;49;00m {$
    [34mhash_data[39;49;00m([31mreq.url[39;49;00m);$
    [34mif[39;49;00m ([31mreq.http.host[39;49;00m) {$
        [34mhash_data[39;49;00m([31mreq.http.host[39;49;00m);$
    } [34melse[39;49;00m {$
        [34mhash_data[39;49;00m([31mserver.ip[39;49;00m);$
    }$
    [34mreturn[39;49;00m ([31mlookup[39;49;00m);$
}$
$
[34msub [39;49;00m[32mvcl_purge[39;49;00m {$
    [34mreturn[39;49;00m ([31msynth[39;49;00m([34m200[39;49;00m, [33m"[39;49;00m[33mPurged[39;49;00m[33m"[39;49;00m));$
}$
$
[34msub [39;49;00m[32mvcl_hit[39;49;00m {$
    [34mif[39;49;00m ([31mobj.ttl[39;49;00m >= 0s) {$
        [37m// A pure unadultered hit, deliver it[39;49;00m$
        [34mreturn[39;49;00m ([31mdeliver[39;49;00m);$
    }$
    [34mif[39;49;00m ([31mobj.ttl[39;49;00m + [31mobj.grace[39;49;00m > 0s) {$
        [37m// Object is in grace, deliver it[39;49;00m$
        [37m// Automatically triggers a background fetch[39;49;00m$
        [34mreturn[39;49;00m ([31mdeliver[39;49;00m);$
    }$
    [37m// fetch & deliver once we get the result[39;49;00m$
    [34mreturn[39;49;00m ([31mmiss[39;49;00m);$
}$
$
[34msub [39;49;00m[32mvcl_miss[39;49;00m {$
    [34mreturn[39;49;00m ([31mfetch[39;49;00m);$
}$
$
[34msub [39;49;00m[32mvcl_deliver[39;49;00m {$
    [34mset[39;49;00m [31mresp.http.x-storage[39;49;00m = [31mstorage.s0.free[39;49;00m;$
    [34mreturn[39;49;00m ([31mdeliver[39;49;00m);$
}$
$
[37m/*[39;49;00m[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m We can come here "invisibly" with the following errors: 413, 417 & 503[39;49;00m$
[37m [39;49;00m[37m*/[39;49;00m$
[34msub [39;49;00m[32mvcl_synth[39;49;00m {$
    [34mset[39;49;00m [31mresp.http.Content-Type[39;49;00m = [33m"[39;49;00m[33mtext/html; charset=utf-8[39;49;00m[33m"[39;49;00m;$
    [34mset[39;49;00m [31mresp.http.Retry-After[39;49;00m = [33m"[39;49;00m[33m5[39;49;00m[33m"[39;49;00m;$
    [34msynthetic[39;49;00m( [33m{"[39;49;00m[33m<[39;49;00m[33m![39;49;00m[33mD[39;49;00m[33mO[39;49;00m[33mC[39;49;00m[33mT[39;49;00m[33mY[39;49;00m[33mP[39;49;00m[33mE[39;49;00m[33m [39;49;00m[33mh[39;49;00m[33mt[39;49;00m[33mm[39;49;00m[33ml[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m<[39;49;00m[33mh[39;49;00m[33mt[39;49;00m[33mm[39;49;00m[33ml[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mh[39;49;00m[33me[39;49;00m[33ma[39;49;00m[33md[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mt[39;49;00m[33mi[39;49;00m[33mt[39;49;00m[33ml[39;49;00m[33me[39;49;00m[33m>[39;49;00m[33m"}[39;49;00m + [31mresp.status[39;49;00m + [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m + [31mresp.reason[39;49;00m + [33m{"[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mt[39;49;00m[33mi[39;49;00m[33mt[39;49;00m[33ml[39;49;00m[33me[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mh[39;49;00m[33me[39;49;00m[33ma[39;49;00m[33md[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mb[39;49;00m[33mo[39;49;00m[33md[39;49;00m[33my[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mh[39;49;00m[33m1[39;49;00m[33m>[39;49;00m[33mE[39;49;00m[33mr[39;49;00m[33mr[39;49;00m[33mo[39;49;00m[33mr[39;49;00m[33m [39;49;00m[33m"}[39;49;00m + [31mresp.status[39;49;00m + [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m + [31mresp.reason[39;49;00m + [33m{"[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mh[39;49;00m[33m1[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33m"}[39;49;00m + [31mresp.reason[39;49;00m + [33m{"[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mh[39;49;00m[33m3[39;49;00m[33m>[39;49;00m[33mG[39;49;00m[33mu[39;49;00m[33mr[39;49;00m[33mu[39;49;00m[33m [39;49;00m[33mM[39;49;00m[33me[39;49;00m[33md[39;49;00m[33mi[39;49;00m[33mt[39;49;00m[33ma[39;49;00m[33mt[39;49;00m[33mi[39;49;00m[33mo[39;49;00m[33mn[39;49;00m[33m:[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mh[39;49;00m[33m3[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33mX[39;49;00m[33mI[39;49;00m[33mD[39;49;00m[33m:[39;49;00m[33m [39;49;00m[33m"}[39;49;00m + [31mreq.xid[39;49;00m + [33m{"[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mh[39;49;00m[33mr[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33mV[39;49;00m[33ma[39;49;00m[33mr[39;49;00m[33mn[39;49;00m[33mi[39;49;00m[33ms[39;49;00m[33mh[39;49;00m[33m [39;49;00m[33mc[39;49;00m[33ma[39;49;00m[33mc[39;49;00m[33mh[39;49;00m[33me[39;49;00m[33m [39;49;00m[33ms[39;49;00m[33me[39;49;00m[33mr[39;49;00m[33mv[39;49;00m[33me[39;49;00m[33mr[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mb[39;49;00m[33mo[39;49;00m[33md[39;49;00m[33my[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m<[39;49;00m[33m/[39;49;00m[33mh[39;49;00m[33mt[39;49;00m[33mm[39;49;00m[33ml[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m"}[39;49;00m );$
    [34mreturn[39;49;00m ([31mdeliver[39;49;00m);$
}$
$
[37m#######################################################################[39;49;00m$
[37m# Backend Fetch[39;49;00m$
$
[34msub [39;49;00m[32mvcl_backend_fetch[39;49;00m {$
    [34mreturn[39;49;00m ([31mfetch[39;49;00m);$
}$
$
[34msub [39;49;00m[32mvcl_backend_response[39;49;00m {$
    [34mif[39;49;00m ([31mberesp.ttl[39;49;00m <= 0s ||$
      [31mberesp.http.Set-Cookie[39;49;00m ||$
      [31mberesp.http.Surrogate-control[39;49;00m ~ [33m"[39;49;00m[33mno-store[39;49;00m[33m"[39;49;00m ||$
      (![31mberesp.http.Surrogate-Control[39;49;00m &&$
        [31mberesp.http.Cache-Control[39;49;00m ~ [33m"[39;49;00m[33mno-cache|no-store|private[39;49;00m[33m"[39;49;00m) ||$
      [31mberesp.http.Vary[39;49;00m == [33m"[39;49;00m[33m*[39;49;00m[33m"[39;49;00m) {$
        [37m/*[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m[37m*[39;49;00m[37m Mark as "Hit-For-Pass" for the next 2 minutes[39;49;00m$
[37m        [39;49;00m[37m*/[39;49;00m$
        [34mset[39;49;00m [31mberesp.ttl[39;49;00m = 120s;$
        [34mset[39;49;00m [31mberesp.uncacheable[39;49;00m = [36mtrue[39;49;00m;$
    }$
    [34mreturn[39;49;00m ([31mdeliver[39;49;00m);$
}$
$
[34msub [39;49;00m[32mvcl_backend_error[39;49;00m {$
    [34mset[39;49;00m [31mberesp.http.Content-Type[39;49;00m = [33m"[39;49;00m[33mtext/html; charset=utf-8[39;49;00m[33m"[39;49;00m;$
    [34mset[39;49;00m [31mberesp.http.Retry-After[39;49;00m = [33m"[39;49;00m[33m5[39;49;00m[33m"[39;49;00m;$
    [34msynthetic[39;49;00m( [33m{"[39;49;00m[33m<[39;49;00m[33m![39;49;00m[33mD[39;49;00m[33mO[39;49;00m[33mC[39;49;00m[33mT[39;49;00m[33mY[39;49;00m[33mP[39;49;00m[33mE[39;49;00m[33m [39;49;00m[33mh[39;49;00m[33mt[39;49;00m[33mm[39;49;00m[33ml[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m<[39;49;00m[33mh[39;49;00m[33mt[39;49;00m[33mm[39;49;00m[33ml[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mh[39;49;00m[33me[39;49;00m[33ma[39;49;00m[33md[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mt[39;49;00m[33mi[39;49;00m[33mt[39;49;00m[33ml[39;49;00m[33me[39;49;00m[33m>[39;49;00m[33m"}[39;49;00m + [31mberesp.status[39;49;00m + [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m + [31mberesp.reason[39;49;00m + [33m{"[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mt[39;49;00m[33mi[39;49;00m[33mt[39;49;00m[33ml[39;49;00m[33me[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mh[39;49;00m[33me[39;49;00m[33ma[39;49;00m[33md[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mb[39;49;00m[33mo[39;49;00m[33md[39;49;00m[33my[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mh[39;49;00m[33m1[39;49;00m[33m>[39;49;00m[33mE[39;49;00m[33mr[39;49;00m[33mr[39;49;00m[33mo[39;49;00m[33mr[39;49;00m[33m [39;49;00m[33m"}[39;49;00m + [31mberesp.status[39;49;00m + [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m + [31mberesp.reason[39;49;00m + [33m{"[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mh[39;49;00m[33m1[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33m"}[39;49;00m + [31mberesp.reason[39;49;00m + [33m{"[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mh[39;49;00m[33m3[39;49;00m[33m>[39;49;00m[33mG[39;49;00m[33mu[39;49;00m[33mr[39;49;00m[33mu[39;49;00m[33m [39;49;00m[33mM[39;49;00m[33me[39;49;00m[33md[39;49;00m[33mi[39;49;00m[33mt[39;49;00m[33ma[39;49;00m[33mt[39;49;00m[33mi[39;49;00m[33mo[39;49;00m[33mn[39;49;00m[33m:[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mh[39;49;00m[33m3[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33mX[39;49;00m[33mI[39;49;00m[33mD[39;49;00m[33m:[39;49;00m[33m [39;49;00m[33m"}[39;49;00m + [31mbereq.xid[39;49;00m + [33m{"[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mh[39;49;00m[33mr[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33mV[39;49;00m[33ma[39;49;00m[33mr[39;49;00m[33mn[39;49;00m[33mi[39;49;00m[33ms[39;49;00m[33mh[39;49;00m[33m [39;49;00m[33mc[39;49;00m[33ma[39;49;00m[33mc[39;49;00m[33mh[39;49;00m[33me[39;49;00m[33m [39;49;00m[33ms[39;49;00m[33me[39;49;00m[33mr[39;49;00m[33mv[39;49;00m[33me[39;49;00m[33mr[39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mp[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m [39;49;00m[33m [39;49;00m[33m<[39;49;00m[33m/[39;49;00m[33mb[39;49;00m[33mo[39;49;00m[33md[39;49;00m[33my[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m<[39;49;00m[33m/[39;49;00m[33mh[39;49;00m[33mt[39;49;00m[33mm[39;49;00m[33ml[39;49;00m[33m>[39;49;00m[33m[39;49;00m$
[33m"}[39;49;00m );$
    [34mreturn[39;49;00m ([31mdeliver[39;49;00m);$
}$
$
[37m#######################################################################[39;49;00m$
[37m# Housekeeping[39;49;00m$
$
[34msub [39;49;00m[32mvcl_init[39;49;00m {$
}$
$
[34msub [39;49;00m[32mvcl_fini[39;49;00m {$
    [34mreturn[39;49;00m ([31mok[39;49;00m);$
}$
