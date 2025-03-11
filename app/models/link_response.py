from typing import Dict
from pydantic import BaseModel, HttpUrl

class LinkResponse(BaseModel):
    source: HttpUrl
    links: Dict[str, HttpUrl]
