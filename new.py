import scipy.stats as stats
import numpy as np

#define lambda
lam = 7

#

prob_7 = stats.poisson.pmf(7, lam)
print(prob_7)

## prob of having 4 or fewer defect:
prob_4 = stats.poisson.cdf(2, lam)
print(prob_4)

## Task 4:
prob_more_than_9 = 1 - stats.poisson.cdf(9, lam)
print(prob_more_than_9)

## Task 5:
month_defects = stats.poisson.rvs(lam, size = 365)

## Task 6:
print(month_defects[0:20])

## Total defects in a year if 7 defects a day:
val = 7 * 365
print(val)

## Task 8:
year_defects = sum(month_defects)
print(year_defects)

## Task 9:
print(np.mean(month_defects))

## Task 10:
print(month_defects.max())

## Task 11:
probability_max = 1 - stats.poisson.cdf(16, lam)
print(probability_max)

## Calc the 90% percentile
percent_90 = stats.poisson.ppf(0.9, lam)
print(percent_90)

## Calc num greater than 90 percentile:

print(sum(year_defects) > stats.poisson.ppf(0.9,lam)/len(year_defects))