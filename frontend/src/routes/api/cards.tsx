import { Table, Panel, Col, Row, Input } from "rsuite"
import { useState } from 'react';
const { Column, HeaderCell, Cell } = Table;

// Route
// Example
// Return (table)
// Query Parameters
// Image display
// Carosel

const c = [{
  "id": "03290811090-541",
  "name": "The Fourth Doctor",
  "art": "https://cards.scryfall.io/png/front/c/8/c84ea0fd-efc7-4614-9f8f-41a3c71fceaa.png?1696636503",
  "rarity": "Mythic",
  "set_name": "Doctor Who"
}]

function Cards() {
    const [art, setArt] = useState("https://cards.scryfall.io/png/front/c/8/c84ea0fd-efc7-4614-9f8f-41a3c71fceaa.png?1696636503")
    const [text, setText] = useState("")
    

    return (
      <Panel header={<h2>Card Getter</h2>} bordered>
        <Row>
          <Col><img src={art} height="320px" width="240px"></img></Col>
          <Col>
            <CardView/>
          </Col>
          <Col>
            <Input type="text" placeholder="Enter Card Name" value={text} onChange={setText} style={{border: "2px black solid"}}/>
            <br></br>
            <Input type="button" value="Request" style={{border: "2px black solid"}}/>
          </Col>
        </Row>
        <br></br>
        <Row>
          <Row>
            <Col><b>Route: </b></Col>
            <Col>mtg-rest.web/api/v1/card</Col>
          </Row>
          <br></br>
          <h4>Query Parameters</h4>
          <br></br>
          <Row>
            <Col><b>name:</b></Col>
            <Col>The card name as a string in quotes</Col>
          </Row>
          <br></br>
          <h4>Example</h4>
          <br></br>
          <a href='https://mtg-rest.web.app/api/v1/card?name="Throes of Chaos"'>https://mtg-rest.web.app/api/v1/card?name="Throes of Chaos"</a>
          <br></br><br></br>
          <h4>Returns</h4>
          <br></br>
          An array of card objects with string keys: id, name, rarity, set_name, image
        </Row>
      </Panel>
    )
}




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

function CardView() {
  return (
    <Table bordered virtualized height={320} width={800} data={c}>
    <Column width={200}>
      <HeaderCell>ID</HeaderCell>
      <Cell dataKey="id"/>
    </Column>

    <Column width={200}>
      <HeaderCell>NAME</HeaderCell>
      <Cell dataKey="name"/>
    </Column>

    <Column width={200}>
      <HeaderCell>SET NAME</HeaderCell>
      <Cell dataKey="set_name"/>
    </Column>

    <Column width={200}>
      <HeaderCell>RARITY</HeaderCell>
      <Cell dataKey="rarity"/>
    </Column>

    </Table>
  );
}

export default Cards;
