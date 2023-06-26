from pydantic import BaseModel, Field


class InputItem(BaseModel):
    input_src: str = Field(default="./examples/example.jpg")
    output_src: str = Field(default="/output/")
