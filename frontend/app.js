let enterCode = 13;

let displayTodos = function () {

}

let addTodo = function (event) {
  let inputField = event.target;
  let text = inputField.value;

  if (event.which === enterCode && text !== '') {
    let newli = document.createElement('li');

    newli.textContent = text;
    document.getElementById('todo-list').appendChild(newli);
    inputField.value = '';
  }
};

let teachNewTodoFieldToAddTodos = function () {
  document.getElementById('new-todo').addEventListener('keyup', addTodo);
};

document.addEventListener('DOMContentLoaded', teachNewTodoFieldToAddTodos);
