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

from org.nema.medical.mint.DataDictionaryElement import DataDictionaryElement
from org.nema.medical.mint.MintAttribute         import MintAttribute
from org.nema.medical.mint.MintInstance          import MintInstance
from org.nema.medical.mint.XmlNode               import XmlNode

# -----------------------------------------------------------------------------
# MintSeries
# -----------------------------------------------------------------------------
class MintSeries():
   
   def __init__(self, root):
       self.__instanceCount = ""
       self.__attributes = {}
       self.__tags = []
       self.__normalizedInstanceAttributes = {}
       self.__normalizedTags = []
       self.__instances = {}
       self.__sopInstanceUIDs = []
       self.__read(root)
       
   def seriesInstanceUID(self): 
       return self.__seriesInstanceUID;
       
   def instanceCount(self): 
       return self.__instanceCount;
       
   def numAttributes(self):
       return len(self.__tags)
          
   def attribute(self, n):
       """
       Returns a MintAttribute at index n.
       """
       tag = self.__tags[n]
       return self.__attributes[tag]

   def attributeByTag(self, tag):
       """
       Returns a MintAttribute if tag is found, otherwise None.
       """
       if self.__attributes.has_key(tag):
          return self.__attributes[tag]
       else:
          return None

   def numNormalizedInstanceAttributes(self):
       return len(self.__normalizedTags)
          
   def normalizedInstanceAttribute(self, n):
       """
       Returns a MintAttribute at index n.
       """
       tag = self.__normalizedTags[n]
       return self.__normalizedInstanceAttributes[tag]

   def normalizedInstanceAttributeByTag(self, tag):
       """
       Returns a MintAttribute if tag is found, otherwise None.
       """
       if self.__normalizedInstanceAttributes.has_key(tag):
          return self.__normalizedInstanceAttributes[tag]
       else:
          return None

   def numInstances(self):
       return len(self.__sopInstanceUIDs)

   def instance(self, n):
       """
       Returns a MintInstance at index n.
       """
       sopInstanceUID = self.__sopInstanceUIDs[n]
       return self.__instances[sopInstanceUID]

   def instanceByUID(self, uid):
       """
       Returns a MintInstance if UID is found, otherwise None.
       """
       if self.__instances.has_key(uid):
          return self.__instances[uid]
       else:
          return None

   def find(self, tag, sopInstanceUID):
       attr = self.attributeByTag(tag)
       if attr == None:
          attr = self.normalizedInstanceAttributeByTag(tag)
          if attr == None:
             instance = self.instanceByUID(sopInstanceUID)
             if instance != None:
                attr = instance.find(tag)           
       return attr
       
   def debug(self, indent=""):
       print indent+"- series seriesInstanceUID", self.__seriesInstanceUID, "instanceCount", self.__instanceCount
       indent += " "
       print indent+"- attributes"
       indent += " "
       numAttributes = self.numAttributes()
       for n in range(0, numAttributes):
           self.attribute(n).debug(indent)
       indent = indent[0:-1]
       print indent+"- attributes"

       print indent+"- normalizedInstanceAttributes"
       indent += " "
       numNormalizedInstanceAttributes = self.numNormalizedInstanceAttributes()
       for n in range(0, numNormalizedInstanceAttributes):
           self.normalizedInstanceAttribute(n).debug(indent)
       indent = indent[0:-1]
       print indent+"- normalizedInstanceAttributes"
          
       print indent+"- instances"
       indent += " "
       numInstances = self.numInstances()
       for n in range(0, numInstances):
           self.instance(n).debug(indent) 
       indent = indent[0:-1]
       print indent+"- instances"
       
   def __read(self, root):
       self.__seriesInstanceUID = root.attributeWithName("seriesInstanceUID")
       self.__instanceCount = root.attributeWithName("instanceCount")

       # ---
       # Read Attributes
       # ---
       node = root.childWithName("attributes")
       if node != None:
          nodes = node.childrenWithName("attr")
          for node in nodes:
              attb = MintAttribute(node)
              self.__attributes[attb.tag()] = attb
          self.__tags = self.__attributes.keys()
          self.__tags.sort()

       # ---
       # Read Normalized Instance Attributes
       # ---
       node = root.childWithName("normalizedInstanceAttributes")
       if node != None:
          nodes = node.childrenWithName("attr")
          for node in nodes:
              attb = MintAttribute(node)
              self.__normalizedInstanceAttributes[attb.tag()] = attb
          self.__normalizedTags = self.__normalizedInstanceAttributes.keys()
          self.__normalizedTags.sort()
               
       # ---
       # Read Instances
       # ---
       node = root.childWithName("instances")
       if node != None:
          nodes = node.childrenWithName("instance")
          for node in nodes:
              instance = MintInstance(node)
              self.__instances[instance.sopInstanceUID()] = instance 
       self.__sopInstanceUIDs = self.__instances.keys()
       self.__sopInstanceUIDs.sort()
