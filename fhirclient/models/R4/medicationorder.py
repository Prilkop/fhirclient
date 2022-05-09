#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationOrder) on 2022-04-28.
#  2022, SMART Health IT.


from . import domainresource

class MedicationOrder(domainresource.DomainResource):
    """ Prescription of medication to for patient.
    
    An order for both supply of the medication and the instructions for
    administration of the medication to a patient. The resource is called
    "MedicationOrder" rather than "MedicationPrescription" to generalize the
    use across inpatient and outpatient settings as well as for care plans,
    etc.
    """
    
    resource_type = "MedicationOrder"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ active | on-hold | completed | entered-in-error | stopped | draft.
        Type `str`. """
        
        self.dateEnded = None
        """ When prescription was stopped.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reasonEnded = None
        """ Why prescription was stopped.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.prescriber = None
        """ Who ordered the medication(s).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Created during encounter/admission/stay.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason or indication for writing the prescription.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note = None
        """ Information about the prescription.
        Type `str`. """
        
        self.medicationCodeableConcept = None
        """ Medication to be taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ Medication to be taken.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.dosageInstruction = None
        """ How medication should be taken.
        List of `MedicationOrderDosageInstruction` items (represented as `dict` in JSON). """
        
        self.dispenseRequest = None
        """ Medication supply authorization.
        Type `MedicationOrderDispenseRequest` (represented as `dict` in JSON). """
        
        self.substitution = None
        """ Any restrictions on medication substitution.
        Type `MedicationOrderSubstitution` (represented as `dict` in JSON). """
        
        self.priorPrescription = None
        """ An order/prescription that this supersedes.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MedicationOrder, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationOrder, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False, None, False),
            ("status", "status", MedicationOrderStatus.str, False, None, False),
            ("dateEnded", "dateEnded", fhirdate.FHIRDate, False, None, False),
            ("reasonEnded", "reasonEnded", codeableconcept.CodeableConcept, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False, "reason", False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, "reason", False),
            ("note", "note", str, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("dosageInstruction", "dosageInstruction", MedicationOrderDosageInstruction, True, None, False),
            ("dispenseRequest", "dispenseRequest", MedicationOrderDispenseRequest, False, None, False),
            ("substitution", "substitution", MedicationOrderSubstitution, False, None, False),
            ("priorPrescription", "priorPrescription", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationOrderDispenseRequest(backboneelement.BackboneElement):
    """ Medication supply authorization.
    
    Indicates the specific details for the dispense or medication supply part
    of a medication order (also known as a Medication Prescription).  Note that
    this information is NOT always sent with the order.  There may be in some
    settings (e.g. hospitals) institutional or system support for completing
    the dispense details in the pharmacy department.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.medicationCodeableConcept = None
        """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ Product to be supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.validityPeriod = None
        """ Time period supply is authorized for.
        Type `Period` (represented as `dict` in JSON). """
        
        self.numberOfRepeatsAllowed = None
        """ Number of refills authorized.
        Type `int`. """
        
        self.quantity = None
        """ Amount of medication to supply per dispense.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.expectedSupplyDuration = None
        """ Number of days supply per dispense.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(MedicationOrderDispenseRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationOrderDispenseRequest, self).elementProperties()
        js.extend([
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", False),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
            ("numberOfRepeatsAllowed", "numberOfRepeatsAllowed", int, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("expectedSupplyDuration", "expectedSupplyDuration", quantity.Quantity, False, None, False),
        ])
        return js


class MedicationOrderDosageInstruction(backboneelement.BackboneElement):
    """ How medication should be taken.
    
    Indicates how the medication is to be used by the patient.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        """ Dosage instructions expressed as text.
        Type `str`. """
        
        self.additionalInstructions = None
        """ Supplemental instructions - e.g. "with meals".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timing = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.asNeededBoolean = None
        """ Take "as needed" (for x).
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteCodeableConcept = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Body site to administer to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseRange = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
        
        self.doseQuantity = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.rateRange = None
        """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        super(MedicationOrderDosageInstruction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationOrderDosageInstruction, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("additionalInstructions", "additionalInstructions", codeableconcept.CodeableConcept, False, None, False),
            ("timing", "timing", timing.Timing, False, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("siteCodeableConcept", "siteCodeableConcept", codeableconcept.CodeableConcept, False, "site", False),
            ("siteReference", "siteReference", fhirreference.FHIRReference, False, "site", False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("doseRange", "doseRange", range.Range, False, "dose", False),
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, "dose", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False),
        ])
        return js


class MedicationOrderSubstitution(backboneelement.BackboneElement):
    """ Any restrictions on medication substitution.
    
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen, and in others it does not matter. This block
    explains the prescriber's intent. If nothing is specified substitution may
    be done.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ generic | formulary +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Why should (not) substitution be made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationOrderSubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationOrderSubstitution, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import MedicationOrderStatus
except ImportError:
    MedicationOrderStatus = sys.modules[__package__ + '.MedicationOrderStatus']
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
