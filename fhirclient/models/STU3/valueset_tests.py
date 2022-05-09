#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 on 2022-05-29.
#  2022, SMART Health IT.


import os
import io
import unittest
import json
from . import valueset
from .fhirdate import FHIRDate


class ValueSetTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ValueSet", js["resourceType"])
        return valueset.ValueSet(js)
    
    def testValueSet1(self):
        inst = self.instantiate_from("valueset-valueset-list-example-codes(list-example-codes).json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet1(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet1(inst2)
    
    def implValueSet1(self, inst):
        self.assertEqual(inst.compose.include[0].system, "http://hl7.org/fhir/list-example-use-codes")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2019-10-24T11:53:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2019-10-24T11:53:00+11:00")
        self.assertEqual(inst.description, "Example use codes for the List resource - typical kinds of use.")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-ballot-status")
        self.assertEqual(inst.extension[0].valueString, "Informative")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm")
        self.assertEqual(inst.extension[1].valueInteger, 1)
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg")
        self.assertEqual(inst.extension[2].valueCode, "fhir")
        self.assertEqual(inst.id, "list-example-codes")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:2.16.840.1.113883.4.642.3.307")
        self.assertTrue(inst.immutable)
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2019-10-24T11:53:00+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2019-10-24T11:53:00+11:00")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/shareablevalueset")
        self.assertEqual(inst.name, "Example Use Codes for List")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ValueSet/list-example-codes")
        self.assertEqual(inst.version, "3.0.2")

