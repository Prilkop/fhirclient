#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/EligibilityResponse) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class EligibilityResponse(domainresource.DomainResource):
    """ EligibilityResponse resource.
    
    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """
    
    resource_type = "EligibilityResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.request = None
        """ Eligibility reference.
        Type `FHIRReference` referencing `EligibilityRequest` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error | partial.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.insurer = None
        """ Insurer issuing the coverage.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.inforce = None
        """ Coverage inforce indicator.
        Type `bool`. """
        
        self.insurance = None
        """ Details by insurance coverage.
        List of `EligibilityResponseInsurance` items (represented as `dict` in JSON). """
        
        self.form = None
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.error = None
        """ Processing errors.
        List of `EligibilityResponseError` items (represented as `dict` in JSON). """
        
        super(EligibilityResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", str, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("inforce", "inforce", bool, False, None, False),
            ("insurance", "insurance", EligibilityResponseInsurance, True, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("error", "error", EligibilityResponseError, True, None, False),
        ])
        return js


from . import backboneelement

class EligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Mutually exclusive with Services Provided (Item).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EligibilityResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class EligibilityResponseInsurance(backboneelement.BackboneElement):
    """ Details by insurance coverage.
    
    The insurer may provide both the details for the requested coverage as well
    as details for additional coverages known to the insurer.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        """ Updated Coverage details.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.contract = None
        """ Contract details.
        Type `FHIRReference` referencing `Contract` (represented as `dict` in JSON). """
        
        self.benefitBalance = None
        """ Benefits by Category.
        List of `EligibilityResponseInsuranceBenefitBalance` items (represented as `dict` in JSON). """
        
        super(EligibilityResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseInsurance, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
            ("contract", "contract", fhirreference.FHIRReference, False, None, False),
            ("benefitBalance", "benefitBalance", EligibilityResponseInsuranceBenefitBalance, True, None, False),
        ])
        return js


class EligibilityResponseInsuranceBenefitBalance(backboneelement.BackboneElement):
    """ Benefits by Category.
    
    Benefits and optionally current balances by Category.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Type of services covered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subCategory = None
        """ Detailed services covered within the type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.excluded = None
        """ Excluded from the plan.
        Type `bool`. """
        
        self.name = None
        """ Short name for the benefit.
        Type `str`. """
        
        self.description = None
        """ Description of the benefit or services covered.
        Type `str`. """
        
        self.network = None
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.term = None
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.financial = None
        """ Benefit Summary.
        List of `EligibilityResponseInsuranceBenefitBalanceFinancial` items (represented as `dict` in JSON). """
        
        super(EligibilityResponseInsuranceBenefitBalance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseInsuranceBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("subCategory", "subCategory", codeableconcept.CodeableConcept, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("financial", "financial", EligibilityResponseInsuranceBenefitBalanceFinancial, True, None, False),
        ])
        return js


class EligibilityResponseInsuranceBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits Used to date.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Deductable, visits, benefit amount.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.allowedUnsignedInt = None
        """ Benefits allowed.
        Type `int`. """
        
        self.allowedString = None
        """ Benefits allowed.
        Type `str`. """
        
        self.allowedMoney = None
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """
        
        self.usedUnsignedInt = None
        """ Benefits used.
        Type `int`. """
        
        self.usedMoney = None
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """
        
        super(EligibilityResponseInsuranceBenefitBalanceFinancial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseInsuranceBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
            ("usedMoney", "usedMoney", money.Money, False, "used", False),
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
