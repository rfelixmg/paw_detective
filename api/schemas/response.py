from typing import List

from pydantic import BaseModel, Field


class ResponseItem(BaseModel):
    breed: str = Field(default="unknown")
    breed_id: int = Field(default=-1)
    confidence: float = Field(default=0)
    output_src: str


ResponseItems = List[ResponseItem]
