import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as escuta:
    frase = rec.listen(escuta)

print(rec.recognize_sphinx(frase))
