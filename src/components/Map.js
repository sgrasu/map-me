import React, {Component} from 'react';

class Map extends Component {
    componentDidMount() {
        this.map = new mapboxgl.Map({
          container: this.mapContainer,
          style: 'mapbox://styles/mapbox/streets-v9'
        });
      }
    
      componentWillUnmount() {
        this.map.remove();
      }
    
      render() {
    
        return <div  ref={el => this.mapContainer = el} />;
      }
    }
export default Map;