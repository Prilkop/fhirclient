#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Claim) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """
    
    resource_type = "Claim"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ institutional | oral | pharmacy | professional | vision.
        Type `str`. """
        
        self.identifier = None
        """ Claim number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Current specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.target = None
        """ Insurer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible provider.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.use = None
        """ complete | proposed | exploratory | other.
        Type `str`. """
        
        self.priority = None
        """ Desired processing priority.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.fundsReserve = None
        """ Funds requested to be reserved.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.enterer = None
        """ Author.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility = None
        """ Servicing Facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.prescription = None
        """ Prescription.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.originalPrescription = None
        """ Original Prescription.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Payee.
        Type `ClaimPayee` (represented as `dict` in JSON). """
        
        self.referral = None
        """ Treatment Referral.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.diagnosis = None
        """ Diagnosis.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ List of presenting Conditions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ The subject of the Products and Services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance or medical plan.
        List of `ClaimCoverage` items (represented as `dict` in JSON). """
        
        self.exception = None
        """ Eligibility exceptions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.school = None
        """ Name of School.
        Type `str`. """
        
        self.accident = None
        """ Accident Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.accidentType = None
        """ Accident Type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.interventionException = None
        """ Intervention and exception code (Pharma).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Goods and Services.
        List of `ClaimItem` items (represented as `dict` in JSON). """
        
        self.additionalMaterials = None
        """ Additional materials, documents, etc..
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.missingTeeth = None
        """ Only if type = oral.
        List of `ClaimMissingTeeth` items (represented as `dict` in JSON). """
        
        super(Claim, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("use", "use", str, False, None, False),
            ("priority", "priority", coding.Coding, False, None, False),
            ("fundsReserve", "fundsReserve", coding.Coding, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("condition", "condition", coding.Coding, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("coverage", "coverage", ClaimCoverage, True, None, False),
            ("exception", "exception", coding.Coding, True, None, False),
            ("school", "school", str, False, None, False),
            ("accident", "accident", fhirdate.FHIRDate, False, None, False),
            ("accidentType", "accidentType", coding.Coding, False, None, False),
            ("interventionException", "interventionException", coding.Coding, True, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("additionalMaterials", "additionalMaterials", coding.Coding, True, None, False),
            ("missingTeeth", "missingTeeth", ClaimMissingTeeth, True, None, False),
        ])
        return js


from . import backboneelement

class ClaimCoverage(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Service instance identifier.
        Type `int`. """
        
        self.focal = None
        """ The focal Coverage.
        Type `bool`. """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.businessArrangement = None
        """ Business agreement.
        Type `str`. """
        
        self.relationship = None
        """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        self.claimResponse = None
        """ Adjudication results.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimCoverage, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("relationship", "relationship", coding.Coding, False, None, True),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
        ])
        return js


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Diagnosis.
    
    Ordered list of patient diagnosis for which care is sought.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Sequence of diagnosis.
        Type `int`. """
        
        self.diagnosis = None
        """ Patient's list of diagnosis.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("diagnosis", "diagnosis", coding.Coding, False, None, True),
        ])
        return js


class ClaimItem(backboneelement.BackboneElement):
    """ Goods and Services.
    
    First tier of goods and services.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.type = None
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.diagnosisLinkId = None
        """ Diagnosis Link.
        List of `int` items. """
        
        self.service = None
        """ Item Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.serviceDate = None
        """ Date of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.net = None
        """ Total item cost.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Service Location.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subSite = None
        """ Service Sub-location.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Additional items.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """
        
        self.prosthesis = None
        """ Prosthetic details.
        Type `ClaimItemProsthesis` (represented as `dict` in JSON). """
        
        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("diagnosisLinkId", "diagnosisLinkId", int, True, None, False),
            ("service", "service", coding.Coding, False, None, True),
            ("serviceDate", "serviceDate", fhirdate.FHIRDate, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("points", "points", float, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("udi", "udi", coding.Coding, False, None, False),
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("subSite", "subSite", coding.Coding, True, None, False),
            ("modifier", "modifier", coding.Coding, True, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
            ("prosthesis", "prosthesis", ClaimItemProsthesis, False, None, False),
        ])
        return js


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second tier of goods and services.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.type = None
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.service = None
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.net = None
        """ Total additional item cost.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subDetail = None
        """ Additional items.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("points", "points", float, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("udi", "udi", coding.Coding, False, None, False),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
        ])
        return js


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third tier of goods and services.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.type = None
        """ Type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.service = None
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.net = None
        """ Net additional item cost.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("points", "points", float, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("udi", "udi", coding.Coding, False, None, False),
        ])
        return js


class ClaimItemProsthesis(backboneelement.BackboneElement):
    """ Prosthetic details.
    
    The materials and placement date of prior fixed prosthesis.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.initial = None
        """ Is this the initial service.
        Type `bool`. """
        
        self.priorDate = None
        """ Initial service Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.priorMaterial = None
        """ Prosthetic Material.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimItemProsthesis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemProsthesis, self).elementProperties()
        js.extend([
            ("initial", "initial", bool, False, None, False),
            ("priorDate", "priorDate", fhirdate.FHIRDate, False, None, False),
            ("priorMaterial", "priorMaterial", coding.Coding, False, None, False),
        ])
        return js


class ClaimMissingTeeth(backboneelement.BackboneElement):
    """ Only if type = oral.
    
    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.tooth = None
        """ Tooth Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Reason for missing.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.extractionDate = None
        """ Date of Extraction.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ClaimMissingTeeth, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimMissingTeeth, self).elementProperties()
        js.extend([
            ("tooth", "tooth", coding.Coding, False, None, True),
            ("reason", "reason", coding.Coding, False, None, False),
            ("extractionDate", "extractionDate", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class ClaimPayee(backboneelement.BackboneElement):
    """ Payee.
    
    The party to be reimbursed for the services.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Party to be paid any benefits payable.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Provider who is the payee.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Organization who is the payee.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.person = None
        """ Other person who is the payee.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("person", "person", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
