import { FaGithub, FaLinkedin, FaEnvelope } from 'react-icons/fa'
import { IconContext } from 'react-icons'
import { Outlet } from 'react-router-dom';
import { Container, Header, Content, Sidebar, Navbar, Nav } from 'rsuite';
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

// Two Seperate ones for card prices, get card, then get trend?
// Same with predictions?
function APIMenu() {
return (
  <Nav.Menu eventKey="3" title="MTG Rest API">
    <Nav.Item eventKey='3-1'>Introduction</Nav.Item>
    <Nav.Menu eventKey="4" title="api/v1">
      <Nav.Item eventKey='3-2'>/color/distribution</Nav.Item>
      <Nav.Item eventKey="3-1">/price/trend</Nav.Item> 
      <Nav.Item eventKey="3-2">/price/prediction</Nav.Item>
    </Nav.Menu>
   
  </Nav.Menu>
  );
}

function SidebarContent() {
  return (
      <Sidenav defaultOpenKeys={['3', '4']}>
        <Sidenav.Body>
          <Nav activeKey="1">
          <Nav.Item eventKey="1"><Link to="profile">About Me</Link></Nav.Item>
          <Nav.Item eventKey="2"><Link to="report">Data Science Report</Link></Nav.Item>
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
