#!/usr/bin/python
# -----------------------------------------------------------------------------
# $Id$
#
# Copyright (C) 2010 MINT Working group. All rights reserved.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Contact mint-user@googlegroups.com if any conditions of this
# licensing are not clear to you.
# -----------------------------------------------------------------------------

import base64
import getopt
import glob
import os
import sys
import traceback

from os.path import join
from struct import unpack

from org.nema.medical.mint.DataDictionary import DataDictionary
from org.nema.medical.mint.DicomAttribute import DicomAttribute
from org.nema.medical.mint.DicomStudy     import DicomStudy
from org.nema.medical.mint.MintAttribute  import MintAttribute
from org.nema.medical.mint.MintStudy      import MintStudy

# -----------------------------------------------------------------------------
# MintDicomCompare
# -----------------------------------------------------------------------------
class MintDicomCompare():
   
   def __init__(self, dicomStudy, mintStudy):
       
       self.__dicom = dicomStudy
       self.__studyInstanceUID = self.__dicom.studyInstanceUID()
       self.__mint = mintStudy
       self.__offsets = {}          
       self.__count = 0
       self.__verbose = False
       self.__inlineBinaryTagsCompared = 0
       self.__binaryTagsCompared = 0
       self.__textTagsCompared = 0
       self.__bytesCompared = 0
       self.__itemsCompared = 0
       self.__lazy= False
       self.__output = None

       self.__readOffsets()

   def setVerbose(self, verbose):
       self.__verbose = verbose
       
   def setLazy(self, lazy):
       self.__lazy = lazy
       
   def setOutput(self, output):
       if output != "": 
          self.__output = open(output, "w")
       
   def compare(self):       
       dicm = self.__dicom
       mint = self.__mint
              
       self.__check("Number of instances",
                    dicm.numInstances(), 
                    mint.numInstances())
       
       numInstances = dicm.numInstances()
       instancesCompared = 0
       for n in range(0, numInstances):
           instance = dicm.instances(n)
           self.__compareInstances(instance, mint)
           instancesCompared += 1

       # ---
       # Print out stats if verbose.
       # ---     
       if self.__verbose:
          if self.__output == None:
             print "%10d instance(s) compared." % (instancesCompared)
             print "%10d text tag(s) compared." % (self.__textTagsCompared)
             print "%10d items(s) compared." % (self.__itemsCompared)
             print "%10d inline binary tag(s) compared." % (self.__inlineBinaryTagsCompared)
             print "%10d binary tag(s) compared." % (self.__binaryTagsCompared)
             print "%10d byte(s) compared." % (self.__bytesCompared)          
          else:
             self.__output.write("%10d instance(s) compared.\n" % (instancesCompared))
             self.__output.write("%10d text tag(s) compared.\n" % (self.__textTagsCompared))
             self.__output.write("%10d items(s) compared.\n" % (self.__itemsCompared))
             self.__output.write("%10d inline binary tag(s) compared.\n" % (self.__inlineBinaryTagsCompared))
             self.__output.write("%10d binary tag(s) compared.\n" % (self.__binaryTagsCompared))
             self.__output.write("%10d byte(s) compared.\n" % (self.__bytesCompared))

       # ---
       # Always print differences.
       # ---
       if self.__count != 0:
          if self.__output == None:
             print "%10d difference(s) found." % (self.__count)
          else:
             self.__output.write("%10d difference(s) found.\n" % (self.__count))
          
       self.__dicom.tidy()
       return self.__count

   def __readOffsets(self):
       
       # ---
       # TODO: 
       # ---
       # offsets = os.path.join(self.__binary, "offsets.dat")
       # if offsets in self.__binaryitems: self.__binaryitems.remove(offsets)       
       # if os.path.isfile(offsets):
       #    table = open(offsets, "r")
       #    line = table.readline()
       #    while line != "":
       #       tokens = line.split()
       #       assert len(tokens) == 2
       #       self.__offsets[tokens[0]] = tokens[1]
       #       line = table.readline()
       #    table.close()
       
       pass

   def __compareInstances(self, instance, mint): 

       # ---
       # Check Study Instance ID.
       # ---
       self.__check("UI",
                    instance.studyInstanceUID(), 
                    mint.studyInstanceUID())
                  
       # ---
       # Check Series Instance ID.
       # ---
       mintSeriesInstanceUID = "None"
       mintSeries = mint.seriesByUID(instance.seriesInstanceUID())
       if mintSeries != None:
          mintSeriesInstanceUID = mintSeries.seriesInstanceUID()
       
       self.__check("UI",
                    instance.seriesInstanceUID(),
                    mintSeriesInstanceUID,
                    instance.seriesInstanceUID())

       # ---
       # Check SOP Instance ID.
       # ---
       mintSopInstanceUID = "None"
       mintInstance = mint.instanceByUID(instance.sopInstanceUID())
       if mintInstance != None:
          mintSopInstanceUID = mintInstance.sopInstanceUID()
       
       self.__check("UI",
                    instance.sopInstanceUID(),
                    mintSopInstanceUID,
                    instance.seriesInstanceUID(),
                    instance.sopInstanceUID())                  

       # ---
       # Check tags.
       # ---
       numAttributes = instance.numAttributes()       
       for n in range(0, numAttributes):
           tag = instance.tag(n)
           self.__checkTag(instance, mint, tag)
                                  
   def __check(self, msg, obj1, obj2, series="", sop=""):
       if obj1 != obj2:
          self.__count += 1
          print "- Study Instance UID", self.__studyInstanceUID
          if series != "":
             print " - Series Instance UID", series
             if sop != "":
                print "  - SOP Instance UID", sop
          print "+++", msg, ":", obj1, "!=", obj2
       
   def __checkTag(self, instance, mint, tag):

       # ---
       # Optional and deprecated Group Length tags are not included so we don't need to look for them,
       # ---
       if tag[4:8] == "0000": return
       
       attr = mint.find(tag, instance.seriesInstanceUID(), instance.sopInstanceUID())
       if attr == None:
          self.__check("Data Element", 
                       tag, 
                       "None", 
                       instance.seriesInstanceUID(), 
                       instance.sopInstanceUID())
       else:
          dicomAttr = instance.attributeByTag(tag)
          self.__checkAttribute(dicomAttr, attr, instance.seriesInstanceUID(), instance.sopInstanceUID())
             
   def __checkAttribute(self, dicomAttr, attr, seriesInstanceUID, sopInstanceUID):
      
       # ---
       # The MINT study may have a more explicit VR for private tags so promote
       # original DICOM tag if necessary.
       # ---
       if dicomAttr.vr() == "UN" and attr.vr() != "UN":
          dicomAttr.promote(attr.vr())
      
       if dicomAttr.vr() != "":
          self.__check(dicomAttr.tag()+" VR",
                       dicomAttr.vr(),
                       attr.vr(),
                       seriesInstanceUID, 
                       sopInstanceUID)
       
       # ---
       # Check binary items and values.
       # ---
       if dicomAttr.isBinary():
          self.__checkBinary(dicomAttr, attr, seriesInstanceUID, sopInstanceUID)
       else:
          self.__check(dicomAttr.tag()+" Value",
                       dicomAttr.val(),
                       attr.val(),
                       seriesInstanceUID, 
                       sopInstanceUID)
          self.__textTagsCompared += 1
          
       # ---
       # Check number of items.
       # ---
       numItems1 = dicomAttr.numItems()
       numItems2 = attr.numItems()
       self.__check(dicomAttr.tag()+" Number of items",
                    numItems1,
                    numItems2)
          
       for i in range(0, numItems1):
          
           # ---
           # Check items.
           # ---
           attributeList = dicomAttr.item(i)
           numAttributes1 = dicomAttr.numItemAttributes(i)
           numAttributes2 = attr.numItemAttributes(i)
           self.__check(dicomAttr.tag()+" number of item attributes",
                        numAttributes1,
                        numAttributes2)

           # ---
           # Check item attributes.
           # ---
           for j in range(0, numAttributes1):
               itemAttribute1 = dicomAttr.itemAttribute(i, j)
               itemAttribute2 = attr.itemAttribute(i, j)
               self.__checkAttribute(itemAttribute1, itemAttribute2, seriesInstanceUID, sopInstanceUID)
           
           self.__itemsCompared += 1
           
   def __checkBinary(self, dicomAttr, attr, seriesInstanceUID, sopInstanceUID):

       if dicomAttr.dat() == "":
          self.__checkInlineBinary(dicomAttr, attr, seriesInstanceUID, sopInstanceUID)
          return

       if self.__lazy: return
       
       # ---
       # Check for DICOM binary item
       # ---
       dat1 = dicomAttr.dat()
       if not os.access(dat1, os.F_OK):
          self.__count += 1
          print "File not found", ":", dat1
          return

       # ---
       # Check for MINT binary item.
       # ---
       if attr.bid() == None:
          self.__check(dicomAttr.tag()+" missing binary",
                       dat1,
                       "None",
                       seriesInstanceUID, 
                       sopInstanceUID)
          return

       # ---
       # TODO: Check to see if this is single file or multi-file binary.
       # ---
       # if len(self.__offsets) > 0:
       #    dat2 = self.__binaryitems[0]
       
       # ---
       # Check binary item byte for byte.
       # ---
       bid1 = open(dat1, "rb")
       bid2 = self.__mint.open(attr.bid())
       
       # ---
       # TODO: Position the MINT binary file pointer.
       # ---
       # boffset = 0
       # if len(self.__offsets):
       #    boffset = int(self.__offsets[attr.bid()])
       # bid2.seek(boffset)
       
       # ---
       # Read in a block.
       # ---
       bufsize = 1024
       block = 0
       buf1 = bid1.read(bufsize)
       buf2 = bid2.read(bufsize)
          
       bytes1 = unpack('B'*len(buf1), buf1)
       bytes2 = unpack('B'*len(buf2), buf2)
       n = len(bytes1)
       while n > 0:        

          # ---
          # Loop through block.
          # ---
          diff = False
          for i in range(0, n):              
              if bytes1[i] != bytes2[i]:
                 self.__check(dicomAttr.tag()+" byte "+str(block*bufsize+i),
                              hex(bytes1[i]),
                              hex(bytes2[i]),
                              seriesInstanceUID, 
                              sopInstanceUID)
                 diff = True
                 break
                    
              self.__bytesCompared += 1

          # ---
          # Skip to end if difference was found.
          # ---
          if diff:
             n = -1
          else:
             buf1 = bid1.read(bufsize)
             buf2 = bid2.read(len(buf1))

             bytes1 = unpack('B'*len(buf1), buf1)
             bytes2 = unpack('B'*len(buf2), buf2)
             n = len(bytes1)
             block += 1
             
       bid1.close()
       bid2.close()
       self.__binaryTagsCompared += 1

   def __checkInlineBinary(self, dicomAttr, attr, seriesInstanceUID, sopInstanceUID):

       self.__check(dicomAttr.tag()+" <Binary Data>",
                    dicomAttr.val(),
                    attr.bytes(),
                    seriesInstanceUID, 
                    sopInstanceUID)

       self.__inlineBinaryTagsCompared += 1
 
# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
def main():
   
    # ---
    # Get options.
    # ---
    progName = os.path.basename(sys.argv[0])
    (options, args)=getopt.getopt(sys.argv[1:], "d:o:p:vlh")

    # ---
    # Check for data dictionary.
    # ---
    dictionaryURL = DataDictionary.DCM4CHE_URL
    for opt in options:
        if opt[0] == "-d":
           dictionaryURL = opt[1]
           
    # ---
    # Check for output option.
    # ---
    output = ""
    for opt in options:
        if opt[0] == "-o":
           output = opt[1]
           
    # ---
    # Check for port option.
    # ---
    port = "8080"
    for opt in options:
        if opt[0] == "-p":
           port = opt[1]
           
    # ---
    # Check for verbose option.
    # ---
    verbose = False
    for opt in options:
        if opt[0] == "-v":
           verbose = True
           
    # ---
    # Check for lazy option.
    # ---
    lazy = False
    for opt in options:
        if opt[0] == "-l":
           lazy = True
           
    # ---
    # Check for help option.
    # ---
    help = False
    for opt in options:
        if opt[0] == "-h":
           help = True
           
    try:
       # ---
       # Check usage.
       # ---
       argc = len(args)
       if help or argc < 3:
          print "Usage:", progName, "[options] <dicom_study_dir> <hostname> <uuid>"
          print "  -d <data_dictionary_url>: defaults to DCM4CHE"
          print "  -o <output>:              output filename (defaults to stdout)"
          print "  -p <port>:                defaults to 8080"
          print "  -v:                       verbose"
          print "  -l:                       lazy check (skips binary content)"
          print "  -h:                       displays usage"
          sys.exit(1)
          
       # ---
       # Read MINT metadata.
       # ---
       dicomStudyDir = args[0];
       hostname      = args[1];
       uuid          = args[2];
       
       dicomStudy = DicomStudy(dicomStudyDir, dictionaryURL)
       mintStudy  = MintStudy(hostname, port, uuid)  
       
       studies = MintDicomCompare(dicomStudy, mintStudy)
       studies.setVerbose(verbose)
       studies.setLazy(lazy)
       studies.setOutput(output)

       return studies.compare()
       
    except Exception, exception:
       traceback.print_exception(sys.exc_info()[0], 
                                 sys.exc_info()[1],
                                 sys.exc_info()[2])
       sys.exit(1)
       
if __name__ == "__main__":
   main()
