def text2list(input_text):
    return [int(x) for x in input_text.split()]

def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    return nums[len(nums)//2]
def main(): 
    input_text = "5 10 3 4 7"