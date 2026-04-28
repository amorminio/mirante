Versão 0.1.1

1 - Instalação : 

    1. Clonar o repositório
    git clone https://github.com/amorminio/mirante.git
    cd mirante

    2. Criar e ativar o ambiente virtual
    python3 -m venv venv
    source venv/bin/activate

    3. Instalar as dependências
    pip install -r requirements.txt

    4. Instalar o projeto
    pip install -e .


2 - Uso :

    A estrutura básica do comando é:
    vendas-cli [ARQUIVO_CSV] [PARÂMETROS]

    Parâmetros Disponíveis :

    Parâmetro   Descrição                                    Formato / Padrão
    arquivo     Caminho para o CSV de vendas.                caminho/do/arquivo.csv 
    --inicio    Data inicial para filtrar o relatório.       dd-mm-YYYY
    --fim       Data final para filtrar o relatório.         dd-mm-YYYY


3 - Exemplos :
    
    vendas-cli vendas.csv
    vendas-cli vendas.csv --inicio 01-04-2026 --fim 30-04-2026


4 - Bateria de Testes :

    1. Executar todos os testes
    pytest

    2. Gerar relatório de cobertura de código
    pytest --cov=src --cov-report=term-missing

    3. Validar tipagem estática
    mypy src/

5 - Arquivo CSV

    produto: Nome do item.

    quantidade: Valor inteiro.

    preco_unitario: Valor numérico (ponto como separador decimal).

    data_venda: Data no formato dd/mm/YYYY.