const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(url).then((response) => {
  return response.json();
}).then((data) => {
  document.querySelector('#hello').textContent = data.hello;
});
