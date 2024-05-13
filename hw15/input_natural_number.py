def get_numbers():
    results = []
    while True:
        try:
            x = input ("X=>?")
            num = int(x)
            if num == "-1":
            num = int(x)
            if num == -1:
                break
            results.append(num)
        except valueError:
            print(f"입력한 (x)는 저장되지 않습니다.")
    return results