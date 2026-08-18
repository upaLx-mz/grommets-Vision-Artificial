![Logo](https://lh3.googleusercontent.com/d/1_A28PnDD6JHo5EDi4M-69e6U8PEWiT2Z)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/upaLx-mz/grommets-Vision-Artificial)

# Grommets Artificial

Sistema de visión artificial diseñado con el proposito de reconocer entre las piezas buenas "OK" y las malas "NOK", que hay al salir de la estacón 180 de la linea de ensamble del IBC de ZF.

Mediante un modelo de IA entrenado con imagenes obtenidas de la linea, se examinan los grommets montados para tomar una desición.


## 🚀 Instalación

### 1. Python
Para correr el programa de detección se necesita Python en su versión 3.10. El instalable de Python se encuentra disponible en el siguiente enlace.

* [Python 3.10.10](https://www.python.org/downloads/release/python-31010/)

Una vez descargado el instalador correspondiente, se ejecuta el archivo y se instala Python de manera convencional, procurando que se agrege a las variables globales automaticamente.

### 2. Repositorio
 Descargar el repositorio de GitHub mediante el comando:

 ```bash
git clone https://github.com/upaLx-mz/grommets-Vision-Artificial.git
 ```
 ó mediante la descarga manual en GitHub.

### 3. Entorno virtual
  >[!NOTE]  
  >Se recomeinda el uso de un entorno virtual para poder aislar las dependencias y librerias del proyecto.


  Abrir una terminal de Powershell en la carpeta del repositorio y crear un entorno virtual de Python con el siguiente comando (en caso de solo tener instalada la versión 3.10.10):

 ```PowerShell
python -m venv .venv
 ```

 Si se tienen instaladas mas versiones de Python utilizar el siguiente comando:

 ```PowerShell
py -3.10 -m venv .venv
 ```

 Una vez creado el entono virtual lo activamos con:

 ```PowerShell
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned); .venv\Scripts\Activate.ps1
 ```
 Si todo lo anterior se realizo correctamente en la terminal se debe observar algo como lo siguiente:
 ```bash
 (.venv) PS C:\Users\user\...
 ```

### 4. Librerias
  >[!IMPORTANT]  
  >Es de suma importancia instalar  las librerias en el ordenn indicado para evitar errores de programa.
  
 Por utlimo paso hay que instalar las librerias que usa el proyecto, para eso utilizamos los comandos:

1.  
 ```pwsh
pip install -r requirements.txt
 ```
2. 
 ```pwsh
 pip install -r requirements2.txt
 ```
## 📖 Uso
Para ejecutar el programa de visión artificial, hay que tener abierto nuestro programa de CODESYS y Factory IO antes y corriendo sin ningun problema.

Despues en la terminal ejecutamos el comando:

```pwsh
python -m src.main
```
Y listo nuestro programa se deberia encontrar corriendo sin alguna novedad y preparada para ejecutar el analisis mediante visión artificial.

## 🔄 Flujo del proyecto
![arq](https://lh3.googleusercontent.com/d/1k1t3Il-stOw3bOxq9Wa2vktcSKhpq397)  
*Arquitectura general del sistema de inspección mediante visión artificial*  

![fswt](https://lh3.googleusercontent.com/d/10H5zsBphIqZLYP1sUtg9jnCxo0LXILws)  
*Diagrama de flujo del software principal*  

![falg](https://lh3.googleusercontent.com/d/1BvIIeDqevqAIJrJyMd7MP5v4QMeeMepq)  
*Flujo del algoritmo de visión artificial*  

![arqcom](https://lh3.googleusercontent.com/d/10ERetoaSOkBDqf9KZd1YscxUtd4XQhQW)  
*Arquitectura de comunicación*  

## ⌨️ Ejemplo de codigo
```python 
while 1:
  
  on = PLC.read_discrete_inputs(address=20, count=1, device_id=1)
  restart = PLC.read_discrete_inputs(address=21, count=1, device_id=1)
  
  onBit = on.bits[0]
  restartBit = restart.bits[0]
  
  ret, frame = camara.read()
  
  if not ret:
    logging.error("No se puede acceder al video")
    break
    
  frame = cv.flip(frame, 1)
  
  cv.rectangle(frame, (270,248), (494,472), (0,255,0), 3)
  cv.rectangle(frame, (528,278), (752,502), (0,255,0), 3)
  cv.rectangle(frame, (786,248), (1010,472), (0,255,0), 3)
  
  roi1 = frame[248:472, 270:494]
  roi2 = frame[278:502, 528:752]
  roi3 = frame[248:472, 786:1010]
  
  cv.imshow("Preview", frame)
  
  key = cv.waitKey(1)
  
  if onBit:
    habilitado = True
    
  if restartBit:
    habilitado = False
    
  if habilitado and conteo < 1:
    objeto1, resultado1 = analisys.analisisRGB(roi1)
    objeto2, resultado2 = analisys.analisisRGB(roi2)
    objeto3, resultado3 = analisys.analisisRGB(roi3)
    
  objetos = [objeto1, objeto2, objeto3]
  resultados = [resultado1, resultado2, resultado3]
  
  PLC.write_coil(address=20, value=True, device_id=1)
  
  logging.info(objetos)
  logging.info(resultados)
  logging.info("------------------")
  
  conteo += 1
  
  
  if "NOK\n" in objetos or "Faltante\n" in objetos and conteo2 == 0:
    conteo2 += 1
    PLC.write_coil(address=18, value=False, device_id=1)
    PLC.write_coil(address=19, value=True, device_id=1)
    logging.info("Pieza mala")

  if "OK\n" in objetos[0] and "OK\n" in objetos[1] and "OK\n" in objetos[2] and conteo2 == 0:  # noqa: E501
    conteo2 += 1
    PLC.write_coil(address=18, value=True, device_id=1)
    PLC.write_coil(address=19, value=False, device_id=1)
    logging.info("Pieza buena")
    
  if not habilitado:
    PLC.write_coil(address=20, value=False, device_id=1)
    conteo = 0
    conteo2 = 0
    objetos = [""] * 3
    
  if key == 27:
    break
  
```

## 🛠️ Tecnologias

* Python
* Factory IO
* Modbus
* CODESYS
