# CHIMAS

## Dependencies VVODKA
* Python 3.9
* matplotlib 3.7.0
* docopt 0.6.2
* pyfastx 0.9.1

You can install these dependencies using pip:

```
pip install matplotlib==3.7.0
pip install docopt==0.6.2
pip install pyfastx==0.9.1
```

## Usage VVODKA
To generate a genome dot plot using VVODKA, you need to provide the following information:
```
Usage:
    VVODKA.py -k <kmer_size> [-r <dpi>] [-s <self>] [-d <dot_size>] <files>...
    VVODKA.py (-h | --help | --version)
    
Options:
    -k <kmer_size>  Specify the size of the k-mer
    -r <dpi>        Specify the DPI [default: 600]
    -s <self>       Specify if files should be plotted against themselves, use Y
                    to plot against itself or N to not plot against itself [default: Y]
    -d <dot_size>   Specify the dot size to be used in the dot plot [default: 2]
    <files>...      Specify the files which are plotted against each other
```

For example, to generate a genome dot plot with a k-mer size of 13, a dpi of 300, and plot the file Cflag_c131.fna 
against itself, use the following command:
```
VVODKA.py -k 13 ../../data/PaperData/Cflag_c131.fna
```
