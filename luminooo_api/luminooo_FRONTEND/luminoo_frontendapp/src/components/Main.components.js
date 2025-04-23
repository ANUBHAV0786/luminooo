
import Home  from './Home.components.js'; // added at step 11
import Header from './Header.components';
import Footer from './Footer.components';


function Main() {
    return (
      <div className="container">
        <Header /> {/* we're calling the header component here created at step 11 */}
        <Home />   {/* we're calling the home component here created at step10 ( but this is step11)*/}
        <Footer /> {/* we're calling the footer component here created at step 11 */}
          {/* <h3>Hello BRO we're at MAin </h3> */}
          
        
      </div>
    );
  }
  
  export default Main;