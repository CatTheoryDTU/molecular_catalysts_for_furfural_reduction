import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(figsize=(8,8))

xlpath = 'data.xlsx'
#location of data
df = pd.read_excel(xlpath, 'scaling')

surfaces = np.array(df['surfaces'][0:9])
pc = np.array(df['surfaces'][9:12])

colors = ['lightcoral','dodgerblue','orange','green']
products = ['H$_2$','FAL','2-MF','Hydrofuroin']

for i in range(4):
    ax.scatter(range(100,104)[i],range(100,104)[i],s=200,label=products[i],color=colors[i])

for i in range(len(surfaces)):
    if i in [0,4]:
        ax.plot(df['Eads_fur'][i], df['Eads_H'][i], marker = 'o', fillstyle='left',markersize=20, color=colors[2],markerfacecoloralt=colors[1],markeredgewidth=0)
        ax.annotate(df['surfaces'][i], (df['Eads_fur'][i]+0.05, df['Eads_H'][i]-0.07), fontsize=16, color='black')
    elif i in [7,8]:
        ax.plot(df['Eads_fur'][i], df['Eads_H'][i], marker = 'o', markersize=20, color='lightcoral')
        ax.annotate(df['surfaces'][i], (df['Eads_fur'][i]+0.05, df['Eads_H'][i]-0.07), fontsize=16, color='black')
    elif i == 1:
        ax.plot(df['Eads_fur'][i], df['Eads_H'][i], marker = 'o', fillstyle='left',markersize=20, color=colors[3],markerfacecoloralt=colors[1],markeredgewidth=0)
        ax.annotate(df['surfaces'][i], (df['Eads_fur'][i]+0.05, df['Eads_H'][i]-0.07), fontsize=16, color='black')
    else:
        ax.plot(df['Eads_fur'][i], df['Eads_H'][i], marker = 'o', markersize=20, color='dodgerblue')
        ax.annotate(df['surfaces'][i], (df['Eads_fur'][i]+0.05, df['Eads_H'][i]-0.07), fontsize=16, color='black')
    
        
for i in range(len(pc)):
    i += 9
    if i == 2+9:
        ax.plot(df['Eads_fur'][i], df['Eads_H'][i], marker = 'o', fillstyle='left',markersize=20, color=colors[3],markerfacecoloralt=colors[1],markeredgewidth=0)
        ax.annotate(df['surfaces'][i], (df['Eads_fur'][i]+0.05, df['Eads_H'][i]-0.07), color='black', fontsize=16)
    else:
        ax.plot(df['Eads_fur'][i], df['Eads_H'][i], marker = 'o', fillstyle='left',markersize=20, color=colors[3],markerfacecoloralt=colors[1],markeredgewidth=0)
        ax.annotate(df['surfaces'][i], (df['Eads_fur'][i]+0.05, df['Eads_H'][i]-0.07), color='grey', fontsize=16)

x = np.linspace(-3,3,1000)
des_H = 0*x
des_FCHO = 0*x
err_H = 0.05
err_FCHO = 0.11


ax.plot(x,des_H,color='gray',ls='--')
ax.plot(des_FCHO,x,color='gray',ls='--')

#plot setting
ax.set_ylabel('$\Delta$G(H) (eV)',fontsize=16)
ax.set_xlabel('$\Delta$G(FCHO) (eV)',fontsize=16)
ax.tick_params(labelsize=16)
ax.legend(loc='upper left',fontsize=16,ncol=4)
ax.set_ylim(-0.5,1.2)
ax.set_xlim(-2,0.5)
