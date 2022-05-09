#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceComponent) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class DeviceComponent(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.
    
    Describes the characteristics, operational status and capabilities of a
    medical-related component of a medical device.
    """
    
    resource_type = "DeviceComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ What kind of component it is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Instance id assigned by the software stack.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.lastSystemChange = None
        """ Recent system change timestamp.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.source = None
        """ A source device of this component.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.parent = None
        """ Parent resource link.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.operationalStatus = None
        """ Component operational status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.parameterGroup = None
        """ Current supported parameter group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.measurementPrinciple = None
        """ other | chemical | electrical | impedance | nuclear | optical |
        thermal | biological | mechanical | acoustical | manual+.
        Type `str`. """
        
        self.productionSpecification = None
        """ Production specification of the component.
        List of `DeviceComponentProductionSpecification` items (represented as `dict` in JSON). """
        
        self.languageCode = None
        """ Language code for the human-readable text strings produced by the
        device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceComponent, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("lastSystemChange", "lastSystemChange", fhirdate.FHIRDate, False, None, True),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("operationalStatus", "operationalStatus", codeableconcept.CodeableConcept, True, None, False),
            ("parameterGroup", "parameterGroup", codeableconcept.CodeableConcept, False, None, False),
            ("measurementPrinciple", "measurementPrinciple", str, False, None, False),
            ("productionSpecification", "productionSpecification", DeviceComponentProductionSpecification, True, None, False),
            ("languageCode", "languageCode", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceComponentProductionSpecification(backboneelement.BackboneElement):
    """ Production specification of the component.
    
    Describes the production specification such as component revision, serial
    number, etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.specType = None
        """ Specification type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.componentId = None
        """ Internal component unique identification.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.productionSpec = None
        """ A printable string defining the component.
        Type `str`. """
        
        super(DeviceComponentProductionSpecification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceComponentProductionSpecification, self).elementProperties()
        js.extend([
            ("specType", "specType", codeableconcept.CodeableConcept, False, None, False),
            ("componentId", "componentId", identifier.Identifier, False, None, False),
            ("productionSpec", "productionSpec", str, False, None, False),
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
