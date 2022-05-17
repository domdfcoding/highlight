Text before$
$
Traceback (most recent call last):$
  File [36m"/usr/lib/python2.3/site-packages/trac/web/main.py"[39;49;00m, line [34m314[39;49;00m, in dispatch_request$
    dispatcher.dispatch(req)$
  File [36m"/usr/lib/python2.3/site-packages/trac/web/main.py"[39;49;00m, line [34m186[39;49;00m, in dispatch$
    req.session = Session([36mself[39;49;00m.env, req)$
  File [36m"/usr/lib/python2.3/site-packages/trac/web/session.py"[39;49;00m, line [34m52[39;49;00m, in __init__$
    [36mself[39;49;00m.promote_session(sid)$
  File [36m"/usr/lib/python2.3/site-packages/trac/web/session.py"[39;49;00m, line [34m125[39;49;00m, in promote_session$
    [33m"[39;49;00m[33mAND authenticated=0[39;49;00m[33m"[39;49;00m, (sid,))$
  File [36m"/usr/lib/python2.3/site-packages/trac/db/util.py"[39;49;00m, line [34m47[39;49;00m, in execute$
    [34mreturn[39;49;00m [36mself[39;49;00m.cursor.execute(sql_escape_percent(sql), args)$
  File [36m"/usr/lib/python2.3/site-packages/trac/db/sqlite_backend.py"[39;49;00m, line [34m44[39;49;00m, in execute$
    args [35mor[39;49;00m [])$
  File [36m"/usr/lib/python2.3/site-packages/trac/db/sqlite_backend.py"[39;49;00m, line [34m36[39;49;00m, in _rollback_on_error$
    [34mreturn[39;49;00m function([36mself[39;49;00m, *args, **kwargs)$
[91mOperationalError[39;49;00m: database is locked$
$
[04m[91mT[39;49;00m[04m[91me[39;49;00m[04m[91mx[39;49;00m[04m[91mt[39;49;00m[04m[91m [39;49;00m[04m[91ma[39;49;00m[04m[91mf[39;49;00m[04m[91mt[39;49;00m[04m[91me[39;49;00m[04m[91mr[39;49;00m$
