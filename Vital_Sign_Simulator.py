#               Programming with Data – CW II
#                   Problem solving and Scalability

# Phase 1: MyHealthcare device: Vital signs simulator

import random as rand
import matplotlib.pyplot as plt
import pandas as pd
import time

n=1000 # n is the vital sign records of a person

def myHealthcare(n):
    rand.seed(404)
    vital_sign_records = []
    for i in range(n):
        ts = i
        Temperature = rand.randint(36,39)
        Heart_rate = rand.randint(55,100)
        Pulse  = rand.randint(55,100)
        Blood_pressure = rand.randint(120,121)
        Respiratory_rate = rand.randint(11,17)
        Oxygen_saturation = rand.randint(93,100)
        ph = rand.uniform(7.1,7.6)
        vital_sign_records.append([ts,Temperature,Heart_rate,Pulse,Blood_pressure,Respiratory_rate,Oxygen_saturation,round(ph,1)])
    return vital_sign_records

vital_sign_records = myHealthcare(n)

for i in range(n): # in order to more useful and eye-pleasing using, we create a data frame
    data_frame_1 = pd.DataFrame(vital_sign_records,columns=["ts","temp","hr","pulse","bloodpr","resrate","oxsat","ph"],dtype=int)

print("----Answer: - 1---------Answer: - 1---------------Answer: - 1-------------")

print(data_frame_1)


#     Phase 2: Run analytics

#Develop a Python function for each of the following analytics:
#2 - a) Find abnormal values for pulse or blood pressure.

k1=50 # to select a small sample we chose the number 50 and we will find the abnormal pulse rate for the selected 50 samples
def abnormal_Sign_Analytics(k1):
        abnormal_pulse_count = 0
        alist1=[]
        for i in range(k1):
            if not (60<= int(vital_sign_records[i][3]) <= 99) :
                alist1.append((vital_sign_records[i][0],vital_sign_records[i][3]))
                abnormal_pulse_count = 1 + abnormal_pulse_count
        return ["Abnormal Pulse count :" , abnormal_pulse_count , " ---> " ,alist1]
print("----Answer: - 2-a--------Answer: - 2-a---------------Answer: - 2-a -------------")  
print(abnormal_Sign_Analytics(k1))

# 2- b) Present a frequency histogram of pulse rates.

# instead of limiting our samples with the abnormal values of the 50 samples ,
#in this step we use all values we have in the selected 50 samples 

def frequency_Analytics(k1): 
    alist3 = vital_sign_records
    dict1={}
    for i in range(k1):
        if alist3[i][3] in dict1:
            dict1[alist3[i][3]] += 1
        else:
            dict1[alist3[i][3]] = 1
    return dict1


answer2b=frequency_Analytics(k1)

print("----Answer: - 2-b--------Answer: - 2-b---------------Answer: - 2-b -------------")  

print(answer2b)

# to show our all pulse rates (including abnormal ones) within the selected samples, we will plot our results on this step

figure1 = plt.figure(1)
hist = data_frame_1["pulse"][:50].hist(bins=50)
plt.xlabel('Pulse Rates')
plt.ylabel('Frequency')
plt.title('Pulse Rates Frequency Histogram')
plt.show()

# 2 - c) Plot the results for 2a and 2b and briefly discuss your observations. What is the
#        complexity of your algorithm?

print("----Answer: - 2-c--------Answer: - 2-c---------------Answer: - 2-c -------------")  

data_frame_2=data_frame_1[:50]
data_frame_2=data_frame_2.sort_values(by=["pulse"])

# to more easier understanding and more interpretability, we will plot our results in the same graph on this step

plt.plot(list(data_frame_2["pulse"]), list(data_frame_2["ts"]), color='green',marker='+',alpha=0.4,label="movement of pulse rates")
plt.scatter(list(data_frame_2["pulse"]), list(data_frame_2["ts"]), color='blue',marker="D",s=20,label='normal')
plt.scatter([i[1] for i in abnormal_Sign_Analytics(k1)[3]],[i[0] for i in abnormal_Sign_Analytics(k1)[3]],marker="d",color='orange',label='abnormal',s=70)
plt.xlabel('Pulse Rates')
plt.ylabel('Frequency')
plt.title('Pulse Rates Frequency Graph',color="red")
plt.legend()
plt.show()


#               Phase 3: Search for heart rates using the HealthAnalyzer
# 3- a) Design a solution (where pulse value is 56)

print("----Answer: - 3-a--------Answer: - 3-a---------------Answer: - 3-a -------------")  

x1=56 # with the given pulse rate 56, first we need to sort our values in order to able to use binary searching method.

#that's why, for the less consumption of time and memory we use  we use default sorting method of Python which is TimSort

def HealthAnalyzer_L(x1): #Linear Search doesn`t require any sorting so we don`t need to sort our values
    alist4=[]
    for i in range(n):
        if int((vital_sign_records[i])[3]) == x1: # if our value equals to the wanted one , let`s add it to the alist4
            alist4.append(list(vital_sign_records[i]))
    return alist4

print("If we use Linear Search Method, we will find that : ")
print(*HealthAnalyzer_L(x1), sep=" \n ")

#we will get a slice of lists where we FIRST encounter with the wanted value

def first_occurence_of_the_pulse_rate(alist5, n, x1):
    first=0  #first index of list
    last=len(alist5)-1  #last index of list
    while first <= last:     
        mid = first + (last - first) // 2
        if (mid == 0 or x1 > int(alist5[mid - 1][n])) and int(alist5[mid][n]) == x1 : 
            return mid 
        elif x1 > int(alist5[mid][n]) : 
            first=mid+1            
        else : 
            last=mid-1      
            
