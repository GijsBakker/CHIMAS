"""Not a serious example.
Usage:
  comtest.py --fastq <fastqfile> --method <method>
  comtest.py (-h | --help)
Options:
  -h, --help
  -f, --fastq
  -m, --method
  -s, --size_slice
  -l, --length
"""
from docopt import docopt
import os
from ChimeraDetector.Self_Aligned import self_aligned
from ChimeraDetector.Mapping_Method import mapping_method
from ChimeraDetector.Remove_Chimeras import remove_from_file


def main(arguments):
    file = arguments["<fastqfile>"]
    chimeras = []
    if os.path.exists(file):
        if arguments["<method>"] == "self_aligned":
            chimeras = self_aligned(file, arguments["--slice_size"], arguments["--length"])
        elif arguments["<method>"] == "mapping":
            chimeras = mapping_method(file)
        elif arguments["<method>"] == "both":
            for self_aligned_chimera in self_aligned(file, arguments["--slice_size"], arguments["--length"]):
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

