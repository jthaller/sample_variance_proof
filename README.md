# sample_variance_proof
I wanted to see if dividing a sample population by n-1 instead of n is actually better. I did this while watching Liverpool vs. Watford. Liverpool won 2-0. Top of the league and 19pts ahead of Man City.

I recently learned that when calculating the sample variance, people divide by n-1 instead of n, where n is the sample size. This is to correction for the liklihood that your sample will underestimate variance. After looking at the analytic proof, I decided to quickly write something to check if this is true by creating a big data set with random numbers.

what I actually found was that the variance for the sample tended to be way higher than the variance of the population. Sometimes they were similar, but never was the sample variance << population vairace.

Of course, the higher the sample size compared to the population size, the better dividing by n will be. I wonder if the results are weird because the population variance is always so small? How to get around that with the random number generator? Maybe just shrink the population size
