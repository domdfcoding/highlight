     1	[37m# Server: ruby p2p.rb password server server-uri merge-servers[39;49;00m$
     2	[37m# Sample: ruby p2p.rb foobar server druby://localhost:1337 druby://foo.bar:1337[39;49;00m$
     3	[37m# Client: ruby p2p.rb password client server-uri download-pattern[39;49;00m$
     4	[37m# Sample: ruby p2p.rb foobar client druby://localhost:1337 *.rb[39;49;00m$
     5	[36mrequire[39;49;00m[33m'[39;49;00m[33mdrb[39;49;00m[33m'[39;49;00m;F,D,C,P,M,U,*O=[31mFile[39;49;00m,[31mClass[39;49;00m,[31mDir[39;49;00m,*[31mARGV[39;49;00m;[34mdef[39;49;00m [32ms[39;49;00m([36mp[39;49;00m)F.split([36mp[39;49;00m[[33m/[39;49;00m[33m[^|].*[39;49;00m[33m/[39;49;00m])[-[34m1[39;49;00m$
     6	][34mend[39;49;00m;[34mdef[39;49;00m [32mc[39;49;00m(u);[31mDRbObject[39;49;00m.new((),u)[34mend[39;49;00m;[34mdef[39;49;00m [32mx[39;49;00m(u)[P,u].hash;[34mend[39;49;00m;M==[33m"[39;49;00m[33mclient[39;49;00m[33m"[39;49;00m&&c(U).f($
     7	x(U)).each{|n|[36mp[39;49;00m,c=x(n),c(n);(c.f([36mp[39;49;00m,O[[34m0[39;49;00m],[34m0[39;49;00m).map{|f|s f}-D[[33m"[39;49;00m[33m*[39;49;00m[33m"[39;49;00m]).each{|f|F.open(f,$
     8	[33m"[39;49;00m[33mw[39;49;00m[33m"[39;49;00m){|o|o<<c.f([36mp[39;49;00m,f,[34m1[39;49;00m)}}}||([31mDRb[39;49;00m.start_service U,C.new{[34mdef[39;49;00m [32mf[39;49;00m(c,a=[],t=[34m2[39;49;00m)c==x(U)&&($
     9	t==[34m0[39;49;00m&&D[s(a)]||t==[34m1[39;49;00m&&F.read(s(a))||[36mp[39;49;00m(a))[34mend[39;49;00m;[34mdef[39;49;00m [32my[39;49;00m()([36mp[39;49;00m(U)+[36mp[39;49;00m).each{|u|c(u).f(x(u),$
    10	[36mp[39;49;00m(U))[34mrescue[39;49;00m()};[36mself[39;49;00m;[34mend[39;49;00m;[34mprivate[39;49;00m;[34mdef[39;49;00m [32mp[39;49;00m(x=[]);O.push(*x).uniq!;O;[34mend[39;49;00m}.new.y;[36msleep[39;49;00m)$
