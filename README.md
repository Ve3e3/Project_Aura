👾 Projeto: Assistente Virtual em Python (Aura) 👾

📖 Descrição do Projeto
Este projeto tem como objetivo o desenvolvimento de uma assistente virtual em Python, batizada de Aura. Ela é capaz de interagir com o usuário por meio de voz, compreender comandos básicos e executar ações simples, proporcionando uma experiência interativa e natural.

A assistente combina tecnologias de reconhecimento de fala (Speech-to-Text) e síntese de voz (Text-to-Speech) para criar um fluxo de comunicação semelhante ao de assistentes digitais comerciais como Siri, Alexa e Google Assistant. O foco principal é o aprendizado e a experimentação com Python em um contexto de inteligência artificial básica.

✨ Funcionalidades
Até o momento, o projeto contempla as seguintes funcionalidades:

🎙️ Reconhecimento de Voz: Captura a fala do usuário através do microfone e a converte em texto, utilizando a biblioteca SpeechRecognition.

🗣️ Resposta em Voz: A assistente responde em áudio com uma voz sintetizada, permitindo um feedback imediato e claro ao usuário, graças à biblioteca pyttsx3.

⚙️ Comandos Básicos: Estrutura preparada para reconhecer comandos simples e executar ações correspondentes, como:

Repetir o que foi dito.

Fornecer a hora e a data atuais.

Responder a saudações e frases pré-definidas.

🔄 Loop Interativo: A assistente opera em um loop contínuo, ouvindo e processando comandos até que receba um comando específico de encerramento.

📂 Estrutura do Projeto
O projeto está organizado da seguinte forma para facilitar a manutenção e escalabilidade:

ProjetoAura/
│
├── main.py            # Código principal da assistente
├── requirements.txt   # Lista de dependências para rodar o projeto
└── README.md          # Esta documentação
🛠️ Bibliotecas Utilizadas
Para o funcionamento do projeto, as seguintes bibliotecas são essenciais:

Biblioteca	Função
SpeechRecognition	Captura e converte o áudio do microfone em texto.
pyttsx3	Sintetiza texto em fala para as respostas da Aura.
PyAudio	Interface de baixo nível com o microfone do sistema.
datetime	Módulo padrão do Python para obter data e hora.
Instalação

Para instalar todas as dependências, execute o seguinte comando no seu terminal:

Bash
pip install -r requirements.txt
🎯 Conceito e Objetivo
O projeto foi criado como uma base para um assistente virtual personalizado e escalável. A ideia é que ele possa evoluir para:

Reconhecer múltiplos comandos e palavras-chave com maior precisão.

Integrar-se com serviços externos via APIs (ex: previsão do tempo, notícias, tocar música no Spotify).

Aprimorar a interação, simulando um assistente que entende contexto e responde de forma mais natural e inteligente.

O principal objetivo é aplicar e aprofundar conhecimentos em Python, incluindo estruturas de funções, loops, manipulação de áudio e lógica de programação voltada para IA.

🚀 Próximos Passos
O roadmap de desenvolvimento inclui:

[ ] Processamento Inteligente de Comandos: Implementar uma lógica mais robusta para interpretar as intenções do usuário.

[ ] Modularização: Criar funções específicas para cada ação (ex: obter_hora(), contar_piada(), buscar_noticia()).

[ ] Interação Contínua: Estruturar o loop principal para ser mais eficiente e responsivo.

[ ] Expansão de Funcionalidades: Adicionar comandos mais avançados, mantendo o código limpo e organizado.

[ ] Personalização da Voz: Permitir a troca da voz e da velocidade da fala.
