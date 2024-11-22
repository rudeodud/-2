print("1번을 누르면 삼각형의 넓이")
print("2번을 누르면 사각형의 넓이")
print("3번을 누르면 원의 넓이")


Figure = int(input("번호를 누르시오(1,2,3):"))
if Figure == 1 :
    area1 = int(input("밑변의 길이:"))
    area2 = int(input("높이: "))
    Arearesult = area1 * area2 / 2
    print("삼각형의 넓이",Arearesult,"cm²")
elif Figure == 2:
    area1 = int(input("가로의 길이:"))
    area2 = int(input("세로의 길이:"))
    Arearesult = area1 * area2
    print("삼각형의 넓이",Arearesult,"cm²")
elif Figure == 3:
    radius = int(input("원의 반지름:"))
    Arearesult = 2 * 3.14 * radius
    print("원의 넓이는",Arearesult,"cm²")
else:
    print("존재 하지 않은 값입니다")
    
    
    
    
