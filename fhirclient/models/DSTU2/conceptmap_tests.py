#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2022-05-29.
#  2022, SMART Health IT.


import os
import io
import unittest
import json
from . import conceptmap
from .fhirdate import FHIRDate


class ConceptMapTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ConceptMap", js["resourceType"])
        return conceptmap.ConceptMap(js)
    
    def testConceptMap1(self):
        inst = self.instantiate_from("conceptmap-example-specimen-type.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap1(inst)
        
        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap1(inst2)
    
    def implConceptMap1(self, inst):
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.contact[1].telecom[0].system, "other")
        self.assertEqual(inst.contact[1].telecom[0].value, "http://www.phconnect.org/group/laboratorymessagingcommunityofpractice/forum/attachment/download?id=3649725%3AUploadedFile%3A145786")
        self.assertEqual(inst.date.date, FHIRDate("2013-07-25").date)
        self.assertEqual(inst.date.as_json(), "2013-07-25")
        self.assertEqual(inst.element[0].code, "ACNE")
        self.assertEqual(inst.element[0].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[0].target[0].code, "309068002")
        self.assertEqual(inst.element[0].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[0].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[1].code, "ACNFLD")
        self.assertEqual(inst.element[1].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[1].target[0].code, "119323008")
        self.assertEqual(inst.element[1].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[1].target[0].comments, "HL7 term is a historical term. mapped to Pus")
        self.assertEqual(inst.element[1].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[1].target[0].product[0].code, "47002008")
        self.assertEqual(inst.element[1].target[0].product[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[1].target[0].product[0].element, "http://hl7.org/fhir/v2/element/SPM-5")
        self.assertEqual(inst.element[2].code, "AIRS")
        self.assertEqual(inst.element[2].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[2].target[0].code, "446302006")
        self.assertEqual(inst.element[2].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[2].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[3].code, "ALL")
        self.assertEqual(inst.element[3].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[3].target[0].code, "119376003")
        self.assertEqual(inst.element[3].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[3].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[3].target[0].product[0].code, "7970006")
        self.assertEqual(inst.element[3].target[0].product[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[3].target[0].product[0].element, "http://hl7.org/fhir/v2/element/SPM-5")
        self.assertEqual(inst.element[4].code, "AMP")
        self.assertEqual(inst.element[4].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[4].target[0].code, "408654003")
        self.assertEqual(inst.element[4].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[4].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[4].target[0].product[0].code, "81723002")
        self.assertEqual(inst.element[4].target[0].product[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[4].target[0].product[0].element, "http://hl7.org/fhir/v2/element/SPM-7")
        self.assertEqual(inst.element[5].code, "ANGI")
        self.assertEqual(inst.element[5].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[5].target[0].code, "119312009")
        self.assertEqual(inst.element[5].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[5].target[0].comments, "TBD in detail")
        self.assertEqual(inst.element[5].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[6].code, "ARTC")
        self.assertEqual(inst.element[6].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[6].target[0].code, "119312009")
        self.assertEqual(inst.element[6].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[6].target[0].comments, "TBD in detail")
        self.assertEqual(inst.element[6].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[7].code, "ASERU")
        self.assertEqual(inst.element[7].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[7].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[7].target[0].comments, "pending")
        self.assertEqual(inst.element[7].target[0].equivalence, "unmatched")
        self.assertEqual(inst.element[8].code, "ASP")
        self.assertEqual(inst.element[8].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[8].target[0].code, "119295008")
        self.assertEqual(inst.element[8].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[8].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[8].target[0].product[0].code, "14766002")
        self.assertEqual(inst.element[8].target[0].product[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[8].target[0].product[0].element, "http://hl7.org/fhir/v2/element/SPM-7")
        self.assertEqual(inst.element[9].code, "ATTE")
        self.assertEqual(inst.element[9].codeSystem, "http://hl7.org/fhir/v2/0487")
        self.assertEqual(inst.element[9].target[0].codeSystem, "http://snomed.info/sct")
        self.assertEqual(inst.element[9].target[0].comments, "TBD")
        self.assertEqual(inst.element[9].target[0].equivalence, "unmatched")
        self.assertFalse(inst.experimental)
        self.assertEqual(inst.id, "102")
        self.assertEqual(inst.name, "Specimen mapping from v2 table 0487 to SNOMED CT")
        self.assertEqual(inst.publisher, "FHIR project team (original source: LabMCoP)")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ConceptMap/102")
        self.assertEqual(inst.version, "20130725")
    
    def testConceptMap2(self):
        inst = self.instantiate_from("conceptmap-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap2(inst)
        
        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap2(inst2)
    
    def implConceptMap2(self, inst):
        self.assertEqual(inst.contact[0].name, "FHIR project team (example)")
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.copyright, "Creative Commons 0")
        self.assertEqual(inst.date.date, FHIRDate("2012-06-13").date)
        self.assertEqual(inst.date.as_json(), "2012-06-13")
        self.assertEqual(inst.description, "A mapping between the FHIR and HL7 v3 AddressUse Code systems")
        self.assertEqual(inst.element[0].code, "home")
        self.assertEqual(inst.element[0].codeSystem, "http://hl7.org/fhir/address-use")
        self.assertEqual(inst.element[0].target[0].code, "H")
        self.assertEqual(inst.element[0].target[0].codeSystem, "http://hl7.org/fhir/v3/AddressUse")
        self.assertEqual(inst.element[0].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[1].code, "home")
        self.assertEqual(inst.element[1].codeSystem, "http://hl7.org/fhir/address-use")
        self.assertEqual(inst.element[1].target[0].code, "H")
        self.assertEqual(inst.element[1].target[0].codeSystem, "http://hl7.org/fhir/v3/AddressUse")
        self.assertEqual(inst.element[1].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[2].code, "work")
        self.assertEqual(inst.element[2].codeSystem, "http://hl7.org/fhir/address-use")
        self.assertEqual(inst.element[2].target[0].code, "WP")
        self.assertEqual(inst.element[2].target[0].codeSystem, "http://hl7.org/fhir/v3/AddressUse")
        self.assertEqual(inst.element[2].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[3].code, "temp")
        self.assertEqual(inst.element[3].codeSystem, "http://hl7.org/fhir/address-use")
        self.assertEqual(inst.element[3].target[0].code, "TMP")
        self.assertEqual(inst.element[3].target[0].codeSystem, "http://hl7.org/fhir/v3/AddressUse")
        self.assertEqual(inst.element[3].target[0].equivalence, "equivalent")
        self.assertEqual(inst.element[4].code, "old")
        self.assertEqual(inst.element[4].codeSystem, "http://hl7.org/fhir/address-use")
        self.assertEqual(inst.element[4].target[0].code, "BAD")
        self.assertEqual(inst.element[4].target[0].codeSystem, "http://hl7.org/fhir/v3/AddressUse")
        self.assertEqual(inst.element[4].target[0].comments, "In the HL7 v3 AD, old is handled by the usablePeriod element, but you have to provide a time, there's no simple equivalent of flagging an address as old")
        self.assertEqual(inst.element[4].target[0].equivalence, "disjoint")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.identifier.system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier.value, "urn:uuid:53cd62ee-033e-414c-9f58-3ca97b5ffc3b")
        self.assertEqual(inst.name, "FHIR/v3 Address Use Mapping")
        self.assertEqual(inst.publisher, "HL7, Inc")
        self.assertEqual(inst.requirements, "To help implementers map from HL7 v3/CDA to FHIR")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ConceptMap/101")
        self.assertEqual(inst.useContext[0].text, "for CDA Usage")
        self.assertEqual(inst.version, "20120613")

