document.addEventListener('DOMContentLoaded', function () {
  const button = document.querySelector('#btn_translate');

  button.addEventListener('click', () => {
    const language = document.querySelector('#language_code').value;
    const url = `https://hellosalut.stefanbohacek.com/?lang=${language}`;
    fetch(url).then(function (response) {
      return response.json();
    }).then(function (data) {
      document.querySelector('#hello').textContent = data.hello;
    });
  });
});
