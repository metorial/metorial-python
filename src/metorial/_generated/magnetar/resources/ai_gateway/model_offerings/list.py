from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayModelOfferingsListOutputItemsProvider:
    id: str
    slug: str
@dataclass
class AiGatewayModelOfferingsListOutputItemsModel:
    id: str
    slug: str
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingText:
    cache_write: List[AiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingImage:
    cache_write: List[AiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingAudio:
    cache_write: List[AiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingVideo:
    cache_write: List[AiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingContextTiers:
    min_input_tokens: float
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingUnits:
    modality: str
    direction: str
    unit: str
    price: float
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingConditionsRates:
    cache_write: List[AiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricingConditions:
    label: str
    description: str
    modality: str
    rates: AiGatewayModelOfferingsListOutputItemsPricingConditionsRates
@dataclass
class AiGatewayModelOfferingsListOutputItemsPricing:
    currency: str
    context_tiers: List[AiGatewayModelOfferingsListOutputItemsPricingContextTiers]
    units: List[AiGatewayModelOfferingsListOutputItemsPricingUnits]
    conditions: List[AiGatewayModelOfferingsListOutputItemsPricingConditions]
    text: Optional[AiGatewayModelOfferingsListOutputItemsPricingText] = None
    image: Optional[AiGatewayModelOfferingsListOutputItemsPricingImage] = None
    audio: Optional[AiGatewayModelOfferingsListOutputItemsPricingAudio] = None
    video: Optional[AiGatewayModelOfferingsListOutputItemsPricingVideo] = None
    web_search_per_1_k: Optional[float] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsModalities:
    input: List[str]
    output: List[str]
@dataclass
class AiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class AiGatewayModelOfferingsListOutputItemsCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[AiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning] = None
    prompt_caching: Optional[AiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching] = None
@dataclass
class AiGatewayModelOfferingsListOutputItemsVariant:
    free: bool
    serving: Optional[str] = None
    reasoning: Optional[str] = None
    quantization: Optional[str] = None
    region: Optional[str] = None
@dataclass
class AiGatewayModelOfferingsListOutputItems:
    object: str
    id: str
    pinned_model: str
    vendor_model_id: str
    display_name: str
    status: str
    provider: AiGatewayModelOfferingsListOutputItemsProvider
    apis: List[str]
    modalities: AiGatewayModelOfferingsListOutputItemsModalities
    capabilities: AiGatewayModelOfferingsListOutputItemsCapabilities
    variant: AiGatewayModelOfferingsListOutputItemsVariant
    model: Optional[AiGatewayModelOfferingsListOutputItemsModel] = None
    pricing: Optional[AiGatewayModelOfferingsListOutputItemsPricing] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None
@dataclass
class AiGatewayModelOfferingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class AiGatewayModelOfferingsListOutput:
    object: str
    items: List[AiGatewayModelOfferingsListOutputItems]
    pagination: AiGatewayModelOfferingsListOutputPagination


class mapAiGatewayModelOfferingsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsProvider:
        return AiGatewayModelOfferingsListOutputItemsProvider(
        id=data.get('id'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsModel:
        return AiGatewayModelOfferingsListOutputItemsModel(
        id=data.get('id'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite:
        return AiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingText:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingText:
        return AiGatewayModelOfferingsListOutputItemsPricingText(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingText, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite:
        return AiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingImage:
        return AiGatewayModelOfferingsListOutputItemsPricingImage(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite:
        return AiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingAudio:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingAudio:
        return AiGatewayModelOfferingsListOutputItemsPricingAudio(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingAudio, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite:
        return AiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingVideo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingVideo:
        return AiGatewayModelOfferingsListOutputItemsPricingVideo(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingVideo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingContextTiers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingContextTiers:
        return AiGatewayModelOfferingsListOutputItemsPricingContextTiers(
        min_input_tokens=data.get('min_input_tokens'),
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingContextTiers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingUnits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingUnits:
        return AiGatewayModelOfferingsListOutputItemsPricingUnits(
        modality=data.get('modality'),
        direction=data.get('direction'),
        unit=data.get('unit'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingUnits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite:
        return AiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingConditionsRates:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingConditionsRates:
        return AiGatewayModelOfferingsListOutputItemsPricingConditionsRates(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingConditionsRates, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricingConditions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricingConditions:
        return AiGatewayModelOfferingsListOutputItemsPricingConditions(
        label=data.get('label'),
        description=data.get('description'),
        modality=data.get('modality'),
        rates=mapAiGatewayModelOfferingsListOutputItemsPricingConditionsRates.from_dict(data.get('rates')) if data.get('rates') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricingConditions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsPricing:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsPricing:
        return AiGatewayModelOfferingsListOutputItemsPricing(
        currency=data.get('currency'),
        text=mapAiGatewayModelOfferingsListOutputItemsPricingText.from_dict(data.get('text')) if data.get('text') else None,
        image=mapAiGatewayModelOfferingsListOutputItemsPricingImage.from_dict(data.get('image')) if data.get('image') else None,
        audio=mapAiGatewayModelOfferingsListOutputItemsPricingAudio.from_dict(data.get('audio')) if data.get('audio') else None,
        video=mapAiGatewayModelOfferingsListOutputItemsPricingVideo.from_dict(data.get('video')) if data.get('video') else None,
        context_tiers=[mapAiGatewayModelOfferingsListOutputItemsPricingContextTiers.from_dict(item) for item in data.get('context_tiers', []) if item],
        units=[mapAiGatewayModelOfferingsListOutputItemsPricingUnits.from_dict(item) for item in data.get('units', []) if item],
        web_search_per_1_k=data.get('web_search_per_1k'),
        conditions=[mapAiGatewayModelOfferingsListOutputItemsPricingConditions.from_dict(item) for item in data.get('conditions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsPricing, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsModalities:
        return AiGatewayModelOfferingsListOutputItemsModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning:
        return AiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching:
        return AiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsCapabilities:
        return AiGatewayModelOfferingsListOutputItemsCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItemsVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItemsVariant:
        return AiGatewayModelOfferingsListOutputItemsVariant(
        serving=data.get('serving'),
        reasoning=data.get('reasoning'),
        quantization=data.get('quantization'),
        free=data.get('free'),
        region=data.get('region')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItemsVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputItems:
        return AiGatewayModelOfferingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        pinned_model=data.get('pinned_model'),
        vendor_model_id=data.get('vendor_model_id'),
        display_name=data.get('display_name'),
        status=data.get('status'),
        provider=mapAiGatewayModelOfferingsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        model=mapAiGatewayModelOfferingsListOutputItemsModel.from_dict(data.get('model')) if data.get('model') else None,
        apis=data.get('apis', []),
        pricing=mapAiGatewayModelOfferingsListOutputItemsPricing.from_dict(data.get('pricing')) if data.get('pricing') else None,
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapAiGatewayModelOfferingsListOutputItemsModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapAiGatewayModelOfferingsListOutputItemsCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None,
        variant=mapAiGatewayModelOfferingsListOutputItemsVariant.from_dict(data.get('variant')) if data.get('variant') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutputPagination:
        return AiGatewayModelOfferingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelOfferingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListOutput:
        return AiGatewayModelOfferingsListOutput(
        object=data.get('object'),
        items=[mapAiGatewayModelOfferingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapAiGatewayModelOfferingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayModelOfferingsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    model_id: Optional[str] = None
    provider: Optional[str] = None


class mapAiGatewayModelOfferingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelOfferingsListQuery:
        return AiGatewayModelOfferingsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        model_id=data.get('model_id'),
        provider=data.get('provider')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelOfferingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

