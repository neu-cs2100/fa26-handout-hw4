"""HW4 Question 2

Write a class TodoList that keeps track of a list of tasks. It should let a user do the following:
- view all unfinished tasks
- add a new unfinished task
- remove an existing task if a user marks it as complete

Requirements:

The constructor should initialize an empty list of unfinished tasks.
Each unfinished task should be stored as a string (a description of the task).
A method add_task(self, description: str) -> None that adds a new unfinished task to the todo 
        list.
A method complete_task(self, index: int = 0) -> None that, as the task at the given index 
        is completed, the method is to remove it from the list. If the client does not 
        specify an index, the first task is completed.
A method get_pending(self) -> list[str] that returns the descriptions of all unfinished tasks.

Make sure to write appropriate tests in test_q2.py.

Example usage:

todo = TodoList()
todo.add_task("Attend CS 2100 office hours")
todo.add_task("Fold laundry")

print(todo.get_pending())    # ["Attend CS 2100 office hours", "Fold laundry"]

todo.complete_task(1)

print(todo.get_pending())    # ["Attend CS 2100 office hours"]

todo.complete_task(0)

print(todo.get_pending())    # []
"""

class TodoList:
    """Class representing a todo list with unfinished tasks that can be added, 
    completed, and viewed."""

def main() -> None:
    """Main method demonstrating the usage of the TodoList class."""
    # # Un-comment the code below to run it once the TodoList class is implemented
    # todo = TodoList()
    # todo.add_task("Attend CS 2100 office hours")
    # todo.add_task("Fold laundry")
    # print(todo.get_pending())    # ["Attend CS 2100 office hours", "Fold laundry"]
    # todo.complete_task(1)
    # print(todo.get_pending())    # ["Attend CS 2100 office hours"]
    # todo.complete_task(0)
    # print(todo.get_pending())    # []

if __name__ == '__main__':
    main()
