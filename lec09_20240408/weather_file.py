def read_tmax(filename):
    # return [3,5,5,7,10]
    results = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tmax = float(tokens[5])
            results.append(tmax)
    return results

def read_weather(filename, col_idx):
    # return [3,5,5,7,10]
    results = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tmax = float(tokens[5])
            results.append(tmax)
    return results





def main():
    tmax = read_tmax("lec06/weather(146)_2022-2022.csv")
    tmax = read_tmin("lec06/weather(146)_2022-2022.csv")
    print("연 최고 온도(max(tmax))는 {max(tmax):.1f}입니다.")
    print("연 최wj 온도(min(tmax))는 {min(tmax):.1f}입니다.")

if __name__ == "__main__":
    main()










    def main():
        tmax = read_tmax("lec06/weather(146)_2022_2022.csv")
        tmin = read_tmin("lec06/weather(146)_2022_2022.csv")

        tmax = read_weather("lec06/weather(146)_2022_2022.csv", 3)
        tmin = read_weather("lec06/weather(146)_2022_2022.csv", 5)

         print("연 최고 온도(max(tmax))는 {max(tmax):.1f}입니다.")
         print("연 최저 온도(min(tmax))는 {min(tmax):.1f}입니다.")
