import score_modul
math = int(input("수학 성적을 입력 하십시오:"))
English = int(input("영어 성적을 입력 하십시오:"))
lgg = int(input("국어 성적을 입력 하십시오:"))
score_modul.ScoreRanck(math)
score_modul.ScoreRanck(English)
score_modul.ScoreRanck(lgg)
score_modul.max_min_score(math,English,lgg)

