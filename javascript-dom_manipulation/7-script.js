const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movies = document.querySelector('ul#list_movies');

fetch(url).then((response) => {
  return response.json();
}).then((data) => {
  for (let i = 0; i < data.results.length; i++) {
    const newItem = document.createElement('li');
    newItem.innerText = data.results[i].title;
    movies.appendChild(newItem);
  }
});
