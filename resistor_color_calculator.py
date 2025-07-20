import cv2
import numpy as np

 #Diccionario de colores con sus valores rgb y 'valor' del color (r, g, b, valor)
codigo_colores = {
    'black':  (0, 0, 0, 0),
    'brown':  (150, 75, 0, 1),
    'red':    (255, 0, 0, 2),
    'orange': (255, 165, 0, 3),
    'yellow': (255, 255, 0, 4),
    'green':  (0, 128, 0, 5),
    'blue':   (0, 0, 255, 6),
    'violet': (128, 0, 128, 7),
    'grey':   (128, 128, 128, 8),
    'white':  (255, 255, 255, 9)
}

def color_mas_cercano(bgr_pixel):
    min_dist=float('inf') #Inicio distancia minima como infinita
    nombre_color=None     #Guardo nombre de color mas cercano
    for nombre, (r,g,b,_) in codigo_colores.items():
        dist= np.sqrt((r-bgr_pixel[2])**2+ (g-bgr_pixel[1])**2+(b-bgr_pixel[0])**2)
        if dist < min_dist:     #Si encontramos distancia mas pequeña
            min_dist =dist      #actualizamos valor
            nombre_color=nombre #guardamos valor de ese color

    return nombre_color         #Devolvemos color mas cercano

#Creamos lista vacia para guardar colores seleccionados por el usuario

colores_seleccionados=[]

#Funcion cuando haces clic en la imagen

def seleccionar_color(event,x,y,flags,param):
    global colores_seleccionados
    if event == cv2.EVENT_LBUTTONDOWN: #clic izq
        alto, ancho, _ = imagen.shape 
         # Definimos los límites de una región de 5x5 píxeles alrededor del clic
        x1 = max(x - 2, 0)
        x2 = min(x + 3, ancho)
        y1 = max(y - 2, 0)
        y2 = min(y + 3, alto)
                # Extraemos la región de 5x5 desde la imagen
        region = imagen[y1:y2, x1:x2]

        # Calculamos el promedio de color de toda esa región (en BGR)
        media_color = region.mean(axis=(0, 1)).astype(int)

        # Identificamos el color más cercano al promedio
        color = color_mas_cercano(media_color)

        # Guardamos el color en la lista
        colores_seleccionados.append(color)

        # Mostramos el color detectado por consola
        print(f"Color detectado (promedio): {color}")

        # Si ya se han seleccionado 3 bandas, calculamos el valor de la resistencia
        if len(colores_seleccionados) == 3:
            calcular_resistencia()

def calcular_resistencia():
    #Obtenemos el valor numero de cada color (posicion 3 en la tupla)
    a= codigo_colores[colores_seleccionados[0]][3]
    b= codigo_colores[colores_seleccionados[1]][3]
    c= codigo_colores[colores_seleccionados[2]][3]

    #Aplicamos la formula: (AB) * 10^C

    valor= (a*10 + b) *(10**c)

    print(f"\nValor de la resistencia: {valor} ohmios")
    print(f"Banda 1: {colores_seleccionados[0]}, Banda 2: {colores_seleccionados[1]}, Multiplicador: {colores_seleccionados[2]}")

# Nombre del archivo de imagen a cargar (ajusta según tu archivo)
ruta_imagen = 'resistencia.jpg'

# Cargamos la imagen con OpenCV
imagen = cv2.imread(ruta_imagen)

# Verificamos que se haya cargado correctamente
if imagen is None:
    print("No se pudo cargar la imagen. Asegúrate de que el archivo existe.")
    exit()

# Creamos una ventana donde se mostrará la imagen
cv2.namedWindow('Selecciona 3 bandas (clic izquierdo)')

# Asociamos la función de clic del mouse a la ventana
cv2.setMouseCallback('Selecciona 3 bandas (clic izquierdo)', seleccionar_color)

# Instrucción para el usuario
print("Haz clic sobre las 3 bandas de color de la resistencia (de izquierda a derecha)...")

# Bucle principal que mantiene abierta la imagen hasta que:
# - se presiona ESC (tecla 27), o
# - se han hecho 3 clics
while True:
    # Mostramos la imagen en la ventana
    cv2.imshow('Selecciona 3 bandas (clic izquierdo)', imagen)

    # Esperamos 1 ms por tecla y comprobamos condiciones de salida
    if cv2.waitKey(1) & 0xFF == 27 or len(colores_seleccionados) >= 3:
        break

# Cerramos todas las ventanas abiertas por OpenCV
cv2.destroyAllWindows()