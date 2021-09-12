import "./App.css";
import Map from "./components/Map";

function App() {
  return (
    <div className="App">
      <header className="App-header"></header>

      {/* これがないと地図がばらばらになる*/}
      <link
        rel="stylesheet"
        href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
      />
      <Map />
    </div>
  );
}

export default App;
