# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict

from pydantic import BaseModel, Extra, Field


class TzbtcStorage(BaseModel):
    class Config:
        extra = Extra.forbid

    big_map: Dict[str, str]
    lambda_: str = Field(..., alias='lambda')
    nat: str
    bool: bool
