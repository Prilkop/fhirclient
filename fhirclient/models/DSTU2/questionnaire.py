#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.
    
    A structured set of questions intended to guide the collection of answers.
    The questions are ordered and grouped into coherent subsets, corresponding
    to the structure of the grouping of the underlying questions.
    """
    
    resource_type = "Questionnaire"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifiers for this questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical identifier for this version of Questionnaire.
        Type `str`. """
        
        self.status = None
        """ draft | published | retired.
        Type `str`. """
        
        self.date = None
        """ Date this version was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Organization/individual who designed the questionnaire.
        Type `str`. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.subjectType = None
        """ Resource that can be subject of QuestionnaireResponse.
        List of `str` items. """
        
        self.group = None
        """ Grouped questions.
        Type `QuestionnaireGroup` (represented as `dict` in JSON). """
        
        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("subjectType", "subjectType", str, True, None, False),
            ("group", "group", QuestionnaireGroup, False, None, True),
        ])
        return js


from . import backboneelement

class QuestionnaireGroup(backboneelement.BackboneElement):
    """ Grouped questions.
    
    A collection of related questions (or further groupings of questions).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.linkId = None
        """ To link questionnaire with questionnaire response.
        Type `str`. """
        
        self.title = None
        """ Name to be displayed for group.
        Type `str`. """
        
        self.concept = None
        """ Concept that represents this section in a questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Additional text for the group.
        Type `str`. """
        
        self.required = None
        """ Whether the group must be included in data results.
        Type `bool`. """
        
        self.repeats = None
        """ Whether the group may repeat.
        Type `bool`. """
        
        self.group = None
        """ Nested questionnaire group.
        List of `QuestionnaireGroup` items (represented as `dict` in JSON). """
        
        self.question = None
        """ Questions in this group.
        List of `QuestionnaireGroupQuestion` items (represented as `dict` in JSON). """
        
        super(QuestionnaireGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireGroup, self).elementProperties()
        js.extend([
            ("linkId", "linkId", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("concept", "concept", coding.Coding, True, None, False),
            ("text", "text", str, False, None, False),
            ("required", "required", bool, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("group", "group", QuestionnaireGroup, True, None, False),
            ("question", "question", QuestionnaireGroupQuestion, True, None, False),
        ])
        return js


class QuestionnaireGroupQuestion(backboneelement.BackboneElement):
    """ Questions in this group.
    
    Set of questions within this group. The order of questions within the group
    is relevant.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.linkId = None
        """ To link questionnaire with questionnaire response.
        Type `str`. """
        
        self.concept = None
        """ Concept that represents this question on a questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text of the question as it is shown to the user.
        Type `str`. """
        
        self.type = None
        """ boolean | decimal | integer | date | dateTime +.
        Type `str`. """
        
        self.required = None
        """ Whether the question must be answered in data results.
        Type `bool`. """
        
        self.repeats = None
        """ Whether the question  can have multiple answers.
        Type `bool`. """
        
        self.options = None
        """ Valueset containing permitted answers.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.option = None
        """ Permitted answer.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.group = None
        """ Nested questionnaire group.
        List of `QuestionnaireGroup` items (represented as `dict` in JSON). """
        
        super(QuestionnaireGroupQuestion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireGroupQuestion, self).elementProperties()
        js.extend([
            ("linkId", "linkId", str, False, None, False),
            ("concept", "concept", coding.Coding, True, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("required", "required", bool, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("options", "options", fhirreference.FHIRReference, False, None, False),
            ("option", "option", coding.Coding, True, None, False),
            ("group", "group", QuestionnaireGroup, True, None, False),
        ])
        return js


import sys
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
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
