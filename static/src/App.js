import React, { Component } from 'react';
import './App.css';
import ReactMapboxGl, { Layer, Feature, GeoJSONLayer } from "react-mapbox-gl";
import * as geojson from './sample_points.json';
import Map from './components/Map'

// const Map = ReactMapboxGl({
//   accessToken: 'pk.eyJ1Ijoic2dyYXN1IiwiYSI6ImNqbGxwOWV5OTB6eHgzcGxkdTRwbmF1MHoifQ.iF-dbH3wdRc0Y_mr4oGDEA'
// });



class App extends Component {

  render() {
    return (
      <div class='App col12 pad4 contain fill-navy dark clip'>
        <div className='sidebar pad2'>Listing</div>
        <div id='map' className='map pad2'>
        <Map></Map>
        </div>
      </div>
    );
  }
}

export default App;
