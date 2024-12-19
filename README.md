# retrieve_fasta tool

usage: extract_fasta.py [-h] -i INPUT -a ACCESSIONS -o OUTPUT

Extract sequences from a multi-FASTA file based on a list of accessions.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input multi-FASTA file containing the sequences.
  -a ACCESSIONS, --accessions ACCESSIONS
                        Text file containing a list of accession numbers, one per line.
  -o OUTPUT, --output OUTPUT
                        Output FASTA file to save the extracted sequences.

Example: python extract_fasta.py -i input.fasta -a accessions.txt -o output.fasta
