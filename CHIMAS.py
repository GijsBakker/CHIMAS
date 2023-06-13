#!/usr/bin/python3

"""
CHIMAS.py: Is usa bundle of dna analysis tools
"""

usage = """
CHIMAS.py: CHIMAS.py is used to ..... TODO

Usage:
    CHIMAS.py <fastq_file> -k <kmer_size> [-r <dpi>] [-s <self>] [-d <dot_size>] [--graphics] [--paf_file=<paf_file>] 
    [--output_file=<output_file>]
    CHIMAS.py (-h | --help | --version)

Options:
    -k <kmer_size>  Specify the size of the k-mer used in the genome dot plot
    -r <dpi>        Specify the DPI of the genome dot plot [default: 600]
    -d <dot_size>   Specify the dot size to be used in the genome dot plot [default: 2]
    
    --paf_file=<paf_file>           Path to the PAF data set used by SLEAP.
    --output_file=<output_file>     Path to the output Fasta data set created by SLEAP. 
                                    (default: {input_name}_contigs.fasta)
    --graphics                      Display SLEAP information using the graphics.py script. [default: False]
    
Author: Gijs Bakker, Ijsbrand Pool, Lisan Eisinga
Version: 1.0
Date of Completion: 13-06-2023
"""

__author__ = "Gijs Bakker"
__version__ = 1.0

import os
from docopt import docopt
from VVODKA_dir import VVODKA
from SLAEP import assembly


def main(args):
    kmer_size = int(args['-k'])
    on_self = "Y"
    dpi = int(args['-r'])
    dot_size = int(args['-d'])

    fastq_file = args["<fastq_file>"]
    output_file = args["--output_file"]
    if not output_file:
        base_name = os.path.splitext(fastq_file)[0]
        output_file = f"{base_name}_contigs.fasta"

    assembly.main(args)
    print("Done Assembly")
    VVODKA.vvodka(kmer_size, [output_file], on_self, dpi, dot_size, pre_extension="")


if __name__ == '__main__':
    args = docopt(usage)
    main(args)
