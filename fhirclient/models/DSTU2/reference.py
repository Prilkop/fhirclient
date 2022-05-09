#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Reference) on 2022-05-29.
#  2022, SMART Health IT.


from . import element

class Reference(element.Element):
    """ A reference from one resource to another.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Relative, internal or absolute URL reference.
        Type `str`. """
        
        self.display = None
        """ Text alternative for the resource.
        Type `str`. """
        
        super(Reference, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Reference, self).elementProperties()
        js.extend([
            ("reference", "reference", str, False, None, False),
            ("display", "display", str, False, None, False),
        ])
        return js


