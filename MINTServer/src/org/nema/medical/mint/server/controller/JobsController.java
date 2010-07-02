/*
 *   Copyright 2010 MINT Working Group
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */
package org.nema.medical.mint.server.controller;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.fileupload.FileItemIterator;
import org.apache.commons.fileupload.FileItemStream;
import org.apache.commons.fileupload.FileUploadException;
import org.apache.commons.fileupload.servlet.ServletFileUpload;
import org.apache.commons.fileupload.util.Streams;
import org.apache.log4j.Logger;
import org.nema.medical.mint.common.domain.JobInfo;
import org.nema.medical.mint.common.domain.JobInfoDAO;
import org.nema.medical.mint.common.domain.JobStatus;
import org.nema.medical.mint.common.domain.StudyDAO;
import org.nema.medical.mint.common.metadata.Study;
import org.nema.medical.mint.common.metadata.StudyIO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class JobsController {

	private static final Logger LOG = Logger.getLogger(JobsController.class);

	@Autowired
	protected File jobTemp;
	@Autowired
	protected File studiesRoot;

	@Autowired
	protected StudyDAO studyDAO = null;
	@Autowired
	protected JobInfoDAO jobInfoDAO = null;

	@RequestMapping(method = RequestMethod.GET, value = {"/jobs/createstudy/{uuid}","/jobs/updatestudy/{uuid}"})
	public String getJobStatus(@PathVariable final String uuid,
			HttpServletResponse res, ModelMap map) throws IOException {
		
		JobInfo jobInfo = jobInfoDAO.findJobInfo(uuid);		
		map.addAttribute("jobinfo", jobInfo);
		map.addAttribute("joburi", jobInfo.getId());
		
		// this will render the job info using jobinfo.jsp
		return "jobinfo";
		
	}

	@RequestMapping(method = RequestMethod.POST, value = "/jobs/createstudy")
	public String createStudy(HttpServletRequest req, HttpServletResponse res,
			ModelMap map) throws IOException {

		String studyUUID = UUID.randomUUID().toString();
		String jobID = UUID.randomUUID().toString();

		File jobFolder = new File(jobTemp, jobID);
		jobFolder.mkdir();

		// the list of files uploaded
		List<File> files = new ArrayList<File>();

		// the set of form parameters
		Map<String, String> params = new HashMap<String, String>();

		// Check that we have a file upload request
		boolean isMultipart = ServletFileUpload.isMultipartContent(req);
		if (!isMultipart) {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			map.put("error_msg", "expected multipart form data");
			return "error";
		}

		try {
			handleUpload(req, res, jobFolder, files, params);
		} catch (FileUploadException e) {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			map.put("error_msg", "unable to parse multipart form data");
			return "error";
		}

		Iterator<File> iterator = files.iterator();
		if (!iterator.hasNext()) {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			map.put("error_msg",
					"at least one file (containing metadata) is required.");
			return "error";
		}		

		File studyRoot = new File(studiesRoot,studyUUID + "/DICOM");
		File metadata = iterator.next();
		Study study = null;
		
		if (metadata.getName().equals("metadata.xml")) {
			study = StudyIO.parseFromXML(metadata);
		} else if (metadata.getName().equals("metadata.gpb")) {
			study = StudyIO.parseFromGPB(metadata);
		} else {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			map.put("error_msg", "unable to parse metadata");
			return "error";
		}
		
		studyRoot.mkdirs();
		StudyIO.writeToGPB(study, new File(studyRoot,"metadata.gpb"));
		StudyIO.writeToXML(study, new File(studyRoot,"metadata.xml"));
		File binaryRoot = new File(studyRoot,"binaryitems");
		binaryRoot.mkdirs();
		while (iterator.hasNext()) {
			File tempfile = iterator.next(); 
			File permfile = new File(binaryRoot,tempfile.getName());
			// just moving the file since the reference implementation
			// is using the same MINT_ROOT for temp and perm storage
			// other implementations may want to copy/delete the file
			// if the temp storage is on a different device
			tempfile.renameTo(permfile);
		}
		metadata.delete();
		metadata.getParentFile().delete();

		JobInfo jobInfo = new JobInfo();
		jobInfo.setId(jobID);
		jobInfo.setStudyID(studyUUID);
		jobInfo.setStatus(JobStatus.IN_PROGRESS);
		jobInfo.setStatusDescription("0% complete");
		map.addAttribute("jobinfo", jobInfo);
		map.addAttribute("joburi", "createstudy/" + jobInfo.getId());

		jobInfoDAO.saveOrUpdateJobInfo(jobInfo);
		
		
		
		
		// this will render the job info using jobinfo.jsp
		return "jobinfo";
	}

	@RequestMapping(method = RequestMethod.POST, value = "/jobs/updatestudy")
	public String updateStudy(HttpServletRequest req, HttpServletResponse res,
			ModelMap map) throws IOException {

		String jobID = UUID.randomUUID().toString();
		File jobFolder = new File(jobTemp, jobID);
		jobFolder.mkdir();

		// the list of files uploaded
		List<File> files = new ArrayList<File>();

		// the set of form parameters
		Map<String, String> params = new HashMap<String, String>();

		// Check that we have a file upload request
		boolean isMultipart = ServletFileUpload.isMultipartContent(req);
		if (!isMultipart) {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			map.put("error_msg", "expected multipart form data");
			return "error";
		}

		try {
			handleUpload(req, res, jobFolder, files, params);
		} catch (FileUploadException e) {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			map.put("error_msg", "unable to parse multipart form data");
			return "error";
		}

		if (files.size() < 1) {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			map.put("error_msg",
					"at least one file (containing metadata) is required.");
			return "error";
		}

		if (!params.containsKey("studyUUID")) {
			res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
			map.put("error_msg", "missing parameter studyUUID");
			return "error";
		}

		// this will render the job info using jobinfo.jsp
		return "jobinfo";
	}

	// returns false if a response.sendError() was discovered
	public void handleUpload(HttpServletRequest request,
			HttpServletResponse response, File jobFolder, List<File> files,
			Map<String, String> params) throws IOException, FileUploadException {

		int bid = 0;

		// Parse the request
		ServletFileUpload upload = new ServletFileUpload();
		FileItemIterator iter;
		iter = upload.getItemIterator(request);
		while (iter.hasNext()) {
			FileItemStream item = iter.next();
			String name = item.getFieldName();
			InputStream in = item.openStream();

			if (item.isFormField()) {
				String value = Streams.asString(in);
				LOG.debug("found form field " + name + " = " + value);
				params.put(name, Streams.asString(in));
			} else {
				File file;
				if (files.isEmpty()) {
					String contentType = item.getContentType();
					if ("text/xml".equals(contentType)) {
						file = new File(jobFolder, "metadata.xml");
					} else if ("application/octet-stream".equals(contentType)) {
						file = new File(jobFolder, "metadata.gpb");
					} else {
						file = new File(jobFolder, "metadata.dat");
					}
				} else {
					file = new File(jobFolder, String.format("%d.dat",bid++));
				}

				FileOutputStream out = null;
				try {
					while (true) {
						byte buf[] = new byte[8 * 1024];
						int len = in.read(buf);
						if (len < 0)
							break;
						if (out == null) {
							// defer create so we don't create empty files
							out = new FileOutputStream(file);
							LOG.info("creating... " + file);
						}
						out.write(buf, 0, len);
					}
				} finally {
					if (out != null) {
						out.close();
						files.add(file);
					}
				}
			}
		}
	}
}
