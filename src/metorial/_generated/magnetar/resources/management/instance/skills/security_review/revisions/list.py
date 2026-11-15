from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance:
    class_: str
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors:
    tag: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation:
    strengths: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths]
    weaknesses: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings:
    key: str
    reason: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges:
    body: str
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReport:
    behaviors: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors]
    resolved_findings: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings]
    summary: Optional[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary] = None
    provenance: Optional[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance] = None
    implementation: Optional[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation] = None
    changes: Optional[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges] = None
    method: Optional[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputItems:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReport
    findings: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles] = None
    scores: Optional[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListOutput:
    items: List[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItems]
    pagination: ManagementInstanceSkillsSecurityReviewRevisionsListOutputPagination


class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScores:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation(
        strengths=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReport:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReport(
        summary=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputItems:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputItems(
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
        files=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItemsFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutputPagination:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsSecurityReviewRevisionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListOutput:
        return ManagementInstanceSkillsSecurityReviewRevisionsListOutput(
        items=[mapManagementInstanceSkillsSecurityReviewRevisionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsSecurityReviewRevisionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsSecurityReviewRevisionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceSkillsSecurityReviewRevisionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsSecurityReviewRevisionsListQuery:
        return ManagementInstanceSkillsSecurityReviewRevisionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsSecurityReviewRevisionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

