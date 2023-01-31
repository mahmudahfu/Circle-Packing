from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

#input
d = 2
width = 77
height = 33


#fig = plt.figure(figsize=(width,height))
#ax = fig.add_subplot(111)

#radius
r = float(d/2)

kode = float(1.0) #kode for line x

#line
line = int (width/d) 

#column
rumus_1 = ((d*d) - (r*r))
rumus_2 = (math.sqrt(rumus_1))
rumus_3 = height - d
rumus_4 = ((rumus_3+rumus_2)/rumus_2)
column = int(rumus_4)
print(column)

x_ood = int (width/d)
x_even = int ((width-r)/d) 
print(x_ood)
print(x_even)

a = np.empty((0), float) # array for many line x
b = np.empty((0), float) # array for many column y
x = np.empty((0), float) # array x
y = np.empty((0), float) # array y
w = np.empty((0), float) # array for number

#array for many line x
for i in range(1, (column+1)):
    a = np.append(a, [i])
    #print(a)
#array x
for j in a:
    if (j % 2) == 0:
        for k in np.arange(d, (width-(r-kode)), d):
            x = np.append(x, [k])
            #print(x)
    else:
        for l in np.arange(r, (width-(r-kode)), d):
            x = np.append(x, [l])
            #print(x)
x1 = len(x)
print(x1)
#print(x)

# array for many column y
for n in range(1, (column+1)):
    b = np.append(b, [n])
    #print(b)

#array y
for m in b:
    if m > 1:
        if (m % 2) == 0:
            f = ((m-1)*math.sqrt(rumus_1))+r
            y = np.append(y, ([f]*x_even))
            #print(y)
        else:
            g = ((m-1)*math.sqrt(rumus_1))+r
            y = np.append(y, ([g]*x_ood))
            #print(y)

    else:
        y = np.append(y, ([r]*x_ood))
        #print(y)
y1 = len(y)
print(y1) 

# combine 2 array for draw circle
combined = np.transpose((x, y))
#print(combined)

#array for number
for v in range(1, (y1+1)):
    w = np.append(w, [v])
    #print(w)

#print output
("""
---------------------------------------
| Number   |      X      |     Y      |
----------------------------------------""")

#combine number,x,y
combined2 = np.transpose((w,x,y))
#print(combined2)

#save excel
df = pd.DataFrame(combined2)
df.columns = ['Number', 'X', 'Y']

writer2 = pd.ExcelWriter('result.xlsx')

df.to_excel(writer2, sheet_name = 'result', index = False)

writer2.save()

#draw circle
for titik1, titik2 in combined:
    circle = plt.Circle((titik1,titik2), r) 
    fig = plt.gcf()
    ax= fig.gca()
    ax.add_patch(circle)  
    fig.set_figheight(height)
    fig.set_figwidth(width)
    #ax.add_artist(circle)   

#show circle
ax.set_xlim(0,width)
ax.set_ylim(0, height)
#print(circle)
fig.savefig('plotcircles.png')
    
    