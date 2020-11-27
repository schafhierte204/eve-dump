import json as js
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.json')
with open(filename) as file:
    data=file.read()

filename = os.path.join(dirname, 'outputMineral.json')
with open(filename) as d:
    data2=d.read()

data=data+'{}]'
d=js.loads(data)
d.pop()
data2=str(data2)
data2='['+data2+'{}]'
d2=js.loads(data2)
d2.pop()
d=d.pop()
d2=d2.pop()
print(   "Veldspar=                         "+"{:.3f}".format(float(d2['Veldspar'])-float(d['Tritanium'])*3.12)+" "+                              "="+"{:.3f}".format(d2['Veldspar'])+"\n"    
        +"Dense Veldspar=                   "+"{:.3f}".format(float(d2['DVeldspar'])-float(d['Tritanium'])*3.44)+" "+                             "="+"{:.3f}".format(d2['DVeldspar'])+"\n"  
        +"Concentrated Veldspar=            "+"{:.3f}".format(float(d2['CoVeldspar'])-float(d['Tritanium'])*3.28)+" "+                            "="+"{:.3f}".format(d2['CoVeldspar'])+"\n" 
        +"Comressed Veldspar=               "+"{:.3f}".format(float(d2['CVeldspar'])-float(d['Tritanium'])*312)+" "+                              "="+"{:.3f}".format(d2['CVeldspar'])+"\n"  
        +"Comressed Dense Veldspar=         "+"{:.3f}".format(float(d2['CDVeldspar'])-float(d['Tritanium'])*344)+" "+                             "="+"{:.3f}".format(d2['CDVeldspar'])+"\n" 
        +"Comressed Concentrated Veldspar=  "+"{:.3f}".format(float(d2['CCoVeldspar'])-float(d['Tritanium'])*328)+" "+                            "="+"{:.3f}".format(d2['CCoVeldspar'])+"\n"
        +"Proxeres=                         "+"{:.3f}".format(float(d2['Pyroxeres'])-(float(d['Pyerite'])*0.7+float(d['Mexallon'])*0.23))+" "+    "="+"{:.3f}".format(d2['Pyroxeres'])+"\n"  
        +"Stable Pyroxeres=                 "+"{:.3f}".format(float(d2['SPyroxeres'])-(float(d['Pyerite'])*0.74+float(d['Mexallon'])*0.25))+" "+  "="+"{:.3f}".format(d2['SPyroxeres'])+"\n" 
        +"Viscos Proxeres=                  "+"{:.3f}".format(float(d2['VPyroxeres'])-(float(d['Pyerite'])*0.77+float(d['Mexallon'])*0.25))+" "+  "="+"{:.3f}".format(d2['VPyroxeres'])+"\n" 
        +"Comressed Proxeres=               "+"{:.3f}".format(float(d2['CPyroxeres'])-(float(d['Pyerite'])*70+float(d['Mexallon'])*23))+" "+      "="+"{:.3f}".format(d2['CPyroxeres'])+"\n" 
        +"Comressed Stable Proxeres=        "+"{:.3f}".format(float(d2['CSPyroxeres'])-(float(d['Pyerite'])*74+float(d['Mexallon'])*25))+" "+     "="+"{:.3f}".format(d2['CSPyroxeres'])+"\n" 
        +"Comressed Viscos Proxeres=        "+"{:.3f}".format(float(d2['CVPyroxeres'])-(float(d['Pyerite'])*77+float(d['Mexallon'])*25))+" "+     "="+"{:.3f}".format(d2['CVPyroxeres'])+"\n" 
        +"Scoredite=                        "+"{:.3f}".format(float(d2['Scoredite'])-(float(d['Tritanium'])*1.17+float(d['Pyerite'])*0.7))+" "+   "="+"{:.3f}".format(d2['Scoredite'])+"\n"   
        +"Massive Scoredite=                "+"{:.3f}".format(float(d2['MScoredite'])-(float(d['Tritanium'])*1.23+float(d['Pyerite'])*0.74))+" "+ "="+"{:.3f}".format(d2['MScoredite'])+"\n"  
        +"Concentrated Scoredite=           "+"{:.3f}".format(float(d2['CoScoredite'])-(float(d['Tritanium'])*129+float(d['Pyerite'])*77))+" "+   "="+"{:.3f}".format(d2['CoScoredite'])+"\n" 
        +"Comressed Scoredite=              "+"{:.3f}".format(float(d2['CScoredite'])-(float(d['Tritanium'])*117+float(d['Pyerite'])*70))+" "+   "="+"{:.3f}".format(d2['CScoredite'])+"\n"  
        +"Comressed Massive Scoredite=      "+"{:.3f}".format(float(d2['CMScoredite'])-(float(d['Tritanium'])*123+float(d['Pyerite'])*74))+" "+   "="+"{:.3f}".format(d2['CMScoredite'])+"\n" 
        +"Comressed Concentrated Scoredite= "+"{:.3f}".format(float(d2['CCoScoredite'])-(float(d['Tritanium'])*129+float(d['Pyerite'])*77))+" "+  "="+"{:.3f}".format(d2['CCoScoredite'])+"\n"
            
        
        )


