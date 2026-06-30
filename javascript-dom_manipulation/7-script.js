const listMoviesElement = document.querySelector('#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(movie => {
        const movieLi = document.createElement('li');
        movieLi.textContent = movie.title;
        listMoviesElement.appendChild(movieLi);
    });
  });