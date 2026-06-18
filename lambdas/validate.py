import json
import csv
from io import StringIO

def lambda_handler(event, context):
    colunas_esperadas = [
        "id",
        "cliente",
        "produto",
        "valor"
    ]

    # extrair as colunas e dados do meu body para validação
    conteudo = event["body"]
    arquivo_csv = StringIO(conteudo)
    leitor = csv.DictReader(arquivo_csv)

    colunas_csv = leitor.fieldnames
    dados = list(leitor)

    # valida se existe colunas no arquivo
    if colunas_csv is None:
        return {
            "status": "invalid",
            "error": "Arquivo vazio"
        }

    # valida o arquivo a partir das colunas esperadas
    colunas_validas = True

    for coluna in colunas_esperadas:
        if coluna not in colunas_csv:
            colunas_validas = False
            break


    # valida se o arquivo possui dados
    if len(dados) >= 1:
        dados_validos = True
    else :
        dados_validos = False


    # mensagem de erro dinâmica
    if not colunas_validas:
        erro = "Colunas inválidas"

    elif not dados_validos:
        erro = "Arquivo sem registros"


    # retorna para o meu choice state
    if colunas_validas and dados_validos :
        return {
            "status": "valid",
            "body": conteudo
        }
    
    else :
        return {
            "status": "invalid",
            "error": erro
        }