from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementation:
    strengths: List[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths]
    weaknesses: List[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportChanges:
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReport:
    behaviors: List[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors]
    resolved_findings: List[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings]
    summary: Optional[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportSummary] = None
    provenance: Optional[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportProvenance] = None
    implementation: Optional[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementation] = None
    changes: Optional[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportChanges] = None
    method: Optional[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportMethod] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReport
    findings: List[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFiles] = None
    scores: Optional[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementation:
    strengths: List[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths]
    weaknesses: List[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportChanges:
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReport:
    behaviors: List[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors]
    resolved_findings: List[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings]
    summary: Optional[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportSummary] = None
    provenance: Optional[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportProvenance] = None
    implementation: Optional[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementation] = None
    changes: Optional[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportChanges] = None
    method: Optional[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportMethod] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReport
    findings: List[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFiles] = None
    scores: Optional[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewGetOutput:
    object: str
    id: str
    verdict: str
    created_at: datetime
    updated_at: datetime
    skill_id: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    current_revision: Optional[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevision] = None
    in_progress_revision: Optional[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevision] = None


class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFiles:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScores:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportSummary:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportProvenance:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementation:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementation(
        strengths=[mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportChanges:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportMethod:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReport:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReport(
        summary=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindings:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevision:
        return DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevision(
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
        files=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputCurrentRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFiles:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScores:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportSummary:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportProvenance:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementation:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementation(
        strengths=[mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportChanges:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportMethod:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReport:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReport(
        summary=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindings:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevision:
        return DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevision(
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
        files=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutputInProgressRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewGetOutput:
        return DashboardInstanceSkillsSecurityReviewGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        verdict=data.get('verdict'),
        dismissed_at=datetime.fromisoformat(data.get('dismissed_at').replace('Z', '+00:00')) if data.get('dismissed_at') else None,
        current_revision=mapDashboardInstanceSkillsSecurityReviewGetOutputCurrentRevision.from_dict(data.get('current_revision')) if data.get('current_revision') else None,
        in_progress_revision=mapDashboardInstanceSkillsSecurityReviewGetOutputInProgressRevision.from_dict(data.get('in_progress_revision')) if data.get('in_progress_revision') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

