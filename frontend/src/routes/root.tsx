import { FaGithub, FaLinkedin, FaMailchimp} from 'react-icons/fa'
import { IconContext } from 'react-icons'
import { Outlet } from 'react-router-dom';

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
          <a href="/linkedin"><FaLinkedin/></a>
        </li>
        <li>
          <a href="/email"><FaMailchimp/></a>
        </li>
        </IconContext.Provider>
      </ul>
    </nav>
    <div id="detail">
      <Outlet />
    </div>
    </>
  );
}

export default Root;