#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ResearchStudy) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class ResearchStudy(domainresource.DomainResource):
    """ Investigation to increase healthcare-related patient-independent knowledge.
    
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """
    
    resource_type = "ResearchStudy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for study.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Name for this study.
        Type `str`. """
        
        self.protocol = None
        """ Steps followed in executing study.
        List of `FHIRReference` items referencing `PlanDefinition` (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of larger study.
        List of `FHIRReference` items referencing `ResearchStudy` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | in-progress | suspended | stopped | completed | entered-in-
        error.
        Type `str`. """
        
        self.category = None
        """ Classifications for the study.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.focus = None
        """ Drugs, devices, conditions, etc. under study.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for the study.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.relatedArtifact = None
        """ References and dependencies.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.keyword = None
        """ Used to search for the study.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Geographic region(s) for study.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ What this is study doing.
        Type `str`. """
        
        self.enrollment = None
        """ Inclusion & exclusion criteria.
        List of `FHIRReference` items referencing `Group` (represented as `dict` in JSON). """
        
        self.period = None
        """ When the study began and ended.
        Type `Period` (represented as `dict` in JSON). """
        
        self.sponsor = None
        """ Organization responsible for the study.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.principalInvestigator = None
        """ The individual responsible for the study.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.site = None
        """ Location involved in study execution.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.reasonStopped = None
        """ Reason for terminating study early.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the event.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.arm = None
        """ Defined path through the study for a subject.
        List of `ResearchStudyArm` items (represented as `dict` in JSON). """
        
        super(ResearchStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchStudy, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("title", "title", str, False, None, False),
            ("protocol", "protocol", fhirreference.FHIRReference, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("focus", "focus", codeableconcept.CodeableConcept, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("keyword", "keyword", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("enrollment", "enrollment", fhirreference.FHIRReference, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("sponsor", "sponsor", fhirreference.FHIRReference, False, None, False),
            ("principalInvestigator", "principalInvestigator", fhirreference.FHIRReference, False, None, False),
            ("site", "site", fhirreference.FHIRReference, True, None, False),
            ("reasonStopped", "reasonStopped", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("arm", "arm", ResearchStudyArm, True, None, False),
        ])
        return js


from . import backboneelement

class ResearchStudyArm(backboneelement.BackboneElement):
    """ Defined path through the study for a subject.
    
    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Label for study arm.
        Type `str`. """
        
        self.code = None
        """ Categorization of study arm.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Short explanation of study path.
        Type `str`. """
        
        super(ResearchStudyArm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchStudyArm, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
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
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
