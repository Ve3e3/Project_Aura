# Esse arquivo vai guardar tudo que for relacionado à voz, escutar e falar.
# Funções que ele deve conter:
# falar(texto) → usa o pyttsx3
# ouvir_comando() → usa o speech_recognition para captar voz e retornar texto
# A ideia é deixar essas funções isoladas, para você poder importar em qualquer outro módulo.

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 180)   
engine.setProperty('volume', 1.0) 

reconhecedor = sr.Recognizer()

def falar(texto):
    """Faz o mecanismo de voz pronunciar o texto recebido."""
    print(f"Aura: {texto}")
    engine.say(texto)
    engine.runAndWait()

def ouvir_comando():
    """Capta o comando de voz do usuário e retorna como texto."""
    with sr.Microphone() as fonte:
        print("Aguardando comando...")
        audio = reconhecedor.listen(fonte)

    try:
        comando = reconhecedor.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
        return ""
    except sr.RequestError:
        print("Erro ao se conectar ao serviço de reconhecimento de fala.")
        return ""
