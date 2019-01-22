
import sys
from math import sin, cos, radians

print("Sup bro! Check out this spiral ")

#for i in range(360):
#    print(cos(radians(i)))

def make_dot_string(x):
    rad = radians(x)
    numspace = int(20 * cos(radians(x)) + 20)
    st = ' ' * numspace + 'o'
    return st


def main():
    for i in range(0,1800,12):
        s = make_dot_string(i)
        print(s)

main()