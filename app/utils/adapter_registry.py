from app.adapters.base_adapter import MusicPlatformAdapter

from typing import List, Optional


class AdapterRegistry:
    def __init__(self, adapters: List[MusicPlatformAdapter]):
        self.adapters = adapters
    

    def get_adapter_for_url(self, url: str) -> Optional[MusicPlatformAdapter]:
        for adapter in self.adapters:
            if adapter.can_handle(url):
                return adapter
        return None
    
    