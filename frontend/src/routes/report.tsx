import { Panel } from "rsuite"
import { Link } from "react-router-dom";
import Card from "../assets/card.png"
import MergeCode from "../assets/merge.png"

const REST = "https://restfulapi.net/"
const MTG = "https://www.mopop.org/resources/archive/landing-pages/science-fiction-and-fantasy-hall-of-fame/sffhof-members/magic-the-gathering/"
const SCRYFALL = "https://scryfall.com/docs/api"
const BULKDATA = "https://scryfall.com/docs/api/bulk-data"
const TCGPlayer = "https://developer.tcgplayer.com/"
const CardMarket = "https://api.cardmarket.com/ws/documentation"
const Github = "https://github.com/AlexDarigan/mtg-rest"
const anvil_tables = "https://anvil.works/docs/data-tables"
const firestore = "https://firebase.google.com/docs/firestore"
const background_tasks = "https://anvil.works/docs/background-tasks"
const batch_writes =  "https://firebase.google.com/docs/firestore/manage-data/transactions"
const topics = "https://cloud.google.com/pubsub/docs/create-topic"
const hosting = "https://firebase.google.com/docs/hosting"
const functions = "https://firebase.google.com/docs/functions"
const schedule = "https://firebase.google.com/docs/functions/schedule-functions?gen=2nd"
const BigQuery = "https://cloud.google.com/bigquery?hl=en"


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
    
    <h2 id="anatomy">Anatomy of A Magic The Gathering Card</h2>
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
    <br></br>

    <h2>Data Storage</h2>
    <br></br>
    <p>
      This project has gone through several different iterations of data storage. 
    </p>
    <br></br>
    <h3>Anvil</h3>
    <p>
      The earliest iteration used <a href={anvil_tables}>Anvil Tables</a> which presented two problems. The first is that Anvil Tables 
      can only store about 150,000 rows, while the total count of cards processed was filtered from 80,000~ to 20,000~, this still 
      presented a problem when storing 20,000 rows of card prices per days. The second problem was that, even with 
      <a href={background_tasks}> Background Tasks </a> actually processing the data took a number of hours, usually failing near 
      the end. Anvil proved unsuitable.
    </p>
    <br></br>
    <h3>Firebase Firestore</h3>
    <p>
      The second iteration of this project used <a href={firestore}>Firebase Firestore </a> in order to store data. Firestore was very flexible
      for the literal act of storing data. An early issue with Firestore was the gathering of the data taking about two hours to be stored per 
      daily update. This was easily solved using <a href={batch_writes}></a> and the Publisher Subscriber model using 
      <a href={topics}> Topics</a> which reduced the two hour update to a few minutes by writing batches of 500 records in parallel. 

      The problem with firebase came to when I was reading the documents, query filters work quite fast on the server-side of Firebase but I
      would run into limitations, such as only being able to query against one field for ranges (i.e I couldn't query a price range within a
      date range, only the price range OR the date range, not both). This meant that I would have to filter client-side, however due to the 
      limited server-side filters, I would be reading a significant amount of documents that would take unreasonably long to reach the client.

      <a href={hosting}>Firebase hosting</a> and <a href={functions}>Firebase functions</a> were introduced into the project during this 
      iteration and have stayed. Firebase Functions allow me to run http functions as cloud "serverless" functions, so I am only paying for 
      what is used rather than a flat rate. Functions also allow for <a href={schedule}>scheduled functions</a>, which is how I manage to 
      run daily updates.
    </p>
    <br></br>
    <h3>Big Query</h3>
    <p>
      <a href={BigQuery}>Big Query</a> was used for the third and final iteration (as of writing) for this project. The data I'm storing 
      in Big Query is miniscule compared to the scale it can be used for, but it was too big for anything else. There are three tables in
      my Big Query dataset, the first table (<b>cards</b>), is for the basic card information, as shown by 
      <a href="#anatomy">Anatomy of a MTG Card</a>, the second table (<b>prices</b>), is a list of prices for each card per day, 
      and the final table (<b>daily_prices</b>), is a staging table for new prices.

      Big Query, due to its use for data science, does not enforce uniqueness constraints. If I were to batch insert the bulk data from 
      Scryfall every day directly into the cards table, it would append all of those as new records despite identical records existing. 
      I've since learned, that the recommended thing to do is to delete the old table, and add the new table.

      The problem with this approach shows its head when storing the prices. I cannot delete the old data because it is <i>historical</i> 
      but it is difficult to append data for new cards without also reappending data that already exists. To solve this, I've introduced an
      intermediate staging table "daily_prices" which takes all of the new data for the day, and then performs a merge into the daily_prices 
      when the card_id and the price date id doesn't match between the tables. That is for any price in daily_prices, if a record with the same
      id and date don't exist, insert that row into prices. If no id matches, then it is a new card, if no date matches, then it is a new price
      record.
      <Panel bordered header={<h5>Merge Code</h5>}>
      <img src={MergeCode} height="160px"></img>
      </Panel>
      <br></br>
      <span>Overall Big Query has proven to be the most suitable Data Storage technology for this project</span>
    </p>
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