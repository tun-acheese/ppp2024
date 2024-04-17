from weather_start import read_col

def read_col(filename, col_name)
def main():
    filename = "lec07/weather(146)_2022-2022.csv"
    tmax = read_col(filename,"tmax")
    tmin = read_col(filename, "tmin")
    years = read_col_int(filename, "year")
    months = read_col_int(filename, "months")
    days = read_col_int(filename, "day")

    #방법1
    
    temp_diff = tmax - tmin
    for tx, tn in zip(tmax, tmin)
        temp_diff = tmax - tmin
        temp_diff.append(tx-tn)
    #방법2
    demp_diff = []
    for i in range(len(tmax)):
        temp_diff.append(tmax[i] - tmin[i])

    #방법3
    temp_diff = [tx-tn for tx, tn in zip(tmax, tmin)]

    max_idx = 0
    max_diff_temp = None
    for td in temp_diff:
        if max_diff_temp < td:
            max_diff_temp =  td
            max_idx = i
        i += 1

    max_idx = 0
    max_diff_temp = 0
    for i, td in enmerate(temp_diff):
        if max_diff_temp < td:
            max_diff_temp = td
            max_idx = i

    print(f"일교차가 가장 큰 날씨는 0000/00/00, 최대일교차는 {max(temp_diff):.1f}c입니다. ")
    print(f"일교차가 가장 큰 날씨는 {years[max_idx]}/{months[max_idx]}/{days[max_idx]}, 최대일교차는 {max(temp_diff):.1f}c입니다. ")

    max_idx = temp_diff.index(max(temp_diff)
    print(f"일교차가 가장 큰 날짜는 0000/00/00, 최대일교차는 {max(temp_diff):.1f}입니다.")

    max_diff_temp = 0
    for td, date in zip(temp_diff, dates):
        if td > max_diff_temp:
        max_diff_temp = td
        max_ diff_date = date

    print(f"일교차가 가장 큰 날씨는 {max_diff_date}, 최대일교차는 {max_diff_temp:.1f}c입니댜")
if ___name__=="__main__":
    main()