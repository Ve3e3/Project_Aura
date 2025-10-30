# Aqui ficará a “inteligência” da Aura.
# Função principal:
# processar_comando(texto)
# Recebe o texto reconhecido da fala
# Analisa palavras-chave
# Decide o que fazer (responder hora, data, sair, etc.)
# Chama falar() para responder

from datetime import datetime
from modules.voz import falar
import time
import requests 

def obter_clima(cidade="São Paulo"):
    """
    Busca o clima atual de uma cidade usando a API do wttr.in.
    """
    try:
        url = f"https://wttr.in/{cidade}?format=j1"
        response = requests.get(url)
        response.raise_for_status() 
        dados = response.json()
        condicao_atual = dados['current_condition'][0]
        temp_c = condicao_atual['temp_C']
        descricao_clima = condicao_atual['weatherDesc'][0]['value']
        
        return f"O tempo em {cidade} agora está com {temp_c} graus Celsius e {descricao_clima}."
        time.sleep(1.5)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar clima: {e}")
        return "Desculpe, não consegui obter os dados do clima no momento."
    except (KeyError, IndexError):
        return f"Não foi possível encontrar os dados do clima para a cidade {cidade}."

def executar_comando(comando):
    comando = comando.lower()

    if "horas" in comando:
        agora = datetime.now().strftime("%H:%M")
        falar(f"Agora são {agora}")
        time.sleep(1.5)

    elif "data" in comando or "dia" in comando:
        hoje = datetime.now().strftime("%d do %m de %Y")
        falar(f"Hoje é dia {hoje}")
        time.sleep(1.5)

    elif "clima" in comando or "tempo" in comando:
        dados_clima = obter_clima("São Paulo") 
        falar(dados_clima)
        time.sleep(1.5)

    elif "tudo bem" in comando or "como vai" in comando or "tudo certo" in comando:
        falar("Estou ótima! E você, tudo bem por aí?")
        time.sleep(1.5)
        
    elif "sim, estou bem" in comando or "também estou bem" in comando:
        falar("Que ótimo! Fico feliz em ouvir isso!")
        time.sleep(1.5)
        
    else:
        falar("Desculpe, ainda não aprendi este comando.")
        time.sleep(1.5)
