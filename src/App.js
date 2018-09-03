import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import ReactMapboxGl, { Layer, Feature } from "react-mapbox-gl";

const Map = ReactMapboxGl({
  accessToken: 'pk.eyJ1Ijoic2dyYXN1IiwiYSI6ImNqbGxwOWV5OTB6eHgzcGxkdTRwbmF1MHoifQ.iF-dbH3wdRc0Y_mr4oGDEA'
});

// or "const mapboxgl = require('mapbox-gl');"


class App extends Component {

  render() {
    return (
      <div class='App col12 pad4 contain fill-navy dark clip'>
        <div className='sidebar pad2'>Listing</div>
        <div id='map' className='map pad2'>
          <Map
            style="mapbox://styles/mapbox/streets-v9"
            containerStyle={{
              height: "100vh",
              width: "100vw"
            }}>
            <Layer
              type="symbol"
              id="marker"
              layout={{ "icon-image": "marker-15" }}>
              <Feature coordinates={[-0.481747846041145, 51.3233379650232]} />
            </Layer>
          </Map></div>
      </div>
    );
  }
}

export default App;
