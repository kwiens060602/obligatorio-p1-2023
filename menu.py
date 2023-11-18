import datetime
from entities.empleado import Empleado
from entities.auto import Auto
from entities.piloto import Piloto
from entities.piloto_suplente import PilotoSuplente
from entities.mecanico import Mecanico
from entities.director_equipo import DirectorDeEquipo
from entities.equipo import Equipo
from exceptions.informacion_invalida import InformacionInvalida


lista_empleados = []
lista_autos = []
lista_equipos = []
lista_lesionados = []
lista_pilotos = []
lista_abandonos = []
lista_error_pits = []
lista_penalidades = []
lista_pilotos_suplentes = []
lista_directores = []



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
    print(" ")
    print("Tipos de empleado:")
    print("1) Piloto")
    print("2) Piloto suplente")
    print("3) Mecanico")
    print("4) Director de equipo")
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
        tipo_empleado = Piloto(nombre_empleado,cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, score_piloto, nro_auto, puntaje_carrera = 0, lesion=False, suplente= False)
        lista_empleados.append(tipo_empleado)
        print("El piloto fue creado")

    elif tipo_empleado == 2:
        score_piloto = int(input("Ingrese el score del piloto: "))
        if not score_piloto >= 1 and score_piloto <= 99:
            raise InformacionInvalida("El score esta fuera del rango")
        nro_auto = int(input("Ingrese el numero del auto: "))
        if not nro_auto >= 1 and nro_auto <=99:
            raise InformacionInvalida("El numero del auto esta fuera del rango")
        tipo_empleado = PilotoSuplente(nombre_empleado,cedula_empleado, fecha_de_nacimiento_empleado, pais_de_nacimiento_empleado, salario_empleado, score_piloto, nro_auto, puntaje_carrera = 0, lesion=False, suplente= True)
        lista_empleados.append(tipo_empleado)
        print("El piloto suplente fue creado")

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
    if not pais_equipo.isalpha():
        raise InformacionInvalida("El dato ingresado no es válido")
    anio_equipo = input("Ingrese el año del equipo: ")
    if not anio_equipo.isnumeric():
        raise InformacionInvalida("El dato ingresado no es válido")

    
    empleados_equipo = []
    veces = 0
    pilotos = 0
    pilotos_suplentes = 0
    mecanicos = 0
    director = 0
   
    while pilotos < 2:
        cedula = input("Ingrese cedula del piloto: ")
        if not cedula.isnumeric():
            raise InformacionInvalida("El dato ingresado no es válido")
        if existe_empleado(cedula):
            empleado = obtener_empleados(cedula)
            if isinstance(empleado, Piloto):
                if chequeo_cedEquipo(cedula, empleados_equipo):
                    print("Ese piloto ya fue registrado")
                else:
                    empleados_equipo.append(empleado)
                    pilotos = pilotos + 1
                    lista_pilotos.append(empleado)
            else:
                print("Ese empleado no es un piloto")
        else:
            print("Ese empleado no existe")


    while pilotos_suplentes < 1:
        cedula = input("Ingrese cedula del piloto suplente: ")
        if not cedula.isnumeric():
            raise InformacionInvalida("El dato ingresado no es válido")      
        if existe_empleado(cedula):
            empleado = obtener_empleados(cedula)
            if isinstance(empleado, PilotoSuplente):
                if chequeo_cedEquipo(cedula, empleados_equipo):
                    print("Ese piloto suplente ya fue registrado")
                else:
                    empleados_equipo.append(empleado)
                    pilotos_suplentes = pilotos_suplentes + 1
                    lista_pilotos.append(empleado)
            else:
                print("Ese empleado no es un piloto suplente")
        else:
            print("Ese empleado no existe")

   
    while mecanicos < 8:
        cedula = input("Ingrese cedula del mecanico: ")
        if not cedula.isnumeric():
            raise InformacionInvalida("El dato ingresado no es válido")
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
        if not cedula.isnumeric():
            raise InformacionInvalida("El dato ingresado no es válido")
        if existe_empleado(cedula):
            empleado = obtener_empleados(cedula)
            if isinstance(empleado, DirectorDeEquipo):
                if chequeo_cedEquipo(cedula, empleados_equipo):
                    print("Ese director de equipo ya fue registrado")
                else:
                    empleados_equipo.append(empleado)
                    director = director + 1
                    lista_directores.append(empleado)
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






