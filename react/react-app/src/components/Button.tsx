interface Props {
  children: string;
  onSelect: (children: string) => void;
  mode: string;
}

function Button({ children, onSelect, mode }: Props) {
  return (
    <button
      className={
        mode === children
          ? "btn btn-primary mb-3"
          : "btn btn-outline-primary mb-3"
      }
      id="mode"
      onClick={() => onSelect(children)}
    >
      {children}
    </button>
  );
}

export default Button;
