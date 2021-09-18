import { MapContainer, TileLayer } from "react-leaflet";
import MarkerPopup from "./MarkerPopup";
import LocationMarker from "./Location";

// TODO intで緯度、経度それぞれjsonに出力するように

const Map = () => {
  return (
    <MapContainer
      center={[43.774187, 142.363559]}
      zoom={11}
      scrollWheelZoom={false}
    >
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <MarkerPopup />
      <LocationMarker />
    </MapContainer>
  );
};

export default Map;
