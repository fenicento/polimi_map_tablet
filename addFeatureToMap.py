import json,csv,re

countries=[
"UNITED STATES OF AMERICA",
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

with open("new-countries.json") as infile:
    inf=json.load(infile)
    
for i in inf['features']:
    
    i['properties']['sel']=0
    
        

with open("new-countries2.json","w") as outfile:
    json.dump(inf,outfile)
    

