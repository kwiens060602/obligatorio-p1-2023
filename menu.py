import datetime
from entities.empleado import Empleado
from entities.auto import Auto
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.director_equipo import DirectorDeEquipo
lista_empleados = []
lista_autos = []
lista_equipos = []

def chequeo_cedula(cedula):
    if len(cedula) == 8 and cedula.isnumeric():
        return True
    else:
        return False

def chequeo_fecha_de_nacimiento(fecha_de_nacimiento_empleado):
    formato = '%d-%m-%Y'
    try:
        datetime.datetime.strptime(fecha_de_nacimiento_empleado, formato)
        return True
    except:
        print ("Uno o más datos ingresados son inválidos, intente nuevamente") 
        return False 


def alta_empleado(lista_empleados):
    cedula_empleado = input ("Ingrese cedula: ")
    if not chequeo_cedula(cedula_empleado):
        raise Exception("Error, la cedula debe tener solo numeros y deben ser 8")
    nombre_empleado = input ("Ingrese nombre: ")
    if not isinstance(nombre_empleado,str):
        raise Exception("El nombre es incorrecto")
    fecha_de_nacimiento_empleado = input("Ingrese fecha de nacimiento (DD-MM-AAAA): ")
    if not chequeo_fecha_de_nacimiento(fecha_de_nacimiento_empleado):
        raise Exception("La fecha es incorrecta")     
    pais_de_nacimiento_empleado = input("Ingrese país del nacimiento: ")       
    if not pais_de_nacimiento_empleado.isalpha():
        raise Exception("El país es incorrecto")
    salario_empleado = int(input("Ingrese salario del empleado: "))
    if not isinstance(salario_empleado,int):
        raise Exception("El salario es incorrecto")
    tipo_empleado = int(input("Ingrese que tipo de empleado es: "))
    if not tipo_empleado == 1 or tipo_empleado == 2 or tipo_empleado == 3 or tipo_empleado == 4:
        raise Exception("El tipo de empleado no existe")
    if tipo_empleado == 1:
        score_piloto = int(input("Ingrese el score del piloto: "))
        if not score_piloto >= 1 and score_piloto <= 99:
            raise Exception("El score esta fuera del rango")
        nro_auto = int(input("Ingrese el numero del auto: "))
        if not nro_auto >= 1 and nro_auto <=99:
            raise Exception("El numero del auto esta fuera del rango")
        puntaje = int(input("Ingrese el puntaje del piloto: "))
        lesion = bool(input("Ingrese si el piloto presenta alguna lesión: "))
        if lesion == True:
            print("El piloto no presenta ninguna lesión")
        else: 
            print("El piloto está lesionado")
            if lesion is not bool:
                raise Exception("El dato lesión es incorrecto")
    tipo_empleado = Piloto(nombre_empleado,cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, score_piloto, nro_auto, puntaje, lesion)
    lista_empleados.append(tipo_empleado)
    print("El piloto fue creado")
    if tipo_empleado == 3:
        score_mecanico = int(input("Ingrese el score del mecanico"))
        if not score_mecanico >= 1 and score_mecanico <= 99:
            raise Exception("El score no entra en el rango")
    tipo_empleado = Mecanico (nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, tipo_empleado, score_mecanico)
    lista_empleados.append(tipo_empleado)
    print("El mecanico fue creado")
    if tipo_empleado == 4:
        tipo_empleado = DirectorDeEquipo(nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado)
        print("El director de equipo fue creado")
        

       
  
               

    
def existe_empleado(cedula):
    for j in lista_empleados:
        if j.cedula == cedula:
            return True
    return False

def obtener_empleados(cedula):
    for j in lista_empleados:
        if j.cedula == cedula:
            return j
    return None


    
    
def alta_auto(lista_autos):
    modelo_de_auto = input("Ingrese el modelo del auto: ")
    if isinstance(modelo_de_auto,str):
        anio_de_auto = int(input("Ingrese año del auto: "))
        if isinstance(anio_de_auto,int):
            score_del_auto = int(input ("Ingrese score del auto: "))
            if score_del_auto >= 1 and score_del_auto <= 99:
                auto = Auto(modelo_de_auto, anio_de_auto, score_del_auto)
                lista_autos.append(auto)
                print("Auto Creado")
            else:
                print("El score es incorrecto, debe ser un numero entre 1 y 99")
        else:
            print("El año del auto es incorrecto")
    else:
        print("El modelo del auto es incorrecto")
        
def alta_equipo ():
    nombre_equipo = input("Ingrese nombre del equipo: ")
    empleados_equipo = []
    veces = 0
    pilotos = 0
    mecanicos = 0
    director = 0
    while veces > 11:
        cedula_empleado = input("Ingrese cedula del piloto: ")
        if existe_empleado(cedula_empleado):
            empleado = obtener_empleados(cedula_empleado)
            if empleado.tipo == "piloto" and pilotos < 3:
                empleados_equipo.append (empleado)
                pilotos += 1
                veces += 1
            elif empleado.tipo == "mecanico" and mecanicos < 8:
                empleados_equipo.append (empleado)
                mecanicos += 1
                veces +=1
            elif empleado.tipo == "director de equipo" and director < 1:
                empleados_equipo.append (empleado)
                director +=1
            else: 
                break 
    
        









menu = True 
while menu: 
    print ("Seleccione la opción del menú: ")
    print ("1. Alta de Empleado")
    print ("2. Alta de Auto")
    print ("3. Alta de Equipo")
    print ("3. Simular Carrera")
    print ("5. Realizar Consultas")
    print ("6. Finalizar Programa")
    opcion = int(input())
    if opcion == 1:
        alta_empleado(lista_empleados)
    elif opcion == 2:
        alta_auto(lista_autos)
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        menu = False
        print("Programa Finalizado")
    elif opcion != 1 or 2 or 3 or 4 or 5 or 6:
        print("Error, eliga una opcion que exista")