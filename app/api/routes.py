from fastapi import APIRouter, Depends, HTTPException

from app.models.link_response import LinkResponse
from app.models.link_request import LinkRequest

from app.services.link_converter_service import LinkConverterService

from app.utils.adapter_loader import load_adapters
from app.utils.adapter_registry import AdapterRegistry

from typing import Annotated


router = APIRouter()


adapters = load_adapters()
adapter_registry = AdapterRegistry(adapters)
link_converter_service = LinkConverterService(adapter_registry)


@router.post("/convert", response_model=LinkResponse)
async def convert_link(request: Annotated[LinkRequest, Depends()]):
    try:
        result = await link_converter_service.convert_link(request.url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return result