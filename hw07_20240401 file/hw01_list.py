def main():
    input_text = "5 10 3 4 7"
    nums = text2list(input_text)
    print("주어진 리스트는",nums)
    print("평균값은{:.1}".format(average(nums))
    print("중앙값은 {}".format(median(nums))
    #단 갯수가 짝수일때는 중앙에 위치한 두 값 중 큰 값을 채택한다
    print(f"최솟값은{}")
    print(f"최댓값은{}")
if__name__=="__main__": 
    main()