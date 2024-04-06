interface Props {
  items: string[][];
  name: string;
  label: string;
}

function SelectGroup({ items, label, name }: Props) {
  return (
    <div className="input-group mb-3">
      <span className="input-group-text">{label}</span>
      <select name={name} className="form-select">
        {items.map((item, index) => (
          <option key={index} value={item[1]}>
            {item[0]}
          </option>
        ))}
      </select>
    </div>
  );
}

export default SelectGroup;
