#  ECIE 3101 Semester 1 Session 23/24
#  Group member:

#Mohammad Fakhrul Amin Bin Zainor 1911309
#Khaled Emad Khaled AlBawaliz 1828405
#Ridhwan Syaafi bin Ma’ahad 1917147
#Muhammad Harith Danial bin Bazli 1923499





#formula of the output
def get_total(nums):
    return sum(nums)

def get_average(nums):
    return get_total(nums) / len(nums)

def get_max(nums):
    return max(nums)

def get_min(nums):
    return min(nums)

def get_range(nums):
    return get_max(nums) - get_min(nums)


#ask user to input number of elements
N = int(input("Please enter the desired number of elements: "))

#creating empty array
nums = []

#ask user to input numbers inside array
print("Enter the elements inside one by one:-")
#iterating untill the desired range
for i in range(N):
    num = int(input())
    nums.append(num) #adding nums of elements

#display output
print("\nThe output of the program:")
print(f"Total value: {get_total(nums)}")
print(f"Average value: {get_average(nums)}")
print(f"Maximum value: {get_max(nums)}")
print(f"Minimum value: {get_min(nums)}")
print(f"Range value: {get_range(nums)}")