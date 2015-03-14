# Attendees #
  * Tim Culp
  * Gorkem Sevinc
  * Jim Philbin
  * Dan Chaffee
  * Anna
  * Tim Dawson
  * Uli Bubbenheimer

# Discussion #
  * Jim Philbin
    * WG27 meeting next Wednesday
    * Working on a white paper to present at WG27
    * Planning to revise DSC workitem proposal to focus on transport and not storage
    * Normalization may be a big part of the work item
    * Transport means
      * HTTP stuff - what MINT messages look like - normalization, binary items, etc
      * Services/verbs that are supported
    * Stuff not in the work item
      * Study UID as part of the URI
      * Requirements around database and metadata synchronization
      * Move/copy
    * Should we have a SIIM Meeting?
      * There is a WG27 meeting on Monday following SIIM with WG6 @ MITA
      * Probably too late to do a formal educational session - look to RSNA and SIIM next year
      * Have a dinner or lunch?
  * Gorkem
    * No updates
  * Tim Culp
    * Reviewed Uli's changes - look good
  * Dan Chaffee
    * Posted an ICD to download area - based on MINT API doc with more detail
  * Anna
    * No updates
  * Uli
    * Will be porting over Vital bug fixes to RI in the next two weeks
  * Tim Dawson
    * No updates
  * Chris Hafey
    * No updates

  * New WG27 Work Item Discussion
    * Create, retrieve, update and delete use cases
    * Changelog
    * Normalization
    * DICOM P10 -> MINT -> DICOM P10
    * Search ??
    * Versioning
    * Data dictionary


# Decisions #

# New Actions #
  * Update metadata document to match RI + decisions (Jim)
  * Coordinate SIIM informal event (Chris)
  * Write up some issues/thoughts related to validation and post to group (Dan)



# Old Actions #
  * Revisit OB/OW/OF/UN tags at study/series levels as part of MINT/WG27 activities (Jim/Chris)
    * Revisit binary floating point tags at study/series levels as part of MINT/WG27 activities (Jim/Chris)
    * Revisit data dictionary design as part of DICOM/WG27 work (Chris/Jim)
    * Explore deprecating implicit transfer syntax support in MINT via DICOM/WG27 work (Chris/Jim)
    * Investigate how the MINT RI handles valdiation errors for insert and update operations and report back to next weeks meeting (Dan)
    * DICOM2MINT conversion should be updated so it handles the decision for how to name binary items with multi-part mime filename [Uli](Uli.md)
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