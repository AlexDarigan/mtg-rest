import { useCallback, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Plot from 'react-plotly.js';
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [text, setText] = useState("")
  const [img, setImg] = useState("https://image.smythstoys.com/original/desktop/171511074_7.jpg")

  // Callback Reference
  const fetcher = useCallback(async () => {
    var response = await fetch("https://run.mocky.io/v3/bb21935b-b670-48f8-bf0f-a50d28328ba2")
    var data = await response.json()
    setText(JSON.stringify(data))
  }, [])

  // 
  const fetcher2 = useCallback(async () => {
    // Error was using no cors && also bad url (check for bad plurals, wrong-order)
    var response = await fetch("https://mtg-rest.web.app/api/v1/measure/cardtypes")
    console.log(response)
    var data = await response.json()
    console.log(data)
  }, [])

  const trends = useCallback(async () => {
    // Error was using no cors && also bad url (check for bad plurals, wrong-order)
    var response = await fetch("https://mtg-rest.web.app/api/v1/price/trends?name=Archivist")
    console.log(response)
    var data = await response.json()
    setImg(data[0]["img"])
    console.log(data)
  }, [])

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <img src="https://images.pexels.com/photos/20787/pexels-photo.jpg?auto=compress&cs=tinysrgb&h=350"/>
      <img src={img} style={{border: "2px black solid"}}/>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <button onClick={() => fetcher()}>Text is {text}</button>
        <button onClick={() => fetcher2()}>App {text}</button>
        <button onClick={() => trends()}>Get Trends</button>
        <Plot
        data={[
          {
            x: [1, 2, 3],
            y: [2, 6, 3],
            type: 'scatter',
            mode: 'lines+markers',
            marker: {color: 'red'},
          },
          {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
        ]}
        layout={ {width: 320, height: 240, title: 'A Fancy Plot'} }
      />
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
