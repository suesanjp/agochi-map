import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import LocationMarker from "./Location";
import mydata from "../mydata.json";

const num = 0;
const name = mydata[num].name;
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
      <Marker position={[43.7332904, 142.3887079]}>
        <Popup>{name}</Popup>
      </Marker>
      <LocationMarker />
    </MapContainer>
  );
};

export default Map;
