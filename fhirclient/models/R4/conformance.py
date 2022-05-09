#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Conformance) on 2022-04-28.
#  2022, SMART Health IT.


from . import domainresource

class Conformance(domainresource.DomainResource):
    """ A conformance statement.
    
    A conformance statement is a set of capabilities of a FHIR Server that may
    be used as a statement of actual server functionality or a statement of
    required or desired server implementation.
    """
    
    resource_type = "Conformance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Logical uri to reference this statement.
        Type `str`. """
        
        self.version = None
        """ Logical id for this version of the statement.
        Type `str`. """
        
        self.name = None
        """ Informal name for this conformance statement.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ConformanceContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Human description of the conformance statement.
        Type `str`. """
        
        self.requirements = None
        """ Why is this needed?.
        Type `str`. """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.kind = None
        """ instance | capability | requirements.
        Type `str`. """
        
        self.software = None
        """ Software that is covered by this conformance statement.
        Type `ConformanceSoftware` (represented as `dict` in JSON). """
        
        self.implementation = None
        """ If this describes a specific instance.
        Type `ConformanceImplementation` (represented as `dict` in JSON). """
        
        self.fhirVersion = None
        """ FHIR Version the system uses.
        Type `str`. """
        
        self.acceptUnknown = None
        """ no | extensions | elements | both.
        Type `str`. """
        
        self.format = None
        """ formats supported (xml | json | mime type).
        List of `str` items. """
        
        self.profile = None
        """ Profiles for use cases supported.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.rest = None
        """ If the endpoint is a RESTful one.
        List of `ConformanceRest` items (represented as `dict` in JSON). """
        
        self.messaging = None
        """ If messaging is supported.
        List of `ConformanceMessaging` items (represented as `dict` in JSON). """
        
        self.document = None
        """ Document definition.
        List of `ConformanceDocument` items (represented as `dict` in JSON). """
        
        super(Conformance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Conformance, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("status", "status", ConformanceResourceStatus.str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ConformanceContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("kind", "kind", ConformanceStatementKind.str, False, None, True),
            ("software", "software", ConformanceSoftware, False, None, False),
            ("implementation", "implementation", ConformanceImplementation, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, True),
            ("acceptUnknown", "acceptUnknown", UnknownContentCode.str, False, None, True),
            ("format", "format", str, True, None, True),
            ("profile", "profile", fhirreference.FHIRReference, True, None, False),
            ("rest", "rest", ConformanceRest, True, None, False),
            ("messaging", "messaging", ConformanceMessaging, True, None, False),
            ("document", "document", ConformanceDocument, True, None, False),
        ])
        return js


from . import backboneelement

class ConformanceContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ConformanceContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ConformanceDocument(backboneelement.BackboneElement):
    """ Document definition.
    
    A document definition.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode = None
        """ producer | consumer.
        Type `str`. """
        
        self.documentation = None
        """ Description of document support.
        Type `str`. """
        
        self.profile = None
        """ Constraint on a resource used in the document.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ConformanceDocument, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceDocument, self).elementProperties()
        js.extend([
            ("mode", "mode", DocumentMode.str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("profile", "profile", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ConformanceImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.
    
    Identifies a specific implementation instance that is described by the
    conformance statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Describes this specific instance.
        Type `str`. """
        
        self.url = None
        """ Base URL for the installation.
        Type `str`. """
        
        super(ConformanceImplementation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceImplementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


class ConformanceMessaging(backboneelement.BackboneElement):
    """ If messaging is supported.
    
    A description of the messaging capabilities of the solution.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint = None
        """ A messaging service end-point.
        List of `ConformanceMessagingEndpoint` items (represented as `dict` in JSON). """
        
        self.reliableCache = None
        """ Reliable Message Cache Length (min).
        Type `int`. """
        
        self.documentation = None
        """ Messaging interface behavior details.
        Type `str`. """
        
        self.event = None
        """ Declare support for this event.
        List of `ConformanceMessagingEvent` items (represented as `dict` in JSON). """
        
        super(ConformanceMessaging, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceMessaging, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", ConformanceMessagingEndpoint, True, None, False),
            ("reliableCache", "reliableCache", int, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("event", "event", ConformanceMessagingEvent, True, None, True),
        ])
        return js


class ConformanceMessagingEndpoint(backboneelement.BackboneElement):
    """ A messaging service end-point.
    
    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.protocol = None
        """ http | ftp | mllp +.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.address = None
        """ Address of end-point.
        Type `str`. """
        
        super(ConformanceMessagingEndpoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceMessagingEndpoint, self).elementProperties()
        js.extend([
            ("protocol", "protocol", coding.Coding, False, None, True),
            ("address", "address", str, False, None, True),
        ])
        return js


class ConformanceMessagingEvent(backboneelement.BackboneElement):
    """ Declare support for this event.
    
    A description of the solution's support for an event at this end-point.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Event type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.category = None
        """ Consequence | Currency | Notification.
        Type `str`. """
        
        self.mode = None
        """ sender | receiver.
        Type `str`. """
        
        self.focus = None
        """ Resource that's focus of message.
        Type `str`. """
        
        self.request = None
        """ Profile that describes the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        """ Profile that describes the response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.documentation = None
        """ Endpoint-specific event documentation.
        Type `str`. """
        
        super(ConformanceMessagingEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceMessagingEvent, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, False, None, True),
            ("category", "category", MessageSignificanceCategory.str, False, None, False),
            ("mode", "mode", ConformanceEventMode.str, False, None, True),
            ("focus", "focus", ResourceType.str, False, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, True),
            ("response", "response", fhirreference.FHIRReference, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class ConformanceRest(backboneelement.BackboneElement):
    """ If the endpoint is a RESTful one.
    
    A definition of the restful capabilities of the solution, if any.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode = None
        """ client | server.
        Type `str`. """
        
        self.documentation = None
        """ General description of implementation.
        Type `str`. """
        
        self.security = None
        """ Information about security of implementation.
        Type `ConformanceRestSecurity` (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resource served on the REST interface.
        List of `ConformanceRestResource` items (represented as `dict` in JSON). """
        
        self.interaction = None
        """ What operations are supported?.
        List of `ConformanceRestInteraction` items (represented as `dict` in JSON). """
        
        self.transactionMode = None
        """ not-supported | batch | transaction | both.
        Type `str`. """
        
        self.searchParam = None
        """ Search params for searching all resources.
        List of `ConformanceRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.operation = None
        """ Definition of an operation or a custom query.
        List of `ConformanceRestOperation` items (represented as `dict` in JSON). """
        
        self.compartment = None
        """ Compartments served/used by system.
        List of `str` items. """
        
        super(ConformanceRest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceRest, self).elementProperties()
        js.extend([
            ("mode", "mode", RestfulConformanceMode.str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("security", "security", ConformanceRestSecurity, False, None, False),
            ("resource", "resource", ConformanceRestResource, True, None, True),
            ("interaction", "interaction", ConformanceRestInteraction, True, None, False),
            ("transactionMode", "transactionMode", TransactionMode.str, False, None, False),
            ("searchParam", "searchParam", ConformanceRestResourceSearchParam, True, None, False),
            ("operation", "operation", ConformanceRestOperation, True, None, False),
            ("compartment", "compartment", str, True, None, False),
        ])
        return js


class ConformanceRestInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    A specification of restful operations supported by the system.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ transaction | search-system | history-system.
        Type `str`. """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        
        super(ConformanceRestInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceRestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", FHIRRestfulInteractions.str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class ConformanceRestOperation(backboneelement.BackboneElement):
    """ Definition of an operation or a custom query.
    
    Definition of an operation or a named query and with its parameters and
    their meaning and type.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name by which the operation/query is invoked.
        Type `str`. """
        
        self.definition = None
        """ The defined operation/query.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ConformanceRestOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceRestOperation, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("definition", "definition", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ConformanceRestResource(backboneelement.BackboneElement):
    """ Resource served on the REST interface.
    
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ A resource type that is supported.
        Type `str`. """
        
        self.profile = None
        """ Base System profile for all uses of resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.interaction = None
        """ What operations are supported?.
        List of `ConformanceRestResourceInteraction` items (represented as `dict` in JSON). """
        
        self.versioning = None
        """ no-version | versioned | versioned-update.
        Type `str`. """
        
        self.readHistory = None
        """ Whether vRead can return past versions.
        Type `bool`. """
        
        self.updateCreate = None
        """ If update can commit to a new identity.
        Type `bool`. """
        
        self.conditionalCreate = None
        """ If allows/uses conditional create.
        Type `bool`. """
        
        self.conditionalUpdate = None
        """ If allows/uses conditional update.
        Type `bool`. """
        
        self.conditionalDelete = None
        """ not-supported | single | multiple - how conditional delete is
        supported.
        Type `str`. """
        
        self.searchInclude = None
        """ _include values supported by the server.
        List of `str` items. """
        
        self.searchRevInclude = None
        """ _revinclude values supported by the server.
        List of `str` items. """
        
        self.searchParam = None
        """ Search params supported by implementation.
        List of `ConformanceRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        super(ConformanceRestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceRestResource, self).elementProperties()
        js.extend([
            ("type", "type", ResourceType.str, False, None, True),
            ("profile", "profile", fhirreference.FHIRReference, False, None, False),
            ("interaction", "interaction", ConformanceRestResourceInteraction, True, None, True),
            ("versioning", "versioning", ResourceVersionPolicy.str, False, None, False),
            ("readHistory", "readHistory", bool, False, None, False),
            ("updateCreate", "updateCreate", bool, False, None, False),
            ("conditionalCreate", "conditionalCreate", bool, False, None, False),
            ("conditionalUpdate", "conditionalUpdate", bool, False, None, False),
            ("conditionalDelete", "conditionalDelete", ConditionalDeleteStatus.str, False, None, False),
            ("searchInclude", "searchInclude", str, True, None, False),
            ("searchRevInclude", "searchRevInclude", str, True, None, False),
            ("searchParam", "searchParam", ConformanceRestResourceSearchParam, True, None, False),
        ])
        return js


class ConformanceRestResourceInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    Identifies a restful operation supported by the solution.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ read | vread | update | delete | history-instance | validate |
        history-type | create | search-type.
        Type `str`. """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        
        super(ConformanceRestResourceInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceRestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", FHIRRestfulInteractions.str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class ConformanceRestResourceSearchParam(backboneelement.BackboneElement):
    """ Search params supported by implementation.
    
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of search parameter.
        Type `str`. """
        
        self.definition = None
        """ Source of definition for parameter.
        Type `str`. """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri.
        Type `str`. """
        
        self.documentation = None
        """ Server-specific usage.
        Type `str`. """
        
        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """
        
        self.modifier = None
        """ missing | exact | contains | not | text | in | not-in | below |
        above | type.
        List of `str` items. """
        
        self.chain = None
        """ Chained names supported.
        List of `str` items. """
        
        super(ConformanceRestResourceSearchParam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceRestResourceSearchParam, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("definition", "definition", str, False, None, False),
            ("type", "type", SearchParamType.str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("target", "target", ResourceType.str, True, None, False),
            ("modifier", "modifier", SearchModifierCode.str, True, None, False),
            ("chain", "chain", str, True, None, False),
        ])
        return js


class ConformanceRestSecurity(backboneelement.BackboneElement):
    """ Information about security of implementation.
    
    Information about security implementation from an interface perspective -
    what a client needs to know.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cors = None
        """ Adds CORS Headers (http://enable-cors.org/).
        Type `bool`. """
        
        self.service = None
        """ OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ General description of how security works.
        Type `str`. """
        
        self.certificate = None
        """ Certificates associated with security profiles.
        List of `ConformanceRestSecurityCertificate` items (represented as `dict` in JSON). """
        
        super(ConformanceRestSecurity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceRestSecurity, self).elementProperties()
        js.extend([
            ("cors", "cors", bool, False, None, False),
            ("service", "service", codeableconcept.CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("certificate", "certificate", ConformanceRestSecurityCertificate, True, None, False),
        ])
        return js


class ConformanceRestSecurityCertificate(backboneelement.BackboneElement):
    """ Certificates associated with security profiles.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Mime type for certificate.
        Type `str`. """
        
        self.blob = None
        """ Actual certificate.
        Type `str`. """
        
        super(ConformanceRestSecurityCertificate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceRestSecurityCertificate, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, False),
            ("blob", "blob", str, False, None, False),
        ])
        return js


class ConformanceSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this conformance statement.
    
    Software that is covered by this conformance statement.  It is used when
    the conformance statement describes the capabilities of a particular
    software version, independent of an installation.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ A name the software is known by.
        Type `str`. """
        
        self.version = None
        """ Version covered by this statement.
        Type `str`. """
        
        self.releaseDate = None
        """ Date this version released.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ConformanceSoftware, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConformanceSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("releaseDate", "releaseDate", fhirdate.FHIRDate, False, None, False),
        ])
        return js


import sys
try:
    from . import ConditionalDeleteStatus
except ImportError:
    ConditionalDeleteStatus = sys.modules[__package__ + '.ConditionalDeleteStatus']
try:
    from . import ConformanceEventMode
except ImportError:
    ConformanceEventMode = sys.modules[__package__ + '.ConformanceEventMode']
try:
    from . import ConformanceResourceStatus
except ImportError:
    ConformanceResourceStatus = sys.modules[__package__ + '.ConformanceResourceStatus']
try:
    from . import ConformanceStatementKind
except ImportError:
    ConformanceStatementKind = sys.modules[__package__ + '.ConformanceStatementKind']
try:
    from . import DocumentMode
except ImportError:
    DocumentMode = sys.modules[__package__ + '.DocumentMode']
try:
    from . import FHIRRestfulInteractions
except ImportError:
    FHIRRestfulInteractions = sys.modules[__package__ + '.FHIRRestfulInteractions']
try:
    from . import MessageSignificanceCategory
except ImportError:
    MessageSignificanceCategory = sys.modules[__package__ + '.MessageSignificanceCategory']
try:
    from . import ResourceType
except ImportError:
    ResourceType = sys.modules[__package__ + '.ResourceType']
try:
    from . import ResourceVersionPolicy
except ImportError:
    ResourceVersionPolicy = sys.modules[__package__ + '.ResourceVersionPolicy']
try:
    from . import RestfulConformanceMode
except ImportError:
    RestfulConformanceMode = sys.modules[__package__ + '.RestfulConformanceMode']
try:
    from . import SearchModifierCode
except ImportError:
    SearchModifierCode = sys.modules[__package__ + '.SearchModifierCode']
try:
    from . import SearchParamType
except ImportError:
    SearchParamType = sys.modules[__package__ + '.SearchParamType']
try:
    from . import TransactionMode
except ImportError:
    TransactionMode = sys.modules[__package__ + '.TransactionMode']
try:
    from . import UnknownContentCode
except ImportError:
    UnknownContentCode = sys.modules[__package__ + '.UnknownContentCode']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
