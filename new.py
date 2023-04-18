import scipy.stats as stats
import numpy as np

#define lambda
lam = 7

# prob of getting exactly 7

prob_7 = stats.poisson.pmf(7, lam)
print(prob_7)

## prob of having 4 or fewer defect:
prob_4 = stats.poisson.cdf(2, lam)
print(prob_4)

## Probability of getting 9 or more defects
prob_more_than_9 = 1 - stats.poisson.cdf(9, lam)
print(prob_more_than_9)

## monthly defects
month_defects = stats.poisson.rvs(lam, size = 365)

## Task 6:
print(month_defects[0:20])

## Total defects in a year if 7 defects a day:
val = 7 * 365
print(val)

## sum of all monthly defects
year_defects = sum(month_defects)
print(year_defects)

## print mean of month_defects
print(np.mean(month_defects))

## maximum defects in a month
print(month_defects.max())

## probaility of getting more than max value
probability_max = 1 - stats.poisson.cdf(16, lam)
print(probability_max)

## Calc the 90% percentile
percent_90 = stats.poisson.ppf(0.9, lam)
print(percent_90)

## Calc num greater than 90 percentile:

print(sum(year_defects) > stats.poisson.ppf(0.9,lam)/len(year_defects))
