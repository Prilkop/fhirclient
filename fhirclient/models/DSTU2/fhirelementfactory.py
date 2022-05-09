#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2022-05-29.
#  2022, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    _resource_class_mapping = {}

    @classmethod
    def _init_resource_class_mapping(cls):
        from . import Account, AllergyIntolerance, Appointment, AppointmentResponse, AuditEvent, Basic, Binary, BodySite, Bundle, CarePlan, Claim, \
                      ClaimResponse, ClinicalImpression, Communication, CommunicationRequest, Composition, ConceptMap, Condition, Conformance, \
                      Contract, Coverage, DataElement, DetectedIssue, Device, DeviceComponent, DeviceMetric, DeviceUseRequest, DeviceUseStatement, \
                      DiagnosticOrder, DiagnosticReport, DocumentManifest, DocumentReference, DomainResource, EligibilityRequest, \
                      EligibilityResponse, Encounter, EnrollmentRequest, EnrollmentResponse, EpisodeOfCare, ExplanationOfBenefit, \
                      FamilyMemberHistory, Flag, Goal, Group, HealthcareService, ImagingObjectSelection, ImagingStudy, Immunization, \
                      ImmunizationRecommendation, ImplementationGuide, List, Location, Media, Medication, MedicationAdministration, \
                      MedicationDispense, MedicationOrder, MedicationStatement, MessageHeader, NamingSystem, NutritionOrder, Observation, \
                      OperationDefinition, OperationOutcome, Order, OrderResponse, Organization, Parameters, Patient, PaymentNotice, \
                      PaymentReconciliation, Person, Practitioner, Procedure, ProcedureRequest, ProcessRequest, ProcessResponse, Provenance, \
                      Questionnaire, QuestionnaireResponse, ReferralRequest, RelatedPerson, Resource, RiskAssessment, Schedule, SearchParameter, \
                      Slot, Specimen, StructureDefinition, Subscription, Substance, SupplyDelivery, SupplyRequest, TestScript, ValueSet, \
                      VisionPrescription, Element

        cls._resource_class_mapping = {
            "Account": Account,
            "AllergyIntolerance": AllergyIntolerance,
            "Appointment": Appointment,
            "AppointmentResponse": AppointmentResponse,
            "AuditEvent": AuditEvent,
            "Basic": Basic,
            "Binary": Binary,
            "BodySite": BodySite,
            "Bundle": Bundle,
            "CarePlan": CarePlan,
            "Claim": Claim,
            "ClaimResponse": ClaimResponse,
            "ClinicalImpression": ClinicalImpression,
            "Communication": Communication,
            "CommunicationRequest": CommunicationRequest,
            "Composition": Composition,
            "ConceptMap": ConceptMap,
            "Condition": Condition,
            "Conformance": Conformance,
            "Contract": Contract,
            "Coverage": Coverage,
            "DataElement": DataElement,
            "DetectedIssue": DetectedIssue,
            "Device": Device,
            "DeviceComponent": DeviceComponent,
            "DeviceMetric": DeviceMetric,
            "DeviceUseRequest": DeviceUseRequest,
            "DeviceUseStatement": DeviceUseStatement,
            "DiagnosticOrder": DiagnosticOrder,
            "DiagnosticReport": DiagnosticReport,
            "DocumentManifest": DocumentManifest,
            "DocumentReference": DocumentReference,
            "DomainResource": DomainResource,
            "EligibilityRequest": EligibilityRequest,
            "EligibilityResponse": EligibilityResponse,
            "Encounter": Encounter,
            "EnrollmentRequest": EnrollmentRequest,
            "EnrollmentResponse": EnrollmentResponse,
            "EpisodeOfCare": EpisodeOfCare,
            "ExplanationOfBenefit": ExplanationOfBenefit,
            "FamilyMemberHistory": FamilyMemberHistory,
            "Flag": Flag,
            "Goal": Goal,
            "Group": Group,
            "HealthcareService": HealthcareService,
            "ImagingObjectSelection": ImagingObjectSelection,
            "ImagingStudy": ImagingStudy,
            "Immunization": Immunization,
            "ImmunizationRecommendation": ImmunizationRecommendation,
            "ImplementationGuide": ImplementationGuide,
            "List": List,
            "Location": Location,
            "Media": Media,
            "Medication": Medication,
            "MedicationAdministration": MedicationAdministration,
            "MedicationDispense": MedicationDispense,
            "MedicationOrder": MedicationOrder,
            "MedicationStatement": MedicationStatement,
            "MessageHeader": MessageHeader,
            "NamingSystem": NamingSystem,
            "NutritionOrder": NutritionOrder,
            "Observation": Observation,
            "OperationDefinition": OperationDefinition,
            "OperationOutcome": OperationOutcome,
            "Order": Order,
            "OrderResponse": OrderResponse,
            "Organization": Organization,
            "Parameters": Parameters,
            "Patient": Patient,
            "PaymentNotice": PaymentNotice,
            "PaymentReconciliation": PaymentReconciliation,
            "Person": Person,
            "Practitioner": Practitioner,
            "Procedure": Procedure,
            "ProcedureRequest": ProcedureRequest,
            "ProcessRequest": ProcessRequest,
            "ProcessResponse": ProcessResponse,
            "Provenance": Provenance,
            "Questionnaire": Questionnaire,
            "QuestionnaireResponse": QuestionnaireResponse,
            "ReferralRequest": ReferralRequest,
            "RelatedPerson": RelatedPerson,
            "Resource": Resource,
            "RiskAssessment": RiskAssessment,
            "Schedule": Schedule,
            "SearchParameter": SearchParameter,
            "Slot": Slot,
            "Specimen": Specimen,
            "StructureDefinition": StructureDefinition,
            "Subscription": Subscription,
            "Substance": Substance,
            "SupplyDelivery": SupplyDelivery,
            "SupplyRequest": SupplyRequest,
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

