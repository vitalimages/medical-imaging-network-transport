# Attendees #
  * Tim Dawson
  * Chris Hafey
  * Tim Culp
  * Jim Philbin
  * Gorkem
  * Anna
  * Rafael
  * Sam

# Agenda #
  * Summarize discussion from last WG-27 meeting
  * Summarize Vital/Toshiba discussion from 7/20

# WG-27 meeting summary/discussion #
  * They would like a first draft to add C-STORE to WADO by the Aug 8th telecon (Tim C is on vacation Jul 22-Aug 06, with other schedules, etc. this date is not likely achievable)
  * They want someone from MINT to do a gap analysis on Supplement 148 to define missing restful endpoints
  * They want to combine the C-STORE Work Item under the existing QIDO work item
  * WG27 meeting scheduled for Sep 19 and WG06 on Sep 20th
  * Final draft due Sep 6th (really end of Aug since it’s Labor Day weekend)

  * Jim will connect with Cor and send an email to everybody

# MINT/DICOM discussion at Vital #
  * Had a meeting at Vital as part of ongoing Vital/Toshiba integration
  * Kevin O'Donnell was involved, Jim Philbin happened to be in town as well, so we invited him and Chris Hafey to join with Tim Dawson at Vital.
  * Reviewed a number of DICOM supplements that were MINT related, discussed alignment
  * Due to the way DICOM committee works, best way to move forward is to tackle an area that's not being well addressed than to change stuff that is seen as 'working' (whether everybody thinks it works well or not)
  * One opportunity rasied was to focus on caching - use MINT as a cache interface to help eliminate viewer-specific caches.
    * This unfortunately doesn't address the core storage strategy we'd like to get to
    * ...but it may get us there.
  * When we engage with DICOM, need to speak with DICOM terms
    * we did not do that in the past and that was a contributing factor
  * Breaking MINT into pieces that match up with existing DICOM supplements
    * Search / QIDO
    * Changelog / NADO
    * Metadata / WADO?
    * Binary items / WADO?
    * Study create/update / C-STORE?
  * Need to work with Larry Tarbox to try to have QIDO consider what we've learned from MINT; similar NADO, etc.
  * Discused need to make sure that we're not too focused on read-only apis
    * Committed data / non-committed data
    * AV can create a new DICOM series - this may be difficult to be part of cache
  * Also discussed the 'marketing' need for a unified set of these APIs - 3 out of 4 of these APIs will fall short of achieving the benefits
    * Working with IHE to define a profile is probably the best way to do this

  * Chris will take an action to take a first pass at scope.