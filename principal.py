import persistencia as sd
import json

data = {
    "carros":[
        {
            "marca": "renault",
            "modelo": 2010
        }, 
        {
            "marca": "mazda",
            "modelo": 2010
        }
    ]
}
carroB ={
    "marca":"Toyota",
    "modelo" : 2019
}

with open("data/midatalst.json", "w") as write_file:
    json.dump(data, write_file,indent= 4)

sd.crearInfo("midatad.json",data)

sd.addInfo(carroB,"midatad")

print(sd.leerArchivo("midatad.json"))