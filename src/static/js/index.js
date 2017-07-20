const SERVER_URL = 'http://127.0.0.1:5000'

function getJourney(origin, destination) {
    var xhr = new XMLHttpRequest()
    xhr.onreadystatechange = () => {
        if (xhr.status === 200 && xhr.readyState === 4) {
            showJourney(JSON.parse(xhr.responseText))
        }
    }
    xhr.open('POST', SERVER_URL + "/getjourney", true)
    xhr.setRequestHeader('Content-Type', 'Application/json')
    xhr.send(JSON.stringify({
        origin: origin,
        destination: destination
    }))
}

function showJourney(journeys) {
    console.log(journeys)
}

initMap = () => {
    const CENTER = {
        lat: 53.346348,
        lng: -6.263098
    }

    var map = new google.maps.Map(
        document.getElementById('map'), {
            zoom: 12,
            center: CENTER
        });

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
        .addListener('dragend', event => {
            getJourney(destinationMarker.position)
        })
}