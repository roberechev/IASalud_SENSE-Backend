#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

def transcribe_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Habla ahora...")
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print("Transcripción: {}".format(text))
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error en la solicitud a la API de reconocimiento de voz: {}".format(e))

# Llama a la función de transcripción desde el micrófono
transcribe_audio()