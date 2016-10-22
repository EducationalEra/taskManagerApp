var url = 'http://localhost:8081/todo'

var getTodos = function () {
  return $.ajax({
    method: 'GET',
    url: url
  })
}

var postTodo = function (todo) {
  return $.ajax({
    method: 'POST',
    url: url,
    data: todo
  })
}

var deleteTodo = function (id) {

}
var api = {
  getTodos: getTodos,
  postTodo: postTodo,
  deleteTodo: deleteTodo
}
