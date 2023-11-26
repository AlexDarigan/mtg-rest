//import { PanelGroup, Panel, Table } from "rsuite";
import { Table } from "rsuite";
const { Column, HeaderCell, Cell } = Table;

//const hostinfo = [{ "host": `mtg-rest.web.app`, "version": 1 }];
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

function Predictions() {
    return (<>
         <Table virtualized height={500} data={projinfo}>
          <Column width={200} align="left" fixed>
            <HeaderCell style={{fontSize: "1rem"}}>Title</HeaderCell>
            <Cell dataKey='title'/>
          </Column>

          <Column width={800}>
            <HeaderCell>Description</HeaderCell>
            <Cell dataKey='desc'/>
          </Column>
      </Table>
    </>)
}

export default Predictions;