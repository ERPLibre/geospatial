# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base_geoengine


class Category(models.Model):
    _name = 'website_leaflet.category'

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Name', required=True)
    company_id = fields.Many2one(
        'res.company',
        string="Company",
    )
    parent = fields.Many2One(comodel_name='website_leaflet.category', ondelete='restrict')


class MapFeature(models.Model):
    _name = 'website_leaflet.mapfeature'

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Name', required=True)
    geo_point = base_geoengine.fields.GeoPoint()
    geo_line = base_geoengine.fields.GeoLine()
    geo_area = base_geoengine.fields.GeoPolygon()
    category = fields.Many2One(comodel_name='website_leaflet.category', ondelete='restrict')
