#  CHIMAS (Chimera Detector and Long Read Assembler with Dotplot Visualization)

[![DOI](https://joss.theoj.org/papers/DOI/badge.svg)](https://doi.org/DOI)# FILL IN

## Summary

The CHIMAS (Chimera Detector and Long Read Assembler with Dotplot Visualization) software created consists of the ChimeraDetector, SLAEP assembler, and VVODKA. Chimera detector finds and removes chimeric sequences in DNA, the SLAEP assembler then assembles the FastQ file for educational purposes, and the VVODKA is a complete genome dot plotting tool that can plot the dot-plot of the reads. These tools aim to identify chimeric sequences, teach students how genome assemblies work, and view the results in a dot plot. The CHIMAS software has many features, including creating a PAF data set, visualization of the FastQ data set, and several options regarding the chimera and dot-plot process. The critical functions of the tool are different for each aspect. The ChimeraDetector functions to specifically find chimeras in the FastQ data set and remove these, SLAEP aims to teach the student how a genome assembly works, and VVODKA specializes in the creation of an accurate dot-plot of the reads in the data set.

## Background
Currently, there are not many chimera detectors that can detect self-chimeras. This changes with the ChimeraDetector. After these chimeras have been removed, the data set can be assembled. However, many assemblers are challenging to understand, need proper documentation, and are very difficult to understand when looking at the code. With SLAEP, this problem is solved. SLAEP makes the process of understanding assembly easy. Lastly, VVODKA makes the visualization of the reads with a dot plot easy, fast, and efficient, unlike currently available tools. These tools were developed for multiple reasons, the key reasons being, Educational purposes and efficiency.

When looking at tools currently out there, it becomes clear that no tool has the same capabilities and features as the CHIMAS software making it unique in bioinformatics.

## Key Features

The CHIMAS software consists of the ChimeraDetector, the key features are that it can detect self-chimeras, can be used with and without a PAF file, and has an understandable Docopt interface. SLAEP's key features include its ability to generate a PAF file if MiniMap2 is available, create an overlap graph from this data, and be adjustable for students with unit tests so the output can always be checked. SLAEP also has visualization options for the FastQ data set. VVODKA's key features are that it is fast, efficient, and understandable, the dot plots are accurate and easy to understand, and the code is adequately documented.

## Installation

In order to install the software, please use the following statement in the command line: ```git clone REPO```. After this, please install the requirements from the requirements.txt file with the following statement: ```pip install -r requirements.txt```. Now the CHIMAS software is ready for use!

## Usage

The tool can be used as one, or the separate tools can be used individually. In order to do that, use the following statements:
* CHIMAS: ```python CHIMAS.py -f -s -l -k enz```

* ChimeraDetector: ``` python ChimeraDetector.py -f [FastQ] -m [Method] -s [Slice size] -l [length]```

* SLAEP:```python Assembly.py <fastq_file> [--paf_file=<paf_file>] [--outputS_file=<output_file>] [--graphics]```

* VVODKA:```python VVODKA.py -k <kmer_size> [-r <dpi>] [-s <self>] [-d <dot_size>] <files>```

The tools can be run with these statements on the correct data sets.

## Documentation

The software can be found in its complete set on REPO.

## Examples

The CHIMAS software can be used on FastQ data sets created by the Oxford nanopore MinION. Since this is its first publication, the software has yet to be applied to use cases.

Provide concrete examples or use cases where your software has been applied. Show how it solves specific problems and provides benefits.

## Evaluation

The tool runs quickly. It can be more efficient, especially the ChimeraDetector and the SLAEP assembler. However, it is memory efficient.

Discuss the evaluation of your software, including benchmarking, performance analysis, or comparisons with existing solutions. Provide insights into its effectiveness and efficiency.

## Limitations

The CHIMAS software has its limitation, as every tool does. The ChimeraDetector functions only with FastQ data set in a specific format, SLAEP requires a PAF file, and this limits its overlap graph, which can cause sub-optimal assemblies and VVODKA: LIMITATIONS HERE

Highlight any known limitations or areas where further improvements are required. Discuss potential future directions for development.

## Conclusion

The critical contributions of the CHIMAS software are that now self chimeras can be detected, students can learn about genome assembly and GIJS 

Summarize the critical contributions of your software and its potential impact in the field. Discuss any plans or ongoing developments.

## Acknowledgements

For the creation of the software, we, the authors, would like to acknowledge Thomas Hackl for the contribution of the data and his invaluable assistance when issues arise.

## References

List any relevant references, papers, or resources associated with your software.

## License

The license for the software is free to use, and anyone can download the tool and use it as they wish.

## How to Cite

To cite the software, please use the following site: CITE

## Contributing

This software is finished as it stands. However, contributions can be made by submitting bug reports to the mail addresses listed below. Any ideas for improvement are always welcome.

## Contact

For contact with the authors or questions about the software, please use the following email addresses:
 * i.j.a.pool@st.hanze.nl
 * j.l.a.eisinga@st.hanze.nl
 * g.bakker@st.hanze.nl
