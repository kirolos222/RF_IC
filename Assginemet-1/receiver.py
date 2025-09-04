import math
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
Pinsen=-102
gainsens=72
Nfsens=1.92
ip3sens=-42.64
Pin=[-70,-65,-60,-50,-40,-30,-20,-15]
gain=[50 ,45,40,30,20,10,0,-5]
Nf=[3.93,4.41,6.15 ,6.48,8.87,16.05,25.64,30.61]
iP3=[-20.74,-15.76,-10.75,-1.65,3.77,5.01,5.18,5.18]
Gain =[gain[7-i] for i in range(len(gain))] 
NF=[Nf[7-i] for i in range(len(gain))] 
plt.plot(Gain, NF)
plt.xlabel('GAIN')
plt.ylabel('NF')
plt.title('figure 1')
plt.legend()
plt.show()

IIP3=[iP3[7-i] for i in range(len(Pin))] 
plt.plot(Gain, IIP3)
plt.xlabel('GAIN')
plt.ylabel('IIP3')
plt.title('figure 2')
plt.legend()
plt.show()
print("SNR is level at sensitivity is equal to ",Pinsen+174-70-Nfsens)
SNR = [Pin[i]+174-70-Nf[i] for i in range(len(Pin))]
IM3=[(2*((-iP3[i]+Pin[i]))+(Pin[i]+gain[i])) for i in range(len(Pin))]
SINAD=[10*math.log10(((10**((((Pin[i]+gain[i])/10)-3))))/((10**(((-174 + Nf[i]+gain[i]  + 70)/10)-3))+(10**((((IM3[i])/10)-3))))) for i in range(len(Pin))]
print(SINAD)
print(IM3)
yval=[30]*len(SINAD)
yh=[0,5,10,20,30,40,50,60]
im3forspec=[-1*(IM3[i]-(Pin[i]+gain[i])) for i in range(len(Pin))]
plt.plot(Pin, im3forspec)
plt.plot(Pin, SNR)
plt.plot(Pin, yval,linestyle='--',label='30 db limit')
plt.plot([-70]*len(SINAD),yh,linestyle='--',label='Pin=-70dbm')
plt.plot([-15]*len(SINAD),yh,linestyle='--',label='Pin=-15dbm')
plt.text(30, 1, '30 db', fontsize=12, color='red')
plt.plot(Pin, SINAD)
plt.xlabel('Pin(dbm)')
plt.ylabel('SNR,SINAD,IM3')
plt.title('figure 3')
plt.legend()
plt.show()
plt.plot(Pin, gain)
plt.xlabel('Pin')
plt.ylabel('Gain')
plt.title('figure 4')
plt.legend()
plt.show()