import React from 'react';
import './App.css';
import apiService from "./services/ApiService"
import DCGrid from "./components/DCGrid"

function App() {
  var api = new apiService();
  var res = api.getData('https://raw.githubusercontent.com/Sulstice/datacity/master/data/government_community_crime_map_incident_payload.json');
  var styles = {'display':'flex'};
  return (
    <div style={styles} className="App">
      <div style={{"flex-grow":'1'}}>
        <DCGrid data={res} ignoreFields={['community_crime_map_missing_incident_numbers']} />
      </div>
    </div>
  );
}

export default App;
