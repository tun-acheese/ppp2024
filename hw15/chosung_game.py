
def get_chosung(text):
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    chosung = []
    for gulja in text:
        print(gulja,ord(gulja) - ord('가'))//588, (ord(*gulja) - ord('가'))%588)

    return chosung
    return "ㅍㅇㅅ"

def main:
    hidden_answer = "프원실"
    problem = get_chosung(hidden_answer)


    hidden_answer = "프원실"
    problem = get_chosung(hidden_answer)
    print(f"문제입니다. 주어진 초성은 {'',join'(problem)}'입니다.")

    answer = input("답은=>?")
    if answer == hidden_answer:
        print("정답입니다.")
    else:
        print("틀렸습니다.")

    if __name__=="_main_":
        main()