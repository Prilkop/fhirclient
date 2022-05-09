#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.
    
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole and to publish a computable definition of all the parts.
    """
    
    resource_type = "ImplementationGuide"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Logical URI to reference this implementation guide (globally
        unique).
        Type `str`. """
        
        self.version = None
        """ Business version of the implementation guide.
        Type `str`. """
        
        self.name = None
        """ Name for this implementation guide (computer friendly).
        Type `str`. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the implementation guide.
        Type `str`. """
        
        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for implementation guide (if applicable).
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
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, False),
            ("dependency", "dependency", ImplementationGuideDependency, True, None, False),
            ("package", "package", ImplementationGuidePackage, True, None, False),
            ("global_fhir", "global", ImplementationGuideGlobal, True, None, False),
            ("binary", "binary", str, True, None, False),
            ("page", "page", ImplementationGuidePage, False, None, False),
        ])
        return js


from . import backboneelement

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
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
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
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.example = None
        """ If not an example, has its normal meaning.
        Type `bool`. """
        
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
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.exampleFor = None
        """ Resource this is an example of (if applicable).
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        super(ImplementationGuidePackageResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePackageResource, self).elementProperties()
        js.extend([
            ("example", "example", bool, False, None, True),
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
        
        self.title = None
        """ Short title shown for navigational assistance.
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
            ("title", "title", str, False, None, True),
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
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
