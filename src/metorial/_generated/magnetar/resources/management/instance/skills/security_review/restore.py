from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation:
    strengths: List[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths]
    weaknesses: List[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges:
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport:
    behaviors: List[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors]
    resolved_findings: List[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings]
    summary: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary] = None
    provenance: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance] = None
    implementation: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation] = None
    changes: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges] = None
    method: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport
    findings: List[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles] = None
    scores: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation:
    strengths: List[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths]
    weaknesses: List[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges:
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport:
    behaviors: List[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors]
    resolved_findings: List[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings]
    summary: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary] = None
    provenance: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance] = None
    implementation: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation] = None
    changes: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges] = None
    method: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport
    findings: List[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles] = None
    scores: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRestoreOutput:
    object: str
    id: str
    verdict: str
    created_at: datetime
    updated_at: datetime
    skill_id: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    current_revision: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevision] = None
    in_progress_revision: Optional[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevision] = None


class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation(
        strengths=[mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport(
        summary=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevision:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevision(
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
        files=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation(
        strengths=[mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport(
        summary=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevision:
        return ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevision(
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
        files=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRestoreOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRestoreOutput:
        return ManagementInstanceSkillsSecurityReviewRestoreOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        verdict=data.get('verdict'),
        dismissed_at=datetime.fromisoformat(data.get('dismissed_at').replace('Z', '+00:00')) if data.get('dismissed_at') else None,
        current_revision=mapManagementInstanceSkillsSecurityReviewRestoreOutputCurrentRevision.from_dict(data.get('current_revision')) if data.get('current_revision') else None,
        in_progress_revision=mapManagementInstanceSkillsSecurityReviewRestoreOutputInProgressRevision.from_dict(data.get('in_progress_revision')) if data.get('in_progress_revision') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRestoreOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

