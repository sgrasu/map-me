import React, { Component } from 'react';
import './App.css';
import ReactMapboxGl, { Layer, Feature, GeoJSONLayer } from "react-mapbox-gl";
import * as SAMPLES from './sample_points.json';
import Map from './components/Map'
import BreweryPin from './components/BreweryPin'
import {Marker} from 'react-mapbox-gl'

class App extends Component {

  _renderBreweryMarker = (city, index) => {
    return (
      <Marker key={`marker-${index}`}
        longitude={city.longitude}
        latitude={city.latitude} >
        <BreweryPin size={20} onClick={() => this.setState({popupInfo: city})} />
      </Marker>
    );
  }

  render() {
    return (
      <div class='App col12 pad4 contain fill-navy dark clip'>
        <div className='sidebar pad2'>Listing</div>
        <div id='map' className='map pad2'>
        <Map>{SAMPLES.map(this._renderBreweryMarker)}</Map>
        </div>
      </div>
    );
  }
}

export default App;
