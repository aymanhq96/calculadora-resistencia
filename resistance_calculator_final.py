import cv2
import numpy as np

# Tabla de colores para las bandas principales (R, G, B)
color_codes = {
    "negro":  (0, 0, 0),
    "marron": (150, 75, 0),
    "rojo":   (255, 0, 0),
    "naranja":(255, 165, 0),
    "amarillo": (255, 255, 0),
    "verde":  (0, 128, 0),
    "azul":   (0, 0, 255),
    "violeta":(138, 43, 226),
    "gris":   (128, 128, 128),
    "blanco": (255, 255, 255)
}

# Función para calcular distancia entre colores
def color_distance(c1, c2):
    return np.sqrt(sum((e1 - e2) ** 2 for e1, e2 in zip(c1, c2)))

# Función para obtener el color más cercano
def closest_color(color):
    
    min_dist = float('inf')
    min_color = None
    for name, rgb in color_codes.items():
        dist = color_distance(rgb, color)
        if dist < min_dist:
            min_dist = dist
            min_color = name
    return min_color

# Cargar imagen y preprocesar
image = cv2.imread('resistencia.jpg')
image = cv2.resize(image, (300, 100))  # reducir tamaño para acelerar

# Convertir a RGB (OpenCV lee BGR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Reshape para clustering
pixels = image_rgb.reshape((-1, 3))
pixels = np.float32(pixels)

# Ejecutar k-means con 3 clusters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 3
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convertir centros a enteros
centers = np.uint8(centers)

# Obtener colores detectados y asignar nombres
detected_colors = [closest_color(tuple(c)) for c in centers]

print("Colores detectados:", detected_colors)

# Asignar valores de las bandas según colores detectados
band_values = {
    "negro": 0,
    "marron": 1,
    "rojo": 2,
    "naranja": 3,
    "amarillo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "gris": 8,
    "blanco": 9
}

# Ordenar las bandas de izquierda a derecha (basado en posición, simplificado)
# Para mayor precisión, se podría detectar posición de cada banda, pero simplificamos

# Calcular valor resistencia: banda1 * 10 + banda2 * 1, multiplicado por banda3 como exponente de 10
try:
    v1 = band_values[detected_colors[0]]
    v2 = band_values[detected_colors[1]]
    multiplier = 10 ** band_values[detected_colors[2]]
    resistencia = (v1 * 10 + v2) * multiplier
    print(f"Resistencia calculada: {resistencia} ohmios")
except KeyError:
    print("Error: color no reconocido en las bandas")

