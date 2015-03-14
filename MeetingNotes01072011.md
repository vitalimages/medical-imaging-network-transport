# Attendees #
  * Tim Dawson
  * Dan Chaffee
  * Gorkem Sevinc
  * Chris Hafey

# Progress Since Last Meeting #
  * Chris Hafey
    * Believes there is a WG27 meeting this month and needs to get that on the schedule and see if we can move MINT forward that
  * Tim Dawson
    * Worked with Uli on non DICOM support.  Got a full end to end test going for this
  * Gorkem Sevinc
    * Built a GUI Admin Tool in SWING.
    * Would like to build the same utility to do MINT2DICOM
  * Dan Chaffee
    * No progress

# Notes #
  * Discussion on first experience
http://code.google.com/p/medical-imaging-network-transport/wiki/FirstExperience?ts=1294411684&updated=FirstExperience

# Decisions #

# New Actions #
  * Send out email to list to propose meeting to brainstorm MINT 2011 roadmap (Chris)

# Old Actions #
  * Modify metadata version number as decided above (Dan Chaffee)
  * Review Gorkem's setup document and provide feedback about what needs to be done for version 1.0 "get started" doc (all)
  * Design "First Experience" and send to mail list (Gorkem)
  * Use cases for proprietary data (Jim)
  * Use cases for de-id (Jim)
  * Update clear canvas to support Multi-frame MINT (Tim Culp)
  * Update conformance test to support Multi-frame (Tim Culp)
  * Recipe/cookbook for deploying MINT securely (Chris Hafey + Tim Culp)
  * Specify MINT standard on Wiki (Chris Hafey + All)
    * Error codes
    * URL
    * XSD
    * Validation rules
    * Update the MINT metadata document with which VRs are candidates for binary items and the option to encode in base 64 and version number and type for study meta (Chris Hafey)
  * Add unit tests for key classes and add junit to ant to produce code coverage (Jeremy)
  * Performance cookbook (Gorkem + Chris + All)
  * Develop integration tests (Jim + Tim Culp)
  * Add support for non DICOM types (Chris)
    * Data dictionaries for Vital Volumes
    * Data dictionary for generic mime type attachments
    * Root study URL to list all types in study
  * Measure performance of MINT vs DICOM as per PPT (Gorkem)
  * Post to ClearCanvas forums, get help with packaging (Gorkem)


# Completed Actions #

# Backlog Items #
  * Look at QC workflow in more detail - specifically about metadata validation errors (does not conform to data dictionary)
  * Add mint server validation



# Issues #

# Future #