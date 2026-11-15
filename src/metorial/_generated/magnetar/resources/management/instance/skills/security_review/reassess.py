from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation:
    strengths: List[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths]
    weaknesses: List[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportChanges:
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReport:
    behaviors: List[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors]
    resolved_findings: List[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings]
    summary: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportSummary] = None
    provenance: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance] = None
    implementation: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation] = None
    changes: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportChanges] = None
    method: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportMethod] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReport
    findings: List[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFiles] = None
    scores: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation:
    strengths: List[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths]
    weaknesses: List[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportChanges:
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReport:
    behaviors: List[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors]
    resolved_findings: List[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings]
    summary: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportSummary] = None
    provenance: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance] = None
    implementation: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation] = None
    changes: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportChanges] = None
    method: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportMethod] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReport
    findings: List[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFiles] = None
    scores: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewReassessOutput:
    object: str
    id: str
    verdict: str
    created_at: datetime
    updated_at: datetime
    skill_id: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    current_revision: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevision] = None
    in_progress_revision: Optional[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevision] = None


class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFiles:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScores:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportSummary:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation(
        strengths=[mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportChanges:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportMethod:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReport:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReport(
        summary=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindings:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevision:
        return ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevision(
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
        files=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFiles:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScores:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportSummary:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation(
        strengths=[mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportChanges:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportMethod:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReport:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReport(
        summary=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindings:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevision:
        return ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevision(
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
        files=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewReassessOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewReassessOutput:
        return ManagementInstanceSkillsSecurityReviewReassessOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        verdict=data.get('verdict'),
        dismissed_at=datetime.fromisoformat(data.get('dismissed_at').replace('Z', '+00:00')) if data.get('dismissed_at') else None,
        current_revision=mapManagementInstanceSkillsSecurityReviewReassessOutputCurrentRevision.from_dict(data.get('current_revision')) if data.get('current_revision') else None,
        in_progress_revision=mapManagementInstanceSkillsSecurityReviewReassessOutputInProgressRevision.from_dict(data.get('in_progress_revision')) if data.get('in_progress_revision') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewReassessOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

