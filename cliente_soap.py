#!/usr/bin/env python

from suds.client import Client
url = 'http://localhost:9014/HelloWorld?WSDL'
client = Client(url)
#print client

# client.service.crearAsignatura("mat-101","Matematica")
# client.service.crearAsignatura("mat-102","Matematica 2")
# client.service.crearAsignatura("esp-101","Espanol")
# estudiante=client.service.crearEstudiante("Manuel Saleta",20110579,"ISC",["mat-101"])
# estudiante=client.service.crearEstudiante("Siseto",20110590,"IC",["esp-101"])
# print client.service.editarEstudiante("Alvaro",20110579,'ITT')
# print client.service.agregarAsignaturaEstudiante(20110579,"mat-102")
# #print client.service.borrarEstudiante(20110579)
# print client.service.agregarAsignaturaEstudiante(20110579,"mat-102")
# print client.service.agregarAsignaturaEstudiante(20110577,"mat-102")
# estudiante = client.service.verEstudiantes()
# print estudiante


# !/usr/bin/python
# -*- coding: utf-8 -*-

import os


def menu():

    os.system('clear')  # NOTA para windows tienes que cambiar clear por cls
    print "Selecciona una opcion"
    print "\t1 - Nueva Asignatura"
    print "\t2 - Nuevo Estudiante"
    print "\t3 - Editar Estudiante"
    print "\t4 - Consultar Estudiante"
    print "\t5 - Borrar Estudiante"
    print "\t6 - Ver Listado Estudiantes"
    print "\t9 - salir"

def menuEdicion():

    while True:
        os.system('clear')  # NOTA para windows tienes que cambiar clear por cls
        print "Selecciona una opcion"
        print "\t1 - Editar Datos Estudiante"
        print "\t2 - Agregar Asignaturas a Estudiante"
        print "\t3 - Quitar Asignaturas a Estudiante"
        print "\t9 - volver"
        opcionMenu = raw_input("inserta un numero valor >> ")
        if opcionMenu == "1":
            editar_datos_estudiante()
        elif opcionMenu == "2":
            agregar_asig_estudiante()
        elif opcionMenu == "3":
            borrar_asig_estudiante()
        elif opcionMenu == "9":
            break
        else:
            print ""
            raw_input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")

def nueva_asignatura():
    os.system('clear')
    clave = ""
    while True:
        clave = raw_input("Digite la clave de la asignatura\n")
        nombre = raw_input("Digite el nombre de la asignatura\n")
        mensaje = client.service.crearAsignatura(clave, nombre)
        if mensaje == clave:
            break
        os.system('clear')
        print "YA HAY UNA ASIGNATURA CON ESTA CLAVE"
        print "Porfavor vuelva a digitar los datos..."
    print "Asignatura '" + clave + "' creada con exito!"
    raw_input("pulsa una tecla para continuar\n")



def nuevo_estudiante():
    os.system('clear')
    matricula = ""
    while True:
        nombre = raw_input("Digite el nombre del estudiante\n")
        matricula = int(raw_input("Digite la matricula\n"))
        carrera = raw_input("Digite la carrera\n")
        print "Ahora debe digitar las asignaturas del estudiante."
        print "Ingrese 0 para acabar de agregar asignaturas."

        asignaturas = []
        while True:
            asig = raw_input("Digite el codigo de la asignatura\n")
            if asig == '0':
                break
            asignaturas.append(asig)
        mensaje = client.service.crearEstudiante(nombre,matricula,carrera,asignaturas)
        if mensaje == matricula:
            break
        elif mensaje == -1:
            os.system('clear')
            print "YA HAY UN ESTUDIANTE CON ESTA MATRICULA"
            print "Porfavor vuelva a digitar los datos..."
        elif mensaje == -2:
            os.system('clear')
            print "HA DIGITADO ASIGNATURAS NO EXISTENTES"
            print "Porfavor vuelva a digitar los datos..."
    print "Estudiante con matricula '" + str(matricula) + "' creado con exito!"
    raw_input("pulsa una tecla para continuar\n")



