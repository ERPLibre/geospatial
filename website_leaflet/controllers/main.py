from odoo import http
import json


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
        lat = 55.505
        lng = 38.6611378
        enable = True
        size = 230
        return json.dumps({
            "lat": lat,
            "lng": lng,
            "enable": enable,
            "size": size,
        })
