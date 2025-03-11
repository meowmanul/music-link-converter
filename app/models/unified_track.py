from pydantic import BaseModel, HttpUrl
from typing import Dict, Optional

class TrackMetadata(BaseModel):
    artist: str
    title: str

class UnifiedTrack(TrackMetadata):
    thumbnail_url: Optional[HttpUrl] = None
    links: Dict[str, HttpUrl] = {}