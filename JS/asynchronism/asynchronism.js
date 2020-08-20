const API_URL = 'https://swapi.dev/api/'
const PEOPLE_URL = 'people/:id'
const opts = { crossDomain: true }

// function getCharacter(id, callback) {
//   const url = `${API_URL}${PEOPLE_URL.replace(':id', id)}`
//   $.get(url, opts, function (character) {
//     console.log(`Hi, I'm ${character.name} ${id}`)
//     if (callback) {
//       callback()
//     }
//   })
// }
// // CALLBACKS HELL
// getCharacter(1, function () {
//   getCharacter(2, function () {
//     getCharacter(3, function () {
//       getCharacter(4, function () {
//         getCharacter(5, function () {
//           getCharacter(6, function () {
//             getCharacter(7)
//           })
//         })
//       })
//     })
//   })
// })

// function getCharacter(id, callback) {
//   const url = `${API_URL}${PEOPLE_URL.replace(':id', id)}`
//   $.get(url, opts, callback).fail(function () {
//     console.log(`Error: Character with id ${id} cannot be loaded`);
//   })
// }
// getCharacter(1, function (character) {
//   console.log(`Hi, I'm ${character.name}`)
//   getCharacter(2, function (character) {
//     console.log(`Hi, I'm ${character.name}`)
//     getCharacter(3, function (character) {
//       console.log(`Hi, I'm ${character.name}`)
//       getCharacter(4, function (character) {
//         console.log(`Hi, I'm ${character.name}`)
//         getCharacter(5, function (character) {
//           console.log(`Hi, I'm ${character.name}`)
//           getCharacter(6, function (character) {
//             console.log(`Hi, I'm ${character.name}`)
//             getCharacter(7, function (character) {
//               console.log(`Hi, I'm ${character.name}`)
//             })
//           })
//         })
//       })
//     })
//   })
// })


function getCharacter(id) {
  return new Promise((resolve, reject) => {
    const url = `${API_URL}${PEOPLE_URL.replace(':id', id)}`
    $
      .get(url, opts, function(data) {
        resolve(data)
      })
      .fail(() => reject(id))
  })
}
function sayHi({name}) {
  console.log(`Hi, I'm ${name}`)
}
function onError(id) {
  console.log(`Error: Character with id ${id} cannot be loaded`)
}
// // NESTED PROMISES
// getCharacter(1)
//   .then(character => {
//     sayHi(character)
//     return getCharacter(2)
//   })
//   .then(character => {
//     sayHi(character)
//     return getCharacter(3)
//   })
//   .then(character => {
//     sayHi(character)
//     return getCharacter(4)
//   })
//   .then(character => {
//     sayHi(character)
//     return getCharacter(5)
//   })
//   .then(sayHi)
//   .catch(onError)

// MULTI PARALLEL PROMISES
async function getCharacters() {
  var ids = [1, 2, 3, 4, 5]
  // var promises = ids.map(function (id) {
  //   return getCharacter(id)
  // })
  var promises = ids.map(id => getCharacter(id))
  /* Promise
  .all(promises)
  .then(characters => characters.map(sayHi))
  .catch(onError) */
  try {
    var characters = await Promise.all(promises) // await until resolve all promises
    characters.map(sayHi)
  } catch (id) {
    onError(id)
  }
}

getCharacters()