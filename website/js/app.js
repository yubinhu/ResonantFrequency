function weather(latitude, longitude){
  var api_key = "173d82a42cf1523ad7e5376688d9921e";
  return "api.openweathermap.org/data/2.5/weather?lat="+latitude+"&lon="+longitude+"&appid=" + api_key;
}
function location() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          var latitude = position.coords.latitude;
          var longitude = position.coords.longitude;
          return latitude, longitude;
        });
    }
}
var latitude, longitude = location();
document.getElementById("result").innerHTML = weather(latitude, longitude);
