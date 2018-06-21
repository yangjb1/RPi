#!/usr/bin/python

import matplotlib.pyplot as plt
import sys

def plot_F(fname):
    temp = []
    flag_F = False

    x = []
    cunt = -5
    with open(fname) as f:
        for lines in f:
            for words in lines.split():
                if words == 'Fahrenheit:':
                    flag_F = True
                elif flag_F:
                    temp.append(float(words))
                    cunt += 5
                    x.append(cunt)
                    flag_F = False

#for words in temp:
#    print words

#for num in x:
#    print num


    plt.figure()
    plt.plot(x,temp)
    plt.ylabel('Fahrenheit')
    plt.xlabel('Run Time (Min)')
    plt.title(fname)


arg = len(sys.argv)
for i in range(1,arg):
    plot_F(sys.argv[i])

plt.show()
