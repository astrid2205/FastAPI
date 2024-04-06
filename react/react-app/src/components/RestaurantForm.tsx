import SelectGroup from "./SelectGroup";

const categories = [
  ["Restaurant", "catering.restaurant"],
  ["Fast food", "catering.fast_food"],
  ["Cafe", "catering.cafe"],
  ["Food court", "catering.food_court"],
  ["Bar", "catering.bar"],
  ["Pub", "catering.pub"],
  ["Ice cream", "catering.ice_cream"],
  ["Taproom", "catering.taproom"],
  ["Afghan", "catering.restaurant.afghan"],
  ["African", "catering.restaurant.african"],
  ["American", "catering.restaurant.american"],
  ["Arab", "catering.restaurant.arab"],
  ["Argentinian", "catering.restaurant.argentinian"],
  ["Asian", "catering.restaurant.asian"],
  ["Austrian", "catering.restaurant.austrian"],
  ["Balkan", "catering.restaurant.balkan"],
  ["Barbecue", "catering.restaurant.barbecue"],
  ["Bavarian", "catering.restaurant.bavarian"],
  ["Beef bowl", "catering.restaurant.beef_bowl"],
  ["Belgian", "catering.restaurant.belgian"],
  ["Bolivian", "catering.restaurant.bolivian"],
  ["Brazilian", "catering.restaurant.brazilian"],
  ["Bubble tea", "catering.cafe.bubble_tea"],
  ["Burger", "catering.restaurant.burger"],
  ["Cake", "catering.cafe.cake"],
  ["Caribbean", "catering.restaurant.caribbean"],
  ["Chicken", "catering.restaurant.chicken"],
  ["Chili", "catering.restaurant.chili"],
  ["Chinese", "catering.restaurant.chinese"],
  ["Coffee", "catering.cafe.coffee"],
  ["Coffee shop", "catering.cafe.coffee_shop"],
  ["Crepe", "catering.cafe.crepe"],
  ["Croatian", "catering.restaurant.croatian"],
  ["Cuban", "catering.restaurant.cuban"],
  ["Curry", "catering.restaurant.curry"],
  ["Czech", "catering.restaurant.czech"],
  ["Danish", "catering.restaurant.danish"],
  ["Dessert", "catering.cafe.dessert"],
  ["Donut", "catering.cafe.donut"],
  ["Dumpling", "catering.restaurant.dumpling"],
  ["Ethiopian", "catering.restaurant.ethiopian"],
  ["European", "catering.restaurant.european"],
  ["Filipino", "catering.restaurant.filipino"],
  ["Fish", "catering.restaurant.fish"],
  ["Fish and chips", "catering.restaurant.fish_and_chips"],
  ["French", "catering.restaurant.french"],
  ["Friture", "catering.restaurant.friture"],
  ["Frozen yogurt", "catering.cafe.frozen_yogurt"],
  ["Georgian", "catering.restaurant.georgian"],
  ["German", "catering.restaurant.german"],
  ["Greek", "catering.restaurant.greek"],
  ["Hawaiian", "catering.restaurant.hawaiian"],
  ["Hot dog", "catering.fast_food.hot_dog"],
  ["Hungarian", "catering.restaurant.hungarian"],
  ["Indian", "catering.restaurant.indian"],
  ["Indonesian", "catering.restaurant.indonesian"],
  ["International", "catering.restaurant.international"],
  ["Irish", "catering.restaurant.irish"],
  ["Italian", "catering.restaurant.italian"],
  ["Jamaican", "catering.restaurant.jamaican"],
  ["Japanese", "catering.restaurant.japanese"],
  ["Kebab", "catering.restaurant.kebab"],
  ["Korean", "catering.restaurant.korean"],
  ["Latin american", "catering.restaurant.latin_american"],
  ["Lebanese", "catering.restaurant.lebanese"],
  ["Malay", "catering.restaurant.malay"],
  ["Malaysian", "catering.restaurant.malaysian"],
  ["Mediterranean", "catering.restaurant.mediterranean"],
  ["Mexican", "catering.restaurant.mexican"],
  ["Moroccan", "catering.restaurant.moroccan"],
  ["Nepalese", "catering.restaurant.nepalese"],
  ["Noodle", "catering.restaurant.noodle"],
  ["Oriental", "catering.restaurant.oriental"],
  ["Pakistani", "catering.restaurant.pakistani"],
  ["Persian", "catering.restaurant.persian"],
  ["Peruvian", "catering.restaurant.peruvian"],
  ["Pita", "catering.restaurant.pita"],
  ["Pizza", "catering.restaurant.pizza"],
  ["Portuguese", "catering.restaurant.portuguese"],
  ["Ramen", "catering.restaurant.ramen"],
  ["Regional", "catering.restaurant.regional"],
  ["Russian", "catering.restaurant.russian"],
  ["Salad", "catering.fast_food.salad"],
  ["Sandwich", "catering.restaurant.sandwich"],
  ["Seafood", "catering.restaurant.seafood"],
  ["Soup", "catering.restaurant.soup"],
  ["Spanish", "catering.restaurant.spanish"],
  ["Steak house", "catering.restaurant.steak_house"],
  ["Sushi", "catering.restaurant.sushi"],
  ["Swedish", "catering.restaurant.swedish"],
  ["Syrian", "catering.restaurant.syrian"],
  ["Tacos", "catering.restaurant.tacos"],
  ["Taiwanese", "catering.restaurant.taiwanese"],
  ["Tapas", "catering.restaurant.tapas"],
  ["Tea", "catering.cafe.tea"],
  ["Tex", "catering.restaurant.tex-mex"],
  ["Thai", "catering.restaurant.thai"],
  ["Turkish", "catering.restaurant.turkish"],
  ["Ukrainian", "catering.restaurant.ukrainian"],
  ["Uzbek", "catering.restaurant.uzbek"],
  ["Vietnamese", "catering.restaurant.vietnamese"],
  ["Waffle", "catering.cafe.waffle"],
  ["Western", "catering.restaurant.western"],
  ["Wings", "catering.restaurant.wings"],
];

interface Props {
  onSubmit: (e: { preventDefault: () => void; target: any }) => void;
}

export default function RestaurantForm({ onSubmit }: Props) {
  return (
    <>
      <p className="input-group mb-3">Recommend a restaurant for you!</p>
      <form onSubmit={onSubmit}>
        <div className="input-group mb-3">
          <span className="input-group-text" id="basic-addon1">
            Location
          </span>
          <input
            type="text"
            name="location"
            className="form-control"
            required
            aria-label="location"
          ></input>
        </div>

        <div className="input-group mb-3">
          <span className="input-group-text">Travel Mode </span>
          <select name="mode" className="form-select">
            <option value="walk">Walk</option>
            <option value="bicycle">Bicycle</option>
            <option value="bus">Bus</option>
          </select>
        </div>

        <div className="input-group mb-3">
          <span className="input-group-text">Time Range (in minutes) </span>
          <input
            type="number"
            name="time_range"
            className="form-control"
            required
            aria-label="time_range"
          ></input>
        </div>

        {/* Show the selection label for restaurant categories */}
        <SelectGroup items={categories} label="Categories" name="categories" />

        <button id="submitBtn" type="submit" className="btn btn-primary mb-3">
          Submit
        </button>
      </form>
    </>
  );
}
