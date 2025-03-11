from app.utils.adapter_registry import AdapterRegistry

import asyncio


class LinkConverterService:
    def __init__(self, adapter_registry: AdapterRegistry):
        self.adapter_registry = adapter_registry
    

    async def convert_link(self, url: str) -> dict:
        source_adapter = self.adapter_registry.get_adapter_for_url(url)
        if not source_adapter:
            raise ValueError(f"No adapter found for URL: {url}")

        metadata = await source_adapter.get_metadata(url)
        if not metadata:
            raise ValueError(f"No metadata found for URL: {url}")

        result_links = {}
        tracks = metadata if isinstance(metadata, list) else [metadata]
    
        # Объединяем ссылки из всех треков
        for track in tracks:
            if hasattr(track, "links") and track.links:
                result_links.update(track.links)

        query = f"{tracks[0].artist} - {tracks[0].title}"

        tasks = []
        for adapter in self.adapter_registry.adapters:
            if adapter.platform_name != source_adapter.platform_name:
                tasks.append(asyncio.create_task(adapter.search(query)))
            else:
                tasks.append(asyncio.create_task(asyncio.sleep(0, result=None)))
    
        search_results = await asyncio.gather(*tasks)

        for adapter, link in zip(self.adapter_registry.adapters, search_results):
            if adapter.platform_name != source_adapter.platform_name and link:
                result_links[adapter.platform_name] = link

        return {
            "source": url,
            "links": result_links
        }