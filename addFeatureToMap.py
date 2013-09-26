import json,csv,re

countries=[
"UNITED STATES",
"UNITED KINGDOM",
"NORWAY",
"FINLAND",
"CHINA",
"POLAND",
"SWITZERLAND",
"LITHUANIA",
"SPAIN",
"PORTUGAL",
"COLOMBIA",
"CANADA",
"SINGAPORE",
"FRANCE",
"CHILE",
"INDIA",
"AUSTRIA",
"NETHERLANDS",
"NICARAGUA",
"TURKEY",
"IRELAND",
"SOUTH AFRICA",
"MEXICO",
"CZECH REPUBLIC",
"MALTA",
"SLOVENIA",
"ISRAEL",
"ARGENTINA",
"HUNGARY",
"LATVIA",
"ECUADOR",
"JAPAN",
"GERMANY",
"AUSTRALIA",
"LEBANON",
"ESTONIA",
"DENMARK",
"SWEDEN",
"BRAZIL",
"CYPRUS",
"RUSSIA",
"GREECE",
"BELGIUM",
"SOUTH KOREA"
]

l=[]

with open("countries-detailed.geo.json") as infile:
    inf=json.load(infile)
    
for i in inf['features']:
    n=i['properties']['NAME'].upper()
    i['properties']['sel']=0
    
    del i['properties']['LON']
    del i['properties']['LAT']
    del i['properties']['REGION']
    del i['properties']['SUBREGION']
    del i['properties']['AREA']
    del i['properties']['UN']
    del i['properties']['POP2005']
    del i['properties']['FIPS']
    del i['properties']['ISO2']
    del i['properties']['ISO3']
    
    if(n in countries):
        l.append(n)
        i['properties']['opacity']=1
    else:
        i['properties']['opacity']=0.4
        
print len(l)
print len(countries)
print list(set(countries) - set(l))

with open("new-countries2.json","w") as outfile:
    json.dump(inf,outfile)
    

