#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


def initializeArray(numbers,n):
    for i in range(n):
        numbers.append(int(input("numbers["+str(i)+"]: ")))
    return numbers

def printArray(numbers,n):
    for i in range(n):
        print(numbers[i])


def twoSumONSquared(numbers,n,target):
    for i in range(n):
        for j in range(0,n):
            if(numbers[i] + numbers[j] == target and i != j):
                print(str(i)+" "+str(j))
                return 0
            
def twoSwumON(numbers,n,target):
    complement_dict = {}

    for i in range(n):
        complement = target - numbers[i]
        if complement in complement_dict:
            print([complement_dict[complement],i])
            return 0

        complement_dict[numbers[i]] = i
    
    print("No such pair found!")
    return 0

numbers = []
n = int(input("n: "))
target = int(input("target: "))
numbers = initializeArray(numbers,n)
twoSumONSquared(numbers,n,target)