#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Narrative) on 2022-05-29.
#  2022, SMART Health IT.


from . import element

class Narrative(element.Element):
    """ A human-readable formatted text, including images.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.status = None
        """ generated | extensions | additional | empty.
        Type `str`. """
        
        self.div = None
        """ Limited xhtml content.
        Type `str`. """
        
        super(Narrative, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Narrative, self).elementProperties()
        js.extend([
            ("status", "status", str, False, None, True),
            ("div", "div", str, False, None, True),
        ])
        return js


