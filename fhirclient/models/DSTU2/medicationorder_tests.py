#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2022-05-29.
#  2022, SMART Health IT.


import os
import io
import unittest
import json
from . import medicationorder
from .fhirdate import FHIRDate


class MedicationOrderTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicationOrder", js["resourceType"])
        return medicationorder.MedicationOrder(js)
    
    def testMedicationOrder1(self):
        inst = self.instantiate_from("medicationorder-example-f001-combivent.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationOrder instance")
        self.implMedicationOrder1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationOrder", js["resourceType"])
        inst2 = medicationorder.MedicationOrder(js)
        self.implMedicationOrder1(inst2)
    
    def implMedicationOrder1(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2013-05-25T19:32:52+01:00").date)
        self.assertEqual(inst.dateWritten.as_json(), "2013-05-25T19:32:52+01:00")
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.code, "d")
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.system, "urn:oid:2.16.840.1.113883.6.8")
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.unit, "days")
        self.assertEqual(inst.dispenseRequest.expectedSupplyDuration.value, 40)
        self.assertEqual(inst.dispenseRequest.numberOfRepeatsAllowed, 20)
        self.assertEqual(inst.dispenseRequest.quantity.code, "ug")
        self.assertEqual(inst.dispenseRequest.quantity.system, "urn:oid:2.16.840.1.113883.6.8")
        self.assertEqual(inst.dispenseRequest.quantity.unit, "mcg")
        self.assertEqual(inst.dispenseRequest.quantity.value, 100)
        self.assertEqual(inst.dispenseRequest.validityPeriod.end.date, FHIRDate("2013-05-30").date)
        self.assertEqual(inst.dispenseRequest.validityPeriod.end.as_json(), "2013-05-30")
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2013-04-08").date)
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.as_json(), "2013-04-08")
        self.assertEqual(inst.dosageInstruction[0].additionalInstructions.text, "for use during pregnancy, contact physician")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.code, "ml")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.unit, "ml")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.value, 10)
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].code, "394899003")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].display, "oral administration of treatment")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].code, "181220002")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].display, "Entire oral cavity")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].text, "3 tot 4 maal daags 1 flacon")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.end.date, FHIRDate("2013-11-05").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.end.as_json(), "2013-11-05")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.date, FHIRDate("2013-08-04").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.as_json(), "2013-08-04")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 3)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.periodUnits, "d")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc/portal/prescriptions")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "order9837293")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].code, "13645005")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].display, "Chronic obstructive pulmonary disease")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedicationOrder2(self):
        inst = self.instantiate_from("medicationorder-example-f002-crestor.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationOrder instance")
        self.implMedicationOrder2(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationOrder", js["resourceType"])
        inst2 = medicationorder.MedicationOrder(js)
        self.implMedicationOrder2(inst2)
    
    def implMedicationOrder2(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2013-04-08").date)
        self.assertEqual(inst.dateWritten.as_json(), "2013-04-08")
        self.assertEqual(inst.dispenseRequest.quantity.code, "46992007")
        self.assertEqual(inst.dispenseRequest.quantity.system, "http://snomed.info/sct")
        self.assertEqual(inst.dispenseRequest.quantity.value, 90)
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2013-04-08").date)
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.as_json(), "2013-04-08")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.code, "mg")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.unit, "mg")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.value, 10)
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].code, "386359008")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].display, "Administration of drug or medicament via oral route")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].code, "181220002")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].display, "Entire oral cavity")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.date, FHIRDate("2013-08-04").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.as_json(), "2013-08-04")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.periodUnits, "d")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/portal/prescriptions")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "order9837343")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].code, "28036006")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].display, "High density lipoprotein cholesterol level")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedicationOrder3(self):
        inst = self.instantiate_from("medicationorder-example-f003-tolbutamide.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationOrder instance")
        self.implMedicationOrder3(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationOrder", js["resourceType"])
        inst2 = medicationorder.MedicationOrder(js)
        self.implMedicationOrder3(inst2)
    
    def implMedicationOrder3(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2011-05-01").date)
        self.assertEqual(inst.dateWritten.as_json(), "2011-05-01")
        self.assertEqual(inst.dispenseRequest.quantity.code, "46992007")
        self.assertEqual(inst.dispenseRequest.quantity.system, "http://snomed.info/sct")
        self.assertEqual(inst.dispenseRequest.quantity.value, 90)
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2011-05-01").date)
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.as_json(), "2011-05-01")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.code, "mg")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.unit, "mg")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.value, 500)
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].code, "386359008")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].display, "Administration of drug or medicament via oral route")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].code, "181220002")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].display, "Entire oral cavity")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.date, FHIRDate("2011-05-01").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.as_json(), "2011-05-01")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 3)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.periodUnits, "d")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/portal/prescriptions")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "order9845343")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].code, "444780001")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].display, "High glucose level in blood")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedicationOrder4(self):
        inst = self.instantiate_from("medicationorder-example-f004-metoprolol.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationOrder instance")
        self.implMedicationOrder4(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationOrder", js["resourceType"])
        inst2 = medicationorder.MedicationOrder(js)
        self.implMedicationOrder4(inst2)
    
    def implMedicationOrder4(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2011-05-01").date)
        self.assertEqual(inst.dateWritten.as_json(), "2011-05-01")
        self.assertEqual(inst.dispenseRequest.quantity.code, "46992007")
        self.assertEqual(inst.dispenseRequest.quantity.system, "http://snomed.info/sct")
        self.assertEqual(inst.dispenseRequest.quantity.value, 90)
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2011-05-01").date)
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.as_json(), "2011-05-01")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.code, "mg")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.unit, "mg")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.value, 50)
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].code, "386359008")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].display, "Administration of drug or medicament via oral route")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].code, "181220002")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].display, "Entire oral cavity")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.date, FHIRDate("2011-05-01").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.as_json(), "2011-05-01")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.periodUnits, "d")
        self.assertEqual(inst.id, "f004")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/portal/prescriptions")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "order9845343")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].code, "38341003")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].display, "High blood pressure")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedicationOrder5(self):
        inst = self.instantiate_from("medicationorder-example-f005-enalapril.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationOrder instance")
        self.implMedicationOrder5(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationOrder", js["resourceType"])
        inst2 = medicationorder.MedicationOrder(js)
        self.implMedicationOrder5(inst2)
    
    def implMedicationOrder5(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2011-05-01").date)
        self.assertEqual(inst.dateWritten.as_json(), "2011-05-01")
        self.assertEqual(inst.dispenseRequest.quantity.code, "46992007")
        self.assertEqual(inst.dispenseRequest.quantity.system, "http://snomed.info/sct")
        self.assertEqual(inst.dispenseRequest.quantity.value, 28)
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.date, FHIRDate("2011-05-01").date)
        self.assertEqual(inst.dispenseRequest.validityPeriod.start.as_json(), "2011-05-01")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.code, "mg")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.unit, "mg")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.value, 5)
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].code, "386359008")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].display, "Administration of drug or medicament via oral route")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].code, "181220002")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].display, "Entire oral cavity")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.date, FHIRDate("2011-05-01").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.as_json(), "2011-05-01")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.periodUnits, "d")
        self.assertEqual(inst.id, "f005")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/portal/prescriptions")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "order9823343")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].code, "38341003")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].display, "High blood pressure")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedicationOrder6(self):
        inst = self.instantiate_from("medicationorder-example-f201-salmeterol.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationOrder instance")
        self.implMedicationOrder6(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationOrder", js["resourceType"])
        inst2 = medicationorder.MedicationOrder(js)
        self.implMedicationOrder6(inst2)
    
    def implMedicationOrder6(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.dateWritten.as_json(), "2013-03-11")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.code, "PUFF")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.system, "http://hl7.org/fhir/v3/orderableDrugForm")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.value, 1)
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.code, "259032004")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.unit, "daily")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.value, 1)
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.code, "415215001")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.unit, "puffs")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.value, 2)
        self.assertEqual(inst.dosageInstruction[0].method.coding[0].code, "320276009")
        self.assertEqual(inst.dosageInstruction[0].method.coding[0].display, "Salmeterol+fluticasone 25/250ug inhaler")
        self.assertEqual(inst.dosageInstruction[0].method.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].code, "321667001")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].display, "Respiratory tract")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].code, "74262004")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].display, "Oral cavity")
        self.assertEqual(inst.dosageInstruction[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].text, "aerosol 25/250ug/do 120do 2x - 1 dose - daily")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.end.date, FHIRDate("2013-05-11").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.end.as_json(), "2013-05-11")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.as_json(), "2013-03-11")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 2)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.periodUnits, "d")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedicationOrder7(self):
        inst = self.instantiate_from("medicationorder-example-f202-flucloxacilline.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationOrder instance")
        self.implMedicationOrder7(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationOrder", js["resourceType"])
        inst2 = medicationorder.MedicationOrder(js)
        self.implMedicationOrder7(inst2)
    
    def implMedicationOrder7(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.dateWritten.as_json(), "2013-03-11")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.code, "258702006")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.unit, "hours")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.value, 24)
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.code, "258682000")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.unit, "gram")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.value, 12)
        self.assertEqual(inst.dosageInstruction[0].method.coding[0].code, "323493005")
        self.assertEqual(inst.dosageInstruction[0].method.coding[0].display, "Injected floxacillin")
        self.assertEqual(inst.dosageInstruction[0].method.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].code, "47625008")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].display, "Intravenous route")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].text, "Flucloxacilline 12g/24h")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.end.date, FHIRDate("2013-03-21").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.end.as_json(), "2013-03-21")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.boundsPeriod.start.as_json(), "2013-03-11")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedicationOrder8(self):
        inst = self.instantiate_from("medicationorder-example-f203-paracetamol.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationOrder instance")
        self.implMedicationOrder8(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationOrder", js["resourceType"])
        inst2 = medicationorder.MedicationOrder(js)
        self.implMedicationOrder8(inst2)
    
    def implMedicationOrder8(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2013-04-04").date)
        self.assertEqual(inst.dateWritten.as_json(), "2013-04-04")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.code, "258702006")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.unit, "hours")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.denominator.value, 24)
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.code, "258684004")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.unit, "milligram")
        self.assertEqual(inst.dosageInstruction[0].maxDosePerPeriod.numerator.value, 3000)
        self.assertEqual(inst.dosageInstruction[0].method.coding[0].code, "322236009")
        self.assertEqual(inst.dosageInstruction[0].method.coding[0].display, "Paracetamol 500mg tablet")
        self.assertEqual(inst.dosageInstruction[0].method.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].text, "Paracetamol 3xdaags 1000mg")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

