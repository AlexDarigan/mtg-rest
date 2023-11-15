import { FaGithub, FaLinkedin, FaEnvelope } from 'react-icons/fa'
import { IconContext } from 'react-icons'
import { Outlet } from 'react-router-dom';
import { Container, Header, Content, Footer, Sidebar, Navbar, Nav } from 'rsuite';
import Sidenav from 'rsuite/Sidenav';
import { Link } from 'react-router-dom';
import 'rsuite/dist/rsuite.min.css';


function HeaderContent() {
  return (
      <Navbar>
        <Navbar.Brand><center style={{fontSize: "1rem"}}>Data Science & Machine Learning Portfolio</center></Navbar.Brand>
        <Nav pullRight>
        <IconContext.Provider value={{ className: "shared-class", size: "42" }}>
        <Nav.Item icon={<FaGithub/>}></Nav.Item>
        <Nav.Item icon={<FaLinkedin/>}></Nav.Item>
        <Nav.Item icon={<FaEnvelope/>}></Nav.Item>
        </IconContext.Provider>
      </Nav>
      </Navbar>
  );
}

function AboutMeMenu() {
return (
    <Nav.Menu eventKey="1" title="About Me">
    <Nav.Item eventKey="1-1"><Link to="portfolio">About Me</Link></Nav.Item>
    <Nav.Item eventKey="1-1">Experience</Nav.Item>
    <Nav.Item eventKey="1-1">Education</Nav.Item>
    <Nav.Item eventKey="1-1">Technologies</Nav.Item>
  </Nav.Menu>
  );
}

function ProjectMenu() {
  return ( 
    <Nav.Menu eventKey="2" title="Projects">
      <Nav.Item eventKey='2-1'><Link to="/dsml">Introduction / Mission Statement</Link></Nav.Item>
      <Nav.Item eventKey='2-2'>REST Project Design</Nav.Item>
      <Nav.Item eventKey='2-3'>Data Sourcing</Nav.Item>
      <Nav.Item eventKey='2-4'>Data Preprocessing</Nav.Item>
      <Nav.Item eventKey='2-5'>Example Charts</Nav.Item>
      <Nav.Item eventKey='2-6'>Code</Nav.Item>
      <Nav.Item eventKey='2-7'>Oppurtunities</Nav.Item>
      <Nav.Item eventKey='2-8'>Challenges</Nav.Item>
    </Nav.Menu>
  );
}

function APIMenu() {
return (
  <Nav.Menu eventKey="3" title="MTG Rest API">
    <Nav.Item eventKey="3-1">Project Structure</Nav.Item>
    <Nav.Item eventKey="3-2">Measure</Nav.Item>
    <Nav.Item eventKey="3-3">Price/Trends</Nav.Item>
    <Nav.Item eventKey="3-3">Price/Predictions</Nav.Item>
  </Nav.Menu>
  );
}

function SidebarContent() {
  return (
      <Sidenav defaultOpenKeys={['3', '4']}>
        <Sidenav.Body>
          <Nav activeKey="1">
            
            <AboutMeMenu/>
            <ProjectMenu/>
            <APIMenu/>
          </Nav>
        </Sidenav.Body>
      </Sidenav>    
    );
}

function Root() {
  return (
    <Container>
      <Container>
        <Header>
          <HeaderContent/>
        </Header>
      </Container>
      <Container>
        <Sidebar style={{height: "100vh"}}><SidebarContent/></Sidebar>
        <Content id="detail"><Outlet/></Content>
      </Container>
    </Container>
  );
}

export default Root;
