#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.
    
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    
    resource_type = "MedicationAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """
        
        self.patient = None
        """ Who received medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.practitioner = None
        """ Who administered substance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter administered as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.prescription = None
        """ Order administration performed against.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.wasNotGiven = None
        """ True if medication not administered.
        Type `bool`. """
        
        self.reasonNotGiven = None
        """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonGiven = None
        """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.effectiveTimeDateTime = None
        """ Start and end time of administration.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectiveTimePeriod = None
        """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ What was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ What was administered.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.device = None
        """ Device used to administer.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Information about the administration.
        Type `str`. """
        
        self.dosage = None
        """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """
        
        super(MedicationAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("practitioner", "practitioner", fhirreference.FHIRReference, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("wasNotGiven", "wasNotGiven", bool, False, None, False),
            ("reasonNotGiven", "reasonNotGiven", codeableconcept.CodeableConcept, True, None, False),
            ("reasonGiven", "reasonGiven", codeableconcept.CodeableConcept, True, None, False),
            ("effectiveTimeDateTime", "effectiveTimeDateTime", fhirdate.FHIRDate, False, "effectiveTime", True),
            ("effectiveTimePeriod", "effectiveTimePeriod", period.Period, False, "effectiveTime", True),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("note", "note", str, False, None, False),
            ("dosage", "dosage", MedicationAdministrationDosage, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.
    
    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        """ Dosage Instructions.
        Type `str`. """
        
        self.siteCodeableConcept = None
        """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Body site administered to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.route = None
        """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.method = None
        """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount administered in one dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.rateRange = None
        """ Dose quantity per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        
        super(MedicationAdministrationDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("siteCodeableConcept", "siteCodeableConcept", codeableconcept.CodeableConcept, False, "site", False),
            ("siteReference", "siteReference", fhirreference.FHIRReference, False, "site", False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
