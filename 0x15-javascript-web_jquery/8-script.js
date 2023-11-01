#!/usr/bin/node

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  let names = data.results;
  for (let i of names) {
    $('UL#list_movies').append(`<li>${i.title}</li>`);
  }
});
