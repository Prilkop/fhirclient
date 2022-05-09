#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ClinicalImpression) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class ClinicalImpression(domainresource.DomainResource):
    """ A clinical assessment performed when planning treatments and management
    strategies for a patient.
    
    A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments are
    often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """
    
    resource_type = "ClinicalImpression"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.patient = None
        """ The patient being assessed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.assessor = None
        """ The clinician performing the assessment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | completed | entered-in-error.
        Type `str`. """
        
        self.date = None
        """ When the assessment occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Why/how the assessment was performed.
        Type `str`. """
        
        self.previous = None
        """ Reference to last assessment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.problem = None
        """ General assessment of patient state.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.triggerCodeableConcept = None
        """ Request or event that necessitated this assessment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.triggerReference = None
        """ Request or event that necessitated this assessment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.investigations = None
        """ One or more sets of investigations (signs, symptions, etc.).
        List of `ClinicalImpressionInvestigations` items (represented as `dict` in JSON). """
        
        self.protocol = None
        """ Clinical Protocol followed.
        Type `str`. """
        
        self.summary = None
        """ Summary of the assessment.
        Type `str`. """
        
        self.finding = None
        """ Possible or likely findings and diagnoses.
        List of `ClinicalImpressionFinding` items (represented as `dict` in JSON). """
        
        self.resolved = None
        """ Diagnoses/conditions resolved since previous assessment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.ruledOut = None
        """ Diagnosis considered not possible.
        List of `ClinicalImpressionRuledOut` items (represented as `dict` in JSON). """
        
        self.prognosis = None
        """ Estimate of likely outcome.
        Type `str`. """
        
        self.plan = None
        """ Plan of action after assessment.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.action = None
        """ Actions taken during assessment.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ClinicalImpression, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpression, self).elementProperties()
        js.extend([
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("assessor", "assessor", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("previous", "previous", fhirreference.FHIRReference, False, None, False),
            ("problem", "problem", fhirreference.FHIRReference, True, None, False),
            ("triggerCodeableConcept", "triggerCodeableConcept", codeableconcept.CodeableConcept, False, "trigger", False),
            ("triggerReference", "triggerReference", fhirreference.FHIRReference, False, "trigger", False),
            ("investigations", "investigations", ClinicalImpressionInvestigations, True, None, False),
            ("protocol", "protocol", str, False, None, False),
            ("summary", "summary", str, False, None, False),
            ("finding", "finding", ClinicalImpressionFinding, True, None, False),
            ("resolved", "resolved", codeableconcept.CodeableConcept, True, None, False),
            ("ruledOut", "ruledOut", ClinicalImpressionRuledOut, True, None, False),
            ("prognosis", "prognosis", str, False, None, False),
            ("plan", "plan", fhirreference.FHIRReference, True, None, False),
            ("action", "action", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class ClinicalImpressionFinding(backboneelement.BackboneElement):
    """ Possible or likely findings and diagnoses.
    
    Specific findings or diagnoses that was considered likely or relevant to
    ongoing treatment.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.item = None
        """ Specific text or code for finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.cause = None
        """ Which investigations support finding.
        Type `str`. """
        
        super(ClinicalImpressionFinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionFinding, self).elementProperties()
        js.extend([
            ("item", "item", codeableconcept.CodeableConcept, False, None, True),
            ("cause", "cause", str, False, None, False),
        ])
        return js


class ClinicalImpressionInvestigations(backboneelement.BackboneElement):
    """ One or more sets of investigations (signs, symptions, etc.).
    
    One or more sets of investigations (signs, symptions, etc.). The actual
    grouping of investigations vary greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ A name/code for the set.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.item = None
        """ Record of a specific investigation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ClinicalImpressionInvestigations, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionInvestigations, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("item", "item", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ClinicalImpressionRuledOut(backboneelement.BackboneElement):
    """ Diagnosis considered not possible.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.item = None
        """ Specific text of code for diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Grounds for elimination.
        Type `str`. """
        
        super(ClinicalImpressionRuledOut, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionRuledOut, self).elementProperties()
        js.extend([
            ("item", "item", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", str, False, None, False),
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
