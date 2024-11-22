while True:
    a = int(input("몸무계를 입력 하시요: "))
    b = int(input("키를 입력하시요: "))
    hap = b * b / a
    if hap < 18.5:
        print("저체중")
    elif hap >= 23 and hap <= 29.9:
        print("정상")
    elif
