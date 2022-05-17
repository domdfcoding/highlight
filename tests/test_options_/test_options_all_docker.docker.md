     1^I[34mFROM[39;49;00m[37m [39;49;00m[33malpine:3.5[39;49;00m$
     2^I[34mMAINTAINER[39;49;00m[37m [39;49;00m[33mFirst O'Last[39;49;00m$
     3^I$
     4^I[37m# comment[39;49;00m$
     5^I[34mrun[39;49;00m[37m [39;49;00m[36mecho[39;49;00m [33m\[39;49;00m$
     6^I  [34m123[39;49;00m [31m$bar[39;49;00m$
     7^I[34mRUN[39;49;00m[37m [39;49;00mapk --update add rsync dumb-init$
     8^I$
     9^I[37m# Test env with both syntax[39;49;00m$
    10^I[34mENV[39;49;00m[37m [39;49;00m[31mFOO[39;49;00m = [33m"BAR"[39;49;00m$
    11^I[34mENV[39;49;00m[37m [39;49;00mFOO [33m\[39;49;00m$
    12^I^I[33m"BAR"[39;49;00m$
    13^I$
    14^I[34mCOPY[39;49;00m[37m [39;49;00mfoo [33m"bar"[39;49;00m$
    15^I[34mCOPY[39;49;00m[37m [39;49;00mfoo [33m\[39;49;00m$
    16^I^I[33m"bar"[39;49;00m$
    17^I$
    18^I[34mHEALTHCHECK[39;49;00m[37m [39;49;00m[33m\[39;49;00m$
    19^I    --interval=5m --timeout=3s [33m\[39;49;00m$
    20^I    [34mCMD[39;49;00m[37m [39;49;00mcurl -f http://localhost/ || [36mexit[39;49;00m [34m1[39;49;00m$
    21^I$
    22^I[37m# ONBUILD keyword, then with linebreak[39;49;00m$
    23^I[34mONBUILD[39;49;00m[37m [39;49;00m[34mADD[39;49;00m[37m [39;49;00m. /app/src$
    24^I[34mONBUILD[39;49;00m[37m [39;49;00m[33m\[39;49;00m$
    25^I^I[34mRUN[39;49;00m[37m [39;49;00m[36mecho[39;49;00m [34m123[39;49;00m [31m$bar[39;49;00m$
    26^I$
    27^I[37m# Potential JSON array parsing, mixed with linebreaks[39;49;00m$
    28^I[34mVOLUME[39;49;00m[37m [39;49;00m[33m\[39;49;00m$
    29^I    /foo$
    30^I[34mVOLUME[39;49;00m[37m [39;49;00m[33m\[39;49;00m$
    31^I    [[33m"/bar"[39;49;00m]$
    32^I[34mVOLUME[39;49;00m[37m [39;49;00m[[33m"/bar"[39;49;00m]$
    33^I[34mVOLUME[39;49;00m[37m [39;49;00m[33m/foo[39;49;00m$
    34^I[34mCMD[39;49;00m[37m [39;49;00m[[33m"foo"[39;49;00m,[37m [39;49;00m[33m"bar"[39;49;00m]$
