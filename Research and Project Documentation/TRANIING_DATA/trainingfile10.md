https://www.youtube.com/watch?v=Xev-pHAmkZ8

==============================================================================================
==============================================================================================
STEP 10: We will work on FrontEND 


            we have create a home component and try to call it through our app.js 

            (and index.js by default call app.js)

==============================================================================================
==============================================================================================

STEP 10.a
        10.a.1 FIRST create a components folder inside src and here we will create various components

        10.a.2 lets first create a file home.js inside components folder created above and   here we will create our home components

        10.a.3 inside ourc home.component.js we will simply copy paste the whole code of app.js for start
                and then change the code of Home as below 



                                    function Home() {
                                    return (
                                        <div className="App">
                                        <header className="App-header">
                                            <h3>Hello BRO we're at HOME </h3>
                                            
                                        </header>
                                        </div>
                                    );
                                    }

                                    export default Home;

        

==============================================================================================

OUR CODE SHALL BE of app.js will be 
            //import logo from './logo.svg';
                            import './App.css';
                            import Home from './components/Home.components'; // added at step 10
                            function App() {
                            return (
                                <div className="App">
                                <Home />   # we're calling the home component here step10
                                </div>
                            );
                            }

                            export default App;
