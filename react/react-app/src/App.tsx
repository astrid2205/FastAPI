import { useState } from "react";
import Button from "./components/Button";
import Map from "./components/Map";
import RestaurantForm from "./components/RestaurantForm";
import PasswordForm from "./components/PasswordForm";
import "./App.css";

function App() {
  const [targetUrl, setTargetUrl] = useState("");
  const [mapVisibility, setMapVisibility] = useState(false);
  const [mode, setMode] = useState("Generate password");

  // Generate the url for the restaurant recommendation app to fetch data
  function handleSubmit(e: { preventDefault: () => void; target: any }) {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const url = new URLSearchParams(formData as any)
      .toString()
      .replaceAll("+", "%20");
    setTargetUrl(url);
  }

  return (
    <div>
      {/* Button to toggle between password and restaurant. */}
      <div className="mt-3">
        <Button onSelect={setMode} mode={mode}>
          Generate password
        </Button>
        <Button
          onSelect={(children) => {
            setMode(children);
            setMapVisibility(false);
          }}
          mode={mode}
        >
          Recommend restaurant
        </Button>
      </div>

      {/* Show form for password generation. */}
      {mode === "Generate password" && <PasswordForm />}

      {/* Show form for restaurant recommendation. */}
      {mode === "Recommend restaurant" && (
        <RestaurantForm
          onSubmit={(e: { preventDefault: () => void; target: any }) => {
            setMapVisibility(true);
            handleSubmit(e);
          }}
        />
      )}

      {/* Show the map. */}
      {mode === "Recommend restaurant" && mapVisibility && (
        <Map url={targetUrl} />
      )}
      {mode === "Recommend restaurant" && (
        <p id="map-message" className="mt-3"></p>
      )}
    </div>
  );
}

export default App;
