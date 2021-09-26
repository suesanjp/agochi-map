import { Marker, Popup } from "react-leaflet";
import mydata from "../mydata.json";

const MarkerPopup = () => {
  return (
    <>
      {mydata.map((item, index) => (
        <ul key={index}>
          <li>
            <Marker position={[item.longitude, item.latitude]}>
              <Popup>
                <h4>{item.name}</h4>
                <p>{item.genre}</p>
                <p>{item.address}</p>
                <p>電話番号: {item.tel}</p>
                <p>営業時間: {item.business_hours}</p>
                <p>定休日: {item.holiday}</p>
              </Popup>
            </Marker>
          </li>
        </ul>
      ))}
    </>
  );
};

export default MarkerPopup;
