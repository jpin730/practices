// PROMISE EXAMPLE
// const somethingWillHappen1 = () => {
//   return new Promise((resolve, reject) => {
//     if (true) {
//       setTimeout(() => {
//         resolve('resolved1')
//       }, 2000)
//     } else {
//       reject(new Error('rejected'))
//     }
//   })
// }

// const somethingWillHappen2 = () => {
//   return new Promise((resolve, reject) => {
//     if (true) {
//       setTimeout(() => {
//         resolve('resolved2')
//       }, 2000)
//     } else {
//       reject(new Error('rejected'))
//     }
//   })
// }

// Promise.all([somethingWillHappen2(), somethingWillHappen1()]) // return after timeout 2 and then 1
//   .then(response => {
//     console.log('Arrays of results', response);
//   })
//   .catch(err => {
//     console.error(err);
//   })


const fetchData = require('../utils/fetchData')
const API = 'https://rickandmortyapi.com/api/character/'

fetchData(API)
  .then(data => { // then will turn to return: fetchData(...)
    console.log(data.info.count)
    return fetchData(`${API}${data.results[0].id}`)
  })
  .then(data => { // <- fetchData(API).fetchData(...).then()
    console.log(data.name);
    return fetchData(data.origin.url)
  })
  .then(data => { // <- fetchData(API).fetchData(...).fetchData(...).then()
    console.log(data.dimension);
  })
  .catch(err => console.error(err))