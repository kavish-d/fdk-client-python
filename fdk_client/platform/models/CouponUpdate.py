"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validation import Validation

from .Restrictions import Restrictions

from .CouponAction import CouponAction

from .Ownership import Ownership

from .Identifier import Identifier



from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .Rule import Rule

from .Validity import Validity

from .CouponSchedule import CouponSchedule

from .State import State

from .DisplayMeta import DisplayMeta



from .RuleDefinition import RuleDefinition




class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    state = fields.Nested(State, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

