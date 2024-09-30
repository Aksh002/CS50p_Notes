'''
from scipy.stats import skew 
  
# Creating a dataset 
dataset = [88, 85, 82, 97, 67, 77, 74, 86,  
           81, 95, 77, 88, 85, 76, 81] 
  
# Calculate the skewness 
print(skew(dataset, axis=0, bias=True))
'''
a=input()
if a%2|3|5|6|