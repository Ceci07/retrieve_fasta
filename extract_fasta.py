import argparse
import time
from Bio import SeqIO

# Arguments
parser = argparse.ArgumentParser(description="Extract FASTA sequences based on a list of accessions.")
parser.add_argument("-i", "--input", required=True, help="Input multi-FASTA file")
parser.add_argument("-a", "--accessions", required=True, help="File containing list of accessions")
parser.add_argument("-o", "--output", required=True, help="Output FASTA file for extracted sequences")

# Parse the arguments
args = parser.parse_args()

start_time = time.time()

# Variables
fasta_file = args.input
accession_file = args.accessions
output_file = args.output

# Load the list of accessions
with open(accession_file) as f:
    accessions = set(line.strip() for line in f)

# Filter sequences
retrieved_count = 0
with open(output_file, "w") as out:
    for record in SeqIO.parse(fasta_file, "fasta"):
        if any(acc in record.id for acc in accessions):
            SeqIO.write(record, out, "fasta")
            retrieved_count += 1

# Measure the end time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Extracted sequences saved to {output_file}")
print(f"Total sequences retrieved: {retrieved_count}")
print(f"Time taken: {elapsed_time:.2f} seconds")
