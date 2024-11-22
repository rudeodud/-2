

while True :
    a = int(input("계산할 첫 번째 수를 입력하세요: "))
    b = int(input("계산할 두 번째 수를 입력하세요: "))
    c = (input("연산자 를 입력 하시요: "))
    hap = 0
    if c ==  '+' :
        hap = a + b
        print("%d + %d = %d" %(a, b, hap))
    elif c == '-':
        hap = a - b
        print("%d - %d = %d" %(a, b, hap))
    elif c == '*':
        hap = a * b
        print("%d * %d = %d" %(a, b, hap))
    elif c == '%':
        hap = a % b
        print("%d % %d = %d" %(a, b, hap))
    else :
        print("알수없는 연산자")

   
        
        
    

    
    
    
    
