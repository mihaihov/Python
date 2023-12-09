#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


def initializeArray(numbers,n):
    for i in range(0,n):
        numbers.append(int(input("numbers["+str(i)+"]: ")))
    return numbers

def printArray(numbers,n):
    for i in range(0,n):
        print(numbers[i])


def twoSum(numbers,n,target):
    for i in range(0,n):
        for j in range(0,n):
            if(numbers[i] + numbers[j] == target and i != j):
                print(str(i)+" "+str(j))
                return 0


numbers = []
n = int(input("n: "))
target = int(input("target: "))
numbers = initializeArray(numbers,n)
twoSum(numbers,n,target)