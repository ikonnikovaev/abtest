# write your code here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from statsmodels.stats.power import TTestIndPower

data_aa = pd.read_csv('aa_test.csv')
#print(data)
sample1 = data_aa['Sample 1']
sample2 = data_aa['Sample 2']
#print(sample1, sample2)

# Levene's test: are the variances equal?
W, pvalue = st.levene(sample1, sample2, center='mean')
threshold = 0.05
if pvalue > threshold:
    sign = '>'
    reject = 'no'
    equal = 'yes'
else:
    sign = '<='
    reject = 'yes'
    equal = 'no'
'''
print("Levene's test")
print(f"W = {round(W, 3)}, p-value {sign} 0.05")
print(f"Reject null hypothesis: {reject}")
print(f"Variances are equal: {equal}")
print()
'''

# Student's test: are the means equal?
t, pvalue = st.ttest_ind(sample1, sample2)
if pvalue > threshold:
    sign = '>'
    reject = 'no'
    equal = 'yes'
else:
    sign = '<='
    reject = 'yes'
    equal = 'no'
'''
print("T-test")
print(f"t = {round(t, 3)}, p-value {sign} 0.05")
print(f"Reject null hypothesis: {reject}")
print(f"Means are equal: {equal}")
'''

# Power analysis
analysis = TTestIndPower()
result = analysis.solve_power(effect_size=0.2, nobs1=None, alpha=0.05, power=0.8, ratio=1.0)
# print(f"Sample Size: {int(round(result, -2))}")
data_ab = pd.read_csv('ab_test.csv')
# print(data_ab.columns)
vc = data_ab['group'].value_counts()
#print(f"Control group: {vc['Control']}")
#print(f"Experimental group: {vc['Experimental']}")

data_ab.date = pd.to_datetime(data_ab.date).dt.day
groups_by_date = pd.DataFrame({'Control': data_ab[data_ab.group == 'Control'].date.value_counts(),
                    'Experimental': data_ab[data_ab.group == 'Experimental'].date.value_counts()})
#print(groups_by_date)

groups_by_date.plot.bar()
plt.ylabel("Number of sessions")
plt.xlabel("June")
plt.legend(["Control", "Experimental"])
plt.savefig("1.jpg")

data_ab.order_value.hist(by=data_ab.group)
plt.savefig("2.jpg")
data_ab.session_duration.hist(by=data_ab.group)
plt.savefig("3.jpg")

ninety_ninth_percentile_order_value = np.percentile(data_ab.order_value, 99)
ninety_ninth_percentile_session = np.percentile(data_ab.session_duration, 99)

order_value_outliers = data_ab.loc[data_ab.order_value >= ninety_ninth_percentile_order_value].index
session_value_outliers = data_ab.loc[data_ab.session_duration >= ninety_ninth_percentile_session].index

data_no_outliers = data_ab.drop(index=order_value_outliers.union(session_value_outliers))
#print(data_no_outliers.columns)
# print(f'Mean: {round(data_no_outliers.order_value.mean(), 2)}')
# print(f'Standard deviation: {round(data_no_outliers.order_value.std(ddof=0), 2)}')
# print(f'Max: {round(data_no_outliers.order_value.max(), 2)}')

sample1 = data_no_outliers[data_no_outliers.group == 'Control'].order_value
sample2 = data_no_outliers[data_no_outliers.group == 'Experimental'].order_value
U1, pvalue = st.mannwhitneyu(sample1, sample2)

if pvalue > threshold:
    sign = '>'
    reject = 'no'
    equal = 'yes'
else:
    sign = '<='
    reject = 'yes'
    equal = 'no'

print("Mann-Whitney U test")
print(f"U1 = {round(U1, 1)}, p-value {sign} 0.05")
print(f"Reject null hypothesis: {reject}")
print(f"Distributions are same: {equal}")
