let v_instance = null;

class View {
  constructor() {
    if (v_instance) return v_instance;

    this.map = L.map('map', {
      maxZoom: 13,
      minZoom: 2,
    }).setView([49.604996, 34.544139], 7);

    this.markerIcon = L.icon({
      iconUrl: '/static/literature/images/marker.png',

      iconSize: [30, 30], // size of the icon
      iconAnchor: [15, 30], // point of the icon which will correspond to marker's location
      popupAnchor: [0, -30], // point from which the popup should open relative to the iconAnchor
    });

    this.map.on('click', this.onMapClick.bind(this));

    this._init();

    v_instance = this;
  }

  _init() {
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      attribution:
        'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      id: 'mapbox/streets-v11',
      tileSize: 512,
      zoomOffset: -1,
      accessToken: 'pk.eyJ1IjoibWlvbGV4IiwiYSI6ImNrczd2N3ZocDFneGMycHBoOGg3b2JwbTEifQ.OQjaxDOtII5wu1rCXKb-1Q',
    }).addTo(this.map);
  }

  onMapClick(e) {
    if (!ADMIN_MODE) return;
    // get position
    const popup = L.popup();

    popup
      .setLatLng(e.latlng)
      .setContent('You clicked the map at ' + e.latlng.toString())
      .openOn(this.map);
  }
}
