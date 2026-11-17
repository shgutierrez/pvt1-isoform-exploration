from Bio import SeqIO
import pandas as pd
from pathlib import Path

genes_alvo = {
    "MALAT1",
    "NEAT1",
    "HOTAIR",
    "PVT1",
    "XIST",
    "GAS5"
}

arquivo = Path(
    "/home/shgtz/linfoma_lncRNA/dados_brutos/gencode.v47.transcripts.fa"
)

resultados = []

for registro in SeqIO.parse(arquivo, "fasta"):

    campos = registro.description.split("|")

    gene = campos[5]

    if gene in genes_alvo:

        seq = str(registro.seq)

        gc = (
            seq.count("G")
            + seq.count("C")
        ) / len(seq) * 100

        resultados.append({
            "gene": gene,
            "transcrito": campos[4],
            "tamanho": len(seq),
            "gc": gc
        })

df = pd.DataFrame(resultados)

df.to_csv(
    "/home/shgtz/linfoma_lncRNA/resultados/lncrnas_gc.csv",
    index=False
)

print(df.head())
