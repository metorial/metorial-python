from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsSecurityReviewRevisionsGetOutputFiles:
    total: float
    analyzed: float
    kinds: Dict[str, float]
@dataclass
class SkillsSecurityReviewRevisionsGetOutputScoresFindingCounts:
    info: float
    low: float
    medium: float
    high: float
    critical: float
@dataclass
class SkillsSecurityReviewRevisionsGetOutputScores:
    security_score: float
    band: str
    exposure: str
    risk: str
    confidence: str
    lethal_trifecta: bool
    headline: List[str]
    finding_counts: SkillsSecurityReviewRevisionsGetOutputScoresFindingCounts
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportSummary:
    text: str
    trust_note: str
    exposure_note: str
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportProvenance:
    class_: str
    body: str
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportBehaviors:
    tag: str
    body: str
    evidence: List[SkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence]
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence]
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses:
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence]
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportImplementation:
    strengths: List[SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths]
    weaknesses: List[SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses]
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportResolvedFindings:
    key: str
    reason: str
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportChanges:
    body: str
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReportMethod:
    included: List[str]
    out_of_scope: List[str]
    limitations: List[str]
@dataclass
class SkillsSecurityReviewRevisionsGetOutputReport:
    behaviors: List[SkillsSecurityReviewRevisionsGetOutputReportBehaviors]
    resolved_findings: List[SkillsSecurityReviewRevisionsGetOutputReportResolvedFindings]
    summary: Optional[SkillsSecurityReviewRevisionsGetOutputReportSummary] = None
    provenance: Optional[SkillsSecurityReviewRevisionsGetOutputReportProvenance] = None
    implementation: Optional[SkillsSecurityReviewRevisionsGetOutputReportImplementation] = None
    changes: Optional[SkillsSecurityReviewRevisionsGetOutputReportChanges] = None
    method: Optional[SkillsSecurityReviewRevisionsGetOutputReportMethod] = None
@dataclass
class SkillsSecurityReviewRevisionsGetOutputFindingsEvidence:
    type: str
    path: str
    lines: Optional[List[float]] = None
@dataclass
class SkillsSecurityReviewRevisionsGetOutputFindings:
    key: str
    kind: str
    category: str
    severity: str
    change: str
    title: str
    body: str
    evidence: List[SkillsSecurityReviewRevisionsGetOutputFindingsEvidence]
    recommendation: Optional[str] = None
