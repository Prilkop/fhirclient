#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.
    
    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    
    resource_type = "PaymentNotice"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.target = None
        """ Insurer or Regulatory body.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.paymentStatus = None
        """ Status of the payment.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(PaymentNotice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("paymentStatus", "paymentStatus", coding.Coding, False, None, True),
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
