import { FaGithub, FaLinkedin, FaEnvelope } from 'react-icons/fa'
import { IconContext } from 'react-icons'
import { Outlet } from 'react-router-dom';
import { Sidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import { Link } from 'react-router-dom';
import { Container, Header, Content, Footer, Sidebar as SideBarContainer } from 'rsuite';
import 'rsuite/dist/rsuite.min.css';

function Root() {
  return (
  <Container>
    <Container>
    <Header>
      <nav className='nav'>
      <a href="" className="site-title">Data Science & Machine Learning Portfolio</a>
      <ul>
        <IconContext.Provider value={{ className: "shared-class", size: "42" }}>
        <li>
          <a href="https://www.github.com/AlexDarigan/mtg-rest"><FaGithub/></a>
        </li>
        <li>
          <a href="https://www.linkedin.com/in/daviddarigan/"><FaLinkedin/></a>
        </li>
        <li>
          <a href="mailto:C00263218@setu.ie"><FaEnvelope/></a>
        </li>
        </IconContext.Provider>
      </ul>
    </nav>
    </Header>
    </Container>
    <Container>
    <SideBarContainer>  
      <Sidebar style={{height: "100vh"}}>
      <Menu>
        <SubMenu label="About Me">
          <MenuItem><Link to={"portfolio"}>About Me</Link></MenuItem>
          <MenuItem>Experience</MenuItem>
          <MenuItem>Education</MenuItem>
          <MenuItem>Technologies</MenuItem>
        </SubMenu>
        <SubMenu label="Projects">
          <MenuItem>Introduction / Mission Statement</MenuItem>
          <MenuItem>REST Project Design</MenuItem>
          <MenuItem>Data Sourcing</MenuItem>
          <MenuItem>Data Preprocessing</MenuItem>
          <MenuItem>Example Charts</MenuItem>
          <MenuItem>Code</MenuItem>
          <MenuItem>Oppurtunities</MenuItem>
          <MenuItem>Challenges</MenuItem>
        </SubMenu>
        <SubMenu label="REST API">
          <MenuItem>REST Structure</MenuItem>
          <MenuItem>Measures</MenuItem>
          <MenuItem>Price</MenuItem>
        </SubMenu>
      </Menu>
      </Sidebar>
    </SideBarContainer>
      <Content>
      <div id="detail" style={{border: "2px blue solid", backgroundColor: "red", width: "100px", height: "100px"}}>
        <Outlet />
      </div>
      </Content>
      </Container>
      <Container>
      <Footer>Footer</Footer>
      </Container>
    </Container>
  );
}

export default Root;