def editar_datos_estudiante():
    os.system('clear')

    while True:
        matricula = raw_input("Digite la clave de la matricula del estudiante a editar\n")
        nombre = raw_input("Digite el nuevo nombre\n")
        carrera = raw_input("Digite la nueva carrera\n")
        mensaje = client.service.editarEstudiante(nombre,matricula,carrera)
        if mensaje == "ok":
            break
        os.system('clear')
        print "ESTE ESTUDIANTE NO EXISTE"
        print "Porfavor vuelva a digitar los datos..."
    print "Estudiante con matricula '" + matricula + "' editada con exito!"
    raw_input("pulsa una tecla para continuar\n")

def borrar_asig_estudiante():
    os.system('clear')

    while True:
        matricula = raw_input("Digite la clave de la matricula del estudiante a editar\n")
        codigo = raw_input("Digite el codigo de la asignatura a borrar.\n")

        mensaje = client.service.borrarAsignaturaEstudiante(matricula, codigo)
        if mensaje == "ok":
            break
        elif mensaje == "error_matricula":
            os.system('clear')
            print "ESTE ESTUDIANTE NO EXISTE"
            print "Porfavor vuelva a digitar los datos..."
        elif mensaje == "error_asignatura":
            os.system('clear')
            print "ESTA ASIGNATURA NO EXISTE"
            print "Porfavor vuelva a digitar los datos..."

    print "Estudiante con matricula '" + matricula + "' editado con exito!"
    raw_input("pulsa una tecla para continuar\n")

def agregar_asig_estudiante():
    os.system('clear')

    while True:
        matricula = raw_input("Digite la clave de la matricula del estudiante a editar\n")
        codigo = raw_input("Digite el codigo de la asignatura a agregar.\n")

        mensaje = client.service.agregarAsignaturaEstudiante(matricula, codigo)
        if mensaje == "ok":
            break
        elif mensaje == "error_matricula":
            os.system('clear')
            print "ESTE ESTUDIANTE NO EXISTE"
            print "Porfavor vuelva a digitar los datos..."
        elif mensaje == "error_asignatura":
            os.system('clear')
            print "ESTA ASIGNATURA NO EXISTE"
            print "Porfavor vuelva a digitar los datos..."
        elif mensaje == "error_asignatura_repetida":
            os.system('clear')
            print "ESTE ESTUDIANTE YA TIENE ESA ASIGNATURA"
            print "Porfavor vuelva a digitar los datos..."

    print "Estudiante con matricula '" + matricula + "' editado con exito!"
    raw_input("pulsa una tecla para continuar\n")

def consultar_estudiante():
    os.system('clear')

    while True:
        matricula = raw_input("Digite la clave de la matricula del estudiante a consultar\n")

        estudiante = client.service.getEstudiante(matricula)
        if estudiante is not None:
            break
        else:
            os.system('clear')
            print "ESTE ESTUDIANTE NO EXISTE"
            print "Porfavor vuelva a digitar los datos..."


    print "\nNombre: " + estudiante.nombre
    print "Matricula: " + str(estudiante.matricula)
    print "Carrera:" + estudiante.carrera
    print "Asignaturas:"
    for asignatura in estudiante.asignaturas:
        print "\t" + asignatura.codigo + " - " + asignatura.nombre
    raw_input("\n\n\nPulsa tecla para continuar...")

def borrar_estudiante():
    os.system('clear')

def ver_estudiantes():
    os.system('clear')

while True:
    # Mostramos el menu
    menu()


    opcionMenu = raw_input("inserta un numero valor >> ")

    if opcionMenu == "1":
        nueva_asignatura()
    elif opcionMenu == "2":
        nuevo_estudiante()
    elif opcionMenu == "3":
        menuEdicion()
    elif opcionMenu == "4":
        consultar_estudiante()
    elif opcionMenu == "9":
        break
    else:
        print ""
        raw_input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")