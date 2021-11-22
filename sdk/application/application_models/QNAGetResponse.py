"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .QNA import QNA

from .Page import Page


class QNAGetResponse(Schema):

    
    items = fields.List(fields.Nested(QNA, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

