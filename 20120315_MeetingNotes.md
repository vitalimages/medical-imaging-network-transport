## Attendees ##

  * Tim Culp
  * Jonathan Whitby
  * Andy Wilson

## Agenda ##

  * Action Item Review
  * C#/.NET project suggestions
  * WADO-RS Supplement
  * QIDO Update
  * Open Technical Items
    * Decimal Representation
    * Normalization (WG-06 normalization rules)
    * Error Queue
    * Web security
    * Unlimited text (UT) international char sets (utf-8 or binary)
    * Pixel data big endian/little endian issues with unsigned
    * MINT Conformance endian issues
    * WADO-RS resources (GetFrames)

## Discussion ##

  * Jonathan is available for helping develop the MINT2.0 SDK.
  * Do we have any projects that could be done in C#/.NET? Chris Hafey is volunteering to help. Jon will check with Tim Dawson for ideas but a simple C#/.NET viewer for a PC, laptop, or mobile phone would be cool.
  * Tim is presenting WADO-RS to WG-27 tomorrow which should finalize the WADO-RS resources. This will be the launching point for the MINT2.0 SDK.
  * Tim reviewed WADO-RS. Question regarding why WADO WS Retrieve Metadata section was listed as "Not supported" under AE Specifications. Also a question whether we want to set an upper limit to the number of concurrent RS users. Jonathan suggested the Bulkdata resource should be a list so it can retrieve a single item or a list of items. Need to beef up security section. Possibly need to describe the Frame parameters in Section 8. Would be nice to have a few example responses and requests for clarity.
  * Kevin talked with Larry and he is available at the end of March to begin work on QIDO. We should reach out to Larry and see if there is any help we can offer.
  * We should also get started on STOW work item. Maybe Harris can take the lead on STOW and Vital on QIDO.
  * WADO-RS resources (GetFrames)
    * Frame resources were resolved at HIMSS.
    * We will provide a simple frame list and a calculated frame list.
  * MINT Conformance endian issues
    * Conformance tools were designed to handle big endian studies but never tested because there was no data
    * JHH data now available and it under covered an issue. When parsing the Part 10 header and discovering the file was big endian, a switch was flipped to treat the remaining binary as big endian. But that does not apply to the remainder of the Part 10 header...just for the SOP Instance data after the header.
    * Fixed it by creating a DicomHeader class that parses the entire header as EVRLE. Then it continues to parse the data in the appropriate endianess.
    * Needs to be regression tested and delivered to the baseline.
  * Decimal Representation
    * Issue is locale can introduce commas and decimals in reversed positions which causes floating point numbers to be misinterpreted.
    * Jonathan says the DICOM standard is pretty explicit about removing commas from floating point numbers and using a period as the whole part fractional part separator.
    * This normalization needs to be done within the MINT Server.

## Decisions ##

  * Provide resource for retrieving a Simple Frame List and a Calculated Frame List as documented in the DICOM WADO-RS Supplement.
  * MINT shall conform to DICOM Standard for decimal representation (ie, remove all commas and use period as the separator).