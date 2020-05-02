# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Category(models.Model):
    _name = 'website_leaflet.category'
    _description = 'Map Feature Category'

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Name', required=True)
    company_id = fields.Many2one(
        'res.company',
        string="Company",
    )
    parent = fields.Many2one(comodel_name='website_leaflet.category', ondelete='restrict')


class Map(models.Model):
    _name = 'website_leaflet.map'
    _description = 'Map'

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
    company_id = fields.Many2one(
        'res.company',
        string="Company",
    )
    category = fields.Many2one(
        comodel_name='website_leaflet.category', string="Company", ondelete='restrict')
    features = fields.Many2many(
        comodel_name='website_leaflet.mapfeature', string="Features")


class MapFeature(models.Model):
    _name = 'website_leaflet.mapfeature'
    _description = 'Map Feature'

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Name', required=True)
    type = fields.Selection(
        selection=[("point", _("Point")), ("line", _("Line")), ("poly", _("Polygon"))], required=True, default="point")
    geo_point = fields.GeoPoint()
    geo_line = fields.GeoLine()
    geo_area = fields.GeoPolygon()
    category = fields.Many2one(
        comodel_name='website_leaflet.category', string="Company", ondelete='restrict')
