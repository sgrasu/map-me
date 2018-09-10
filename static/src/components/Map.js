import React, {Component} from 'react';
import ReactMapGL from 'react-map-gl';

class Map extends Component {

  state = {
    viewport: {
      width: 500,
      height: 500,
      latitude: 37.7577,
      longitude: -122.4376,
      zoom: 8
    }
  };
  componentDidMount() {
    window.addEventListener('resize', this._resize);
    this._resize();
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this._resize);
  }

  _resize = () => {
    this.setState({
      viewport: {
        ...this.state.viewport,
        width: this.props.width || window.innerWidth,
        height: this.props.height || window.innerHeight
      }
    });
  };
  render() {
    return (
      <ReactMapGL
      mapboxApiAccessToken = 'pk.eyJ1Ijoic2dyYXN1IiwiYSI6ImNqbGxwOWV5OTB6eHgzcGxkdTRwbmF1MHoifQ.iF-dbH3wdRc0Y_mr4oGDEA'

        {...this.state.viewport}
        onViewportChange={(viewport) => this.setState({viewport})}
      />
    );
  }
}
export default Map