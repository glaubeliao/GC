import serial
import time
import numpy as np
import matplotlib.pyplot as plt

ser= serial.Serial("COM3")


i=0
time=[]
data=[]

    

for i in range(20):
    i=i+1
    a=ser.readline()
    b=int(a)
    data.append(b)
    time.append(i)
    #print(i)
    print(b)
    
    if i == 5:
        ser.write(b'F')
    elif i == 15:
        ser.write(b'Q')
    
    
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(time,data )

# Labeland Title
plt.xlabel("T (sec)", fontsize=10)
plt.xticks(fontsize=10)
plt.ylabel("Count", fontsize=10)
plt.yticks(fontsize=10)
#plt.title("Exp 10/20", fontsize=16)
plt.show()
