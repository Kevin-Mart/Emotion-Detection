# Emotion-Detection

## 📚 **Emotion-Detection: AI-Powered Sentiment Analysis**

🚀 **Descripción del Proyecto:**

Emotion-Detection es una aplicación basada en **Machine Learning** que identifica emociones humanas a partir de texto, imágenes o audio. Utilizando técnicas avanzadas de **NLP (Procesamiento de Lenguaje Natural)** y **CNN (Redes Neuronales Convolucionales)**, el modelo es capaz de analizar sentimientos como alegría, tristeza, enojo, sorpresa y más.

### 🎯 **Objetivo:**
Desarrollar un sistema capaz de detectar y clasificar emociones en tiempo real para aplicaciones como:
✅ Análisis de sentimientos en redes sociales.  
✅ Monitoreo de salud mental.  
✅ Mejora en la experiencia del cliente mediante análisis de retroalimentación.  

---

## 🛠️ **Tecnologías Utilizadas:**
- Python (TensorFlow, Keras, Scikit-learn)
- OpenCV para análisis de imágenes


## 📥 ¿Cómo instalar?

### 1. Clonar el repositorio

Primero necesitas clonar este proyecto en tu máquina local:

git clone https://tu-repositorio.git


### 2. Instalaciones requeridas
Antes de ejecutar el proyecto, necesitas instalar algunas dependencias.

### 🛠 OpenCV
OpenCV es una biblioteca de visión por computadora que permite detectar y procesar imágenes.

### Primero instala la versión básica:

pip install opencv-python
Después, reemplaza esta instalación con la versión "contrib", que incluye módulos adicionales necesarios para la detección de emociones:


pip uninstall opencv-python
pip install opencv-contrib-python
(La versión contrib contiene algoritmos extra que no están disponibles en la instalación estándar de OpenCV.)

### Crear la carpeta Data
El proyecto requiere una carpeta llamada Data, donde se almacenarán las imágenes de entrenamiento clasificadas por emociones.

Simplemente crea una carpeta llamada:

Data

### 4. Modificar la ruta de acceso (path) en el código
Dentro del archivo main.py, ubica la siguiente línea:
dataPath = 'C:/Users/xdkev/Documents/Uaemex/9/Tecnologias Emergentes/Proyecto/Emotion-Detection/Data'
Debes cambiar esta ruta para que apunte a la ubicación donde creaste la carpeta Data en tu computadora.
Por ejemplo:
dataPath = 'D:/MisProyectos/Emotion-Detection/Data'
### 🔵 Importante: Usa rutas absolutas y asegúrate de usar la sintaxis correcta de barras (/ o \\) según tu sistema operativo.

### 5. Ejecutar el proyecto
Una vez configurado todo, ejecuta el archivo principal con el siguiente comando en la terminal:

python main.py

# 🚀 ¡Todo listo para comenzar a detectar emociones!