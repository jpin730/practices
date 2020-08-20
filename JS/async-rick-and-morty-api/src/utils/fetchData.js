let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest

const fetchData = url_api => {
  return new Promise((resolve, reject) => {
    const xhttp = new XMLHttpRequest()
    xhttp.open('GET', url_api, true) // explicit true for async mode (default is true)
    xhttp.onreadystatechange = (() => {
      // status:
      // (0) init, (1) loading, (2) loaded, is any data (3) downloaded, (4) completed
      if (xhttp.readyState === 4) {
        (xhttp.status === 200)
          ? resolve(JSON.parse(xhttp.responseText))
          : reject(new Error('Error', url_api))
      }
    })
    xhttp.send()
  })
}

module.exports = fetchData