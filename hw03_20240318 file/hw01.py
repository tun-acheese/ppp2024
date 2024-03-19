import math
weight=input("몸무게를 입력하시오.")
height=input("키를 입력하시오.")
BMI=int(weight)/(int(height)/100)*(int(height)/100)
   print("BMI=",BMI)
    
if BMI<23:
  print("비만 의심 증상이 없습니다.")
elif 23<=BMI and BMI <=24.9:
   print("비만 전단계")
elif 25<=BMI and BMI <=29.9:
   print("1단계 비만")
elif 30<=BMI and BMI <=34.9:
 print("2단계 비만")
else:
 print("3단계 비만")
