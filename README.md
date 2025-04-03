# Configuração do Apache Superset no Ubuntu 24.04 LTS (WSL 2)

Este repositório contém arquivos de configuração e instruções para instalar e rodar o Apache Superset em um ambiente Ubuntu 24.04 LTS (ou similar) via WSL 2, utilizando Python 3.10.

## Pré-requisitos

*   Windows 10 ou 11 com WSL 2 instalado e configurado.
*   Ubuntu 24.04 LTS (ou uma versão que suporte Python 3.10 via PPA) instalado no WSL 2.
*   Git instalado no Ubuntu (`sudo apt install git`).
*   Acesso à internet para baixar pacotes.
*   `openssl` instalado (geralmente padrão no Ubuntu) para gerar a `SECRET_KEY`.

## Instalação Passo a Passo

1.  **Clone este Repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO_GITHUB>
    cd <NOME_DO_DIRETORIO_CLONADO> # Ex: cd superset-config
    ```

2.  **Instale Dependências do Sistema:**
    ```bash
    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y build-essential libssl-dev libffi-dev pkg-config default-libmysqlclient-dev libpq-dev software-properties-common
    ```

3.  **Instale Python 3.10 (Usando PPA deadsnakes):**
    *   Se o Python 3.10 não estiver disponível diretamente nos repositórios da sua versão do Ubuntu:
        ```bash
        sudo add-apt-repository ppa:deadsnakes/ppa
        sudo apt update
        sudo apt install -y python3.10 python3.10-dev python3.10-venv
        ```
    *   Verifique a instalação: `python3.10 --version`

4.  **Crie e Ative o Ambiente Virtual Python:**
    ```bash
    python3.10 -m venv venv
    source venv/bin/activate
    ```
    *(O prompt deve mudar para incluir `(venv)`)*

5.  **Atualize Pip e Instale Ferramentas de Build:**
    ```bash
    pip install --upgrade pip setuptools wheel
    ```

6.  **Instale as Dependências Python do Projeto:**
    ```bash
    pip install -r requirements.txt
    ```

7.  **Configure a `SECRET_KEY`:**
    *   **Gere sua chave:** No terminal, execute:
        ```bash
        openssl rand -base64 42
        ```
    *   **Copie** a chave gerada.
    *   **Edite o arquivo `superset_config.py`:**
        ```bash
        nano superset_config.py
        ```
    *   **Substitua** a linha `SECRET_KEY = 'COLOQUE_SUA_CHAVE_SECRETA_FORTE_GERADA_AQUI'` pela chave que você acabou de copiar (mantenha as aspas simples).
    *   Salve e feche (`Ctrl+X`, `Y`, `Enter`).

8.  **Defina Variáveis de Ambiente:**
    ```bash
    export FLASK_APP=superset
    # Opcional, mas recomendado: informa onde está o config
    export SUPERSET_CONFIG_PATH=$(pwd)/superset_config.py
    ```
    *(Lembre-se de exportar estas variáveis sempre que ativar o venv em um novo terminal)*

9.  **Inicialize o Banco de Dados do Superset:**
    ```bash
    superset db upgrade
    ```

10. **Crie o Usuário Administrador:**
    ```bash
    superset fab create-admin
    ```
    *(Siga as instruções interativas)*

11. **Carregue Dados de Exemplo (Opcional):**
    ```bash
    superset load_examples
    ```

12. **Inicialize Roles e Permissões:**
    ```bash
    superset init
    ```

13. **Pronto!** Você pode iniciar o servidor.

## Rodando o Servidor

1.  Navegue até o diretório do projeto: `cd <NOME_DO_DIRETORIO_CLONADO>`
2.  Ative o ambiente virtual: `source venv/bin/activate`
3.  Exporte as variáveis de ambiente:
    ```bash
    export FLASK_APP=superset
    export SUPERSET_CONFIG_PATH=$(pwd)/superset_config.py
    ```
4.  Inicie o servidor:
    ```bash
    superset run -p 8088 --with-threads --reload --debugger
    ```
5.  Acesse `http://localhost:8088` no navegador do seu Windows.
6.  Para parar o servidor, pressione `Ctrl + C` no terminal.

```
*   Salve e feche o `nano`.
