"""
def menu():
        menu = [" "," ============================================================","||----------------------------------------------------------||",
        "||                           MENÚ                           ||",
        "||----------------------------------------------------------||",
        "||    1). Verificacion De Aprobado                          ||",
        "||    2). Ingreso De Notas Y Calculo Del Promedio           ||",
        "||    3). Contar Calificaciones Mayores                     ||",
        "||    4). Verificar y Contar Calificaciones Epecificas      ||",
        "||    5). Menu                                              ||",
        "||    6). Salir Del Programa                                ||",
        "||----------------------------------------------------------||",
        " ============================================================"]
        for hola in menu:
            print(hola)
    
menu()

Respuesta =input("")
"""

def solicitud_de_dato():    
    while True:
        try:
            nombre_de_producto = str(input("Introduce El nombre Del Producto: "))
            precio_del_producto = float(input("Introduce El precio Del Producto: "))
            cantidad_de_productos = int(input("La Cantidad De Producto Que Tienes: "))
        except:
            print("""
UPS! ERROR. Al Perecer Ingresaste Un Valor Erroneo: 
...
...
Por Favor Vuelve a Digitarlos:
...
            
            """)
            
            continue
        
        break
    
    i = 0
    preguntar_al_usuario = input("Cantos Productos Va a Ingrezar")
    for i in preguntar_al_usuario:
        solicitud_de_datos()
        i+= 1
        
        
        
solicitud_de_dato()        

    i = 0
    preguntar_al_usuario = input("Cantos Productos Va a Ingrezar")
    for i in preguntar_al_usuario:
        solicitud_de_datos()
        i+= 1   
    
        