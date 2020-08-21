# bounce.py
#
# Exercise 1.5
height = 100 #meters
bounce_back_ratio = 3 / 5
bounce_times = 0
bounce = 0
bounce_max = 10

while bounce_times < bounce_max:
    height = height * bounce_back_ratio
    bounce_times = bounce_times + 1
    print(bounce_times, round(height, 4))
