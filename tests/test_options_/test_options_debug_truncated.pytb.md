Using lexer <pygments.lexers.PythonTracebackLexer with {'ensurenl': False, 'tabsize': 0}>
  File [36m"/usr/lib/python2.3/site-packages/trac/web/main.py"[39;49;00m, line [34m314[39;49;00m, in dispatch_request
    dispatcher.dispatch(req)
  File [36m"/usr/lib/python2.3/site-packages/trac/web/main.py"[39;49;00m, line [34m186[39;49;00m, in dispatch
    req.session = Session([36mself[39;49;00m.env, req)
  File [36m"/usr/lib/python2.3/site-packages/trac/web/session.py"[39;49;00m, line [34m52[39;49;00m, in __init__
    [36mself[39;49;00m.promote_session(sid)
  File [36m"/usr/lib/python2.3/site-packages/trac/web/session.py"[39;49;00m, line [34m125[39;49;00m, in promote_session
    [33m"[39;49;00m[33mAND authenticated=0[39;49;00m[33m"[39;49;00m, (sid,))
  File [36m"/usr/lib/python2.3/site-packages/trac/db/util.py"[39;49;00m, line [34m47[39;49;00m, in execute
    [34mreturn[39;49;00m [36mself[39;49;00m.cursor.execute(sql_escape_percent(sql), args)
  File [36m"/usr/lib/python2.3/site-packages/trac/db/sqlite_backend.py"[39;49;00m, line [34m44[39;49;00m, in execute
    args [35mor[39;49;00m [])
  File [36m"/usr/lib/python2.3/site-packages/trac/db/sqlite_backend.py"[39;49;00m, line [34m36[39;49;00m, in _rollback_on_error
    [34mreturn[39;49;00m function([36mself[39;49;00m, *args, **kwargs)
[04m[91mO[39;49;00m[04m[91mp[39;49;00m[04m[91me[39;49;00m[04m[91mr[39;49;00m[04m[91ma[39;49;00m[04m[91mt[39;49;00m[04m[91mi[39;49;00m[04m[91mo[39;49;00m[04m[91mn[39;49;00m[04m[91ma[39;49;00m[04m[91ml[39;49;00m[04m[91mE[39;49;00m[04m[91mr[39;49;00m[04m[91mr[39;49;00m[04m[91mo[39;49;00m[04m[91mr[39;49;00m[04m[91m:[39;49;00m[04m[91m [39;49;00m[04m[91md[39;49;00m[04m[91ma[39;49;00m[04m[91mt[39;49;00m[04m[91ma[39;49;00m[04m[91mb[39;49;00m[04m[91ma[39;49;00m[04m[91ms[39;49;00m[04m[91me[39;49;00m[04m[91m [39;49;00m[04m[91mi[39;49;00m[04m[91ms[39;49;00m[04m[91m [39;49;00m[04m[91ml[39;49;00m[04m[91mo[39;49;00m[04m[91mc[39;49;00m[04m[91mk[39;49;00m[04m[91me[39;49;00m[04m[91md[39;49;00m
