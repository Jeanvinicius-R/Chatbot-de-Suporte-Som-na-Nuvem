# 🎵 Chatbot de Suporte — Som na Nuvem

Este projeto consiste no desenvolvimento de um **chatbot de suporte ao cliente** para a plataforma fictícia de streaming de música **Som na Nuvem**. O chatbot foi desenvolvido utilizando **Rasa** e tem como objetivo automatizar o atendimento aos assinantes, respondendo dúvidas comuns e auxiliando na resolução de problemas.

---

# 📌 Contexto

A plataforma **Som na Nuvem** recebe diversas solicitações de suporte relacionadas a:

- Problemas de acesso à conta
- Mudança de plano de assinatura
- Falhas no aplicativo
- Problemas de pagamento

Para melhorar a experiência do usuário e reduzir a sobrecarga da equipe de suporte, foi implementado um chatbot capaz de identificar o problema do usuário e fornecer orientações automáticas.

---

# ⚙️ Tecnologias Utilizadas

- Python
- Rasa
- Rasa SDK
- Miniconda
- HTML (interface web)
- Socket.IO
- JSON (base de dados de suporte)

---

# 🧠 Funcionamento do Chatbot

O chatbot utiliza conceitos fundamentais de desenvolvimento de assistentes conversacionais.

## Entity

A entity **`problema`** identifica o tipo de problema relatado pelo usuário.

Exemplos:

- acesso à conta
- mudar plano
- aplicativo não funciona
- pagamento

---

## Slot

O slot **`problema`** armazena o tipo de problema informado pelo usuário, permitindo manter o contexto da conversa.

---

## Action

A action customizada **`action_fornecer_suporte`** é responsável por:

- consultar a base de dados
- retornar instruções de solução
- enviar links de ajuda
- encaminhar para atendimento humano quando necessário

---

# 🗂 Estrutura do Projeto

chatbot04/
│
├── actions/
│ └── actions.py
│
├── data/
│ ├── nlu.yml
│ ├── rules.yml
│ └── stories.yml
│
├── models/
│
├── base_suporte.json
├── config.yml
├── credentials.yml
├── domain.yml
├── endpoints.yml
│
├── chat.html
│
└── README.md


---

# 💬 Interface Web

Foi criada uma interface simples em **HTML** utilizando o widget **rasa-webchat**, permitindo que o usuário interaja com o chatbot diretamente pelo navegador.

---

# 🚀 Como Executar o Projeto

## 1️⃣ Ativar o ambient,
````bash
conda activate chatbot

````
2️⃣ Rodar o servidor de actions
````
rasa run actions
````
3️⃣ Rodar o servidor do chatbot
````
rasa run --enable-api --cors "*"
````
4️⃣ Abrir a interface web

Abra o arquivo:

chat.html

no navegador.

📈 Benefícios do Chatbot

Redução do tempo de espera dos assinantes

Atendimento automatizado 24 horas

Melhoria na experiência do usuário

Redução da carga da equipe de suporte

👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos para estudo de chatbots, processamento de linguagem natural e automação de atendimento ao cliente

