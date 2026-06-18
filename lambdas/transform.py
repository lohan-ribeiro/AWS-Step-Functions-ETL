import csv
from io import StringIO


def lambda_handler(event, context):

    conteudo = event["body"]

    arquivo_csv = StringIO(conteudo)
    leitor = csv.DictReader(arquivo_csv)

    saida = StringIO()

    campos = [
        "id",
        "cliente",
        "produto",
        "valor",
        "imposto"
    ]

    writer = csv.DictWriter(
        saida,
        fieldnames=campos
    )

    writer.writeheader()

    for linha in leitor:

        valor = float(linha["valor"])

        writer.writerow({
            "id": linha["id"],
            "cliente": linha["cliente"].upper(),
            "produto": linha["produto"],
            "valor": linha["valor"],
            "imposto": round(valor * 0.10, 2)
        })

    return {
        "arquivo_tratado": saida.getvalue()
    }