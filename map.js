var map;
var directionsService;

$(document).ready(function()
{
});

/**
 * Init map
 */
function initMap()
{
  var coo = document.getElementById('coord');
  var gpx = document.getElementById('gpx');
  console.log(gpx);
  
  directionsService = new google.maps.DirectionsService();
  
  var stadshal = new google.maps.LatLng(51.0536865,3.7260684);  //51.0540764,3.7247118 stadshal
  var myOptions = {
    zoom: 14.25,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    //mapTypeId: google.maps.MapTypeId.SATELLITE,
    //mapTypeId: google.maps.MapTypeId.HYBRID,
    center: stadshal
  }
  map = new google.maps.Map(document.getElementById('map'), myOptions);
  
  google.maps.event.addListener(map, 'click', function(e) {
    var lat = e["latLng"].lat();
    var lng = e["latLng"].lng();
    console.log(lat + ", " + lng);
    var marker = new google.maps.Marker({
      position: e["latLng"]
    });       
    marker.setMap(map);
    coo.innerHTML += "<br>" + lat + ", " + lng;
    gpx.innerHTML += '<br>&lt;trkpt lat="'+lat+'" lon="'+lng +'"&gt;&lt;/trkpt&gt;';
  });
}

/**
 * Add marker
 */
function addMarker(myLatLng)
{
  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}

/**
 * Markers
 */
function setMarkers(path)
{
  var markerIcon = {
    scaledSize: new google.maps.Size(80, 80),
    origin: new google.maps.Point(0, 0),
    anchor: new google.maps.Point(32,65),
    labelOrigin:  new google.maps.Point(40,33),
  };
  var markers = [];
  for(var i=0; i<path.length-1; i++) {
    markers.push(
      new google.maps.Marker({
        position: new google.maps.LatLng(path[i].lat(), path[i].lng()),
        map: map,
        icon: markerIcon,
        label: {
          text: i.toString(),
          color: "#FFF",
          fontSize: "14px",
          fontWeight: "300"
        },
        visible: false
      })
    )
  }
  return markers;
}

function toggleMarker(marker)
{
  if(marker.getVisible())
    marker.setVisible(false);
  else
    marker.setVisible(true);
}