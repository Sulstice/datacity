import React from 'react';
import './App.css';
import apiService from "./services/ApiService"
import DCGrid from "./components/DCGrid"

function App() {
  var api = new apiService();
  var cacheBreaker = Math.floor(Math.random() * Math.floor(10000000))
  var res = api.getData('https://raw.githubusercontent.com/Sulstice/datacity/master/data/government_community_crime_map_incident_payload.json' + '?' + cacheBreaker);
  return (
    <div style={{}} className="App">
        <section id="banner">
            <div className="inner">
                <header>
                    <h1>Welcome to DataCity</h1>
                </header>

                <footer>
                    <a href="#" className="button">Get Started</a>
                </footer>
            </div>
        </section>
        <div style={{'display':'flex', 'flex-direction':'column', 'align-items':'center'}}>

                <br/>
                <h2>Data Output</h2>
                <hr style={{ 'width':'75%'}}/>
                <div style={{'flex-grow':'1', 'width':'90%'}}>
                    <DCGrid data={res} ignoreFields={['Government Missing Incident Numbers']} />
                </div>
        </div>
    </div>
  );
}

export default App;
