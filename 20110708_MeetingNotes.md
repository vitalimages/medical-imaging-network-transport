# Attendees #
  * Tim Dawson
  * Uli Bubenheimer
  * Chris Hafey
  * Tim Culp
  * Jim Philbin
  * Gorkem
  * Anna
  * Rafael
  * Sam
  * Mahmoud

# Agenda #
  * Review notes from previous meetings
  * Status updates
  * Continue discussion of changes needed for MINT 2.0

# Discussion #
  * Long term goal of MINT with respect to DICOM
    * Continue progressing MINT as a common standard in its own right
    * Continue working with DICOM committee to improve DICOM with concepts or APIs from MINT
    * Discussion of using multiframe DICOM to provide normalized access within DICOM similar to MINT
    * Need to tighten group and become more formal than in the past
  * FUD exists in marketplace from opponents
    * We haven't defined MINT well enough
    * Define use cases, e.g. archive vs. viewer
    * Some people will always be opposed to MINT, but we have to eliminate misunderstandings and misinformation
  * What is the theme for MINT 2.0?
    * Harden APIs, improve documentation
    * Defined normalization algorithm
    * Improve reference implementation
      * This isn't necessarily part of the spec per se, but part of RI and done in the same timeframe.
      * Storage API
      * Logging/Error Handling API
      * Client API/SDK
    * Address governance issues with standardization
  * Proposed in-person meeting @ Vital May 2/3 with Conference Call
    * Strategic planning July 15 11:30am CST / 12:30pm EST
      * Tim, Dan from Harris, Tim, Uli from Vital, Gorkem, Jim, Chris Hafey
  * Special meeting Friday July 15 at usualy time (10:30am CST) to discuss remaining tactical MINT isuses below

# remaining items to discuss for MINT 2.0 #
  * Binary data upload part naming
  * Client SDK
    * H2MI has implemented something, needs permission to release (Gorkem)
  * Permanent vs. Temporary Updates & Types
  * Error Handling (and inclusion within metadata)
    * introduced the topic (issues when converting from DICOM)
  * Ability to make single-call pull of metadata + binary
  * Ability to request binary response with offsets instead of multipart-mime
    * Performance test to compare and validate before finalizing change
  * Reference Impl changes (Storage API)