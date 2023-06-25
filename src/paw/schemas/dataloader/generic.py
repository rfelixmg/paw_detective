import csv
import pydantic
from typing import Any
from pydantic import BaseModel


class GenericModel(BaseModel):
    def __getitem__(self: Any, item: int) -> Any:
        return self.__root__[item]

    def __iter__(self: Any) -> Any:
        for item in self.__root__:
            yield item

    def __len__(self: Any) -> int:
        return len(self.__root__)

    def size(self: Any) -> int:
        return self.__len__()

    @classmethod
    def from_csv(cls: Any, pathdir: str) -> Any:
        with open(pathdir, "r") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader, None)
            assert header is not None
            rows = []
            for row in csv_reader:
                rows.append({key: item for key, item in zip(header, row)})
        return pydantic.parse_obj_as(cls, rows)
