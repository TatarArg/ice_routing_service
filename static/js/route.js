document.getElementById("pick-start-btn").addEventListener("click", () => {
    if (AppState.pickingMode === "start") {
        AppState.pickingMode = null;
        document.getElementById("pick-start-btn").classList.remove("selecting");
        document.getElementById("pick-start-btn").textContent = "Выбрать начало";
    } else {
        AppState.pickingMode = "start";
        document.getElementById("pick-start-btn").classList.add("selecting");
        document.getElementById("pick-start-btn").textContent = "Кликните на карте...";
        document.getElementById("pick-end-btn").classList.remove("selecting");
        document.getElementById("pick-end-btn").textContent = "Выбрать конец";
    }
});

document.getElementById("pick-end-btn").addEventListener("click", () => {
    if (AppState.pickingMode === "end") {
        AppState.pickingMode = null;
        document.getElementById("pick-end-btn").classList.remove("selecting");
        document.getElementById("pick-end-btn").textContent = "Выбрать конец";
    } else {
        AppState.pickingMode = "end";
        document.getElementById("pick-end-btn").classList.add("selecting");
        document.getElementById("pick-end-btn").textContent = "Кликните на карте...";
        document.getElementById("pick-start-btn").classList.remove("selecting");
        document.getElementById("pick-start-btn").textContent = "Выбрать начало";
    }
});

function checkRunBtn() {
    const areaId = document.getElementById("water-area-select").value;
    document.getElementById("run-btn").disabled = !(areaId && AppState.routeStart && AppState.routeEnd);
}

function setStatus(msg, pct) {
    const statusEl = document.getElementById("status");
    if (pct !== undefined) {
        statusEl.innerHTML = `
            <div>${msg}</div>
            <div style="margin-top:6px; background:#ddd; border-radius:4px; height:8px; width:100%;">
                <div style="background:#3388ff; height:8px; border-radius:4px; width:${pct}%; transition:width 0.3s;"></div>
            </div>
            <div style="font-size:11px; color:#888; margin-top:2px;">${pct}%</div>`;
    } else {
        statusEl.textContent = msg;
    }
}

document.getElementById("run-btn").addEventListener("click", () => {
    const areaId = document.getElementById("water-area-select").value;
    const iceClass = document.getElementById("ice-class-select").value;

    if (!areaId || !AppState.routeStart || !AppState.routeEnd) return;

    clearRoute();
    setStatus("Запуск...", 0);
    document.getElementById("run-btn").disabled = true;

    const { lat: sLat, lng: sLon } = AppState.routeStart;
    const { lat: eLat, lng: eLon } = AppState.routeEnd;

    const url = `/api/route-progress/?water_area=${areaId}&ice_class=${iceClass}&start_lat=${sLat}&start_lon=${sLon}&end_lat=${eLat}&end_lon=${eLon}`;
    const es = new EventSource(url);

    es.onmessage = (event) => {
        const data = JSON.parse(event.data);

        if (data.type === "progress") {
            setStatus(data.msg, data.pct);

        } else if (data.type === "done") {
            es.close();
            document.getElementById("run-btn").disabled = false;

            const route = data.route;
            if (!route || route.length === 0) {
                setStatus("Маршрут не найден");
                return;
            }

            const coords = route.map(p => [p.latitude, p.longitude]);
            AppState.trackLayer = L.polyline(coords, { color: "blue", weight: 3 }).addTo(map);

            if (AppState.startMarker) map.removeLayer(AppState.startMarker);
            if (AppState.endMarker) map.removeLayer(AppState.endMarker);

            AppState.startMarker = L.circleMarker(coords[0], {
                radius: 8, color: "green", fillColor: "green", fillOpacity: 1
            }).addTo(map).bindPopup("Начало маршрута");

            AppState.endMarker = L.circleMarker(coords[coords.length - 1], {
                radius: 8, color: "red", fillColor: "red", fillOpacity: 1
            }).addTo(map).bindPopup("Конец маршрута");

            map.fitBounds(AppState.trackLayer.getBounds());

            document.getElementById("cur-lat").textContent = sLat.toFixed(6);
            document.getElementById("cur-lon").textContent = sLon.toFixed(6);
            document.getElementById("cur-speed").textContent = "—";
            setStatus(`Маршрут построен (${route.length} точек)`);

        } else if (data.type === "error") {
            es.close();
            document.getElementById("run-btn").disabled = false;
            setStatus("Ошибка: " + data.msg);
        }
    };

    es.onerror = () => {
        es.close();
        document.getElementById("run-btn").disabled = false;
        setStatus("Ошибка соединения");
    };
});