#we will get a slice of lists where we LAST encounter with the wanted value    

def last_occurence_of_the_pulse_rate(alist5,n, x1) : 
    first=0  #first index of list
    last=len(alist5)-1  #last index of list
    while first <= last:     
        mid = first + (last - first) // 2
        if (mid == last or x1 < int(alist5[mid + 1][n])) and int(alist5[mid][n]) == x1: 
            return mid 
        elif x1 < int(alist5[mid][n]): 
            last=mid-1                       
        else : 
            first=mid+1   
            
# the slices will give us the wanted multidimensional list 

def HealthAnalyzer_B(alist6, x1):
    alist5=sorted(alist6, key = lambda x2: x2[3]) # this line for sorting our values (Pulse Rates) using TimSort
    return alist5[first_occurence_of_the_pulse_rate(alist5,3,x1):(last_occurence_of_the_pulse_rate(alist5,3,x1)+1)]

print("If we use Binary Search Method, we will find that : ")
print(*HealthAnalyzer_B(vital_sign_records,x1), sep=" \n ")

# 3 - b) What is the complexity of your solution?

print("----Answer: - 3-b--------Answer: - 3-b---------------Answer: - 3-b -------------")  

# to make comparisons between time of the searching methods first we calculate the time of the operations

Linear_time = 0
for _ in range(1000):
    start, end = 0, 0
    start=time.time()
    HealthAnalyzer_L(56)
    end=time.time()
    Linear_time += (end-start)
    
print("Linear Operation Time for 1000 times of running of our program : ",(Linear_time))

Binary_time = 0
for _ in range(1000):
    start, end = 0, 0
    start=time.time()
    HealthAnalyzer_B(vital_sign_records,56)
    end=time.time()
    Binary_time += (end-start)
    
print("Binary Operation Time for 1000 times of running of our program : ",(Binary_time))

#Now we have the operation time , So we can find which searching method is the best possible solution for our problem

print("Is the Linear Operation Time greater than the Binary Operation Time : " ,bool( (Linear_time)>(Binary_time)))

# 3 - c) Plot the heart rate values for records having pulse rate 56.

print("----Answer: - 3-c--------Answer: - 3-c---------------Answer: - 3-c -------------")  

# to visualise the heart rates having pulse rate 56, let`s use the scatter method of the values ,
# and to show changing of the values let`s use the line plot method

plt.plot([i[0] for i in HealthAnalyzer_B(vital_sign_records,x1) if not( (54 < i[2]< 60)or(i[2]==100))],[i[2] for i in HealthAnalyzer_B(vital_sign_records,x1) if not( (54 < i[2]< 60)or(i[2]==100))], color='orange',marker='o')
plt.scatter([i[0] for i in HealthAnalyzer_B(vital_sign_records,x1) if not( (54 < i[2]< 60)or(i[2]==100))],[i[2] for i in HealthAnalyzer_B(vital_sign_records,x1) if not( (54 < i[2]< 60)or(i[2]==100))],color='orange',label='normal')
plt.scatter([i[0] for i in HealthAnalyzer_B(vital_sign_records,x1) if( (54 < i[2]< 60)or(i[2]==100))],[i[2] for i in HealthAnalyzer_B(vital_sign_records,x1) if( (54 < i[2]< 60)or(i[2]==100))],color='blue',label='abnormal')
plt.title('Heart Rate Values Having 56 Pulse Rate Frequency',fontsize=10, color='red')
plt.xlabel('Frequency')
plt.ylabel('Heart Rate')
plt.legend()

plt.grid(axis='y',alpha=0.60)
plt.show()


#           Phase 4: Testing scalability of your algorithm
#Benchmark the MyHealthData application simulating n = 1000, 2500, 5000, 7500 and
#10000 records from phase 1 (MyHealthcare device).

# 4 - a) Measure the running time and plot the results for different n values.

print("----Answer: - 4-a--------Answer: - 4-a---------------Answer: - 4-a -------------")  

# in order to Measure the running time , let`s create a function which counts the time

def benchmarking(myHealthcare,samples):
    time_count = {}
    for i in samples:
        start,end = 0,0
        start = time.time()
        myHealthcare(i)
        end=time.time()
        time_count[i]=end-start
    return time_count

samples=[1000,2500,5000,7500,10000]

# in order to more useful and eye-pleasing using, we create a data frame
#we use the given simulating n variables (samples) 

data_frame_2 = pd.DataFrame(index=samples)

fig,ax = plt.subplots(1,10, figsize=(10, 5), sharey=True)

for i in range(10):# let`s run our program 10 times and plot 10 graphes in order to see the differance of the runs
  
    data2=benchmarking(myHealthcare,samples)
    data_frame_2['Sample '+ str(i+1)]=list(data2.values())
    ax[i].plot(list(data2.keys()), list(data2.values()) ,linewidth=4.0)
    ax[i].set_title('Sample '+ str(i+1),fontsize=10, color='green')

plt.show()

print(data_frame_2)



# 4 -b) Present diagrams and discussions in the report.

print("----Answer: - 4-b--------Answer: - 4-b---------------Answer: - 4-b -------------") 
 
data_frame_2_trans=data_frame_2.transpose() 

fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=False, figsize=(20,10))

data_frame_2.plot.line(ax=ax1,legend=True,linewidth=3.0)

ax1.set_title("Sample results",y=1, color='green')

data_frame_2_trans.plot.line(ax=ax2, legend=True,linewidth=4.0)

ax2.set_title("Comparison of each n-record",y=1., color='blue')

plt.show()

