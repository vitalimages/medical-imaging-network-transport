# MINT Performance Testing #

## Summary ##
This independent performance test is intended to verify the initial findings from the first documented MINT performance test. The test will attempt to match the original environment as closely as possible and to report performance results. Some additional, supplementary tests and findings are included.

## Testing Environment ##

  * Servers
    1. (VM) Windows Server 2003 Standard Edition SP2, Intel Xeon CPU E5502 @ 1.87GHz, 2GB RAM
    1. (VM) Windows Server 2008 [R2](https://code.google.com/p/medical-imaging-network-transport/source/detail?r=2) Standard Edition, Intel Xeon CPU dual core 1.87Ghz, 4GB RAM
    1. TBD linux

  * Client
    1. (VM) Windows Server 2003 Standard Edition SP2, Intel Xeon CPU E5502 @ 1.87GHz, 2GB RAM

Client system is connected to the servers via 1Gigabit intranet connection with <1ms ping response. Ping response was determined by doing a "ping `<server>` -n 20" to get average response time.Curl was used to measure transport. Curl redirected output to NUL(curl -o NUL `<url>`) to ensure client disk latency was not a factor.

# Testing methodology #
For each test, 6 runs were performed, with the first one always being thrown out to ensure the data was cached in memory by the OS.
The same study was used for all test runs, with a request of http://{ip}/MINT/studies/{uuid}/DICOM/binaryitems/all. The study used represented 540M of binary data. For testing throughput on non-MINT transfers, the binary items were concatenated into a single file and served out.
For Windows operating systems four tests were run:

  * MINT get all binary items request served directly by Tomcat.
  * Binaryitems file served by Apache httpd.
  * Binaryitems file served by ftp via IIS.
  * MINT get all binary items request served by IIS with an AJP ISAPI redirect to Tomcat.

Windows 2003 tests ran IIS 6.0. Windows 2008 tests ran IIS 7.0. For IIS 6.0, there is a known performance issue with ISAPI redirects (http://support.microsoft.com/kb/906977/). The testing was run with the change to MaxBufferedSendBytes as instructed by the kb article.

httpd on Windows 2008 required a modification to the httpd.conf to uncomment out the following entries

  * #EnableMMAP off
  * #EnableSendfile off

Transfer speeds before this change were < 1MB/s, and ~17MB/s after the change

## Test Results ##

## Data Table ##

Test data results are available below for reference.  All values for runs represent average MB/sec over the entire transfer, except for the Average column which represents the average value of all runs.<br />
| | **Average** | **Run 1** | **Run 2** | **Run 3** | **Run 4** | **Run 5** |
|:|:------------|:----------|:----------|:----------|:----------|:----------|
| **Windows 2003-MINT served directly by Tomcat** |40.0|40.3|40.5|41.4|39.3|38.7|
| **Windows 2003-Binaryitems file served by Apache httpd** |X |X |X |X |X |X |
| **Windows 2003-Binaryitems file served by IIS over FTP** |26.7|30.0|28.2|22.8|27.5|24.8|
| **Windows 2003-MINT AJP ISAPI redirect from IIS** |X |X |X |X |X |X |
| **Windows 2008-MINT served directly by Tomcat** |21.1|21.1|20.4|22.1|21.1|20.8|
| **Windows 2008-Binaryitems file served by Apache httpd** |16.7|17.0|16.6|16.9|16.8|16.0|
| **Windows 2008-Binaryitems file served by IIS over FTP** |47.0|42.2|50.8|47.9|49.1|45.3|
| **Windows 2008-MINT AJP ISAPI redirect from IIS** |36.6|36.5|37.3|36.0|35.7|37.5|
| **Linux TBD-Binaryitems file served by Apache httpd** |X |X |X |X |X |X |
| **Linux TBD-Binaryitems file served by vsftp** |X |X |X |X |X |X |
| **Linux TBD-MINT served directly by Tomcat** |X |X |X |X |X |X |