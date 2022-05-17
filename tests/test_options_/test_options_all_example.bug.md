     1^I[37m# Alligators: multinomial - logistic regression [39;49;00m$
     2^I[37m#  http://www.openbugs.info/Examples/Aligators.html[39;49;00m$
     3^I[34mmodel[39;49;00m {$
     4^I   [37m# PRIORS    [39;49;00m$
     5^I   alpha[[34m1[39;49;00m] <- [34m0[39;49;00m; [37m# zero contrast for baseline food[39;49;00m$
     6^I   [34mfor[39;49;00m (k [34min[39;49;00m [34m2[39;49;00m : K) { $
     7^I     alpha[k] ~ [36mdnorm[39;49;00m([34m0[39;49;00m, [34m0.00001[39;49;00m) [37m# vague priors[39;49;00m$
     8^I   } $
     9^I   [37m# Loop around lakes:[39;49;00m$
    10^I   [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K){ $
    11^I      beta[[34m1[39;49;00m, k] <- [34m0[39;49;00m $
    12^I   } [37m# corner-point contrast with first lake [39;49;00m$
    13^I   [34mfor[39;49;00m (i [34min[39;49;00m [34m2[39;49;00m : I) { $
    14^I     beta[i, [34m1[39;49;00m] <- [34m0[39;49;00m ; [37m# zero contrast for baseline food[39;49;00m$
    15^I     [34mfor[39;49;00m (k [34min[39;49;00m [34m2[39;49;00m : K){ $
    16^I       beta[i, k] ~ [36mdnorm[39;49;00m([34m0[39;49;00m, [34m0.00001[39;49;00m) [37m# vague priors[39;49;00m$
    17^I     } $
    18^I   }$
    19^I   [37m# Loop around sizes:[39;49;00m$
    20^I   [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K){ $
    21^I     gamma[[34m1[39;49;00m, k] <- [34m0[39;49;00m [37m# corner-point contrast with first size [39;49;00m$
    22^I   } $
    23^I   [34mfor[39;49;00m (j [34min[39;49;00m [34m2[39;49;00m : J) { $
    24^I     gamma[j, [34m1[39;49;00m] <- [34m0[39;49;00m ; [37m# zero contrast for baseline food[39;49;00m$
    25^I     [34mfor[39;49;00m ( k [34min[39;49;00m [34m2[39;49;00m : K){ $
    26^I       gamma[j, k] ~ [36mdnorm[39;49;00m([34m0[39;49;00m, [34m0.00001[39;49;00m) [37m# vague priors[39;49;00m$
    27^I     } $
    28^I   }$
    29^I$
    30^I   [37m# LIKELIHOOD   [39;49;00m$
    31^I   [34mfor[39;49;00m (i [34min[39;49;00m [34m1[39;49;00m : I) { [37m# loop around lakes[39;49;00m$
    32^I     [34mfor[39;49;00m (j [34min[39;49;00m [34m1[39;49;00m : J) { [37m# loop around sizes[39;49;00m$
    33^I$
    34^I       [37m# Fit standard Poisson regressions relative to baseline[39;49;00m$
    35^I       lambda[i, j] ~ dflat()   [37m# vague priors [39;49;00m$
    36^I       [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K) { [37m# loop around foods[39;49;00m$
    37^I           X[i, j, k] ~ [36mdpois[39;49;00m(mu[i, j, k])$
    38^I           [36mlog[39;49;00m(mu[i, j, k]) <- lambda[i, j] + alpha[k] + beta[i, k] + gamma[j, k]$
    39^I           culmative.X[i, j, k] <- culmative(X[i, j, k], X[i, j, k])$
    40^I       }$
    41^I     }$
    42^I   }$
    43^I$
    44^I   [37m# TRANSFORM OUTPUT TO ENABLE COMPARISON [39;49;00m$
    45^I   [37m# WITH AGRESTI'S RESULTS[39;49;00m$
    46^I   [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K) { [37m# loop around foods[39;49;00m$
    47^I       [34mfor[39;49;00m (i [34min[39;49;00m [34m1[39;49;00m : I) { [37m# loop around lakes[39;49;00m$
    48^I         b[i, k] <- beta[i, k] - [36mmean[39;49;00m(beta[, k]); [37m# sum to zero constraint[39;49;00m$
    49^I       }$
    50^I       [34mfor[39;49;00m (j [34min[39;49;00m [34m1[39;49;00m : J) { [37m# loop around sizes[39;49;00m$
    51^I         g[j, k] <- gamma[j, k] - [36mmean[39;49;00m(gamma[, k]); [37m# sum to zero constraint[39;49;00m$
    52^I       }$
    53^I   }$
    54^I} $
