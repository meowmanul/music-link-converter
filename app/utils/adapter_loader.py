import pkgutil
import importlib

from app.adapters.base_adapter import MusicPlatformAdapter

def load_adapters() -> list[MusicPlatformAdapter]:
    adapters = []
    package_name = "app.adapters"
    package = importlib.import_module(package_name)
    
    # Перебираем все модули внутри пакета app.adapters
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package_name}.{module_name}")
        # Ищем классы, наследующие от MusicPlatformAdapter (исключая сам базовый класс)
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if (
                isinstance(attribute, type)
                and issubclass(attribute, MusicPlatformAdapter)
                and attribute is not MusicPlatformAdapter
            ):
                adapters.append(attribute())
    return adapters