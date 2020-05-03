# Test
Pycharm Project



########### STRUCTURE OF THE PROJECT ##########################################

# DATA MANIPULATION
#
# 1. IMPORT NUMPY AND PANDAS
#
# 1. 1 ASSIGNING DATASETS TO FD
#
# 1. 1. 1 DISPLAY FIRST 5 OF THE ENTIRE DATASET
#
# 2. TO VIEW EACH COLUMN NAME
#
# 2. 1 DELETE A SPECIFIC COLUMN
#
# 3. TO FIND TOTAL NUMBER OF ROWS
#
# 4. FETCH UNIQUE VALUES
#
# 4. 1
#
# 4. 2 DATASTRUCTURE IN PYTHON
#
# 5. TO DISPLAY DATASET WITH SPECIFIC CONSTRAINTS
#
# 6. CONVERT STRING TO FLOAT
#
# 7. TO CACULATE MAX VALUE AND PRINT THE ROW WHICH HAS THE MAXIMUM VALUE
#
# 7.1 MINIMUM VALUE
#
# DATA VISUALIZATION
#
# SET 1 FOR VALUES CITYNAME.INDEX AND CITYNAME.VALUES
#
# 1. BAR GRAPH
#
# 2. SCATTER PLOT
#
# 3. PIE CHART
#
# SET 2 FOR VALUES INVESTNAME.INDEX AND INVESTNAME.VALUES
#
# 1. BAR GRAPH
#
# 2. SCATTER PLOT
#
# 3. PIE CHART


# IMPORT NUMPY AND PANDAS
import matplotlib
import numpy as np
#adds support for large, multi-dimensional arrays and matrices
#along with a large collection of high-level mathematical functions to operate.

import pandas as pd
#high-performance,easy-to-use data structures

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
py.init_notebook_mode(connected=True)



# 1. 1 ASSIGNING DATASETS TO FD
#
# 1. 1. 1 DISPLAY FIRST 5 OF THE ENTIRE DATASET

fd = pd.read_csv("C:\\Users\\Siddharth\\Downloads\\startup_funding.csv",engine='python',encoding='latin')  # data processing, CSV file I/O (e.g. pd.read_csv)

print(fd.head(5))  #shows the first 5 DATASET
print("\n")

# Data Shape and structure
print("Shape of the given data is : ",fd.shape)

# 2. TO VIEW EACH COLUMN NAME ##########################################################3

print(*fd.columns)
print("\n")

print(fd.columns)
print("\n")

# 2. 1 DELETE A SPECIFIC COLUMN ###########################################################

del fd['Remarks'] #del - command
fd.head(5)
print("\n")

# 3. TO FIND TOTAL NUMBER OF ROWS

leng=len(fd.index)+1  #find length

print(leng,"ROWS are present in this DATASET")
print("\n")

# 4. FETCH UNIQUE VALUES#######################################################################################

name = fd['InvestorsName'].unique()   #stores unique values of INVESTORS NAME
amount = fd['AmountInUSD'].unique()   #stores unique values of INVESTORS NAME


print(*amount[:5])
print("\n")

print(amount[:7])
print("\n")

print(type(amount))
print("\n")

#to find unique names of listed cities

uni_city = [] #array declaration
uni_city = fd['CityLocation'].unique() #to find unique
print("\n")

uni_city1 = fd['CityLocation'].value_counts() #to count values in list.
print("\n")

print("Total number of different cities are : ",len(uni_city))
print("\n")

print("Total number of different cities are : ",len(uni_city1))
print("\n")

print(uni_city[:7])
print("\n")

print(type(uni_city))
print("\n")

# DATA STRUCTURES & ALGORITHMS IN PYTHON

# 1. LIST

uni_city_list=np.array(uni_city).tolist()  #converts np.array to list

uni_city_list.append('R.m.d')   #appends RMD

print(uni_city_list[:5])
print("\n")

print("The length of the above list is : ", len(uni_city_list))   #prints len of list
print("\n")

print(type(uni_city_list))
print("\n")

# 2. DICTIONARY ####################################

startup={}      ## making a key-value pair of dictionary
print(type(startup))

for i in range(0,len(uni_city)):
    startup[uni_city[i]]=amount[i];
for i,j in startup.items():          ## printing the key value pairs of the entire dictionary
    print(i,":",j)

print("\n")
print(startup)        ## printing whole dictionary
print("\n")

# 5. TO DISPLAY DATASET WITH SPECIFIC CONSTRAINTS