def simular_carrera(lista_lesionados, lista_abandonos, lista_error_pits, lista_penalidades):

    print("Si ya ingresó todos los pilotos lesionados, ingrese el numero 0")
    terminado = True
    while terminado:
        nro_auto_lesionado = input("Ingresar el numero de auto del piloto lesionado: ")
        if not nro_auto_lesionado.isnumeric():
            raise InformacionInvalida("El dato ingresado no es válido")
        if nro_auto_lesionado == 0:
            terminado = False
        else:
            for i in lista_pilotos:
                if i.nro_auto == nro_auto_lesionado:
                    lesionado = lista_pilotos[i]
                    lesionado.lesion = True
                    lista_lesionados.append(lesionado)


    
    nro_auto_abandono = input("Ingrese los numeros de los autos que abandonaron separados por una coma y sin espacios: ")
    lista_strings = nro_auto_abandono.split(",")

    lista_integers = []
    
    for i in range(len(lista_strings)):
        numero = int(lista_strings[i])
        lista_integers.append(numero)

    for i in lista_pilotos:
        for j in lista_integers:
            if i.nro_auto == lista_integers[j]:
                abandono = lista_pilotos[i]
                abandono.lesion = True
                lista_abandonos.append(abandono)



    print("Si ya ingresó todos los pilotos que cometieron error, ingrese el numero 0")
    terminado = True
    while terminado:
        nro_auto_error = input("Ingrese el numero de auto de todos los pilotos que cometen error en pits: ")
        if not nro_auto_error.isnumeric():
            raise InformacionInvalida("El dato ingresado no es válido")
        if nro_auto_error == 0:
            terminado = False
        else:
            for i in lista_pilotos:
                if i.nro_auto == nro_auto_error:
                    errores = lista_pilotos[i]
                    lista_error_pits.append(errores)



    print("Si ya ingresó todos los pilotos que recibieron penalidades, ingrese el numero 0")
    terminado = True
    while terminado:
        nro_auto_penalidad = input("Ingrese el numero de auto de todos los pilotos que reciben penalidad: ")
        if not nro_auto_penalidad.isnumeric():
            raise InformacionInvalida("El dato ingresado no es válido")
        if nro_auto_penalidad == 0:
            terminado = False
        else:
            for i in lista_pilotos:
                if i.nro_auto == nro_auto_penalidad:
                    penalizado = lista_pilotos[i]
                    lista_penalidades.append(penalizado)







    for i in lista_equipos:
        puntaje_piloto_uno = 0
        puntaje_piloto_dos = 0
        puntaje_piloto_suplente = 0
        puntaje_mecanico = 0
        puntaje_todos_mecanicos = 0
        pilotos_sanos = []

        
                
        for j in i.empleados()[3:11]:
            puntaje_mecanico = j.score_mecanico
            puntaje_sin_restar = puntaje_sin_restar + puntaje_mecanico

        puntaje_auto = i.auto().score
        puntaje_sin_restar = puntaje_sin_restar + puntaje_auto

        for j in i.empleados()[0:1]:
            if j.lesion == False:
                pilotos_sanos.append(j)
                puntaje_piloto_uno = j.score_piloto
                score_final_uno = puntaje_sin_restar + puntaje_piloto_uno
                j.puntaje_carrera_nuevo = score_final_uno
            elif j.lesion == True:
                puntaje_piloto_uno = 0

        for j in i.empleados()[1:2]:
            if j.lesion == False:
                pilotos_sanos.append(j)
                puntaje_piloto_dos = j.score_piloto
                score_final_dos = puntaje_sin_restar + puntaje_piloto_dos
                j.puntaje_carrera_nuevo = score_final_dos
            elif j.lesion == True:
                puntaje_piloto_dos = 0

        for j in i.empleados()[2:3]:
            if j.lesion == False:
                puntaje_piloto_suplente = j.score_piloto
                score_final_suplente = puntaje_sin_restar + puntaje_piloto_suplente
                j.puntaje_carrera_nuevo = score_final_suplente

            elif j.lesion == True:
                puntaje_piloto_suplente = puntaje_piloto_suplente + 0

            





def realizar_consultas():
    print("1) Top 10 pilotos con mas puntos en el campeonato")
    print("2) Resumen campeonato de constructores")
    print("3) Top 5 pilotos mejores pagos")
    print("4) Top 3 pilotos mas habilidosos")
    print("5) Retornar jefes de equipo")
    consulta = input("Eliga la consulta que quiera realizar")
    if consulta == 5:
        print(lista_directores)







      
    




menu = True 
while menu:
    print(" ")
    print ("Menú Principal")
    print ("Seleccione la opción del menú: ")
    print ("1. Alta de Empleado")
    print ("2. Alta de Auto")
    print ("3. Alta de Equipo")
    print ("4. Simular Carrera")
    print ("5. Realizar Consultas")
    print ("6. Finalizar Programa")
    opcion = int(input())
    try:
        if opcion == 1:
            alta_empleado(lista_empleados)
        elif opcion == 2:
            alta_auto(lista_autos)
        elif opcion == 3:
            alta_equipo(lista_equipos)
        elif opcion == 4:
            simular_carrera(lista_lesionados, lista_abandonos, lista_error_pits, lista_penalidades)
        elif opcion == 5:
            realizar_consultas()
        elif opcion == 6:
            menu = False
            print("Programa Finalizado")
        elif opcion != 1 or 2 or 3 or 4 or 5 or 6:
            print("Error, eliga una opcion que exista")
    except InformacionInvalida as e:
        print("Dato incorrecto")










