from odoo import http
from operator import attrgetter
import json
import numpy
from pyproj import Proj, transform


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
        name = "test"
        lat = 45.587134
        lng = -73.733368
        enable = True
        size_width = 800
        size_height = 600
        # provider list comes from files leaflet-providers
        # lire le fichier javascript et extraire le json pour obtenir tous les provider
        #
        provider = "CartoDB"
        # Zoom maximal est dans l'information du provider. Permet range de 1 à max
        zoom = 13
        # provider = "OpenStreetMap"
        categories = {
            3: {
                "name": "ok3",
                "description": "une description 3"
            },
            2: {
                "name": "ok2",
                "description": "une description 2"
            },
            4: {
                "name": "ok4",
                "description": "une description 4"
            },
        }
        features = {
            "markers":
                [
                    {
                        "category_id": 3,
                        "coordinates": [
                            45.58945757862049,
                            -73.7531526184082
                        ],
                        "html_popup": "<b>Hello world!</b><br>I am a popup.",
                        "open_popup": True,
                    },
                    {
                        "category_id": 2,
                        "coordinates": [
                            45.58965957862049,
                            -73.7541526184082
                        ],
                        "html_popup": "<b>Hello people!</b><br>I am a nice popup.",
                        "open_popup": False,
                    },
                    {
                        "category_id": 2,
                        "coordinates": [
                            45.58065957862049,
                            -73.7591526184082
                        ],
                        "html_popup": """
                        <p>Hôpital au nom moyennement long</p><br/>
                        <div class="row">
                            <div class="col-md-4">
                                <div class="leaflet_card_container">
                                  <img src="/website_leaflet/static/src/images/img_avatar.png" alt="Avatar" class="leaflet_card_image" style="width:60px">
                                  <div class="leaflet_card_middle">
                                    <div class="leaflet_card_green_text">DISPO. 300</div>
                                  </div>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="leaflet_card_container">
                                  <img src="/website_leaflet/static/src/images/img_avatar.png" alt="Avatar" class="leaflet_card_image" style="width:60px">
                                  <div class="leaflet_card_middle">
                                    <div class="leaflet_card_yellow_text">Restant 123</div>
                                  </div>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="leaflet_card_container">
                                  <img src="/website_leaflet/static/src/images/img_avatar.png" alt="Avatar" class="leaflet_card_image" style="width:60px">
                                  <div class="leaflet_card_middle">
                                    <div class="leaflet_card_red_text">&amp; 36 Besoin 3023600</div>
                                  </div>
                                </div>
                            </div>
                        </div>
                        <br/>
                        <div class="row">
                            <div class="col-md-4">
                                <div class="leaflet_card_container">
                                  <img src="/website_leaflet/static/src/images/img_avatar.png" alt="Avatar" class="leaflet_card_image" style="width:60px">
                                  <div class="leaflet_card_middle">
                                    <div class="leaflet_card_green_text">DISPO. 12</div>
                                  </div>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="leaflet_card_container">
                                  <img src="/website_leaflet/static/src/images/img_avatar.png" alt="Avatar" class="leaflet_card_image" style="width:60px">
                                  <div class="leaflet_card_middle">
                                    <div class="leaflet_card_red_text">&lt; 6778 Besoin 40</div>
                                  </div>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="leaflet_card_container">
                                  <img src="/website_leaflet/static/src/images/img_avatar.png" alt="Avatar" class="leaflet_card_image" style="width:60px">
                                  <div class="leaflet_card_middle">
                                    <div class="leaflet_card_text">En attente</div>
                                  </div>
                                </div>
                            </div>
                        </div>
                        """,
                        "open_popup": False,
                    }
                ]
        }
        geojson = """
        {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "marker-color": "#FF0000",
                        "marker-size": "medium",
                        "marker-symbol": "circle",
                        "category_id": 4,
                        "popup": "<a href=\\\"https://www.glitter-graphics.com\\\" style=\\\"text-decoration: none\\\"><font color=#ff0000>T</font><font color=#f1280d>o</font><font color=#e44f1a>u</font><font color=#d67428>t</font><font color=#c99635>e</font><font color=#bbb543>s</font> <font color=#a1e35d>l</font><font color=#93f36b>e</font><font color=#86fc78>s</font> <font color=#6bfb93>c</font><font color=#5df1a1>o</font><font color=#50e1ae>u</font><font color=#43ccbb>l</font><font color=#35b2c9>e</font><font color=#2893d6>u</font><font color=#1a70e4>r</font><font color=#0d4bf1>s</font></a>"
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            -73.739119,
                            45.590738
                        ]
                    }
                },
                {
                    "type": "Feature",
                    "properties": {
                        "name": "Coors Field",
                        "amenity": "Baseball Stadium",
                        "popupContent": "This is where the Rockies play!"
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            -73.7537526184082,
                            45.57945957862049
                        ]
                    }
                },
                {
                    "type": "Feature",
                    "properties": {
                        "name": "Coors Field",
                        "amenity": "Baseball Stadium",
                        "popupContent": "This is where the Rockies play!"
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [-104.99404, 39.75621]
                    }
                },
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    -73.7702751159668,
                                    45.58220847715823
                                ],
                                [
                                    -73.76821517944336,
                                    45.574759101436825
                                ],
                                [
                                    -73.75276565551758,
                                    45.57367765830111
                                ],
                                [
                                    -73.74950408935545,
                                    45.57992570897905
                                ],
                                [
                                    -73.7563705444336,
                                    45.58485156646601
                                ],
                                [
                                    -73.7702751159668,
                                    45.58220847715823
                                ]
                            ]
                        ]
                    }
                },
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    -73.72821807861328,
                                    45.58845557862049
                                ],
                                [
                                    -73.71345520019531,
                                    45.58845557862049
                                ],
                                [
                                    -73.71345520019531,
                                    45.6095944559168
                                ],
                                [
                                    -73.72821807861328,
                                    45.6095944559168
                                ],
                                [
                                    -73.72821807861328,
                                    45.58845557862049
                                ]
                            ]
                        ]
                    }
                },
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [
                            [
                                -73.73233795166016,
                                45.58028615223038
                            ],
                            [
                                -73.7343978881836,
                                45.586173064456226
                            ],
                            [
                                -73.73079299926758,
                                45.587494531337384
                            ]
                        ]
                    }
                }
            ]
        }
        """
        return json.dumps({
            "name": name,
            "lat": lat,
            "lng": lng,
            "enable": enable,
            "size_width": size_width,
            "size_height": size_height,
            "zoom": zoom,
            "provider": provider,
            "features": features,
            "categories": categories,
            "geojson": geojson,
        })


    @http.route(['/map/detail/<model("website_leaflet.map"):obj>/'], type='http', auth="user", website=True,
                methods=['POST', 'GET'], csrf=False)
    def map_detail(self, obj=None):
        name = "test"
        lat = 45.587134
        lng = -73.733368
        enable = True
        size_width = 800
        size_height = 600
        provider = "CartoDB"
        zoom = 13
        categories = {}
        for i in http.request.env['website_leaflet.category'].search([["active", "=", True]]):
            categories[i.id] = {
                "name": i.name,
                "description": i.description,
            }
        features = {
            "markers": []
        }

        inProj = Proj('epsg:3857')
        outProj = Proj('epsg:4326')

        for feature in obj.features.search([["type", "=", "point"], ["active", "=", True]]):
            coord_UTM = numpy.column_stack(feature.geo_point.xy).tolist()[0]
            coord_lat_long = transform(inProj, outProj, *coord_UTM)
            features["markers"].append({
                "category_id": feature.category.id,
                "coordinates": coord_lat_long,
                "html_popup": feature.html_text,
                "open_popup": feature.open_popup,
            })
        return json.dumps({
            "name": name,
            "lat": lat,
            "lng": lng,
            "enable": enable,
            "size_width": size_width,
            "size_height": size_height,
            "zoom": zoom,
            "provider": provider,
            "features": features,
            "categories": categories,
        })
        
        # features = obj.features.search([])
        # to_output = []
        # coord_attr_map = {
        #     "point": "geo_point.xy",
        #     "line": "geo_line.xy",
        #     "area": "geo_area.exterior.coords.xy",
        # }
        # for feature in features:
        #     to_output.append({
        #         "type": feature.type,
        #         "coordinates": numpy.column_stack(
        #             attrgetter(coord_attr_map[feature.type])(feature)).tolist(),
        #     })
        # return http.Response(json.dumps(
        #     to_output),content_type='application/json;charset=utf-8',status=200)
