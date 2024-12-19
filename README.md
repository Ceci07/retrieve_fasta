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
**show this help message and exit**  

```
-h, --help
```
**Input multi-FASTA file containing the sequences.**  

```
-i INPUT, --input INPUT
```

**Text file containing a list of accession numbers, one per line.**  

```
-a ACCESSIONS, --accessions ACCESSIONS
```

**Output FASTA file to save the extracted sequences.**  

```
-o OUTPUT, --output OUTPUT
```

**Example**  

```
python extract_fasta.py -i input.fasta -a accessions.txt -o output.fasta
```
