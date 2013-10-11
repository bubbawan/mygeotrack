var map = L.mapbox.map('map','mbantzt.map-pokecpco');

function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup(feature.properties.popupContent);
    }
}


var geojsonLayer;

console.log('hello');
setInterval(function(){updateData()},1000);
function updateData(){
httpinvoke('http://localhost:5000/geodata', 'GET', function(err, json) {
	if(geojsonLayer){
		geojsonLayer.clearLayers();
    }
    		
    if(err) {
        return console.log('Failure', err);
    }
    geojsonLayer = L.geoJson(JSON.parse(json), {
    	onEachFeature: onEachFeature
	}).addTo(map);
   
});}