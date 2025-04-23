//import logo from './logo.svg';
//import './App.css';

function Header() {
    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <a className="navbar-brand" href="#">Luminooo</a>
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item active">
            <a className="nav-link" href="#">Courses <span className="sr-only">(current)</span></a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#">Teachers</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#">Exam</a>
          </li>
          <li className="nav-item">
            <a className="nav-link disabled" href="#" tabIndex="-1" aria-disabled="true">Disabled</a>
          </li>
        </ul>
      </div>
    </nav>
    );
  }
  
  export default Header;
  