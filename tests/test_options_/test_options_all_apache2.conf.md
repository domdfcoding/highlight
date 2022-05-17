     1^I[37m# Based upon the NCSA server configuration files originally by Rob McCool.[39;49;00m[37m[39;49;00m$
     2^I[37m# Changed extensively for the Debian package by Daniel Stone <daniel@sfarc.net>[39;49;00m[37m[39;49;00m$
     3^I[37m# and also by Thom May <thom@debian.org>.[39;49;00m[37m[39;49;00m$
     4^I[37m[39;49;00m$
     5^I[37m# ServerRoot: The top of the directory tree under which the server's[39;49;00m[37m[39;49;00m$
     6^I[37m# configuration, error, and log files are kept.[39;49;00m[37m[39;49;00m$
     7^I[37m#[39;49;00m[37m[39;49;00m$
     8^I[37m# NOTE!  If you intend to place this on an NFS (or otherwise network)[39;49;00m[37m[39;49;00m$
     9^I[37m# mounted filesystem then please read the LockFile documentation[39;49;00m[37m[39;49;00m$
    10^I[37m# (available at <URL:http://www.apache.org/docs/mod/core.html#lockfile>);[39;49;00m[37m[39;49;00m$
    11^I[37m# you will save yourself a lot of trouble.[39;49;00m[37m[39;49;00m$
    12^I[37m[39;49;00m$
    13^I[36mServerRoot[39;49;00m[37m [39;49;00m[33m"/etc/apache2"[39;49;00m[37m[39;49;00m$
    14^I[37m[39;49;00m$
    15^I[37m# The LockFile directive sets the path to the lockfile used when Apache[39;49;00m[37m[39;49;00m$
    16^I[37m# is compiled with either USE_FCNTL_SERIALIZED_ACCEPT or[39;49;00m[37m[39;49;00m$
    17^I[37m# USE_FLOCK_SERIALIZED_ACCEPT. This directive should normally be left at[39;49;00m[37m[39;49;00m$
    18^I[37m# its default value. The main reason for changing it is if the logs[39;49;00m[37m[39;49;00m$
    19^I[37m# directory is NFS mounted, since the lockfile MUST BE STORED ON A LOCAL[39;49;00m[37m[39;49;00m$
    20^I[37m# DISK. The PID of the main server process is automatically appended to[39;49;00m[37m[39;49;00m$
    21^I[37m# the filename. [39;49;00m[37m[39;49;00m$
    22^I[37m[39;49;00m$
    23^I[36mLockFile[39;49;00m[37m [39;49;00m[33m/var/lock/apache2/accept.lock[39;49;00m[37m[39;49;00m$
    24^I[37m[39;49;00m$
    25^I[37m# PidFile: The file in which the server should record its process[39;49;00m[37m[39;49;00m$
    26^I[37m# identification number when it starts.[39;49;00m[37m[39;49;00m$
    27^I[37m[39;49;00m$
    28^I[36mPidFile[39;49;00m[37m [39;49;00m[33m/var/run/apache2.pid[39;49;00m[37m[39;49;00m$
    29^I[37m[39;49;00m$
    30^I[37m# Timeout: The number of seconds before receives and sends time out.[39;49;00m[37m[39;49;00m$
    31^I[37m[39;49;00m$
    32^I[36mTimeout[39;49;00m[37m [39;49;00m[34m300[39;49;00m[37m[39;49;00m$
    33^I[37m[39;49;00m$
    34^I[37m# KeepAlive: Whether or not to allow persistent connections (more than[39;49;00m[37m[39;49;00m$
    35^I[37m# one request per connection). Set to "Off" to deactivate.[39;49;00m[37m[39;49;00m$
    36^I[37m[39;49;00m$
    37^I[36mKeepAlive[39;49;00m[37m [39;49;00m[34mOn[39;49;00m[37m[39;49;00m$
    38^I[37m[39;49;00m$
    39^I[37m# MaxKeepAliveRequests: The maximum number of requests to allow[39;49;00m[37m[39;49;00m$
    40^I[37m# during a persistent connection. Set to 0 to allow an unlimited amount.[39;49;00m[37m[39;49;00m$
    41^I[37m# We recommend you leave this number high, for maximum performance.[39;49;00m[37m[39;49;00m$
    42^I[37m[39;49;00m$
    43^I[36mMaxKeepAliveRequests[39;49;00m[37m [39;49;00m[34m100[39;49;00m[37m[39;49;00m$
    44^I[37m[39;49;00m$
    45^I[37m# KeepAliveTimeout: Number of seconds to wait for the next request from the[39;49;00m[37m[39;49;00m$
    46^I[37m# same client on the same connection.[39;49;00m[37m[39;49;00m$
    47^I[37m[39;49;00m$
    48^I[36mKeepAliveTimeout[39;49;00m[37m [39;49;00m[34m15[39;49;00m[37m[39;49;00m$
    49^I[37m[39;49;00m$
    50^I[37m##[39;49;00m[37m[39;49;00m$
    51^I[37m## Server-Pool Size Regulation (MPM specific)[39;49;00m[37m[39;49;00m$
    52^I[37m## [39;49;00m[37m[39;49;00m$
    53^I[37m[39;49;00m$
    54^I[37m# prefork MPM[39;49;00m[37m[39;49;00m$
    55^I[37m# StartServers ......... number of server processes to start[39;49;00m[37m[39;49;00m$
    56^I[37m# MinSpareServers ...... minimum number of server processes which are kept spare[39;49;00m[37m[39;49;00m$
    57^I[37m# MaxSpareServers ...... maximum number of server processes which are kept spare[39;49;00m[37m[39;49;00m$
    58^I[37m# MaxClients ........... maximum number of server processes allowed to start[39;49;00m[37m[39;49;00m$
    59^I[37m# MaxRequestsPerChild .. maximum number of requests a server process serves[39;49;00m[37m[39;49;00m$
    60^I[94m<IfModule[39;49;00m[37m [39;49;00m[33mprefork.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    61^I[36mStartServers[39;49;00m[37m         [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    62^I[36mMinSpareServers[39;49;00m[37m      [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    63^I[36mMaxSpareServers[39;49;00m[37m     [39;49;00m[34m10[39;49;00m[37m[39;49;00m$
    64^I[36mMaxClients[39;49;00m[37m          [39;49;00m[34m20[39;49;00m[37m[39;49;00m$
    65^I[36mMaxRequestsPerChild[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
    66^I[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    67^I[37m[39;49;00m$
    68^I[37m# pthread MPM[39;49;00m[37m[39;49;00m$
    69^I[37m# StartServers ......... initial  number of server processes to start[39;49;00m[37m[39;49;00m$
    70^I[37m# MaxClients ........... maximum  number of server processes allowed to start[39;49;00m[37m[39;49;00m$
    71^I[37m# MinSpareThreads ...... minimum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
    72^I[37m# MaxSpareThreads ...... maximum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
    73^I[37m# ThreadsPerChild ...... constant number of worker threads in each server process[39;49;00m[37m[39;49;00m$
    74^I[37m# MaxRequestsPerChild .. maximum  number of requests a server process serves[39;49;00m[37m[39;49;00m$
    75^I[94m<IfModule[39;49;00m[37m [39;49;00m[33mworker.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    76^I[36mStartServers[39;49;00m[37m         [39;49;00m[34m2[39;49;00m[37m[39;49;00m$
    77^I[36mMaxClients[39;49;00m[37m         [39;49;00m[34m150[39;49;00m[37m [39;49;00m[37m[39;49;00m$
    78^I[36mMinSpareThreads[39;49;00m[37m     [39;49;00m[34m25[39;49;00m[37m[39;49;00m$
    79^I[36mMaxSpareThreads[39;49;00m[37m     [39;49;00m[34m75[39;49;00m[37m[39;49;00m$
    80^I[36mThreadsPerChild[39;49;00m[37m     [39;49;00m[34m25[39;49;00m[37m[39;49;00m$
    81^I[36mMaxRequestsPerChild[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
    82^I[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    83^I[37m[39;49;00m$
    84^I[37m# perchild MPM[39;49;00m[37m[39;49;00m$
    85^I[37m# NumServers ........... constant number of server processes[39;49;00m[37m[39;49;00m$
    86^I[37m# StartThreads ......... initial  number of worker threads in each server process[39;49;00m[37m[39;49;00m$
    87^I[37m# MinSpareThreads ...... minimum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
    88^I[37m# MaxSpareThreads ...... maximum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
    89^I[37m# MaxThreadsPerChild ... maximum  number of worker threads in each server process[39;49;00m[37m[39;49;00m$
    90^I[37m# MaxRequestsPerChild .. maximum  number of connections per server process (then it dies)[39;49;00m[37m[39;49;00m$
    91^I[94m<IfModule[39;49;00m[37m [39;49;00m[33mperchild.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    92^I[36mNumServers[39;49;00m[37m           [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    93^I[36mStartThreads[39;49;00m[37m         [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    94^I[36mMinSpareThreads[39;49;00m[37m      [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    95^I[36mMaxSpareThreads[39;49;00m[37m     [39;49;00m[34m10[39;49;00m[37m[39;49;00m$
    96^I[36mMaxThreadsPerChild[39;49;00m[37m  [39;49;00m[34m20[39;49;00m[37m[39;49;00m$
    97^I[36mMaxRequestsPerChild[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
    98^I[36mAcceptMutex[39;49;00m[37m [39;49;00mfcntl[37m[39;49;00m$
    99^I[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   100^I[37m[39;49;00m$
   101^I[36mUser[39;49;00m[37m [39;49;00mwww-data[37m[39;49;00m$
   102^I[36mGroup[39;49;00m[37m [39;49;00mwww-data[37m[39;49;00m$
   103^I[37m[39;49;00m$
   104^I[37m# The following directives define some format nicknames for use with[39;49;00m[37m[39;49;00m$
   105^I[37m# a CustomLog directive (see below).[39;49;00m[37m[39;49;00m$
   106^I[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\""[39;49;00m[37m [39;49;00mcombined[37m[39;49;00m$
   107^I[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%h %l %u %t \"%r\" %>s %b"[39;49;00m[37m [39;49;00mcommon[37m[39;49;00m$
   108^I[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%{Referer}i -> %U"[39;49;00m[37m [39;49;00mreferer[37m[39;49;00m$
   109^I[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%{User-agent}i"[39;49;00m[37m [39;49;00magent[37m[39;49;00m$
   110^I[37m[39;49;00m$
   111^I[37m[39;49;00m$
   112^I[37m# Global error log.[39;49;00m[37m[39;49;00m$
   113^I[36mErrorLog[39;49;00m[37m [39;49;00m[33m/var/log/apache2/error.log[39;49;00m[37m[39;49;00m$
   114^I[37m[39;49;00m$
   115^I[37m# Include module configuration:[39;49;00m[37m[39;49;00m$
   116^I[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/mods-enabled/*.load[39;49;00m[37m[39;49;00m$
   117^I[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/mods-enabled/*.conf[39;49;00m[37m[39;49;00m$
   118^I[37m[39;49;00m$
   119^I[37m# Include all the user configurations:[39;49;00m[37m[39;49;00m$
   120^I[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/httpd.conf[39;49;00m[37m[39;49;00m$
   121^I[37m[39;49;00m$
   122^I[37m# Include ports listing[39;49;00m[37m[39;49;00m$
   123^I[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/ports.conf[39;49;00m[37m[39;49;00m$
   124^I[37m[39;49;00m$
   125^I[37m# Include generic snippets of statements[39;49;00m[37m[39;49;00m$
   126^I[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/conf.d/[39;49;00m[^.#]*[37m[39;49;00m$
   127^I[37m[39;49;00m$
   128^I[37m#Let's have some Icons, shall we?[39;49;00m[37m[39;49;00m$
   129^I[36mAlias[39;49;00m[37m [39;49;00m[33m/icons/[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/icons/"[39;49;00m[37m[39;49;00m$
   130^I[94m<Directory[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/icons"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   131^I[37m    [39;49;00m[36mOptions[39;49;00m[37m [39;49;00mIndexes[37m [39;49;00mMultiViews[37m[39;49;00m$
   132^I[37m    [39;49;00m[36mAllowOverride[39;49;00m[37m [39;49;00m[34mNone[39;49;00m[37m[39;49;00m$
   133^I[37m    [39;49;00m[36mOrder[39;49;00m[37m [39;49;00mallow,deny[37m[39;49;00m$
   134^I[37m    [39;49;00m[36mAllow[39;49;00m[37m [39;49;00mfrom[37m [39;49;00m[34mall[39;49;00m[37m[39;49;00m$
   135^I[94m</Directory[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   136^I[37m[39;49;00m$
   137^I[37m# Set up the default error docs.[39;49;00m[37m[39;49;00m$
   138^I[37m#[39;49;00m[37m[39;49;00m$
   139^I[37m# Customizable error responses come in three flavors:[39;49;00m[37m[39;49;00m$
   140^I[37m# 1) plain text 2) local redirects 3) external redirects[39;49;00m[37m[39;49;00m$
   141^I[37m#[39;49;00m[37m[39;49;00m$
   142^I[37m# Some examples:[39;49;00m[37m[39;49;00m$
   143^I[37m#ErrorDocument 500 "The server made a boo boo."[39;49;00m[37m[39;49;00m$
   144^I[37m#ErrorDocument 404 /missing.html[39;49;00m[37m[39;49;00m$
   145^I[37m#ErrorDocument 404 "/cgi-bin/missing_handler.pl"[39;49;00m[37m[39;49;00m$
   146^I[37m#ErrorDocument 402 http://www.example.com/subscription_info.html[39;49;00m[37m[39;49;00m$
   147^I[37m#[39;49;00m[37m[39;49;00m$
   148^I[37m[39;49;00m$
   149^I[37m#[39;49;00m[37m[39;49;00m$
   150^I[37m# Putting this all together, we can Internationalize error responses.[39;49;00m[37m[39;49;00m$
   151^I[37m#[39;49;00m[37m[39;49;00m$
   152^I[37m# We use Alias to redirect any /error/HTTP_<error>.html.var response to[39;49;00m[37m[39;49;00m$
   153^I[37m# our collection of by-error message multi-language collections.  We use [39;49;00m[37m[39;49;00m$
   154^I[37m# includes to substitute the appropriate text.[39;49;00m[37m[39;49;00m$
   155^I[37m#[39;49;00m[37m[39;49;00m$
   156^I[37m# You can modify the messages' appearance without changing any of the[39;49;00m[37m[39;49;00m$
   157^I[37m# default HTTP_<error>.html.var files by adding the line;[39;49;00m[37m[39;49;00m$
   158^I[37m#[39;49;00m[37m[39;49;00m$
   159^I[37m#   Alias /error/include/ "/your/include/path/"[39;49;00m[37m[39;49;00m$
   160^I[37m#[39;49;00m[37m[39;49;00m$
   161^I[37m# which allows you to create your own set of files by starting with the[39;49;00m[37m[39;49;00m$
   162^I[37m# /usr/local/apache2/error/include/ files and[39;49;00m[37m[39;49;00m$
   163^I[37m# copying them to /your/include/path/, even on a per-VirtualHost basis.[39;49;00m[37m[39;49;00m$
   164^I[37m#[39;49;00m[37m[39;49;00m$
   165^I[37m[39;49;00m$
   166^I[94m<IfModule[39;49;00m[37m [39;49;00m[33mmod_negotiation.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   167^I[94m<IfModule[39;49;00m[37m [39;49;00m[33mmod_include.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   168^I[37m    [39;49;00m[36mAlias[39;49;00m[37m [39;49;00m[33m/error/[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/error/"[39;49;00m[37m[39;49;00m$
   169^I[37m[39;49;00m$
   170^I[37m    [39;49;00m[94m<Directory[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/error"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   171^I[37m        [39;49;00m[36mAllowOverride[39;49;00m[37m [39;49;00m[34mNone[39;49;00m[37m[39;49;00m$
   172^I[37m        [39;49;00m[36mOptions[39;49;00m[37m [39;49;00mIncludesNoExec[37m[39;49;00m$
   173^I[37m        [39;49;00m[36mAddOutputFilter[39;49;00m[37m [39;49;00mIncludes[37m [39;49;00mhtml[37m[39;49;00m$
   174^I[37m        [39;49;00m[36mAddHandler[39;49;00m[37m [39;49;00mtype-map[37m [39;49;00mvar[37m[39;49;00m$
   175^I[37m        [39;49;00m[36mOrder[39;49;00m[37m [39;49;00mallow,deny[37m[39;49;00m$
   176^I[37m        [39;49;00m[36mAllow[39;49;00m[37m [39;49;00mfrom[37m [39;49;00m[34mall[39;49;00m[37m[39;49;00m$
   177^I[37m        [39;49;00m[36mLanguagePriority[39;49;00m[37m [39;49;00men[37m [39;49;00mes[37m [39;49;00mde[37m [39;49;00mfr[37m[39;49;00m$
   178^I[37m        [39;49;00m[36mForceLanguagePriority[39;49;00m[37m [39;49;00mPrefer[37m [39;49;00mFallback[37m[39;49;00m$
   179^I[37m    [39;49;00m[94m</Directory[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   180^I[37m[39;49;00m$
   181^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m400[39;49;00m[37m [39;49;00m[33m/error/HTTP_BAD_REQUEST.html.var[39;49;00m[37m[39;49;00m$
   182^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m401[39;49;00m[37m [39;49;00m[33m/error/HTTP_UNAUTHORIZED.html.var[39;49;00m[37m[39;49;00m$
   183^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m403[39;49;00m[37m [39;49;00m[33m/error/HTTP_FORBIDDEN.html.var[39;49;00m[37m[39;49;00m$
   184^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m404[39;49;00m[37m [39;49;00m[33m/error/HTTP_NOT_FOUND.html.var[39;49;00m[37m[39;49;00m$
   185^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m405[39;49;00m[37m [39;49;00m[33m/error/HTTP_METHOD_NOT_ALLOWED.html.var[39;49;00m[37m[39;49;00m$
   186^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m408[39;49;00m[37m [39;49;00m[33m/error/HTTP_REQUEST_TIME_OUT.html.var[39;49;00m[37m[39;49;00m$
   187^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m410[39;49;00m[37m [39;49;00m[33m/error/HTTP_GONE.html.var[39;49;00m[37m[39;49;00m$
   188^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m411[39;49;00m[37m [39;49;00m[33m/error/HTTP_LENGTH_REQUIRED.html.var[39;49;00m[37m[39;49;00m$
   189^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m412[39;49;00m[37m [39;49;00m[33m/error/HTTP_PRECONDITION_FAILED.html.var[39;49;00m[37m[39;49;00m$
   190^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m413[39;49;00m[37m [39;49;00m[33m/error/HTTP_REQUEST_ENTITY_TOO_LARGE.html.var[39;49;00m[37m[39;49;00m$
   191^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m414[39;49;00m[37m [39;49;00m[33m/error/HTTP_REQUEST_URI_TOO_LARGE.html.var[39;49;00m[37m[39;49;00m$
   192^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m415[39;49;00m[37m [39;49;00m[33m/error/HTTP_SERVICE_UNAVAILABLE.html.var[39;49;00m[37m[39;49;00m$
   193^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m500[39;49;00m[37m [39;49;00m[33m/error/HTTP_INTERNAL_SERVER_ERROR.html.var[39;49;00m[37m[39;49;00m$
   194^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m501[39;49;00m[37m [39;49;00m[33m/error/HTTP_NOT_IMPLEMENTED.html.var[39;49;00m[37m[39;49;00m$
   195^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m502[39;49;00m[37m [39;49;00m[33m/error/HTTP_BAD_GATEWAY.html.var[39;49;00m[37m[39;49;00m$
   196^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m503[39;49;00m[37m [39;49;00m[33m/error/HTTP_SERVICE_UNAVAILABLE.html.var[39;49;00m[37m[39;49;00m$
   197^I[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m506[39;49;00m[37m [39;49;00m[33m/error/HTTP_VARIANT_ALSO_VARIES.html.var[39;49;00m[37m[39;49;00m$
   198^I[37m[39;49;00m$
   199^I[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   200^I[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   201^I[37m[39;49;00m$
   202^I[36mDirectoryIndex[39;49;00m[37m [39;49;00mindex.html[37m [39;49;00mindex.cgi[37m [39;49;00mindex.pl[37m [39;49;00mindex.php[37m [39;49;00mindex.xhtml[37m[39;49;00m$
   203^I[37m[39;49;00m$
   204^I[37m# UserDir is now a module[39;49;00m[37m[39;49;00m$
   205^I[37m#UserDir public_html[39;49;00m[37m[39;49;00m$
   206^I[37m#UserDir disabled root[39;49;00m[37m[39;49;00m$
   207^I[37m[39;49;00m$
   208^I[37m#<Directory /home/*/public_html>[39;49;00m[37m[39;49;00m$
   209^I[37m#^IAllowOverride FileInfo AuthConfig Limit[39;49;00m[37m[39;49;00m$
   210^I[37m#^IOptions Indexes SymLinksIfOwnerMatch IncludesNoExec[39;49;00m[37m[39;49;00m$
   211^I[37m#</Directory>[39;49;00m[37m[39;49;00m$
   212^I[37m[39;49;00m$
   213^I[36mAccessFileName[39;49;00m[37m [39;49;00m.htaccess[37m[39;49;00m$
   214^I[37m[39;49;00m$
   215^I[94m<Files[39;49;00m[37m [39;49;00m[33m~ "^\.ht"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   216^I[37m    [39;49;00m[36mOrder[39;49;00m[37m [39;49;00mallow,deny[37m[39;49;00m$
   217^I[37m    [39;49;00m[36mDeny[39;49;00m[37m [39;49;00mfrom[37m [39;49;00m[34mall[39;49;00m[37m[39;49;00m$
   218^I[94m</Files[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   219^I[37m[39;49;00m$
   220^I[36mUseCanonicalName[39;49;00m[37m [39;49;00m[34mOff[39;49;00m[37m[39;49;00m$
   221^I[37m[39;49;00m$
   222^I[36mTypesConfig[39;49;00m[37m [39;49;00m[33m/etc/mime.types[39;49;00m[37m[39;49;00m$
   223^I[36mDefaultType[39;49;00m[37m [39;49;00mtext/plain[37m[39;49;00m$
   224^I[37m[39;49;00m$
   225^I[36mHostnameLookups[39;49;00m[37m [39;49;00m[34mOff[39;49;00m[37m[39;49;00m$
   226^I[37m[39;49;00m$
   227^I[36mIndexOptions[39;49;00m[37m [39;49;00mFancyIndexing[37m [39;49;00mVersionSort[37m[39;49;00m$
   228^I[37m[39;49;00m$
   229^I[36mAddIconByEncoding[39;49;00m[37m [39;49;00m(CMP,/icons/compressed.gif)[37m [39;49;00mx-compress[37m [39;49;00mx-gzip[37m[39;49;00m$
   230^I[37m[39;49;00m$
   231^I[36mAddIconByType[39;49;00m[37m [39;49;00m(TXT,/icons/text.gif)[37m [39;49;00mtext/*[37m[39;49;00m$
   232^I[36mAddIconByType[39;49;00m[37m [39;49;00m(IMG,/icons/image2.gif)[37m [39;49;00mimage/*[37m[39;49;00m$
   233^I[36mAddIconByType[39;49;00m[37m [39;49;00m(SND,/icons/sound2.gif)[37m [39;49;00maudio/*[37m[39;49;00m$
   234^I[36mAddIconByType[39;49;00m[37m [39;49;00m(VID,/icons/movie.gif)[37m [39;49;00mvideo/*[37m[39;49;00m$
   235^I[37m[39;49;00m$
   236^I[37m# This really should be .jpg.[39;49;00m[37m[39;49;00m$
   237^I[37m[39;49;00m$
   238^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/binary.gif[39;49;00m[37m [39;49;00m.bin[37m [39;49;00m.exe[37m[39;49;00m$
   239^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/binhex.gif[39;49;00m[37m [39;49;00m.hqx[37m[39;49;00m$
   240^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/tar.gif[39;49;00m[37m [39;49;00m.tar[37m[39;49;00m$
   241^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/world2.gif[39;49;00m[37m [39;49;00m.wrl[37m [39;49;00m.wrl.gz[37m [39;49;00m.vrml[37m [39;49;00m.vrm[37m [39;49;00m.iv[37m[39;49;00m$
   242^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/compressed.gif[39;49;00m[37m [39;49;00m.Z[37m [39;49;00m.z[37m [39;49;00m.tgz[37m [39;49;00m.gz[37m [39;49;00m.zip[37m[39;49;00m$
   243^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/a.gif[39;49;00m[37m [39;49;00m.ps[37m [39;49;00m.ai[37m [39;49;00m.eps[37m[39;49;00m$
   244^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/layout.gif[39;49;00m[37m [39;49;00m.html[37m [39;49;00m.shtml[37m [39;49;00m.htm[37m [39;49;00m.pdf[37m[39;49;00m$
   245^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/text.gif[39;49;00m[37m [39;49;00m.txt[37m[39;49;00m$
   246^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/c.gif[39;49;00m[37m [39;49;00m.c[37m[39;49;00m$
   247^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/p.gif[39;49;00m[37m [39;49;00m.pl[37m [39;49;00m.py[37m[39;49;00m$
   248^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/f.gif[39;49;00m[37m [39;49;00m.for[37m[39;49;00m$
   249^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/dvi.gif[39;49;00m[37m [39;49;00m.dvi[37m[39;49;00m$
   250^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/uuencoded.gif[39;49;00m[37m [39;49;00m.uu[37m[39;49;00m$
   251^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/script.gif[39;49;00m[37m [39;49;00m.conf[37m [39;49;00m.sh[37m [39;49;00m.shar[37m [39;49;00m.csh[37m [39;49;00m.ksh[37m [39;49;00m.tcl[37m[39;49;00m$
   252^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/tex.gif[39;49;00m[37m [39;49;00m.tex[37m[39;49;00m$
   253^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/bomb.gif[39;49;00m[37m [39;49;00mcore[37m[39;49;00m$
   254^I[37m[39;49;00m$
   255^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/back.gif[39;49;00m[37m [39;49;00m..[37m[39;49;00m$
   256^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/hand.right.gif[39;49;00m[37m [39;49;00mREADME[37m[39;49;00m$
   257^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/folder.gif[39;49;00m[37m [39;49;00m^^DIRECTORY^^[37m[39;49;00m$
   258^I[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/blank.gif[39;49;00m[37m [39;49;00m^^BLANKICON^^[37m[39;49;00m$
   259^I[37m[39;49;00m$
   260^I[37m[39;49;00m$
   261^I[37m# This is from Matty J's patch. Anyone want to make the icons?[39;49;00m[37m[39;49;00m$
   262^I[37m#AddIcon /icons/dirsymlink.jpg ^^SYMDIR^^[39;49;00m[37m[39;49;00m$
   263^I[37m#AddIcon /icons/symlink.jpg ^^SYMLINK^^[39;49;00m[37m[39;49;00m$
   264^I[37m[39;49;00m$
   265^I[36mDefaultIcon[39;49;00m[37m [39;49;00m[33m/icons/unknown.gif[39;49;00m[37m[39;49;00m$
   266^I[37m[39;49;00m$
   267^I[36mReadmeName[39;49;00m[37m [39;49;00mREADME.html[37m[39;49;00m$
   268^I[36mHeaderName[39;49;00m[37m [39;49;00mHEADER.html[37m[39;49;00m$
   269^I[37m[39;49;00m$
   270^I[36mIndexIgnore[39;49;00m[37m [39;49;00m.??*[37m [39;49;00m*~[37m [39;49;00m*#[37m [39;49;00mHEADER*[37m [39;49;00mRCS[37m [39;49;00mCVS[37m [39;49;00m*,t[37m[39;49;00m$
   271^I[37m[39;49;00m$
   272^I[36mAddEncoding[39;49;00m[37m [39;49;00mx-compress[37m [39;49;00mZ[37m[39;49;00m$
   273^I[36mAddEncoding[39;49;00m[37m [39;49;00mx-gzip[37m [39;49;00mgz[37m [39;49;00mtgz[37m[39;49;00m$
   274^I[37m[39;49;00m$
   275^I[36mAddLanguage[39;49;00m[37m [39;49;00mda[37m [39;49;00m.dk[37m[39;49;00m$
   276^I[36mAddLanguage[39;49;00m[37m [39;49;00mnl[37m [39;49;00m.nl[37m[39;49;00m$
   277^I[36mAddLanguage[39;49;00m[37m [39;49;00men[37m [39;49;00m.en[37m[39;49;00m$
   278^I[36mAddLanguage[39;49;00m[37m [39;49;00met[37m [39;49;00m.et[37m[39;49;00m$
   279^I[36mAddLanguage[39;49;00m[37m [39;49;00mfr[37m [39;49;00m.fr[37m[39;49;00m$
   280^I[36mAddLanguage[39;49;00m[37m [39;49;00mde[37m [39;49;00m.de[37m[39;49;00m$
   281^I[36mAddLanguage[39;49;00m[37m [39;49;00mel[37m [39;49;00m.el[37m[39;49;00m$
   282^I[36mAddLanguage[39;49;00m[37m [39;49;00mit[37m [39;49;00m.it[37m[39;49;00m$
   283^I[36mAddLanguage[39;49;00m[37m [39;49;00mja[37m [39;49;00m.ja[37m[39;49;00m$
   284^I[36mAddLanguage[39;49;00m[37m [39;49;00mpl[37m [39;49;00m.po[37m[39;49;00m$
   285^I[36mAddLanguage[39;49;00m[37m [39;49;00mko[37m [39;49;00m.ko[37m[39;49;00m$
   286^I[36mAddLanguage[39;49;00m[37m [39;49;00mpt[37m [39;49;00m.pt[37m[39;49;00m$
   287^I[36mAddLanguage[39;49;00m[37m [39;49;00mno[37m [39;49;00m.no[37m[39;49;00m$
   288^I[36mAddLanguage[39;49;00m[37m [39;49;00mpt-br[37m [39;49;00m.pt-br[37m[39;49;00m$
   289^I[36mAddLanguage[39;49;00m[37m [39;49;00mltz[37m [39;49;00m.ltz[37m[39;49;00m$
   290^I[36mAddLanguage[39;49;00m[37m [39;49;00mca[37m [39;49;00m.ca[37m[39;49;00m$
   291^I[36mAddLanguage[39;49;00m[37m [39;49;00mes[37m [39;49;00m.es[37m[39;49;00m$
   292^I[36mAddLanguage[39;49;00m[37m [39;49;00msv[37m [39;49;00m.se[37m[39;49;00m$
   293^I[36mAddLanguage[39;49;00m[37m [39;49;00mcz[37m [39;49;00m.cz[37m[39;49;00m$
   294^I[36mAddLanguage[39;49;00m[37m [39;49;00mru[37m [39;49;00m.ru[37m[39;49;00m$
   295^I[36mAddLanguage[39;49;00m[37m [39;49;00mtw[37m [39;49;00m.tw[37m[39;49;00m$
   296^I[36mAddLanguage[39;49;00m[37m [39;49;00mzh-tw[37m [39;49;00m.tw[37m[39;49;00m$
   297^I[37m[39;49;00m$
   298^I[36mLanguagePriority[39;49;00m[37m [39;49;00men[37m [39;49;00mda[37m [39;49;00mnl[37m [39;49;00met[37m [39;49;00mfr[37m [39;49;00mde[37m [39;49;00mel[37m [39;49;00mit[37m [39;49;00mja[37m [39;49;00mko[37m [39;49;00mno[37m [39;49;00mpl[37m [39;49;00mpt[37m [39;49;00mpt-br[37m [39;49;00mltz[37m [39;49;00mca[37m [39;49;00mes[37m [39;49;00msv[37m [39;49;00mtw[37m[39;49;00m$
   299^I[37m[39;49;00m$
   300^I[37m[39;49;00m$
   301^I[37m#AddDefaultCharset^IISO-8859-1[39;49;00m[37m[39;49;00m$
   302^I[37m[39;49;00m$
   303^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-1[37m  [39;49;00m.iso8859-1[37m  [39;49;00m.latin1[37m[39;49;00m$
   304^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-2[37m  [39;49;00m.iso8859-2[37m  [39;49;00m.latin2[37m [39;49;00m.cen[37m[39;49;00m$
   305^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-3[37m  [39;49;00m.iso8859-3[37m  [39;49;00m.latin3[37m[39;49;00m$
   306^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-4[37m  [39;49;00m.iso8859-4[37m  [39;49;00m.latin4[37m[39;49;00m$
   307^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-5[37m  [39;49;00m.iso8859-5[37m  [39;49;00m.latin5[37m [39;49;00m.cyr[37m [39;49;00m.iso-ru[37m[39;49;00m$
   308^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-6[37m  [39;49;00m.iso8859-6[37m  [39;49;00m.latin6[37m [39;49;00m.arb[37m[39;49;00m$
   309^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-7[37m  [39;49;00m.iso8859-7[37m  [39;49;00m.latin7[37m [39;49;00m.grk[37m[39;49;00m$
   310^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-8[37m  [39;49;00m.iso8859-8[37m  [39;49;00m.latin8[37m [39;49;00m.heb[37m^I[39;49;00m[37m[39;49;00m$
   311^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-9[37m  [39;49;00m.iso8859-9[37m  [39;49;00m.latin9[37m [39;49;00m.trk[37m[39;49;00m$
   312^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-2022-JP[37m [39;49;00m.iso2022-jp[37m [39;49;00m.jis[37m[39;49;00m$
   313^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-2022-KR[37m [39;49;00m.iso2022-kr[37m [39;49;00m.kis[37m[39;49;00m$
   314^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-2022-CN[37m [39;49;00m.iso2022-cn[37m [39;49;00m.cis[37m[39;49;00m$
   315^I[36mAddCharset[39;49;00m[37m [39;49;00mBig5[37m        [39;49;00m.Big5[37m       [39;49;00m.big5[37m[39;49;00m$
   316^I[37m# For russian, more than one charset is used (depends on client, mostly):[39;49;00m[37m[39;49;00m$
   317^I[36mAddCharset[39;49;00m[37m [39;49;00mWINDOWS-1251[37m [39;49;00m.cp-1251[37m   [39;49;00m.win-1251[37m[39;49;00m$
   318^I[36mAddCharset[39;49;00m[37m [39;49;00mCP866[37m       [39;49;00m.cp866[37m[39;49;00m$
   319^I[36mAddCharset[39;49;00m[37m [39;49;00mKOI8-r[37m      [39;49;00m.koi8-r[37m [39;49;00m.koi8-ru[37m[39;49;00m$
   320^I[36mAddCharset[39;49;00m[37m [39;49;00mKOI8-ru[37m     [39;49;00m.koi8-uk[37m [39;49;00m.ua[37m[39;49;00m$
   321^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-10646-UCS-2[37m [39;49;00m.ucs2[37m[39;49;00m$
   322^I[36mAddCharset[39;49;00m[37m [39;49;00mISO-10646-UCS-4[37m [39;49;00m.ucs4[37m[39;49;00m$
   323^I[36mAddCharset[39;49;00m[37m [39;49;00mUTF-8[37m       [39;49;00m.utf8[37m[39;49;00m$
   324^I[37m[39;49;00m$
   325^I[36mAddCharset[39;49;00m[37m [39;49;00mGB2312[37m      [39;49;00m.gb2312[37m [39;49;00m.gb[37m [39;49;00m[37m[39;49;00m$
   326^I[36mAddCharset[39;49;00m[37m [39;49;00mutf-7[37m       [39;49;00m.utf7[37m[39;49;00m$
   327^I[36mAddCharset[39;49;00m[37m [39;49;00mutf-8[37m       [39;49;00m.utf8[37m[39;49;00m$
   328^I[36mAddCharset[39;49;00m[37m [39;49;00mbig5[37m^I       [39;49;00m.big5[37m [39;49;00m.b5[37m[39;49;00m$
   329^I[36mAddCharset[39;49;00m[37m [39;49;00mEUC-TW[37m      [39;49;00m.euc-tw[37m^I[39;49;00m[37m[39;49;00m$
   330^I[36mAddCharset[39;49;00m[37m [39;49;00mEUC-JP[37m      [39;49;00m.euc-jp[37m[39;49;00m$
   331^I[36mAddCharset[39;49;00m[37m [39;49;00mEUC-KR[37m      [39;49;00m.euc-kr[37m[39;49;00m$
   332^I[36mAddCharset[39;49;00m[37m [39;49;00mshift_jis[37m   [39;49;00m.sjis[37m[39;49;00m$
   333^I[37m[39;49;00m$
   334^I[37m#AddType application/x-httpd-php .php[39;49;00m[37m[39;49;00m$
   335^I[37m#AddType application/x-httpd-php-source .phps[39;49;00m[37m[39;49;00m$
   336^I[37m[39;49;00m$
   337^I[36mAddType[39;49;00m[37m [39;49;00mapplication/x-tar[37m [39;49;00m.tgz[37m[39;49;00m$
   338^I[37m[39;49;00m$
   339^I[37m# To use CGI scripts outside /cgi-bin/:[39;49;00m[37m[39;49;00m$
   340^I[37m#[39;49;00m[37m[39;49;00m$
   341^I[37m#AddHandler cgi-script .cgi[39;49;00m[37m[39;49;00m$
   342^I[37m[39;49;00m$
   343^I[37m# To use server-parsed HTML files[39;49;00m[37m[39;49;00m$
   344^I[37m#[39;49;00m[37m[39;49;00m$
   345^I[94m<FilesMatch[39;49;00m[37m [39;49;00m[33m"\.shtml(\..+)?$"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   346^I[37m    [39;49;00m[36mSetOutputFilter[39;49;00m[37m [39;49;00mINCLUDES[37m[39;49;00m$
   347^I[94m</FilesMatch[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   348^I[37m[39;49;00m$
   349^I[37m# If you wish to use server-parsed imagemap files, use[39;49;00m[37m[39;49;00m$
   350^I[37m#[39;49;00m[37m[39;49;00m$
   351^I[37m#AddHandler imap-file map[39;49;00m[37m[39;49;00m$
   352^I[37m[39;49;00m$
   353^I[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"Mozilla/2"[39;49;00m[37m [39;49;00mnokeepalive[37m[39;49;00m$
   354^I[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"MSIE 4\.0b2;"[39;49;00m[37m [39;49;00mnokeepalive[37m [39;49;00mdowngrade-1.0[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
   355^I[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"RealPlayer 4\.0"[39;49;00m[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
   356^I[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"Java/1\.0"[39;49;00m[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
   357^I[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"JDK/1\.0"[39;49;00m[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
   358^I[37m[39;49;00m$
   359^I[37m#[39;49;00m[37m[39;49;00m$
   360^I[37m# The following directive disables redirects on non-GET requests for[39;49;00m[37m[39;49;00m$
   361^I[37m# a directory that does not include the trailing slash.  This fixes a [39;49;00m[37m[39;49;00m$
   362^I[37m# problem with Microsoft WebFolders which does not appropriately handle [39;49;00m[37m[39;49;00m$
   363^I[37m# redirects for folders with DAV methods.[39;49;00m[37m[39;49;00m$
   364^I[37m#[39;49;00m[37m[39;49;00m$
   365^I[37m[39;49;00m$
   366^I[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"Microsoft Data Access Internet Publishing Provider"[39;49;00m[37m [39;49;00mredirect-carefully[37m[39;49;00m$
   367^I[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"^WebDrive"[39;49;00m[37m [39;49;00mredirect-carefully[37m[39;49;00m$
   368^I[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"^gnome-vfs"[39;49;00m[37m [39;49;00mredirect-carefully[37m [39;49;00m[37m[39;49;00m$
   369^I[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"^WebDAVFS/1.[012]"[39;49;00m[37m [39;49;00mredirect-carefully[37m[39;49;00m$
   370^I[37m[39;49;00m$
   371^I[37m# Allow server status reports, with the URL of http://servername/server-status[39;49;00m[37m[39;49;00m$
   372^I[37m# Change the ".your_domain.com" to match your domain to enable.[39;49;00m[37m[39;49;00m$
   373^I[37m#[39;49;00m[37m[39;49;00m$
   374^I[37m#<Location /server-status>[39;49;00m[37m[39;49;00m$
   375^I[37m#    SetHandler server-status[39;49;00m[37m[39;49;00m$
   376^I[37m#    Order deny,allow[39;49;00m[37m[39;49;00m$
   377^I[37m#    Deny from all[39;49;00m[37m[39;49;00m$
   378^I[37m#    Allow from .your_domain.com[39;49;00m[37m[39;49;00m$
   379^I[37m#</Location>[39;49;00m[37m[39;49;00m$
   380^I[37m[39;49;00m$
   381^I[37m# Allow remote server configuration reports, with the URL of[39;49;00m[37m[39;49;00m$
   382^I[37m#  http://servername/server-info (requires that mod_info.c be loaded).[39;49;00m[37m[39;49;00m$
   383^I[37m# Change the ".your_domain.com" to match your domain to enable.[39;49;00m[37m[39;49;00m$
   384^I[37m#[39;49;00m[37m[39;49;00m$
   385^I[37m#<Location /server-info>[39;49;00m[37m[39;49;00m$
   386^I[37m#    SetHandler server-info[39;49;00m[37m[39;49;00m$
   387^I[37m#    Order deny,allow[39;49;00m[37m[39;49;00m$
   388^I[37m#    Deny from all[39;49;00m[37m[39;49;00m$
   389^I[37m#    Allow from .your_domain.com[39;49;00m[37m[39;49;00m$
   390^I[37m#</Location>[39;49;00m[37m[39;49;00m$
   391^I[37m[39;49;00m$
   392^I[37m# Include the virtual host configurations:[39;49;00m[37m[39;49;00m$
   393^I[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/sites-enabled/[39;49;00m[^.#]*[37m[39;49;00m$
   394^I[37m[39;49;00m$
   395^I[37m# From PR#766[39;49;00m[37m[39;49;00m$
   396^I[94m<IfVersion[39;49;00m[37m [39;49;00m[33m>= 2.4[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   397^I[36mErrorLogFormat[39;49;00m[37m [39;49;00m[33m"%{cu}t %M"[39;49;00m[37m[39;49;00m$
   398^I[94m</IfVersion[39;49;00m[94m>[39;49;00m$
