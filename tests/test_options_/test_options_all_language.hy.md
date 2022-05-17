     1^I;;;; This [36mcontains[39;49;00m some [34mof[39;49;00m the core Hy functions used$
     2^I;;;; to make functional programming slightly easier.$
     3^I;;;;$
     4^I$
     5^I$
     6^I(defn _numeric-check [x]$
     7^I  ([34mif[39;49;00m (not (numeric? x))$
     8^I    (raise (TypeError (.format [33m"{0!r} is not a number"[39;49;00m x)))))$
     9^I$
    10^I(defn cycle [coll]$
    11^I  [33m"Yield an infinite repetition of the items in coll"[39;49;00m$
    12^I  (setv seen [])$
    13^I  ([34mfor[39;49;00m [x coll]$
    14^I    (yield x)$
    15^I    (.append seen x))$
    16^I  ([34mwhile[39;49;00m seen$
    17^I    ([34mfor[39;49;00m [x seen]$
    18^I      (yield x))))$
    19^I$
    20^I(defn dec [n]$
    21^I  [33m"Decrement n by 1"[39;49;00m$
    22^I  (_numeric-check n)$
    23^I  (- n [34m1[39;49;00m))$
    24^I$
    25^I(defn distinct [coll]$
    26^I  [33m"Return a generator from the original collection with duplicates[39;49;00m$
    27^I[33m   removed"[39;49;00m$
    28^I  (let [[seen []] [citer (iter coll)]]$
    29^I    ([34mfor[39;49;00m [val citer]$
    30^I      ([34mif[39;49;00m (not_in val seen)$
    31^I        ([34mdo[39;49;00m$
    32^I         (yield val)$
    33^I         (.append seen val))))))$
    34^I$
    35^I(defn drop [count coll]$
    36^I  [33m"Drop `count` elements from `coll` and yield back the rest"[39;49;00m$
    37^I  (let [[citer (iter coll)]]$
    38^I    ([34mtry[39;49;00m ([34mfor[39;49;00m [i (range count)]$
    39^I           ([34mnext[39;49;00m citer))$
    40^I         ([34mcatch[39;49;00m [StopIteration]))$
    41^I    citer))$
    42^I$
    43^I(defn even? [n]$
    44^I  [33m"Return true if n is an even number"[39;49;00m$
    45^I  (_numeric-check n)$
    46^I  (= (% n [34m2[39;49;00m) [34m0[39;49;00m))$
    47^I$
    48^I(defn filter [pred coll]$
    49^I  [33m"Return all elements from `coll` that pass `pred`"[39;49;00m$
    50^I  (let [[citer (iter coll)]]$
    51^I    ([34mfor[39;49;00m [val citer]$
    52^I      ([34mif[39;49;00m (pred val)$
    53^I        (yield val)))))$
    54^I$
    55^I(defn inc [n]$
    56^I  [33m"Increment n by 1"[39;49;00m$
    57^I  (_numeric-check n)$
    58^I  (+ n [34m1[39;49;00m))$
    59^I$
    60^I(defn instance? [klass x]$
    61^I  (isinstance x klass))$
    62^I$
    63^I(defn iterable? [x]$
    64^I  [33m"Return true if x is iterable"[39;49;00m$
    65^I  ([34mtry[39;49;00m ([34mdo[39;49;00m (iter x) [34mtrue[39;49;00m)$
    66^I       ([34mcatch[39;49;00m [[36mException[39;49;00m] [34mfalse[39;49;00m)))$
    67^I$
    68^I(defn iterate [f x]$
    69^I  (setv val x)$
    70^I  ([34mwhile[39;49;00m [34mtrue[39;49;00m$
    71^I    (yield val)$
    72^I    (setv val (f val))))$
    73^I$
    74^I(defn iterator? [x]$
    75^I  [33m"Return true if x is an iterator"[39;49;00m$
    76^I  ([34mtry[39;49;00m (= x (iter x))$
    77^I       ([34mcatch[39;49;00m [TypeError] [34mfalse[39;49;00m)))$
    78^I$
    79^I(defn neg? [n]$
    80^I  [33m"Return true if n is < 0"[39;49;00m$
    81^I  (_numeric-check n)$
    82^I  (< n [34m0[39;49;00m))$
    83^I$
    84^I(defn none? [x]$
    85^I  [33m"Return true if x is None"[39;49;00m$
    86^I  (is x None))$
    87^I$
    88^I(defn numeric? [x]$
    89^I  ([34mimport[39;49;00m [04m[36mnumbers[39;49;00m)$
    90^I  (instance? numbers.[36mNumber[39;49;00m x))$
    91^I$
    92^I(defn nth [coll index]$
    93^I  [33m"Return nth item in collection or sequence, counting from 0"[39;49;00m$
    94^I  ([34mif[39;49;00m (not (neg? index))$
    95^I    ([34mif[39;49;00m (iterable? coll)$
    96^I      ([34mtry[39;49;00m (first (list (take [34m1[39;49;00m (drop index coll))))$
    97^I           ([34mcatch[39;49;00m [IndexError] None))$
    98^I      ([34mtry[39;49;00m (get coll index)$
    99^I           ([34mcatch[39;49;00m [IndexError] None)))$
   100^I    None))$
   101^I$
   102^I(defn odd? [n]$
   103^I  [33m"Return true if n is an odd number"[39;49;00m$
   104^I  (_numeric-check n)$
   105^I  (= (% n [34m2[39;49;00m) [34m1[39;49;00m))$
   106^I$
   107^I(defn pos? [n]$
   108^I  [33m"Return true if n is > 0"[39;49;00m$
   109^I  (_numeric_check n)$
   110^I  (> n [34m0[39;49;00m))$
   111^I$
   112^I(defn [36mremove[39;49;00m [pred coll]$
   113^I  [33m"Return coll with elements removed that pass `pred`"[39;49;00m$
   114^I  (let [[citer (iter coll)]]$
   115^I    ([34mfor[39;49;00m [val citer]$
   116^I      ([34mif[39;49;00m (not (pred val))$
   117^I        (yield val)))))$
   118^I$
   119^I(defn repeat [x &optional n]$
   120^I  [33m"Yield x forever or optionally n times"[39;49;00m$
   121^I  ([34mif[39;49;00m (none? n)$
   122^I    (setv dispatch (fn [] ([34mwhile[39;49;00m [34mtrue[39;49;00m (yield x))))$
   123^I    (setv dispatch (fn [] ([34mfor[39;49;00m [_ (range n)] (yield x)))))$
   124^I  (dispatch))$
   125^I$
   126^I(defn repeatedly [func]$
   127^I  [33m"Yield result of running func repeatedly"[39;49;00m$
   128^I  ([34mwhile[39;49;00m [34mtrue[39;49;00m$
   129^I    (yield (func))))$
   130^I$
   131^I(defn take [count coll]$
   132^I  [33m"Take `count` elements from `coll`, or the whole set if the total[39;49;00m$
   133^I[33m    number of entries in `coll` is less than `count`."[39;49;00m$
   134^I  (let [[citer (iter coll)]]$
   135^I    ([34mfor[39;49;00m [_ (range count)]$
   136^I      (yield ([34mnext[39;49;00m citer)))))$
   137^I$
   138^I(defn take-nth [n coll]$
   139^I  [33m"Return every nth member of coll[39;49;00m$
   140^I[33m     raises ValueError for (not (pos? n))"[39;49;00m$
   141^I  ([34mif[39;49;00m (pos? n)$
   142^I    (let [[citer (iter coll)] [skip (dec n)]]$
   143^I      ([34mfor[39;49;00m [val citer]$
   144^I        (yield val)$
   145^I        ([34mfor[39;49;00m [_ (range skip)]$
   146^I          ([34mnext[39;49;00m citer))))$
   147^I    (raise (ValueError [33m"n must be positive"[39;49;00m))))$
   148^I$
   149^I(defn take-[34mwhile[39;49;00m [pred coll]$
   150^I  [33m"Take all elements while `pred` is true"[39;49;00m$
   151^I  (let [[citer (iter coll)]]$
   152^I    ([34mfor[39;49;00m [val citer]$
   153^I      ([34mif[39;49;00m (pred val)$
   154^I        (yield val)$
   155^I        ([34mbreak[39;49;00m)))))$
   156^I$
   157^I(defn zero? [n]$
   158^I  [33m"Return true if n is 0"[39;49;00m$
   159^I  (_numeric_check n)$
   160^I  (= n [34m0[39;49;00m))$
   161^I$
   162^I(def *exports* [[33m"cycle"[39;49;00m [33m"dec"[39;49;00m [33m"distinct"[39;49;00m [33m"drop"[39;49;00m [33m"even?"[39;49;00m [33m"filter"[39;49;00m [33m"inc"[39;49;00m$
   163^I                [33m"instance?"[39;49;00m [33m"iterable?"[39;49;00m [33m"iterate"[39;49;00m [33m"iterator?"[39;49;00m [33m"neg?"[39;49;00m$
   164^I                [33m"none?"[39;49;00m [33m"nth"[39;49;00m [33m"numeric?"[39;49;00m [33m"odd?"[39;49;00m [33m"pos?"[39;49;00m [33m"remove"[39;49;00m [33m"repeat"[39;49;00m$
   165^I                [33m"repeatedly"[39;49;00m [33m"take"[39;49;00m [33m"take_nth"[39;49;00m [33m"take_while"[39;49;00m [33m"zero?"[39;49;00m])$
