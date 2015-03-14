# Agenda #
  * DICOM WG-27 update
  * MINT Meeting @ RSNA
  * MINT 2.0 implementation

# Notes - DICOM WG27 #
  * Briefed redlines to Supplement 148 to suggest enhancing the URI support to have the same retrieve functionality as WADO WS
  * They suggested we continue to present our redlines in Supplement 148 however they will eventually be captured in a new supplement
  * They will provide a draft of DICOM Part 18 2012 in January for us to formally submit our inputs
  * There was a question regarding how caching would work (specifically if it would return the wrong cached item) if we supported both URIs with parameters as well as REST resource style URIs
  * They suggested we also look at the open items against the WADO WS specification since we could potentially address both in this new supplement
  * Suggested we reference WG 23 Part 18 XML schema for now since that is the only documented schema. A normalized schema should emerge out of WG-06 Multi-frame work item and our supplement will just inherit those schema changes
  * Asked us to remove change log resources although they agree it’s an important topic that needs to be addressed (outside the scope of the current work item)
  * They request we add series back into the study/series/sop resource. If the server does not support relational queries, it might be very inefficient for the server to discover the series UID when it can be passed in directly by the user (who should already know it)
  * Asked us to add an open issues section in front of the document
  * Presenting again at RSNA

# Notes - MINT @ RSNA #
  * Monday Nov 28, 11am-4pm @ Vital's suite
  * define detailed agenda @ next meeting (Nov 17)

# Notes - MINT 2.0 impl #
  * Harris is looking to devote resources, at least 1 full time, 1 part time
  * Vital is planning to devote 1 full time, 2 part time resources
  * Still looking for additional resources