@dataclass
class SkillsSecurityReviewRevisionsGetOutput:
    object: str
    id: str
    security_review_id: str
    number: float
    status: str
    ai_generated: bool
    trigger: str
    report: SkillsSecurityReviewRevisionsGetOutputReport
    findings: List[SkillsSecurityReviewRevisionsGetOutputFindings]
    created_at: datetime
    skill_version_id: Optional[str] = None
    stage: Optional[str] = None
    block_reason: Optional[str] = None
    files: Optional[SkillsSecurityReviewRevisionsGetOutputFiles] = None
    scores: Optional[SkillsSecurityReviewRevisionsGetOutputScores] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapSkillsSecurityReviewRevisionsGetOutputFiles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputFiles:
        return SkillsSecurityReviewRevisionsGetOutputFiles(
        total=data.get('total'),
        analyzed=data.get('analyzed'),
        kinds=data.get('kinds')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputFiles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputScoresFindingCounts:
        return SkillsSecurityReviewRevisionsGetOutputScoresFindingCounts(
        info=data.get('info'),
        low=data.get('low'),
        medium=data.get('medium'),
        high=data.get('high'),
        critical=data.get('critical')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputScoresFindingCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputScores:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputScores:
        return SkillsSecurityReviewRevisionsGetOutputScores(
        security_score=data.get('security_score'),
        band=data.get('band'),
        exposure=data.get('exposure'),
        risk=data.get('risk'),
        confidence=data.get('confidence'),
        lethal_trifecta=data.get('lethal_trifecta'),
        headline=data.get('headline', []),
        finding_counts=mapSkillsSecurityReviewRevisionsGetOutputScoresFindingCounts.from_dict(data.get('finding_counts')) if data.get('finding_counts') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputScores, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportSummary:
        return SkillsSecurityReviewRevisionsGetOutputReportSummary(
        text=data.get('text'),
        trust_note=data.get('trust_note'),
        exposure_note=data.get('exposure_note')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportProvenance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportProvenance:
        return SkillsSecurityReviewRevisionsGetOutputReportProvenance(
        class_=data.get('class'),
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportProvenance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence:
        return SkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportBehaviors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportBehaviors:
        return SkillsSecurityReviewRevisionsGetOutputReportBehaviors(
        tag=data.get('tag'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRevisionsGetOutputReportBehaviorsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportBehaviors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence:
        return SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths:
        return SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengthsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence:
        return SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses:
        return SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses(
        title=data.get('title'),
        body=data.get('body'),
        evidence=[mapSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknessesEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportImplementation:
        return SkillsSecurityReviewRevisionsGetOutputReportImplementation(
        strengths=[mapSkillsSecurityReviewRevisionsGetOutputReportImplementationStrengths.from_dict(item) for item in data.get('strengths', []) if item],
        weaknesses=[mapSkillsSecurityReviewRevisionsGetOutputReportImplementationWeaknesses.from_dict(item) for item in data.get('weaknesses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportResolvedFindings:
        return SkillsSecurityReviewRevisionsGetOutputReportResolvedFindings(
        key=data.get('key'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportResolvedFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportChanges:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportChanges:
        return SkillsSecurityReviewRevisionsGetOutputReportChanges(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportChanges, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReportMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReportMethod:
        return SkillsSecurityReviewRevisionsGetOutputReportMethod(
        included=data.get('included', []),
        out_of_scope=data.get('out_of_scope', []),
        limitations=data.get('limitations', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReportMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputReport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputReport:
        return SkillsSecurityReviewRevisionsGetOutputReport(
        summary=mapSkillsSecurityReviewRevisionsGetOutputReportSummary.from_dict(data.get('summary')) if data.get('summary') else None,
        provenance=mapSkillsSecurityReviewRevisionsGetOutputReportProvenance.from_dict(data.get('provenance')) if data.get('provenance') else None,
        behaviors=[mapSkillsSecurityReviewRevisionsGetOutputReportBehaviors.from_dict(item) for item in data.get('behaviors', []) if item],
        implementation=mapSkillsSecurityReviewRevisionsGetOutputReportImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        resolved_findings=[mapSkillsSecurityReviewRevisionsGetOutputReportResolvedFindings.from_dict(item) for item in data.get('resolved_findings', []) if item],
        changes=mapSkillsSecurityReviewRevisionsGetOutputReportChanges.from_dict(data.get('changes')) if data.get('changes') else None,
        method=mapSkillsSecurityReviewRevisionsGetOutputReportMethod.from_dict(data.get('method')) if data.get('method') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputReport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputFindingsEvidence:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputFindingsEvidence:
        return SkillsSecurityReviewRevisionsGetOutputFindingsEvidence(
        type=data.get('type'),
        path=data.get('path'),
        lines=data.get('lines', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputFindingsEvidence, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutputFindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutputFindings:
        return SkillsSecurityReviewRevisionsGetOutputFindings(
        key=data.get('key'),
        kind=data.get('kind'),
        category=data.get('category'),
        severity=data.get('severity'),
        change=data.get('change'),
        title=data.get('title'),
        body=data.get('body'),
        recommendation=data.get('recommendation'),
        evidence=[mapSkillsSecurityReviewRevisionsGetOutputFindingsEvidence.from_dict(item) for item in data.get('evidence', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutputFindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsSecurityReviewRevisionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsSecurityReviewRevisionsGetOutput:
        return SkillsSecurityReviewRevisionsGetOutput(
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
        files=mapSkillsSecurityReviewRevisionsGetOutputFiles.from_dict(data.get('files')) if data.get('files') else None,
        scores=mapSkillsSecurityReviewRevisionsGetOutputScores.from_dict(data.get('scores')) if data.get('scores') else None,
        report=mapSkillsSecurityReviewRevisionsGetOutputReport.from_dict(data.get('report')) if data.get('report') else None,
        findings=[mapSkillsSecurityReviewRevisionsGetOutputFindings.from_dict(item) for item in data.get('findings', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsSecurityReviewRevisionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

