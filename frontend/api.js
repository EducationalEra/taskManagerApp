let url = 'http://localhost:8081/todo'
/**
 * Calls a get server's method of the tasks list
 *
 * @returns {promise}
 */
let getTodos = function () {
  return $.ajax({
    method: 'GET',
    url: url
  })
}
/**
 * Posts a new todo task object to the server
 *
 * @param {string} todo
 * @returns {promise}
 */
let postTodo = function (todo) {
  return $.ajax({
    method: 'POST',
    url: url,
    contentType: 'application/json',
    data: JSON.stringify({
      todo: todo
    })
  })
}
/**
 * Method that is needed to be implemented
 * @param {string} todo
 */
let deleteTodo = function (todo) {

}

let api = {
  getTodos: getTodos,
  postTodo: postTodo,
  deleteTodo: deleteTodo
}
