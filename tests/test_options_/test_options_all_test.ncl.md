     1^I[34mload[39;49;00m [33m"$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"[39;49;00m$
     2^I[34mload[39;49;00m [33m"$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"[39;49;00m$
     3^I[34mload[39;49;00m [33m"$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"[39;49;00m$
     4^I[34mbegin[39;49;00m$
     5^I[34m    [39;49;00mint_num = [34m1[39;49;00m$
     6^I    float_num = [34m0.1[39;49;00m$
     7^I    str = [33m"A void map"[39;49;00m$
     8^I    array = (/[34m1[39;49;00m, [34m2[39;49;00m, [34m3[39;49;00m, [34m4[39;49;00m, [34m5[39;49;00m/)$
     9^I$
    10^I$
    11^I    wks = [36mgsn_open_wks[39;49;00m([33m"X11"[39;49;00m, [33m"test_for_pygments"[39;49;00m)$
    12^I$
    13^I    res = [34mTrue[39;49;00m$
    14^I[34m    [39;49;00mres@[36mmpMinLonF[39;49;00m = [34m9[39;49;00m[34m0.[39;49;00m$
    15^I    res@[36mmpMaxLonF[39;49;00m = [34m18[39;49;00m[34m0.[39;49;00m$
    16^I    res@[36mmpMinLatF[39;49;00m = [34m0.[39;49;00m$
    17^I    res@[36mmpMaxLatF[39;49;00m = [34m9[39;49;00m[34m0.[39;49;00m$
    18^I$
    19^I    plot = [36mgsn_csm_map_ce[39;49;00m(wks, res)$
    20^I[34mend[39;49;00m$
