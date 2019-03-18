# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:57:05 2019

@author: S291366
"""
import numpy as np
import matplotlib.pyplot as plt

Xa=input('Podaj Xa:')
Ya=input('Podaj Ya:')
Xb=input('Podaj Xb:')
Yb=input('Podaj Yb:')
Xp=input('Podaj Xp:')
Yp=input('Podaj Yp:')

Xac=Xa.strip('-').replace('.','0')
XA=Xac.isdigit()
if XA==True:
    Xa=float(Xa) 
else:
    Xa=input('Podaj Xa:')
    Xa=float(Xa) 

Xbc=Xb.strip('-').replace('.','0')
XB=Xbc.isdigit()
if XB==True:
   Xb=float(Xb) 
else:
    Xb=input('Podaj Xb:')
    Xb=float(Xb)

Yac=Ya.strip('-').replace('.','0')
YA=Yac.isdigit()
if YA==True:
   Ya=float(Ya) 
else:
    Ya=input('Podaj Ya:')
    Ya=float(Ya) 

Ybc=Yb.strip('-').replace('.','0')
YB=Ybc.isdigit()
if YB==True:
   Yb=float(Yb) 
else:
    Yb=input('Podaj Yb:')
    Yb=float(Yb) 
    
Xpc=Xp.strip('-').replace('.','0')
XP=Xpc.isdigit()
if XP==True:
   Xp=float(Xp) 
else:
    Xp=input('Podaj Xp:')
    Xp=float(Xp)

Ypc=Yp.strip('-').replace('.','0')
YP=Ypc.isdigit()
if YP==True:
   Yp=float(Yp) 
else:
    Yp=input('Podaj Yp:')
    Yp=float(Yp)

det=Xa*Yb+Xb*Yp+Xp*Ya-Xp*Yb-Xa*Yp-Xb*Ya

if det>0:
    print('Punkt P leży po prawej stronie odcinka AB')
elif det<0:
    print('Punkt P leży po lewej stronie odcinka AB')
elif det==0:
    print('Punkty P,A i B są współliniowe')
    
dXab=Xb-Xa
dYab=Yb-Ya
dXap=Xp-Xa
dYap=Yp-Ya
ilocz=dXab*dYap-dXap*dYab

    
X=[Xa,Xb]
Y=[Ya,Yb]
plt.plot(X,Y)
plt.scatter(Xp,Yp)
plt.show()
