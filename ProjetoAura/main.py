import time
from modules.voz import falar, ouvir_comando
from modules.comandos import executar_comando

def log(mensagem):
    """Exibe logs informativos no terminal para acompanhar o fluxo."""
    print(f"[LOG] {mensagem}")

def selecionar_modo(boas_vindas=True):
    """Pergunta ao usuário qual modo deseja usar."""
    if boas_vindas:
        log("Executando introdução inicial...")
        falar("Olá! Meu nome é Aura.")
        time.sleep(0.1)
        falar("Irei te ajudar hoje!")
        time.sleep(1.3)
    else:
        log("Mudança de modo detectada, pulando introdução...")

    falar("Diga: repetir, responder perguntas, ou sair para encerrar.")
    time.sleep(1.3)

    comando = ouvir_comando().lower()
    log(f"Comando reconhecido para modo: {comando}")

    if "repetir" in comando:
        log("Modo definido: repetir")
        time.sleep(0.8)
        return "repetir"
    elif "responder" in comando or "perguntar" in comando:
        log("Modo definido: responder")
        time.sleep(0.8)
        return "responder"
    elif "sair" in comando or "encerrar" in comando:
        log("Comando de saída recebido no menu principal")
        time.sleep(0.8)
        return "sair"
    else:
        log("Modo não reconhecido. Tentando novamente...")
        falar("Não entendi o modo escolhido. Vamos tentar de novo.")
        time.sleep(0.5)
        return selecionar_modo(boas_vindas=False)

def main():
    log("Iniciando Aura...")
    modo = selecionar_modo(boas_vindas=True)
    time.sleep(1)

    while True:
        log(f"Iniciando ciclo principal no modo: {modo}")

        if modo == "sair":
            falar("Encerrando o sistema. Até logo!")
            log("Sistema encerrado pelo usuário.")
            break

        if modo == "repetir":
            falar("Modo repetir ativado. Diga algo.")
            log("Esperando comando de voz no modo repetir.")
            time.sleep(1.5)
            comando = ouvir_comando()
            log(f"Comando captado no modo repetir: {comando}")

            if not comando:
                log("Nenhum comando reconhecido, repetindo escuta.")
                continue

            if "trocar modo" in comando or "mudar modo" in comando:
                falar("Certo. Vamos trocar o modo.")
                log("Usuário solicitou troca de modo.")
                time.sleep(1.5)
                modo = selecionar_modo(boas_vindas=False)
                continue
            elif "sair" in comando or "encerrar" in comando:
                falar("Encerrando o sistema. Até logo!")
                log("Usuário solicitou encerramento no modo repetir.")
                break
            else:
                falar(f"Você disse: {comando}")
                log("Repetição concluída.")
                time.sleep(1.5)

        elif modo == "responder":
            falar("Modo responder ativado. Faça uma pergunta.")
            log("Esperando pergunta no modo responder.")
            time.sleep(1.5)
            comando = ouvir_comando()
            log(f"Comando captado no modo responder: {comando}")

            if not comando:
                log("Nenhuma pergunta reconhecida, repetindo escuta.")
                continue

            if "trocar modo" in comando or "mudar modo" in comando:
                falar("Certo. Vamos trocar o modo.")
                log("Usuário solicitou troca de modo.")
                time.sleep(1.5)
                modo = selecionar_modo(boas_vindas=False)
                continue
            elif "sair" in comando or "encerrar" in comando:
                falar("Encerrando o sistema. Até logo!")
                log("Usuário solicitou encerramento no modo responder.")
                time.sleep(1.5)
                break
            else:
                log("Executando comando no modo responder...")
                executar_comando(comando)
                log("Execução do comando concluída.")
                time.sleep(1.2)

if __name__ == "__main__":
    main()
