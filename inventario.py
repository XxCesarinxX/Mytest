import pandas as pd

df=pd.read_csv("lista_de_precios.csv")
df2=pd.read_csv("inventa.csv")
vent=pd.read_csv("ventas.csv")
"""
def agregar_ainventario():
    agregar=input("agrega; en este orden\n->'Modelo'<-\t->'Color'<-\t'Tallas(separadas por espacios)'\n")
    lista =agregar.split()
    modelo=lista[0]
    color=lista[1]
    lista.remove(modelo)
    lista.remove(color)
    lista_key=[]
    lista_value=[]
    for i in lista:
        if i.isdigit():
            lista_value.append(i)
        else:
            lista_key.append(i)
    print(lista_key, lista_value)
    global diccionario_resultado
    diccionario_resultado=dict(zip(lista_key,lista_value))
    diccionario_resultado['modelo']=modelo
    diccionario_resultado['color']=color
    print(diccionario_resultado)

def busquedas():
    global ubicaciones 
    ubicaciones = []
    search = input("introduzca el modelo a buscar\n-->")
    if search.islower():
        search=search.upper()
    for i in range(len(df["Modelo"])):
        if search==df.loc[i,'Modelo']:
            print(df.iloc[i],"\n")
            ubicaciones.append(i)
#            df.loc[i, "Tallas"] = "XL"cambiar valor de ese bloque

def venta ():
    venta = input("Venta\n 'modelo'   >'talla'<   >'color'<   >'coste'<   >'nombre de cliente'<\n")
    lista = venta.split()
    print(lista)

def cambio():
    auxi=0
    for i in range(len(df["Precio"])):
        auxi = df.loc[i, "Precio"]
        fin = auxi+600
        if fin == 1350:
            fin=1400
        if fin==1450:
            fin=1500
        if fin ==1550:
            fin = 1700
        
    "?    df.loc[i, "Precio"]= fin

    print(df["Precio"])
    df.to_csv("Precios.csv")
"""
class venta:
    def __init__(self, modelo, color, talla, precio):
        self.model=modelo
        self.colo=color
        self.talla=talla
        self.total=precio
        self.canti=1

    def decrementacion(self):
        for i in range(len(df2["Modelo"])):
            if self.model == df2.loc[i,"Modelo"]:
                df2.loc[i, self.talla]-=1
        print(df2)
    def ganancia(self):
        for i in range(len(df["Modelo"])):
            if self.model == df.loc[i,"Modelo"]:
                global costo, ganar
                costo = df.loc[i, "Precio"]
                ganar =  self.total - costo
                #cosoto=self.total-costo
        print("usted tiene una ganancia de: --> ",ganar)
    def adjuntar(self):
        ven=vent.append({'Cantidad':self.canti,'Modelo':self.model, 'Color':self.colo,'Talla':self.talla, 'Ganancia':ganar,'Total':self.total, 'Precio':costo}, ignore_index=True)
        print(ven)
        ven.to_csv("ventas.csv", index=False)
    def reponer(self):
        for i in range(len(vent["Modelo"])):
            if self.model == vent.loc[i,"Modelo"]:
                print('mismo modelo')
                if self.colo == vent.loc[i,"Color"]:
                    print('mismo color')
                    if self.talla == vent.loc[i,"Talla"]:
                        print('mismo talla')
                        vent.loc[i,"Cantidad"]+=1
            
        print(vent)
            

dia = venta("Canelo", "NEGRO", "XL", 1500)
dia.reponer()