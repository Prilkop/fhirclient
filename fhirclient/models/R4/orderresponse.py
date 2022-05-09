#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/OrderResponse) on 2022-04-28.
#  2022, SMART Health IT.


from . import domainresource

class OrderResponse(domainresource.DomainResource):
    """ A response to an order.
    """
    
    resource_type = "OrderResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.request = None
        """ The order that this is a response to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the response was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.who = None
        """ Who made the response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.orderStatus = None
        """ pending | review | rejected | error | accepted | cancelled |
        replaced | aborted | completed.
        Type `str`. """
        
        self.description = None
        """ Additional description of the response.
        Type `str`. """
        
        self.fulfillment = None
        """ Details of the outcome of performing the order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(OrderResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrderResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
            ("orderStatus", "orderStatus", OrderStatus.str, False, None, True),
            ("description", "description", str, False, None, False),
            ("fulfillment", "fulfillment", fhirreference.FHIRReference, True, None, False),
        ])
        return js


import sys
try:
    from . import OrderStatus
except ImportError:
    OrderStatus = sys.modules[__package__ + '.OrderStatus']
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
