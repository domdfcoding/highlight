;;;; This [36mcontains[39;49;00m some [34mof[39;49;00m the core Hy functions used
;;;; to make functional programming slightly easier.
;;;;


(defn _numeric-check [x]
  ([34mif[39;49;00m (not (numeric? x))
    (raise (TypeError (.format [33m"{0!r} is not a number"[39;49;00m x)))))

(defn cycle [coll]
  [33m"Yield an infinite repetition of the items in coll"[39;49;00m
  (setv seen [])
  ([34mfor[39;49;00m [x coll]
    (yield x)
    (.append seen x))
  ([34mwhile[39;49;00m seen
    ([34mfor[39;49;00m [x seen]
      (yield x))))

(defn dec [n]
  [33m"Decrement n by 1"[39;49;00m
  (_numeric-check n)
  (- n [34m1[39;49;00m))

(defn distinct [coll]
  [33m"Return a generator from the original collection with duplicates[39;49;00m
[33m   removed"[39;49;00m
  (let [[seen []] [citer (iter coll)]]
    ([34mfor[39;49;00m [val citer]
      ([34mif[39;49;00m (not_in val seen)
        ([34mdo[39;49;00m
         (yield val)
         (.append seen val))))))

(defn drop [count coll]
  [33m"Drop `count` elements from `coll` and yield back the rest"[39;49;00m
  (let [[citer (iter coll)]]
    ([34mtry[39;49;00m ([34mfor[39;49;00m [i (range count)]
           ([34mnext[39;49;00m citer))
         ([34mcatch[39;49;00m [StopIteration]))
    citer))

(defn even? [n]
  [33m"Return true if n is an even number"[39;49;00m
  (_numeric-check n)
  (= (% n [34m2[39;49;00m) [34m0[39;49;00m))

(defn filter [pred coll]
  [33m"Return all elements from `coll` that pass `pred`"[39;49;00m
  (let [[citer (iter coll)]]
    ([34mfor[39;49;00m [val citer]
      ([34mif[39;49;00m (pred val)
        (yield val)))))

(defn inc [n]
  [33m"Increment n by 1"[39;49;00m
  (_numeric-check n)
  (+ n [34m1[39;49;00m))

(defn instance? [klass x]
  (isinstance x klass))

(defn iterable? [x]
  [33m"Return true if x is iterable"[39;49;00m
  ([34mtry[39;49;00m ([34mdo[39;49;00m (iter x) [34mtrue[39;49;00m)
       ([34mcatch[39;49;00m [[36mException[39;49;00m] [34mfalse[39;49;00m)))

(defn iterate [f x]
  (setv val x)
  ([34mwhile[39;49;00m [34mtrue[39;49;00m
    (yield val)
    (setv val (f val))))

(defn iterator? [x]
  [33m"Return true if x is an iterator"[39;49;00m
  ([34mtry[39;49;00m (= x (iter x))
       ([34mcatch[39;49;00m [TypeError] [34mfalse[39;49;00m)))

(defn neg? [n]
  [33m"Return true if n is < 0"[39;49;00m
  (_numeric-check n)
  (< n [34m0[39;49;00m))

(defn none? [x]
  [33m"Return true if x is None"[39;49;00m
  (is x None))

(defn numeric? [x]
  ([34mimport[39;49;00m [04m[36mnumbers[39;49;00m)
  (instance? numbers.[36mNumber[39;49;00m x))

(defn nth [coll index]
  [33m"Return nth item in collection or sequence, counting from 0"[39;49;00m
  ([34mif[39;49;00m (not (neg? index))
    ([34mif[39;49;00m (iterable? coll)
      ([34mtry[39;49;00m (first (list (take [34m1[39;49;00m (drop index coll))))
           ([34mcatch[39;49;00m [IndexError] None))
      ([34mtry[39;49;00m (get coll index)
           ([34mcatch[39;49;00m [IndexError] None)))
    None))

(defn odd? [n]
  [33m"Return true if n is an odd number"[39;49;00m
  (_numeric-check n)
  (= (% n [34m2[39;49;00m) [34m1[39;49;00m))

(defn pos? [n]
  [33m"Return true if n is > 0"[39;49;00m
  (_numeric_check n)
  (> n [34m0[39;49;00m))

(defn [36mremove[39;49;00m [pred coll]
  [33m"Return coll with elements removed that pass `pred`"[39;49;00m
  (let [[citer (iter coll)]]
    ([34mfor[39;49;00m [val citer]
      ([34mif[39;49;00m (not (pred val))
        (yield val)))))

(defn repeat [x &optional n]
  [33m"Yield x forever or optionally n times"[39;49;00m
  ([34mif[39;49;00m (none? n)
    (setv dispatch (fn [] ([34mwhile[39;49;00m [34mtrue[39;49;00m (yield x))))
    (setv dispatch (fn [] ([34mfor[39;49;00m [_ (range n)] (yield x)))))
  (dispatch))

(defn repeatedly [func]
  [33m"Yield result of running func repeatedly"[39;49;00m
  ([34mwhile[39;49;00m [34mtrue[39;49;00m
    (yield (func))))

(defn take [count coll]
  [33m"Take `count` elements from `coll`, or the whole set if the total[39;49;00m
[33m    number of entries in `coll` is less than `count`."[39;49;00m
  (let [[citer (iter coll)]]
    ([34mfor[39;49;00m [_ (range count)]
      (yield ([34mnext[39;49;00m citer)))))

(defn take-nth [n coll]
  [33m"Return every nth member of coll[39;49;00m
[33m     raises ValueError for (not (pos? n))"[39;49;00m
  ([34mif[39;49;00m (pos? n)
    (let [[citer (iter coll)] [skip (dec n)]]
      ([34mfor[39;49;00m [val citer]
        (yield val)
        ([34mfor[39;49;00m [_ (range skip)]
          ([34mnext[39;49;00m citer))))
    (raise (ValueError [33m"n must be positive"[39;49;00m))))

(defn take-[34mwhile[39;49;00m [pred coll]
  [33m"Take all elements while `pred` is true"[39;49;00m
  (let [[citer (iter coll)]]
    ([34mfor[39;49;00m [val citer]
      ([34mif[39;49;00m (pred val)
        (yield val)
        ([34mbreak[39;49;00m)))))

(defn zero? [n]
  [33m"Return true if n is 0"[39;49;00m
  (_numeric_check n)
  (= n [34m0[39;49;00m))

(def *exports* [[33m"cycle"[39;49;00m [33m"dec"[39;49;00m [33m"distinct"[39;49;00m [33m"drop"[39;49;00m [33m"even?"[39;49;00m [33m"filter"[39;49;00m [33m"inc"[39;49;00m
                [33m"instance?"[39;49;00m [33m"iterable?"[39;49;00m [33m"iterate"[39;49;00m [33m"iterator?"[39;49;00m [33m"neg?"[39;49;00m
                [33m"none?"[39;49;00m [33m"nth"[39;49;00m [33m"numeric?"[39;49;00m [33m"odd?"[39;49;00m [33m"pos?"[39;49;00m [33m"remove"[39;49;00m [33m"repeat"[39;49;00m
                [33m"repeatedly"[39;49;00m [33m"take"[39;49;00m [33m"take_nth"[39;49;00m [33m"take_while"[39;49;00m [33m"zero?"[39;49;00m])
