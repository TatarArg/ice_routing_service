function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
    return "";
}

function computeOctagon(bounds, cutTL, cutTR, cutBL, cutBR) {
    const N = bounds.getNorth();
    const S = bounds.getSouth();
    const W = bounds.getWest();
    const E = bounds.getEast();
    const dLat = N - S;
    const dLon = E - W;

    const tl = cutTL / 100;
    const tr = cutTR / 100;
    const bl = cutBL / 100;
    const br = cutBR / 100;

    return [
        [N - dLat * tl, W],
        [N, W + dLon * tl],
        [N, E - dLon * tr],
        [N - dLat * tr, E],
        [S + dLat * br, E],
        [S, E - dLon * br],
        [S, W + dLon * bl],
        [S + dLat * bl, W],
    ];
}

function computeOctagonFromCenter(center, radiusKm, cutPercent) {
    const lat = center.lat;
    const lon = center.lng;

    const dLat = radiusKm / 111;
    const dLon = radiusKm / (111 * Math.cos(lat * Math.PI / 180));

    const N = lat + dLat;
    const S = lat - dLat;
    const W = lon - dLon;
    const E = lon + dLon;

    const fakeBounds = L.latLngBounds([[S, W], [N, E]]);
    return computeOctagon(fakeBounds, cutPercent, cutPercent, cutPercent, cutPercent);
}

function saveOctagonPoints(areaId, points) {
    const promises = points.map((pt, idx) =>
        fetch("/api/water-area-points/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({
                water_area: areaId,
                order: idx,
                latitude: pt[0].toFixed(6),
                longitude: pt[1].toFixed(6),
            }),
        })
    );
    return Promise.all(promises);
}