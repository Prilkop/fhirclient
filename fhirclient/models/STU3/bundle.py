#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Bundle) on 2022-05-29.
#  2022, SMART Health IT.


from . import resource

class Bundle(resource.Resource):
    """ Contains a collection of resources.
    
    A container for a collection of resources.
    """
    
    resource_type = "Bundle"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Persistent identifier for the bundle.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ document | message | transaction | transaction-response | batch |
        batch-response | history | searchset | collection.
        Type `str`. """
        
        self.total = None
        """ If search, the total number of matches.
        Type `int`. """
        
        self.link = None
        """ Links related to this Bundle.
        List of `BundleLink` items (represented as `dict` in JSON). """
        
        self.entry = None
        """ Entry in the bundle - will have a resource, or information.
        List of `BundleEntry` items (represented as `dict` in JSON). """
        
        self.signature = None
        """ Digital Signature.
        Type `Signature` (represented as `dict` in JSON). """
        
        super(Bundle, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Bundle, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", str, False, None, True),
            ("total", "total", int, False, None, False),
            ("link", "link", BundleLink, True, None, False),
            ("entry", "entry", BundleEntry, True, None, False),
            ("signature", "signature", signature.Signature, False, None, False),
        ])
        return js


from . import backboneelement

class BundleEntry(backboneelement.BackboneElement):
    """ Entry in the bundle - will have a resource, or information.
    
    An entry in a bundle resource - will either contain a resource, or
    information about a resource (transactions and history only).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.link = None
        """ Links related to this entry.
        List of `BundleLink` items (represented as `dict` in JSON). """
        
        self.fullUrl = None
        """ Absolute URL for resource (server address, or UUID/OID).
        Type `str`. """
        
        self.resource = None
        """ A resource in the bundle.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.search = None
        """ Search related information.
        Type `BundleEntrySearch` (represented as `dict` in JSON). """
        
        self.request = None
        """ Transaction Related Information.
        Type `BundleEntryRequest` (represented as `dict` in JSON). """
        
        self.response = None
        """ Transaction Related Information.
        Type `BundleEntryResponse` (represented as `dict` in JSON). """
        
        super(BundleEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntry, self).elementProperties()
        js.extend([
            ("link", "link", BundleLink, True, None, False),
            ("fullUrl", "fullUrl", str, False, None, False),
            ("resource", "resource", resource.Resource, False, None, False),
            ("search", "search", BundleEntrySearch, False, None, False),
            ("request", "request", BundleEntryRequest, False, None, False),
            ("response", "response", BundleEntryResponse, False, None, False),
        ])
        return js


class BundleEntryRequest(backboneelement.BackboneElement):
    """ Transaction Related Information.
    
    Additional information about how this entry should be processed as part of
    a transaction.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.method = None
        """ GET | POST | PUT | DELETE.
        Type `str`. """
        
        self.url = None
        """ URL for HTTP equivalent of this entry.
        Type `str`. """
        
        self.ifNoneMatch = None
        """ For managing cache currency.
        Type `str`. """
        
        self.ifModifiedSince = None
        """ For managing update contention.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.ifMatch = None
        """ For managing update contention.
        Type `str`. """
        
        self.ifNoneExist = None
        """ For conditional creates.
        Type `str`. """
        
        super(BundleEntryRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntryRequest, self).elementProperties()
        js.extend([
            ("method", "method", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("ifNoneMatch", "ifNoneMatch", str, False, None, False),
            ("ifModifiedSince", "ifModifiedSince", fhirdate.FHIRDate, False, None, False),
            ("ifMatch", "ifMatch", str, False, None, False),
            ("ifNoneExist", "ifNoneExist", str, False, None, False),
        ])
        return js


class BundleEntryResponse(backboneelement.BackboneElement):
    """ Transaction Related Information.
    
    Additional information about how this entry should be processed as part of
    a transaction.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.status = None
        """ Status response code (text optional).
        Type `str`. """
        
        self.location = None
        """ The location, if the operation returns a location.
        Type `str`. """
        
        self.etag = None
        """ The etag for the resource (if relevant).
        Type `str`. """
        
        self.lastModified = None
        """ Server's date time modified.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.outcome = None
        """ OperationOutcome with hints and warnings (for batch/transaction).
        Type `Resource` (represented as `dict` in JSON). """
        
        super(BundleEntryResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntryResponse, self).elementProperties()
        js.extend([
            ("status", "status", str, False, None, True),
            ("location", "location", str, False, None, False),
            ("etag", "etag", str, False, None, False),
            ("lastModified", "lastModified", fhirdate.FHIRDate, False, None, False),
            ("outcome", "outcome", resource.Resource, False, None, False),
        ])
        return js


class BundleEntrySearch(backboneelement.BackboneElement):
    """ Search related information.
    
    Information about the search process that lead to the creation of this
    entry.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode = None
        """ match | include | outcome - why this is in the result set.
        Type `str`. """
        
        self.score = None
        """ Search ranking (between 0 and 1).
        Type `float`. """
        
        super(BundleEntrySearch, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntrySearch, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, False),
            ("score", "score", float, False, None, False),
        ])
        return js


class BundleLink(backboneelement.BackboneElement):
    """ Links related to this Bundle.
    
    A series of links that provide context to this bundle.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.relation = None
        """ See http://www.iana.org/assignments/link-relations/link-
        relations.xhtml#link-relations-1.
        Type `str`. """
        
        self.url = None
        """ Reference details for the link.
        Type `str`. """
        
        super(BundleLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleLink, self).elementProperties()
        js.extend([
            ("relation", "relation", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
