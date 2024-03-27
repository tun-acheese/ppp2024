#첫 번째 방법
def largest(nums):
    largest_num = nums[0]
    for num in nums;
        if largest_num < num:
            largest_num = num
    return largest_num

def main():
    x = [3, 7, 5, 6, 3]
    print(f"최대값은 {largest(x)입니다.}")


if __name__ == "__main__":
    main()

#두 번째 방법
def largest(nums):
   return max(nums) 

def main():
    x = [3, 7, 5, 6, 3]
    print(f"최대값은 {largest(x)입니다.}")


if __name__ == "__main__":
    main()