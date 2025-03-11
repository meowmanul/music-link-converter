from abc import ABC, abstractmethod
from typing import List, Optional

from app.models.unified_track import UnifiedTrack


class MusicPlatformAdapter(ABC):
    @property
    @abstractmethod
    def platform_name(self) -> str:
        """Имя платформы."""
        pass
        

    @abstractmethod
    def can_handle(self, url: str) -> bool:
        """Проверяет, может ли адаптер обработать данный URL."""
        pass


    @abstractmethod
    def get_metadata(self, url: str) -> List[UnifiedTrack]:
        """
        Извлекает метаданные (исполнитель, название) по ссылке.
        Используется для ссылки-источника.
        """
        pass


    @abstractmethod
    def search(self, query: str) -> Optional[str]:
        """
        Выполняет поиск трека по запросу и возвращает URL найденного трека на своей платформе.
        """
        pass

