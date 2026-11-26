from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsProvider:
    id: str
    slug: str
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsModel:
    id: str
    slug: str
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingText:
    cache_write: List[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImage:
    cache_write: List[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio:
    cache_write: List[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo:
    cache_write: List[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers:
    min_input_tokens: float
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits:
    modality: str
    direction: str
    unit: str
    price: float
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates:
    cache_write: List[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions:
    label: str
    description: str
    modality: str
    rates: DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricing:
    currency: str
    context_tiers: List[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers]
    units: List[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits]
    conditions: List[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions]
    text: Optional[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingText] = None
    image: Optional[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImage] = None
    audio: Optional[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio] = None
    video: Optional[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo] = None
    web_search_per_1_k: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsModalities:
    input: List[str]
    output: List[str]
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning] = None
    prompt_caching: Optional[DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItemsVariant:
    free: bool
    serving: Optional[str] = None
    reasoning: Optional[str] = None
    quantization: Optional[str] = None
    region: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputItems:
    object: str
    id: str
    pinned_model: str
    vendor_model_id: str
    display_name: str
    status: str
    provider: DashboardInstanceAiGatewayModelOfferingsListOutputItemsProvider
    apis: List[str]
    modalities: DashboardInstanceAiGatewayModelOfferingsListOutputItemsModalities
    capabilities: DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilities
    variant: DashboardInstanceAiGatewayModelOfferingsListOutputItemsVariant
    model: Optional[DashboardInstanceAiGatewayModelOfferingsListOutputItemsModel] = None
    pricing: Optional[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricing] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayModelOfferingsListOutput:
    object: str
    items: List[DashboardInstanceAiGatewayModelOfferingsListOutputItems]
    pagination: DashboardInstanceAiGatewayModelOfferingsListOutputPagination


class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsProvider:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsProvider(
        id=data.get('id'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsModel:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsModel(
        id=data.get('id'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingText:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingText:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingText(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingText, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImage:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImage(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers(
        min_input_tokens=data.get('min_input_tokens'),
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits(
        modality=data.get('modality'),
        direction=data.get('direction'),
        unit=data.get('unit'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions(
        label=data.get('label'),
        description=data.get('description'),
        modality=data.get('modality'),
        rates=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates.from_dict(data.get('rates')) if data.get('rates') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricing:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricing:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricing(
        currency=data.get('currency'),
        text=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingText.from_dict(data.get('text')) if data.get('text') else None,
        image=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingImage.from_dict(data.get('image')) if data.get('image') else None,
        audio=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio.from_dict(data.get('audio')) if data.get('audio') else None,
        video=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo.from_dict(data.get('video')) if data.get('video') else None,
        context_tiers=[mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers.from_dict(item) for item in data.get('context_tiers', []) if item],
        units=[mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits.from_dict(item) for item in data.get('units', []) if item],
        web_search_per_1_k=data.get('web_search_per_1k'),
        conditions=[mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions.from_dict(item) for item in data.get('conditions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsPricing, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsModalities:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilities:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItemsVariant:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItemsVariant(
        serving=data.get('serving'),
        reasoning=data.get('reasoning'),
        quantization=data.get('quantization'),
        free=data.get('free'),
        region=data.get('region')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItemsVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputItems:
        return DashboardInstanceAiGatewayModelOfferingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        pinned_model=data.get('pinned_model'),
        vendor_model_id=data.get('vendor_model_id'),
        display_name=data.get('display_name'),
        status=data.get('status'),
        provider=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        model=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsModel.from_dict(data.get('model')) if data.get('model') else None,
        apis=data.get('apis', []),
        pricing=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsPricing.from_dict(data.get('pricing')) if data.get('pricing') else None,
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None,
        variant=mapDashboardInstanceAiGatewayModelOfferingsListOutputItemsVariant.from_dict(data.get('variant')) if data.get('variant') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutputPagination:
        return DashboardInstanceAiGatewayModelOfferingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelOfferingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListOutput:
        return DashboardInstanceAiGatewayModelOfferingsListOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceAiGatewayModelOfferingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceAiGatewayModelOfferingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayModelOfferingsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    model_id: Optional[str] = None
    provider: Optional[str] = None


class mapDashboardInstanceAiGatewayModelOfferingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelOfferingsListQuery:
        return DashboardInstanceAiGatewayModelOfferingsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        model_id=data.get('model_id'),
        provider=data.get('provider')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelOfferingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

