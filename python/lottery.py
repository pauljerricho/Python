import random

for i in range(0,9):
    li = [2,3,5,6,7,10,11,12,14,15,17,18,19,20,22,25,28,29,30,33,35,39,40,41,43]
    # 리스트에서 3개 랜덤 추출
    sampleList = random.sample(li, 3)
    # print(sampleList)

    li_2 = [17,30,40,43,3,7,33,35,20,28,41,2,22,19]
    sampleList_2 = random.sample(li_2, 3)

    li_t = sampleList+sampleList_2
    li_t = sorted(li_t)
    print(f"{li_t}")
exit()