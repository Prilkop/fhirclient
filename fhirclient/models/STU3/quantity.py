#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Quantity) on 2022-05-29.
#  2022, SMART Health IT.


from . import element

class Quantity(element.Element):
    """ A measured or measurable amount.
    
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.value = None
        """ Numerical value (with implicit precision).
        Type `float`. """
        
        self.comparator = None
        """ < | <= | >= | > - how to understand the value.
        Type `str`. """
        
        self.unit = None
        """ Unit representation.
        Type `str`. """
        
        self.system = None
        """ System that defines coded unit form.
        Type `str`. """
        
        self.code = None
        """ Coded form of the unit.
        Type `str`. """
        
        super(Quantity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Quantity, self).elementProperties()
        js.extend([
            ("value", "value", float, False, None, False),
            ("comparator", "comparator", str, False, None, False),
            ("unit", "unit", str, False, None, False),
            ("system", "system", str, False, None, False),
            ("code", "code", str, False, None, False),
        ])
        return js

