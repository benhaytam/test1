import json
import os

class ToDoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load()

    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                # Handle empty or corrupt JSON files gracefully
                return []
        return []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.todos, f, indent=4)

    def add(self, task):
        self.todos.append({"task": task, "done": False})
        self.save()
        print(f"Added: {task}")

    def list(self):
        if not self.todos:
            print("No tasks found.")
            return
        for i, todo in enumerate(self.todos):
            status = "✅" if todo["done"] else "❌"
            print(f"{i + 1}. {status} {todo['task']}")

    def mark_done(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]["done"] = True
            self.save()
            print(f"Marked as done: {self.todos[index]['task']}")
        else:
            print("Invalid task number.")

    def delete(self, index):
        if 0 <= index < len(self.todos):
            removed = self.todos.pop(index)
            self.save()
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")

if __name__ == "__main__": print("Welcome to ToDoList!")
