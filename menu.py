import datetime
from entities.empleado import Empleado
from entities.auto import Auto
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.director_equipo import DirectorDeEquipo
from entities.equipo import Equipo
from exceptions.informacion_invalida import InformacionInvalida

lista_empleados = []
lista_autos = []
lista_equipos = []

def chequeo_cedula(cedula):
    if len(cedula) == 8 and cedula.isnumeric():
        return True
    else:
        return False

def chequeo_ced(cedula):
    for i in lista_empleados:
        if i.cedula_empleado == cedula:
            raise InformacionInvalida("El empleado ya fue creado con esa cedula")

def chequeo_cedEquipo(cedula, lista):
    for i in lista:
        if i.cedula_empleado == cedula:
            return True

def chequeo_autoEquipo(modelo, lista):
    for i in lista:
        if i.modelo_auto == modelo:
            return True

def chequeo_cedula_equipo(cedula):
    for i in lista_empleados:
        if i.cedula != cedula:
            raise InformacionInvalida("El empleado no existe")

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
        raise InformacionInvalida("Error, la cedula debe tener solo numeros y deben ser 8")
    chequeo_ced(cedula_empleado)
    nombre_empleado = input ("Ingrese nombre: ")
    if not isinstance(nombre_empleado,str):
        raise InformacionInvalida("El nombre es incorrecto")
    fecha_de_nacimiento_empleado = input("Ingrese fecha de nacimiento (DD-MM-AAAA): ")
    if not chequeo_fecha_de_nacimiento(fecha_de_nacimiento_empleado):
        raise InformacionInvalida("La fecha es incorrecta")     
    pais_de_nacimiento_empleado = input("Ingrese país del nacimiento: ")       
    if not pais_de_nacimiento_empleado.isalpha():
        raise InformacionInvalida("El país es incorrecto")
    salario_empleado = int(input("Ingrese salario del empleado: "))
    if not isinstance(salario_empleado,int):
        raise InformacionInvalida("El salario es incorrecto")
    tipo_empleado = int(input("Ingrese que tipo de empleado es: "))
    if not (tipo_empleado == 1 or tipo_empleado == 2 or tipo_empleado == 3 or tipo_empleado == 4):
        raise InformacionInvalida("El tipo de empleado no existe")
    if tipo_empleado == 1:
        score_piloto = int(input("Ingrese el score del piloto: "))
        if not score_piloto >= 1 and score_piloto <= 99:
            raise InformacionInvalida("El score esta fuera del rango")
        nro_auto = int(input("Ingrese el numero del auto: "))
        if not (nro_auto >= 1 and nro_auto <=99):
            raise InformacionInvalida("El numero del auto esta fuera del rango")
        tipo_empleado = Piloto(nombre_empleado,cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, score_piloto, nro_auto, lesion=False, suplente= True)
        lista_empleados.append(tipo_empleado)
        print("El piloto fue creado")
    elif tipo_empleado == 2:
        score_piloto = int(input("Ingrese el score del piloto: "))
        if not score_piloto >= 1 and score_piloto <= 99:
            raise InformacionInvalida("El score esta fuera del rango")
        nro_auto = int(input("Ingrese el numero del auto: "))
        if not nro_auto >= 1 and nro_auto <=99:
            raise InformacionInvalida("El numero del auto esta fuera del rango")
        tipo_empleado = Piloto(nombre_empleado,cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, score_piloto, nro_auto, lesion=False, suplente= True)
        lista_empleados.append(tipo_empleado)
        print("El piloto fue creado")
    elif tipo_empleado == 3:
        score_mecanico = int(input("Ingrese el score del mecanico: "))
        if not score_mecanico >= 1 and score_mecanico <= 99:
           raise InformacionInvalida("El score no entra en el rango")
        tipo_empleado = Mecanico (nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, score_mecanico)
        lista_empleados.append(tipo_empleado)
        print("El mecanico fue creado")
    if tipo_empleado == 4:
        tipo_empleado = DirectorDeEquipo(nombre_empleado, cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado)
        lista_empleados.append(tipo_empleado)
        print("El director de equipo fue creado")


