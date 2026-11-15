from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: SkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence]
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence]
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence]
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportImplementation:
    strengths: List[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths]
    weaknesses: List[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses]
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportChanges:
    body: str
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionReport:
    behaviors: List[SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors]
    resolved_findings: List[SkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings]
    summary: Optional[SkillsSecurityReviewGetOutputCurrentRevisionReportSummary] = None
    provenance: Optional[SkillsSecurityReviewGetOutputCurrentRevisionReportProvenance] = None
    implementation: Optional[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementation] = None
    changes: Optional[SkillsSecurityReviewGetOutputCurrentRevisionReportChanges] = None
    method: Optional[SkillsSecurityReviewGetOutputCurrentRevisionReportMethod] = None
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[SkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class SkillsSecurityReviewGetOutputCurrentRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: SkillsSecurityReviewGetOutputCurrentRevisionReport
    findings: List[SkillsSecurityReviewGetOutputCurrentRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[SkillsSecurityReviewGetOutputCurrentRevisionFiles] = None
    scores: Optional[SkillsSecurityReviewGetOutputCurrentRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: SkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence]
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence]
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence]
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportImplementation:
    strengths: List[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths]
    weaknesses: List[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses]
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportChanges:
    body: str
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionReport:
    behaviors: List[SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors]
    resolved_findings: List[SkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings]
    summary: Optional[SkillsSecurityReviewGetOutputInProgressRevisionReportSummary] = None
    provenance: Optional[SkillsSecurityReviewGetOutputInProgressRevisionReportProvenance] = None
    implementation: Optional[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementation] = None
    changes: Optional[SkillsSecurityReviewGetOutputInProgressRevisionReportChanges] = None
    method: Optional[SkillsSecurityReviewGetOutputInProgressRevisionReportMethod] = None
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[SkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class SkillsSecurityReviewGetOutputInProgressRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: SkillsSecurityReviewGetOutputInProgressRevisionReport
    findings: List[SkillsSecurityReviewGetOutputInProgressRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[SkillsSecurityReviewGetOutputInProgressRevisionFiles] = None
    scores: Optional[SkillsSecurityReviewGetOutputInProgressRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsSecurityReviewGetOutput:
    object: str
    id: str
    verdict: str
    created_at: datetime
    updated_at: datetime
    skill_id: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    current_revision: Optional[SkillsSecurityReviewGetOutputCurrentRevision] = None
    in_progress_revision: Optional[SkillsSecurityReviewGetOutputInProgressRevision] = None


class mapSkillsSecurityReviewGetOutputCurrentRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionFiles:
        return SkillsSecurityReviewGetOutputCurrentRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts:
        return SkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionScores:
        return SkillsSecurityReviewGetOutputCurrentRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapSkillsSecurityReviewGetOutputCurrentRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportSummary:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportProvenance:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportImplementation:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportImplementation(
        strengths=[mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportChanges:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReportMethod:
        return SkillsSecurityReviewGetOutputCurrentRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionReport:
        return SkillsSecurityReviewGetOutputCurrentRevisionReport(
        summary=mapSkillsSecurityReviewGetOutputCurrentRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapSkillsSecurityReviewGetOutputCurrentRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapSkillsSecurityReviewGetOutputCurrentRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapSkillsSecurityReviewGetOutputCurrentRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapSkillsSecurityReviewGetOutputCurrentRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapSkillsSecurityReviewGetOutputCurrentRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapSkillsSecurityReviewGetOutputCurrentRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence:
        return SkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevisionFindings:
        return SkillsSecurityReviewGetOutputCurrentRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapSkillsSecurityReviewGetOutputCurrentRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputCurrentRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputCurrentRevision:
        return SkillsSecurityReviewGetOutputCurrentRevision(
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
        files=mapSkillsSecurityReviewGetOutputCurrentRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapSkillsSecurityReviewGetOutputCurrentRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapSkillsSecurityReviewGetOutputCurrentRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapSkillsSecurityReviewGetOutputCurrentRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputCurrentRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionFiles:
        return SkillsSecurityReviewGetOutputInProgressRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts:
        return SkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionScores:
        return SkillsSecurityReviewGetOutputInProgressRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapSkillsSecurityReviewGetOutputInProgressRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportSummary:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportProvenance:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportImplementation:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportImplementation(
        strengths=[mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportChanges:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReportMethod:
        return SkillsSecurityReviewGetOutputInProgressRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionReport:
        return SkillsSecurityReviewGetOutputInProgressRevisionReport(
        summary=mapSkillsSecurityReviewGetOutputInProgressRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapSkillsSecurityReviewGetOutputInProgressRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapSkillsSecurityReviewGetOutputInProgressRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapSkillsSecurityReviewGetOutputInProgressRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapSkillsSecurityReviewGetOutputInProgressRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapSkillsSecurityReviewGetOutputInProgressRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapSkillsSecurityReviewGetOutputInProgressRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence:
        return SkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevisionFindings:
        return SkillsSecurityReviewGetOutputInProgressRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapSkillsSecurityReviewGetOutputInProgressRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutputInProgressRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutputInProgressRevision:
        return SkillsSecurityReviewGetOutputInProgressRevision(
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
        files=mapSkillsSecurityReviewGetOutputInProgressRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapSkillsSecurityReviewGetOutputInProgressRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapSkillsSecurityReviewGetOutputInProgressRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapSkillsSecurityReviewGetOutputInProgressRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutputInProgressRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewGetOutput:
        return SkillsSecurityReviewGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        verdict=data.get('verdict'),
        dismissed_at=datetime.fromisoformat(data.get('dismissed_at').replace('Z', '+00:00')) if data.get('dismissed_at') else None,
        current_revision=mapSkillsSecurityReviewGetOutputCurrentRevision.from_dict(data.get('current_revision')) if data.get('current_revision') else None,
        in_progress_revision=mapSkillsSecurityReviewGetOutputInProgressRevision.from_dict(data.get('in_progress_revision')) if data.get('in_progress_revision') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

