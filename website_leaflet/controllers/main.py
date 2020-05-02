from odoo import http

class MapFeatureController(http.Controller):

    @http.route('/mapfeatures/', auth='public')
    def list(self, **kw):
        return http.request.render('website_leaflet.listing', {
            'root': '/website_leaflet/website_leaflet',
            'objects': http.request.env['website_leaflet.mapfeature'].search([]),
        })

    @http.route('/mapfeatures/<model("website_leaflet.mapfeature"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('website_leaflet.object', {
            'object': obj
        })

    @http.route('/mapfeatures/test/', auth='public')
    def index(self, **kw):
        return "Hello, world"
