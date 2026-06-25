# Fast Port Scanner em Python

Um script simples, rápido e eficiente em Python para escanear portas de rede utilizando `ThreadPoolExecutor` para execução em paralelo (multithreading). O script identifica portas abertas em um determinado host/IP e tenta mapear o serviço que está rodando nelas.

---

## 🚀 Funcionalidades

* **Escaneamento Multithreaded:** Utiliza até 100 workers simultâneos para checar as portas rapidamente.
* **Resolução de Host:** Aceita tanto endereços IP quanto nomes de domínio (ex: `google.com`).
* **Identificação de Serviços:** Tenta traduzir o número da porta aberta para o nome do serviço padrão (ex: 80 -> http).
* **Sem Dependências Externas:** Escrito utilizando apenas bibliotecas nativas do Python (`socket`, `concurrent.futures`, `time`, `sys`).

---

## 🛠️ Pré-requisitos

Você só precisa do **Python 3.x** instalado na sua máquina. Nenhuma instalação de pacote via `pip` é necessária.

---

## 🔧 Como Usar

1. Clone o repositório ou baixe o arquivo `scan.py`.
2. Abra o terminal (Bash, CMD ou PowerShell) na pasta do arquivo.
3. Execute o script passando o **Host**, a **Porta Inicial** e a **Porta Final** como argumentos:

```bash
python scan.py <HOST_OU_IP> <PORTA_INICIAL> <PORTA_FINAL>
