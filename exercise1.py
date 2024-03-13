# Write a function that takes a list of integers and returns the median value. *Can assume that the list of integers is sorted in ascending value*.


def mean(nums):
    # make a variable to store the sum of all numbers
    total = 0

    # go through each number in the list
    for num in nums:
        # change the number to a float and add it to the total
        total += float(num)

    # find the mean by dividing the total sum by the number of elements in the list
    median = total / len(nums)
    return median


# list of numbers
nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# call the mean function with the list of numbers and store the result in a variable
mean_result = mean(nums_list)

# print the mean value
print(mean_result)
