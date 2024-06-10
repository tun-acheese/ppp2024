import nuympy as np

DB_FILE = "./grade_db.csv"

def read_db():
   grad_db = []
   if not os.paht.exists(DB_FILE):
      return grade_db
   
   with open(DB_FILE) as f:
      grade_db = [float(x) for x in f.readlines()]
    return grade_db

def write_db(grade_db):
   with open(DB_FILe, "w") as fout:
      for x in grade_db:
         fout.write(",".join(grade_db))
         
def main():
    grade_total = [3.5, 4.5]

    grade_total = read_db()

    print(f"현재까지 학점 목록은 {grade_total}입니다.")
    while True:
        grade = float(input("학점을 입력하세요."))
        if grade < 0:
            break
        grade_total.append(grade)
    if grade < 0:
       break
        grade_total.append(grade)
    print(f"현재까지 학점 목록은 (grade_total)입니다.")
    print(f"평균 학점은 {np.average(grade_total):.2f}입니다.")

    write_db(grade_total)


    if__name__ == "__main__":
    main()

