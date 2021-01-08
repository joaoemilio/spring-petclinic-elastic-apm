/*
 * Copyright 2002-2017 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.springframework.samples.petclinic.service;

import java.util.Collection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.samples.petclinic.model.Alert;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.client.RestTemplate;

import co.elastic.apm.api.CaptureSpan;

/**
 * Mostly used as a facade for all Petclinic controllers
 * Also a placeholder for @Transactional and @Cacheable annotations
 *
 * @author Joao Emilio
 */
@Service

public class AlertServiceImpl implements AlertService {

    @Autowired
     public AlertServiceImpl() {
    }

	@Override
	@Transactional(readOnly = true)
	public Collection<Alert> findAllAlerts() throws DataAccessException {

		try{
			final String uri = "http://localhost:5000/";

			RestTemplate restTemplate = new RestTemplate();
			String result = restTemplate.getForObject(uri, String.class);

			System.out.println(result);

			String url_php = "http://localhost:9080/health.php";
			result = restTemplate.getForObject(url_php, String.class);

			System.out.println(result);

		}catch(Exception e) {
			System.out.println("error: " + e.getMessage() );
			e.printStackTrace();
		}

		Collection<Alert> alerts = new java.util.Vector<Alert>();
		Alert alert = new Alert();
		alert.setCode("0001");
		alert.setMessage("alert message 0001");
		alerts.add(alert);

		tracedMethod();
		
		return alerts;
	}

	@CaptureSpan
	private void tracedMethod() {

		System.out.println("tracedMethod");
	}


}