print(fd[fd.CityLocation == 'Chennai'].head(5))
print("\n")

print(fd[fd['CityLocation'] == 'Chennai'].head(5))
print("\n")

# 6. CONVERT STRING TO FLOAT

#to convert string to float

fd["AmountInUSD"] = fd["AmountInUSD"].apply(lambda x: float(str(x).replace(",",""))) #expression conversion is done using lambda
fd["AmountInUSD"] = pd.to_numeric(fd["AmountInUSD"]) #now those amount are converted to numeric format

print(fd.head(5))
print("\n")

# 6.1 CONVERSION OF NaN TO 0 #########################################################

#to convert NaN (Not a NUMBER) to 0

fd.fillna(0)

print(fd.fillna(0).head())
print("\n")

#total

val = fd['AmountInUSD'].sum()       #which sums up all the values in the row "AmountInUSD"

val1 = fd.AmountInUSD.sum()    # Alternate way   #which sums up all the values in the row "AmountInUSD"


print("Total funding amount : ",val)   #print total
print("Total funding amount : ",val1)   #print total
print("\n")

#to calculate max value and to print the max row

max_invest=max(fd['AmountInUSD'])  #find max
max_invest1=max(fd.AmountInUSD)  #find max          ## just an Alternate way for max

print("maximum amount invested",max_invest)
print("maximum amount invested",max_invest1) ## just an Alternate way for max
print("\n")

max_index=fd['AmountInUSD'].idxmax()   #to assign max amount's index value
max_index1=fd.AmountInUSD.idxmax()   #to assign max amount's index value

print(fd.iloc[[max_index]])     #  #print the max row
print(fd.iloc[[max_index1]])     #  #print the max row
print("\n")

# 7.1 MINIMUM VALUE

min_invest=min(fd['AmountInUSD'])
min_invest1=min(fd.AmountInUSD)
print("\n")

print("minimum amount invested",min_invest)   #find min
print("minimum amount invested",min_invest1)  #find min     ## just an Alternate way for min
print("\n")

min_index=fd['AmountInUSD'].idxmin()   #to assign min amount's index value
min_index1=fd.AmountInUSD.idxmin()   #to assign min amount's index value


print(fd.iloc[[min_index]])   #print the min row
print(fd.iloc[[min_index1]])   #print the min row


# DATA VISUALIZATION ##########################################################################

# SET 1 FOR VALUES CITYNAME.INDEX AND CITYNAME.VALUES
#
# 1. BAR GRAPH

cityname = fd['CityLocation'].value_counts().head(10)
plt.figure(figsize=(15,8))
sns.barplot(cityname.index, cityname.values)
plt.xticks(rotation='vertical')
plt.xlabel('Cities Name')
plt.ylabel('Number of STARTUPS in each cities')

plt.show()

#fd.loc[fd['CityLocation'] == "Mumbai", 'AmountInUSD']

#total = fd.loc[fd['CityLocation'] == "Bangalore", 'StartupName'].sum()

x=0
for i in cityname.index:
    print("Number of STARTUPS in",i, "are",cityname.values[x])
    x=x+1

print(fd['CityLocation'].value_counts().head(10))

print(cityname.index)
print(*cityname.index)
print(cityname.values)

# 2. SCATTER PLOT ##################################################

plt.scatter(cityname.index,cityname.values)
plt.xticks(rotation='vertical')
plt.xlabel('Cities Name')
plt.ylabel('Number of STARTUPS in each cities')
plt.show()

# 3. PIE CHART
plt.pie(cityname.values, labels = cityname.index, autopct = "%.01f")
plt.show()

# SET 2 FOR VALUES INVESTNAME.INDEX AND INVESTNAME.VALUES #############################################################

# 1. BAR GRAPH ####################

investname = fd['InvestorsName'].value_counts().head(5)
plt.figure(figsize=(15,8))
sns.barplot(investname.index, investname.values)
#plt.xticks(rotation='vertical')
plt.xlabel('Investors Name')
plt.ylabel('No. of Investments made')

plt.show()

x=0
for i in investname.index:
    print("Investments made by",i, "on",investname.values[x],"startups")
    x=x+1

print(fd['InvestorsName'].value_counts())

# 2. SCATTER PLOT

plt.scatter(investname.index,investname.values)
plt.xticks(rotation='vertical')
plt.xlabel('Investors Name')
plt.ylabel('No. of Investments made')

plt.show()

#3. PIE CHART

plt.pie(investname.values, labels = investname.index, autopct = "%.01f")
plt.show()

