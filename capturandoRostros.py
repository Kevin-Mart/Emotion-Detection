import cv2
import os
import imutils

# Lista de emociones
emotions = ['Enojo', 'Felicidad', 'Sorpresa', 'Tristeza']

dataPath = 'C:/Users/xdkev/Documents/Uaemex/9/Tecnologias Emergentes/Proyecto/Emotion-Detection/Data' # Cambia a tu ruta base

# Inicializar el clasificador de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Captura de video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

for emotionName in emotions:
    print(f"*** Capturando rostros para emoción: {emotionName} ***")

    emotionsPath = os.path.join(dataPath, emotionName)
    
    # Crear carpeta si no existe
    if not os.path.exists(emotionsPath):
        print('Carpeta creada: ', emotionsPath)
        os.makedirs(emotionsPath)
    
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(os.path.join(emotionsPath, f'rostro_{count}.jpg'), rostro)
            count += 1

        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)
        if k == 27 or count >= 200:
            break

    print(f"*** Se capturaron {count} imágenes para la emoción: {emotionName} ***")
    cv2.destroyAllWindows()

# Liberar la cámara al final
cap.release()
