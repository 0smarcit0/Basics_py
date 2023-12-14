diccionario = {
    "nba": "baloncesto",
    "fifa":"futbol",
    "mlb": "baseball"
    
}
for i in diccionario: #diccionario.value
    
 print(diccionario[i]) 
  #print(diccionario)
  #print(i)

diccionario["fifa"] = "fubo"

print(diccionario)

diccionario["waza"] = "wazawaza"
print(diccionario["waza"])

diccionario.pop("nba")
print(diccionario)

print(diccionario["waza"])