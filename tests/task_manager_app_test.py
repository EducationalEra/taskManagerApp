from selene.support.conditions import have
from selene.tools import visit, s, ss


def test_add_tasks():
    visit('http://localhost:8081')

    s('#new-todo').set_value('watch lesson').press_enter()
    ss('#todo-list>li').should(have.exact_texts('watch lesson'))

    s('#new-todo').set_value('do homework').press_enter()
    ss('#todo-list>li').should(have.exact_texts('watch lesson', 'do homework'))
