/*
 * Copyright 2016-2017 the original author or authors.
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

package org.springframework.samples.petclinic.rest;

import java.util.Collection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.samples.petclinic.model.Alert;
import org.springframework.samples.petclinic.service.AlertService;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import co.elastic.apm.api.ElasticApm;
import co.elastic.apm.api.Transaction;

/**
 * @author Vitaliy Fedoriv
 *
 */

@RestController
@CrossOrigin(exposedHeaders = "errors, content-type")
@RequestMapping("api/alerts")
public class AlertRestController {

	@Autowired
	private AlertService alertService;

	@RequestMapping(value = "/alert", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_UTF8_VALUE)
	public ResponseEntity<Collection<Alert>> getAlert() {
		Transaction transaction = ElasticApm.startTransaction();
		Collection<Alert> alerts = null;
		try {
			transaction.setName("AlertService.getAlert()");
			transaction.setType(Transaction.TYPE_REQUEST);

			alerts = this.alertService.findAllAlerts();

		} catch (Exception e) {
			transaction.captureException(e);
			throw e;
		} finally {
			transaction.end();
		}
		
		return new ResponseEntity<Collection<Alert>>( alerts, HttpStatus.OK );
	}


}
