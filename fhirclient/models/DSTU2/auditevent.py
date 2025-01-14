#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class AuditEvent(domainresource.DomainResource):
    """ Event record kept for security purposes.
    
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """
    
    resource_type = "AuditEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.event = None
        """ What was done.
        Type `AuditEventEvent` (represented as `dict` in JSON). """
        
        self.participant = None
        """ A person, a hardware device or software process.
        List of `AuditEventParticipant` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Application systems and processes.
        Type `AuditEventSource` (represented as `dict` in JSON). """
        
        self.object = None
        """ Specific instances of data or objects that have been accessed.
        List of `AuditEventObject` items (represented as `dict` in JSON). """
        
        super(AuditEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEvent, self).elementProperties()
        js.extend([
            ("event", "event", AuditEventEvent, False, None, True),
            ("participant", "participant", AuditEventParticipant, True, None, True),
            ("source", "source", AuditEventSource, False, None, True),
            ("object", "object", AuditEventObject, True, None, False),
        ])
        return js


from . import backboneelement

class AuditEventEvent(backboneelement.BackboneElement):
    """ What was done.
    
    Identifies the name, action type, time, and disposition of the audited
    event.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Type/identifier of event.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subtype = None
        """ More specific type/id for the event.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.action = None
        """ Type of action performed during the event.
        Type `str`. """
        
        self.dateTime = None
        """ Time when the event occurred on source.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.outcome = None
        """ Whether the event succeeded or failed.
        Type `str`. """
        
        self.outcomeDesc = None
        """ Description of the event outcome.
        Type `str`. """
        
        self.purposeOfEvent = None
        """ The purposeOfUse of the event.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(AuditEventEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventEvent, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, True),
            ("subtype", "subtype", coding.Coding, True, None, False),
            ("action", "action", str, False, None, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, True),
            ("outcome", "outcome", str, False, None, False),
            ("outcomeDesc", "outcomeDesc", str, False, None, False),
            ("purposeOfEvent", "purposeOfEvent", coding.Coding, True, None, False),
        ])
        return js


class AuditEventObject(backboneelement.BackboneElement):
    """ Specific instances of data or objects that have been accessed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Specific instance of object (e.g. versioned).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Specific instance of resource (e.g. versioned).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of object involved.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.role = None
        """ What role the Object played.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.lifecycle = None
        """ Life-cycle stage for the object.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ Security labels applied to the object.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Instance-specific descriptor for Object.
        Type `str`. """
        
        self.description = None
        """ Descriptive text.
        Type `str`. """
        
        self.query = None
        """ Actual query for object.
        Type `str`. """
        
        self.detail = None
        """ Additional Information about the Object.
        List of `AuditEventObjectDetail` items (represented as `dict` in JSON). """
        
        super(AuditEventObject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventObject, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("role", "role", coding.Coding, False, None, False),
            ("lifecycle", "lifecycle", coding.Coding, False, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("query", "query", str, False, None, False),
            ("detail", "detail", AuditEventObjectDetail, True, None, False),
        ])
        return js


class AuditEventObjectDetail(backboneelement.BackboneElement):
    """ Additional Information about the Object.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Name of the property.
        Type `str`. """
        
        self.value = None
        """ Property value.
        Type `str`. """
        
        super(AuditEventObjectDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventObjectDetail, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class AuditEventParticipant(backboneelement.BackboneElement):
    """ A person, a hardware device or software process.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        """ User roles (e.g. local RBAC codes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ Direct reference to resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.userId = None
        """ Unique identifier for the user.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.altId = None
        """ Alternative User id e.g. authentication.
        Type `str`. """
        
        self.name = None
        """ Human-meaningful name for the user.
        Type `str`. """
        
        self.requestor = None
        """ Whether user is initiator.
        Type `bool`. """
        
        self.location = None
        """ Where.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.policy = None
        """ Policy that authorized event.
        List of `str` items. """
        
        self.media = None
        """ Type of media.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.network = None
        """ Logical network location for application activity.
        Type `AuditEventParticipantNetwork` (represented as `dict` in JSON). """
        
        self.purposeOfUse = None
        """ Reason given for this user.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(AuditEventParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("userId", "userId", identifier.Identifier, False, None, False),
            ("altId", "altId", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("requestor", "requestor", bool, False, None, True),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("media", "media", coding.Coding, False, None, False),
            ("network", "network", AuditEventParticipantNetwork, False, None, False),
            ("purposeOfUse", "purposeOfUse", coding.Coding, True, None, False),
        ])
        return js


class AuditEventParticipantNetwork(backboneelement.BackboneElement):
    """ Logical network location for application activity.
    
    Logical network location for application activity, if the activity has a
    network location.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Identifier for the network access point of the user device.
        Type `str`. """
        
        self.type = None
        """ The type of network access point.
        Type `str`. """
        
        super(AuditEventParticipantNetwork, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventParticipantNetwork, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class AuditEventSource(backboneelement.BackboneElement):
    """ Application systems and processes.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.site = None
        """ Logical source location within the enterprise.
        Type `str`. """
        
        self.identifier = None
        """ The identity of source detecting the event.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of source where event originated.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(AuditEventSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventSource, self).elementProperties()
        js.extend([
            ("site", "site", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("type", "type", coding.Coding, True, None, False),
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
