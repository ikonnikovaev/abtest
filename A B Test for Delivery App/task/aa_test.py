# write your code here
import pandas as pd
import scipy.stats as st
from statsmodels.stats.power import TTestIndPower

data_aa = pd.read_csv('aa_test.csv')
#print(data)
sample1 = data_aa['Sample 1']
sample2 = data_aa['Sample 2']
#print(sample1, sample2)

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
analysis = TTestIndPower()
result = analysis.solve_power(effect_size=0.2, nobs1=None, alpha=0.05, power=0.8, ratio=1.0)
print(f"Sample Size: {int(round(result, -2))}")
data_ab = pd.read_csv('ab_test.csv')
#print(data_ab.columns)
vc = data_ab['group'].value_counts()
print(f"Control group: {vc['Control']}")
print(f"Experimental group: {vc['Experimental']}")
