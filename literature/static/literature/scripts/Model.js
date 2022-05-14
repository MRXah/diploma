let m_instance = null;

class Model {
  constructor(blob) {
    if (m_instance) return m_instance;
    // imitation of database
    this.database = [];
    blob.forEach((e) => {
      this.database.push([[e.fields.x, e.fields.y], e.fields.name, e.pk]);
    });
    m_instance = this;
  }
}
