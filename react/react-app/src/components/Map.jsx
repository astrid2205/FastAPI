import { MapContainer, TileLayer, useMap } from "react-leaflet";
import { useRef } from "react";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import icon from "leaflet/dist/images/marker-icon.png";
import iconShadow from "leaflet/dist/images/marker-shadow.png";

let DefaultIcon = L.icon({
  iconUrl: icon,
  shadowUrl: iconShadow,
});

L.Marker.prototype.options.icon = DefaultIcon;

// Get a restaurant recommendation and draw the route to the destination on the map.
function GetRestaurant({ url }) {
  document.getElementById("map-message").innerHTML = "";
  document.getElementById("loading").innerHTML = "Loading...";
  const map = useMap();
  const baseUrl = "https://fastapi-n8ag.onrender.com/recommend-restaurant?";
  fetch(baseUrl + url)
    .then((res) => res.json())
    .then(
      (result) => {
        // Successful result
        if ("features" in result) {
          // Set map center to the start location
          const feature = result["features"][0];
          const start = feature["start"];
          map.setView([start["lat"], start["lon"]], 14);

          // Other route information
          const destination = feature["destination"];
          const time = feature["properties"]["time"];
          const distance = feature["properties"]["distance"];
          const distance_units = feature["properties"]["distance_units"];

          // Add start marker to the map
          const startMarker = L.marker([start["lat"], start["lon"]])
            .addTo(map)
            .bindPopup(
              `<div><b>${start["name"]}</b></div><div>${start["address"]}</div>`
            );

          // Add destination marker to the map
          const destinationMarker = L.marker([
            destination["lat"],
            destination["lon"],
          ])
            .addTo(map)
            .bindPopup(
              `<div><b>${destination["name"]}</b></div><div>${destination["address"]}</div>`
            );

          // Note! GeoJSON uses [longitude, latutude] format for coordinates
          L.geoJSON(result, {
            style: (feature) => {
              return {
                color: "rgba(20, 137, 255, 0.7)",
                weight: 5,
              };
            },
          })
            .bindPopup((layer) => {
              return `${layer.feature.properties.distance.toFixed(0)} ${
                layer.feature.properties.distance_units
              }, ${(layer.feature.properties.time / 60).toFixed(2)} minutes`;
            })
            .addTo(map);

          // collect all transition positions
          const turnByTurns = [];
          result.features.forEach((feature) =>
            feature.properties.legs.forEach((leg, legIndex) =>
              leg.steps.forEach((step) => {
                const pointFeature = {
                  type: "Feature",
                  geometry: {
                    type: "Point",
                    coordinates:
                      feature.geometry.coordinates[legIndex][step.from_index],
                  },
                  properties: {
                    instruction: step.instruction.text,
                  },
                };
                turnByTurns.push(pointFeature);
              })
            )
          );
          const turnByTurnMarkerStyle = {
            radius: 5,
            fillColor: "#fff",
            color: "#555",
            weight: 1,
            opacity: 1,
            fillOpacity: 1,
          };

          L.geoJSON(
            {
              type: "FeatureCollection",
              features: turnByTurns,
            },
            {
              pointToLayer: function (feature, latlng) {
                return L.circleMarker(latlng, turnByTurnMarkerStyle);
              },
            }
          )
            .bindPopup((layer) => {
              return `${layer.feature.properties.instruction}`;
            })
            .addTo(map);

          // Display the route information
          document.getElementById("map-message").innerHTML = `<div>From <b>${
            start["name"]
          }</b></div>
          <div class="address mb-1">${start["address"]}</div>
          <div>To <b>${destination["name"]}</b></div>
          <div class="address mb-1">${destination["address"]}</div>
          <div class="mb-1">Distance: ${distance} ${distance_units}</div>
          <div>Time: ${(time / 60).toFixed(2)} min(s)</div>`;
        } else if ("start" in result) {
          // When no restaurant is found, only show the start point on the map
          const start = result["start"];
          map.setView([start["lat"], start["lon"]], 14);
          const startMarker = L.marker([start["lat"], start["lon"]])
            .addTo(map)
            .bindPopup(
              `<div><b>${start["name"]}</b></div><div>${start["address"]}</div>`
            );
          document.getElementById("map-message").innerHTML =
            "No restaurant is found in the area. <br>Modify your search criteria and try again.";
        } else if ("detail" in result) {
          // Show other error messages
          document.getElementById("map-message").innerHTML = result["detail"];
        }
        document.getElementById("loading").innerHTML = "";
      },
      (error) => console.log(error)
    );
}

function Map({ url }) {
  const mapRef = useRef(null);
  const latitude = 51.505;
  const longitude = -0.09;

  return (
    <>
      <div id="loading" className="mb-3"></div>
      <MapContainer
        id="map"
        center={[latitude, longitude]}
        zoom={13}
        ref={mapRef}
        key={url}
        style={{ height: "60vh", width: "calc(100vw-40px)" }}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <GetRestaurant url={url} />
      </MapContainer>
    </>
  );
}

export default Map;
