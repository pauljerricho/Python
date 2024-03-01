import numpy as np

sample = np.random.choice(['2','6','8','12','16','17','20','24','25','26','27','32','34','35','40','41','42'],
                          6 , 
                          replace = False)
# print(sample)

list = [24, 8, 41 ,42, 34, 35]
list2 = [12, 20, 40, 32, 2, 26]
list3 = [34, 27, 8, 26, 35, 12]
list.sort(reverse=False)
list2.sort(reverse=False)
list3.sort(reverse=False)
print(list2)
print(list3)