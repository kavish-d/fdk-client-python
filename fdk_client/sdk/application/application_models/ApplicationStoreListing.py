"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .StoreDepartments import StoreDepartments

from .AppStore import AppStore

from .Page import Page


class ApplicationStoreListing(BaseSchema):

    
    filters = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    items = fields.List(fields.Nested(AppStore, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

