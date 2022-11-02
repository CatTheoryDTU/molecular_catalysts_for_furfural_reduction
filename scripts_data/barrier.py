#coupling barriers with graphene
fig, ax = plt.subplots(figsize=(8,8))

Ea=[0.84,1.27,1.32,0.58,0.64,0.48]
Efcho=[-0.93,-1.91,-2.20,-0.52,-0.74,-0.42]
surf=['Cu','Pt','Ru','Pb','Ag','C']

xx = np.linspace(-3,0.5,100)
a, b = np.polyfit([e for e in Efcho],Ea,1)


variance = np.var(Ea)
residuals = np.var([(a*xx + b - yy)  for xx,yy in zip(Efcho,Ea)])
Rsqr = np.round(1-residuals/variance, decimals=2)
print(a, b, Rsqr)


#surface    
ax.plot(xx, a*xx+b, ls ='--', lw=3)
ax.scatter([e for e in Efcho],Ea,s=300,facecolor='black',edgecolor='black',label = 'Y='+str(round(a,2))+'X+'+str(round(b,2))+', R$^2$='+str(round(Rsqr,2)), alpha = 0.5)
    
#pc
mc=['CoPc','CuPc']
colors=['pink','peru']
gfcho=[-0.10,0.04]

for i,g in enumerate(gfcho):
    ax.scatter(g,a*g+b,s=400,marker='^',color=colors[i])
    ax.annotate(mc[i],(g+0.05,a*(g)+b),fontsize=20,color=colors[i])

ax.set_xlim(-2.5,0.1)
ax.set_ylim(0.2,1.5)

#plot setting
ax.set_xlabel('$\Delta$E(FCHO) (eV)',fontsize=16)
ax.set_ylabel('$\Delta$E$_a$ (eV)',fontsize=16)
ax.tick_params(labelsize=16)
ax.legend(loc='upper right',fontsize=16)

