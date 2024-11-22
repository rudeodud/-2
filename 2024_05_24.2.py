import random

def rolling_dice(pip):
    n = random.randint(1,pip)
    print(pip, "면 주사위 골린 결과: ", n)

rolling_dice(4)
rolling_dice(6)
rolling_dice(6)
rolling_dice(8)
rolling_dice(10)
rolling_dice(12)
rolling_dice(20)
