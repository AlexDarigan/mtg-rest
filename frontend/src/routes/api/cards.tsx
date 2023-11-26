import { Table, Panel, Col, Row, Input, Button } from "rsuite"
import { useState } from 'react';
import { RowDataType } from "rsuite/esm/Table";
const { Column, HeaderCell, Cell } = Table;

function Cards() {
    const [art, setArt] = useState("https://i.imgur.com/LdOBU1I.jpeg")
    const [text, setText] = useState("")
    const [cards, setCards] = useState([])
    
    async function getCard() {
      var card_name = text
      setText("")
      var response = await fetch(`https://mtg-rest.web.app/api/v1/card?name="${card_name}"`)
      var data = await response.json()
      setCards(data)
    }

    function changeCell(rowData: RowDataType) {
      var card = cards.find((card) => card["id"] == rowData.id)
      if(card) {
        setArt(card["image"]);
      }
    }

    return (
      <Panel header={<h2>Card Getter</h2>} bordered>
        <Row>
          <Col><img src={art} height="320px" width="240px"></img></Col>
          <Col>
            <CardView cards={cards} changeCell={changeCell}/>
          </Col>
          <Col>
            <Input type="text" placeholder="Enter Card Name" value={text} onChange={setText} style={{border: "2px black solid"}}/>
            <br></br>
            <center><Button onClick={getCard}>Request</Button></center>
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
          An array of card objects with string keys: id, name, rarity, set, image
        </Row>
      </Panel>
    )
}

function CardView({cards, changeCell}) {
  return (
    <Table bordered virtualized height={320} width={800} data={cards} onRowClick={changeCell}>
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
      <Cell dataKey="set"/>
    </Column>

    <Column width={200}>
      <HeaderCell>RARITY</HeaderCell>
      <Cell dataKey="rarity"/>
    </Column>

    </Table>
  );
}

export default Cards;
