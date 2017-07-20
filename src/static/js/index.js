const SERVER_URL = 'http://127.0.0.1:5000'

function getStops(origin, destination) {
    var xhr = new XMLHttpRequest()
    xhr.onreadystatechange = () => {
        if (xhr.status === 200 && xhr.readyState === 4) {
            showStops(JSON.parse(xhr.responseText))
        }
    }
    xhr.open('POST', SERVER_URL + "/getstops", true)
    xhr.setRequestHeader('Content-Type', 'Application/json')
    //xhr.send(JSON.stringify({origin: origin, destination: destination}))
    xhr.send(JSON.stringify({
        origin: origin,
        destination: destination
    }))
}

function showStops(stops) {
    stops = stops.origins.concat(stops.destinations)
    console.log(stops)
    const markers = stops.map(x => new google.maps.Marker({
        position: {
            lat: x.coords[0],
            lng: x.coords[1]
        },
        map: window.map
    }))
    zoomToBounds(markers)
}

function zoomToBounds(markers) {
    console.log(markers)
    var bounds = markers.reduce(
        (bounds, marker) => bounds.extend(marker.getPosition()),
        new google.maps.LatLngBounds())

    window.map.fitBounds(bounds)
}

initMap = () => {
    const CENTER = {
        lat: 53.346348,
        lng: -6.263098
    }

    window.map = new google
        .maps
        .Map(document.getElementById('map'), {
            zoom: 12,
            center: CENTER
        });

    var originMarker = new google
        .maps
        .Marker({
            position: {
                lat: 53.346348,
                lng: -6.263098
            },
            map: map,
            label: "O",
            draggable: true
        })

    var destinationMarker = new google
        .maps
        .Marker({
            position: {
                lat: 53.344196,
                lng: -6.257776
            },
            map: map,
            label: "D",
            draggable: true
        })

    destinationMarker.addListener('dragend', event => {
        var origin = {
            lat: originMarker
                .getPosition()
                .lat(),
            lng: originMarker
                .getPosition()
                .lng()
        }
        var destination = {
            lat: destinationMarker
                .getPosition()
                .lat(),
            lng: destinationMarker
                .getPosition()
                .lng()
        }
        getStops(origin, destination)
    })
}