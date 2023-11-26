import { Panel, Row, Col, Input, Button } from "rsuite";
import { useState, useEffect } from "react"
import Plot from 'react-plotly.js';

function ColorDistribution() {
    const [start, setStart] = useState("")
    const [end, setEnd] = useState("")
    const [data, setData] = useState([0, 0, 0, 0, 0, 0])

    async function getDistribution() {
        var first = start
        var last = end
        if(first == "") { first = "20030101" }
        if(last == "") { last = new Date().toISOString().split("T")[0] }
        var response = await fetch(`https://mtg-rest.web.app/api/v1/color/distribution?start=${first}&end=${last}`)
        var data = await response.json()
        var values = [data["R"], data["G"], data["U"], data["W"], data["B"], data["N"]]
        setData(values)
    }

    useEffect(() => { getDistribution() }, [])

    return (
      <Panel header={<h2>Color Distribution</h2>} bordered>
        <Row>
            <Col>
            <PieChart data={data}></PieChart>
            </Col>
            <Col>
            <Row>
              <Input type="text" placeholder="Enter Start Date (YYYYMMDD)" value={start} onChange={setStart} style={{border: "2px black solid"}}/>
            </Row>
            <Row>
            <Input type="text" placeholder="Enter End Date (YYYYMMDD)" value={end} onChange={setEnd} style={{border: "2px black solid"}}/>
            </Row>
            <br></br>
              <Button onClick={getDistribution}>Request</Button>
            </Col>
        </Row>
        <br></br>
        <Row>
          <Row>
            <Col><b>Route: </b></Col>
            <Col>mtg-rest.web/api/v1/color/distribution</Col>
          </Row>
          <br></br>
          <h4>Query Parameters</h4>
          <br></br>
          <Row>
              <b>start:</b>
              The earliest date that cards may have been released (earliest is Jan 1st 2003)
          </Row>
          <Row>
              <b>end:</b>
              The most recent date that cards may have been released (most recent is today after 3 UTC)
          </Row>
          <br></br>
          <h4>Example</h4>
          <br></br>
          <a href='https://mtg-rest.web.app/api/v1/color/distribution?start=20220101&end=20221231'>https://mtg-rest.web.app/api/v1/color/distribution?start=20220101&end=20221231</a>
          <br></br><br></br>
          <h4>Returns</h4>
          <br></br>
          A key-value pair representing each color and their total count for the specified date range (Red (R), Green (G), Blue (U), Black (B), White (W) & Colorness (N))
        </Row>      
      </Panel>
    );
}

function PieChart({data}) {
    return (
      <Plot
        data={[
          {
            values: data,
            labels: ["R", "G", "U", "W", "B", "N"],
            type: 'pie',
          },
        ]}
        layout={ {width: 640, height: 640, title: 'Color Distribution'} }
      />
    );
}

export default ColorDistribution;