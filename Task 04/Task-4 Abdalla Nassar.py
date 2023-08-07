import numpy #pip install numpy
numbers = list(map(int, input("Enter numbers: ").split()))
numbers.sort()
#------------------------------Mean------------------------------------------------
def Mean ():
    mean = numpy.mean(numbers)
    print("The mean of this data set is = ", mean)
#-------------------------------------------------
    mean1 = sum(numbers) / len(numbers)
    print("The mean of this data set is = ", mean1)
#Mean ()

#------------------------------Median------------------------------------------------
def Median ():
    median = numpy.median(numbers)
    print("The median of this data set is = ", median)
#-----------------------------------------------
    if(len(numbers)%2==0):
        median = (numbers[len(numbers)//2]+numbers[len(numbers)//2-1])/2
        print("The median of this data set is = ", median)
    else:
        median = numbers[len(numbers)//2]
        print("The median of this data set is = ", median)
#Median ()

#------------------------------Mode------------------------------------------------
def Mode ():
    mode = max(set(numbers), key = numbers.count)
    print("The mode of this data set is = ", mode)
Mode ()