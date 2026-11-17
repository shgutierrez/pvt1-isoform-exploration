from Bio import SeqIO
from collections import Counter
import pandas as pd

genes_alvo = {
    "MALAT1",
    "NEAT1",
    "HOTAIR",
    "PVT1",
    "XIST",
    "GAS5"
}

arquivo = "/home/shgtz/linfoma_lncRNA/dados_brutos/gencode.v47.transcripts.fa"

resultados = []

for registro in SeqIO.parse(arquivo, "fasta"):

    campos = registro.description.split("|")

    gene = campos[5]

    if gene not in genes_alvo:
        continue

    seq = str(registro.seq)

    dinucs = [
        seq[i:i+2]
        for i in range(len(seq)-1)
    ]

    contagem = Counter(dinucs)

    total = sum(contagem.values())

    linha = {
        "gene": gene,
        "transcrito": campos[4]
    }

    for dinuc in [
        "AA","AC","AG","AT",
        "CA","CC","CG","CT",
        "GA","GC","GG","GT",
        "TA","TC","TG","TT"
    ]:

        linha[dinuc] = (
            contagem.get(dinuc,0) /
            total
        )

    resultados.append(linha)

df_dinuc = pd.DataFrame(resultados)

df_dinuc.to_csv(
    "/home/shgtz/linfoma_lncRNA/resultados/dinucleotideos.csv",
    index=False
)

print(df_dinuc.head())