#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient or group.
    
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """
    
    resource_type = "CarePlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this plan.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ Protocol or definition.
        List of `FHIRReference` items referencing `PlanDefinition, Questionnaire` (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ Fulfills care plan.
        List of `FHIRReference` items referencing `CarePlan` (represented as `dict` in JSON). """
        
        self.replaces = None
        """ CarePlan replaced by this CarePlan.
        List of `FHIRReference` items referencing `CarePlan` (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced CarePlan.
        List of `FHIRReference` items referencing `CarePlan` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | suspended | completed | entered-in-error |
        cancelled | unknown.
        Type `str`. """
        
        self.intent = None
        """ proposal | plan | order | option.
        Type `str`. """
        
        self.category = None
        """ Type of plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Human-friendly name for the CarePlan.
        Type `str`. """
        
        self.description = None
        """ Summary of nature of plan.
        Type `str`. """
        
        self.subject = None
        """ Who care plan is for.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        self.context = None
        """ Created in context of.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period plan covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.author = None
        """ Who is responsible for contents of the plan.
        List of `FHIRReference` items referencing `Patient, Practitioner, RelatedPerson, Organization, CareTeam` (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ Who's involved in plan?.
        List of `FHIRReference` items referencing `CareTeam` (represented as `dict` in JSON). """
        
        self.addresses = None
        """ Health issues this plan addresses.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.supportingInfo = None
        """ Information considered as part of plan.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.goal = None
        """ Desired outcome of plan.
        List of `FHIRReference` items referencing `Goal` (represented as `dict` in JSON). """
        
        self.activity = None
        """ Action to occur as part of plan.
        List of `CarePlanActivity` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments about the plan.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(CarePlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("definition", "definition", fhirreference.FHIRReference, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("intent", "intent", str, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("title", "title", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("careTeam", "careTeam", fhirreference.FHIRReference, True, None, False),
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("activity", "activity", CarePlanActivity, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
        ])
        return js


from . import backboneelement

class CarePlanActivity(backboneelement.BackboneElement):
    """ Action to occur as part of plan.
    
    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.outcomeCodeableConcept = None
        """ Results of the activity.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcomeReference = None
        """ Appointment, Encounter, Procedure, etc..
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.progress = None
        """ Comments about the activity status/progress.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ Activity details defined in specific resource.
        Type `FHIRReference` referencing `Appointment, CommunicationRequest, DeviceRequest, MedicationRequest, NutritionOrder, Task, ProcedureRequest, ReferralRequest, VisionPrescription, RequestGroup` (represented as `dict` in JSON). """
        
        self.detail = None
        """ In-line definition of activity.
        Type `CarePlanActivityDetail` (represented as `dict` in JSON). """
        
        super(CarePlanActivity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend([
            ("outcomeCodeableConcept", "outcomeCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False),
            ("progress", "progress", annotation.Annotation, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("detail", "detail", CarePlanActivityDetail, False, None, False),
        ])
        return js


class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ In-line definition of activity.
    
    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ diet | drug | encounter | observation | procedure | supply | other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definition = None
        """ Protocol or definition.
        Type `FHIRReference` referencing `PlanDefinition, ActivityDefinition, Questionnaire` (represented as `dict` in JSON). """
        
        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why activity should be done or why activity was prohibited.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Condition triggering need for activity.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.goal = None
        """ Goals this activity relates to.
        List of `FHIRReference` items referencing `Goal` (represented as `dict` in JSON). """
        
        self.status = None
        """ not-started | scheduled | in-progress | on-hold | completed |
        cancelled | unknown.
        Type `str`. """
        
        self.statusReason = None
        """ Reason for current status.
        Type `str`. """
        
        self.prohibited = None
        """ Do NOT do.
        Type `bool`. """
        
        self.scheduledTiming = None
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.scheduledPeriod = None
        """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scheduledString = None
        """ When activity is to occur.
        Type `str`. """
        
        self.location = None
        """ Where it should happen.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who will be responsible?.
        List of `FHIRReference` items referencing `Practitioner, Organization, RelatedPerson, Patient, CareTeam` (represented as `dict` in JSON). """
        
        self.productCodeableConcept = None
        """ What is to be administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productReference = None
        """ What is to be administered/supplied.
        Type `FHIRReference` referencing `Medication, Substance` (represented as `dict` in JSON). """
        
        self.dailyAmount = None
        """ How to consume/day?.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ How much to administer/supply/consume.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description = None
        """ Extra info describing activity to perform.
        Type `str`. """
        
        super(CarePlanActivityDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("definition", "definition", fhirreference.FHIRReference, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", str, False, None, False),
            ("prohibited", "prohibited", bool, False, None, False),
            ("scheduledTiming", "scheduledTiming", timing.Timing, False, "scheduled", False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False, "scheduled", False),
            ("scheduledString", "scheduledString", str, False, "scheduled", False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("dailyAmount", "dailyAmount", quantity.Quantity, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']