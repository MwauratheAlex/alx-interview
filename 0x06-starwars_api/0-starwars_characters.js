#!/usr/bin/node

/*
 * Script fetches and prints Star Wars characters for a given movie id
 *
 * Usage: ./0-starwars_characters.js <movie_id>')
 */

const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

async function fetchCharacterName (url) {
  const response = await requestPromise({ url, json: true });
  const name = response.body.name;
  console.log(name);
}

async function fetchCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  const response = await requestPromise({ url, json: true });
  const characterUrls = response.body.characters;

  for (const url of characterUrls) {
    await fetchCharacterName(url);
  }
}

fetchCharacters(movieId);
