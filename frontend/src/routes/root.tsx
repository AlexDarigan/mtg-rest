import { FaGithub, FaLinkedin, FaEnvelope } from 'react-icons/fa'
import { IconContext } from 'react-icons'
import { Outlet } from 'react-router-dom';
import { Sidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';


function Root() {
  return (
    <>
    <nav className='nav'>
      <a href="" className="site-title">Site Name</a>
      <ul>
        <li>
          <a href="Portfolio">About Me</a>
        </li>
        <li>
          <a href="mtgrest">M:TG Rest API</a>
        </li>
        <li>
          <a href="dsml">DSMLX</a>
        </li>
      </ul>
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
    <div id="detail">
      <Outlet />
    </div>
    <Sidebar>
    <Menu>
    <SubMenu label="About Me">
      <MenuItem>About Me</MenuItem>
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
    </>
  );
}

export default Root;
