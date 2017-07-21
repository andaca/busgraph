const SERVER_URL = 'http://127.0.0.1:5000'

function getStops(origin, destination) {
    var xhr = new XMLHttpRequest()
    xhr.onreadystatechange = () => {
        if (xhr.status === 200 && xhr.readyState === 4) {
            showJourneys(JSON.parse(xhr.responseText))
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

function showJourneys(journeys) {
    console.log(journeys)
    window.polylines = journeys.map(x => new google.maps.Polyline({
        path: [
            new google.maps.LatLng(x.board.coords[0],
                x.board.coords[1]),
            new google.maps.LatLng(x.deboard.coords[0],
                x.deboard.coords[1])
        ],
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 1,
        map: window.map
    }))

    /*
    var markers = []

    for (var i = 0; i < journeys.length; i++) {
        for (var j = 0; j < journeys[i].length; j++) {
            var section = journeys[i][j]
            markers.push(new google.maps.Marker({
                position: {
                    lat: section
                }
            }))
        }
    }
    var markers = journeys.map(journey => {

        new google.maps.Marker({
            position: {
                lat: x.coords[0],
                lng: x.coords[1]
            },
            label: x.id,
            map: window.map
        })
    })

    zoomToBounds(markers)*/
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

    window.map = new google.maps.Map(
        document.getElementById('map'), {
            zoom: 12,
            center: CENTER
        }
    )

    var originMarker = new google.maps.Marker({
        position: {
            lat: 53.346348,
            lng: -6.263098
        },
        map: map,
        label: "O",
        draggable: true
    })

    var destinationMarker = new google.maps.Marker({
        position: {
            lat: 53.344196,
            lng: -6.257776
        },
        map: map,
        label: "D",
        draggable: true
    })

    destinationMarker.addListener('dragend', event => {
        if (typeof window.polylines !== 'undefined') {
            for (var i = 0; i < window.polylines.length; i++) {
                window.polylines[i].setMap(null)
            }
            window.polylines = []
        }
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