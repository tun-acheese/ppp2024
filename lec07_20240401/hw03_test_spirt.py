def main():
    inpu_text = "5, 10 ,3 ,4 ,7"
    tokens= = input_text.split(",")
    # print(sum(tokens))
    results = []
    for token in tokens:
        results.append(int(token))
    print(max(results))
 
    results2 = [int(x) for x in input_text.split(",")]
    print(results2)
 \
if __name__ == "__main__":
    main():