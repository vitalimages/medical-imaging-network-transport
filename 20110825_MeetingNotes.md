# Agenda #

  * Mission Statement
  * DICOM work items
  * Define projects / tasks (primarily for MINT 2.0)
  * Define process for adding contributors/committers, acepting changes, development standards
  * MINT 2.0 REST API change discussion

# Details #

**Mission Statement**

Finalized on "Our mission is to improve medical imaging by addressing the need for fast, easy and interoperable access to unified medical imaging records.  We will achieve this by defining interim standards and creating production quality open source implementations that leverage web and other new technologies.  We will collaborate with vendors to validate solutions in the real world, and work with existing industry standards bodies (DICOM, IHE, HL7) to incorporate and standardize these new approaches."

**DICOM work items**

  * Discussed STOW (Store Over the Web) work item.  Agreed that the approach is non-controversial, need to keep discussion of metadata normalization out, try to address separately in the future.

  * WADO REST/SOAP gap analysis
    * need to define the differences between REST and SOAP versions of WADO, so we can bring them up to functional equivalence
    * then need to define work items for bulk and individual access to binary items

  * QIDO
    * will be discussed at next WG-27 meeting (Mon Sept 19 in DC 830-noon).  Jim to reach out to Larry Tarbox.

  * NADO
    * need to investigate where this is, provide feedback of what we've learned with MINT changelog polling

  * Study level relaxed multiframe
    * Need to check with David Clunie create the work item to allow study level relaxed multiframe for CT, MR, and PET.

  * MIME type SOP class
    * Suggested we propose a SOP class for MIME type data - similar to PDF wrap but simply mime type + binary item

**Projects Defined**

  * DICOM encoding of MINT metadata
    * Discussed adding DICOM encoding for metadata to MINT; this would be less controversial for DICOM committee than (1) pushing metadata normalization or (2) adding MINT's GPB format.  It is also comparable to GPB in overall size, however does require a DICOM library to be used.
    * Content negotiation via mime type
    * Need to discuss further whether we want to 'tighten up' the DICOM metadata format allowed by MINT, use explicit transfer syntax, little endian, define sequence encoding, etc.
    * Owner: ?

  * Internal metadata format for open source implementation
    * Need to determine the most efficient metadata format (suspect gzipped DICOM will be comparable to existing gzipped GPB in size, decoding time)
    * Owner: ?

  * Flesh out FAQ for website
    * Review/revise existing FAQ
    * Technical vs. Organizational FAQ
    * Owner: core leadership team
    * Organizational
      * What is MINT
        * focus on network transport - still DICOM data internally
        * implementation is a cache, not an archive
        * Why MINT? - history and mission
      * Is MINT trying to replace DICOM?
        * Why doesn't MINT render images, provide window/level, zoom, etc.
          * separation of concerns
      * What is MINT's relationship with DICOM?
      * Who currently implements MINT? (who are we targeting to implement MINT)
      * How/where is MINT being used today?
        * diagram showing MINT cache and DICOM archive
        * show DICOM within MINT transport
      * How can I get involved?
    * Technical
      * Why doesn't MINT use existing supplement 118 XML format?
        * Why REST?

  * Flesh out API documentation more fully
    * define handling of HEAD and other requests
    * define usage of eTag, files not updated, etc.

  * Address security explicitly
    * Make security explicit within MINT implementation
    * Define recommendations

  * Update semantics
    * review existing literature/standards (IHE supplement for image object change management)
    * need to cover add/delete/modify (e.g. patient name change)

  * MINT 2.0 REST API
    * detail later this afternoon

  * Diagram Common Scenarios
    * Viewer, MINT cache, DICOM archive & prefetch
    * Viewer, MINT cachem, MINT archive & prefetch
    * Thin client, browser client w/web server
    * Viewer, MINT archive alone
    * etc.

  * MINT viewers
    * goal: illustrate performance of MINT via open source viewers
    * capabilities needed
      * basic viewer with minimal setup
      * fast time to first image display: chest xray, CT, MR
      * 1x1
    * W/L
    * thumbnail
      * options
        * iPad
    * mobile phone client
      * Thin C# client to show performance of direct access to MINT
    * adapt Oviyam to work off MINT
    * continue to maintain clear canvas (doesn't met needs above though)
    * investigate using WADO render API off MINT server

  * ATNA audit logging

  * pull remaining projects from http://code.google.com/p/medical-imaging-network-transport/wiki/20110715_MeetingNotes