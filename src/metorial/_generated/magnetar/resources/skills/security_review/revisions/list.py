from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: SkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportProvenance:
    class_: str
    body: str
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportBehaviors:
    tag: str
    body: str
    evidence: List[SkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence]
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence]
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence]
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportImplementation:
    strengths: List[SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths]
    weaknesses: List[SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses]
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings:
    key: str
    reason: str
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportChanges:
    body: str
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsReport:
    behaviors: List[SkillsSecurityReviewRevisionsListOutputItemsReportBehaviors]
    resolved_findings: List[SkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings]
    summary: Optional[SkillsSecurityReviewRevisionsListOutputItemsReportSummary] = None
    provenance: Optional[SkillsSecurityReviewRevisionsListOutputItemsReportProvenance] = None
    implementation: Optional[SkillsSecurityReviewRevisionsListOutputItemsReportImplementation] = None
    changes: Optional[SkillsSecurityReviewRevisionsListOutputItemsReportChanges] = None
    method: Optional[SkillsSecurityReviewRevisionsListOutputItemsReportMethod] = None
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRevisionsListOutputItemsFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class SkillsSecurityReviewRevisionsListOutputItems:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: SkillsSecurityReviewRevisionsListOutputItemsReport
    findings: List[SkillsSecurityReviewRevisionsListOutputItemsFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[SkillsSecurityReviewRevisionsListOutputItemsFiles] = None
    scores: Optional[SkillsSecurityReviewRevisionsListOutputItemsScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsSecurityReviewRevisionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class SkillsSecurityReviewRevisionsListOutput:
    object: str
    items: List[SkillsSecurityReviewRevisionsListOutputItems]
    pagination: SkillsSecurityReviewRevisionsListOutputPagination


class mapSkillsSecurityReviewRevisionsListOutputItemsFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsFiles:
        return SkillsSecurityReviewRevisionsListOutputItemsFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts:
        return SkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsScores:
        return SkillsSecurityReviewRevisionsListOutputItemsScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportSummary:
        return SkillsSecurityReviewRevisionsListOutputItemsReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportProvenance:
        return SkillsSecurityReviewRevisionsListOutputItemsReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence:
        return SkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportBehaviors:
        return SkillsSecurityReviewRevisionsListOutputItemsReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence:
        return SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths:
        return SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence:
        return SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses:
        return SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportImplementation:
        return SkillsSecurityReviewRevisionsListOutputItemsReportImplementation(
        strengths=[mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings:
        return SkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportChanges:
        return SkillsSecurityReviewRevisionsListOutputItemsReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReportMethod:
        return SkillsSecurityReviewRevisionsListOutputItemsReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsReport:
        return SkillsSecurityReviewRevisionsListOutputItemsReport(
        summary=mapSkillsSecurityReviewRevisionsListOutputItemsReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapSkillsSecurityReviewRevisionsListOutputItemsReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapSkillsSecurityReviewRevisionsListOutputItemsReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapSkillsSecurityReviewRevisionsListOutputItemsReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapSkillsSecurityReviewRevisionsListOutputItemsReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence:
        return SkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItemsFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItemsFindings:
        return SkillsSecurityReviewRevisionsListOutputItemsFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItemsFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputItems:
        return SkillsSecurityReviewRevisionsListOutputItems(
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
        files=mapSkillsSecurityReviewRevisionsListOutputItemsFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapSkillsSecurityReviewRevisionsListOutputItemsScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapSkillsSecurityReviewRevisionsListOutputItemsReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapSkillsSecurityReviewRevisionsListOutputItemsFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutputPagination:
        return SkillsSecurityReviewRevisionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListOutput:
        return SkillsSecurityReviewRevisionsListOutput(
        object=data.get('object'),
        items=[mapSkillsSecurityReviewRevisionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsSecurityReviewRevisionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsSecurityReviewRevisionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapSkillsSecurityReviewRevisionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsListQuery:
        return SkillsSecurityReviewRevisionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

