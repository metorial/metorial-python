from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation:
    strengths: List[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths]
    weaknesses: List[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges:
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport:
    behaviors: List[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors]
    resolved_findings: List[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings]
    summary: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary] = None
    provenance: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance] = None
    implementation: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation] = None
    changes: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges] = None
    method: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport
    findings: List[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles] = None
    scores: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation:
    strengths: List[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths]
    weaknesses: List[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges:
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport:
    behaviors: List[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors]
    resolved_findings: List[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings]
    summary: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary] = None
    provenance: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance] = None
    implementation: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation] = None
    changes: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges] = None
    method: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport
    findings: List[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles] = None
    scores: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRestoreOutput:
    object: str
    id: str
    verdict: str
    created_at: datetime
    updated_at: datetime
    skill_id: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    current_revision: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevision] = None
    in_progress_revision: Optional[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevision] = None


class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation(
        strengths=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport(
        summary=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevision:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevision(
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
        files=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation(
        strengths=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport(
        summary=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevision:
        return DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevision(
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
        files=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRestoreOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRestoreOutput:
        return DashboardInstanceSkillsSecurityReviewRestoreOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        verdict=data.get('verdict'),
        dismissed_at=datetime.fromisoformat(data.get('dismissed_at').replace('Z', '+00:00')) if data.get('dismissed_at') else None,
        current_revision=mapDashboardInstanceSkillsSecurityReviewRestoreOutputCurrentRevision.from_dict(data.get('current_revision')) if data.get('current_revision') else None,
        in_progress_revision=mapDashboardInstanceSkillsSecurityReviewRestoreOutputInProgressRevision.from_dict(data.get('in_progress_revision')) if data.get('in_progress_revision') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRestoreOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

