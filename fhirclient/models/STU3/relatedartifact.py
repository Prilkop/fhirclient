#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/RelatedArtifact) on 2022-05-29.
#  2022, SMART Health IT.


from . import element

class RelatedArtifact(element.Element):
    """ Related artifacts for a knowledge resource.
    
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ documentation | justification | citation | predecessor | successor
        | derived-from | depends-on | composed-of.
        Type `str`. """
        
        self.display = None
        """ Brief description of the related artifact.
        Type `str`. """
        
        self.citation = None
        """ Bibliographic citation for the artifact.
        Type `str`. """
        
        self.url = None
        """ Where the artifact can be accessed.
        Type `str`. """
        
        self.document = None
        """ What document is being referenced.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.resource = None
        """ What resource is being referenced.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(RelatedArtifact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedArtifact, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("display", "display", str, False, None, False),
            ("citation", "citation", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("document", "document", attachment.Attachment, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
