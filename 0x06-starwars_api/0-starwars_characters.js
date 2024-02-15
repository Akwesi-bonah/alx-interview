#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${url}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const characters = JSON.parse(body).characters;
    const characterName = characters.map(
      (Url) =>
        new Promise((resolve, reject) => {
          request(Url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
    );

    Promise.all(characterName)
      .then((names) => console.log(names.join('\n')))
      .catch((allErr) => console.log(allErr));
  });
}
