def ScoreRanck(score):
    if score >= 90:
        print("성적: A")
    elif score < 90 and score >= 80:
        print("성적: B")
    elif score < 80 and score >=70:
        print("성적: C")
    elif score < 70 and score >60:
        print("성적: D")
    else :
        print("성적: E")

def max_min_score(math,English,lgg):
    max = 0
    min = 0
    tmep = 0
    midle = 0
    if math > English :
        max = math
        min = English
    else  :
        max = English
        min = math
        
    if max > lgg :
        midle = lgg
    else :
        temp = max
        max = lgg
        midle = temp
        
    if midle < min:
        temp = midle
        middle = min
        min = temp
        print("최고", max)
        print("최저", min)
    else :
        print("최고", max)
        print("최저", min)
        
        
        
        
    




        
