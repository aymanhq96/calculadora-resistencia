# Detector de colores de bandas de resistencia

Este proyecto permite calcular el valor de una resistencia a partir de una imagen usando clics de usuario para seleccionar las 3 bandas de color.

### Tecnologías utilizadas
  -Python 3
  -OpenCV
  -NumPy

### ¿Cómo funciona?
  1. Cargas una imagen de una resistencia ('resistencia.jpg')
  2. Haces clic sobre las 3 bandas de color de izquierda a derecha.
  3. El programa calcula y muestra el valor en Ohmios

### Ejecución
  1.Instala los modulos necesarios:

```
pip install opencv-python numpy
```

  2.Coloca una imagen llamada resistencia.jpg en la misma carpeta

  3.Ejecuta el script

  4.Haz clic en las 3 bandas de la resistencia (de izq a derecha)

### Notas
   -El script trabaja con el promedio de color en un area de 5x5 píxeles alrededor del clic.
   
   -Se ignora la banda de tolerancia
   
   -La detección de color se basa en la distancia euclidea entre colores estandar y el color promedio clicado
   
```
calculadora-resistencia/
├── resistencia.jpg
├── resistor_color_calculator.py
├── README.md
```

### Mejoras futuras
   -Deteccion automatica de bandas
   
   -Soporte para mas bandas
   
   -Mejora de precisión con HSV o modelos de aprendizaje automático

   
