import { Panel, PanelGroup, Row, Col } from 'rsuite';
import Me from "../assets/me.jpeg"

function Profile() {

  return (
    <>
    <PanelGroup bordered style={{fontSize: "1rem"}}>
      <Panel bordered header={<h3>About Me - David Darigan</h3>}>
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
      
      <Panel bordered header={<h3>Experience</h3>}>
        <Panel header={<h5>DELL Technologies Undergraduate Internship March 2023 - August 2023</h5>}>
          <ul>
          <li>Contributed to the efforts of the Finance Integration Services Team to support over 150 class 1 financial microservices.</li>
          <li>Used PowerShell to reduce 2 days of work a year to 30 minutes by automating the task of restaging all applications in each non-production environment.</li>
          <li>Raised CI / CD Maturity KPI by 12% to reach a total of 76.8% in May from 64.8% in April by applying a number of adjustments to several applications to make them compliant with CI / CD metrics of success. 87.8% was the final score reached as of the end of my internship.</li>
          <li>Reduced over several thousand application vulnerabilities through proper dependency management of each application.</li>
          <li>Applied abstraction enhancements to several applications in order to reduce duplicated code and global variables.</li>
          <li>Utilized GitLab & Spring Configuration Server REST APIs in order to write a feature in Bash to set metadata on applications during the deploy task of the deployment pipeline.</li>
          </ul>
        </Panel>
        <Panel header={<h5>Google Developers Student Club Team Lead 2022 - Present</h5>}>
          <ul>
            <li>Co-ordinate weekly events</li>
            <li>Communicate fundamental technological ideas to members through presentations</li>
            <li>Manage budgeting with the aid of Google Developer Student Club co-ordinators</li>
          </ul>
      </Panel>
      <Panel header={<h5>Google Developers Student Club Core Team Member 2021 - 2022</h5>}>
        <ul>
          <li>Create applications in order to demonstrate a diverse range of technologies used in presentations</li>
          <li>Assist other core members with the organization of events</li>
        </ul>
      </Panel>
      <Panel header={<h3>Education</h3>}>
        <ul>
          <li>BSc in Software Development (First Class Honours) 2020 - 2023</li>
          <li>Currently studying for BSc (Honours) in Software Development 2023 - 2024</li>
        </ul>
      </Panel>
      <Panel header={<h3>Technologies</h3>}>
        <Row>
          <Col>
            <ul>
              <li>Kotlin</li>
              <li>Java</li>
              <li>Python</li>
              <li>C#</li>
            </ul>
          </Col>
          <Col>
            <ul>
              <li>Spring / Spring Boot</li>
              <li>Maven</li>
              <li>Git</li>
              <li>Docker</li>
            </ul>
          </Col>
          <Col>
            <ul>
              <li>HTTP</li>
              <li>C / C++</li>
              <li>SQL</li>
              <li>SQLite</li>
            </ul>
          </Col>
        </Row>
      </Panel>
    </Panel>
    </PanelGroup>
    </>
  );
}

export default Profile;