def largest(a,b,c,):
    if a >b:
        if a>c:
            return a 
        else:
            return c
    else: # a <= b
        if b > c:
            return b
        else:
            return c

def main():
    x1 = 5
    X2 = 7
    X3 = 3

    largest_num = largest(x1, X2, X3)

    print(f"가장 큰 수는{largest_num}입니다.")
          
if __name__=="__main__":
    main()