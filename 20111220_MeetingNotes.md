# Attendees #
  * Tim Dawson
  * Tim Culp
  * Uli Bubenheimer

# Agenda #
  * Transfer syntax for WADO-RS
  * MINT 2.0 API
  * F2F meeting in January

# Transfer Syntax for pixel data #
  * WADO uses URL parameter
  * REST best practices use 'accept' header
  * should WADO-RS accept either or both? if we allow URL, most people will use this
  * regardless, response content-type will say what they're getting
  * if no requested type, just gives what is specified in metadata
  * similar to DICOM, support for multiple transfer syntaxes is optional, must support little-endian unless image is only available lossy

# MINT 2.0 API #
  * Append Study - POST studies/{identifier} - if we push a study to an off-site archive, does it retain the same UUID? if so this is also an alternate CREATE study
  * Replace Study - PUT studies/{identifier} - does multipart-mime PUT even exist? if so, does this address the pushing a study to another archive? (not necessarily 'replace'...)
  * Delete Study - DELETE studies/{identifier} - no changes needed
  * Cache operations: Acquire/Release retention lock - needed for marking a study in a cache to prevent it from being taken offline; optional. may allow separate expiration dates per person requesting the retention.
  * QC operations: get/release study lock - concern raised that use case is theoretical; propose pushing this until we have someone willing/ready to implement a client
  * Changelog: proposed returning this (had previously been removed). needs further discussion. at minimum must be optional.
  * Search: no changes, approved for draft final
  * approved removal of jobs interface, summary, and 'info' api for draft final
  * punted on authentication, encryption, de-identification, and thumbnails until January meeting

# Face to face meeting in January #
  * January 9, 10 - in Orlando. Tim Culp to send details.
  * Agenda: finalize MINT 2.0 API, discuss interface to DICOM (WADO-RS, QIDO, NADO), MINT reference implementation & community