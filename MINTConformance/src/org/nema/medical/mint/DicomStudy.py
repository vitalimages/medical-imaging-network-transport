#!/usr/bin/python
# -----------------------------------------------------------------------------
# $Id$
#
# Copyright (C) 2010-2012 MINT Working group. All rights reserved.
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

import getopt
import glob
import os
import string
import sys
import traceback

from os.path import join

from org.nema.medical.mint.DCM4CHE_Dictionary import DCM4CHE_Dictionary
from org.nema.medical.mint.DicomSeries        import DicomSeries
from org.nema.medical.mint.DicomInstance      import DicomInstance
from org.nema.medical.mint.DicomHeader        import DicomHeader

# -----------------------------------------------------------------------------
# DicomStudy
# -----------------------------------------------------------------------------
class DicomStudy():
   def __init__(self, dcmDir, dataDictionary, skipPrivate=False, source=""):
   
       if not os.path.isdir(dcmDir):
          raise IOError("Directory does not exist - "+dcmDir)
          
       self.__dcmDir = dcmDir
       self.__studyInstanceUID = ""
       self.__series = {}
       self.__seriesInstanceUIDs = []
       self.__dataDictionary = dataDictionary
       self.__output = None
       self.__skipPrivate = skipPrivate
       self.__source = source
 
       self.__read()

   def tidy(self):
       if self.__output != None: self.__output.close()

   def setOutput(self, output):
       if output == "": return
       if self.__output != None: self.__output.close()
       self.__output = open(output, "w")
       
   def studyInstanceUID(self):
       return self.__studyInstanceUID

   def attributeByTag(self, tag):
       attr = None
       if self.numSeries() > 0:
          series = self.series(0)
          if series != None and series.numInstances() > 0:
             instance = series.instance(0)
             if instance != None:
                attr = instance.attributeByTag(tag)
       return attr
      
   def numSeries(self):
       return len(self.__series)
       
   def series(self, n):
       if len(self.__seriesInstanceUIDs) == 0:
          self.__seriesInstanceUIDs = self.__series.keys()
          self.__seriesInstanceUIDs.sort()
	  
       return self.__series[self.__seriesInstanceUIDs[n]]
       
   def seriesByUID(self, seriesInstanceUID):
       return self.__seriesByUID[seriesInstanceUID]
       
   def dataDictionary(self):
       return self.__dataDictionary

   def printTag(self, tag):
       val = None
       attr = self.attributeByTag(tag)
       if attr != None: val = attr.val()
       if self.__output == None:
          print val
       else:
          self.__output.write(val)

   def debug(self):
       if self.__output == None:
          print "> Study", self.studyInstanceUID()
       else:
          self.__output.write("> Study "+self.studyInstanceUID()+"\n")
       numSeries = self.numSeries()
       for n in range(0, numSeries):
           series = self.series(n)
           series.debug(self.__output)
       
   def __read(self):

       dcmNames = []
       for root, dirs, files in os.walk(self.__dcmDir, topdown=False):
           for name in files:
               filename = join(root, name)
               if DicomHeader.isDicom(filename):
                  dcmNames.append(filename)

       for dcmName in dcmNames:
           instance = DicomInstance(dcmName, self.__dataDictionary, self.__skipPrivate, self.__source)
	              
           if self.__studyInstanceUID == "":
              self.__studyInstanceUID = instance.studyInstanceUID()
           else:
              if self.__studyInstanceUID != instance.studyInstanceUID():
                 raise IOError("Study Instance UID do not match - " +
                               self.__studyInstanceUID + " != " +
                               instance.studyInstanceUID())

           seriesInstanceUID = instance.seriesInstanceUID()
           if self.__series.has_key(seriesInstanceUID):
              self.__series[seriesInstanceUID].append(instance)
           else:
              series = DicomSeries()
              series.append(instance)
              self.__series[seriesInstanceUID] = series
           
# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
def main():
    progName = sys.argv[0]
    (options, args)=getopt.getopt(sys.argv[1:], "o:s:t:ph")
               
    # ---
    # Check for output option.
    # ---
    output = ""
    for opt in options:
        if opt[0] == "-o":
           output = opt[1]
           if os.access(output, os.F_OK):
              raise IOError("File already exists - "+output)
           
    # ---
    # Check for source option.
    # ---
    source = ""
    for opt in options:
        if opt[0] == "-s":
           source = opt[1]

    # ---
    # Check for tag output option.
    # ---
    outputTag = ""
    for opt in options:
        if opt[0] == "-t":
           outputTag = opt[1]
           
    # ---
    # Check for switches.
    # ---
    skipPrivate = False
    help = False
    for opt in options:
        if opt[0] == "-h":
           help = True
        if opt[0] == "-p":
           skipPrivate = True

    try:
       if help or len(args) < 1:

          print "Usage", progName, "[options] <dicom_dir>"
          print "  -o <output>:     output filename (defaults to stdout)"
	  print "  -s <source>:     source of the DICOM file, ie. -s \"UV\""
	  print "  -t <output tag>: outputs tag (ie. -t 00020010)"
	  print "  -p:              skip private tags"
	  print "  -h:              displays usage"

          sys.exit(1)
          
       # ---
       # Read dicom.
       # ---
       dcmDir = args[0];
       dataDictionary = DCM4CHE_Dictionary()
       study = DicomStudy(dcmDir, dataDictionary, skipPrivate, source)
       study.setOutput(output)

       if outputTag != "":
          study.printTag(outputTag)
       else:
          study.debug()

       study.tidy()
       
    except Exception, exception:
       traceback.print_exception(sys.exc_info()[0], 
                                 sys.exc_info()[1],
                                 sys.exc_info()[2])
       sys.exit(1)
       
if __name__ == "__main__":
   main()
