#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationStatement) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class MedicationStatement(domainresource.DomainResource):
    """ Record of medication being taken by a patient.
    
    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now, or has taken the medication in the past or will be taking
    the medication in the future.  The source of this information can be the
    patient, significant other (such as a family member or spouse), or a
    clinician.  A common scenario where this information is captured is during
    the history taking process during a patient visit or stay.   The medication
    information may come from e.g. the patient's memory, from a prescription
    bottle,  or from a list of medications the patient, clinician or other
    party maintains
    
    The primary difference between a medication statement and a medication
    administration is that the medication administration has complete
    administration information and is based on actual administration
    information from the person who administered the medication.  A medication
    statement is often, if not always, less specific.  There is no required
    date/time when the medication was administered, in fact we only know that a
    source has reported the patient is taking this medication, where details
    such as time, quantity, or rate or even medication product may be
    incomplete or missing or less precise.  As stated earlier, the medication
    statement information may come from the patient's memory, from a
    prescription bottle or from a list of medications the patient, clinician or
    other party maintains.  Medication administration is more formal and is not
    missing detailed information.
    """
    
    resource_type = "MedicationStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who is/was taking  the medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.informationSource = None
        """ None.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.dateAsserted = None
        """ When the statement was asserted?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ active | completed | entered-in-error | intended.
        Type `str`. """
        
        self.wasNotTaken = None
        """ True if medication is/was not being taken.
        Type `bool`. """
        
        self.reasonNotTaken = None
        """ True if asserting medication was not given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonForUseCodeableConcept = None
        """ None.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonForUseReference = None
        """ None.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
        """ Over what period was medication consumed?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ Over what period was medication consumed?.
        Type `Period` (represented as `dict` in JSON). """
        
        self.note = None
        """ Further information about the statement.
        Type `str`. """
        
        self.supportingInformation = None
        """ Additional supporting information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ What medication was taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ What medication was taken.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Details of how medication was taken.
        List of `MedicationStatementDosage` items (represented as `dict` in JSON). """
        
        super(MedicationStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationStatement, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("informationSource", "informationSource", fhirreference.FHIRReference, False, None, False),
            ("dateAsserted", "dateAsserted", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("wasNotTaken", "wasNotTaken", bool, False, None, False),
            ("reasonNotTaken", "reasonNotTaken", codeableconcept.CodeableConcept, True, None, False),
            ("reasonForUseCodeableConcept", "reasonForUseCodeableConcept", codeableconcept.CodeableConcept, False, "reasonForUse", False),
            ("reasonForUseReference", "reasonForUseReference", fhirreference.FHIRReference, False, "reasonForUse", False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("note", "note", str, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("dosage", "dosage", MedicationStatementDosage, True, None, False),
        ])
        return js


from . import backboneelement

class MedicationStatementDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.
    
    Indicates how the medication is/was used by the patient.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        """ Reported dosage information.
        Type `str`. """
        
        self.timing = None
        """ When/how often was medication taken.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.asNeededBoolean = None
        """ Take "as needed" (for x).
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteCodeableConcept = None
        """ Where (on body) medication is/was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Where (on body) medication is/was administered.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.route = None
        """ How the medication entered the body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique used to administer medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantityQuantity = None
        """ Amount administered in one dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.quantityRange = None
        """ Amount administered in one dose.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.rateRange = None
        """ Dose quantity per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Maximum dose that was consumed per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        super(MedicationStatementDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationStatementDosage, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("timing", "timing", timing.Timing, False, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("siteCodeableConcept", "siteCodeableConcept", codeableconcept.CodeableConcept, False, "site", False),
            ("siteReference", "siteReference", fhirreference.FHIRReference, False, "site", False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("quantityQuantity", "quantityQuantity", quantity.Quantity, False, "quantity", False),
            ("quantityRange", "quantityRange", range.Range, False, "quantity", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False),
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
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
