from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: SkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence]
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence]
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence]
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation:
    strengths: List[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths]
    weaknesses: List[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses]
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportChanges:
    body: str
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionReport:
    behaviors: List[SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors]
    resolved_findings: List[SkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings]
    summary: Optional[SkillsSecurityReviewReassessOutputCurrentRevisionReportSummary] = None
    provenance: Optional[SkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance] = None
    implementation: Optional[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation] = None
    changes: Optional[SkillsSecurityReviewReassessOutputCurrentRevisionReportChanges] = None
    method: Optional[SkillsSecurityReviewReassessOutputCurrentRevisionReportMethod] = None
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[SkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class SkillsSecurityReviewReassessOutputCurrentRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: SkillsSecurityReviewReassessOutputCurrentRevisionReport
    findings: List[SkillsSecurityReviewReassessOutputCurrentRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[SkillsSecurityReviewReassessOutputCurrentRevisionFiles] = None
    scores: Optional[SkillsSecurityReviewReassessOutputCurrentRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: SkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence]
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence]
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence]
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation:
    strengths: List[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths]
    weaknesses: List[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses]
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportChanges:
    body: str
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionReport:
    behaviors: List[SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors]
    resolved_findings: List[SkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings]
    summary: Optional[SkillsSecurityReviewReassessOutputInProgressRevisionReportSummary] = None
    provenance: Optional[SkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance] = None
    implementation: Optional[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation] = None
    changes: Optional[SkillsSecurityReviewReassessOutputInProgressRevisionReportChanges] = None
    method: Optional[SkillsSecurityReviewReassessOutputInProgressRevisionReportMethod] = None
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[SkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class SkillsSecurityReviewReassessOutputInProgressRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: SkillsSecurityReviewReassessOutputInProgressRevisionReport
    findings: List[SkillsSecurityReviewReassessOutputInProgressRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[SkillsSecurityReviewReassessOutputInProgressRevisionFiles] = None
    scores: Optional[SkillsSecurityReviewReassessOutputInProgressRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsSecurityReviewReassessOutput:
    object: str
    id: str
    verdict: str
    created_at: datetime
    updated_at: datetime
    skill_id: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    current_revision: Optional[SkillsSecurityReviewReassessOutputCurrentRevision] = None
    in_progress_revision: Optional[SkillsSecurityReviewReassessOutputInProgressRevision] = None


class mapSkillsSecurityReviewReassessOutputCurrentRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionFiles:
        return SkillsSecurityReviewReassessOutputCurrentRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts:
        return SkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionScores:
        return SkillsSecurityReviewReassessOutputCurrentRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapSkillsSecurityReviewReassessOutputCurrentRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportSummary:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation(
        strengths=[mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportChanges:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReportMethod:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionReport:
        return SkillsSecurityReviewReassessOutputCurrentRevisionReport(
        summary=mapSkillsSecurityReviewReassessOutputCurrentRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapSkillsSecurityReviewReassessOutputCurrentRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapSkillsSecurityReviewReassessOutputCurrentRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapSkillsSecurityReviewReassessOutputCurrentRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapSkillsSecurityReviewReassessOutputCurrentRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapSkillsSecurityReviewReassessOutputCurrentRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapSkillsSecurityReviewReassessOutputCurrentRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence:
        return SkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevisionFindings:
        return SkillsSecurityReviewReassessOutputCurrentRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapSkillsSecurityReviewReassessOutputCurrentRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputCurrentRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputCurrentRevision:
        return SkillsSecurityReviewReassessOutputCurrentRevision(
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
        files=mapSkillsSecurityReviewReassessOutputCurrentRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapSkillsSecurityReviewReassessOutputCurrentRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapSkillsSecurityReviewReassessOutputCurrentRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapSkillsSecurityReviewReassessOutputCurrentRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputCurrentRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionFiles:
        return SkillsSecurityReviewReassessOutputInProgressRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts:
        return SkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionScores:
        return SkillsSecurityReviewReassessOutputInProgressRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapSkillsSecurityReviewReassessOutputInProgressRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportSummary:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation(
        strengths=[mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportChanges:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReportMethod:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionReport:
        return SkillsSecurityReviewReassessOutputInProgressRevisionReport(
        summary=mapSkillsSecurityReviewReassessOutputInProgressRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapSkillsSecurityReviewReassessOutputInProgressRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapSkillsSecurityReviewReassessOutputInProgressRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapSkillsSecurityReviewReassessOutputInProgressRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapSkillsSecurityReviewReassessOutputInProgressRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapSkillsSecurityReviewReassessOutputInProgressRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapSkillsSecurityReviewReassessOutputInProgressRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence:
        return SkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevisionFindings:
        return SkillsSecurityReviewReassessOutputInProgressRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapSkillsSecurityReviewReassessOutputInProgressRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutputInProgressRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutputInProgressRevision:
        return SkillsSecurityReviewReassessOutputInProgressRevision(
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
        files=mapSkillsSecurityReviewReassessOutputInProgressRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapSkillsSecurityReviewReassessOutputInProgressRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapSkillsSecurityReviewReassessOutputInProgressRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapSkillsSecurityReviewReassessOutputInProgressRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutputInProgressRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewReassessOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewReassessOutput:
        return SkillsSecurityReviewReassessOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        verdict=data.get('verdict'),
        dismissed_at=datetime.fromisoformat(data.get('dismissed_at').replace('Z', '+00:00')) if data.get('dismissed_at') else None,
        current_revision=mapSkillsSecurityReviewReassessOutputCurrentRevision.from_dict(data.get('current_revision')) if data.get('current_revision') else None,
        in_progress_revision=mapSkillsSecurityReviewReassessOutputInProgressRevision.from_dict(data.get('in_progress_revision')) if data.get('in_progress_revision') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewReassessOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

