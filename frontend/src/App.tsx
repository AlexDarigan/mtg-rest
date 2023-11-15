import { useCallback, useState } from 'react'
import { FaGithub, FaLinkedin, FaMailchimp} from 'react-icons/fa'
import { IconContext } from 'react-icons'

function NavBar() {
  return (
    <nav className='nav'>
      <a href="" className="site-title">Site Name</a>
      <ul>
        <li>
          <a href="Portfolio">About Me</a>
        </li>
        <li>
          <a href="Portfolio">M:TG Rest API</a>
        </li>
        <li>
          <a href="Portfolio">DSML</a>
        </li>
      </ul>
      <ul>
        <IconContext.Provider value={{ className: "shared-class", size: "42" }}>
        <li>
          <a href="https://www.github.com/AlexDarigan/mtg-rest"><FaGithub/></a>
        </li>
        <li>
          <a href="/linkedin"><FaLinkedin/></a>
        </li>
        <li>
          <a href="/email"><FaMailchimp/></a>
        </li>
        </IconContext.Provider>
      </ul>
    </nav>
  )
}

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
    // use path/?var=value for queries and not path?var=value
    var response = await fetch("/api/v1/price/trends?name=Archivist")
    console.log(response)
    var data = await response.json()
    setImg(data[0]["img"])
    console.log(data)
  }, [])

  return (
    <>
    <div>
      <NavBar></NavBar>
    </div>
    </>
  )
}

export default App


// <img src={img} style={{border: "2px black solid"}}/>
// <div className="card">
//   <button onClick={() => setCount((count) => count + 1)}>
//     count is {count}
//   </button>
//   <button onClick={() => fetcher()}>Text is {text}</button>
//   <button onClick={() => fetcher2()}>App {text}</button>
//   <button onClick={() => trends()}>Get Trends</button>
//   <Plot
//   data={[
//     {
//       x: [1, 2, 3],
//       y: [2, 6, 3],
//       type: 'scatter',
//       mode: 'lines+markers',
//       marker: {color: 'red'},
//     },
//     {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
//   ]}
//   layout={ {width: 320, height: 240, title: 'A Fancy Plot'} }
// />
//   <p>
//     Edit <code>src/App.tsx</code> and save to test HMR
//   </p>
// </div>
// <p className="read-the-docs">
//   Click on the Vite and React logos to learn more
// </p>