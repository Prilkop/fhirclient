#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Device) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class Device(domainresource.DomainResource):
    """ An instance of a manufactured te that is used in the provision of
    healthcare.
    
    This resource identifies an instance of a manufactured item that is used in
    the provision of healthcare without being substantially changed through
    that activity. The device may be a medical or non-medical device.  Medical
    devices includes durable (reusable) medical equipment, implantable devices,
    as well as disposable equipment used for diagnostic, treatment, and
    research for healthcare and public health.  Non-medical devices may include
    items such as a machine, cellphone, computer, application, etc.
    """
    
    resource_type = "Device"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Instance id from manufacturer, owner, and others.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of device this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None
        """ Device notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.status = None
        """ available | not-available | entered-in-error.
        Type `str`. """
        
        self.manufacturer = None
        """ Name of device manufacturer.
        Type `str`. """
        
        self.model = None
        """ Model id assigned by the manufacturer.
        Type `str`. """
        
        self.version = None
        """ Version number (i.e. software).
        Type `str`. """
        
        self.manufactureDate = None
        """ Manufacture date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.expiry = None
        """ Date and time of expiry of this device (if applicable).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.udi = None
        """ FDA mandated Unique Device Identifier.
        Type `str`. """
        
        self.lotNumber = None
        """ Lot number of manufacture.
        Type `str`. """
        
        self.owner = None
        """ Organization responsible for device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the resource is found.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient = None
        """ If the resource is affixed to a person.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Network address to contact device.
        Type `str`. """
        
        super(Device, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("status", "status", str, False, None, False),
            ("manufacturer", "manufacturer", str, False, None, False),
            ("model", "model", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("manufactureDate", "manufactureDate", fhirdate.FHIRDate, False, None, False),
            ("expiry", "expiry", fhirdate.FHIRDate, False, None, False),
            ("udi", "udi", str, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
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
