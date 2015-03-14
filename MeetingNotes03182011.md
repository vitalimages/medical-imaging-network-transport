# Attendees #
  * Chris Hafey
  * Tim Culp
  * Gorkem Sevinc
  * Anasuya Basu

# Progress Since Last Meeting #
  * Chris Hafey
    * DICOM WG27 has created a work item for a MINT like standard
    * DICOM WG27 meeting next Wednesday at 11:30 EST - planning to call in
    * Continual positive support for MINT from the customer side
  * Tim Culp
    * DICOM WG27 - did review the work item, will be discussed @ next wed meeting
    * Reference Implementation - sent out some mail messages regarding extra tags show up in a couple of test cases they are running.  Looks like DCM4CHE is implicitly inserting them into the DICOM Stream.
      * Unclear why this is happening - is dcm4che fixing the data or ?
      * Need to check with Damien/dcm4che if this can be changed
    * Fixed a bug related to sequence items in MINT2DICOM
    * Have nightly automated test suite setup with nightly syncs from repository
      * 4 studies, 10 different scenarios
    * Mint conformance - running into issues where the MINT data dictionary is more accurate than the mint conformance one
      * Planning to add test case to validate mint conformance data dictionary test
  * Anasuya Basu
    * No updates
  * Gorkem Sevinc
    * Worked with Tim to figure out that dcm4che was adding elements to MINT2DICOM
    * Fixed a bug in MINT2DICOM with sequence items
    * Contacted by Tim Rajah at NIH that was interested in MINT

# Discussion #
  * Gorkem asked about whether or not we could add an alternative batch binary mechanism that returns a binary blob with offsets + binary items in addition to the multi-part mime mechanism.  Everyone OK with this
    * Use a custom mime-type and pass that to binaryitems/all - server will detect and return alternative representation
    * Gorkem to prototype and report back with results

  * Gorkem asked how the study summary is defined
    * Implicit logic - uses study and series level attributes defined in data dictionary

# Decisions #

# Issues raise @ WG27 meeting #

# Old Actions #
  * schedule meeting at SIIM to discuss 2.0 version of protocol
  * support for move/copy operations as forms of post operations
  * need to discuss binary and float handling with DICOM vendors at HIMSS (Jim)
  * need to reach out to DCM4CHE re: 2GB limit (Chris/Jim)
  * Tim C to send Dan a pathology image to test with DCM4CHE
  * Send out email to list to propose meeting to brainstorm MINT 2011 roadmap (Chris)
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