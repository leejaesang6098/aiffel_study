def numbers():
    arr = []
    while True:
        number = input("Enter a number ('q' key to quit): ")
        while number != "q":
            try:
                x = float(number)
                arr.append(x)
            except ValueError:
                print("Not a number please input number")
            number = input("Enter a number ('q' key to quit): ")
        if len(arr) > 1:
            return arr


arr = numbers()
print("arr: ", arr)


# def aver():
#     total = 0
#     count = 0
#     nums = input('Enter a number: (input "q" to quit) ')
#
#     while nums != "q":
#         try:
#             x = float(nums)
#             total += x
#             count += 1
#         except ValueError:
#             print('Not a number! please input just number')
#
#         nums = input('Enter a number: (input "q" to quit) ')
#
#     return total / count
#
# print(aver())

def mean(nums):
    return sum(nums) / len(nums)


avg = mean(arr)
print("mean: ", avg)


def median(nums):
    nums.sort()
    x = len(nums) // 2
    if len(nums) % 2:
        return nums[x]
    else:
        return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2


med = median(arr)
print("median: ", med)


def std_dev(nums):
    x = 0.0
    for i in nums:
        x += (i - (sum(nums) / len(nums))) ** 2  # 각 숫자와 평균값의 차이의 제곱을 계속 더함
    return (x / len(nums)) ** 0.5  # 그 총합을 숫자갯수로 나눈 값의 제곱근을 리턴


std = std_dev(arr)
print("std_dev: ", std)
