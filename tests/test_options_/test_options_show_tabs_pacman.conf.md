[37m#[39;49;00m[37m[39;49;00m
[37m# /etc/pacman.conf[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# This example file has no relation to `pacman.ijs`[39;49;00m[37m[39;49;00m
[37m# but is of configuration of Arch Linux's package manager `pacman`.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# GENERAL OPTIONS[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[34m[options][39;49;00m[37m[39;49;00m
[36mRootDir[39;49;00m[37m     [39;49;00m=[37m [39;49;00m/opt/local/site-private[37m[39;49;00m
[37m#DBPath      = /var/lib/pacman/[39;49;00m[37m[39;49;00m
[37m#CacheDir    = /var/cache/pacman/pkg/[39;49;00m[37m[39;49;00m
[36mLogFile[39;49;00m[37m     [39;49;00m=[37m [39;49;00m/opt/local/site-private/var/log/pacman.log[37m[39;49;00m
[37m#GPGDir      = /etc/pacman.d/gnupg/[39;49;00m[37m[39;49;00m
[36mHoldPkg[39;49;00m[37m      [39;49;00m=[37m [39;49;00mpacman[37m[39;49;00m
[37m#XferCommand = /usr/bin/curl -C - -f %u > %o[39;49;00m[37m[39;49;00m
[36mXferCommand[39;49;00m[37m [39;49;00m=[37m [39;49;00m/usr/local/bin/wget[37m [39;49;00m--passive-ftp[37m [39;49;00m-c[37m [39;49;00m-O[37m [39;49;00m[31m%o[39;49;00m[37m [39;49;00m[31m%u[39;49;00m[37m[39;49;00m
[37m#CleanMethod = KeepInstalled[39;49;00m[37m[39;49;00m
[37m#UseDelta    = 0.7[39;49;00m[37m[39;49;00m
[36mArchitecture[39;49;00m[37m [39;49;00m=[37m [39;49;00mauto[37m[39;49;00m
[37m[39;49;00m
[37m#IgnorePkg   =[39;49;00m[37m[39;49;00m
[37m#IgnoreGroup =[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36mNoUpgrade[39;49;00m[37m [39;49;00m=[37m [39;49;00metc/passwd[37m [39;49;00metc/group[37m [39;49;00metc/shadow[37m[39;49;00m
[36mNoUpgrade[39;49;00m[37m [39;49;00m=[37m [39;49;00metc/fstab[37m[39;49;00m
[37m#NoExtract   =[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m#UseSyslog[39;49;00m[37m[39;49;00m
[36mColor[39;49;00m[37m[39;49;00m
[37m#TotalDownload[39;49;00m[37m[39;49;00m
[36mCheckSpace[39;49;00m[37m[39;49;00m
[37m#VerbosePkgLists[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m#SigLevel = Never[39;49;00m[37m[39;49;00m
[36mSigLevel[39;49;00m[37m    [39;49;00m=[37m [39;49;00mRequired[37m [39;49;00mDatabaseOptional[37m[39;49;00m
[36mLocalFileSigLevel[39;49;00m[37m [39;49;00m=[37m [39;49;00mOptional[37m[39;49;00m
[36mRemoteFileSigLevel[39;49;00m[37m [39;49;00m=[37m [39;49;00mRequired[37m[39;49;00m
[37m[39;49;00m
[36mServer[39;49;00m[37m [39;49;00m=[37m [39;49;00mftp://ftp9.yaphatchpotchgen.net/[31m$repo[39;49;00m/os/[31m$arch[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34m[fubar32][39;49;00m[37m[39;49;00m
[36mInclude[39;49;00m[37m [39;49;00m=[37m [39;49;00m/etc/pacman.d/mirrorlist.fubar32[37m [39;49;00m[37m# comment is allowed here[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m#[custom][39;49;00m[37m[39;49;00m
[37m#SigLevel = Optional TrustAll[39;49;00m[37m[39;49;00m
[37m#Server = file:///home/custompkgs[39;49;00m
