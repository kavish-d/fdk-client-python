"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .FeedbackMedia import FeedbackMedia

from .Page import Page


class MediaGetResponse(Schema):

    
    items = fields.List(fields.Nested(FeedbackMedia, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

