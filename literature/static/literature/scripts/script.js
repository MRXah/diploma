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

document.querySelector('.header__hamburger').addEventListener('click', toggleMenu);
document.querySelector('.header__search__button').addEventListener('click', toggleSearch);
