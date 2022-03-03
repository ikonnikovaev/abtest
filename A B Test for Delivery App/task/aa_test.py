# write your code here
import pandas as pd
import scipy.stats as st

data = pd.read_csv('aa_test.csv')
#print(data)
sample1 = data['Sample 1']
sample2 = data['Sample 2']
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

print("Levene's test")
print(f"W = {round(W, 3)}, p-value {sign} 0.05")
print(f"Reject null hypothesis: {reject}")
print(f"Variances are equal: {equal}")
print()

t, pvalue = st.ttest_ind(sample1, sample2)

if pvalue > threshold:
    sign = '>'
    reject = 'no'
    equal = 'yes'
else:
    sign = '<='
    reject = 'yes'
    equal = 'no'
print("T-test")
print(f"t = {round(t, 3)}, p-value {sign} 0.05")
print(f"Reject null hypothesis: {reject}")
print(f"Means are equal: {equal}")


