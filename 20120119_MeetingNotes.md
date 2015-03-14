# Agenda #
  * HIMSS meeting
  * Governance - chair/secretary/etc
  * Resourcing for Reference Implementation
  * WADO rendering - consider this for MINT?
  * Discuss Vital's storage implementation for reference implementation
  * Decimal representation
  * Normalization logic / QC / error logging in metadata?

# MINT @ HIMSS meeting #
  * Options: Feb 21 730-1030am, Feb 21 10am-1pm, or Feb 22 8am-1030am
  * Agenda: review API, resourcing for refimpl, discuss relationship to WADO-RS, governance

# Governance #
  * Need to pass the baton, Tim Dawson has been doing the scehduling and note-taking for quite a while now
  * Tim Culp volunteered to take over as chair for the next three months
  * Need to define more formal roles, guidance, voting, etc.

# Reference Implementation resourcing #
  * Vital will update base API (remove /DICOM from url), implement attachments, and storage API
  * Harris volunteered resources for DICOM, transfer syntax
  * still need owners for other API

# WADO rendering #
  * Need to investigate whether this is part of WADO-WS... if not may be able to ignore for WADO-RS
  * Should we separate this as WADR? (Web Access to DICOM Rendering) or something like that?
  * Definitely not part of MINT either way; a MINT server could implement WADO or WADR or whatever...

# Vital's storage impl #
  * reviewed, recommended a few changes:
  * current base path based on UUID is good
  * for MINT 2.0 can flatten the structure under the base path to:
  * [uuid](uuid.md)/bulkdata
  * [uuid](uuid.md)/metadata
  * [uuid](uuid.md)/attachments

# Decimal Representation #
  * a user commented that parsing numerics from XML gave an error in Belgium, because 1.234 is one thousand two hundred thirty four because "." is thousands and "," is decimal.
  * need to define that MINT stnadard uses XSD decimal standard where period "." is the decimal seprator.

# Normalization Logic #
  * discussed need to identify when data has been automatically 'fixed up' or when errors have been detected.
  * discussed but did not finalize and idea about having a spot in the metadata to store recoverable and unrecoverable errors for the error queue