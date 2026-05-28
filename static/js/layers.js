const LayerState = {
    shipTrack: null,
    coursesLayer: null,
};

function updateLayerToggles(areaId) {
    document.getElementById("toggle-courses").disabled = !areaId;
    if (!areaId) {
        document.getElementById("toggle-courses").checked = false;
        if (LayerState.coursesLayer) { map.removeLayer(LayerState.coursesLayer); LayerState.coursesLayer = null; }
    }
}

function initCoursesLayer(points) {
    if (LayerState.coursesLayer) {
        map.removeLayer(LayerState.coursesLayer);
        LayerState.coursesLayer = null;
    }
    if (!points.length) return;

    const markers = points.map(p => {
        const icon = L.divIcon({
            className: "",
            html: `<div style="
                width:0; height:0;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-bottom: 10px solid rgba(30,100,200,0.7);
                transform: rotate(${p.course}deg);
                transform-origin: center bottom;
            "></div>`,
            iconSize: [8, 10],
            iconAnchor: [4, 5],
        });
        return L.marker([p.lat, p.lon], { icon });
    });

    LayerState.coursesLayer = L.layerGroup(markers).addTo(map);
}

document.getElementById("toggle-courses").addEventListener("change", function () {
    if (!this.checked) {
        if (LayerState.coursesLayer) {
            map.removeLayer(LayerState.coursesLayer);
            LayerState.coursesLayer = null;
        }
        return;
    }
    const areaId = document.getElementById("water-area-select").value;
    if (!areaId) return;

    document.getElementById("status").textContent = "Загружаем курсы судов...";
    fetch(`/api/courses/?water_area=${areaId}&limit=3000`)
        .then(res => res.json())
        .then(data => {
            initCoursesLayer(data);
            document.getElementById("status").textContent = `Курсы судов: ${data.length} точек`;
        });
});