#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ValueSet) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class ValueSet(domainresource.DomainResource):
    """ A set of codes drawn from one or more code systems.
    
    A value set specifies a set of codes drawn from one or more code systems.
    """
    
    resource_type = "ValueSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Globally unique logical identifier for  value set.
        Type `str`. """
        
        self.identifier = None
        """ Additional identifier for the value set (e.g. HL7 v2 / CDA).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical identifier for this version of the value set.
        Type `str`. """
        
        self.name = None
        """ Informal name for this value set.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ValueSetContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lockedDate = None
        """ Fixed date for all referenced code systems and value sets.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Human language description of the value set.
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.immutable = None
        """ Indicates whether or not any change to the content logical
        definition may occur.
        Type `bool`. """
        
        self.requirements = None
        """ Why needed.
        Type `str`. """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.extensible = None
        """ Whether this is intended to be used with an extensible binding.
        Type `bool`. """
        
        self.codeSystem = None
        """ An inline code system, which is part of this value set.
        Type `ValueSetCodeSystem` (represented as `dict` in JSON). """
        
        self.compose = None
        """ When value set includes codes from elsewhere.
        Type `ValueSetCompose` (represented as `dict` in JSON). """
        
        self.expansion = None
        """ Used when the value set is "expanded".
        Type `ValueSetExpansion` (represented as `dict` in JSON). """
        
        super(ValueSet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSet, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ValueSetContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("lockedDate", "lockedDate", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
            ("immutable", "immutable", bool, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("extensible", "extensible", bool, False, None, False),
            ("codeSystem", "codeSystem", ValueSetCodeSystem, False, None, False),
            ("compose", "compose", ValueSetCompose, False, None, False),
            ("expansion", "expansion", ValueSetExpansion, False, None, False),
        ])
        return js


from . import backboneelement

class ValueSetCodeSystem(backboneelement.BackboneElement):
    """ An inline code system, which is part of this value set.
    
    A definition of a code system, inlined into the value set (as a packaging
    convenience). Note that the inline code system may be used from other value
    sets by referring to its (codeSystem.system) directly.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.system = None
        """ URI to identify the code system (e.g. in Coding.system).
        Type `str`. """
        
        self.version = None
        """ Version (for use in Coding.version).
        Type `str`. """
        
        self.caseSensitive = None
        """ If code comparison is case sensitive.
        Type `bool`. """
        
        self.concept = None
        """ Concepts in the code system.
        List of `ValueSetCodeSystemConcept` items (represented as `dict` in JSON). """
        
        super(ValueSetCodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetCodeSystem, self).elementProperties()
        js.extend([
            ("system", "system", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("caseSensitive", "caseSensitive", bool, False, None, False),
            ("concept", "concept", ValueSetCodeSystemConcept, True, None, True),
        ])
        return js


class ValueSetCodeSystemConcept(backboneelement.BackboneElement):
    """ Concepts in the code system.
    
    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meaning of the hierarchical relationships are.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code that identifies concept.
        Type `str`. """
        
        self.abstract = None
        """ If this code is not for use as a real concept.
        Type `bool`. """
        
        self.display = None
        """ Text to display to the user.
        Type `str`. """
        
        self.definition = None
        """ Formal definition.
        Type `str`. """
        
        self.designation = None
        """ Additional representations for the concept.
        List of `ValueSetCodeSystemConceptDesignation` items (represented as `dict` in JSON). """
        
        self.concept = None
        """ Child Concepts (is-a/contains/categorizes).
        List of `ValueSetCodeSystemConcept` items (represented as `dict` in JSON). """
        
        super(ValueSetCodeSystemConcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetCodeSystemConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("abstract", "abstract", bool, False, None, False),
            ("display", "display", str, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("designation", "designation", ValueSetCodeSystemConceptDesignation, True, None, False),
            ("concept", "concept", ValueSetCodeSystemConcept, True, None, False),
        ])
        return js


class ValueSetCodeSystemConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for the concept.
    
    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ Human language of the designation.
        Type `str`. """
        
        self.use = None
        """ Details how this designation would be used.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ The text value for this designation.
        Type `str`. """
        
        super(ValueSetCodeSystemConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetCodeSystemConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


class ValueSetCompose(backboneelement.BackboneElement):
    """ When value set includes codes from elsewhere.
    
    A set of criteria that provide the content logical definition of the value
    set by including or excluding codes from outside this value set.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.import_fhir = None
        """ Import the contents of another value set.
        List of `str` items. """
        
        self.include = None
        """ Include one or more codes from a code system.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        self.exclude = None
        """ Explicitly exclude codes.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        super(ValueSetCompose, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetCompose, self).elementProperties()
        js.extend([
            ("import_fhir", "import", str, True, None, False),
            ("include", "include", ValueSetComposeInclude, True, None, False),
            ("exclude", "exclude", ValueSetComposeInclude, True, None, False),
        ])
        return js


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """ Include one or more codes from a code system.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.system = None
        """ The system the codes come from.
        Type `str`. """
        
        self.version = None
        """ Specific version of the code system referred to.
        Type `str`. """
        
        self.concept = None
        """ A concept defined in the system.
        List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON). """
        
        self.filter = None
        """ Select codes/concepts by their properties (including relationships).
        List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON). """
        
        super(ValueSetComposeInclude, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeInclude, self).elementProperties()
        js.extend([
            ("system", "system", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("concept", "concept", ValueSetComposeIncludeConcept, True, None, False),
            ("filter", "filter", ValueSetComposeIncludeFilter, True, None, False),
        ])
        return js


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """ A concept defined in the system.
    
    Specifies a concept to be included or excluded.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code or expression from system.
        Type `str`. """
        
        self.display = None
        """ Test to display for this code for this value set.
        Type `str`. """
        
        self.designation = None
        """ Additional representations for this valueset.
        List of `ValueSetCodeSystemConceptDesignation` items (represented as `dict` in JSON). """
        
        super(ValueSetComposeIncludeConcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("display", "display", str, False, None, False),
            ("designation", "designation", ValueSetCodeSystemConceptDesignation, True, None, False),
        ])
        return js


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """ Select codes/concepts by their properties (including relationships).
    
    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.property = None
        """ A property defined by the code system.
        Type `str`. """
        
        self.op = None
        """ = | is-a | is-not-a | regex | in | not-in.
        Type `str`. """
        
        self.value = None
        """ Code from the system, or regex criteria.
        Type `str`. """
        
        super(ValueSetComposeIncludeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeFilter, self).elementProperties()
        js.extend([
            ("property", "property", str, False, None, True),
            ("op", "op", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class ValueSetContact(backboneelement.BackboneElement):
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
        """ Name of an individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ValueSetContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ValueSetExpansion(backboneelement.BackboneElement):
    """ Used when the value set is "expanded".
    
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Uniquely identifies this expansion.
        Type `str`. """
        
        self.timestamp = None
        """ Time ValueSet expansion happened.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.total = None
        """ Total number of codes in the expansion.
        Type `int`. """
        
        self.offset = None
        """ Offset at which this resource starts.
        Type `int`. """
        
        self.parameter = None
        """ Parameter that controlled the expansion process.
        List of `ValueSetExpansionParameter` items (represented as `dict` in JSON). """
        
        self.contains = None
        """ Codes in the value set.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        super(ValueSetExpansion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansion, self).elementProperties()
        js.extend([
            ("identifier", "identifier", str, False, None, True),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False, None, True),
            ("total", "total", int, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("parameter", "parameter", ValueSetExpansionParameter, True, None, False),
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
        ])
        return js


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """ Codes in the value set.
    
    The codes that are contained in the value set expansion.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.system = None
        """ System value for the code.
        Type `str`. """
        
        self.abstract = None
        """ If user cannot select this entry.
        Type `bool`. """
        
        self.version = None
        """ Version in which this code/display is defined.
        Type `str`. """
        
        self.code = None
        """ Code - if blank, this is not a selectable code.
        Type `str`. """
        
        self.display = None
        """ User display for the concept.
        Type `str`. """
        
        self.contains = None
        """ Codes contained under this entry.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        super(ValueSetExpansionContains, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionContains, self).elementProperties()
        js.extend([
            ("system", "system", str, False, None, False),
            ("abstract", "abstract", bool, False, None, False),
            ("version", "version", str, False, None, False),
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
        ])
        return js


class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """ Parameter that controlled the expansion process.
    
    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name as assigned by the server.
        Type `str`. """
        
        self.valueString = None
        """ Value of the named parameter.
        Type `str`. """
        
        self.valueBoolean = None
        """ Value of the named parameter.
        Type `bool`. """
        
        self.valueInteger = None
        """ Value of the named parameter.
        Type `int`. """
        
        self.valueDecimal = None
        """ Value of the named parameter.
        Type `float`. """
        
        self.valueUri = None
        """ Value of the named parameter.
        Type `str`. """
        
        self.valueCode = None
        """ Value of the named parameter.
        Type `str`. """
        
        super(ValueSetExpansionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("valueString", "valueString", str, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("valueCode", "valueCode", str, False, "value", False),
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
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
