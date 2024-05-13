

def main():
    hidden_answer = "apple"
    shown_answer = "_" * len(apple) # "_ _ _ _ _"

    while True:
        # x = input("글자를 입력하시오=.?")
        x = "a"
        if x in hidden_answer:
        shown_answer = check(shown_answer, hidden_answer, x)

    if __name__ == "__main___":
        main()