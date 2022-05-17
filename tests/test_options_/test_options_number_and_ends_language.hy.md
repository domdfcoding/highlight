     1	;;;; This [36mcontains[39;49;00m some [34mof[39;49;00m the core Hy functions used$
     2	;;;; to make functional programming slightly easier.$
     3	;;;;$
     4	$
     5	$
     6	(defn _numeric-check [x]$
     7	  ([34mif[39;49;00m (not (numeric? x))$
     8	    (raise (TypeError (.format [33m"{0!r} is not a number"[39;49;00m x)))))$
     9	$
    10	(defn cycle [coll]$
    11	  [33m"Yield an infinite repetition of the items in coll"[39;49;00m$
    12	  (setv seen [])$
    13	  ([34mfor[39;49;00m [x coll]$
    14	    (yield x)$
    15	    (.append seen x))$
    16	  ([34mwhile[39;49;00m seen$
    17	    ([34mfor[39;49;00m [x seen]$
    18	      (yield x))))$
    19	$
    20	(defn dec [n]$
    21	  [33m"Decrement n by 1"[39;49;00m$
    22	  (_numeric-check n)$
    23	  (- n [34m1[39;49;00m))$
    24	$
    25	(defn distinct [coll]$
    26	  [33m"Return a generator from the original collection with duplicates[39;49;00m$
    27	[33m   removed"[39;49;00m$
    28	  (let [[seen []] [citer (iter coll)]]$
    29	    ([34mfor[39;49;00m [val citer]$
    30	      ([34mif[39;49;00m (not_in val seen)$
    31	        ([34mdo[39;49;00m$
    32	         (yield val)$
    33	         (.append seen val))))))$
    34	$
    35	(defn drop [count coll]$
    36	  [33m"Drop `count` elements from `coll` and yield back the rest"[39;49;00m$
    37	  (let [[citer (iter coll)]]$
    38	    ([34mtry[39;49;00m ([34mfor[39;49;00m [i (range count)]$
    39	           ([34mnext[39;49;00m citer))$
    40	         ([34mcatch[39;49;00m [StopIteration]))$
    41	    citer))$
    42	$
    43	(defn even? [n]$
    44	  [33m"Return true if n is an even number"[39;49;00m$
    45	  (_numeric-check n)$
    46	  (= (% n [34m2[39;49;00m) [34m0[39;49;00m))$
    47	$
    48	(defn filter [pred coll]$
    49	  [33m"Return all elements from `coll` that pass `pred`"[39;49;00m$
    50	  (let [[citer (iter coll)]]$
    51	    ([34mfor[39;49;00m [val citer]$
    52	      ([34mif[39;49;00m (pred val)$
    53	        (yield val)))))$
    54	$
    55	(defn inc [n]$
    56	  [33m"Increment n by 1"[39;49;00m$
    57	  (_numeric-check n)$
    58	  (+ n [34m1[39;49;00m))$
    59	$
    60	(defn instance? [klass x]$
    61	  (isinstance x klass))$
    62	$
    63	(defn iterable? [x]$
    64	  [33m"Return true if x is iterable"[39;49;00m$
    65	  ([34mtry[39;49;00m ([34mdo[39;49;00m (iter x) [34mtrue[39;49;00m)$
    66	       ([34mcatch[39;49;00m [[36mException[39;49;00m] [34mfalse[39;49;00m)))$
    67	$
    68	(defn iterate [f x]$
    69	  (setv val x)$
    70	  ([34mwhile[39;49;00m [34mtrue[39;49;00m$
    71	    (yield val)$
    72	    (setv val (f val))))$
    73	$
    74	(defn iterator? [x]$
    75	  [33m"Return true if x is an iterator"[39;49;00m$
    76	  ([34mtry[39;49;00m (= x (iter x))$
    77	       ([34mcatch[39;49;00m [TypeError] [34mfalse[39;49;00m)))$
    78	$
    79	(defn neg? [n]$
    80	  [33m"Return true if n is < 0"[39;49;00m$
    81	  (_numeric-check n)$
    82	  (< n [34m0[39;49;00m))$
    83	$
    84	(defn none? [x]$
    85	  [33m"Return true if x is None"[39;49;00m$
    86	  (is x None))$
    87	$
    88	(defn numeric? [x]$
    89	  ([34mimport[39;49;00m [04m[36mnumbers[39;49;00m)$
    90	  (instance? numbers.[36mNumber[39;49;00m x))$
    91	$
    92	(defn nth [coll index]$
    93	  [33m"Return nth item in collection or sequence, counting from 0"[39;49;00m$
    94	  ([34mif[39;49;00m (not (neg? index))$
    95	    ([34mif[39;49;00m (iterable? coll)$
    96	      ([34mtry[39;49;00m (first (list (take [34m1[39;49;00m (drop index coll))))$
    97	           ([34mcatch[39;49;00m [IndexError] None))$
    98	      ([34mtry[39;49;00m (get coll index)$
    99	           ([34mcatch[39;49;00m [IndexError] None)))$
   100	    None))$
   101	$
   102	(defn odd? [n]$
   103	  [33m"Return true if n is an odd number"[39;49;00m$
   104	  (_numeric-check n)$
   105	  (= (% n [34m2[39;49;00m) [34m1[39;49;00m))$
   106	$
   107	(defn pos? [n]$
   108	  [33m"Return true if n is > 0"[39;49;00m$
   109	  (_numeric_check n)$
   110	  (> n [34m0[39;49;00m))$
   111	$
   112	(defn [36mremove[39;49;00m [pred coll]$
   113	  [33m"Return coll with elements removed that pass `pred`"[39;49;00m$
   114	  (let [[citer (iter coll)]]$
   115	    ([34mfor[39;49;00m [val citer]$
   116	      ([34mif[39;49;00m (not (pred val))$
   117	        (yield val)))))$
   118	$
   119	(defn repeat [x &optional n]$
   120	  [33m"Yield x forever or optionally n times"[39;49;00m$
   121	  ([34mif[39;49;00m (none? n)$
   122	    (setv dispatch (fn [] ([34mwhile[39;49;00m [34mtrue[39;49;00m (yield x))))$
   123	    (setv dispatch (fn [] ([34mfor[39;49;00m [_ (range n)] (yield x)))))$
   124	  (dispatch))$
   125	$
   126	(defn repeatedly [func]$
   127	  [33m"Yield result of running func repeatedly"[39;49;00m$
   128	  ([34mwhile[39;49;00m [34mtrue[39;49;00m$
   129	    (yield (func))))$
   130	$
   131	(defn take [count coll]$
   132	  [33m"Take `count` elements from `coll`, or the whole set if the total[39;49;00m$
   133	[33m    number of entries in `coll` is less than `count`."[39;49;00m$
   134	  (let [[citer (iter coll)]]$
   135	    ([34mfor[39;49;00m [_ (range count)]$
   136	      (yield ([34mnext[39;49;00m citer)))))$
   137	$
   138	(defn take-nth [n coll]$
   139	  [33m"Return every nth member of coll[39;49;00m$
   140	[33m     raises ValueError for (not (pos? n))"[39;49;00m$
   141	  ([34mif[39;49;00m (pos? n)$
   142	    (let [[citer (iter coll)] [skip (dec n)]]$
   143	      ([34mfor[39;49;00m [val citer]$
   144	        (yield val)$
   145	        ([34mfor[39;49;00m [_ (range skip)]$
   146	          ([34mnext[39;49;00m citer))))$
   147	    (raise (ValueError [33m"n must be positive"[39;49;00m))))$
   148	$
   149	(defn take-[34mwhile[39;49;00m [pred coll]$
   150	  [33m"Take all elements while `pred` is true"[39;49;00m$
   151	  (let [[citer (iter coll)]]$
   152	    ([34mfor[39;49;00m [val citer]$
   153	      ([34mif[39;49;00m (pred val)$
   154	        (yield val)$
   155	        ([34mbreak[39;49;00m)))))$
   156	$
   157	(defn zero? [n]$
   158	  [33m"Return true if n is 0"[39;49;00m$
   159	  (_numeric_check n)$
   160	  (= n [34m0[39;49;00m))$
   161	$
   162	(def *exports* [[33m"cycle"[39;49;00m [33m"dec"[39;49;00m [33m"distinct"[39;49;00m [33m"drop"[39;49;00m [33m"even?"[39;49;00m [33m"filter"[39;49;00m [33m"inc"[39;49;00m$
   163	                [33m"instance?"[39;49;00m [33m"iterable?"[39;49;00m [33m"iterate"[39;49;00m [33m"iterator?"[39;49;00m [33m"neg?"[39;49;00m$
   164	                [33m"none?"[39;49;00m [33m"nth"[39;49;00m [33m"numeric?"[39;49;00m [33m"odd?"[39;49;00m [33m"pos?"[39;49;00m [33m"remove"[39;49;00m [33m"repeat"[39;49;00m$
   165	                [33m"repeatedly"[39;49;00m [33m"take"[39;49;00m [33m"take_nth"[39;49;00m [33m"take_while"[39;49;00m [33m"zero?"[39;49;00m])$
