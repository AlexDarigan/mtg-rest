import { PanelGroup, Panel, Table } from "rsuite";
import ColorDistribution from "./api/color_distribution";
import Cards from "./api/cards";
import Trends from "./api/trends";
import Predictions from "./api/predictions";
const { Column, HeaderCell, Cell } = Table;

const REST: string = "https://en.wikipedia.org/wiki/REST";
const MTG_INFO: string = "https://www.mopop.org/resources/archive/landing-pages/science-fiction-and-fantasy-hall-of-fame/sffhof-members/magic-the-gathering/";
const MTG_FANDOM: string = "https://mtg.fandom.com/wiki/Magic:_The_Gathering";
const BLACK_LOTUS: string = "https://www.ign.com/articles/magic-the-gatherings-most-sought-after-card-sells-for-record-540000)";

const hostinfo = [{ "host": `mtg-rest.web.app`, "version": 1 }];
const projinfo = [
  {"title": "Title", "desc": "The project title"},
  {"title": "Description", "desc": "A brief description of the project"},
  {"title": "HTTP Route", "desc": "The HTTP Route of the project"},
  {"title": "Resources", "desc": "A tabled list of HTTP Resources"},
  {"title": "Query Parameters", "desc": "A optional tabled set of HTTP query parameters"},
  {"title": "Technologies", "desc": "The technologies used in the project (e.g python)"},
  {"title": "Libraries", "desc": "The libraries used in the project (e.g pandas)"},
  {"title": "Data Sources", "desc": "The data sources used for that project (e.g scryfall[4]"},
  {"title": "Data Storage", "desc": "How and where our transformed data is stored (e.g CSV, Cloud)"},
]

const response_example = JSON.stringify({
    "mode": "green",
    "median": "red",
    "mean": "blue"
});

function API() {
  return (
    <>
    <PanelGroup bordered style={{fontSize: "1rem"}}>
      <Panel bordered header={<h3>Introduction / Mission Statement</h3>}>
      A <a href={REST}>REST</a>ful API to serve Magic: The Gathering cards statistics. Magic: The Gathering (M:TG) is a trading card game created in 
      1993 by <a href={MTG_INFO}>Richard  Garfield</a> There are over <a href={MTG_FANDOM}>25,000 cards that exist for M:TG as of 2023</a>A number of 
      these cards are noteworthy for being exceptionally expensive, such as a copy of <a href={BLACK_LOTUS}>Black Lotus” selling for $540,000</a>
      While Black Lotus is an exceptional case, many M:TG cards fluctuate in price as the context of the game changes. This project is intended to 
      serve statistical data regarding M:TG card attributes and prices.
      </Panel>
      
      <Panel bordered header={<h3>Rest Project Design</h3>}>
        <i>You can find more detail on the REST API link in the main menu</i>
        <br></br><br></br>
        The primary navigation area of the project will be on the API Hostname as of the projects 
        version at that time.
        <br></br><br></br>

        <Table virtualized height={100} data={hostinfo}>
          <Column width={200} align="center" fixed>
            <HeaderCell>Host</HeaderCell>
            <Cell dataKey='host'/>
          </Column>

          <Column width={130}>
            <HeaderCell>Version</HeaderCell>
            <Cell dataKey='version'/>
          </Column>
      </Table>
      <br></br><br></br>
      This project will be a set of projects that exist as a single RESTful API. 
      <br></br><br></br>
      <strong>Click Panels Below To Expand / Collapse Details</strong>
      </Panel>
    </PanelGroup>

    <PanelGroup accordion bordered style={{fontSize: "1rem"}}>
        <Cards/>
        <ColorDistribution/>
        <Trends/>
        <Predictions/>
    </PanelGroup>
    </>
  );
}


// Color Distribution
// Price Trends
// Price Predictions

// Format

export default API;