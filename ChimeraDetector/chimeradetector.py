#!/usr/bin/env python3
"""
Usage:
  chimeradetector.py <fastqfile> <method> [--size_slice=<slice_size>] [--length=<length>]
  chimeradetector.py (-h | --help)
Options:
  -h, --help
  --size_slice=<slice_size>
  --length=<length>
"""
from docopt import docopt
import os
from ChimeraDetector.Self_Aligned import self_aligned
from ChimeraDetector.Mapping_Method import mapping_method
from ChimeraDetector.Remove_Chimeras import remove_from_file


def main(arguments):
    file = arguments["<fastq_file>"]
    chimeras = []
    if os.path.exists(file):
        if arguments["<method>"] == "self_aligned":
            chimeras = self_aligned(file, arguments["--size_slice"], arguments["--length"])
        elif arguments["<method>"] == "mapping":
            chimeras = mapping_method(file)
        elif arguments["<method>"] == "both":
            for self_aligned_chimera in self_aligned(file, arguments["--size_slice"], arguments["--length"]):
                chimeras.append(self_aligned_chimera)
            for mapping_chimera in mapping_method(file):
                if mapping_chimera not in chimeras:
                    chimeras.append(mapping_chimera)

        print(len(chimeras), "chimeras found.")

        if len(chimeras) >= 1:
            remove_from_file(chimeras, file)

        print("Self chimeras removed from file", file)
    else:
        print("File not found! The file or file path given does not exist.")


if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
    main(arguments)

