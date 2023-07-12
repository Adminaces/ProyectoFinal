import pytest
from Codigo_Proyecto_Final import escalar_sensorluz, leer_sensor
from Codigo_Proyecto_Final import tiempo_muestreo

#Pruebas Unitarias

def test1_escalarluz():
    assert escalar_sensorluz(80,24,35) == [80,24,35]
def test2_escalarluz():
    assert escalar_sensorluz(65.493,39.444,70.455) == [80,24,35]
def test3_escalarluz():
    assert escalar_sensorluz(-1,4024040,-40182.1441) == [-1,-1,-1]
    
def test1_tiempo_muestreo():
    assert tiempo_muestreo(1023) == 5
def test1_tiempo_muestreo():
    assert tiempo_muestreo(1023) == 5

def test1_leer_sensor():
    assert leer_sensor(25, 15)==[25,15] 
#def test2_leer_sensor():
#def test3_leer_sensor():    
if __name__ == '_main_':
    #Ejecutamos pruebas