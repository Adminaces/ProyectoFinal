import pytest
from Codigo_Proyecto_Final import escalar_sensorluz

#Pruebas Unitarias
#Aunque probamos con todo lo que se nos ocurria al realizar las pruebas unitarias siempre
# se atoraba en collecting ... 
def test1_escalarluz():
    assert escalar_sensorluz(800) == 10
def test2_escalarluz():
    assert escalar_sensorluz(310.968) == 7
def test3_escalarluz():
    assert escalar_sensorluz(500.4993) == 6
    
#def test2_leer_sensor():
#def test3_leer_sensor():    
if __name__ == '_main_':
    #Ejecutamos pruebas
    test1_escalarluz()
    test2_escalarluz()
    test3_escalarluz()