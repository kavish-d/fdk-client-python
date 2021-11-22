"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .ReviewMetric import ReviewMetric

from .Page import Page


class ReviewMetricGetResponse(Schema):

    
    items = fields.List(fields.Nested(ReviewMetric, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

