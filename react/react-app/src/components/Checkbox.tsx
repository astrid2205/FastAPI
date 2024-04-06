import { useState } from "react";

interface Props {
  name: string;
  children: string;
}

function Checkbox({ name, children }: Props) {
  const [isChecked, setIsChecked] = useState(true);

  const checkHandler = () => {
    setIsChecked(!isChecked);
  };
  return (
    <div className="form-check mb-1">
      <input
        className="form-check-input"
        type="checkbox"
        id={name}
        name={name}
        checked={isChecked}
        onChange={checkHandler}
      ></input>
      {/* Send value false when the checkbox is not selected */}
      {!isChecked && <input type="hidden" name={name} value="false"></input>}
      {children}
    </div>
  );
}

export default Checkbox;
