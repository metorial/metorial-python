from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation:
    strengths: List[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths]
    weaknesses: List[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges:
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport:
    behaviors: List[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors]
    resolved_findings: List[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings]
    summary: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary] = None
    provenance: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance] = None
    implementation: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation] = None
    changes: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges] = None
    method: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport
    findings: List[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles] = None
    scores: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation:
    strengths: List[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths]
    weaknesses: List[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges:
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport:
    behaviors: List[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors]
    resolved_findings: List[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings]
    summary: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary] = None
    provenance: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance] = None
    implementation: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation] = None
    changes: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges] = None
    method: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport
    findings: List[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles] = None
    scores: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewDismissOutput:
    object: str
    id: str
    verdict: str
    created_at: datetime
    updated_at: datetime
    skill_id: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    current_revision: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevision] = None
    in_progress_revision: Optional[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevision] = None


class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation(
        strengths=[mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport(
        summary=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevision:
        return DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevision(
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
        files=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation(
        strengths=[mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport(
        summary=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevision:
        return DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevision(
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
        files=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewDismissOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewDismissOutput:
        return DashboardInstanceSkillsSecurityReviewDismissOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        verdict=data.get('verdict'),
        dismissed_at=datetime.fromisoformat(data.get('dismissed_at').replace('Z', '+00:00')) if data.get('dismissed_at') else None,
        current_revision=mapDashboardInstanceSkillsSecurityReviewDismissOutputCurrentRevision.from_dict(data.get('current_revision')) if data.get('current_revision') else None,
        in_progress_revision=mapDashboardInstanceSkillsSecurityReviewDismissOutputInProgressRevision.from_dict(data.get('in_progress_revision')) if data.get('in_progress_revision') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewDismissOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

