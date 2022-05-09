#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.
    
    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """
    
    resource_type = "VisionPrescription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.prescriber = None
        """ Who authorizes the vision product.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Created during encounter / admission / stay.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason or indication for writing the prescription.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.dispense = None
        """ Vision supply authorization.
        List of `VisionPrescriptionDispense` items (represented as `dict` in JSON). """
        
        super(VisionPrescription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False, "reason", False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, "reason", False),
            ("dispense", "dispense", VisionPrescriptionDispense, True, None, False),
        ])
        return js


from . import backboneelement

class VisionPrescriptionDispense(backboneelement.BackboneElement):
    """ Vision supply authorization.
    
    Deals with details of the dispense part of the supply specification.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.product = None
        """ Product to be supplied.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.eye = None
        """ right | left.
        Type `str`. """
        
        self.sphere = None
        """ Lens sphere.
        Type `float`. """
        
        self.cylinder = None
        """ Lens cylinder.
        Type `float`. """
        
        self.axis = None
        """ Lens axis.
        Type `int`. """
        
        self.prism = None
        """ Lens prism.
        Type `float`. """
        
        self.base = None
        """ up | down | in | out.
        Type `str`. """
        
        self.add = None
        """ Lens add.
        Type `float`. """
        
        self.power = None
        """ Contact lens power.
        Type `float`. """
        
        self.backCurve = None
        """ Contact lens back curvature.
        Type `float`. """
        
        self.diameter = None
        """ Contact lens diameter.
        Type `float`. """
        
        self.duration = None
        """ Lens wear duration.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.color = None
        """ Lens add.
        Type `str`. """
        
        self.brand = None
        """ Lens add.
        Type `str`. """
        
        self.notes = None
        """ Notes for coatings.
        Type `str`. """
        
        super(VisionPrescriptionDispense, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescriptionDispense, self).elementProperties()
        js.extend([
            ("product", "product", coding.Coding, False, None, True),
            ("eye", "eye", str, False, None, False),
            ("sphere", "sphere", float, False, None, False),
            ("cylinder", "cylinder", float, False, None, False),
            ("axis", "axis", int, False, None, False),
            ("prism", "prism", float, False, None, False),
            ("base", "base", str, False, None, False),
            ("add", "add", float, False, None, False),
            ("power", "power", float, False, None, False),
            ("backCurve", "backCurve", float, False, None, False),
            ("diameter", "diameter", float, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("color", "color", str, False, None, False),
            ("brand", "brand", str, False, None, False),
            ("notes", "notes", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
