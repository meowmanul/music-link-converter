from pydantic import BaseModel, HttpUrl


class LinkRequest(BaseModel):
    
    url: HttpUrl