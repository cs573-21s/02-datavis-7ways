import pandas as pd

from matplotlib import pyplot as plt

from matplotlib.legend import Legend

from matplotlib.ticker import (MultipleLocator, 
                               FormatStrFormatter, 
                               AutoMinorLocator) 

plt.style.use('ggplot')

data = pd.read_csv('cars.csv')
cars = data['Car']
makes = data['Manufacturer']
mpg = data['MPG']
weights = data['Weight']
adjust = data['Cylinders']

manus = ['bmw', 'ford', 'honda', 'mercedes', 'toyota']

cs = ['black', 'blue', 'red', 'purple', '#dc9a09']

fig, ax = plt.subplots()

colors = {'bmw':'black', 'ford':'blue', 'honda':'red', 'mercedes':'purple', 'toyota':'#dc9a09'}

ax.scatter(weights, mpg, c=makes.map(colors), s=adjust*25 , alpha=0.4, facecolor='#EDEEF0')

m = [plt.plot([],[], c=cs[i], marker='o', alpha=0.5, ls='', ms=5)[0] for i in range(0,5)]

leg = plt.legend(handles=m, labels=['bmw', 'ford', 'honda', 'mercedes', 'toyota'],
    title='Manufacturer', loc=(1.02,0.5), fancybox=False, facecolor='#EDEEF0',
    fontsize='small', labelspacing=1.0, frameon=False)

ax.add_artist(leg)

w = [plt.plot([],[], c='k', marker='o', alpha=0.4, ms=i, ls='')[0] for i in range(8,11)]

plt.legend(handles=w,labels=['2000','3000','4000'], loc=(1.03,0.22),
   title='Weight', fancybox=False, facecolor='#EDEEF0', fontsize='small', labelspacing=1.0,
   frameon=False)

majorLocatorX = MultipleLocator(1000)
majorFormatter = FormatStrFormatter('%d')
minorLocatorX = MultipleLocator(500)

ax.set_xlabel('Weight', fontfamily='arial',c='black', fontsize='medium')
ax.set_ylabel('MPG', fontfamily='arial',c='black', fontsize='medium')

ax.xaxis.set_major_locator(majorLocatorX)
ax.xaxis.set_major_formatter(majorFormatter)

ax.xaxis.set_minor_locator(minorLocatorX)
ax.xaxis.grid(b=True, which='minor', color='white', linewidth=0.5)
ax.xaxis.grid(b=True, which='major', color='white', linewidth=1.25)

ax.yaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_formatter(majorFormatter)

ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.yaxis.grid(b=True, which='minor', color='white', linewidth=0.5)
ax.yaxis.grid(b=True, which='major', color='white', linewidth=1.25)

ax.tick_params(which='minor', color='white')

ax.tick_params(which='major', pad=2, colors='black', width=1, labelsize='small')
plt.yticks(fontname='arial')
plt.xticks(fontname='arial')
ax.set_facecolor('#EDEEF0')

plt.grid(True)
plt.tight_layout()
plt.savefig('ss_matplotlib.png')

plt.show()
