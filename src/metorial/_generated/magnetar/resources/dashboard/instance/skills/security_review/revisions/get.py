from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance:
    class_: str
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors:
    tag: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation:
    strengths: List[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths]
    weaknesses: List[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings:
    key: str
    reason: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges:
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReport:
    behaviors: List[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors]
    resolved_findings: List[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings]
    summary: Optional[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary] = None
    provenance: Optional[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance] = None
    implementation: Optional[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation] = None
    changes: Optional[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges] = None
    method: Optional[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsGetOutput:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReport
    findings: List[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFiles] = None
    scores: Optional[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFiles:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScores:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation(
        strengths=[mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReport:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReport(
        summary=mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindings:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutput:
        return DashboardInstanceSkillsSecurityReviewRevisionsGetOutput(
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
        files=mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutputFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

