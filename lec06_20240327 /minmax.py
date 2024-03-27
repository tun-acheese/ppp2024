def minmax(nums):
    max_num = max(nums)
    min_num = min(nums)
    return min_num, max_num

def main():
    nums = [3, 5, 7, 4, 10, 2]
    mn, mx = minmax(nums)

    print(f"최솟값은 {mn}, 최댓값은 {mx}")

if __name__ == "__main__ ":
    main()