#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.
    
    This resource provides payment details and claim references supporting a
    bulk payment.
    """
    
    resource_type = "PaymentReconciliation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.request = None
        """ Claim reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error.
        Type `str`. """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.period = None
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Insurer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Details.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """
        
        self.form = None
        """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.total = None
        """ Total amount of Payment.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.note = None
        """ Note text.
        List of `PaymentReconciliationNote` items (represented as `dict` in JSON). """
        
        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False, None, False),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("form", "form", coding.Coding, False, None, False),
            ("total", "total", quantity.Quantity, False, None, True),
            ("note", "note", PaymentReconciliationNote, True, None, False),
        ])
        return js


from . import backboneelement

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ Details.
    
    List of individual settlement amounts and the corresponding transaction.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Type code.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.request = None
        """ Claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.responce = None
        """ Claim Response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.submitter = None
        """ Submitter.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Payee.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ Invoice date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.amount = None
        """ Detail amount.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("responce", "responce", fhirreference.FHIRReference, False, None, False),
            ("submitter", "submitter", fhirreference.FHIRReference, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("amount", "amount", quantity.Quantity, False, None, False),
        ])
        return js


class PaymentReconciliationNote(backboneelement.BackboneElement):
    """ Note text.
    
    Suite of notes.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.text = None
        """ Notes text.
        Type `str`. """
        
        super(PaymentReconciliationNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationNote, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, False),
            ("text", "text", str, False, None, False),
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
