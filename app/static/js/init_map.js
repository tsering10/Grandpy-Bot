// GOOGLE MAPS SETUP: Javascript API //

// initialize google map objects
var map = {};
var marker = {};
var infowindow = {};

// Function called when page is loaded with initial coordinates
function initMap() {
    // initial coordinates displayed on the page
    coordinates = {lat: 48.856614, lng: 2.3522219}
    map = new google.maps.Map(document.getElementById('map'), {
        scaleControl: true,
        zoom: 10,
        center: coordinates,
        mapTypeId: google.maps.MapTypeId.ROADMAP


    });

    marker = new google.maps.Marker({
        position: coordinates,
        map: map
    });

   infowindow = new google.maps.InfoWindow();
}

// function called to actualise map with new coordinates
function updateMap(latitude, longitude, address) {
  infowindow.setContent(address);
  coordinates = {lat: latitude, lng: longitude};
  map.panTo(coordinates);
  marker.addListener('position_changed', function() {
    infowindow.close();
    infowindow.open(map, marker);
  })
  marker.setPosition(coordinates);
  marker.setAnimation(google.maps.Animation.BOUNCE);

  marker.addListener('click', function() {

          infowindow.open(map, marker);
        });

  map.setZoom(15)

}