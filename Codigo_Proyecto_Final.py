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
import grovepi
import subprocess
from grove_rgb_lcd import *
from grove_i2c_barometic_sensor_BMP180 import BMP085

#################################################################
## Se inicializa un archivo que guardara los datos separados por comas

archivo="/home/pi/Desktop/Datos_Guardados.csv"     # Se guardara en el escritorio de la Raspberry Pi

#################################################################
                                         
## Pines de los sensores 
light_sensor            = 0     #Sensor de Luminosidad
temp_humidity_sensor    = 4     #Sensor de Humedad-Temperatura

#Pin de la resistencia variable
potenciometer = 2 #Se usa una resistencia variable para determinar el tiempo de muestreo en el programa   

#Se inicializa la luz de fondo del display en blanco
setRGB(255,255,255)

#Función para guardar los datos en el archivo CSV
def guardar_datos() :
     try:
           # Guardamos el tiempo y los datos de los sensores el el archivo CSV
            print("Guardando datos...")
            f=open(archivo,'a')
            f.write("%s,%.2f,%.2f,%d;\n" %(str(fecha_actual),light,temp,humidity))
            f.close() 
            return 0
     except (IOError,TypeError) as e:
        return 0
    
#Función usada para leer los datos de los sensores
def leer_sensor(light_sensor,temp_humidity_sensor):
    try:
        light=grovepi.analogRead(light_sensor)
        [temp,humidity] = grovepi.dht(temp_humidity_sensor,0)
        return [light,temp,humidity]
    except (IOError,TypeError) as e:
            #En caso de un error
            return [-1,-1,-1,-1]

def escalar_sensorluz(luz):
    try:
        luz = luz//80
        return luz
    except (IOError,TypeError) as e:
        return -1
def tiempo_muestreo(pot):
    try:
        res= (grovepi.analogRead(pot)//255.75)+ 1
        return res
    except (IOError,TypeError) as e:
        return -1
# Main
while True:
    #Ajustamos la escala del potencimetro para el tiempo de muestreo
    resp = tiempo_muestreo(potenciometer)
    #Obtiene la fecha actual de ejecución del programa
    fecha_actual = time.strftime("%Y-%m-%d:%H-%M-%S")
    #Obtiene el tiempo de ejecución del programa
    current_time = int(time.time())
    #Lee los datos de los sensores
    [light,temp,humidity]=leer_sensor(light_sensor,temp_humidity_sensor)
    #Escala el valor del sensor de luz
    light =escalar_sensorluz(light)
    #Muestra en la consola la fecha de ejecucion y los datos de los sensores
    print(("Time:%s\nLight: %d\nTemp: %.2fC\nHumidity: %d \n" %(fecha_actual,light,temp,humidity)))

    # Ajustamos el tiempo en que se guardan las lecturas segun el potencimetro
    if current_time-last_read_sensor>resp:
        
        guardar_datos()
        #Reinicia el tiempo de espera
        last_read_sensor=current_time
        
    #Actualizamos los datos del LCD    
    setText_norefresh("T:" + str(temp) + "c  L:" + str(light)+"lm  H:" + str(humidity) +"% Ts:"+str(resp))
    
    #Delay de 1 segundo
    time.sleep(1)
    