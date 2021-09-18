import { Marker, Popup } from "react-leaflet";
import mydata from "../mydata.json";

let num = 1;
const name = mydata[num].name;
const area = mydata[num].area;
const genre = mydata[num].genre;
const address = mydata[num].address;
const tel = mydata[num].tel;
const businessHours = mydata[num].business_hours;
const holiday = mydata[num].holiday;
const longitude = mydata[num].longitude;
const latitude = mydata[num].latitude;

const MarkerPopup = () => {
  return (
    <Marker position={[longitude, latitude]}>
      <Popup>
        {name}
        <br />
        {area}
        <br />
        {genre}
        <br />
        {address}
        <br />
        {tel}
        <br />
        {businessHours}
        <br />
        {holiday}
        <br />
      </Popup>
    </Marker>
  );
};

export default MarkerPopup;
