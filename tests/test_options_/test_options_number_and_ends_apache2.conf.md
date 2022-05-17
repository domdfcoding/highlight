     1	[37m# Based upon the NCSA server configuration files originally by Rob McCool.[39;49;00m[37m[39;49;00m$
     2	[37m# Changed extensively for the Debian package by Daniel Stone <daniel@sfarc.net>[39;49;00m[37m[39;49;00m$
     3	[37m# and also by Thom May <thom@debian.org>.[39;49;00m[37m[39;49;00m$
     4	[37m[39;49;00m$
     5	[37m# ServerRoot: The top of the directory tree under which the server's[39;49;00m[37m[39;49;00m$
     6	[37m# configuration, error, and log files are kept.[39;49;00m[37m[39;49;00m$
     7	[37m#[39;49;00m[37m[39;49;00m$
     8	[37m# NOTE!  If you intend to place this on an NFS (or otherwise network)[39;49;00m[37m[39;49;00m$
     9	[37m# mounted filesystem then please read the LockFile documentation[39;49;00m[37m[39;49;00m$
    10	[37m# (available at <URL:http://www.apache.org/docs/mod/core.html#lockfile>);[39;49;00m[37m[39;49;00m$
    11	[37m# you will save yourself a lot of trouble.[39;49;00m[37m[39;49;00m$
    12	[37m[39;49;00m$
    13	[36mServerRoot[39;49;00m[37m [39;49;00m[33m"/etc/apache2"[39;49;00m[37m[39;49;00m$
    14	[37m[39;49;00m$
    15	[37m# The LockFile directive sets the path to the lockfile used when Apache[39;49;00m[37m[39;49;00m$
    16	[37m# is compiled with either USE_FCNTL_SERIALIZED_ACCEPT or[39;49;00m[37m[39;49;00m$
    17	[37m# USE_FLOCK_SERIALIZED_ACCEPT. This directive should normally be left at[39;49;00m[37m[39;49;00m$
    18	[37m# its default value. The main reason for changing it is if the logs[39;49;00m[37m[39;49;00m$
    19	[37m# directory is NFS mounted, since the lockfile MUST BE STORED ON A LOCAL[39;49;00m[37m[39;49;00m$
    20	[37m# DISK. The PID of the main server process is automatically appended to[39;49;00m[37m[39;49;00m$
    21	[37m# the filename. [39;49;00m[37m[39;49;00m$
    22	[37m[39;49;00m$
    23	[36mLockFile[39;49;00m[37m [39;49;00m[33m/var/lock/apache2/accept.lock[39;49;00m[37m[39;49;00m$
    24	[37m[39;49;00m$
    25	[37m# PidFile: The file in which the server should record its process[39;49;00m[37m[39;49;00m$
    26	[37m# identification number when it starts.[39;49;00m[37m[39;49;00m$
    27	[37m[39;49;00m$
    28	[36mPidFile[39;49;00m[37m [39;49;00m[33m/var/run/apache2.pid[39;49;00m[37m[39;49;00m$
    29	[37m[39;49;00m$
    30	[37m# Timeout: The number of seconds before receives and sends time out.[39;49;00m[37m[39;49;00m$
    31	[37m[39;49;00m$
    32	[36mTimeout[39;49;00m[37m [39;49;00m[34m300[39;49;00m[37m[39;49;00m$
    33	[37m[39;49;00m$
    34	[37m# KeepAlive: Whether or not to allow persistent connections (more than[39;49;00m[37m[39;49;00m$
    35	[37m# one request per connection). Set to "Off" to deactivate.[39;49;00m[37m[39;49;00m$
    36	[37m[39;49;00m$
    37	[36mKeepAlive[39;49;00m[37m [39;49;00m[34mOn[39;49;00m[37m[39;49;00m$
    38	[37m[39;49;00m$
    39	[37m# MaxKeepAliveRequests: The maximum number of requests to allow[39;49;00m[37m[39;49;00m$
    40	[37m# during a persistent connection. Set to 0 to allow an unlimited amount.[39;49;00m[37m[39;49;00m$
    41	[37m# We recommend you leave this number high, for maximum performance.[39;49;00m[37m[39;49;00m$
    42	[37m[39;49;00m$
    43	[36mMaxKeepAliveRequests[39;49;00m[37m [39;49;00m[34m100[39;49;00m[37m[39;49;00m$
    44	[37m[39;49;00m$
    45	[37m# KeepAliveTimeout: Number of seconds to wait for the next request from the[39;49;00m[37m[39;49;00m$
    46	[37m# same client on the same connection.[39;49;00m[37m[39;49;00m$
    47	[37m[39;49;00m$
    48	[36mKeepAliveTimeout[39;49;00m[37m [39;49;00m[34m15[39;49;00m[37m[39;49;00m$
    49	[37m[39;49;00m$
    50	[37m##[39;49;00m[37m[39;49;00m$
    51	[37m## Server-Pool Size Regulation (MPM specific)[39;49;00m[37m[39;49;00m$
    52	[37m## [39;49;00m[37m[39;49;00m$
    53	[37m[39;49;00m$
    54	[37m# prefork MPM[39;49;00m[37m[39;49;00m$
    55	[37m# StartServers ......... number of server processes to start[39;49;00m[37m[39;49;00m$
    56	[37m# MinSpareServers ...... minimum number of server processes which are kept spare[39;49;00m[37m[39;49;00m$
    57	[37m# MaxSpareServers ...... maximum number of server processes which are kept spare[39;49;00m[37m[39;49;00m$
    58	[37m# MaxClients ........... maximum number of server processes allowed to start[39;49;00m[37m[39;49;00m$
    59	[37m# MaxRequestsPerChild .. maximum number of requests a server process serves[39;49;00m[37m[39;49;00m$
    60	[94m<IfModule[39;49;00m[37m [39;49;00m[33mprefork.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    61	[36mStartServers[39;49;00m[37m         [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    62	[36mMinSpareServers[39;49;00m[37m      [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    63	[36mMaxSpareServers[39;49;00m[37m     [39;49;00m[34m10[39;49;00m[37m[39;49;00m$
    64	[36mMaxClients[39;49;00m[37m          [39;49;00m[34m20[39;49;00m[37m[39;49;00m$
    65	[36mMaxRequestsPerChild[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
    66	[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    67	[37m[39;49;00m$
    68	[37m# pthread MPM[39;49;00m[37m[39;49;00m$
    69	[37m# StartServers ......... initial  number of server processes to start[39;49;00m[37m[39;49;00m$
    70	[37m# MaxClients ........... maximum  number of server processes allowed to start[39;49;00m[37m[39;49;00m$
    71	[37m# MinSpareThreads ...... minimum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
    72	[37m# MaxSpareThreads ...... maximum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
    73	[37m# ThreadsPerChild ...... constant number of worker threads in each server process[39;49;00m[37m[39;49;00m$
    74	[37m# MaxRequestsPerChild .. maximum  number of requests a server process serves[39;49;00m[37m[39;49;00m$
    75	[94m<IfModule[39;49;00m[37m [39;49;00m[33mworker.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    76	[36mStartServers[39;49;00m[37m         [39;49;00m[34m2[39;49;00m[37m[39;49;00m$
    77	[36mMaxClients[39;49;00m[37m         [39;49;00m[34m150[39;49;00m[37m [39;49;00m[37m[39;49;00m$
    78	[36mMinSpareThreads[39;49;00m[37m     [39;49;00m[34m25[39;49;00m[37m[39;49;00m$
    79	[36mMaxSpareThreads[39;49;00m[37m     [39;49;00m[34m75[39;49;00m[37m[39;49;00m$
    80	[36mThreadsPerChild[39;49;00m[37m     [39;49;00m[34m25[39;49;00m[37m[39;49;00m$
    81	[36mMaxRequestsPerChild[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
    82	[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    83	[37m[39;49;00m$
    84	[37m# perchild MPM[39;49;00m[37m[39;49;00m$
    85	[37m# NumServers ........... constant number of server processes[39;49;00m[37m[39;49;00m$
    86	[37m# StartThreads ......... initial  number of worker threads in each server process[39;49;00m[37m[39;49;00m$
    87	[37m# MinSpareThreads ...... minimum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
    88	[37m# MaxSpareThreads ...... maximum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
    89	[37m# MaxThreadsPerChild ... maximum  number of worker threads in each server process[39;49;00m[37m[39;49;00m$
    90	[37m# MaxRequestsPerChild .. maximum  number of connections per server process (then it dies)[39;49;00m[37m[39;49;00m$
    91	[94m<IfModule[39;49;00m[37m [39;49;00m[33mperchild.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
    92	[36mNumServers[39;49;00m[37m           [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    93	[36mStartThreads[39;49;00m[37m         [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    94	[36mMinSpareThreads[39;49;00m[37m      [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
    95	[36mMaxSpareThreads[39;49;00m[37m     [39;49;00m[34m10[39;49;00m[37m[39;49;00m$
    96	[36mMaxThreadsPerChild[39;49;00m[37m  [39;49;00m[34m20[39;49;00m[37m[39;49;00m$
    97	[36mMaxRequestsPerChild[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
    98	[36mAcceptMutex[39;49;00m[37m [39;49;00mfcntl[37m[39;49;00m$
    99	[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   100	[37m[39;49;00m$
   101	[36mUser[39;49;00m[37m [39;49;00mwww-data[37m[39;49;00m$
   102	[36mGroup[39;49;00m[37m [39;49;00mwww-data[37m[39;49;00m$
   103	[37m[39;49;00m$
   104	[37m# The following directives define some format nicknames for use with[39;49;00m[37m[39;49;00m$
   105	[37m# a CustomLog directive (see below).[39;49;00m[37m[39;49;00m$
   106	[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\""[39;49;00m[37m [39;49;00mcombined[37m[39;49;00m$
   107	[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%h %l %u %t \"%r\" %>s %b"[39;49;00m[37m [39;49;00mcommon[37m[39;49;00m$
   108	[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%{Referer}i -> %U"[39;49;00m[37m [39;49;00mreferer[37m[39;49;00m$
   109	[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%{User-agent}i"[39;49;00m[37m [39;49;00magent[37m[39;49;00m$
   110	[37m[39;49;00m$
   111	[37m[39;49;00m$
   112	[37m# Global error log.[39;49;00m[37m[39;49;00m$
   113	[36mErrorLog[39;49;00m[37m [39;49;00m[33m/var/log/apache2/error.log[39;49;00m[37m[39;49;00m$
   114	[37m[39;49;00m$
   115	[37m# Include module configuration:[39;49;00m[37m[39;49;00m$
   116	[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/mods-enabled/*.load[39;49;00m[37m[39;49;00m$
   117	[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/mods-enabled/*.conf[39;49;00m[37m[39;49;00m$
   118	[37m[39;49;00m$
   119	[37m# Include all the user configurations:[39;49;00m[37m[39;49;00m$
   120	[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/httpd.conf[39;49;00m[37m[39;49;00m$
   121	[37m[39;49;00m$
   122	[37m# Include ports listing[39;49;00m[37m[39;49;00m$
   123	[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/ports.conf[39;49;00m[37m[39;49;00m$
   124	[37m[39;49;00m$
   125	[37m# Include generic snippets of statements[39;49;00m[37m[39;49;00m$
   126	[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/conf.d/[39;49;00m[^.#]*[37m[39;49;00m$
   127	[37m[39;49;00m$
   128	[37m#Let's have some Icons, shall we?[39;49;00m[37m[39;49;00m$
   129	[36mAlias[39;49;00m[37m [39;49;00m[33m/icons/[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/icons/"[39;49;00m[37m[39;49;00m$
   130	[94m<Directory[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/icons"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   131	[37m    [39;49;00m[36mOptions[39;49;00m[37m [39;49;00mIndexes[37m [39;49;00mMultiViews[37m[39;49;00m$
   132	[37m    [39;49;00m[36mAllowOverride[39;49;00m[37m [39;49;00m[34mNone[39;49;00m[37m[39;49;00m$
   133	[37m    [39;49;00m[36mOrder[39;49;00m[37m [39;49;00mallow,deny[37m[39;49;00m$
   134	[37m    [39;49;00m[36mAllow[39;49;00m[37m [39;49;00mfrom[37m [39;49;00m[34mall[39;49;00m[37m[39;49;00m$
   135	[94m</Directory[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   136	[37m[39;49;00m$
   137	[37m# Set up the default error docs.[39;49;00m[37m[39;49;00m$
   138	[37m#[39;49;00m[37m[39;49;00m$
   139	[37m# Customizable error responses come in three flavors:[39;49;00m[37m[39;49;00m$
   140	[37m# 1) plain text 2) local redirects 3) external redirects[39;49;00m[37m[39;49;00m$
   141	[37m#[39;49;00m[37m[39;49;00m$
   142	[37m# Some examples:[39;49;00m[37m[39;49;00m$
   143	[37m#ErrorDocument 500 "The server made a boo boo."[39;49;00m[37m[39;49;00m$
   144	[37m#ErrorDocument 404 /missing.html[39;49;00m[37m[39;49;00m$
   145	[37m#ErrorDocument 404 "/cgi-bin/missing_handler.pl"[39;49;00m[37m[39;49;00m$
   146	[37m#ErrorDocument 402 http://www.example.com/subscription_info.html[39;49;00m[37m[39;49;00m$
   147	[37m#[39;49;00m[37m[39;49;00m$
   148	[37m[39;49;00m$
   149	[37m#[39;49;00m[37m[39;49;00m$
   150	[37m# Putting this all together, we can Internationalize error responses.[39;49;00m[37m[39;49;00m$
   151	[37m#[39;49;00m[37m[39;49;00m$
   152	[37m# We use Alias to redirect any /error/HTTP_<error>.html.var response to[39;49;00m[37m[39;49;00m$
   153	[37m# our collection of by-error message multi-language collections.  We use [39;49;00m[37m[39;49;00m$
   154	[37m# includes to substitute the appropriate text.[39;49;00m[37m[39;49;00m$
   155	[37m#[39;49;00m[37m[39;49;00m$
   156	[37m# You can modify the messages' appearance without changing any of the[39;49;00m[37m[39;49;00m$
   157	[37m# default HTTP_<error>.html.var files by adding the line;[39;49;00m[37m[39;49;00m$
   158	[37m#[39;49;00m[37m[39;49;00m$
   159	[37m#   Alias /error/include/ "/your/include/path/"[39;49;00m[37m[39;49;00m$
   160	[37m#[39;49;00m[37m[39;49;00m$
   161	[37m# which allows you to create your own set of files by starting with the[39;49;00m[37m[39;49;00m$
   162	[37m# /usr/local/apache2/error/include/ files and[39;49;00m[37m[39;49;00m$
   163	[37m# copying them to /your/include/path/, even on a per-VirtualHost basis.[39;49;00m[37m[39;49;00m$
   164	[37m#[39;49;00m[37m[39;49;00m$
   165	[37m[39;49;00m$
   166	[94m<IfModule[39;49;00m[37m [39;49;00m[33mmod_negotiation.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   167	[94m<IfModule[39;49;00m[37m [39;49;00m[33mmod_include.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   168	[37m    [39;49;00m[36mAlias[39;49;00m[37m [39;49;00m[33m/error/[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/error/"[39;49;00m[37m[39;49;00m$
   169	[37m[39;49;00m$
   170	[37m    [39;49;00m[94m<Directory[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/error"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   171	[37m        [39;49;00m[36mAllowOverride[39;49;00m[37m [39;49;00m[34mNone[39;49;00m[37m[39;49;00m$
   172	[37m        [39;49;00m[36mOptions[39;49;00m[37m [39;49;00mIncludesNoExec[37m[39;49;00m$
   173	[37m        [39;49;00m[36mAddOutputFilter[39;49;00m[37m [39;49;00mIncludes[37m [39;49;00mhtml[37m[39;49;00m$
   174	[37m        [39;49;00m[36mAddHandler[39;49;00m[37m [39;49;00mtype-map[37m [39;49;00mvar[37m[39;49;00m$
   175	[37m        [39;49;00m[36mOrder[39;49;00m[37m [39;49;00mallow,deny[37m[39;49;00m$
   176	[37m        [39;49;00m[36mAllow[39;49;00m[37m [39;49;00mfrom[37m [39;49;00m[34mall[39;49;00m[37m[39;49;00m$
   177	[37m        [39;49;00m[36mLanguagePriority[39;49;00m[37m [39;49;00men[37m [39;49;00mes[37m [39;49;00mde[37m [39;49;00mfr[37m[39;49;00m$
   178	[37m        [39;49;00m[36mForceLanguagePriority[39;49;00m[37m [39;49;00mPrefer[37m [39;49;00mFallback[37m[39;49;00m$
   179	[37m    [39;49;00m[94m</Directory[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   180	[37m[39;49;00m$
   181	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m400[39;49;00m[37m [39;49;00m[33m/error/HTTP_BAD_REQUEST.html.var[39;49;00m[37m[39;49;00m$
   182	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m401[39;49;00m[37m [39;49;00m[33m/error/HTTP_UNAUTHORIZED.html.var[39;49;00m[37m[39;49;00m$
   183	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m403[39;49;00m[37m [39;49;00m[33m/error/HTTP_FORBIDDEN.html.var[39;49;00m[37m[39;49;00m$
   184	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m404[39;49;00m[37m [39;49;00m[33m/error/HTTP_NOT_FOUND.html.var[39;49;00m[37m[39;49;00m$
   185	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m405[39;49;00m[37m [39;49;00m[33m/error/HTTP_METHOD_NOT_ALLOWED.html.var[39;49;00m[37m[39;49;00m$
   186	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m408[39;49;00m[37m [39;49;00m[33m/error/HTTP_REQUEST_TIME_OUT.html.var[39;49;00m[37m[39;49;00m$
   187	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m410[39;49;00m[37m [39;49;00m[33m/error/HTTP_GONE.html.var[39;49;00m[37m[39;49;00m$
   188	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m411[39;49;00m[37m [39;49;00m[33m/error/HTTP_LENGTH_REQUIRED.html.var[39;49;00m[37m[39;49;00m$
   189	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m412[39;49;00m[37m [39;49;00m[33m/error/HTTP_PRECONDITION_FAILED.html.var[39;49;00m[37m[39;49;00m$
   190	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m413[39;49;00m[37m [39;49;00m[33m/error/HTTP_REQUEST_ENTITY_TOO_LARGE.html.var[39;49;00m[37m[39;49;00m$
   191	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m414[39;49;00m[37m [39;49;00m[33m/error/HTTP_REQUEST_URI_TOO_LARGE.html.var[39;49;00m[37m[39;49;00m$
   192	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m415[39;49;00m[37m [39;49;00m[33m/error/HTTP_SERVICE_UNAVAILABLE.html.var[39;49;00m[37m[39;49;00m$
   193	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m500[39;49;00m[37m [39;49;00m[33m/error/HTTP_INTERNAL_SERVER_ERROR.html.var[39;49;00m[37m[39;49;00m$
   194	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m501[39;49;00m[37m [39;49;00m[33m/error/HTTP_NOT_IMPLEMENTED.html.var[39;49;00m[37m[39;49;00m$
   195	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m502[39;49;00m[37m [39;49;00m[33m/error/HTTP_BAD_GATEWAY.html.var[39;49;00m[37m[39;49;00m$
   196	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m503[39;49;00m[37m [39;49;00m[33m/error/HTTP_SERVICE_UNAVAILABLE.html.var[39;49;00m[37m[39;49;00m$
   197	[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m506[39;49;00m[37m [39;49;00m[33m/error/HTTP_VARIANT_ALSO_VARIES.html.var[39;49;00m[37m[39;49;00m$
   198	[37m[39;49;00m$
   199	[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   200	[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   201	[37m[39;49;00m$
   202	[36mDirectoryIndex[39;49;00m[37m [39;49;00mindex.html[37m [39;49;00mindex.cgi[37m [39;49;00mindex.pl[37m [39;49;00mindex.php[37m [39;49;00mindex.xhtml[37m[39;49;00m$
   203	[37m[39;49;00m$
   204	[37m# UserDir is now a module[39;49;00m[37m[39;49;00m$
   205	[37m#UserDir public_html[39;49;00m[37m[39;49;00m$
   206	[37m#UserDir disabled root[39;49;00m[37m[39;49;00m$
   207	[37m[39;49;00m$
   208	[37m#<Directory /home/*/public_html>[39;49;00m[37m[39;49;00m$
   209	[37m#	AllowOverride FileInfo AuthConfig Limit[39;49;00m[37m[39;49;00m$
   210	[37m#	Options Indexes SymLinksIfOwnerMatch IncludesNoExec[39;49;00m[37m[39;49;00m$
   211	[37m#</Directory>[39;49;00m[37m[39;49;00m$
   212	[37m[39;49;00m$
   213	[36mAccessFileName[39;49;00m[37m [39;49;00m.htaccess[37m[39;49;00m$
   214	[37m[39;49;00m$
   215	[94m<Files[39;49;00m[37m [39;49;00m[33m~ "^\.ht"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   216	[37m    [39;49;00m[36mOrder[39;49;00m[37m [39;49;00mallow,deny[37m[39;49;00m$
   217	[37m    [39;49;00m[36mDeny[39;49;00m[37m [39;49;00mfrom[37m [39;49;00m[34mall[39;49;00m[37m[39;49;00m$
   218	[94m</Files[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   219	[37m[39;49;00m$
   220	[36mUseCanonicalName[39;49;00m[37m [39;49;00m[34mOff[39;49;00m[37m[39;49;00m$
   221	[37m[39;49;00m$
   222	[36mTypesConfig[39;49;00m[37m [39;49;00m[33m/etc/mime.types[39;49;00m[37m[39;49;00m$
   223	[36mDefaultType[39;49;00m[37m [39;49;00mtext/plain[37m[39;49;00m$
   224	[37m[39;49;00m$
   225	[36mHostnameLookups[39;49;00m[37m [39;49;00m[34mOff[39;49;00m[37m[39;49;00m$
   226	[37m[39;49;00m$
   227	[36mIndexOptions[39;49;00m[37m [39;49;00mFancyIndexing[37m [39;49;00mVersionSort[37m[39;49;00m$
   228	[37m[39;49;00m$
   229	[36mAddIconByEncoding[39;49;00m[37m [39;49;00m(CMP,/icons/compressed.gif)[37m [39;49;00mx-compress[37m [39;49;00mx-gzip[37m[39;49;00m$
   230	[37m[39;49;00m$
   231	[36mAddIconByType[39;49;00m[37m [39;49;00m(TXT,/icons/text.gif)[37m [39;49;00mtext/*[37m[39;49;00m$
   232	[36mAddIconByType[39;49;00m[37m [39;49;00m(IMG,/icons/image2.gif)[37m [39;49;00mimage/*[37m[39;49;00m$
   233	[36mAddIconByType[39;49;00m[37m [39;49;00m(SND,/icons/sound2.gif)[37m [39;49;00maudio/*[37m[39;49;00m$
   234	[36mAddIconByType[39;49;00m[37m [39;49;00m(VID,/icons/movie.gif)[37m [39;49;00mvideo/*[37m[39;49;00m$
   235	[37m[39;49;00m$
   236	[37m# This really should be .jpg.[39;49;00m[37m[39;49;00m$
   237	[37m[39;49;00m$
   238	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/binary.gif[39;49;00m[37m [39;49;00m.bin[37m [39;49;00m.exe[37m[39;49;00m$
   239	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/binhex.gif[39;49;00m[37m [39;49;00m.hqx[37m[39;49;00m$
   240	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/tar.gif[39;49;00m[37m [39;49;00m.tar[37m[39;49;00m$
   241	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/world2.gif[39;49;00m[37m [39;49;00m.wrl[37m [39;49;00m.wrl.gz[37m [39;49;00m.vrml[37m [39;49;00m.vrm[37m [39;49;00m.iv[37m[39;49;00m$
   242	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/compressed.gif[39;49;00m[37m [39;49;00m.Z[37m [39;49;00m.z[37m [39;49;00m.tgz[37m [39;49;00m.gz[37m [39;49;00m.zip[37m[39;49;00m$
   243	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/a.gif[39;49;00m[37m [39;49;00m.ps[37m [39;49;00m.ai[37m [39;49;00m.eps[37m[39;49;00m$
   244	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/layout.gif[39;49;00m[37m [39;49;00m.html[37m [39;49;00m.shtml[37m [39;49;00m.htm[37m [39;49;00m.pdf[37m[39;49;00m$
   245	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/text.gif[39;49;00m[37m [39;49;00m.txt[37m[39;49;00m$
   246	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/c.gif[39;49;00m[37m [39;49;00m.c[37m[39;49;00m$
   247	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/p.gif[39;49;00m[37m [39;49;00m.pl[37m [39;49;00m.py[37m[39;49;00m$
   248	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/f.gif[39;49;00m[37m [39;49;00m.for[37m[39;49;00m$
   249	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/dvi.gif[39;49;00m[37m [39;49;00m.dvi[37m[39;49;00m$
   250	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/uuencoded.gif[39;49;00m[37m [39;49;00m.uu[37m[39;49;00m$
   251	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/script.gif[39;49;00m[37m [39;49;00m.conf[37m [39;49;00m.sh[37m [39;49;00m.shar[37m [39;49;00m.csh[37m [39;49;00m.ksh[37m [39;49;00m.tcl[37m[39;49;00m$
   252	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/tex.gif[39;49;00m[37m [39;49;00m.tex[37m[39;49;00m$
   253	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/bomb.gif[39;49;00m[37m [39;49;00mcore[37m[39;49;00m$
   254	[37m[39;49;00m$
   255	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/back.gif[39;49;00m[37m [39;49;00m..[37m[39;49;00m$
   256	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/hand.right.gif[39;49;00m[37m [39;49;00mREADME[37m[39;49;00m$
   257	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/folder.gif[39;49;00m[37m [39;49;00m^^DIRECTORY^^[37m[39;49;00m$
   258	[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/blank.gif[39;49;00m[37m [39;49;00m^^BLANKICON^^[37m[39;49;00m$
   259	[37m[39;49;00m$
   260	[37m[39;49;00m$
   261	[37m# This is from Matty J's patch. Anyone want to make the icons?[39;49;00m[37m[39;49;00m$
   262	[37m#AddIcon /icons/dirsymlink.jpg ^^SYMDIR^^[39;49;00m[37m[39;49;00m$
   263	[37m#AddIcon /icons/symlink.jpg ^^SYMLINK^^[39;49;00m[37m[39;49;00m$
   264	[37m[39;49;00m$
   265	[36mDefaultIcon[39;49;00m[37m [39;49;00m[33m/icons/unknown.gif[39;49;00m[37m[39;49;00m$
   266	[37m[39;49;00m$
   267	[36mReadmeName[39;49;00m[37m [39;49;00mREADME.html[37m[39;49;00m$
   268	[36mHeaderName[39;49;00m[37m [39;49;00mHEADER.html[37m[39;49;00m$
   269	[37m[39;49;00m$
   270	[36mIndexIgnore[39;49;00m[37m [39;49;00m.??*[37m [39;49;00m*~[37m [39;49;00m*#[37m [39;49;00mHEADER*[37m [39;49;00mRCS[37m [39;49;00mCVS[37m [39;49;00m*,t[37m[39;49;00m$
   271	[37m[39;49;00m$
   272	[36mAddEncoding[39;49;00m[37m [39;49;00mx-compress[37m [39;49;00mZ[37m[39;49;00m$
   273	[36mAddEncoding[39;49;00m[37m [39;49;00mx-gzip[37m [39;49;00mgz[37m [39;49;00mtgz[37m[39;49;00m$
   274	[37m[39;49;00m$
   275	[36mAddLanguage[39;49;00m[37m [39;49;00mda[37m [39;49;00m.dk[37m[39;49;00m$
   276	[36mAddLanguage[39;49;00m[37m [39;49;00mnl[37m [39;49;00m.nl[37m[39;49;00m$
   277	[36mAddLanguage[39;49;00m[37m [39;49;00men[37m [39;49;00m.en[37m[39;49;00m$
   278	[36mAddLanguage[39;49;00m[37m [39;49;00met[37m [39;49;00m.et[37m[39;49;00m$
   279	[36mAddLanguage[39;49;00m[37m [39;49;00mfr[37m [39;49;00m.fr[37m[39;49;00m$
   280	[36mAddLanguage[39;49;00m[37m [39;49;00mde[37m [39;49;00m.de[37m[39;49;00m$
   281	[36mAddLanguage[39;49;00m[37m [39;49;00mel[37m [39;49;00m.el[37m[39;49;00m$
   282	[36mAddLanguage[39;49;00m[37m [39;49;00mit[37m [39;49;00m.it[37m[39;49;00m$
   283	[36mAddLanguage[39;49;00m[37m [39;49;00mja[37m [39;49;00m.ja[37m[39;49;00m$
   284	[36mAddLanguage[39;49;00m[37m [39;49;00mpl[37m [39;49;00m.po[37m[39;49;00m$
   285	[36mAddLanguage[39;49;00m[37m [39;49;00mko[37m [39;49;00m.ko[37m[39;49;00m$
   286	[36mAddLanguage[39;49;00m[37m [39;49;00mpt[37m [39;49;00m.pt[37m[39;49;00m$
   287	[36mAddLanguage[39;49;00m[37m [39;49;00mno[37m [39;49;00m.no[37m[39;49;00m$
   288	[36mAddLanguage[39;49;00m[37m [39;49;00mpt-br[37m [39;49;00m.pt-br[37m[39;49;00m$
   289	[36mAddLanguage[39;49;00m[37m [39;49;00mltz[37m [39;49;00m.ltz[37m[39;49;00m$
   290	[36mAddLanguage[39;49;00m[37m [39;49;00mca[37m [39;49;00m.ca[37m[39;49;00m$
   291	[36mAddLanguage[39;49;00m[37m [39;49;00mes[37m [39;49;00m.es[37m[39;49;00m$
   292	[36mAddLanguage[39;49;00m[37m [39;49;00msv[37m [39;49;00m.se[37m[39;49;00m$
   293	[36mAddLanguage[39;49;00m[37m [39;49;00mcz[37m [39;49;00m.cz[37m[39;49;00m$
   294	[36mAddLanguage[39;49;00m[37m [39;49;00mru[37m [39;49;00m.ru[37m[39;49;00m$
   295	[36mAddLanguage[39;49;00m[37m [39;49;00mtw[37m [39;49;00m.tw[37m[39;49;00m$
   296	[36mAddLanguage[39;49;00m[37m [39;49;00mzh-tw[37m [39;49;00m.tw[37m[39;49;00m$
   297	[37m[39;49;00m$
   298	[36mLanguagePriority[39;49;00m[37m [39;49;00men[37m [39;49;00mda[37m [39;49;00mnl[37m [39;49;00met[37m [39;49;00mfr[37m [39;49;00mde[37m [39;49;00mel[37m [39;49;00mit[37m [39;49;00mja[37m [39;49;00mko[37m [39;49;00mno[37m [39;49;00mpl[37m [39;49;00mpt[37m [39;49;00mpt-br[37m [39;49;00mltz[37m [39;49;00mca[37m [39;49;00mes[37m [39;49;00msv[37m [39;49;00mtw[37m[39;49;00m$
   299	[37m[39;49;00m$
   300	[37m[39;49;00m$
   301	[37m#AddDefaultCharset	ISO-8859-1[39;49;00m[37m[39;49;00m$
   302	[37m[39;49;00m$
   303	[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-1[37m  [39;49;00m.iso8859-1[37m  [39;49;00m.latin1[37m[39;49;00m$
   304	[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-2[37m  [39;49;00m.iso8859-2[37m  [39;49;00m.latin2[37m [39;49;00m.cen[37m[39;49;00m$
   305	[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-3[37m  [39;49;00m.iso8859-3[37m  [39;49;00m.latin3[37m[39;49;00m$
   306	[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-4[37m  [39;49;00m.iso8859-4[37m  [39;49;00m.latin4[37m[39;49;00m$
   307	[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-5[37m  [39;49;00m.iso8859-5[37m  [39;49;00m.latin5[37m [39;49;00m.cyr[37m [39;49;00m.iso-ru[37m[39;49;00m$
   308	[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-6[37m  [39;49;00m.iso8859-6[37m  [39;49;00m.latin6[37m [39;49;00m.arb[37m[39;49;00m$
   309	[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-7[37m  [39;49;00m.iso8859-7[37m  [39;49;00m.latin7[37m [39;49;00m.grk[37m[39;49;00m$
   310	[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-8[37m  [39;49;00m.iso8859-8[37m  [39;49;00m.latin8[37m [39;49;00m.heb[37m	[39;49;00m[37m[39;49;00m$
   311	[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-9[37m  [39;49;00m.iso8859-9[37m  [39;49;00m.latin9[37m [39;49;00m.trk[37m[39;49;00m$
   312	[36mAddCharset[39;49;00m[37m [39;49;00mISO-2022-JP[37m [39;49;00m.iso2022-jp[37m [39;49;00m.jis[37m[39;49;00m$
   313	[36mAddCharset[39;49;00m[37m [39;49;00mISO-2022-KR[37m [39;49;00m.iso2022-kr[37m [39;49;00m.kis[37m[39;49;00m$
   314	[36mAddCharset[39;49;00m[37m [39;49;00mISO-2022-CN[37m [39;49;00m.iso2022-cn[37m [39;49;00m.cis[37m[39;49;00m$
   315	[36mAddCharset[39;49;00m[37m [39;49;00mBig5[37m        [39;49;00m.Big5[37m       [39;49;00m.big5[37m[39;49;00m$
   316	[37m# For russian, more than one charset is used (depends on client, mostly):[39;49;00m[37m[39;49;00m$
   317	[36mAddCharset[39;49;00m[37m [39;49;00mWINDOWS-1251[37m [39;49;00m.cp-1251[37m   [39;49;00m.win-1251[37m[39;49;00m$
   318	[36mAddCharset[39;49;00m[37m [39;49;00mCP866[37m       [39;49;00m.cp866[37m[39;49;00m$
   319	[36mAddCharset[39;49;00m[37m [39;49;00mKOI8-r[37m      [39;49;00m.koi8-r[37m [39;49;00m.koi8-ru[37m[39;49;00m$
   320	[36mAddCharset[39;49;00m[37m [39;49;00mKOI8-ru[37m     [39;49;00m.koi8-uk[37m [39;49;00m.ua[37m[39;49;00m$
   321	[36mAddCharset[39;49;00m[37m [39;49;00mISO-10646-UCS-2[37m [39;49;00m.ucs2[37m[39;49;00m$
   322	[36mAddCharset[39;49;00m[37m [39;49;00mISO-10646-UCS-4[37m [39;49;00m.ucs4[37m[39;49;00m$
   323	[36mAddCharset[39;49;00m[37m [39;49;00mUTF-8[37m       [39;49;00m.utf8[37m[39;49;00m$
   324	[37m[39;49;00m$
   325	[36mAddCharset[39;49;00m[37m [39;49;00mGB2312[37m      [39;49;00m.gb2312[37m [39;49;00m.gb[37m [39;49;00m[37m[39;49;00m$
   326	[36mAddCharset[39;49;00m[37m [39;49;00mutf-7[37m       [39;49;00m.utf7[37m[39;49;00m$
   327	[36mAddCharset[39;49;00m[37m [39;49;00mutf-8[37m       [39;49;00m.utf8[37m[39;49;00m$
   328	[36mAddCharset[39;49;00m[37m [39;49;00mbig5[37m	       [39;49;00m.big5[37m [39;49;00m.b5[37m[39;49;00m$
   329	[36mAddCharset[39;49;00m[37m [39;49;00mEUC-TW[37m      [39;49;00m.euc-tw[37m	[39;49;00m[37m[39;49;00m$
   330	[36mAddCharset[39;49;00m[37m [39;49;00mEUC-JP[37m      [39;49;00m.euc-jp[37m[39;49;00m$
   331	[36mAddCharset[39;49;00m[37m [39;49;00mEUC-KR[37m      [39;49;00m.euc-kr[37m[39;49;00m$
   332	[36mAddCharset[39;49;00m[37m [39;49;00mshift_jis[37m   [39;49;00m.sjis[37m[39;49;00m$
   333	[37m[39;49;00m$
   334	[37m#AddType application/x-httpd-php .php[39;49;00m[37m[39;49;00m$
   335	[37m#AddType application/x-httpd-php-source .phps[39;49;00m[37m[39;49;00m$
   336	[37m[39;49;00m$
   337	[36mAddType[39;49;00m[37m [39;49;00mapplication/x-tar[37m [39;49;00m.tgz[37m[39;49;00m$
   338	[37m[39;49;00m$
   339	[37m# To use CGI scripts outside /cgi-bin/:[39;49;00m[37m[39;49;00m$
   340	[37m#[39;49;00m[37m[39;49;00m$
   341	[37m#AddHandler cgi-script .cgi[39;49;00m[37m[39;49;00m$
   342	[37m[39;49;00m$
   343	[37m# To use server-parsed HTML files[39;49;00m[37m[39;49;00m$
   344	[37m#[39;49;00m[37m[39;49;00m$
   345	[94m<FilesMatch[39;49;00m[37m [39;49;00m[33m"\.shtml(\..+)?$"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   346	[37m    [39;49;00m[36mSetOutputFilter[39;49;00m[37m [39;49;00mINCLUDES[37m[39;49;00m$
   347	[94m</FilesMatch[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   348	[37m[39;49;00m$
   349	[37m# If you wish to use server-parsed imagemap files, use[39;49;00m[37m[39;49;00m$
   350	[37m#[39;49;00m[37m[39;49;00m$
   351	[37m#AddHandler imap-file map[39;49;00m[37m[39;49;00m$
   352	[37m[39;49;00m$
   353	[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"Mozilla/2"[39;49;00m[37m [39;49;00mnokeepalive[37m[39;49;00m$
   354	[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"MSIE 4\.0b2;"[39;49;00m[37m [39;49;00mnokeepalive[37m [39;49;00mdowngrade-1.0[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
   355	[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"RealPlayer 4\.0"[39;49;00m[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
   356	[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"Java/1\.0"[39;49;00m[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
   357	[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"JDK/1\.0"[39;49;00m[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
   358	[37m[39;49;00m$
   359	[37m#[39;49;00m[37m[39;49;00m$
   360	[37m# The following directive disables redirects on non-GET requests for[39;49;00m[37m[39;49;00m$
   361	[37m# a directory that does not include the trailing slash.  This fixes a [39;49;00m[37m[39;49;00m$
   362	[37m# problem with Microsoft WebFolders which does not appropriately handle [39;49;00m[37m[39;49;00m$
   363	[37m# redirects for folders with DAV methods.[39;49;00m[37m[39;49;00m$
   364	[37m#[39;49;00m[37m[39;49;00m$
   365	[37m[39;49;00m$
   366	[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"Microsoft Data Access Internet Publishing Provider"[39;49;00m[37m [39;49;00mredirect-carefully[37m[39;49;00m$
   367	[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"^WebDrive"[39;49;00m[37m [39;49;00mredirect-carefully[37m[39;49;00m$
   368	[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"^gnome-vfs"[39;49;00m[37m [39;49;00mredirect-carefully[37m [39;49;00m[37m[39;49;00m$
   369	[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"^WebDAVFS/1.[012]"[39;49;00m[37m [39;49;00mredirect-carefully[37m[39;49;00m$
   370	[37m[39;49;00m$
   371	[37m# Allow server status reports, with the URL of http://servername/server-status[39;49;00m[37m[39;49;00m$
   372	[37m# Change the ".your_domain.com" to match your domain to enable.[39;49;00m[37m[39;49;00m$
   373	[37m#[39;49;00m[37m[39;49;00m$
   374	[37m#<Location /server-status>[39;49;00m[37m[39;49;00m$
   375	[37m#    SetHandler server-status[39;49;00m[37m[39;49;00m$
   376	[37m#    Order deny,allow[39;49;00m[37m[39;49;00m$
   377	[37m#    Deny from all[39;49;00m[37m[39;49;00m$
   378	[37m#    Allow from .your_domain.com[39;49;00m[37m[39;49;00m$
   379	[37m#</Location>[39;49;00m[37m[39;49;00m$
   380	[37m[39;49;00m$
   381	[37m# Allow remote server configuration reports, with the URL of[39;49;00m[37m[39;49;00m$
   382	[37m#  http://servername/server-info (requires that mod_info.c be loaded).[39;49;00m[37m[39;49;00m$
   383	[37m# Change the ".your_domain.com" to match your domain to enable.[39;49;00m[37m[39;49;00m$
   384	[37m#[39;49;00m[37m[39;49;00m$
   385	[37m#<Location /server-info>[39;49;00m[37m[39;49;00m$
   386	[37m#    SetHandler server-info[39;49;00m[37m[39;49;00m$
   387	[37m#    Order deny,allow[39;49;00m[37m[39;49;00m$
   388	[37m#    Deny from all[39;49;00m[37m[39;49;00m$
   389	[37m#    Allow from .your_domain.com[39;49;00m[37m[39;49;00m$
   390	[37m#</Location>[39;49;00m[37m[39;49;00m$
   391	[37m[39;49;00m$
   392	[37m# Include the virtual host configurations:[39;49;00m[37m[39;49;00m$
   393	[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/sites-enabled/[39;49;00m[^.#]*[37m[39;49;00m$
   394	[37m[39;49;00m$
   395	[37m# From PR#766[39;49;00m[37m[39;49;00m$
   396	[94m<IfVersion[39;49;00m[37m [39;49;00m[33m>= 2.4[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
   397	[36mErrorLogFormat[39;49;00m[37m [39;49;00m[33m"%{cu}t %M"[39;49;00m[37m[39;49;00m$
   398	[94m</IfVersion[39;49;00m[94m>[39;49;00m$
