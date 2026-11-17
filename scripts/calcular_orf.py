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

    if gene not in genes_alvo:
        continue

    seq = str(registro.seq)

    maior_orf = 0

    for frame in range(3):

        inicio = frame

        while inicio < len(seq) - 2:

            codon = seq[inicio:inicio+3]

            if codon == "ATG":

                fim = inicio + 3

                while fim < len(seq) - 2:

                    stop = seq[fim:fim+3]

                    if stop in ["TAA", "TAG", "TGA"]:

                        tamanho_orf = fim + 3 - inicio

                        if tamanho_orf > maior_orf:
                            maior_orf = tamanho_orf

                        break

                    fim += 3

            inicio += 3

    resultados.append({
        "gene": gene,
        "transcrito": campos[4],
        "tamanho": len(seq),
        "maior_orf": maior_orf
    })

df_orf = pd.DataFrame(resultados)

df_orf.to_csv(
    "/home/shgtz/linfoma_lncRNA/resultados/orfs.csv",
    index=False
)

print(df_orf.head())