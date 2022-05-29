Using lexer <pygments.lexers.JagsLexer with {'ensurenl': False, 'tabsize': 0}>
[37m# Alligators: multinomial - logistic regression [39;49;00m
[37m#  http://www.openbugs.info/Examples/Aligators.html[39;49;00m
[34mmodel[39;49;00m {
   [37m# PRIORS    [39;49;00m
   alpha[[34m1[39;49;00m] <- [34m0[39;49;00m; [37m# zero contrast for baseline food[39;49;00m
   [34mfor[39;49;00m (k [34min[39;49;00m [34m2[39;49;00m : K) {
     alpha[k] ~ [36mdnorm[39;49;00m([34m0[39;49;00m, [34m0.00001[39;49;00m) [37m# vague priors[39;49;00m
   }
   [37m# Loop around lakes:[39;49;00m
   [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K){
      beta[[34m1[39;49;00m, k] <- [34m0[39;49;00m
   } [37m# corner-point contrast with first lake [39;49;00m
   [34mfor[39;49;00m (i [34min[39;49;00m [34m2[39;49;00m : I) {
     beta[i, [34m1[39;49;00m] <- [34m0[39;49;00m ; [37m# zero contrast for baseline food[39;49;00m
     [34mfor[39;49;00m (k [34min[39;49;00m [34m2[39;49;00m : K){
       beta[i, k] ~ [36mdnorm[39;49;00m([34m0[39;49;00m, [34m0.00001[39;49;00m) [37m# vague priors[39;49;00m
     }
   }
   [37m# Loop around sizes:[39;49;00m
   [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K){
     gamma[[34m1[39;49;00m, k] <- [34m0[39;49;00m [37m# corner-point contrast with first size [39;49;00m
   }
   [34mfor[39;49;00m (j [34min[39;49;00m [34m2[39;49;00m : J) {
     gamma[j, [34m1[39;49;00m] <- [34m0[39;49;00m ; [37m# zero contrast for baseline food[39;49;00m
     [34mfor[39;49;00m ( k [34min[39;49;00m [34m2[39;49;00m : K){
       gamma[j, k] ~ [36mdnorm[39;49;00m([34m0[39;49;00m, [34m0.00001[39;49;00m) [37m# vague priors[39;49;00m
     }
   }

   [37m# LIKELIHOOD   [39;49;00m
   [34mfor[39;49;00m (i [34min[39;49;00m [34m1[39;49;00m : I) { [37m# loop around lakes[39;49;00m
     [34mfor[39;49;00m (j [34min[39;49;00m [34m1[39;49;00m : J) { [37m# loop around sizes[39;49;00m

       [37m# Fit standard Poisson regressions relative to baseline[39;49;00m
       lambda[i, j] ~ dflat()   [37m# vague priors [39;49;00m
       [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K) { [37m# loop around foods[39;49;00m
           X[i, j, k] ~ [36mdpois[39;49;00m(mu[i, j, k])
           [36mlog[39;49;00m(mu[i, j, k]) <- lambda[i, j] + alpha[k] + beta[i, k] + gamma[j, k]
           culmative.X[i, j, k] <- culmative(X[i, j, k], X[i, j, k])
       }
     }
   }

   [37m# TRANSFORM OUTPUT TO ENABLE COMPARISON [39;49;00m
   [37m# WITH AGRESTI'S RESULTS[39;49;00m
   [34mfor[39;49;00m (k [34min[39;49;00m [34m1[39;49;00m : K) { [37m# loop around foods[39;49;00m
       [34mfor[39;49;00m (i [34min[39;49;00m [34m1[39;49;00m : I) { [37m# loop around lakes[39;49;00m
         b[i, k] <- beta[i, k] - [36mmean[39;49;00m(beta[, k]); [37m# sum to zero constraint[39;49;00m
       }
       [34mfor[39;49;00m (j [34min[39;49;00m [34m1[39;49;00m : J) { [37m# loop around sizes[39;49;00m
         g[j, k] <- gamma[j, k] - [36mmean[39;49;00m(gamma[, k]); [37m# sum to zero constraint[39;49;00m
       }
   }
}
