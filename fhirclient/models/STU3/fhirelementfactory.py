#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 on 2022-05-29.
#  2022, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    _resource_class_mapping = {}

    @classmethod
    def _init_resource_class_mapping(cls):
        from . import Account, ActivityDefinition, AdverseEvent, AllergyIntolerance, Appointment, AppointmentResponse, AuditEvent, Basic, Binary, \
                      BodySite, Bundle, CapabilityStatement, CarePlan, CareTeam, ChargeItem, Claim, ClaimResponse, ClinicalImpression, CodeSystem, \
                      Communication, CommunicationRequest, CompartmentDefinition, Composition, ConceptMap, Condition, Consent, Contract, Coverage, \
                      DataElement, DetectedIssue, Device, DeviceComponent, DeviceMetric, DeviceRequest, DeviceUseStatement, DiagnosticReport, \
                      DocumentManifest, DocumentReference, DomainResource, EligibilityRequest, EligibilityResponse, Encounter, Endpoint, \
                      EnrollmentRequest, EnrollmentResponse, EpisodeOfCare, ExpansionProfile, ExplanationOfBenefit, FamilyMemberHistory, Flag, \
                      Goal, GraphDefinition, Group, GuidanceResponse, HealthcareService, ImagingManifest, ImagingStudy, Immunization, \
                      ImmunizationRecommendation, ImplementationGuide, Library, Linkage, List, Location, Measure, MeasureReport, Media, Medication, \
                      MedicationAdministration, MedicationDispense, MedicationRequest, MedicationStatement, MessageDefinition, MessageHeader, \
                      NamingSystem, NutritionOrder, Observation, OperationDefinition, OperationOutcome, Organization, Parameters, Patient, \
                      PaymentNotice, PaymentReconciliation, Person, PlanDefinition, Practitioner, PractitionerRole, Procedure, ProcedureRequest, \
                      ProcessRequest, ProcessResponse, Provenance, Questionnaire, QuestionnaireResponse, ReferralRequest, RelatedPerson, \
                      RequestGroup, ResearchStudy, ResearchSubject, Resource, RiskAssessment, Schedule, SearchParameter, Sequence, \
                      ServiceDefinition, Slot, Specimen, StructureDefinition, StructureMap, Subscription, Substance, SupplyDelivery, SupplyRequest, \
                      Task, TestReport, TestScript, ValueSet, VisionPrescription, Element

        cls._resource_class_mapping = {
            "Account": Account,
            "ActivityDefinition": ActivityDefinition,
            "AdverseEvent": AdverseEvent,
            "AllergyIntolerance": AllergyIntolerance,
            "Appointment": Appointment,
            "AppointmentResponse": AppointmentResponse,
            "AuditEvent": AuditEvent,
            "Basic": Basic,
            "Binary": Binary,
            "BodySite": BodySite,
            "Bundle": Bundle,
            "CapabilityStatement": CapabilityStatement,
            "CarePlan": CarePlan,
            "CareTeam": CareTeam,
            "ChargeItem": ChargeItem,
            "Claim": Claim,
            "ClaimResponse": ClaimResponse,
            "ClinicalImpression": ClinicalImpression,
            "CodeSystem": CodeSystem,
            "Communication": Communication,
            "CommunicationRequest": CommunicationRequest,
            "CompartmentDefinition": CompartmentDefinition,
            "Composition": Composition,
            "ConceptMap": ConceptMap,
            "Condition": Condition,
            "Consent": Consent,
            "Contract": Contract,
            "Coverage": Coverage,
            "DataElement": DataElement,
            "DetectedIssue": DetectedIssue,
            "Device": Device,
            "DeviceComponent": DeviceComponent,
            "DeviceMetric": DeviceMetric,
            "DeviceRequest": DeviceRequest,
            "DeviceUseStatement": DeviceUseStatement,
            "DiagnosticReport": DiagnosticReport,
            "DocumentManifest": DocumentManifest,
            "DocumentReference": DocumentReference,
            "DomainResource": DomainResource,
            "EligibilityRequest": EligibilityRequest,
            "EligibilityResponse": EligibilityResponse,
            "Encounter": Encounter,
            "Endpoint": Endpoint,
            "EnrollmentRequest": EnrollmentRequest,
            "EnrollmentResponse": EnrollmentResponse,
            "EpisodeOfCare": EpisodeOfCare,
            "ExpansionProfile": ExpansionProfile,
            "ExplanationOfBenefit": ExplanationOfBenefit,
            "FamilyMemberHistory": FamilyMemberHistory,
            "Flag": Flag,
            "Goal": Goal,
            "GraphDefinition": GraphDefinition,
            "Group": Group,
            "GuidanceResponse": GuidanceResponse,
            "HealthcareService": HealthcareService,
            "ImagingManifest": ImagingManifest,
            "ImagingStudy": ImagingStudy,
            "Immunization": Immunization,
            "ImmunizationRecommendation": ImmunizationRecommendation,
            "ImplementationGuide": ImplementationGuide,
            "Library": Library,
            "Linkage": Linkage,
            "List": List,
            "Location": Location,
            "Measure": Measure,
            "MeasureReport": MeasureReport,
            "Media": Media,
            "Medication": Medication,
            "MedicationAdministration": MedicationAdministration,
            "MedicationDispense": MedicationDispense,
            "MedicationRequest": MedicationRequest,
            "MedicationStatement": MedicationStatement,
            "MessageDefinition": MessageDefinition,
            "MessageHeader": MessageHeader,
            "NamingSystem": NamingSystem,
            "NutritionOrder": NutritionOrder,
            "Observation": Observation,
            "OperationDefinition": OperationDefinition,
            "OperationOutcome": OperationOutcome,
            "Organization": Organization,
            "Parameters": Parameters,
            "Patient": Patient,
            "PaymentNotice": PaymentNotice,
            "PaymentReconciliation": PaymentReconciliation,
            "Person": Person,
            "PlanDefinition": PlanDefinition,
            "Practitioner": Practitioner,
            "PractitionerRole": PractitionerRole,
            "Procedure": Procedure,
            "ProcedureRequest": ProcedureRequest,
            "ProcessRequest": ProcessRequest,
            "ProcessResponse": ProcessResponse,
            "Provenance": Provenance,
            "Questionnaire": Questionnaire,
            "QuestionnaireResponse": QuestionnaireResponse,
            "ReferralRequest": ReferralRequest,
            "RelatedPerson": RelatedPerson,
            "RequestGroup": RequestGroup,
            "ResearchStudy": ResearchStudy,
            "ResearchSubject": ResearchSubject,
            "Resource": Resource,
            "RiskAssessment": RiskAssessment,
            "Schedule": Schedule,
            "SearchParameter": SearchParameter,
            "Sequence": Sequence,
            "ServiceDefinition": ServiceDefinition,
            "Slot": Slot,
            "Specimen": Specimen,
            "StructureDefinition": StructureDefinition,
            "StructureMap": StructureMap,
            "Subscription": Subscription,
            "Substance": Substance,
            "SupplyDelivery": SupplyDelivery,
            "SupplyRequest": SupplyRequest,
            "Task": Task,
            "TestReport": TestReport,
            "TestScript": TestScript,
            "ValueSet": ValueSet,
            "VisionPrescription": VisionPrescription,
            None: Element
        }

    @classmethod
    def get_resource_class(cls, resource_type):
        """ Return a resource class for the type correlating to "resource_type".

        :param str resource_type: The name/type of the resource to instantiate
        :returns: A resource class for the respective type or `Element`
        """
        if not cls._resource_class_mapping:
            cls._init_resource_class_mapping()

        return cls._resource_class_mapping.get(resource_type, cls._resource_class_mapping[None])

    @classmethod
    def instantiate(cls, resource_type, jsondict):
        """ Instantiate a resource of the type correlating to "resource_type".

        :param str resource_type: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :returns: A resource of the respective type or `Element`
        """
        klass = cls.get_resource_class(resource_type)
        return klass(jsondict)

    @classmethod
    def read_from(cls, path, server):
        """ Requests data from the given REST path on the server and creates
        an instance of based on the path.

        :param str path: The REST path to read from
        :param FHIRServer server: An instance of a FHIR server or compatible class
        :returns: An instance of the receiving class
        """
        if not path:
            raise Exception("Cannot read resource without REST path")
        if server is None:
            raise Exception("Cannot read resource without server instance")

        resource_type = path.split('/')[0]
        klass = cls.get_resource_class(resource_type)
        return klass.read_from(path, server)

