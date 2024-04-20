'''
Q2.Write a function that converts hours into seconds.

Examples:
how_many_seconds(2) ➞ 7200
how_many_seconds(10) ➞ 36000
how_many_seconds(24) ➞ 86400

60 seconds in a minute, 60 minutes in an hou
Don't forget to return your answer.

'''

def time(h):
    t=h*3600
    return t
h=int(input("Enter hours:"))
res=time(h)
print(res)