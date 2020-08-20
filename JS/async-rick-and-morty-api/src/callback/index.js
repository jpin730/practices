let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest
let API = 'https://rickandmortyapi.com/api/character/'

function fetchData (url_api, callback) {
  let xhttp = new XMLHttpRequest()
  xhttp.open('GET', url_api, true) // explicit true for async mode (default is true)
  xhttp.onreadystatechange = function (event) {
    // status:
    // (0) init, (1) loading, (2) loaded, is any data (3) downloaded, (4) completed
    if (xhttp.readyState === 4) {
      if (xhttp.status === 200) {
        // callback standard: (error, info)
        callback(null, JSON.parse(xhttp.responseText)) // text to object
      } else {
        const error = new Error('Error' + url_api)
        return callback(error, null)
      }
    }
  }
  xhttp.send()
}

fetchData(API, function(error1, data1) {
  if (error1) return console.error(error1)
  fetchData(API + data1.results[0].id, function(error2, data2) {
    if (error2) return console.error(error2)
    fetchData(data2.origin.url, function(error3, data3) {
      if (error3) return console.error(error3)
      console.log(data1.info.count)
      console.log(data2.name)
      console.log(data3.dimension)
    })
  })
})