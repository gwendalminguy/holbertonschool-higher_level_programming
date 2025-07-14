const header = document.querySelector('header');
const red = document.querySelector('#red_header');

red.addEventListener('click', () => {
  header.classList.add('red');
});
