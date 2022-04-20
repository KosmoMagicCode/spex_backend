from flask_restx import fields, Model
from .responses import response

templates_model = Model('TemplateBase', {
    'pipeline_source': fields.String,
    'date': fields.DateTime(dt_format='rfc822'),

})

templates_get_model = templates_model.inherit('Templates get', {
    'id': fields.String(
        required=True,
        description='Hist id'
    ),
    'author': fields.Wildcard(fields.String)
})

templates_post_model = templates_model.inherit('Templates post')


list_templates_response = response.inherit('TemplatesListResponse', {
    'data': fields.List(fields.Nested(templates_get_model))
})

a_templates_response = response.inherit('TemplatesResponse', {
    'data': fields.List(fields.Nested(templates_get_model))
})
