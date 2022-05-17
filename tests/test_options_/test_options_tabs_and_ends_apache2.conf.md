[37m# Based upon the NCSA server configuration files originally by Rob McCool.[39;49;00m[37m[39;49;00m$
[37m# Changed extensively for the Debian package by Daniel Stone <daniel@sfarc.net>[39;49;00m[37m[39;49;00m$
[37m# and also by Thom May <thom@debian.org>.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# ServerRoot: The top of the directory tree under which the server's[39;49;00m[37m[39;49;00m$
[37m# configuration, error, and log files are kept.[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m# NOTE!  If you intend to place this on an NFS (or otherwise network)[39;49;00m[37m[39;49;00m$
[37m# mounted filesystem then please read the LockFile documentation[39;49;00m[37m[39;49;00m$
[37m# (available at <URL:http://www.apache.org/docs/mod/core.html#lockfile>);[39;49;00m[37m[39;49;00m$
[37m# you will save yourself a lot of trouble.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mServerRoot[39;49;00m[37m [39;49;00m[33m"/etc/apache2"[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# The LockFile directive sets the path to the lockfile used when Apache[39;49;00m[37m[39;49;00m$
[37m# is compiled with either USE_FCNTL_SERIALIZED_ACCEPT or[39;49;00m[37m[39;49;00m$
[37m# USE_FLOCK_SERIALIZED_ACCEPT. This directive should normally be left at[39;49;00m[37m[39;49;00m$
[37m# its default value. The main reason for changing it is if the logs[39;49;00m[37m[39;49;00m$
[37m# directory is NFS mounted, since the lockfile MUST BE STORED ON A LOCAL[39;49;00m[37m[39;49;00m$
[37m# DISK. The PID of the main server process is automatically appended to[39;49;00m[37m[39;49;00m$
[37m# the filename. [39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mLockFile[39;49;00m[37m [39;49;00m[33m/var/lock/apache2/accept.lock[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# PidFile: The file in which the server should record its process[39;49;00m[37m[39;49;00m$
[37m# identification number when it starts.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mPidFile[39;49;00m[37m [39;49;00m[33m/var/run/apache2.pid[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# Timeout: The number of seconds before receives and sends time out.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mTimeout[39;49;00m[37m [39;49;00m[34m300[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# KeepAlive: Whether or not to allow persistent connections (more than[39;49;00m[37m[39;49;00m$
[37m# one request per connection). Set to "Off" to deactivate.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mKeepAlive[39;49;00m[37m [39;49;00m[34mOn[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# MaxKeepAliveRequests: The maximum number of requests to allow[39;49;00m[37m[39;49;00m$
[37m# during a persistent connection. Set to 0 to allow an unlimited amount.[39;49;00m[37m[39;49;00m$
[37m# We recommend you leave this number high, for maximum performance.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mMaxKeepAliveRequests[39;49;00m[37m [39;49;00m[34m100[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# KeepAliveTimeout: Number of seconds to wait for the next request from the[39;49;00m[37m[39;49;00m$
[37m# same client on the same connection.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mKeepAliveTimeout[39;49;00m[37m [39;49;00m[34m15[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m##[39;49;00m[37m[39;49;00m$
[37m## Server-Pool Size Regulation (MPM specific)[39;49;00m[37m[39;49;00m$
[37m## [39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# prefork MPM[39;49;00m[37m[39;49;00m$
[37m# StartServers ......... number of server processes to start[39;49;00m[37m[39;49;00m$
[37m# MinSpareServers ...... minimum number of server processes which are kept spare[39;49;00m[37m[39;49;00m$
[37m# MaxSpareServers ...... maximum number of server processes which are kept spare[39;49;00m[37m[39;49;00m$
[37m# MaxClients ........... maximum number of server processes allowed to start[39;49;00m[37m[39;49;00m$
[37m# MaxRequestsPerChild .. maximum number of requests a server process serves[39;49;00m[37m[39;49;00m$
[94m<IfModule[39;49;00m[37m [39;49;00m[33mprefork.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[36mStartServers[39;49;00m[37m         [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
[36mMinSpareServers[39;49;00m[37m      [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
[36mMaxSpareServers[39;49;00m[37m     [39;49;00m[34m10[39;49;00m[37m[39;49;00m$
[36mMaxClients[39;49;00m[37m          [39;49;00m[34m20[39;49;00m[37m[39;49;00m$
[36mMaxRequestsPerChild[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# pthread MPM[39;49;00m[37m[39;49;00m$
[37m# StartServers ......... initial  number of server processes to start[39;49;00m[37m[39;49;00m$
[37m# MaxClients ........... maximum  number of server processes allowed to start[39;49;00m[37m[39;49;00m$
[37m# MinSpareThreads ...... minimum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
[37m# MaxSpareThreads ...... maximum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
[37m# ThreadsPerChild ...... constant number of worker threads in each server process[39;49;00m[37m[39;49;00m$
[37m# MaxRequestsPerChild .. maximum  number of requests a server process serves[39;49;00m[37m[39;49;00m$
[94m<IfModule[39;49;00m[37m [39;49;00m[33mworker.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[36mStartServers[39;49;00m[37m         [39;49;00m[34m2[39;49;00m[37m[39;49;00m$
[36mMaxClients[39;49;00m[37m         [39;49;00m[34m150[39;49;00m[37m [39;49;00m[37m[39;49;00m$
[36mMinSpareThreads[39;49;00m[37m     [39;49;00m[34m25[39;49;00m[37m[39;49;00m$
[36mMaxSpareThreads[39;49;00m[37m     [39;49;00m[34m75[39;49;00m[37m[39;49;00m$
[36mThreadsPerChild[39;49;00m[37m     [39;49;00m[34m25[39;49;00m[37m[39;49;00m$
[36mMaxRequestsPerChild[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# perchild MPM[39;49;00m[37m[39;49;00m$
[37m# NumServers ........... constant number of server processes[39;49;00m[37m[39;49;00m$
[37m# StartThreads ......... initial  number of worker threads in each server process[39;49;00m[37m[39;49;00m$
[37m# MinSpareThreads ...... minimum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
[37m# MaxSpareThreads ...... maximum  number of worker threads which are kept spare[39;49;00m[37m[39;49;00m$
[37m# MaxThreadsPerChild ... maximum  number of worker threads in each server process[39;49;00m[37m[39;49;00m$
[37m# MaxRequestsPerChild .. maximum  number of connections per server process (then it dies)[39;49;00m[37m[39;49;00m$
[94m<IfModule[39;49;00m[37m [39;49;00m[33mperchild.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[36mNumServers[39;49;00m[37m           [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
[36mStartThreads[39;49;00m[37m         [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
[36mMinSpareThreads[39;49;00m[37m      [39;49;00m[34m5[39;49;00m[37m[39;49;00m$
[36mMaxSpareThreads[39;49;00m[37m     [39;49;00m[34m10[39;49;00m[37m[39;49;00m$
[36mMaxThreadsPerChild[39;49;00m[37m  [39;49;00m[34m20[39;49;00m[37m[39;49;00m$
[36mMaxRequestsPerChild[39;49;00m[37m  [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
[36mAcceptMutex[39;49;00m[37m [39;49;00mfcntl[37m[39;49;00m$
[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mUser[39;49;00m[37m [39;49;00mwww-data[37m[39;49;00m$
[36mGroup[39;49;00m[37m [39;49;00mwww-data[37m[39;49;00m$
[37m[39;49;00m$
[37m# The following directives define some format nicknames for use with[39;49;00m[37m[39;49;00m$
[37m# a CustomLog directive (see below).[39;49;00m[37m[39;49;00m$
[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\""[39;49;00m[37m [39;49;00mcombined[37m[39;49;00m$
[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%h %l %u %t \"%r\" %>s %b"[39;49;00m[37m [39;49;00mcommon[37m[39;49;00m$
[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%{Referer}i -> %U"[39;49;00m[37m [39;49;00mreferer[37m[39;49;00m$
[36mLogFormat[39;49;00m[37m [39;49;00m[33m"%{User-agent}i"[39;49;00m[37m [39;49;00magent[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m# Global error log.[39;49;00m[37m[39;49;00m$
[36mErrorLog[39;49;00m[37m [39;49;00m[33m/var/log/apache2/error.log[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# Include module configuration:[39;49;00m[37m[39;49;00m$
[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/mods-enabled/*.load[39;49;00m[37m[39;49;00m$
[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/mods-enabled/*.conf[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# Include all the user configurations:[39;49;00m[37m[39;49;00m$
[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/httpd.conf[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# Include ports listing[39;49;00m[37m[39;49;00m$
[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/ports.conf[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# Include generic snippets of statements[39;49;00m[37m[39;49;00m$
[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/conf.d/[39;49;00m[^.#]*[37m[39;49;00m$
[37m[39;49;00m$
[37m#Let's have some Icons, shall we?[39;49;00m[37m[39;49;00m$
[36mAlias[39;49;00m[37m [39;49;00m[33m/icons/[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/icons/"[39;49;00m[37m[39;49;00m$
[94m<Directory[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/icons"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mOptions[39;49;00m[37m [39;49;00mIndexes[37m [39;49;00mMultiViews[37m[39;49;00m$
[37m    [39;49;00m[36mAllowOverride[39;49;00m[37m [39;49;00m[34mNone[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mOrder[39;49;00m[37m [39;49;00mallow,deny[37m[39;49;00m$
[37m    [39;49;00m[36mAllow[39;49;00m[37m [39;49;00mfrom[37m [39;49;00m[34mall[39;49;00m[37m[39;49;00m$
[94m</Directory[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# Set up the default error docs.[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m# Customizable error responses come in three flavors:[39;49;00m[37m[39;49;00m$
[37m# 1) plain text 2) local redirects 3) external redirects[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m# Some examples:[39;49;00m[37m[39;49;00m$
[37m#ErrorDocument 500 "The server made a boo boo."[39;49;00m[37m[39;49;00m$
[37m#ErrorDocument 404 /missing.html[39;49;00m[37m[39;49;00m$
[37m#ErrorDocument 404 "/cgi-bin/missing_handler.pl"[39;49;00m[37m[39;49;00m$
[37m#ErrorDocument 402 http://www.example.com/subscription_info.html[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m# Putting this all together, we can Internationalize error responses.[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m# We use Alias to redirect any /error/HTTP_<error>.html.var response to[39;49;00m[37m[39;49;00m$
[37m# our collection of by-error message multi-language collections.  We use [39;49;00m[37m[39;49;00m$
[37m# includes to substitute the appropriate text.[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m# You can modify the messages' appearance without changing any of the[39;49;00m[37m[39;49;00m$
[37m# default HTTP_<error>.html.var files by adding the line;[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m#   Alias /error/include/ "/your/include/path/"[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m# which allows you to create your own set of files by starting with the[39;49;00m[37m[39;49;00m$
[37m# /usr/local/apache2/error/include/ files and[39;49;00m[37m[39;49;00m$
[37m# copying them to /your/include/path/, even on a per-VirtualHost basis.[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[94m<IfModule[39;49;00m[37m [39;49;00m[33mmod_negotiation.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[94m<IfModule[39;49;00m[37m [39;49;00m[33mmod_include.c[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mAlias[39;49;00m[37m [39;49;00m[33m/error/[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/error/"[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[94m<Directory[39;49;00m[37m [39;49;00m[33m"/usr/share/apache2/error"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m[36mAllowOverride[39;49;00m[37m [39;49;00m[34mNone[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m[36mOptions[39;49;00m[37m [39;49;00mIncludesNoExec[37m[39;49;00m$
[37m        [39;49;00m[36mAddOutputFilter[39;49;00m[37m [39;49;00mIncludes[37m [39;49;00mhtml[37m[39;49;00m$
[37m        [39;49;00m[36mAddHandler[39;49;00m[37m [39;49;00mtype-map[37m [39;49;00mvar[37m[39;49;00m$
[37m        [39;49;00m[36mOrder[39;49;00m[37m [39;49;00mallow,deny[37m[39;49;00m$
[37m        [39;49;00m[36mAllow[39;49;00m[37m [39;49;00mfrom[37m [39;49;00m[34mall[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m[36mLanguagePriority[39;49;00m[37m [39;49;00men[37m [39;49;00mes[37m [39;49;00mde[37m [39;49;00mfr[37m[39;49;00m$
[37m        [39;49;00m[36mForceLanguagePriority[39;49;00m[37m [39;49;00mPrefer[37m [39;49;00mFallback[37m[39;49;00m$
[37m    [39;49;00m[94m</Directory[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m400[39;49;00m[37m [39;49;00m[33m/error/HTTP_BAD_REQUEST.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m401[39;49;00m[37m [39;49;00m[33m/error/HTTP_UNAUTHORIZED.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m403[39;49;00m[37m [39;49;00m[33m/error/HTTP_FORBIDDEN.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m404[39;49;00m[37m [39;49;00m[33m/error/HTTP_NOT_FOUND.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m405[39;49;00m[37m [39;49;00m[33m/error/HTTP_METHOD_NOT_ALLOWED.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m408[39;49;00m[37m [39;49;00m[33m/error/HTTP_REQUEST_TIME_OUT.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m410[39;49;00m[37m [39;49;00m[33m/error/HTTP_GONE.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m411[39;49;00m[37m [39;49;00m[33m/error/HTTP_LENGTH_REQUIRED.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m412[39;49;00m[37m [39;49;00m[33m/error/HTTP_PRECONDITION_FAILED.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m413[39;49;00m[37m [39;49;00m[33m/error/HTTP_REQUEST_ENTITY_TOO_LARGE.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m414[39;49;00m[37m [39;49;00m[33m/error/HTTP_REQUEST_URI_TOO_LARGE.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m415[39;49;00m[37m [39;49;00m[33m/error/HTTP_SERVICE_UNAVAILABLE.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m500[39;49;00m[37m [39;49;00m[33m/error/HTTP_INTERNAL_SERVER_ERROR.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m501[39;49;00m[37m [39;49;00m[33m/error/HTTP_NOT_IMPLEMENTED.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m502[39;49;00m[37m [39;49;00m[33m/error/HTTP_BAD_GATEWAY.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m503[39;49;00m[37m [39;49;00m[33m/error/HTTP_SERVICE_UNAVAILABLE.html.var[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mErrorDocument[39;49;00m[37m [39;49;00m[34m506[39;49;00m[37m [39;49;00m[33m/error/HTTP_VARIANT_ALSO_VARIES.html.var[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[94m</IfModule[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mDirectoryIndex[39;49;00m[37m [39;49;00mindex.html[37m [39;49;00mindex.cgi[37m [39;49;00mindex.pl[37m [39;49;00mindex.php[37m [39;49;00mindex.xhtml[37m[39;49;00m$
[37m[39;49;00m$
[37m# UserDir is now a module[39;49;00m[37m[39;49;00m$
[37m#UserDir public_html[39;49;00m[37m[39;49;00m$
[37m#UserDir disabled root[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m#<Directory /home/*/public_html>[39;49;00m[37m[39;49;00m$
[37m#^IAllowOverride FileInfo AuthConfig Limit[39;49;00m[37m[39;49;00m$
[37m#^IOptions Indexes SymLinksIfOwnerMatch IncludesNoExec[39;49;00m[37m[39;49;00m$
[37m#</Directory>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mAccessFileName[39;49;00m[37m [39;49;00m.htaccess[37m[39;49;00m$
[37m[39;49;00m$
[94m<Files[39;49;00m[37m [39;49;00m[33m~ "^\.ht"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mOrder[39;49;00m[37m [39;49;00mallow,deny[37m[39;49;00m$
[37m    [39;49;00m[36mDeny[39;49;00m[37m [39;49;00mfrom[37m [39;49;00m[34mall[39;49;00m[37m[39;49;00m$
[94m</Files[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mUseCanonicalName[39;49;00m[37m [39;49;00m[34mOff[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mTypesConfig[39;49;00m[37m [39;49;00m[33m/etc/mime.types[39;49;00m[37m[39;49;00m$
[36mDefaultType[39;49;00m[37m [39;49;00mtext/plain[37m[39;49;00m$
[37m[39;49;00m$
[36mHostnameLookups[39;49;00m[37m [39;49;00m[34mOff[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mIndexOptions[39;49;00m[37m [39;49;00mFancyIndexing[37m [39;49;00mVersionSort[37m[39;49;00m$
[37m[39;49;00m$
[36mAddIconByEncoding[39;49;00m[37m [39;49;00m(CMP,/icons/compressed.gif)[37m [39;49;00mx-compress[37m [39;49;00mx-gzip[37m[39;49;00m$
[37m[39;49;00m$
[36mAddIconByType[39;49;00m[37m [39;49;00m(TXT,/icons/text.gif)[37m [39;49;00mtext/*[37m[39;49;00m$
[36mAddIconByType[39;49;00m[37m [39;49;00m(IMG,/icons/image2.gif)[37m [39;49;00mimage/*[37m[39;49;00m$
[36mAddIconByType[39;49;00m[37m [39;49;00m(SND,/icons/sound2.gif)[37m [39;49;00maudio/*[37m[39;49;00m$
[36mAddIconByType[39;49;00m[37m [39;49;00m(VID,/icons/movie.gif)[37m [39;49;00mvideo/*[37m[39;49;00m$
[37m[39;49;00m$
[37m# This really should be .jpg.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/binary.gif[39;49;00m[37m [39;49;00m.bin[37m [39;49;00m.exe[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/binhex.gif[39;49;00m[37m [39;49;00m.hqx[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/tar.gif[39;49;00m[37m [39;49;00m.tar[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/world2.gif[39;49;00m[37m [39;49;00m.wrl[37m [39;49;00m.wrl.gz[37m [39;49;00m.vrml[37m [39;49;00m.vrm[37m [39;49;00m.iv[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/compressed.gif[39;49;00m[37m [39;49;00m.Z[37m [39;49;00m.z[37m [39;49;00m.tgz[37m [39;49;00m.gz[37m [39;49;00m.zip[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/a.gif[39;49;00m[37m [39;49;00m.ps[37m [39;49;00m.ai[37m [39;49;00m.eps[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/layout.gif[39;49;00m[37m [39;49;00m.html[37m [39;49;00m.shtml[37m [39;49;00m.htm[37m [39;49;00m.pdf[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/text.gif[39;49;00m[37m [39;49;00m.txt[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/c.gif[39;49;00m[37m [39;49;00m.c[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/p.gif[39;49;00m[37m [39;49;00m.pl[37m [39;49;00m.py[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/f.gif[39;49;00m[37m [39;49;00m.for[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/dvi.gif[39;49;00m[37m [39;49;00m.dvi[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/uuencoded.gif[39;49;00m[37m [39;49;00m.uu[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/script.gif[39;49;00m[37m [39;49;00m.conf[37m [39;49;00m.sh[37m [39;49;00m.shar[37m [39;49;00m.csh[37m [39;49;00m.ksh[37m [39;49;00m.tcl[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/tex.gif[39;49;00m[37m [39;49;00m.tex[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/bomb.gif[39;49;00m[37m [39;49;00mcore[37m[39;49;00m$
[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/back.gif[39;49;00m[37m [39;49;00m..[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/hand.right.gif[39;49;00m[37m [39;49;00mREADME[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/folder.gif[39;49;00m[37m [39;49;00m^^DIRECTORY^^[37m[39;49;00m$
[36mAddIcon[39;49;00m[37m [39;49;00m[33m/icons/blank.gif[39;49;00m[37m [39;49;00m^^BLANKICON^^[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m# This is from Matty J's patch. Anyone want to make the icons?[39;49;00m[37m[39;49;00m$
[37m#AddIcon /icons/dirsymlink.jpg ^^SYMDIR^^[39;49;00m[37m[39;49;00m$
[37m#AddIcon /icons/symlink.jpg ^^SYMLINK^^[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mDefaultIcon[39;49;00m[37m [39;49;00m[33m/icons/unknown.gif[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mReadmeName[39;49;00m[37m [39;49;00mREADME.html[37m[39;49;00m$
[36mHeaderName[39;49;00m[37m [39;49;00mHEADER.html[37m[39;49;00m$
[37m[39;49;00m$
[36mIndexIgnore[39;49;00m[37m [39;49;00m.??*[37m [39;49;00m*~[37m [39;49;00m*#[37m [39;49;00mHEADER*[37m [39;49;00mRCS[37m [39;49;00mCVS[37m [39;49;00m*,t[37m[39;49;00m$
[37m[39;49;00m$
[36mAddEncoding[39;49;00m[37m [39;49;00mx-compress[37m [39;49;00mZ[37m[39;49;00m$
[36mAddEncoding[39;49;00m[37m [39;49;00mx-gzip[37m [39;49;00mgz[37m [39;49;00mtgz[37m[39;49;00m$
[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mda[37m [39;49;00m.dk[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mnl[37m [39;49;00m.nl[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00men[37m [39;49;00m.en[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00met[37m [39;49;00m.et[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mfr[37m [39;49;00m.fr[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mde[37m [39;49;00m.de[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mel[37m [39;49;00m.el[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mit[37m [39;49;00m.it[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mja[37m [39;49;00m.ja[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mpl[37m [39;49;00m.po[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mko[37m [39;49;00m.ko[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mpt[37m [39;49;00m.pt[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mno[37m [39;49;00m.no[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mpt-br[37m [39;49;00m.pt-br[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mltz[37m [39;49;00m.ltz[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mca[37m [39;49;00m.ca[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mes[37m [39;49;00m.es[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00msv[37m [39;49;00m.se[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mcz[37m [39;49;00m.cz[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mru[37m [39;49;00m.ru[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mtw[37m [39;49;00m.tw[37m[39;49;00m$
[36mAddLanguage[39;49;00m[37m [39;49;00mzh-tw[37m [39;49;00m.tw[37m[39;49;00m$
[37m[39;49;00m$
[36mLanguagePriority[39;49;00m[37m [39;49;00men[37m [39;49;00mda[37m [39;49;00mnl[37m [39;49;00met[37m [39;49;00mfr[37m [39;49;00mde[37m [39;49;00mel[37m [39;49;00mit[37m [39;49;00mja[37m [39;49;00mko[37m [39;49;00mno[37m [39;49;00mpl[37m [39;49;00mpt[37m [39;49;00mpt-br[37m [39;49;00mltz[37m [39;49;00mca[37m [39;49;00mes[37m [39;49;00msv[37m [39;49;00mtw[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m#AddDefaultCharset^IISO-8859-1[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-1[37m  [39;49;00m.iso8859-1[37m  [39;49;00m.latin1[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-2[37m  [39;49;00m.iso8859-2[37m  [39;49;00m.latin2[37m [39;49;00m.cen[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-3[37m  [39;49;00m.iso8859-3[37m  [39;49;00m.latin3[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-4[37m  [39;49;00m.iso8859-4[37m  [39;49;00m.latin4[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-5[37m  [39;49;00m.iso8859-5[37m  [39;49;00m.latin5[37m [39;49;00m.cyr[37m [39;49;00m.iso-ru[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-6[37m  [39;49;00m.iso8859-6[37m  [39;49;00m.latin6[37m [39;49;00m.arb[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-7[37m  [39;49;00m.iso8859-7[37m  [39;49;00m.latin7[37m [39;49;00m.grk[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-8[37m  [39;49;00m.iso8859-8[37m  [39;49;00m.latin8[37m [39;49;00m.heb[37m^I[39;49;00m[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-8859-9[37m  [39;49;00m.iso8859-9[37m  [39;49;00m.latin9[37m [39;49;00m.trk[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-2022-JP[37m [39;49;00m.iso2022-jp[37m [39;49;00m.jis[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-2022-KR[37m [39;49;00m.iso2022-kr[37m [39;49;00m.kis[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-2022-CN[37m [39;49;00m.iso2022-cn[37m [39;49;00m.cis[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mBig5[37m        [39;49;00m.Big5[37m       [39;49;00m.big5[37m[39;49;00m$
[37m# For russian, more than one charset is used (depends on client, mostly):[39;49;00m[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mWINDOWS-1251[37m [39;49;00m.cp-1251[37m   [39;49;00m.win-1251[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mCP866[37m       [39;49;00m.cp866[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mKOI8-r[37m      [39;49;00m.koi8-r[37m [39;49;00m.koi8-ru[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mKOI8-ru[37m     [39;49;00m.koi8-uk[37m [39;49;00m.ua[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-10646-UCS-2[37m [39;49;00m.ucs2[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mISO-10646-UCS-4[37m [39;49;00m.ucs4[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mUTF-8[37m       [39;49;00m.utf8[37m[39;49;00m$
[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mGB2312[37m      [39;49;00m.gb2312[37m [39;49;00m.gb[37m [39;49;00m[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mutf-7[37m       [39;49;00m.utf7[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mutf-8[37m       [39;49;00m.utf8[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mbig5[37m^I       [39;49;00m.big5[37m [39;49;00m.b5[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mEUC-TW[37m      [39;49;00m.euc-tw[37m^I[39;49;00m[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mEUC-JP[37m      [39;49;00m.euc-jp[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mEUC-KR[37m      [39;49;00m.euc-kr[37m[39;49;00m$
[36mAddCharset[39;49;00m[37m [39;49;00mshift_jis[37m   [39;49;00m.sjis[37m[39;49;00m$
[37m[39;49;00m$
[37m#AddType application/x-httpd-php .php[39;49;00m[37m[39;49;00m$
[37m#AddType application/x-httpd-php-source .phps[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mAddType[39;49;00m[37m [39;49;00mapplication/x-tar[37m [39;49;00m.tgz[37m[39;49;00m$
[37m[39;49;00m$
[37m# To use CGI scripts outside /cgi-bin/:[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m#AddHandler cgi-script .cgi[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# To use server-parsed HTML files[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[94m<FilesMatch[39;49;00m[37m [39;49;00m[33m"\.shtml(\..+)?$"[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mSetOutputFilter[39;49;00m[37m [39;49;00mINCLUDES[37m[39;49;00m$
[94m</FilesMatch[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# If you wish to use server-parsed imagemap files, use[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m#AddHandler imap-file map[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"Mozilla/2"[39;49;00m[37m [39;49;00mnokeepalive[37m[39;49;00m$
[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"MSIE 4\.0b2;"[39;49;00m[37m [39;49;00mnokeepalive[37m [39;49;00mdowngrade-1.0[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"RealPlayer 4\.0"[39;49;00m[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"Java/1\.0"[39;49;00m[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"JDK/1\.0"[39;49;00m[37m [39;49;00mforce-response-1.0[37m[39;49;00m$
[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m# The following directive disables redirects on non-GET requests for[39;49;00m[37m[39;49;00m$
[37m# a directory that does not include the trailing slash.  This fixes a [39;49;00m[37m[39;49;00m$
[37m# problem with Microsoft WebFolders which does not appropriately handle [39;49;00m[37m[39;49;00m$
[37m# redirects for folders with DAV methods.[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"Microsoft Data Access Internet Publishing Provider"[39;49;00m[37m [39;49;00mredirect-carefully[37m[39;49;00m$
[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"^WebDrive"[39;49;00m[37m [39;49;00mredirect-carefully[37m[39;49;00m$
[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"^gnome-vfs"[39;49;00m[37m [39;49;00mredirect-carefully[37m [39;49;00m[37m[39;49;00m$
[36mBrowserMatch[39;49;00m[37m [39;49;00m[33m"^WebDAVFS/1.[012]"[39;49;00m[37m [39;49;00mredirect-carefully[37m[39;49;00m$
[37m[39;49;00m$
[37m# Allow server status reports, with the URL of http://servername/server-status[39;49;00m[37m[39;49;00m$
[37m# Change the ".your_domain.com" to match your domain to enable.[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m#<Location /server-status>[39;49;00m[37m[39;49;00m$
[37m#    SetHandler server-status[39;49;00m[37m[39;49;00m$
[37m#    Order deny,allow[39;49;00m[37m[39;49;00m$
[37m#    Deny from all[39;49;00m[37m[39;49;00m$
[37m#    Allow from .your_domain.com[39;49;00m[37m[39;49;00m$
[37m#</Location>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# Allow remote server configuration reports, with the URL of[39;49;00m[37m[39;49;00m$
[37m#  http://servername/server-info (requires that mod_info.c be loaded).[39;49;00m[37m[39;49;00m$
[37m# Change the ".your_domain.com" to match your domain to enable.[39;49;00m[37m[39;49;00m$
[37m#[39;49;00m[37m[39;49;00m$
[37m#<Location /server-info>[39;49;00m[37m[39;49;00m$
[37m#    SetHandler server-info[39;49;00m[37m[39;49;00m$
[37m#    Order deny,allow[39;49;00m[37m[39;49;00m$
[37m#    Deny from all[39;49;00m[37m[39;49;00m$
[37m#    Allow from .your_domain.com[39;49;00m[37m[39;49;00m$
[37m#</Location>[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m# Include the virtual host configurations:[39;49;00m[37m[39;49;00m$
[36mInclude[39;49;00m[37m [39;49;00m[33m/etc/apache2/sites-enabled/[39;49;00m[^.#]*[37m[39;49;00m$
[37m[39;49;00m$
[37m# From PR#766[39;49;00m[37m[39;49;00m$
[94m<IfVersion[39;49;00m[37m [39;49;00m[33m>= 2.4[39;49;00m[94m>[39;49;00m[37m[39;49;00m$
[36mErrorLogFormat[39;49;00m[37m [39;49;00m[33m"%{cu}t %M"[39;49;00m[37m[39;49;00m$
[94m</IfVersion[39;49;00m[94m>[39;49;00m$
