import { useState } from "react";
import Checkbox from "./Checkbox";

export default function PasswordForm() {
  const [password, setPassword] = useState("");
  const [error, setError] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  // Fetch random password from FastAPI
  function handleSubmit(e: { preventDefault: () => void; target: any }) {
    e.preventDefault();

    // Read the form data
    const form = e.target;
    const formData = new FormData(form);
    const jsonformData = JSON.stringify(Object.fromEntries(formData.entries()));

    // Fetch password from API
    const baseUrl = "https://fastapi-n8ag.onrender.com/generate-password";
    fetch(baseUrl, {
      method: form.method,
      headers: { "Content-Type": "application/json" },
      body: jsonformData,
    })
      .then((res) => {
        if (res.status !== 200) {
          setError(true);
        } else {
          setError(false);
        }
        return res.json();
      })
      .then((result) => {
        if ("password" in result) {
          setPassword(result["password"]);
        } else {
          setErrorMessage(result["detail"]);
        }
      }),
      (error: any) => console.log(error);
  }

  return (
    <>
      <p className="input-group mb-3">Generate a random password.</p>
      {error && <div className="input-group mb-3 error">{errorMessage}</div>}
      <div className="input-group mb-3">
        <span id="random-password" className="input-group-text">
          Random Password
        </span>
        <input
          id="random-password-value"
          className="form-control"
          aria-label="random-password "
          value={password}
          readOnly
        ></input>
      </div>
      <form method="post" onSubmit={handleSubmit}>
        <div className="input-group mb-1">
          <span className="input-group-text">Password length </span>
          <input
            type="number"
            name="length"
            className="form-control"
            required
            aria-label="length"
            defaultValue={12}
          ></input>
        </div>
        <Checkbox name="allow_upper" children="Uppercase" />
        <Checkbox name="allow_number" children="Numbers" />
        <Checkbox name="allow_special" children="Special Characters" />
        <button id="submitBtn" type="submit" className="btn btn-primary mb-3">
          Submit
        </button>
      </form>
    </>
  );
}
