import ast
from typing import List, Any
from pydantic import BaseModel
from .generic import GenericModel


class AnnotationItem(BaseModel):
    Sample_ID: str
    Breed: str
    PET_ID: str

    @property
    def id(self: Any) -> str:
        return self.Sample_ID

    @property
    def breed(self: Any) -> List[str]:
        return ast.literal_eval(self.Breed)

    @property
    def pet_id(self: Any) -> List[int]:
        return ast.literal_eval(self.PET_ID)


class AnnotationItems(GenericModel):
    __root__: List[AnnotationItem]
