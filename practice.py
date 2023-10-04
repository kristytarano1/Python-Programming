# from math import sqrt


# players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
# total = 0
# values = 0


# def average ():
#     global total
#     global values 
#     for p in players:
#         total += p
#         values += 1

#     mean = total/values
#     return mean

# mean = average()

# def variance (m):
#     sum = 0
#     count = 0
#     global players
#     for p in players:
#         count += 1
#         variant = (p - m)**2
#         sum += variant 
    
#     variance = sum/count
#     stDeviant = float(format(sqrt(variance), '.3f'))
      
#     return stDeviant

# def stanDeviation (s, m):
#     counter = 0
#     for p in players:
#         if p >= m - s  and p <= m + s:
#             counter += 1
#         else:
#             pass

#     return counter

# print(stanDeviation(variance(mean), mean))

# import pandas as pd
# import random as rd

# data = {
#     'name': ['Clayton', 'Jose', 'Kristy', 'Robert'],
#         'day': ['Tuesday', 'Wednesday', 'Thursday', 'Friday'] }


# df = pd.DataFrame(data, index=['Tuesday', 'Wednesday', 'Thursday', 'Friday'])

# for i in df['name']:
#     print((i) + '' )))

# #print(df['name']
#number = list(range(0, 9, 2))
#print(number)

special = '1357 Country Ln.'
s_string = special[ :4]

print(s_string[-1])