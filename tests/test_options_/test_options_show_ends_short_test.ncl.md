[34mload[39;49;00m [33m"$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"[39;49;00m$
[34mload[39;49;00m [33m"$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"[39;49;00m$
[34mload[39;49;00m [33m"$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"[39;49;00m$
[34mbegin[39;49;00m$
[34m    [39;49;00mint_num = [34m1[39;49;00m$
    float_num = [34m0.1[39;49;00m$
    str = [33m"A void map"[39;49;00m$
    array = (/[34m1[39;49;00m, [34m2[39;49;00m, [34m3[39;49;00m, [34m4[39;49;00m, [34m5[39;49;00m/)$
$
$
    wks = [36mgsn_open_wks[39;49;00m([33m"X11"[39;49;00m, [33m"test_for_pygments"[39;49;00m)$
$
    res = [34mTrue[39;49;00m$
[34m    [39;49;00mres@[36mmpMinLonF[39;49;00m = [34m9[39;49;00m[34m0.[39;49;00m$
    res@[36mmpMaxLonF[39;49;00m = [34m18[39;49;00m[34m0.[39;49;00m$
    res@[36mmpMinLatF[39;49;00m = [34m0.[39;49;00m$
    res@[36mmpMaxLatF[39;49;00m = [34m9[39;49;00m[34m0.[39;49;00m$
$
    plot = [36mgsn_csm_map_ce[39;49;00m(wks, res)$
[34mend[39;49;00m$
