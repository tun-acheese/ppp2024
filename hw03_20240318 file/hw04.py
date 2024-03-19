import math
radius = input ("반지름을 입력하시오.")

# 원의 둘레 소수점 1의 자리까지
circumference =  int(radius)*2*3.141592
circumference = "%0.1f" % circumference
print("원의 둘레=",circumference)

#원의 넓이 소수점 2의 자리까지
circle_area = int(radius)*int(radius)*3.141592
circle_area = "%0.2f" % circle_area
print("원의 면적=",circle_area)
