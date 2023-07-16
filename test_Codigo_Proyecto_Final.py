import pytest
from Codigo_Proyecto_Final import escalar_sensorluz
from Codigo_Proyecto_Final import tiempo_muestreo

#Pruebas Unitarias

def test1_escalarluz():
    assert escalar_sensorluz(800) == 10
def test2_escalarluz():
    assert escalar_sensorluz(310.968) == 7
def test3_escalarluz():
    assert escalar_sensorluz(500.4993) == 6
    
def test1_tiempo_muestreo():
    assert tiempo_muestreo("60") == 60
def test2_tiempo_muestreo():
    assert tiempo_muestreo("600.25") == 600
def test3_tiempo_muestreo():
    assert tiempo_muestreo("45.25") == 45

#def test2_leer_sensor():
#def test3_leer_sensor():    
if __name__ == '_main_':
    #Ejecutamos pruebas
    test1_escalarluz()
    test2_escalarluz()
    test3_escalarluz()
    test1_tiempo_muestreo()
    test2_tiempo_muestreo() 
    test3_tiempo_muestreo()