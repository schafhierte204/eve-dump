import json as js
import matplotlib.pyplot as plt
with open('output.json') as file:
    data=file.read()

def getvalues(str,d):
    t=[]
    for i in d:
        t.append(i[str])
    dc=enumerate(t)
    dx=[x[0] for x in dc]
    dc=enumerate(t)
    dy=[x[1] for x in dc]
    return dx,dy
    
data=data+'{}]'
d=js.loads(data)
d.pop()
tx,ty=getvalues('Tritanium',d)
px,py=getvalues('Pyerite',d)
mx,my=getvalues('Mexallon',d)
ix,iy=getvalues('Isogen',d)
nx,ny=getvalues('Noxium',d)
zx,zy=getvalues('Zydrine',d)
ex,ey=getvalues('Megacyte',d)
ox,oy=getvalues('Morphite',d)

plt.plot(tx,ty,'o-b',px,py,'o-r',mx,my,'o-g',ix,iy,'+-b',nx,ny,'+-r',zx,zy,'+-g',ex,ey,'1-b',ox,oy,'1-r')
plt.ylabel('price')
plt.xlabel('time')
plt.show()

