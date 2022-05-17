     1^I[37m#[39;49;00m[37m[39;49;00m$
     2^I[37m# /etc/pacman.conf[39;49;00m[37m[39;49;00m$
     3^I[37m#[39;49;00m[37m[39;49;00m$
     4^I[37m# This example file has no relation to `pacman.ijs`[39;49;00m[37m[39;49;00m$
     5^I[37m# but is of configuration of Arch Linux's package manager `pacman`.[39;49;00m[37m[39;49;00m$
     6^I[37m#[39;49;00m[37m[39;49;00m$
     7^I[37m[39;49;00m$
     8^I[37m#[39;49;00m[37m[39;49;00m$
     9^I[37m# GENERAL OPTIONS[39;49;00m[37m[39;49;00m$
    10^I[37m#[39;49;00m[37m[39;49;00m$
    11^I[34m[options][39;49;00m[37m[39;49;00m$
    12^I[36mRootDir[39;49;00m[37m     [39;49;00m=[37m [39;49;00m/opt/local/site-private[37m[39;49;00m$
    13^I[37m#DBPath      = /var/lib/pacman/[39;49;00m[37m[39;49;00m$
    14^I[37m#CacheDir    = /var/cache/pacman/pkg/[39;49;00m[37m[39;49;00m$
    15^I[36mLogFile[39;49;00m[37m     [39;49;00m=[37m [39;49;00m/opt/local/site-private/var/log/pacman.log[37m[39;49;00m$
    16^I[37m#GPGDir      = /etc/pacman.d/gnupg/[39;49;00m[37m[39;49;00m$
    17^I[36mHoldPkg[39;49;00m[37m      [39;49;00m=[37m [39;49;00mpacman[37m[39;49;00m$
    18^I[37m#XferCommand = /usr/bin/curl -C - -f %u > %o[39;49;00m[37m[39;49;00m$
    19^I[36mXferCommand[39;49;00m[37m [39;49;00m=[37m [39;49;00m/usr/local/bin/wget[37m [39;49;00m--passive-ftp[37m [39;49;00m-c[37m [39;49;00m-O[37m [39;49;00m[31m%o[39;49;00m[37m [39;49;00m[31m%u[39;49;00m[37m[39;49;00m$
    20^I[37m#CleanMethod = KeepInstalled[39;49;00m[37m[39;49;00m$
    21^I[37m#UseDelta    = 0.7[39;49;00m[37m[39;49;00m$
    22^I[36mArchitecture[39;49;00m[37m [39;49;00m=[37m [39;49;00mauto[37m[39;49;00m$
    23^I[37m[39;49;00m$
    24^I[37m#IgnorePkg   =[39;49;00m[37m[39;49;00m$
    25^I[37m#IgnoreGroup =[39;49;00m[37m[39;49;00m$
    26^I[37m[39;49;00m$
    27^I[36mNoUpgrade[39;49;00m[37m [39;49;00m=[37m [39;49;00metc/passwd[37m [39;49;00metc/group[37m [39;49;00metc/shadow[37m[39;49;00m$
    28^I[36mNoUpgrade[39;49;00m[37m [39;49;00m=[37m [39;49;00metc/fstab[37m[39;49;00m$
    29^I[37m#NoExtract   =[39;49;00m[37m[39;49;00m$
    30^I[37m[39;49;00m$
    31^I[37m#UseSyslog[39;49;00m[37m[39;49;00m$
    32^I[36mColor[39;49;00m[37m[39;49;00m$
    33^I[37m#TotalDownload[39;49;00m[37m[39;49;00m$
    34^I[36mCheckSpace[39;49;00m[37m[39;49;00m$
    35^I[37m#VerbosePkgLists[39;49;00m[37m[39;49;00m$
    36^I[37m[39;49;00m$
    37^I[37m#SigLevel = Never[39;49;00m[37m[39;49;00m$
    38^I[36mSigLevel[39;49;00m[37m    [39;49;00m=[37m [39;49;00mRequired[37m [39;49;00mDatabaseOptional[37m[39;49;00m$
    39^I[36mLocalFileSigLevel[39;49;00m[37m [39;49;00m=[37m [39;49;00mOptional[37m[39;49;00m$
    40^I[36mRemoteFileSigLevel[39;49;00m[37m [39;49;00m=[37m [39;49;00mRequired[37m[39;49;00m$
    41^I[37m[39;49;00m$
    42^I[36mServer[39;49;00m[37m [39;49;00m=[37m [39;49;00mftp://ftp9.yaphatchpotchgen.net/[31m$repo[39;49;00m/os/[31m$arch[39;49;00m[37m[39;49;00m$
    43^I[37m[39;49;00m$
    44^I[34m[fubar32][39;49;00m[37m[39;49;00m$
    45^I[36mInclude[39;49;00m[37m [39;49;00m=[37m [39;49;00m/etc/pacman.d/mirrorlist.fubar32[37m [39;49;00m[37m# comment is allowed here[39;49;00m[37m[39;49;00m$
    46^I[37m[39;49;00m$
    47^I[37m#[custom][39;49;00m[37m[39;49;00m$
    48^I[37m#SigLevel = Optional TrustAll[39;49;00m[37m[39;49;00m$
    49^I[37m#Server = file:///home/custompkgs[39;49;00m$
