import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

reconhecedor = sr.Recognizer()

with sr.Microphone() as fonte:
    print("Diga algo...")
    reconhido = False
    while not reconhido:
        try:
            audio = reconhecedor.listen(fonte)
            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            falar(f"Você disse: {texto}")
            reconhido = True
        except sr.UnknownValueError:
            print("Não entendi, tente novamente...")
        except sr.RequestError:
            print("Erro ao conectar com o serviço de reconhecimento de fala")
            break
