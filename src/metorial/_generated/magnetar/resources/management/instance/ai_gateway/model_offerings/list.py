from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsProvider:
    id: str
    slug: str
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsModel:
    id: str
    slug: str
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingText:
    cache_write: List[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImage:
    cache_write: List[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio:
    cache_write: List[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo:
    cache_write: List[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers:
    min_input_tokens: float
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits:
    modality: str
    direction: str
    unit: str
    price: float
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite:
    price: float
    ttl: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates:
    cache_write: List[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite]
    input: Optional[float] = None
    output: Optional[float] = None
    cache_read: Optional[float] = None
    reasoning: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions:
    label: str
    description: str
    modality: str
    rates: ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricing:
    currency: str
    context_tiers: List[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers]
    units: List[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits]
    conditions: List[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions]
    text: Optional[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingText] = None
    image: Optional[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImage] = None
    audio: Optional[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio] = None
    video: Optional[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo] = None
    web_search_per_1_k: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsModalities:
    input: List[str]
    output: List[str]
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning] = None
    prompt_caching: Optional[ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItemsVariant:
    free: bool
    serving: Optional[str] = None
    reasoning: Optional[str] = None
    quantization: Optional[str] = None
    region: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputItems:
    object: str
    id: str
    pinned_model: str
    vendor_model_id: str
    display_name: str
    status: str
    provider: ManagementInstanceAiGatewayModelOfferingsListOutputItemsProvider
    apis: List[str]
    modalities: ManagementInstanceAiGatewayModelOfferingsListOutputItemsModalities
    capabilities: ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilities
    variant: ManagementInstanceAiGatewayModelOfferingsListOutputItemsVariant
    model: Optional[ManagementInstanceAiGatewayModelOfferingsListOutputItemsModel] = None
    pricing: Optional[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricing] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayModelOfferingsListOutput:
    object: str
    items: List[ManagementInstanceAiGatewayModelOfferingsListOutputItems]
    pagination: ManagementInstanceAiGatewayModelOfferingsListOutputPagination


class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsProvider:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsProvider(
        id=data.get('id'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsModel:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsModel(
        id=data.get('id'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingText:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingText:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingText(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingTextCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingText, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImage:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImage(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImageCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudioCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideoCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers(
        min_input_tokens=data.get('min_input_tokens'),
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits(
        modality=data.get('modality'),
        direction=data.get('direction'),
        unit=data.get('unit'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite(
        ttl=data.get('ttl'),
        price=data.get('price')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates(
        input=data.get('input'),
        output=data.get('output'),
        cache_read=data.get('cache_read'),
        cache_write=[mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRatesCacheWrite.from_dict(item) for item in data.get('cache_write', []) if item],
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions(
        label=data.get('label'),
        description=data.get('description'),
        modality=data.get('modality'),
        rates=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditionsRates.from_dict(data.get('rates')) if data.get('rates') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricing:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricing:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricing(
        currency=data.get('currency'),
        text=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingText.from_dict(data.get('text')) if data.get('text') else None,
        image=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingImage.from_dict(data.get('image')) if data.get('image') else None,
        audio=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingAudio.from_dict(data.get('audio')) if data.get('audio') else None,
        video=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingVideo.from_dict(data.get('video')) if data.get('video') else None,
        context_tiers=[mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingContextTiers.from_dict(item) for item in data.get('context_tiers', []) if item],
        units=[mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingUnits.from_dict(item) for item in data.get('units', []) if item],
        web_search_per_1_k=data.get('web_search_per_1k'),
        conditions=[mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricingConditions.from_dict(item) for item in data.get('conditions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsPricing, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsModalities:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilities:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItemsVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItemsVariant:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItemsVariant(
        serving=data.get('serving'),
        reasoning=data.get('reasoning'),
        quantization=data.get('quantization'),
        free=data.get('free'),
        region=data.get('region')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItemsVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputItems:
        return ManagementInstanceAiGatewayModelOfferingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        pinned_model=data.get('pinned_model'),
        vendor_model_id=data.get('vendor_model_id'),
        display_name=data.get('display_name'),
        status=data.get('status'),
        provider=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        model=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsModel.from_dict(data.get('model')) if data.get('model') else None,
        apis=data.get('apis', []),
        pricing=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsPricing.from_dict(data.get('pricing')) if data.get('pricing') else None,
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None,
        variant=mapManagementInstanceAiGatewayModelOfferingsListOutputItemsVariant.from_dict(data.get('variant')) if data.get('variant') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutputPagination:
        return ManagementInstanceAiGatewayModelOfferingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelOfferingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListOutput:
        return ManagementInstanceAiGatewayModelOfferingsListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceAiGatewayModelOfferingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceAiGatewayModelOfferingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayModelOfferingsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    model_id: Optional[str] = None
    provider: Optional[str] = None


class mapManagementInstanceAiGatewayModelOfferingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelOfferingsListQuery:
        return ManagementInstanceAiGatewayModelOfferingsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        model_id=data.get('model_id'),
        provider=data.get('provider')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelOfferingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

