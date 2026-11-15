from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: SkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence]
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence]
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence]
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation:
    strengths: List[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths]
    weaknesses: List[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses]
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges:
    body: str
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionReport:
    behaviors: List[SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors]
    resolved_findings: List[SkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings]
    summary: Optional[SkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary] = None
    provenance: Optional[SkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance] = None
    implementation: Optional[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation] = None
    changes: Optional[SkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges] = None
    method: Optional[SkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod] = None
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class SkillsSecurityReviewRestoreOutputCurrentRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: SkillsSecurityReviewRestoreOutputCurrentRevisionReport
    findings: List[SkillsSecurityReviewRestoreOutputCurrentRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[SkillsSecurityReviewRestoreOutputCurrentRevisionFiles] = None
    scores: Optional[SkillsSecurityReviewRestoreOutputCurrentRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: SkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance:
    class_: str
    body: str
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors:
    tag: str
    body: str
    evidence: List[SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence]
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence]
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence]
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation:
    strengths: List[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths]
    weaknesses: List[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses]
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings:
    key: str
    reason: str
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges:
    body: str
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionReport:
    behaviors: List[SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors]
    resolved_findings: List[SkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings]
    summary: Optional[SkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary] = None
    provenance: Optional[SkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance] = None
    implementation: Optional[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation] = None
    changes: Optional[SkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges] = None
    method: Optional[SkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod] = None
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevisionFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class SkillsSecurityReviewRestoreOutputInProgressRevision:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: SkillsSecurityReviewRestoreOutputInProgressRevisionReport
    findings: List[SkillsSecurityReviewRestoreOutputInProgressRevisionFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[SkillsSecurityReviewRestoreOutputInProgressRevisionFiles] = None
    scores: Optional[SkillsSecurityReviewRestoreOutputInProgressRevisionScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsSecurityReviewRestoreOutput:
    object: str
    id: str
    verdict: str
    created_at: datetime
    updated_at: datetime
    skill_id: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    current_revision: Optional[SkillsSecurityReviewRestoreOutputCurrentRevision] = None
    in_progress_revision: Optional[SkillsSecurityReviewRestoreOutputInProgressRevision] = None


class mapSkillsSecurityReviewRestoreOutputCurrentRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionFiles:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionScores:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapSkillsSecurityReviewRestoreOutputCurrentRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation(
        strengths=[mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionReport:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionReport(
        summary=mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapSkillsSecurityReviewRestoreOutputCurrentRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevisionFindings:
        return SkillsSecurityReviewRestoreOutputCurrentRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapSkillsSecurityReviewRestoreOutputCurrentRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputCurrentRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputCurrentRevision:
        return SkillsSecurityReviewRestoreOutputCurrentRevision(
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
        files=mapSkillsSecurityReviewRestoreOutputCurrentRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapSkillsSecurityReviewRestoreOutputCurrentRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapSkillsSecurityReviewRestoreOutputCurrentRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapSkillsSecurityReviewRestoreOutputCurrentRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputCurrentRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionFiles:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionScores:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapSkillsSecurityReviewRestoreOutputInProgressRevisionScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation(
        strengths=[mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionReport:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionReport(
        summary=mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapSkillsSecurityReviewRestoreOutputInProgressRevisionReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevisionFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevisionFindings:
        return SkillsSecurityReviewRestoreOutputInProgressRevisionFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapSkillsSecurityReviewRestoreOutputInProgressRevisionFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevisionFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutputInProgressRevision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutputInProgressRevision:
        return SkillsSecurityReviewRestoreOutputInProgressRevision(
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
        files=mapSkillsSecurityReviewRestoreOutputInProgressRevisionFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapSkillsSecurityReviewRestoreOutputInProgressRevisionScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapSkillsSecurityReviewRestoreOutputInProgressRevisionReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapSkillsSecurityReviewRestoreOutputInProgressRevisionFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutputInProgressRevision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRestoreOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRestoreOutput:
        return SkillsSecurityReviewRestoreOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        verdict=data.get('verdict'),
        dismissed_at=datetime.fromisoformat(data.get('dismissed_at').replace('Z', '+00:00')) if data.get('dismissed_at') else None,
        current_revision=mapSkillsSecurityReviewRestoreOutputCurrentRevision.from_dict(data.get('current_revision')) if data.get('current_revision') else None,
        in_progress_revision=mapSkillsSecurityReviewRestoreOutputInProgressRevision.from_dict(data.get('in_progress_revision')) if data.get('in_progress_revision') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRestoreOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

