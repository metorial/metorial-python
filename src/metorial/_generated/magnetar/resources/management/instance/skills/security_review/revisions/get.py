from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance:
    class_: str
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors:
    tag: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation:
    strengths: List[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths]
    weaknesses: List[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings:
    key: str
    reason: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges:
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReport:
    behaviors: List[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors]
    resolved_findings: List[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings]
    summary: Optional[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary] = None
    provenance: Optional[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance] = None
    implementation: Optional[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation] = None
    changes: Optional[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges] = None
    method: Optional[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsGetOutput:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReport
    findings: List[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFiles] = None
    scores: Optional[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFiles:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScores:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation(
        strengths=[mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReport:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReport(
        summary=mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindings:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsGetOutput:
        return ManagementInstanceSkillsSecurityReviewRevisionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        security_review_id=data.get('security_review_id'),
        skill_version_id=data.get('skill_version_id'),
        number=data.get('number'),
        status=data.get('status'),
        stage=data.get('stage'),
        block_reason=data.get('block_reason'),
        ai_generated=data.get('ai_generated'),
        trigger=data.get('trigger'),
        files=mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapManagementInstanceSkillsSecurityReviewRevisionsGetOutputFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

