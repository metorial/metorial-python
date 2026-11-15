from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation:
    strengths: List[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths]
    weaknesses: List[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges:
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport:
    behaviors: List[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors]
    resolved_findings: List[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings]
    summary: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary] = None
    provenance: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance] = None
    implementation: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation] = None
    changes: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges] = None
    method: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport
    findings: List[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles] = None
    scores: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation:
    strengths: List[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths]
    weaknesses: List[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges:
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport:
    behaviors: List[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors]
    resolved_findings: List[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings]
    summary: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary] = None
    provenance: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance] = None
    implementation: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation] = None
    changes: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges] = None
    method: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport
    findings: List[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles] = None
    scores: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewDismissOutput:
    object: str
    id: str
    verdict: str
    created_at: datetime
    updated_at: datetime
    skill_id: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    current_revision: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevision] = None
    in_progress_revision: Optional[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevision] = None


class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation(
        strengths=[mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport(
        summary=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevision:
        return ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevision(
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
        files=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation(
        strengths=[mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport(
        summary=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevision:
        return ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevision(
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
        files=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewDismissOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewDismissOutput:
        return ManagementInstanceSkillsSecurityReviewDismissOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        verdict=data.get('verdict'),
        dismissed_at=datetime.fromisoformat(data.get('dismissed_at').replace('Z', '+00:00')) if data.get('dismissed_at') else None,
        current_revision=mapManagementInstanceSkillsSecurityReviewDismissOutputCurrentRevision.from_dict(data.get('current_revision')) if data.get('current_revision') else None,
        in_progress_revision=mapManagementInstanceSkillsSecurityReviewDismissOutputInProgressRevision.from_dict(data.get('in_progress_revision')) if data.get('in_progress_revision') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewDismissOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

