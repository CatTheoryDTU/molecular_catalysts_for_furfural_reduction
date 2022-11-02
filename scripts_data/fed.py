# importing the required packages
#------------------------------------------
# get_ipython().run_line_magic('matplotlib', 'auto')
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

#------------------------------------------
#   Making the figure object
#------------------------------------------
fig, ax = plt.subplots(figsize=(16,7))

#------------------------------------------
#   Reading data from Excel sheet
#------------------------------------------
xlpath = 'data.xlsx'
df = pd.read_excel(xlpath, 'FED')
df.set_index('surfaces', inplace=True)

#----------------------------------------------------------
#   Energies as dictionary and surfaces + steps as list
#----------------------------------------------------------
steps = list(df.keys())[0:7]
E = df.T.to_dict()
surfaces = list(E.keys())[0:4]

# desorption of FCHOH*     
xx = np.linspace(0,8,100)
yy = 0*xx + 0.86 + u
ax.plot(xx, yy, color = 'grey', ls = '--', lw = 3, alpha = 0.5)

#print(E)

u = -0.5
for s in surfaces:
    e = E[s]
    for i,ss in enumerate(steps):
        if i == 3:
            e[ss]+=u
        if i > 3:
            e[ss]+=2*u
        else:
            e[ss]+=0
        


#------------------------------------------------------
#   Defining colors for each surface as dictionary
#------------------------------------------------------
colors = {'CoPc':'pink','CuPc':'peru', 'graphene':'black','Pb(111)':'gray','Co(0001)':'brown','Cu(111)':'orange'}

#------------------------------------------
#   Plotting the data
#------------------------------------------
for surf in surfaces:
    k = 0
    for st in steps:
        #----------------------------------
        #   Solid lines
        #----------------------------------
        if k == 0:
            plt.plot([k, k+0.5], [E[surf][st], E[surf][st]], label=surf, color=colors[surf],ls='-', lw=3)
        else:
            plt.plot([k, k+0.5], [E[surf][st], E[surf][st]], color=colors[surf],ls='-', lw=3)
        
        #----------------------------------
        #   dotted lines
        #----------------------------------
        if k<len(steps)-1:
            y1 = E[surf][st]
            y2 = E[surf][steps[k+1]]
            plt.plot([k+0.5, k+1], [y1, y2], color=colors[surf], ls='--', lw=1)
        k = k + 1

#------------------------------------------
#   Ticks, labels, legends
#------------------------------------------
ticks = steps
loc = [0.25, 1.25, 2.25, 3.25, 4.25, 5.25, 6.25]

plt.tick_params(axis='x',          # changes apply to the x-axis
                which='both',      # both major and minor ticks are affected
                bottom=True,       # ticks along the bottom edge are off
                top=False,          # ticks along the top edge are off
                labelbottom=True,
                labeltop=False)    # labels along the bottom edge are off



#ax.xaxis.tick_top()
plt.ylim([-1.5, 1.5])
plt.xlim([0, 6.5])
plt.xticks(loc, ticks, fontsize=15, rotation=0.)
plt.yticks(fontsize=18)
#plt.xlabel('Reaction coordinate', fontsize=20)
plt.ylabel('$\Delta$G (eV)', fontsize=20)
#plt.title('HF\n')
plt.tight_layout()
plt.legend(fontsize=20)
