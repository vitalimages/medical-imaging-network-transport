

# Setting up your environment #

The MINT Conformance tools require [Python2.7](http://www.python.org) or later. Currently the tools are run directly from the MINTConformance package in a subversion trunk (installation scripts will be provided later). In order to run the tools, the **PYTHONPATH** environment variable must be set to point to the python source code. The python application must also be in your **PATH**. For example, if **MC\_HOME** is the path to your subversion trunk, then set your PYTHONPATH as follows:

**Unix**
```
PATH=${PATH}:/usr/local/bin/python/bin
PYTHONPATH=$MC_HOME/MINTConformance/src
```

**Windows**
```
set PATH=%PATH%;C:\Python2.7.1
set PYTHONPATH=%MC_HOME%\MINTConformance\src
```


---


# MINTConformance Tools #

The MINTConformance package was developed based on the draft [MINT Conformance Test](http://groups.google.com/group/mint-user/files) Power Point specification located in the [mint-user Google Group](http://groups.google.com). It currently consists of three tools.

## Mint Study Compare ##

The [MintStudyCompare.py](http://code.google.com/p/medical-imaging-network-transport/source/browse/trunk/MINTConformance/src/org/nema/medical/mint/MintStudyCompare.py) tool is a python application that compares a MINT study on the file system to a MINT study on the MINTServer. This is useful for regression testing the MINTServer against a previous golden copy. It compares the metadata.xml and the binary items on the filesystem to the study on the MINTServer.

Launch the tool by using the _python_ command to parse the file. This tool should run either in a Unix or Windows command shell.

Running the tool with no arguments displays the usage:

```
> python %PYTHONPATH%\org\nema\medical\mint\MintStudyCompare.py
Usage: MintStudyCompare.py [options] <mint_study_dir> <hostname> <uuid>
  -o <output>: output filename (defaults to stdout)
  -p <port>:   defaults to 8080
  -v:          verbose
  -l:          lazy check (skips binary content)
  -h:          displays usage
```

The output option is for specifying an output file to capture the summary results (useful for automated testing). The verbose flag turns on output to show how many tags and bytes were compared. Otherwise nothing is displayed when there are no differences. You can optionally skip checking the binary to save time when debugging.

```
> cd $MINT_HOME\testdata\MINT\20_phase\DICOM
> python %PYTHONPATH%\org\nema\medical\mint\MintStudyCompare.py -v . localhost 02e47f6a-6f5c-4a50-887a-94d0802198b7
        12 study attribute(s) compared.
         2 series compared.
        14 series attribute(s) compared.
       112 normalized instance attribute(s) compared.
         4 instance(s) compared.
        32 instance attribute(s) compared.
         0 sequence items(s) compared.
         0 sequence attributes(s) compared.
         4 inline binary item(s) compared.
         4 binary item(s) compared.
         0 offset(s) compared.
   2097152 byte(s) compared.
```

## Mint Dicom Compare ##

The [MintDicomCompare.py](http://code.google.com/p/medical-imaging-network-transport/source/browse/trunk/MINTConformance/src/org/nema/medical/mint/MintDicomCompare.py) tool is a python application that compares a DICOM study on the file system to a MINT study on the MINTServer by parsing the data elements in the DICOM and comparing them to the metadata and binary items in the MINT study.

There are some subtle differences between the DICOM and MINT representations if you are using another tool for comparison. Some binary VRs are represented as text in MINT for clarity ("SS", "US", "SL", "UL", "FL", "FD", "OF", "AT") so the values will not compare directly to the DICOM binaries. Arrays of these primitive types are represented as strings with the values separated by a "\" delimiter (ie. 208.55017\166.19896). Note that the precision for floating point representations is set to 6.

Launch the tool by using the _python_ command to parse the file. This tool should run either in a Unix or Windows command shell.

Running the tool with no arguments displays the usage:

```
> python %PYTHONPATH%\org\nema\medical\mint\MintDicomCompare.py
Usage: MintDicomCompare.py [options] <dicom_study_dir> <hostname> <uuid>
  -o <output>: output filename (defaults to stdout)
  -p <port>:   defaults to 8080
  -v:          verbose
  -l:          lazy check (skips binary content)
  -h:          displays usage
```

The data dictionary is required for looking up implicit VRs based on the group-element tag. The output option is for specifying an output file to capture the summary results (useful for automated testing). The verbose flag turns on output to show how many tags and bytes were compared. Otherwise nothing is displayed when there are no differences. You can optionally skip checking the binary to save time when debugging.

```
> cd $MINT_HOME\testdata\MINT\20_phase\DICOM
> python %PYTHONPATH%\org\nema\medical\mint\MintDicomCompare.py -v . localhost 02e47f6a-6f5c-4a50-887a-94d0802198b7
         2 series compared.
         4 instance(s) compared.
       324 text tag(s) compared.
         0 floating point tag(s) compared.
         0 items(s) compared.
         4 inline binary tag(s) compared.
         4 binary tag(s) compared.
   2097152 byte(s) compared.
```

## Dicom Study Compare ##

The [DicomStudyCompare.py](http://code.google.com/p/medical-imaging-network-transport/source/browse/trunk/MINTConformance/src/org/nema/medical/mint/DicomStudyCompare.py) tool is a python application that compares an original DICOM study on the file system to an exported DICOM study on the file system (by running MINT2DICOM on a MINTServer study). It parses the data elements in the original DICOM and compares them to the data elements in the exported DICOM.

There are some subtle differences between the original DICOM and exported MINT DICOM if you are using another tool for comparison. Group length tags are stripped out of MINT studies so they will not be present in the exported DICOM. Also Sequence data elements (VR of SQ) have undefined lengths (-1) in exported studies instead of an explicit lengths.

Launch the tool by using the _python_ command to parse the file. This tool should run either in a Unix or Windows command shell.

Running the tool with no arguments displays the usage:

```
> python %PYTHONPATH%\org\nema\medical\mint\DicomStudyCompare.py
Usage: DicomStudyCompare.py [options] <ref_dicom_study_dir> <new_dicom_study_dir
>
  -o <output>:  output filename (defaults to stdout)
  -x <exclude>: list of tags to exclude, ie. "08590030,600001nn"
  -v:           verbose
  -l:           lazy check (skips binary content)
  -w:           show warnings
  -h:           displays usage
```

The data dictionary is required for looking up implicit VRs based on the group-element tag. The output option is for specifying an output file to capture the summary results (useful for automated testing). The verbose flag turns on output to show how many tags and bytes were compared. Otherwise nothing is displayed when there are no differences. You can optionally skip checking the binary to save time when debugging.

There is an additional option for excluding tags in case you identify a difference but discover it is not an error (for example dcm4chee might implicitly add additional attribution that you might want to ignore).

By default, non-alphanumeric padding characters at the right end of a string (such as <sup>^</sup> or \\\) are treated as warnings as opposed to differences. To see these differences use the -w option.

```
> cd $MINT_HOME\testdata\MINT\20_phase\DICOM
> python %PYTHONPATH%\org\nema\medical\mint\DicomStudyCompare.py -vw original-20_phase exported-20_phase
         2 series compared.
         4 instance(s) compared.
       328 text tag(s) compared.
         0 items(s) compared.
         4 inline binary tag(s) compared.
         4 binary tag(s) compared.
   2097152 byte(s) compared.
         0 excluded tag(s).
         0 warning(s) found.
```

To see all the differences the application should be run twice, switching the command line arguments. This will find all the tags that may be present in one study but not the other.

```
> cd $MINT_HOME\testdata\MINT\20_phase\DICOM
> python %PYTHONPATH%\org\nema\medical\mint\DicomStudyCompare.py -vw exported-20_phase original-20_phase
         2 series compared.
         4 instance(s) compared.
       328 text tag(s) compared.
         0 items(s) compared.
         4 inline binary tag(s) compared.
         4 binary tag(s) compared.
   2097152 byte(s) compared.
         0 excluded tag(s).
         0 warning(s) found.
```


---


# Status #

**Issues Discovered**

  * MINT only stores VRs of OB, OW, and UN as binary.
  * MINT was stripping Part 10 private header tags (corrected)
  * MINT strips group length tags (except for 0002000)
  * Some external DICOM applications strip padding from text tags
  * MINT does not reflect float types with exact precision
  * MINT2DICOM stores SQ lengths as undefined (-1)
  * MINT2DICOM sometimes adds additional tags to SOP Instances
  * MINT2DICOM was removing items from sequence records (corrected)
  * MINT Data Dictionary does not match DCM4CHEE Data Dictionary (corrected)

**Completed Tasks**

  * Resolve binary/text differences between DICOM and MINT
  * Revisit Part 10 header differences between DICOM and MINT
  * Parse sequencing data elements (SQ) in MintStudy
  * Compare sequencing data elements (SQ) between MINT studies
  * Parse sequencing data elements (SQ) in DICOM
  * Detect endianness, explicit VRs
  * Compare sequencing data elements (SQ) between DICOM and MINT
  * Use data dictionary to find VRs
  * Store binary in temp files for large DICOMs
  * Provide support for inline binary
  * Provide support for bulk binary
  * Read DCM4CHE data dictionary from URL
  * Added warning option to DicomStudyCompare.
  * Added logic for comparing floats within an epsilon.
  * Created DicomSeries class that is a collection of DicomInstances.
  * Added output option to DataDictionary to support integration testing.
  * Uses MINT Dictionary when comparing studies on a MINTServer and DCM4CHE when comparing studies on the file system.
  * Fixed DicomTransfer to use ExplicitVR encoding for compressed images.
  * Added logic to DicomStudyCompare to handle mixed endian comparisons.

**To Do**

  * Provide support for undefined lengths for OW, OB, and UN tags.
  * Consider cases for multiple VRs
  * Comparisons before and after DICOM2MINT update
  * Support multi-frame DICOM