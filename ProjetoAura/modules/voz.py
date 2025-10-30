import speech_recognition as sr
import pyttsx3
import time

# Inicializa a engine de voz
engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

# Inicializa o reconhecedor de fala
reconhecedor = sr.Recognizer()

def falar(texto):
    """Faz o mecanismo de voz pronunciar o texto recebido sem travar."""
    print(f"Aura: {texto}")

    # Divide o texto em partes menores para evitar travamento
    partes = texto.split(". ")
    for parte in partes:
        if parte.strip():
            engine.say(parte.strip())
            engine.runAndWait()
            time.sleep(0.2)  # pequena pausa entre frases

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
