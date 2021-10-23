function locationSuccess (pos){
  return pos.coords;
}
function locationError(geoLocationError) {
  return "37.875759, -122.258733";
}
function weather () {
  return;
}

if (navigator.geolocation) {
  document.write(navigator.geolocation.getCurrentPosition(locationSuccess, locationError));
} else {
  document.write("37.875759, -122.258733")
}
