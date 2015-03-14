# Agenda #
  * Open items from email list
  * Supplement 148 changes for RSNA
  * MINT Meeting @ RSNA

# Open items from email list #
  * Content negotiation
> > cannot do this today, but would be possible using HTTP accept header.
> > this would increase the cost of implementing MINT if we required transformations, so it must be optional - which would allow vendor differentiation
  * HTTP caching - Accept header vs. REST resource
> > need to research different caches; Dan will send a link
> > one idea: allow accept header & redirect to REST resource with content type
  * DICOM UT value representation
> > agree with Uli's recommendation... UT should be inline if small, otherwise externalized into a binary item. same basic rules as small binary items, but no need to base64 encode (do need to encode to prevent embedded characters causing xml problems)
> > Jonathan - look at UT tags in part19 XML
  * Non-DICOM types & hierarchy
> > first draft had just a single level of files underneath a type
> > this is too restrictive and would cause vendors to create a lot of different types
> > nested folder structures seems like a reasonable approach
> > still need to talk about type registration

# Supplement 148 changes for RSNA - open issues #
  * what metadata schema will we use? WG-27 desires use of part19
    * concern of non-normalized metadata
    * XPATH is problematic
    * enh. multiframe conversion may attack this
    * need a shorthand mapping of ID within a study to a UID representing an instance/frame
  * returning a range of SOP instances
    * do we need to specify multiple, or can we filter on a series?
    * cannot do range of UIDs, need a list
  * HTTP accept headers
    * application/dicom vs. application/wado
    * for transfer syntaxes? application/dicom/xferSyntax?
  * private metadata
    * how does 3.19 handle private XML tags?
  * Metadata/info vs. XPath
    * xpath puts burden on users to create XPath, on server to apply
    * performance impact
    * cannot cache study info
    * however, xpath does provide advantage of allowing client choice
  * Parameters vs. resource
    * URL length, caching resource

# Notes - MINT @ RSNA #
  * Monday Nov 28, 11am-4pm @ Vital's suite
  * define goals for meeting
    * finalize proposed MINT 2.0 REST API
    * review/finalize recommendation for sup148
    * performance implications / Jim present
    * community discussion
    * attendee list
  * open issues for MINT 2.0
    * need to address type collision
    * discuss potential use of part19 XML