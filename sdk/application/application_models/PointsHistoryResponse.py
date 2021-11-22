"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .PointsHistory import PointsHistory

from .Page import Page


class PointsHistoryResponse(Schema):

    
    items = fields.List(fields.Nested(PointsHistory, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

