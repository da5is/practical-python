# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.

height = 100.00
bounce_distance = 3/5
times_bounced = 1

while times_bounced <= 10:
    height = height * bounce_distance
    print (f'{times_bounced} {round(height, 4)}')
    times_bounced += 1
