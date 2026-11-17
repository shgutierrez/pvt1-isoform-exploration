# PVT1 Isoform Exploration
Exploratory bioinformatics project investigating the structural and compositional diversity of PVT1 lncRNA isoforms and their potential relevance to lymphoma biology using GENCODE annotations.

## Background

PVT1 is a long non-coding RNA (lncRNA) frequently associated with cancer biology, transcriptomic plasticity, and complex regulatory networks. The large number of annotated PVT1 isoforms raises the possibility that functional diversity may emerge not from a single dominant transcript, but from context-dependent usage of structurally related transcript families.

## Research Question

Can PVT1 isoforms be organized into structural and compositional families that suggest distinct regulatory programs?

## Data Sources

- GENCODE v47 transcriptome annotation
- GENCODE v47 GTF annotation

## Workflow

### Sequence-based analyses

- Identification of selected lncRNAs
- Isoform counting
- Transcript length characterization
- GC content analysis
- Longest ORF detection
- Dinucleotide composition analysis

### Motif-based analyses

Exploration of sequence motifs potentially associated with RNA-binding proteins (RBPs), including motifs related to:

- SRSF1-like regulation
- PTBP1-like regulation
- HNRNPC-like regulation
- G-rich regions
- AU-rich regions

### Multivariate analyses

- Principal Component Analysis (PCA)
- Isoform clustering based on motif composition

### Structural analyses

- Exploration of PVT1 transcript architectures using GTF annotations
- Identification of candidate transcript families

## Preliminary Findings

- 426 PVT1 isoforms were identified in GENCODE v47.
- Several transcripts emerged as compositional outliers during PCA analysis.
- Some outlier transcripts share highly similar exon architectures.
- Results suggest the existence of structural and compositional transcript families rather than a completely random distribution of isoforms.

## Working Hypothesis

PVT1 functional diversity may arise from context-dependent selection of transcript families, potentially mediated by alternative splicing programs and RNA-binding proteins, rather than from a single dominant transcript architecture.

## Next Steps

- Organize the repository and analysis pipeline.
- Search for publicly available Burkitt lymphoma RNA-seq datasets.
- Evaluate expression patterns of candidate PVT1 transcript families.
- Investigate possible associations between transcript family usage and disease context.

