let c_instance = null;

class Controller {
  constructor(model, view) {
    if (c_instance) return c_instance;

    this.model = model;
    this.view = view;

    this._init();

    c_instance = this;
  }

  _init() {
    this._addPlacesFromDB();
  }

  _addPlacesFromDB() {
    this.model.database.forEach((element) => {
      L.marker([element[0][0], element[0][1]], { icon: this.view.markerIcon })
        .addTo(this.view.map)
        .bindPopup(
          `<p id='place-id' hidden>${element[2]}</p><b><i>${element[1]}</i></b><br><a href="detail/${element[2]}">Переглянути інформацію</a>`
        );
    });
  }
}
