#==============================Abdalla Nassar============================
lst=[5,7,9,10,9,5,1,4,6,8,7,10,55,33,18,19,99,0]#list
lst = sorted(lst)#Sort the list
n = len(lst)#The number of values in the list

def measures_of_spread():
# --------------------------Max number----------------------------
    max_val = lst[-1]
#--------------------------min number-----------------------------
    min_val = lst[0]
# --------------------------Median number--------------------------
    if n % 2 == 0:
        median = (lst[n // 2] + lst[n // 2 - 1]) / 2  
    else:
        median = lst[n // 2]
#--------------------------Q1 and Q3 number--------------------------
    if n % 4 == 0:
        q1 = (lst[n // 4] + lst[n // 4 - 1]) / 2
        q1 = (lst[3 * n // 4] + lst[3 * n // 4 - 1]) / 2
    else:
        q1 = lst[n // 4]
        q3 = lst[3 * n // 4]
#---------------------------Range number-----------------------------
    Range = max_val - min_val
#--------------------------Interquartile range------------------------
    iqr = q3 - q1
#--------------------------mean number--------------------------------
    mean = sum(lst) / n
#-------------------------variance number-----------------------------
    variance = sum((x - mean) ** 2 for x in lst) / (n - 1)
#-------------------------standard deviation number--------------------
    std_dev = variance ** 0.5
#-------------------------End code-----------------------------
    return([min_val,q1,median,q3,max_val],[Range,iqr],['%.3f' % variance,'%.3f' % std_dev]) 
measures_of_spread()
print(measures_of_spread())
#==============================Abdalla Nassar============================
#==============================كلمه شكرا تكفي ==========================