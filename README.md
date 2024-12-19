# retrieve_fasta tool

Extract sequences from a multi-FASTA file based on a list of accessions.
E.g: SILVA database accessions
accessions.txt
AACK01000032
AACY020355234
AACY020469094
AACY020551516
AACY020558197
AAFJ01000001
AAFJ01000001
AAFJ01000008
AAFL01000001
AAFL01000004




**Usage**  

```
extract_fasta.py [-h] -i INPUT -a ACCESSIONS -o OUTPUT
```

**Extract sequences from a multi-FASTA file based on a list of accessions.**

options:  
```
-h, --help
```
**show this help message and exit**  

```
-i INPUT, --input INPUT
```
**Input multi-FASTA file containing the sequences.**  

```
-a ACCESSIONS, --accessions ACCESSIONS
```
**Text file containing a list of accession numbers, one per line.**  

```
-o OUTPUT, --output OUTPUT
```
**Output FASTA file to save the extracted sequences.**  


**Example**  

```
python extract_fasta.py -i input.fasta -a accessions.txt -o output.fasta
```