def existe_empleado(cedula):
    for j in lista_empleados:
        if j.cedula_empleado == cedula:
            return True  
    return False

def obtener_empleados(cedula):
    for j in lista_empleados:
        if j.cedula_empleado == cedula:
            return j
    return None

def existe_auto(modelo):
    for k in lista_autos:
        if k.modelo_de_auto == modelo:
            return True
    return False

def obtener_autos(modelo):
    for k in lista_autos:
        if k.modelo_de_auto == modelo:
            return True
    return False    
    
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

def validar_equipo (lista_empleados, tipo_empleado) :
        piloto = 0
        mecanico = 0
        director = 0
        for piloto in lista_empleados:
            if tipo_empleado == 1 or tipo_empleado == 2:
                piloto = piloto + 1 
            elif tipo_empleado == 3:
                mecanico = mecanico + 1
            elif tipo_empleado == 4:
                director = director + 1
            
        if piloto != 3 or mecanico < 8 or director != 1:
            print ("Uno o más datos ingresados son inválidos, intente nuevamente")        





def alta_equipo (lista_equipos):
    #hacer las validaciones
    nombre_equipo = input("Ingrese nombre del equipo: ")
    pais_equipo = input("Ingrese el pais del equipo: ")
    anio_equipo = input("Ingrese el año del equipo: ")
    #
    empleados_equipo = []
    veces = 0
    pilotos = 0
    mecanicos = 0
    director = 0
   
    while pilotos < 3:
        cedula = input("Ingrese cedula del piloto: ")      
        if existe_empleado(cedula):
            empleado = obtener_empleados(cedula)
            if isinstance(empleado, Piloto):
                if chequeo_cedEquipo(cedula, empleados_equipo):
                    print("Ese piloto ya fue registrado")
                else:
                    empleados_equipo.append(empleado)
                    pilotos = pilotos + 1
            else:
                print("Ese empleado no es un piloto")
        else:
            print("Ese empleado no existe")
   
   
    while mecanicos < 8:
        cedula = input("Ingrese cedula del mecanico: ")
        if existe_empleado(cedula):
            empleado = obtener_empleados(cedula)
            if isinstance(empleado, Mecanico):
                if chequeo_cedEquipo(cedula, empleados_equipo):
                    print("Ese mecanico ya fue registrado")
                else:
                    empleados_equipo.append(empleado)
                    mecanicos = mecanicos + 1
            else:
                print("Ese empleado no es un mecanico")
        else:
            print("Ese empleado no existe")
   
   
    while director < 1:
        cedula = input("Ingrese la cedula director de equipo: ")
        if existe_empleado(cedula):
            empleado = obtener_empleados(cedula)
            if isinstance(empleado, DirectorDeEquipo):
                if chequeo_cedEquipo(cedula, empleados_equipo):
                    print("Ese director de equipo ya fue registrado")
                else:
                    empleados_equipo.append(empleado)
                    director = director + 1
            else:
                print("Ese empleado no es un director de equipo")
        else:
            print("Ese empleado no existe")
   
    while veces < 1:
        modelo = input("Ingrese el modelo del auto del equipo")
        if existe_auto(modelo):
            auto = obtener_autos(modelo)
            if isinstance(auto,Auto):
                print("Este auto ya fue registrado")
                veces = veces + 1
            else:
                print("El auto no existe")
                

    equipo = Equipo(nombre_equipo, pais_equipo, anio_equipo, auto)

    for i in empleados_equipo:
        equipo.agregar_empleado(empleados_equipo[i])

    lista_equipos.append(equipo)
            
    print("El equipo fue creado con exito")

def simular_carre








