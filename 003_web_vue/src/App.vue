<template>
  <div id="app" class="app">
    <header class="app-header">
      <h1>Vue 3 App</h1>

      <!-- Counter Section -->
      <div class="counter-section">
        <h2>Counter: {{ count }}</h2>
        <button @click="count++">Increment</button>
        <button @click="count--">Decrement</button>
        <button @click="count = 0">Reset</button>
      </div>

      <!-- Todo Section -->
      <div class="todo-section">
        <h2>Todo List</h2>
        <div class="todo-input">
          <input
            v-model="newTodo"
            @keyup.enter="addTodo"
            placeholder="Add a new todo..."
          />
          <button @click="addTodo">Add</button>
        </div>
        <ul class="todo-list">
          <li
            v-for="todo in todos"
            :key="todo.id"
            :class="{ completed: todo.completed }"
          >
            <span @click="toggleTodo(todo.id)">{{ todo.text }}</span>
            <button @click="deleteTodo(todo.id)">Delete</button>
          </li>
        </ul>
      </div>
    </header>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'App',
  setup() {
    const count = ref(0);
    const newTodo = ref('');
    const todos = ref([]);

    const addTodo = () => {
      if (newTodo.value.trim()) {
        todos.value.push({
          id: Date.now(),
          text: newTodo.value,
          completed: false
        });
        newTodo.value = '';
      }
    };

    const toggleTodo = (id) => {
      const todo = todos.value.find(t => t.id === id);
      if (todo) {
        todo.completed = !todo.completed;
      }
    };

    const deleteTodo = (id) => {
      todos.value = todos.value.filter(t => t.id !== id);
    };

    return {
      count,
      newTodo,
      todos,
      addTodo,
      toggleTodo,
      deleteTodo
    };
  }
};
</script>

<style>
.app {
  text-align: center;
}

.app-header {
  background-color: #35495e;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
  padding: 20px;
}

.counter-section {
  margin: 20px 0;
}

.counter-section button {
  margin: 0 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #42b983;
  border: none;
  border-radius: 5px;
  color: white;
  font-weight: bold;
}

.counter-section button:hover {
  background-color: #33a06f;
}

.todo-section {
  margin-top: 40px;
  width: 100%;
  max-width: 500px;
}

.todo-input {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.todo-input input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: 2px solid #42b983;
  border-radius: 5px;
  background-color: #2c3e50;
  color: white;
}

.todo-input button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #42b983;
  border: none;
  border-radius: 5px;
  color: white;
  font-weight: bold;
}

.todo-list {
  list-style: none;
  padding: 0;
}

.todo-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  margin: 5px 0;
  background-color: #2c3e50;
  border-radius: 5px;
}

.todo-list li span {
  flex: 1;
  text-align: left;
  cursor: pointer;
}

.todo-list li.completed span {
  text-decoration: line-through;
  opacity: 0.5;
}

.todo-list li button {
  padding: 5px 10px;
  font-size: 14px;
  cursor: pointer;
  background-color: #e74c3c;
  border: none;
  border-radius: 3px;
  color: white;
}
</style>
