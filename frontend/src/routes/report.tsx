import { Panel } from "rsuite"
import { Link } from "react-router-dom";
import Card from "../assets/card.png"

const REST = "https://restfulapi.net/"
const MTG = "https://www.mopop.org/resources/archive/landing-pages/science-fiction-and-fantasy-hall-of-fame/sffhof-members/magic-the-gathering/"
const SCRYFALL = "https://scryfall.com/docs/api"
const BULKDATA = "https://scryfall.com/docs/api/bulk-data"
const TCGPlayer = "https://developer.tcgplayer.com/"
const CardMarket = "https://api.cardmarket.com/ws/documentation"
const Github = "https://github.com/AlexDarigan/mtg-rest"
const MTG_CARD = "https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/2/2c/Parts_of_a_Magic_card.jpg"

function Report() { 
  return (
    <>
    <Panel bordered header={<h1>Report</h1>} style={{marginLeft: "32px", marginTop: "32px", width: "1200px", fontSize: "1.5em"}}>
    <h2>Introduction</h2>
    <br></br>
    <p>
      This is a report on my experience in creating a Data Science Project primarily aimed at creating a <a href={REST}>REST</a> API 
      that allows users to query <a href={MTG}>Magic: The Gathering</a> card price trends. This report includes which data sources were 
      used, the experience of finding suitable data storage technologies that were suitable, the considerations of which data to remove 
      or not remove during data preprocessing and which technologies were used in order to do so. There are interactive data 
      visualization charts present on the <Link to="docs">M:TG API</Link> page demonstrating the API during the Web GUI.

      You can find the code for this project on the <a href={Github}>Github Repository</a>
    </p>
    <br></br>

    <h2>Data Sources</h2>
    <br></br>
    <p>
    The primary data for this project was taken from the <a href={SCRYFALL}>Scryfall API</a> using their daily updated  
    <a href={BULKDATA}> bulk data</a>, specifically using the "Default Cards" version in order to avoid immediate redundant cards. 
    The price data for Scryfall is taken from the <a href={CardMarket}>Card Market API</a> and <a href={TCGPlayer}>TCGPlayer API. </a> 
    I was not able to access those directly because they are locked down without a formal application, so this project exclusively pulls 
    from Scryfall.
    </p>
    <br></br>
    
    <h2>Anatomy of A Magic The Gathering Card</h2>
    <p>
      <img src={Card} width="1000px"></img>
      <br></br>
      <center><a href="https://mtg.fandom.com/wiki/Parts_of_a_card">Source</a></center>
    </p>
    <br></br>

    <h2>Data Preprocessing</h2>
    <br></br>
    <p>Content</p>
    <br></br>

    <h2>Exploratory Data / Data Visualizations</h2>
    <br></br>
    <p>
      On the <Link to="docs">MTG Rest API</Link> page, you will find three seperate projects that allow for data visualization, through
      a WEB GUI.
    </p>
    	<br></br>
      <ul>
        <li>
          <h4>Card Getter</h4>
          <br></br>
          <video src="https://drive.google.com/uc?id=19YfqXmKdMnk1VPTc4YcWz1Fd9daIBb0_" controls width="1000px"/>
          <br></br><br></br>
          <p>
            Card Getter takes the name of a card, and then returns all versions of that card with an id, image, name, rarity & 
            which set they were released in.
          </p>
          <br></br>
        </li>
        <li>
          <h4>Card Color Distribution</h4>
          <br></br>
          <video src="https://drive.google.com/uc?id=1NXGIh-Rk0ag582rkMDK0Amg5qbzn3jOM" controls width="1000px"/>
          <br></br><br></br>
          <p>
            Color Distribution will detail a pie chart of card color percentages in any given date range.
          </p>
          <br></br>
        </li>
        <li>
          <h4>Price Trend</h4>
          <br></br>
          <video src="https://drive.google.com/uc?id=1DwZVKvvsgmvfTnClIGW4q6tO2wTdjMw0" controls width="1000px"/>
          <br></br><br></br>
          <p>
            Price Trends will return a list of daily card prices of euro and us dollar prices when given a card id and a date range 
            for the trend in question. 
          </p>
        </li>
      </ul>
    {/* </p> */}
    <br></br>

    <h2>Data Storage</h2>
    <br></br>
    <p>Content</p>
    <br></br>

    <h2>Opportunities</h2>
    <br></br>
    <p>Content</p>
    <br></br>

    <h2>Challenges</h2>
    <br></br>
    <p>Content</p>
    </Panel>
    </>
  );
}

export default Report;

// TODO REPORT
// Iteration 2 -  
// Final portfolio  
// Data sources - use of appropriate data sources, data collection methods understanding/use, data provenance and quality 2 
// Data preprocessing - data cleaning and handling of missing values, feature engineering 4 
// Data visualisations - effective use of graphs, charts, and plots to aid/enhance understanding 4 
// Exploratory data analysis (EDA)- use of basic statistics, summarising main characteristics of the data used 4 
// Inclusion and utilisation of online sources/links/blogs/data sources etc 2 
// Quality – overall quality and potential impact of the portfolio, originality and innovation in creating the portfolio 2 
// Tool & techniques used 2 
// *clear evidence of improvement from iteration 1 is essential for iteration 2 ,20
//     