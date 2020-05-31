function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    return
  }
}

var categoryItems = document.querySelectorAll("[data-loc]");
var categoryItemsArray = Array.from(categoryItems);

function sorter(a,b) {
  if(a.dataset.distance < b.dataset.distance) return -1;
  if(a.dataset.distance > b.dataset.distance) return 1;
  }


function haversineDistance(coords1, coords2) {
  function toRad(x) {
    return x * Math.PI / 180;
  }

  var lon1 = coords1[0];
  var lat1 = coords1[1];

  var lon2 = coords2[0];
  var lat2 = coords2[1];

  var R = 6371; // km

  var x1 = lat2 - lat1;
  var dLat = toRad(x1);
  var x2 = lon2 - lon1;
  var dLon = toRad(x2)
  var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  var d = R * c;


  return d;
}

function showPosition(position) {

currentLoc = [position.coords.latitude, position.coords.longitude]

for (let index = 0; index < jsonLoc.length; index++) {

    thisVerySpecificDiv = document.getElementById('loctarget' + jsonLoc[index].cabinet_id);
    distance = haversineDistance([jsonLoc[index].data.lat, jsonLoc[index].data.lng], currentLoc);
    thisVerySpecificDiv.dataset.distance = distance

    var sortedByLoc = categoryItemsArray.sort(sorter)
    console.log(sortedByLoc)
    sortedByLoc.forEach(e => document.querySelector("#big-container").appendChild(e));
    
    
}

locString = currentLoc[0] + ', ' +  currentLoc[1]
document.getElementById('locbyjs').innerHTML = locString
}

getLocation()


