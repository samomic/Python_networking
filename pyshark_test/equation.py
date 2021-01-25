import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(z,t):
    p1= -(0.98+0.02)*z[0]+1*z[9]
    p2= -1*z[1]+0.98*z[0]+1*z[2]+0.5*z[5]
    p3=-1*z[2]+0.1*z[1]
    p4=-1*z[3]+0.85*z[1]
    p5=-1*z[4]+0.6*z[3]
    p6=-1*z[5]+0.3*z[3]+1*z[4]
    p7=-1*z[6]+0.5*z[5]+1*z[7]
    p8=-1*z[7]+0.3*z[6]
    p9=-1*z[8]+0.1*z[3]+0.7*z[6]
    p10=-1*z[9]+0.02*z[0]+0.05*z[1]+1*z[8]
    dzdt = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
    return dzdt
# initial condition
z0 = [56,0,0,0,0,0,0,0,0,0]
# time points
t = np.linspace(0,15)
# solve ODE
z = odeint(model,z0,t)
# plot results
plt.plot(t,z[:,0],'b-',label='p1')
plt.plot(t,z[:,1],'g-',label='p2')
plt.plot(t,z[:,2],'r-',label='p3')
plt.plot(t,z[:,3],'c-',label='p4')
plt.plot(t,z[:,4],'m-',label='p5')
plt.plot(t,z[:,5],'y-',label='p6')
plt.plot(t,z[:,6],'k-',label='p7')
plt.plot(t,z[:,7],'#C74FB4',label='p8')
plt.plot(t,z[:,8],'#D9FE35',label='p9')
plt.plot(t,z[:,9],'#0f83c3',label='p10')
plt.ylabel('Вероятность')
plt.xlabel('Время')
plt.title('Бегович')
plt.legend(loc='best')
plt.show()
