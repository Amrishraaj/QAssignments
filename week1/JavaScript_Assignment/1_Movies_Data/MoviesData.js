
const movies_url = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies-2010s.json?'

async function fetchMovies(url) {
  console.log('fetching movies data...')
  const movies = await fetch(url)
  const moviesData = await movies.json()
  console.log('movies data fetched successfully')

  // map contains actor name as key and movies list as value
  let actorsMap = {}

  // map contains genre as key and movies list as value
  let genreMap = {}
  moviesData.forEach(movie => {
    let actors = movie.cast
    actors.forEach(actor => {
      
      //there is some issue with API data, so I have used some conditions to avoid those data
      if(actor.length > 3 && /^[a-zA-Z]+$/.test(actor)) {
        if(actorsMap[actor] == undefined){
          actorsMap[actor] = [movie.title]
        }
        else{
          actorsMap[actor].push(movie.title)
        }
      }
    
    })

    //create genre map
    let genres = movie.genres
    genres.forEach(genre => {
      if(genreMap[genre] === undefined){
        genreMap[genre] = [movie.title]
      }
      else{
        genreMap[genre].push(movie.title)
      }
    })

  })

  //changing the actor map to required format [{actor: actorName, movies: [movie1, movie2, ...]}, ...]
  actorsMap = Object.keys(actorsMap).map(actor => {
    return {Name: actor, Movies: actorsMap[actor]}
  })

  //changing the genre map to required format [{genre: genreName, movies: [movie1, movie2, ...]}, ...]
  genreMap = Object.keys(genreMap).map(genre => {
    return {Type: genre, Movies: genreMap[genre]}
  })

  //updating the DOM
  document.querySelector('#genre-data').innerHTML = JSON.stringify(genreMap, undefined, 4)
  document.querySelector('#actors-data').innerHTML = JSON.stringify(actorsMap, undefined, 4)
}

fetchMovies(movies_url)