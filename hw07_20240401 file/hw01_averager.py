def average(nums):
    # return sum(nums)/len(nums)
    total = 0
    count = 0
    for num in nums:
        total += num
        count +=1

        return total / count
    
def main():
    numbers=[3, 5, 10, 15, 7]
    print(f"주어진 리스트의 평균은 {average(nums):.1f}입니다.")

if_name_=="__main__":
    main()