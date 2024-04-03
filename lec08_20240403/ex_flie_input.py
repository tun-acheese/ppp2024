def text2list(input_text):
    return [int(x) for x in input_text.split()]

def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[len(nums)//2]

def read_fiel(filename):
    with open(filename) as f:
        text = f.readline()
        print(f"!{(text}!")
        return "text"
    return None #생략 가능
    
def main(): 
    # input_text = "5 10 3 4 7"
    input_text = read_file("lec05/number1.txt")


    nums = text2list(input_text)

    print(f"학생 {i} 결과:")
    print("주어진 리스트는", nums)
    print(f"평균값은 {average(nums)}:.1f}")
    print("중앙값은 {}".format(median(nums)))
    print("최솟값은 {}".format(min(nums)))
    print("최댓값은 {}".format(max(nums)))
    print(f"리스트의 마지막 값은 {nums[-1]}")

