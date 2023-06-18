# descripciones de productos

#  precio

# encontraar precio y mostrar por pantalla


des1= "Este bolso de cuero de la marca: Hugo tiene un precio de 199.98€. es una oferta esencial"
des2 = "Las botas de la marca: nike valen 89€. nunca han estado tan rebajadas"
des3 = "¡Tenemos el bambu en oferta! ahora por 1.2€ el kg no la dejes pasar" 

conversion = 1.21

def findPrice(text):
    textList = text.split()
    for word in textList:
        position = word.find("€")
        if position != -1:
            indexWord = textList.index(word)
            euroPrice = float(word.split("€")[0])
            print(f"Price in euro: {euroPrice}")
            dollarPrice = euroPrice * conversion
            textList[indexWord] = str(dollarPrice) + "$"
            nuevaDes = " ".join(textList)
            break
    return dollarPrice, nuevaDes

precio , descripcion = findPrice(des3)

print(f"Precio in dollar; {precio}")
print(f"Descripcion: {descripcion}")