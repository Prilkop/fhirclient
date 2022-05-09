#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.
    
    A set of rules or how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole, and to publish a computable definition of all the parts.
    """
    
    resource_type = "ImplementationGuide"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Absolute URL used to reference this Implementation Guide.
        Type `str`. """
        
        self.version = None
        """ Logical id for this version of the Implementation Guide.
        Type `str`. """
        
        self.name = None
        """ Informal name for this Implementation Guide.
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
        List of `ImplementationGuideContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for this version of the Implementation Guide.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the Implementation Guide.
        Type `str`. """
        
        self.useContext = None
        """ The implementation guide is intended to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.fhirVersion = None
        """ FHIR Version this Implementation Guide targets.
        Type `str`. """
        
        self.dependency = None
        """ Another Implementation guide this depends on.
        List of `ImplementationGuideDependency` items (represented as `dict` in JSON). """
        
        self.package = None
        """ Group of resources as used in .page.package.
        List of `ImplementationGuidePackage` items (represented as `dict` in JSON). """
        
        self.global_fhir = None
        """ Profiles that apply globally.
        List of `ImplementationGuideGlobal` items (represented as `dict` in JSON). """
        
        self.binary = None
        """ Image, css, script, etc..
        List of `str` items. """
        
        self.page = None
        """ Page/Section in the Guide.
        Type `ImplementationGuidePage` (represented as `dict` in JSON). """
        
        super(ImplementationGuide, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuide, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ImplementationGuideContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, False),
            ("dependency", "dependency", ImplementationGuideDependency, True, None, False),
            ("package", "package", ImplementationGuidePackage, True, None, True),
            ("global_fhir", "global", ImplementationGuideGlobal, True, None, False),
            ("binary", "binary", str, True, None, False),
            ("page", "page", ImplementationGuidePage, False, None, True),
        ])
        return js


from . import backboneelement

class ImplementationGuideContact(backboneelement.BackboneElement):
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
        
        super(ImplementationGuideContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ImplementationGuideDependency(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.
    
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ reference | inclusion.
        Type `str`. """
        
        self.uri = None
        """ Where to find dependency.
        Type `str`. """
        
        super(ImplementationGuideDependency, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDependency, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("uri", "uri", str, False, None, True),
        ])
        return js


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.
    
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Type this profiles applies to.
        Type `str`. """
        
        self.profile = None
        """ Profile that all resources must conform to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ImplementationGuideGlobal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("profile", "profile", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ImplementationGuidePackage(backboneelement.BackboneElement):
    """ Group of resources as used in .page.package.
    
    A logical group of resources. Logical groups can be used when building
    pages.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name used .page.package.
        Type `str`. """
        
        self.description = None
        """ Human readable text describing the package.
        Type `str`. """
        
        self.resource = None
        """ Resource in the implementation guide.
        List of `ImplementationGuidePackageResource` items (represented as `dict` in JSON). """
        
        super(ImplementationGuidePackage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePackage, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("resource", "resource", ImplementationGuidePackageResource, True, None, True),
        ])
        return js


class ImplementationGuidePackageResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, conformance statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.purpose = None
        """ example | terminology | profile | extension | dictionary | logical.
        Type `str`. """
        
        self.name = None
        """ Human Name for the resource.
        Type `str`. """
        
        self.description = None
        """ Reason why included in guide.
        Type `str`. """
        
        self.acronym = None
        """ Short code to identify the resource.
        Type `str`. """
        
        self.sourceUri = None
        """ Location of the resource.
        Type `str`. """
        
        self.sourceReference = None
        """ Location of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.exampleFor = None
        """ Resource this is an example of (if applicable).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ImplementationGuidePackageResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePackageResource, self).elementProperties()
        js.extend([
            ("purpose", "purpose", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("acronym", "acronym", str, False, None, False),
            ("sourceUri", "sourceUri", str, False, "source", True),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", True),
            ("exampleFor", "exampleFor", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class ImplementationGuidePage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.
    
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.source = None
        """ Where to find that page.
        Type `str`. """
        
        self.name = None
        """ Short name shown for navigational assistance.
        Type `str`. """
        
        self.kind = None
        """ page | example | list | include | directory | dictionary | toc |
        resource.
        Type `str`. """
        
        self.type = None
        """ Kind of resource to include in the list.
        List of `str` items. """
        
        self.package = None
        """ Name of package to include.
        List of `str` items. """
        
        self.format = None
        """ Format of the page (e.g. html, markdown, etc.).
        Type `str`. """
        
        self.page = None
        """ Nested Pages / Sections.
        List of `ImplementationGuidePage` items (represented as `dict` in JSON). """
        
        super(ImplementationGuidePage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePage, self).elementProperties()
        js.extend([
            ("source", "source", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("kind", "kind", str, False, None, True),
            ("type", "type", str, True, None, False),
            ("package", "package", str, True, None, False),
            ("format", "format", str, False, None, False),
            ("page", "page", ImplementationGuidePage, True, None, False),
        ])
        return js


import sys
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
