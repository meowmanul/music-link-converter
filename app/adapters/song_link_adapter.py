from app.adapters.base_adapter import MusicPlatformAdapter

from app.models.unified_track import UnifiedTrack

from typing import List, Optional

from urllib.parse import quote


import httpx
import asyncio
import re


class SongLinkAdapter(MusicPlatformAdapter):
    @property
    def platform_name(self) -> str:
        return "song_link"


    def can_handle(self, url: str) -> bool:
        url_str = str(url)
        url_lower = url_str.lower()
        patterns = [
            r"open\.spotify\.com",         
            r"itunes\.apple\.com",         
            r"music\.apple\.com",          
            r"youtu\.be",                  
            r"youtube\.com",               
            r"music\.youtube\.com",        
            r"play\.google\.com",          
            r"pandora\.com",               
            r"deezer\.com",                
            r"tidal\.com",                 
            r"amazon(?:store|music)?\.com",
            r"soundcloud\.com",            
            r"napster\.com",               
            r"music\.yandex\.ru",         
            r"spinrilla\.com",             
            r"audius\.co",                 
            r"anghami\.com",               
            r"boomplay\.com",              
            r"audiomack\.com"              
        ]

        for pattern in patterns:
            if re.search(pattern, url_lower):
                return True
        return False


    async def get_metadata(self, url) -> Optional[List[UnifiedTrack]]:
        encoded_url = quote(str(url), safe='')
        request_url = f"https://api.song.link/v1-alpha.1/links?url={encoded_url}&userCountry=US&songIfSingle=true"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(request_url)
            response.raise_for_status()
            data = response.json()
        entities = data.get("entitiesByUniqueId", {})
        links_by_platform = data.get("linksByPlatform", {})

        unified_tracks: List[UnifiedTrack] = []
        
        for entity_id, entity_data in entities.items():
            title = entity_data.get("title", "")
            artist = entity_data.get("artistName", "")
            thumbnail = entity_data.get("thumbnailUrl")
    
            unified_links = {}
            for platform, link_info in links_by_platform.items():
                if link_info.get("entityUniqueId") == entity_id:
                    link_url = link_info.get("url")
                    if link_url:
                        unified_links[platform] = link_url
            
            track = UnifiedTrack(
                title=title,
                artist=artist,
                thumbnail_url=thumbnail,
                links=unified_links
            )
            unified_tracks.append(track)
        
        return unified_tracks
    

    async def search(self, query: str) -> Optional[str]:
        await asyncio.sleep(1)
        return None
