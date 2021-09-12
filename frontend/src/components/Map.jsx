import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import LocationMarker from "./Location";

const PopupItem = "つぼ八ツインハープ店";
/* <br />
〒078-8373旭川市旭神3条5丁目2‐9
<br />
0166-65-8995
<br />
月〜木・日曜日：17時00分〜23時00分
<br />
金・土曜日・祝日前：17時00分〜0時00分
<br />
年中無休" */

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
        <Popup>{PopupItem}</Popup>
      </Marker>
      <LocationMarker />
    </MapContainer>
  );
};

export default Map;
