//import logo from './logo.svg';
import './App.css';
//import Home from './components/Home.components'; // added at step 10 ,then commented out at step11
import Main from './components/Main.components'; // added at step 11
function App() {
  return (
    <div className="App">
      <Main />   { /*we're calling the home component here*/  }
    </div>
  );
}

export default App;
