     1	[37m# Alligators: multinomial - logistic regression [39;49;00m
     2	[37m#  http://www.openbugs.info/Examples/Aligators.html[39;49;00m
     3	[34mmodel[39;49;00m {
     4	   [37m# PRIORS    [39;49;00m
     5	   alpha[[34m1[39;49;00m] <- [34m0[39;49;00m; [37m# zero contrast for baseline food[39;49;00m
     6	   [34mfor[39;49;00m (k [34min[39;49;00m [34m2[39;49;00m : K) {
     7	     alpha[k] ~ [36mdnorm[39;49;00m([34m0[39;49;00m, [34m0.00001[39;49;00m) [37m# vague priors[39;49;00m
     8	   }
     9	   [37m# Loop around lakes:[39;49;00m
    10	   [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K){
    11	      beta[[34m1[39;49;00m, k] <- [34m0[39;49;00m
    12	   } [37m# corner-point contrast with first lake [39;49;00m
    13	   [34mfor[39;49;00m (i [34min[39;49;00m [34m2[39;49;00m : I) {
    14	     beta[i, [34m1[39;49;00m] <- [34m0[39;49;00m ; [37m# zero contrast for baseline food[39;49;00m
    15	     [34mfor[39;49;00m (k [34min[39;49;00m [34m2[39;49;00m : K){
    16	       beta[i, k] ~ [36mdnorm[39;49;00m([34m0[39;49;00m, [34m0.00001[39;49;00m) [37m# vague priors[39;49;00m
    17	     }
    18	   }
    19	   [37m# Loop around sizes:[39;49;00m
    20	   [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K){
    21	     gamma[[34m1[39;49;00m, k] <- [34m0[39;49;00m [37m# corner-point contrast with first size [39;49;00m
    22	   }
    23	   [34mfor[39;49;00m (j [34min[39;49;00m [34m2[39;49;00m : J) {
    24	     gamma[j, [34m1[39;49;00m] <- [34m0[39;49;00m ; [37m# zero contrast for baseline food[39;49;00m
    25	     [34mfor[39;49;00m ( k [34min[39;49;00m [34m2[39;49;00m : K){
    26	       gamma[j, k] ~ [36mdnorm[39;49;00m([34m0[39;49;00m, [34m0.00001[39;49;00m) [37m# vague priors[39;49;00m
    27	     }
    28	   }
    29
    30	   [37m# LIKELIHOOD   [39;49;00m
    31	   [34mfor[39;49;00m (i [34min[39;49;00m [34m1[39;49;00m : I) { [37m# loop around lakes[39;49;00m
    32	     [34mfor[39;49;00m (j [34min[39;49;00m [34m1[39;49;00m : J) { [37m# loop around sizes[39;49;00m
    33
    34	       [37m# Fit standard Poisson regressions relative to baseline[39;49;00m
    35	       lambda[i, j] ~ dflat()   [37m# vague priors [39;49;00m
    36	       [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K) { [37m# loop around foods[39;49;00m
    37	           X[i, j, k] ~ [36mdpois[39;49;00m(mu[i, j, k])
    38	           [36mlog[39;49;00m(mu[i, j, k]) <- lambda[i, j] + alpha[k] + beta[i, k] + gamma[j, k]
    39	           culmative.X[i, j, k] <- culmative(X[i, j, k], X[i, j, k])
    40	       }
    41	     }
    42	   }
    43
    44	   [37m# TRANSFORM OUTPUT TO ENABLE COMPARISON [39;49;00m
    45	   [37m# WITH AGRESTI'S RESULTS[39;49;00m
    46	   [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K) { [37m# loop around foods[39;49;00m
    47	       [34mfor[39;49;00m (i [34min[39;49;00m [34m1[39;49;00m : I) { [37m# loop around lakes[39;49;00m
    48	         b[i, k] <- beta[i, k] - [36mmean[39;49;00m(beta[, k]); [37m# sum to zero constraint[39;49;00m
    49	       }
    50	       [34mfor[39;49;00m (j [34min[39;49;00m [34m1[39;49;00m : J) { [37m# loop around sizes[39;49;00m
    51	         g[j, k] <- gamma[j, k] - [36mmean[39;49;00m(gamma[, k]); [37m# sum to zero constraint[39;49;00m
    52	       }
    53	   }
    54	}
