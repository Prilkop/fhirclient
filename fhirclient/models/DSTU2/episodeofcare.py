#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare) on 2022-05-29.
#  2022, SMART Health IT.


from . import domainresource

class EpisodeOfCare(domainresource.DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.
    
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """
    
    resource_type = "EpisodeOfCare"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifier(s) for the EpisodeOfCare.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled.
        Type `str`. """
        
        self.statusHistory = None
        """ Past list of status codes.
        List of `EpisodeOfCareStatusHistory` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type/class  - e.g. specialist referral, disease management.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ Conditions/problems/diagnoses this episode of care is for.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient for this episode of care.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization that assumes care.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ Interval during responsibility is assumed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.referralRequest = None
        """ Originating Referral Request(s).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.careManager = None
        """ Care manager/care co-ordinator for the patient.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ Other practitioners facilitating this episode of care.
        List of `EpisodeOfCareCareTeam` items (represented as `dict` in JSON). """
        
        super(EpisodeOfCare, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCare, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusHistory", "statusHistory", EpisodeOfCareStatusHistory, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", fhirreference.FHIRReference, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("referralRequest", "referralRequest", fhirreference.FHIRReference, True, None, False),
            ("careManager", "careManager", fhirreference.FHIRReference, False, None, False),
            ("careTeam", "careTeam", EpisodeOfCareCareTeam, True, None, False),
        ])
        return js


from . import backboneelement

class EpisodeOfCareCareTeam(backboneelement.BackboneElement):
    """ Other practitioners facilitating this episode of care.
    
    The list of practitioners that may be facilitating this episode of care for
    specific purposes.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        """ Role taken by this team member.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Period of time for this role.
        Type `Period` (represented as `dict` in JSON). """
        
        self.member = None
        """ The practitioner (or Organization) within the team.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(EpisodeOfCareCareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareCareTeam, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("member", "member", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """ Past list of status codes.
    
    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled.
        Type `str`. """
        
        self.period = None
        """ Period for the status.
        Type `Period` (represented as `dict` in JSON). """
        
        super(EpisodeOfCareStatusHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareStatusHistory, self).elementProperties()
        js.extend([
            ("status", "status", str, False, None, True),
            ("period", "period", period.Period, False, None, True),
        ])
        return js


import sys
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
