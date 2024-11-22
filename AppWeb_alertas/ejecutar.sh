#!/bin/bash

echo "Ejecutando el script de Alertas: Madrid Digital y tamaño ficheros"
python3 ./src/alertas.py 


echo "Iniciando la aplicación web AppWebFinanzas"
python3 ./src/app.py


# Esperar a que ambos procesos terminen
wait
echo "Todos los procesos han terminado."