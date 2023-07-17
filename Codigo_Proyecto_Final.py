#Código Proyecto Final V3--- 12 de Julio de 2023

#Integrantes

# Jose Miguel Caicedo Ortiz - 202225784 (Programador)

# Manuel Alejandro Almendra Ipia - 202229089 (Proveedor de Información)

# Catalina Henao Roa - 202226604 (Redactora)

# Camilo - 2022 (Ensamblador)

#AdminAces

'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

#################################################################
#Se importan las librerias necesarias para controlar los módulos del proyecto

import time
import subprocess
import csv

#################################################################
## Se inicializa un archivo que guardara los datos separados por comas

#archivo="\Users\Usuario\Usuario\Desktop\Datos_Guardados.csv"     # Se guardara en el escritorio

#################################################################
                                         
# Pines de los sensores 
light_sensor            = 0     #Sensor de Luminosidad
temp_humidity_sensor    = 4     #Sensor de Humedad-Temperatura

# Listas para guardar los arreglos de datos
Light_Data = []
Hum_Data = []
Temp_Data = []
Fecha = []
#Pin de la resistencia variable
#potenciometer = 2 #Se usa una resistencia variable para determinar el tiempo de muestreo en el programa   

#Variable para el tiempo de respuesta
resp = 1  
# Variable para el ciclo único de la funcion tiempo de muestreo
k = True
#Variable para guardar el tiempo previo
last_read_sensor = int(time.time())
#Función para guardar los datos en el archivo CSV
def guardar_datos() :
     try:
        # Guardamos el tiempo y los datos de los sensores el el archivo CSV
        '''
        long = len(Light_Data)
        f=open(archivo,'a')
        for i in long:
        f.write("%s,%.2f,%.2f,%d;\n" %(fecha_actual,Light_Data[i],Temp_Data[i],Hum_Data[i]))
        print("Guardando datos...")
        f.close()
        '''
        #for i in range[0, len(Fecha)]:
            #Fecha[i].append(str(Light_Data[i]))
            #Fecha[i].append(str(Temp_Data[i]))
            #Fecha[i].append(str(Hum_Data[i]))
        print(Fecha)
        with open('Datos_Guardados.csv', 'w', newline='') as csvf:
            escritor = csv.writer(csvf) 
            escritor.writerow(Fecha)
            escritor.writerow(Light_Data)
            escritor.writerow(Temp_Data)
            escritor.writerows(Hum_Data)
        return 0
     except (IOError,TypeError) as e:
        print("Error")
        return 0
    
#Función usada para leer los datos de los sensores por la consola
def leer_sensor():
    try:
        #Para simular los valores de los sensores estos se ingresan a través la consola para probar
            light=float(input('Ingrese la intensidad luminica\n'))
            temp = float(input('Ingrese la temperatura\n'))
            humidity = float(input('Ingrese la humedad\n'))
            return [light,temp,humidity]
    except (IOError,TypeError) as e:
            #En caso de un error
            return [-1,-1,-1]

def escalar_sensorluz(valor):
    try:
        result = valor//80
        return result
    except (IOError,TypeError) as e:
        return -1
def tiempo_muestreo():
    try:
        #res= (potencimeter//255.75)+ 1
        response = int(input('Ingrese el tiempo de muestreo\n'))
        return response
    except (IOError,TypeError) as e:
        return -1
# Main
while True:
    #Ajustamos la escala del potencimetro para el tiempo de muestreo !!(Una Vez)
    if  k:
        resp = tiempo_muestreo()
        k = False
    #Obtiene la fecha actual de ejecución del programa
    fecha_actual = time.strftime("%Y-%m-%d:%H-%M-%S")
    #Obtiene el tiempo de ejecución del programa
    current_time = int(time.time())
    #Lee los datos de los sensores
    [light,temp,humidity]=leer_sensor()
    #Escala el valor del sensor de luz
    light =escalar_sensorluz(light)
    #Guarda los datos de los sensores en las listas
    Light_Data.append(light)
    Temp_Data.append(temp)
    Hum_Data.append(humidity)
    Fecha.append(fecha_actual)
    #Muestra en la consola la fecha de ejecucion y los datos de los sensores
    print("Registro {0}:\n[Fecha: {1}, Intensidad Lum: {2} Lm, Temperatura: {3} C, Humedad: {4} %]".format(len(Light_Data),fecha_actual,light,temp,humidity))

    # Ajustamos el tiempo en que se guardan las lecturas segun el potencimetro
    if current_time-last_read_sensor>resp:
        print("Guardando datos...")
        guardar_datos()
        #Reinicia el tiempo de espera
        last_read_sensor=current_time
    #Actualizamos los datos del LCD    
    #setText_norefresh("T:" + str(temp) + "c  L:" + str(light)+"lm  H:" + str(humidity) +"% Ts:"+str(resp))
    
    #Delay de 1 segundos
    time.sleep(1)
    