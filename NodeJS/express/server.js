var express = require('express')
var app = express()

app.get('/', home)
app.get('/courses', courses)

function home(request, respond) {
  respond.send('Here is <strong>Home</strong>')
}

function courses(request, respond) {
  respond.send('Here is <strong>Courses</strong>')
}

app.listen(8080)