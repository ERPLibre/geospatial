from odoo import http
from operator import attrgetter
import json
import numpy


class MapFeatureController(http.Controller):

    # @http.route('/mapfeatures/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('website_leaflet.listing', {
    #         'root': '/website_leaflet/website_leaflet',
    #         'objects': http.request.env['website_leaflet.mapfeature'].search([]),
    #     })

    # @http.route('/mapfeatures/<model("website_leaflet.mapfeature"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('website_leaflet.object', {
    #         'object': obj
    #     })

    @http.route('/mapfeatures/test/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route(['/map/config'], type='http', auth="public", website=True,
                methods=['POST', 'GET'], csrf=False)
    def map_config(self):
        # lat = http.request.env['ir.config_parameter'].sudo().get_param("website_leaflet_lat")
        # lng = http.request.env['ir.config_parameter'].sudo().get_param("website_leaflet_lng")
        # enable = http.request.env['ir.config_parameter'].sudo().get_param("website_leaflet_enable")
        # size = http.request.env['ir.config_parameter'].sudo().get_param("website_leaflet_size")
        lat = 45.587134
        lng = -73.733368
        enable = True
        size_width = 1000
        size_height = 800
        zoom = 13
        return json.dumps({
            "lat": lat,
            "lng": lng,
            "enable": enable,
            "size_width": size_width,
            "size_height": size_height,
            "zoom": zoom,
        })


    @http.route(['/map/config/<model("website_leaflet.map"):obj>/'], type='http', auth="user", website=True,
                methods=['POST', 'GET'], csrf=False)
    def map_config(self, obj=None):
        # lat = http.request.env['ir.config_parameter'].sudo().get_param("website_leaflet_lat")
        # lng = http.request.env['ir.config_parameter'].sudo().get_param("website_leaflet_lng")
        # enable = http.request.env['ir.config_parameter'].sudo().get_param("website_leaflet_enable")
        # size = http.request.env['ir.config_parameter'].sudo().get_param("website_leaflet_size")
        features = obj.features.search([])
        to_output = []
        coord_attr_map = {
            "point": "geo_point.xy",
            "line": "geo_line.xy",
            "area": "geo_area.exterior.coords.xy",
        }
        for feature in features:
            to_output.append({
                "type": feature.type,
                "coordinates": numpy.column_stack(
                    attrgetter(coord_attr_map[feature.type])(feature)).tolist(),
            })
        return http.Response(json.dumps(
            to_output),content_type='application/json;charset=utf-8',status=200)
