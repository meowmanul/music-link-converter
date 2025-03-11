## Особенности
- **Унифицированный формат данных:** Все ссылки агрегируются в единый словарь, что упрощает дальнейшую интеграцию и использование.
- **Асинхронная обработка:** Использование FastAPI и httpx позволяет параллельно отправлять запросы к API внешних сервисов, сокращая время отклика.
- **Расширяемость:** Проект спроектирован с учётом принципов SOLID, что облегчает добавление поддержки новых сервисов без изменения базовой архитектуры.


## Установка и запуск

### Локальный запуск

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/yourusername/music-link-converter.git
```
```bash
cd music-link-converter
```

2. **Создайте и активируйте виртуальное окружение:**
```bash
python -m venv .venv
```
Windows: 
```bash
.venv\Scripts\activate
```
Linux/macOS: source
```bash
.venv/bin/activate
```

3. **Установите зависимости:**
```bash
pip install --upgrade pip pip install -r requirements.txt
```

4. **Запустите приложение:**
```bash
uvicorn app.main:app --reload
```

Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000).

---
### Запуск с Docker

1. **Соберите образ:**
```bash
docker build -t music-link-converter .
```

2. **Запустите контейнер:**
```bash
docker run -d -p 8000:8000 music-link-converter
```

Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000).

---
## API

### Конвертация ссылки

- **Endpoint:** `POST /convert`
- **Описание:** Принимает JSON с исходной ссылкой и возвращает объект с исходной ссылкой и набором ссылок на разные платформы.

#### Пример запроса:

```json
{   
"url": "https://music.yandex.ru/album/12843644/track/73781461?utm_source=desktop&utm_medium=copy_link" 
}
```
#### Пример ответа:

```json
{   
"source": "https://music.yandex.ru/album/12843644/track/73781461?utm_source=desktop&utm_medium=copy_link",
"links": {
	"spotify": "https://open.spotify.com/track/...",
	"youtube": "https://www.youtube.com/watch?v=...",
	"deezer": "https://www.deezer.com/track/...",
	"tidal": "https://listen.tidal.com/track/...",
	"pandora": "https://www.pandora.com/..."   
 } 
}
```
