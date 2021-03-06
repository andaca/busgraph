const SERVER_URL = 'http://127.0.0.1:5000'


function initMap() {

    window.map = new google.maps.Map(
        document.getElementById('map'), {
            zoom: 12,
            center: {
                lat: 53.346348,
                lng: -6.263098
            }
        }
    )

    window.originMarker = new google.maps.Marker({
        position: {
            lat: 53.346348,
            lng: -6.263098
        },
        map: window.map,
        label: "O",
        draggable: true
    })

    window.destinationMarker = new google.maps.Marker({
        position: {
            lat: 53.344196,
            lng: -6.257776
        },
        map: window.map,
        label: "D",
        draggable: true
    })

    destinationMarker.addListener('dragend', handleDragEnd)
    originMarker.addListener('dragend', handleDragEnd)

    new google.maps.InfoWindow({
        content: "Drag to origin"
    }).open(map, originMarker)

    new google.maps.InfoWindow({
        content: "Drag to destination"
    }).open(map, destinationMarker)
}


function handleDragEnd(event) {
    if (typeof window.polylines !== 'undefined') {
        window.polylines.forEach(x => x.setMap(null))
        window.polylines = []
    }

    const origin = {
        lat: window.originMarker
            .getPosition()
            .lat(),
        lng: window.originMarker
            .getPosition()
            .lng()
    }

    const destination = {
        lat: window.destinationMarker
            .getPosition()
            .lat(),
        lng: window.destinationMarker
            .getPosition()
            .lng()
    }

    getStops(origin, destination)
}


function getStops(origin, destination) {

    var xhr = new XMLHttpRequest()
    xhr.onreadystatechange = () => {
        if (xhr.status === 200 && xhr.readyState === 4) {
            showJourneys(JSON.parse(xhr.responseText))
        }
    }

    xhr.open('POST', SERVER_URL + "/getstops", true)
    xhr.setRequestHeader('Content-Type', 'Application/json')

    xhr.send(JSON.stringify({
        origin: origin,
        destination: destination
    }))
}


function showJourneys(journeys) {
    console.log(journeys)

    window.polylines = journeys.map(x => new google.maps.Polyline({
        path: [
            new google.maps.LatLng(
                x.board.coords[0],
                x.board.coords[1]
            ),
            new google.maps.LatLng(
                x.deboard.coords[0],
                x.deboard.coords[1]
            )
        ],

        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 1,
        map: window.map
    }))
}

/*
function zoomToBounds(markers) {
    console.log(markers)
    var bounds = markers.reduce(
        (bounds, marker) => bounds.extend(marker.getPosition()),
        new google.maps.LatLngBounds())

    window.map.fitBounds(bounds)
}
*/