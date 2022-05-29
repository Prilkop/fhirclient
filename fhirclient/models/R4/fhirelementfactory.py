#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2022-05-02.
#  2022, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    _resource_class_mapping = {}

    @classmethod
    def _init_resource_class_mapping(cls):
        from . import Account, ActivityDefinition, AdverseEvent, AllergyIntolerance, Appointment, AppointmentResponse, AuditEvent, Basic, Binary, \
                      BiologicallyDerivedProduct, BodyStructure, Bundle, CapabilityStatement, CarePlan, CareTeam, CatalogEntry, ChargeItem, \
                      ChargeItemDefinition, Claim, ClaimResponse, ClinicalImpression, CodeSystem, Communication, CommunicationRequest, \
                      CompartmentDefinition, Composition, ConceptMap, Condition, Consent, Contract, Coverage, CoverageEligibilityRequest, \
                      CoverageEligibilityResponse, DetectedIssue, Device, DeviceDefinition, DeviceMetric, DeviceRequest, DeviceUseStatement, \
                      DiagnosticReport, DocumentManifest, DocumentReference, DomainResource, EffectEvidenceSynthesis, Encounter, Endpoint, \
                      EnrollmentRequest, EnrollmentResponse, EpisodeOfCare, EventDefinition, Evidence, EvidenceVariable, ExampleScenario, \
                      ExplanationOfBenefit, FamilyMemberHistory, Flag, Goal, GraphDefinition, Group, GuidanceResponse, HealthcareService, \
                      ImagingStudy, Immunization, ImmunizationEvaluation, ImmunizationRecommendation, ImplementationGuide, InsurancePlan, Invoice, \
                      Library, Linkage, List, Location, Measure, MeasureReport, Media, Medication, MedicationAdministration, MedicationDispense, \
                      MedicationKnowledge, MedicationRequest, MedicationStatement, MedicinalProduct, MedicinalProductAuthorization, \
                      MedicinalProductContraindication, MedicinalProductIndication, MedicinalProductIngredient, MedicinalProductInteraction, \
                      MedicinalProductManufactured, MedicinalProductPackaged, MedicinalProductPharmaceutical, MedicinalProductUndesirableEffect, \
                      MessageDefinition, MessageHeader, MolecularSequence, NamingSystem, NutritionOrder, Observation, ObservationDefinition, \
                      OperationDefinition, OperationOutcome, Organization, OrganizationAffiliation, Parameters, Patient, PaymentNotice, \
                      PaymentReconciliation, Person, PlanDefinition, Practitioner, PractitionerRole, Procedure, Provenance, Questionnaire, \
                      QuestionnaireResponse, RelatedPerson, RequestGroup, ResearchDefinition, ResearchElementDefinition, ResearchStudy, \
                      ResearchSubject, Resource, RiskAssessment, RiskEvidenceSynthesis, Schedule, SearchParameter, ServiceRequest, Slot, Specimen, \
                      SpecimenDefinition, StructureDefinition, StructureMap, Subscription, Substance, SubstanceNucleicAcid, SubstancePolymer, \
                      SubstanceProtein, SubstanceReferenceInformation, SubstanceSourceMaterial, SubstanceSpecification, SupplyDelivery, \
                      SupplyRequest, Task, TerminologyCapabilities, TestReport, TestScript, ValueSet, VerificationResult, VisionPrescription, \
                      Element

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
            "BiologicallyDerivedProduct": BiologicallyDerivedProduct,
            "BodyStructure": BodyStructure,
            "Bundle": Bundle,
            "CapabilityStatement": CapabilityStatement,
            "CarePlan": CarePlan,
            "CareTeam": CareTeam,
            "CatalogEntry": CatalogEntry,
            "ChargeItem": ChargeItem,
            "ChargeItemDefinition": ChargeItemDefinition,
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
            "CoverageEligibilityRequest": CoverageEligibilityRequest,
            "CoverageEligibilityResponse": CoverageEligibilityResponse,
            "DetectedIssue": DetectedIssue,
            "Device": Device,
            "DeviceDefinition": DeviceDefinition,
            "DeviceMetric": DeviceMetric,
            "DeviceRequest": DeviceRequest,
            "DeviceUseStatement": DeviceUseStatement,
            "DiagnosticReport": DiagnosticReport,
            "DocumentManifest": DocumentManifest,
            "DocumentReference": DocumentReference,
            "DomainResource": DomainResource,
            "EffectEvidenceSynthesis": EffectEvidenceSynthesis,
            "Encounter": Encounter,
            "Endpoint": Endpoint,
            "EnrollmentRequest": EnrollmentRequest,
            "EnrollmentResponse": EnrollmentResponse,
            "EpisodeOfCare": EpisodeOfCare,
            "EventDefinition": EventDefinition,
            "Evidence": Evidence,
            "EvidenceVariable": EvidenceVariable,
            "ExampleScenario": ExampleScenario,
            "ExplanationOfBenefit": ExplanationOfBenefit,
            "FamilyMemberHistory": FamilyMemberHistory,
            "Flag": Flag,
            "Goal": Goal,
            "GraphDefinition": GraphDefinition,
            "Group": Group,
            "GuidanceResponse": GuidanceResponse,
            "HealthcareService": HealthcareService,
            "ImagingStudy": ImagingStudy,
            "Immunization": Immunization,
            "ImmunizationEvaluation": ImmunizationEvaluation,
            "ImmunizationRecommendation": ImmunizationRecommendation,
            "ImplementationGuide": ImplementationGuide,
            "InsurancePlan": InsurancePlan,
            "Invoice": Invoice,
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
            "MedicationKnowledge": MedicationKnowledge,
            "MedicationRequest": MedicationRequest,
            "MedicationStatement": MedicationStatement,
            "MedicinalProduct": MedicinalProduct,
            "MedicinalProductAuthorization": MedicinalProductAuthorization,
            "MedicinalProductContraindication": MedicinalProductContraindication,
            "MedicinalProductIndication": MedicinalProductIndication,
            "MedicinalProductIngredient": MedicinalProductIngredient,
            "MedicinalProductInteraction": MedicinalProductInteraction,
            "MedicinalProductManufactured": MedicinalProductManufactured,
            "MedicinalProductPackaged": MedicinalProductPackaged,
            "MedicinalProductPharmaceutical": MedicinalProductPharmaceutical,
            "MedicinalProductUndesirableEffect": MedicinalProductUndesirableEffect,
            "MessageDefinition": MessageDefinition,
            "MessageHeader": MessageHeader,
            "MolecularSequence": MolecularSequence,
            "NamingSystem": NamingSystem,
            "NutritionOrder": NutritionOrder,
            "Observation": Observation,
            "ObservationDefinition": ObservationDefinition,
            "OperationDefinition": OperationDefinition,
            "OperationOutcome": OperationOutcome,
            "Organization": Organization,
            "OrganizationAffiliation": OrganizationAffiliation,
            "Parameters": Parameters,
            "Patient": Patient,
            "PaymentNotice": PaymentNotice,
            "PaymentReconciliation": PaymentReconciliation,
            "Person": Person,
            "PlanDefinition": PlanDefinition,
            "Practitioner": Practitioner,
            "PractitionerRole": PractitionerRole,
            "Procedure": Procedure,
            "Provenance": Provenance,
            "Questionnaire": Questionnaire,
            "QuestionnaireResponse": QuestionnaireResponse,
            "RelatedPerson": RelatedPerson,
            "RequestGroup": RequestGroup,
            "ResearchDefinition": ResearchDefinition,
            "ResearchElementDefinition": ResearchElementDefinition,
            "ResearchStudy": ResearchStudy,
            "ResearchSubject": ResearchSubject,
            "Resource": Resource,
            "RiskAssessment": RiskAssessment,
            "RiskEvidenceSynthesis": RiskEvidenceSynthesis,
            "Schedule": Schedule,
            "SearchParameter": SearchParameter,
            "ServiceRequest": ServiceRequest,
            "Slot": Slot,
            "Specimen": Specimen,
            "SpecimenDefinition": SpecimenDefinition,
            "StructureDefinition": StructureDefinition,
            "StructureMap": StructureMap,
            "Subscription": Subscription,
            "Substance": Substance,
            "SubstanceNucleicAcid": SubstanceNucleicAcid,
            "SubstancePolymer": SubstancePolymer,
            "SubstanceProtein": SubstanceProtein,
            "SubstanceReferenceInformation": SubstanceReferenceInformation,
            "SubstanceSourceMaterial": SubstanceSourceMaterial,
            "SubstanceSpecification": SubstanceSpecification,
            "SupplyDelivery": SupplyDelivery,
            "SupplyRequest": SupplyRequest,
            "Task": Task,
            "TerminologyCapabilities": TerminologyCapabilities,
            "TestReport": TestReport,
            "TestScript": TestScript,
            "ValueSet": ValueSet,
            "VerificationResult": VerificationResult,
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

