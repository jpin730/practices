// ASYNC EXAMPLE
// const doSomethingAsync = () => {
//   return new Promise((resolve, reject) => {
//     true
//       ? setTimeout(() => resolve('Do something async'), 3000)
//       : reject(new Error('Test Error'))
//   })
// }

// const doSomething = async () => {
//   const something = await doSomethingAsync()
//   console.log(something)
// }

// doSomething()

// const anotherFunction = async () => {
//   try {
//     const something = await doSomethingAsync()
//     console.log(something)
//   }
//   catch { // optional catch binding: catch(error)
//     console.error(error)
//   }
// }

// anotherFunction()

const fetchData = require('../utils/fetchData')
const API = 'https://rickandmortyapi.com/api/character/'

const anotherFunction = async (url_api) => {
  try {
    const data = await fetchData(url_api)
    const character = await fetchData(`${API}${data.results[0].id}`)
    const origin = await fetchData(character.origin.url)
    console.log(data.info.count)
    console.log(character.name)
    console.log(origin.dimension)
  }
  catch { // optional catch binding: catch(error)
    console.error(error)
  }
}

anotherFunction(API)