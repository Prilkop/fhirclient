#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2022-05-29.
#  2022, SMART Health IT.


import os
import io
import unittest
import json
from . import encounter
from .fhirdate import FHIRDate


class EncounterTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Encounter", js["resourceType"])
        return encounter.Encounter(js)
    
    def testEncounter1(self):
        inst = self.instantiate_from("encounter-example-f001-heart.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter1(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter1(inst2)
    
    def implEncounter1(self, inst):
        self.assertEqual(inst.class_fhir, "outpatient")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].code, "305956004")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].display, "Referral by physician")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].code, "306689006")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].display, "Discharge to home")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.system, "http://www.amc.nl/zorgportal/identifiers/pre-admissions")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.use, "official")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.value, "93042")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http://www.amc.nl/zorgportal/identifiers/visits")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "v1451")
        self.assertEqual(inst.length.code, "min")
        self.assertEqual(inst.length.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.length.unit, "min")
        self.assertEqual(inst.length.value, 140)
        self.assertEqual(inst.priority.coding[0].code, "310361003")
        self.assertEqual(inst.priority.coding[0].display, "Non-urgent cardiological admission")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reason[0].coding[0].code, "34068001")
        self.assertEqual(inst.reason[0].coding[0].display, "Heart valve replacement")
        self.assertEqual(inst.reason[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "270427003")
        self.assertEqual(inst.type[0].coding[0].display, "Patient-initiated encounter")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter2(self):
        inst = self.instantiate_from("encounter-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter2(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter2(inst2)
    
    def implEncounter2(self, inst):
        self.assertEqual(inst.class_fhir, "outpatient")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].code, "305997006")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].display, "Referral by radiologist")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].code, "306689006")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].display, "Discharge to home")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.system, "http://www.bmc.nl/zorgportal/identifiers/pre-admissions")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.use, "official")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.value, "98682")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/encounters")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "v3251")
        self.assertEqual(inst.length.code, "min")
        self.assertEqual(inst.length.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.length.unit, "min")
        self.assertEqual(inst.length.value, 140)
        self.assertEqual(inst.priority.coding[0].code, "103391001")
        self.assertEqual(inst.priority.coding[0].display, "Urgent")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reason[0].coding[0].code, "34068001")
        self.assertEqual(inst.reason[0].coding[0].display, "Partial lobectomy of lung")
        self.assertEqual(inst.reason[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "270427003")
        self.assertEqual(inst.type[0].coding[0].display, "Patient-initiated encounter")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter3(self):
        inst = self.instantiate_from("encounter-example-f003-abscess.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter3(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter3(inst2)
    
    def implEncounter3(self, inst):
        self.assertEqual(inst.class_fhir, "outpatient")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].code, "305956004")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].display, "Referral by physician")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].code, "306689006")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].display, "Discharge to home")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.system, "http://www.bmc.nl/zorgportal/identifiers/pre-admissions")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.use, "official")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.value, "93042")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/encounters")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "v6751")
        self.assertEqual(inst.length.code, "min")
        self.assertEqual(inst.length.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.length.unit, "min")
        self.assertEqual(inst.length.value, 90)
        self.assertEqual(inst.priority.coding[0].code, "103391001")
        self.assertEqual(inst.priority.coding[0].display, "Non-urgent ear, nose and throat admission")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reason[0].coding[0].code, "18099001")
        self.assertEqual(inst.reason[0].coding[0].display, "Retropharyngeal abscess")
        self.assertEqual(inst.reason[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reason[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/encounter-primaryDiagnosis")
        self.assertEqual(inst.reason[0].extension[0].valueInteger, 1)
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "270427003")
        self.assertEqual(inst.type[0].coding[0].display, "Patient-initiated encounter")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter4(self):
        inst = self.instantiate_from("encounter-example-f201-20130404.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter4(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter4(inst2)
    
    def implEncounter4(self, inst):
        self.assertEqual(inst.class_fhir, "outpatient")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.identifier[0].use, "temp")
        self.assertEqual(inst.identifier[0].value, "Encounter_Roel_20130404")
        self.assertEqual(inst.priority.coding[0].code, "17621005")
        self.assertEqual(inst.priority.coding[0].display, "Normal")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reason[0].text, "The patient had fever peaks over the last couple of days. He is worried about these peaks.")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "11429006")
        self.assertEqual(inst.type[0].coding[0].display, "Consultation")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter5(self):
        inst = self.instantiate_from("encounter-example-f202-20130128.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter5(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter5(inst2)
    
    def implEncounter5(self, inst):
        self.assertEqual(inst.class_fhir, "outpatient")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.identifier[0].use, "temp")
        self.assertEqual(inst.identifier[0].value, "Encounter_Roel_20130128")
        self.assertEqual(inst.length.code, "258701004")
        self.assertEqual(inst.length.system, "http://snomed.info/sct")
        self.assertEqual(inst.length.unit, "minutes")
        self.assertEqual(inst.length.value, 56)
        self.assertEqual(inst.priority.coding[0].code, "103391001")
        self.assertEqual(inst.priority.coding[0].display, "Urgent")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reason[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/encounter-primaryDiagnosis")
        self.assertEqual(inst.reason[0].extension[0].valueInteger, 2)
        self.assertEqual(inst.reason[0].text, "The patient is treated for a tumor.")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "367336001")
        self.assertEqual(inst.type[0].coding[0].display, "Chemotherapy")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter6(self):
        inst = self.instantiate_from("encounter-example-f203-20130311.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter6(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter6(inst2)
    
    def implEncounter6(self, inst):
        self.assertEqual(inst.class_fhir, "inpatient")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].code, "309902002")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].display, "Clinical Oncology Department")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.dietPreference[0].coding[0].code, "276026009")
        self.assertEqual(inst.hospitalization.dietPreference[0].coding[0].display, "Fluid balance regulation")
        self.assertEqual(inst.hospitalization.dietPreference[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.reAdmission.coding[0].display, "readmitted")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.identifier[0].use, "temp")
        self.assertEqual(inst.identifier[0].value, "Encounter_Roel_20130311")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-03-20").date)
        self.assertEqual(inst.period.end.as_json(), "2013-03-20")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.period.start.as_json(), "2013-03-11")
        self.assertEqual(inst.priority.coding[0].code, "394849002")
        self.assertEqual(inst.priority.coding[0].display, "High priority")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reason[0].text, "The patient seems to suffer from bilateral pneumonia and renal insufficiency, most likely due to chemotherapy.")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "183807002")
        self.assertEqual(inst.type[0].coding[0].display, "Inpatient stay for nine days")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter7(self):
        inst = self.instantiate_from("encounter-example-home.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter7(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter7(inst2)
    
    def implEncounter7(self, inst):
        self.assertEqual(inst.class_fhir, "virtual")
        self.assertEqual(inst.contained[0].id, "home")
        self.assertEqual(inst.id, "home")
        self.assertEqual(inst.location[0].period.end.date, FHIRDate("2015-01-17T16:30:00+10:00").date)
        self.assertEqual(inst.location[0].period.end.as_json(), "2015-01-17T16:30:00+10:00")
        self.assertEqual(inst.location[0].period.start.date, FHIRDate("2015-01-17T16:00:00+10:00").date)
        self.assertEqual(inst.location[0].period.start.as_json(), "2015-01-17T16:00:00+10:00")
        self.assertEqual(inst.location[0].status, "completed")
        self.assertEqual(inst.participant[0].period.end.date, FHIRDate("2015-01-17T16:30:00+10:00").date)
        self.assertEqual(inst.participant[0].period.end.as_json(), "2015-01-17T16:30:00+10:00")
        self.assertEqual(inst.participant[0].period.start.date, FHIRDate("2015-01-17T16:00:00+10:00").date)
        self.assertEqual(inst.participant[0].period.start.as_json(), "2015-01-17T16:00:00+10:00")
        self.assertEqual(inst.period.end.date, FHIRDate("2015-01-17T16:30:00+10:00").date)
        self.assertEqual(inst.period.end.as_json(), "2015-01-17T16:30:00+10:00")
        self.assertEqual(inst.period.start.date, FHIRDate("2015-01-17T16:00:00+10:00").date)
        self.assertEqual(inst.period.start.as_json(), "2015-01-17T16:00:00+10:00")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.div, "<div>Encounter with patient @example who is at home</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testEncounter8(self):
        inst = self.instantiate_from("encounter-example-xcda.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter8(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter8(inst2)
    
    def implEncounter8(self, inst):
        self.assertEqual(inst.class_fhir, "outpatient")
        self.assertEqual(inst.id, "xcda")
        self.assertEqual(inst.identifier[0].system, "http://healthcare.example.org/identifiers/enocunter")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "1234213.52345873")
        self.assertEqual(inst.reason[0].coding[0].code, "T-D8200")
        self.assertEqual(inst.reason[0].coding[0].display, "Arm")
        self.assertEqual(inst.reason[0].coding[0].system, "http://ihe.net/xds/connectathon/eventCodes")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
    
    def testEncounter9(self):
        inst = self.instantiate_from("encounter-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter9(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter9(inst2)
    
    def implEncounter9(self, inst):
        self.assertEqual(inst.class_fhir, "inpatient")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.status, "in-progress")
        self.assertEqual(inst.text.div, "<div>Encounter with patient @example</div>")
        self.assertEqual(inst.text.status, "generated")

