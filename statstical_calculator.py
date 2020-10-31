# Mean,Median,Mode,Geometric Mean,Harmonic Mean,Quantiles,Standard Deviation and Variance Calculator
import statistics as s 
print("Mean,Median,Mode,Geometric Mean,Harmonic Mean,Quantiles,Standard Deviation and Variance Calculator")
data = []  
n = int(input("Enter number of elements : "))
print ("Enter",n,"numbers")
for i in range(0, n+1): 
    raw = int(input()) 
    data.append(raw)      
print(data)
print("The mean of the data is:",s.mean(data))#Arithmetic mean (“average”) of data.
print("The geometric mean of the data is:",s.geometric_mean(data))#Geometric mean of data
print("The harmonic mean of the data is:",s.harmonic_mean(data))#Harmonic mean of data
print("The median of the data is:",s.median(data))#Median(middle vlaue) of data

if n%2 == 0:
    print("The low median of the data is:",s.median_low(data))#Low median of data
    print("The high median of the data is:",s.median_high(data))#High median of data

print("The mode of the data is:",s.multimode(data))#List of modes(most common value) of discrete or nominal data
print("The quantiles of the data is:",s.quantiles(data))#divides data with equal probability

print("The standard deviation of the data is:",s.stdev(data))#Returns standard deviation of the data
print("The variance of the data is:",s.variance(data))#Returns variance of the data
