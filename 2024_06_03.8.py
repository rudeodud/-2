figure = int(input("숫자를 입력 하십시오(1:사각형 2:삼각형 3:원)"))

if figure == 1:
    bottom = int(input("밑변을 입력"))
    height = int(input("높이를 입력"))
    num = bottom * height
    print(num,"cm²")
elif figure == 2:
    bottom = int(input("밑변을 입력"))
    height = int(input("높이를 입력"))
    num = bottom * height / 2
    print(num,"cm²")
elif figure == 3:
    radius = int(input("반지름을 입력"))
    num = radius * radius * 3.14
    print(num,"πcm²")
else:
    print("없는 값")
