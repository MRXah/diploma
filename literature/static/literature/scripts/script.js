function toggleMenu() {
  let elements = document.querySelectorAll('.header__hamburger,.header__menu');

  elements.forEach(function (element) {
    element.classList.toggle('active');
  });
}

function toggleSearch() {
  let elements = document.querySelectorAll('.header__search,.header__search__button');

  elements.forEach(function (element) {
    element.classList.toggle('active');
  });
}

let url = 'api';
const U = document.getElementById('myUL');

fetch(url)
  .then((res) => res.json())
  .then((out) => {
    out.forEach((o) => {
      console.log(o);
      const L = document.createElement('li');
      L.innerHTML = `<a href="detail/${o.pk}">${o.fields.name}</a><br>`;
      U.appendChild(L);
    });
    if (out.length < 1) {
      const L = document.createElement('h1');
      L.innerText = `Нажаль ми не знайшли жодного місця((`;
      U.appendChild(L);
    }
  })
  .catch((err) => console.error(err));

function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById('myUL');
  li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName('a')[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = '';
    } else {
      li[i].style.display = 'none';
    }
  }
}

document.querySelector('.header__hamburger').addEventListener('click', toggleMenu);
document.querySelector('.header__search__button').addEventListener('click', toggleSearch);
