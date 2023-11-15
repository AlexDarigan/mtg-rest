import { Panel, Placeholder, PanelGroup, Row, Col } from 'rsuite';
import Me from "../assets/me.jpeg"


function Card(props: any) {
  return (
    <Panel {...props} bordered header="Card title">
      <Placeholder.Paragraph />
    </Panel>);
}


function Portfolio() {

  return (
    <>
    <PanelGroup bordered>
      <Panel header="About Me - David Darigan">
        <Row>
          <Col  xs={4}><img src={Me} height={200}></img></Col>
          <Col xs={12}>
          I started studying software independently in 2017 before enrolling in BSc (Honours) in Software Development at SETU Carlow in 2020.
          <br/><br/>
          I created WAT (Waiting and Testing). The penultimate most popular unit testing plugin for Godot, which is currently at 300+ stars on Github. 
          I wrote the initial iteration in GDScript with a further iteration adding C# interop. The C# version is currently referenced in the official 
          JetBrains Rider plugin for Godot. 
          <br/><br/>
          During my time in college I have learned and utilized Java, Java Swing, SQL, Javascript, PHP, HTML, CSS, 
          C/C++, Assembly 68000 (via Easy68k) and python. I'm also studying Kotlin, Gradle, Jetpack Compose & Firebase as part of my role as a 
          Google Developers Student Club Team Lead.
          </Col>
        </Row>
      </Panel>
      <Panel header="Experience">
        
      </Panel>
      <Panel header="Education">
        
      </Panel>
      <Panel header="Technologies">
        
      </Panel>
    </PanelGroup>
    </>
  );
}

export default Portfolio;