# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteLeaflet(http.Controller):
#     @http.route('/website_leaflet/website_leaflet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_leaflet/website_leaflet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_leaflet.listing', {
#             'root': '/website_leaflet/website_leaflet',
#             'objects': http.request.env['website_leaflet.website_leaflet'].search([]),
#         })

#     @http.route('/website_leaflet/website_leaflet/objects/<model("website_leaflet.website_leaflet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_leaflet.object', {
#             'object': obj
#         })