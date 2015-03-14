# Attendees #
  * Tim Dawson
  * Chris Hafey
  * Tim Culp
  * Dan Chaffee
  * Jim Philbin
  * Gorkem
  * Anna

# Agenda #
  * Continue discussion of changes needed for MINT 2.0

# MINT 2.0 Tactics Discussion #
  * Binary data upload part naming
    * defer until Uli and Gorkem are present
  * Client SDK
    * H2MI implementation pending legal release
    * not a required portion of the specification
    * move to strategy discussion
  * Permanent vs. Temporary Updates & Types
    * types are vendor specific, implementation could define a whole type as permanent vs. temporary.
    * types mechanism is a bit cumbersome, needs further polish
    * discussion about MINT cache vs. archive - move to strategic discussion
  * Error Handling (and inclusion within metadata)
    * how do we handle issues when converting from DICOM (e.g. from SCP)
    * this would be helpful for query/retrieve
    * push to strategic discussion - use cases
      * DICOM to MINT
  * Ability to make single-call pull of metadata + binary for a given type
    * this is the converse of the MINT study create multi-part mime
    * metadata followed by binary items
  * Ability to request binary response with offsets instead of multipart-mime
    * Sam built and tested, not significantly faster
    * Could do as a custom response based on mime-type content negotiation
  * Reference Impl changes (Storage API)
    * cleans up the reference impl readability
    * allows reuse of controller layer
    * storage API would allow others to implement easier
    * original priority was to make it readable - real priority should have been to make it easy for us to implement

and manage change between implementation
  * would allow the single-file implementation rather than per-binary-time files

# MINT 2.0 Strategic Discussion #
  * brainstorm of topics to discuss
    * relationship with DICOM WG27
    * cache model
    * transient & persistent changes
    * separate REST interfaces for viewers vs. archives
      * profiles, use cases, security
    * revisit extensible type model
    * data dictionary
    * MINT search API
    * extensible search capabilities / discovery of capabilities
    * relationship with DICOM Q/R
    * relationship with QIDO
    * formal definition of normalization
    * DICOM multiframe format to gain similar benefits to MINT
      * JHU is researching
    * formal reference documentation
    * formal SDK
    * error handling
    * strategies for easing implementation of MINT
      * storage API
      * better docs
    * non-destructive updates vs. destructive updates
      * eliminates lock complexity
      * modify is only for Q/C operations, very infrequent
      * DICOM has no update semantics
    * de-identification
    * hierarchy
      * separate out patient data from study data
      * access at the series level
      * level between patient and study - 'case'
    * address FUD created by MINT opponents
      * what mint IS and ISNOT
      * architecture diagram of use cases
    * standards body - governance of MINT
      * vision / mission statement
      * specific goals
    * compression (fits with persistent / non-persistent)
      * support some compression DICOM does not support?
    * encryption
      * use of manually encrypted payload within HTTP on port 80
    * security
      * whitepaper / cookbook
      * address concerns raised by opponents re: IHE/SAML
      * encryption at rest
    * simple viewer in the reference implementation
      * (CH) would help adoption. address who the mint clients are
    * should MINT move beyond a specification and RI to an entire open source product
      * DCM4CHE is an example (e.g. if DICOM and DCM4CHE were the same thing)
      * could integrate DCM4CHEE viewer
    * wikipedia article to get rid of the FUD
    * beyond the enterprise - regional/national/world level
  * need to flesh some of these these out to make in-person meeting more productive
  * prioritization
    * vision, mission, goals first
      * Chris, Jim will each craft a document, distribute by Wednesday for review next Friday
    * revisit prioritization items above later