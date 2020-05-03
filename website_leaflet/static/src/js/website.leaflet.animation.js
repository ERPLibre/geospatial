odoo.define('website_leaflet.animation', function (require) {
    'use strict';

    require('web.dom_ready');
    var lat = 55.505,
        lng = 38.6611378,
        enable = false,
        size_width = 500,
        size_height = 300,
        zoom = 13,
        provider = 'OpenStreetMap',
        name = '',
        features = '',
        geojson = '';

    $.get("/map/config", function (data) {
        var data_json = JSON.parse(data);
        lat = data_json['lat'];
        lng = data_json['lng'];
        enable = data_json['enable'];
        size_width = data_json['size_width'];
        size_height = data_json['size_height'];
        zoom = data_json['zoom'];
        provider = data_json['provider'];
        name = data_json['name'];
        try {
            geojson = JSON.parse(data_json['geojson']);
        } catch (error) {
            console.error(error);
            console.debug(data_json['geojson']);
            geojson = ""
        }
        features = data_json['features'];

        if (enable && $('#mapid').length) {
            $('#mapid').width(size_width);
            // $('#mapid').css('width', size_width);
            $('#mapid').height(size_height);
            // $('#mapid').css('height', size_height)
            // hide google icon
            // $('.img-fluid').hide();
            var point = new L.LatLng(lat, lng);
            var map = L.map('mapid').setView(point, zoom);
            // var map = L.map('mapid_' + name).setView(point, zoom);
            L.tileLayer.provider(provider).addTo(map);
            if (geojson) {
                L.geoJSON(geojson, {
                    onEachFeature: function (feature, layer) {
                        if (feature.properties.popup) {
                            layer.bindPopup(feature.properties.popup);
                        }
                    }
                }).addTo(map);
            }
            if (features) {
                if (features.markers) {
                    let markers = features.markers;
                    for (let marker of markers) {
                        console.info(marker);
                        // Implement category
                        var obj = L.marker(marker.coordinates).addTo(map);
                        if (marker.html_popup) {
                            let obj_popup = obj.bindPopup(marker.html_popup);
                            if (marker.open_popup) {
                                obj_popup.openPopup();
                            }
                        }
                    }
                }
                if (features.lines) {
                    let lines = features.lines;
                    for (let line of lines) {
                        console.info(line);
                        var obj = L.polyline(line.coordinates).addTo(map);
                        if (line.html_popup) {
                            let obj_popup = obj.bindPopup(line.html_popup);
                            if (line.open_popup) {
                                obj_popup.openPopup();
                            }
                        }
                    }
                }
                if (features.areas) {
                    let areas = features.areas;
                    for (let area of areas) {
                        console.info(area);
                        var obj = L.polygon(area.coordinates).addTo(map);
                        if (area.html_popup) {
                            let obj_popup = obj.bindPopup(area.html_popup);
                            if (area.open_popup) {
                                obj_popup.openPopup();
                            }
                        }
                    }
                }
            }
            var popup = L.popup();

            function onMapClick(e) {
                popup
                    .setLatLng(e.latlng)
                    .setContent("You clicked the map at " + e.latlng.toString())
                    .openOn(map);
            }

            map.on('click', onMapClick);
        }
    });
});
