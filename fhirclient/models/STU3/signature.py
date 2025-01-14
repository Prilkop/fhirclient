#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Signature) on 2022-05-29.
#  2022, SMART Health IT.


from . import element

class Signature(element.Element):
    """ A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..
    
    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different signature
    approaches have different utilities.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.when = None
        """ When the signature was created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.whoUri = None
        """ Who signed.
        Type `str`. """
        
        self.whoReference = None
        """ Who signed.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device, Organization` (represented as `dict` in JSON). """
        
        self.onBehalfOfUri = None
        """ The party represented.
        Type `str`. """
        
        self.onBehalfOfReference = None
        """ The party represented.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device, Organization` (represented as `dict` in JSON). """
        
        self.contentType = None
        """ The technical format of the signature.
        Type `str`. """
        
        self.blob = None
        """ The actual signature content (XML DigSig. JWT, picture, etc.).
        Type `str`. """
        
        super(Signature, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, True, None, True),
            ("when", "when", fhirdate.FHIRDate, False, None, True),
            ("whoUri", "whoUri", str, False, "who", True),
            ("whoReference", "whoReference", fhirreference.FHIRReference, False, "who", True),
            ("onBehalfOfUri", "onBehalfOfUri", str, False, "onBehalfOf", False),
            ("onBehalfOfReference", "onBehalfOfReference", fhirreference.FHIRReference, False, "onBehalfOf", False),
            ("contentType", "contentType", str, False, None, False),
            ("blob", "blob", str, False, None, False),
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
