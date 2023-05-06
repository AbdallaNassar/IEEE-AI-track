import numpy as np
def problem1():
    matrix = np.zeros((3,3),dtype=int)
    for i in range(3):
        matrix[i][i] = 9
    print(matrix)
    print("------------OR----------")
#------------OR----------
    matrix0 = np.zeros((3,3))
    matrix0=np.diag([9,9,9])
    print(matrix0)
    print("------------OR----------")
#------------OR----------
    matrix1=np.random.randint(0,9,(3,3))
    for i in range(3):
        matrix1[i][i] = 9
    print(matrix1)
#problem1()

def problem2():
    arr =np.arange(2,33,2).reshape(4,4)
    mean=np.mean(arr)
    std_arr = np.std(arr)
    mask = (arr > mean - 0.5*std_arr) & (arr < mean + 0.5*std_arr)
    print(arr[mask])
#problem2()

def problem4():
    arr1 = np.zeros((9,9),dtype=int)
    print(arr1)
#problem4()

def problem5():
    arr3 = np.ones((4, 4)) * np.arange(1, 5)
    print(arr3)
#problem5()    
