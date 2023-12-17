"""
CSE357 
Naseeba Faiza
Group: The Random Rebels
Assignment 5
Question 5
Instruction to run: python a5_q5.py
Note: Make sure to pip3 install all libraries please!

"""

import pandas as pd  # for handling data structures (loading and processing CSV data)
from scipy.stats import norm  # for calculating Z-scores and critical Z-values
from scipy.stats import ttest_1samp  # for performing single-sample T-tests
from scipy.stats import ttest_rel  # for performing paired T-tests
from scipy.stats import ttest_ind  # for performing unpaired (independent samples) T-tests

"""

Part a)

Z-test to compare mean heights of women from two tribes
Known variance: 121

Ho: No difference in mean heights
H1: Difference in mean heights

Inputs:
  - height_female.csv: Heights from settlement A
  - height_female_200.csv: Sample heights from tribe B

Outputs:
  - Z-score, critical Z-value, and hypothesis test conclusion

"""

print("\n@-->--@-->-- Part (a) @-->--@-->--")
heights_a = pd.read_csv('height_female.csv', header=None)
heights_b = pd.read_csv('height_female_200.csv', header=None)
mean_a = heights_a.mean().item()  # mean for settlement A
variance_b = 121 # known variance of the sample of 200 women
std_dev_b = variance_b**0.5
mean_b = heights_b.mean().item()  # mean for the sample from tribe B
n_b = len(heights_b) # sample size for tribe B
Z = (mean_b - mean_a) / (std_dev_b / (n_b ** 0.5)) # Z-score using the sample standard deviation
Z_critical = norm.ppf(0.975) # critical Z-value for alpha = 0.05 (two-tailed test!)
reject_null = abs(Z) > Z_critical # reject the null hypothesis?

print(f'Z-score: {Z}')
print(f'Critical value: {Z_critical}')
if reject_null:
    print('Reject Ho: There is difference in heights')
else:
    print('Fail to reject Ho: There is no difference in heights')

"""
Part b)

Z-test to compare mean heights of the first 50 males and females
Known variances: 110 for males, 121 for females

Ho: There is no difference in mean heights between genders
H1: There is difference in mean heights between genders

Inputs:
  - height_male.csv: Sample heights of the first 50 males
  - height_female.csv: Sample heights of the first 50 females

Outputs:
  - Z-score, critical Z-value, and hypothesis test conclusion

"""
print("\n@-->--@-->-- Part (b) @-->--@-->--")
heights_male = pd.read_csv('height_male.csv', header=None).iloc[:50, 0] # first 50 males!!!!!
heights_female = pd.read_csv('height_female.csv', header=None).iloc[:50, 0]
variance_male = 110 # Known variances
variance_female = 121
std_dev_male = variance_male**0.5 # standard deviations
std_dev_female = variance_female**0.5
mean_male = heights_male.mean() # means for the first 50 males and females
mean_female = heights_female.mean()
n_male = len(heights_male) # samples for both groups
n_female = len(heights_female)
pooled_std_dev = ((std_dev_male**2 / n_male) + (std_dev_female**2 / n_female))**0.5 # Z-score
Z = (mean_male - mean_female) / pooled_std_dev
Z_critical = norm.ppf(0.975) # critical value for alpha = 0.05 (two-tailed)

print(f'Z-score: {Z}')
print(f'Critical value: {Z_critical}')
if abs(Z) > Z_critical:
    print('Reject Ho: There is a significant difference in mean heights between females and males')
else:
    print('Fail to reject Ho: There is no significant difference in mean heights between females and males')

"""
Part c)

A single-sample T-test to compare mean heights of men from tribe B against settlement A
Population variance is unknown and the sample size is small

Ho: No difference in mean heights
H1: Difference in mean heights

Inputs:
  - height_male.csv: Heights from settlement A
  - heights_b_list: Sample heights from tribe B

Outputs:
  - T-score, critical T-value, and hypothesis test conclusion

"""

print("\n@-->--@-->-- Part (c) @-->--@-->--")
heights_b_list = [157.74, 155.98, 186.2, 171.63, 169.11, 168.71, 179.55, 174.7, 183.09, 152.33] # sample heights of men from tribe B
heights_a_male = pd.read_csv('height_male.csv', header=None) # population heights of men from settlement A
population_mean_a = heights_a_male.mean().item() # mean height for men from settlement A
t_stat, p_val = ttest_1samp(heights_b_list, population_mean_a) # T-test
t_critical = 2.2622 # T critical value for alpha = 0.05 and 9 df

print(f'T-statistic: {t_stat}')
print(f'p-value: {p_val / 2}')  # / 2 cuz it's a one-tailed test
print(f'Critical T-value: {t_critical}')
if abs(t_stat) > t_critical:
    print('Reject Ho: There is a significant difference in mean heights')
else:
    print('Fail to reject Ho: There is no significant difference in mean heights')

"""
Part d)

A paired T-test to evaluate the effect of time on the heights of men from settlement A

Ho: No difference in mean heights over one year
H1: Difference in mean heights over one year

Inputs:
  - Sample taken now: Heights of 10 males from settlement A
  - Sample taken 1 year later: Heights of the same 10 males from settlement A

Outputs:
  - T-score, critical T-value, and hypothesis test conclusion

"""

print("\n@-->--@-->-- Part (d) @-->--@-->--")

heights_now = [158.2, 160.5, 174.1, 162.36, 162.84, 172.70, 186.92, 183.01, 167.22, 159.19] # now and later
heights_later = [167.04, 161.54, 174.31, 162.56, 163.84, 172.73, 188.62, 184.62, 168.43, 171.19]
t_stat, p_val = ttest_rel(heights_now, heights_later) # paired T-test
t_critical = 2.2622 # T critical value for alpha = 0.05 and 9 df

print(f'Paired T-statistic: {t_stat}')
print(f'p-value: {p_val}')  # cuz this is a two-tailed test
print(f'Critical T-value: {t_critical}')
if abs(t_stat) > t_critical:
    print('Reject Ho: There is a significant difference in mean heights over one year')
else:
    print('Fail to reject Ho: There is no significant difference in mean heights over one year')

"""
Part e)

Performs an unpaired T-test (independent samples T-test) to compare mean heights between
settlement A and tribe B.

Ho: No difference in mean heights between the two groups
H1: A difference in mean heights between the two groups

Inputs:
  - Heights from settlement A: Array of heights from 10 individuals
  - Heights from tribe B: Array of heights from 10 individuals

Outputs:
  - T-score, critical T-value, and hypothesis test conclusion

"""

print("\n@-->--@-->-- Part (e) @-->--@-->--")

heights_a = [158.17, 175.87, 147.86, 138.77, 165.57, 166.56, 180.09, 175.14, 171.21, 179.0]
heights_b = [145.74, 174.73, 154.43, 142.25, 142.74, 160.88, 160.82, 170.01, 165.45, 170.04]
t_stat, p_val = ttest_ind(heights_a, heights_b) # unpaired T-test
t_critical = 2.1 # T critical value for alpha = 0.05 (two-tailed)

print(f'Unpaired T-statistic: {t_stat}')
print(f'p-value: {p_val}')
print(f'Critical T-value: {t_critical}')
if abs(t_stat) > t_critical:
    print('Reject Ho: There is a significant difference in mean heights between the two groups')
else:
    print('Fail to reject Ho: There is no significant difference in mean heights between the two groups')

print("\n:-)")
