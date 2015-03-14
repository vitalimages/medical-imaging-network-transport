## Attendees ##

  * Tim Culp
  * Jonathan Whitby
  * Andy Wilson
  * Jim Philbin

## Agenda ##

  * Action Item Review
  * Open Health Tools April 12-13 (MN) 17-18th (FL)
  * BigEndian issue in MINT1.0 Server
  * WADO-RS Supplement Update
  * Vital Updates
  * Open Technical Items
    * Normalization (WG-06 normalization rules)
    * Error Queue
    * Web security
    * Unlimited text (UT) international char sets (utf-8 or binary)
    * Pixel data big endian/little endian issues with unsigned
    * MINT Conformance endian issues

---

## Discussion ##
  * Had discussions with Chris Hafey regarding refreshing the ClearCanvas plugin. He also might consider building a C# MINT2.0 Server
  * Discussed MINT conformance to DICOM Standard for decimal representation (ie, remove all commas and use period as the separator). It was suggested that we should encompass all DICOM encoding standards (date/time, etc). Jim suggested that we should have a single, normalized form for the server implementation, and then appropriately convert to whatever format on the edge.
  * MINTConformance tools have been updated to check for differences for studies with mixed endian architectures. Seems to be a problem with MINT1.0 Server where BigEndian studies have "OW" binary items that are being stored as little endian.
  * Draft WADO RS API presentation for WG-27 went swimmingly. Tim C. will be sending out a revision to this group for final comment then forwarding to a few WG-06 members for pre-review.
  * Open Health Tool web site set up. Charter project is called MIAMI and MINT is a subproject and is setup with the atlassian suite of integrated tools. They are a cloud based environment called "on-demand" and it's free for open source projects (ohtmiami.atlassian.net). We will have a special MINT meeting next week for a demo of the development environment and a discussion for our next face to face meetings. TBD Minneapolis April 12-13 and TBD FL April 17-18.
  * Mahmoud is finishing up the documentation for Multi-Series DICOM and the code is uploaded to atlassian
  * Vital is finalizing requirements for their mid June implementation based on MINT2.0 resources. This server will support attachments but will only partially support the other resources. Jon has time to help out with ICD, specifically the areas that Vital is developing.

## Decisions ##

  * MINT2 server shall have a single, normalized form for the server implementation (MS-DICOM), and then appropriately convert to appropriate formats on the edge.

## Actions ##

  * Tim C. to forward BigEndian test results to Vital for confirmation of MINT Server endian issue.
  * Set up meeting next week for mid April (Jon and Tim C.)
  * Send an email to Jim Philbin so he can open Miami accounts for the develop (everyone)