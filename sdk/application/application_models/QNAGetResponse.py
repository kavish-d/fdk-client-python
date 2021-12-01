"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .QNA import QNA

from .Page import Page


class QNAGetResponse(BaseSchema):

    
    items = fields.List(fields.Nested(QNA, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

