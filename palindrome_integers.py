def palindrome(nums):
    for num in nums:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palindrome(numbers)


# string[::-1] дава ни стринга на обратно асд = дса