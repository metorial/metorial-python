from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance:
    class_: str
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors:
    tag: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation:
    strengths: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths]
    weaknesses: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings:
    key: str
    reason: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges:
    body: str
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReport:
    behaviors: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors]
    resolved_findings: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings]
    summary: Optional[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary] = None
    provenance: Optional[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance] = None
    implementation: Optional[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation] = None
    changes: Optional[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges] = None
    method: Optional[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputItems:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReport
    findings: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles] = None
    scores: Optional[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListOutput:
    items: List[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItems]
    pagination: DashboardInstanceSkillsSecurityReviewRevisionsListOutputPagination


class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScores:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation(
        strengths=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReport:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReport(
        summary=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputItems:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputItems(
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
        files=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutputPagination:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsSecurityReviewRevisionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutput:
        return DashboardInstanceSkillsSecurityReviewRevisionsListOutput(
        items=[mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSkillsSecurityReviewRevisionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsSecurityReviewRevisionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceSkillsSecurityReviewRevisionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsSecurityReviewRevisionsListQuery:
        return DashboardInstanceSkillsSecurityReviewRevisionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsSecurityReviewRevisionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

