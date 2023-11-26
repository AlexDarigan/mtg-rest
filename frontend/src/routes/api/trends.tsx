import { Table, Panel, Col, Row, Input, Button } from "rsuite"
import { useState } from 'react';
import Plot from 'react-plotly.js';

function Trends() {
    const [text, setText] = useState("")
    const [start, setStart] = useState("")
    const [end, setEnd] = useState("")
    const [data, setData] = useState({"x": [], "y": []})

    async function getTrend() {
        var card_id = text
        var first = start
        var last = end
        if(first == "") { first = "20030101" }
        if(last == "") { last = new Date().toISOString().split("T")[0] }
        var response = await fetch(`https://mtg-rest.web.app/api/v1/price/trend?id="${card_id}"&start=${first}&end=${last}`)
        var data = await response.json()
        data.sort(function(a, b) {
          return Number(new Date(a.date)) - Number(new Date(b.date));
        });

        var x = data.map(obj => new Date(obj.date))
        var y = data.map(obj => obj.usd)
        setData({"x": x, "y": y})
    }

    return (
      <Panel header={<h2>Price Trends</h2>} bordered>
        <Row>
          {/* <Col><img src={art} height="320px" width="240px"></img></Col> */}
          <Row>
            <TrendChart data={data}/>
          </Row>
          <Row>
          <Col>
            <Col>
              <Input type="text" placeholder="Enter Card ID" value={text} onChange={setText} style={{border: "2px black solid"}}/>
            </Col>
            <Col>
              <Input type="text" placeholder="Enter Start Date (YYYYMMDD)" value={start} onChange={setStart} style={{border: "2px black solid"}}/>
            </Col>
            <Col>
              <Input type="text" placeholder="Enter End Date (YYYYMMDD)" value={end} onChange={setEnd} style={{border: "2px black solid"}}/>
            </Col>
            <Row>
              <br></br>
              <center><Button onClick={getTrend}>Request</Button></center>
            </Row>
          </Col>
          </Row>
        </Row>
        <br></br>
        <Row>
          <Row>
            <Col><b>Route: </b></Col>
            <Col>mtg-rest.web/api/v1/price/trend</Col>
          </Row>
          <br></br>
          <h4>Query Parameters</h4>
          <br></br>
          <Row>
            <Col><b>id</b></Col>
            <Col>The card id as a string in quotes</Col>
          </Row>
          <Row>
            <Col><b>start</b></Col>
            <Col>The starting date of the trend as YYYYMMDD</Col>
          </Row>
          <Row>
            <Col><b>id</b></Col>
            <Col>The ending date of the trend as YYYYMMDD</Col>
          </Row>
          <br></br>
          <h4>Example</h4>
          <br></br>
          <a href='https://mtg-rest.web.app/api/v1/price/trend?id="1024d5f1-69f4-4a09-ba83-6fcc249217fa"&start=20231101&end=20231125'>
            https://mtg-rest.web.app/api/v1/price/trend?id="1024d5f1-69f4-4a09-ba83-6fcc249217fa"&start=20231101&end=20231125
          </a>
          <br></br><br></br>
          <h4>Returns</h4>
          <br></br>
          A list of prices for the selected card by each day with keys date, eur and usd.
        </Row>
      </Panel>
    )
}

function TrendChart({data}) {
  return (
    <Plot
      data={[
        {
          x: data["x"],
          y: data["y"],
          type: 'scatter',
          mode: 'lines+markers',
          marker: {color: "red"},
        },
      ]}
      layout={{title: 'Trend Chart', xaxis: {"title": "Date", "type": "date"}, yaxis: {"title": "USD$"}, width: 1080, height: 800, } }
    />
  );
}
export default Trends;