let enterCode = 13

/**
 * Gets a list of todos from a server and displays them in a list
 */
let displayTodos = function () {
  api.getTodos().then(function (todos) {
    for (let i = 0; i < todos.length; i++) {
      let newli = document.createElement('li')
      newli.textContent = todos[i]
      document.getElementById('todo-list').appendChild(newli)
    }
  })
}

/**
 * Calls an api to add a new task to the list and then calls the displayTodos function to display the new list of todos
 * @param event
 */
let addTodo = function (event) {
  let inputField = event.target
  let text = inputField.value

  if (event.which === enterCode && text !== '') {
    api.postTodo(text).then(function () {
      displayTodos()
      inputField.value = ''
    })
  }
}

let teachNewTodoFieldToAddTodos = function () {
  document.getElementById('new-todo').addEventListener('keyup', addTodo)
}

document.addEventListener('DOMContentLoaded', teachNewTodoFieldToAddTodos)
displayTodos()