menu = True 
while menu:
    print ("Menú Principal")
    print ("Seleccione la opción del menú: ")
    print ("1. Alta de Empleado")
    print ("2. Alta de Auto")
    print ("3. Alta de Equipo")
    print ("4. Simular Carrera")
    print ("5. Realizar Consultas")
    print ("6. Finalizar Programa")
    opcion = int(input())
    if opcion == 1:
        alta_empleado(lista_empleados)
    elif opcion == 2:
        alta_auto(lista_autos)
    elif opcion == 3:
        alta_equipo(lista_equipos)
    elif opcion == 4:
        pass
    elif opcion == 5:
        menu = False
    elif opcion == 6:
        menu = False
        print("Programa Finalizado")
    elif opcion != 1 or 2 or 3 or 4 or 5 or 6:
        print("Error, eliga una opcion que exista")











"""while veces < 12:
        print(veces)
        print(pilotos)
        cedula = input("Ingrese cedula del empleado: ")
        if chequeo_cedula(cedula):
            chequeo_cedula_equipo(cedula)
            if existe_empleado(cedula):
                empleado = obtener_empleados(cedula)
                if chequeo_cedEquipo(cedula, empleados_equipo):
                    print("Ese empleado ya fue registrado")
                    
                elif isinstance(empleado, Piloto):
                    if pilotos < 3:
                        empleados_equipo.append(empleado)
                        veces = veces + 1
                        pilotos = pilotos + 1
                    else:
                        print("Ya hay suficientes pilotos")

                elif isinstance(empleado, Mecanico):
                    if mecanicos < 8:
                        empleados_equipo.append(empleado)
                        veces = veces + 1
                        mecanicos += 1
                    else:
                        print("Ya hay suficientes mecanicos")

                elif isinstance(empleado, DirectorDeEquipo):
                    if director < 1:
                        empleados_equipo.append(empleado)
                        veces = veces + 1
                        director += 1
                    else:
                        print("Ya hay un director de equipo")
            
        equipo = Equipo(nombre_equipo, pais, anio, empleados_equipo)

        lista_equipos.append(equipo)

        


    for i in range(3):
        cedula = input("Ingrese cedula del piloto: ")
        if chequeo_cedula(cedula):
            chequeo_ced(cedula)
            if existe_empleado(cedula):
                empleado = obtener_empleados(cedula)
                if isinstance(empleado, Piloto):
                    if chequeo_cedEquipo(cedula, empleados_equipo):
                        print("Ese piloto ya fue registrado")
                    else:
                        empleados_equipo.append(empleado)
                else:
                    print("Ese empleado no es un piloto")
            else:
                print("Ese empleado no existe")

    for i in range(8):
        cedula = input("Ingrese cedula del mecanico: ")
        if chequeo_cedula(cedula):
            chequeo_ced(cedula)
            if existe_empleado(cedula):
                empleado = obtener_empleados(cedula)
                if isinstance(empleado, Mecanico):
                    if chequeo_cedEquipo(cedula, empleados_equipo):
                        print("Ese mecanico ya fue registrado")
                    else:
                        empleados_equipo.append(empleado)
                else:
                    print("Ese empleado no es un mecanico")
            else:
                print("Ese empleado no existe")

    for i in range(1):
        cedula = input("Ingrese cedula del director de equipo: ")
        if chequeo_cedula(cedula):
            chequeo_ced(cedula)
            if existe_empleado(cedula):
                empleado = obtener_empleados(cedula)
                if isinstance(empleado, DirectorDeEquipo):
                    if chequeo_cedEquipo(cedula, empleados_equipo):
                        print("Ese director de equipo ya fue registrado")
                    else:
                        empleados_equipo.append(empleado)
                else:
                    print("Ese empleado no es un director de equipo")
            else:
                print("Ese empleado no existe")

        print("El equipo fue creado con exito")


    while veces < 11:
        cedula_empleado = input("Ingrese cedula del empleado: ")
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
                print("El director fue asignado al equipo")
            else: 
                break

            if pilotos == 3: 
                print("Los pilotos fueron asignados al equipo")
            if mecanicos ==8: 
                print("Los mecanicos fueron asignados al equipo")"""
            