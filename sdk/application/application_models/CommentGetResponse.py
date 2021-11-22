"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Comment import Comment

from .Page import Page


class CommentGetResponse(Schema):

    
    items = fields.List(fields.Nested(Comment, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

