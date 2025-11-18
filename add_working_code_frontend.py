#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프론트엔드 주요 템플릿에 실제 동작하는 코드 추가
React, Vue, Angular
"""

import os
import json
from pathlib import Path

templates_to_improve = {
    "002_web_react": {
        "files": {
            "src/App.js": """import React, { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const addTodo = () => {
    if (inputValue.trim()) {
      setTodos([...todos, { id: Date.now(), text: inputValue, completed: false }]);
      setInputValue('');
    }
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>React App</h1>

        {/* Counter Section */}
        <div className="counter-section">
          <h2>Counter: {count}</h2>
          <button onClick={() => setCount(count + 1)}>Increment</button>
          <button onClick={() => setCount(count - 1)}>Decrement</button>
          <button onClick={() => setCount(0)}>Reset</button>
        </div>

        {/* Todo Section */}
        <div className="todo-section">
          <h2>Todo List</h2>
          <div className="todo-input">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && addTodo()}
              placeholder="Add a new todo..."
            />
            <button onClick={addTodo}>Add</button>
          </div>
          <ul className="todo-list">
            {todos.map(todo => (
              <li key={todo.id} className={todo.completed ? 'completed' : ''}>
                <span onClick={() => toggleTodo(todo.id)}>{todo.text}</span>
                <button onClick={() => deleteTodo(todo.id)}>Delete</button>
              </li>
            ))}
          </ul>
        </div>
      </header>
    </div>
  );
}

export default App;
""",
            "src/App.css": """.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
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
  background-color: #61dafb;
  border: none;
  border-radius: 5px;
  color: #282c34;
  font-weight: bold;
}

.counter-section button:hover {
  background-color: #4fa8c5;
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
  border: 2px solid #61dafb;
  border-radius: 5px;
  background-color: #1e2127;
  color: white;
}

.todo-input button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #61dafb;
  border: none;
  border-radius: 5px;
  color: #282c34;
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
  background-color: #1e2127;
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
""",
            "src/index.js": """import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
""",
            "src/index.css": """body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
""",
            "public/index.html": """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="React App - Production Ready Template" />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
"""
        },
        "package_updates": {
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "web-vitals": "^2.1.4"
            },
            "scripts": {
                "start": "react-scripts start",
                "build": "react-scripts build",
                "test": "react-scripts test",
                "eject": "react-scripts eject"
            },
            "devDependencies": {
                "react-scripts": "5.0.1"
            }
        }
    },
    "003_web_vue": {
        "files": {
            "src/App.vue": """<template>
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
""",
            "src/main.js": """import { createApp } from 'vue';
import App from './App.vue';
import './style.css';

createApp(App).mount('#app');
""",
            "src/style.css": """body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  text-align: center;
}
""",
            "index.html": """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vue 3 App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
""",
            "vite.config.js": """import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
});
"""
        },
        "package_updates": {
            "dependencies": {
                "vue": "^3.3.11"
            },
            "devDependencies": {
                "@vitejs/plugin-vue": "^4.5.2",
                "vite": "^5.0.8"
            },
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview"
            }
        }
    },
    "004_web_angular": {
        "files": {
            "src/app/app.component.ts": """import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface Todo {
  id: number;
  text: string;
  completed: boolean;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Angular App';
  count = 0;
  newTodo = '';
  todos: Todo[] = [];

  increment() {
    this.count++;
  }

  decrement() {
    this.count--;
  }

  reset() {
    this.count = 0;
  }

  addTodo() {
    if (this.newTodo.trim()) {
      this.todos.push({
        id: Date.now(),
        text: this.newTodo,
        completed: false
      });
      this.newTodo = '';
    }
  }

  toggleTodo(id: number) {
    const todo = this.todos.find(t => t.id === id);
    if (todo) {
      todo.completed = !todo.completed;
    }
  }

  deleteTodo(id: number) {
    this.todos = this.todos.filter(t => t.id !== id);
  }
}
""",
            "src/app/app.component.html": """<div class="app">
  <header class="app-header">
    <h1>{{ title }}</h1>

    <!-- Counter Section -->
    <div class="counter-section">
      <h2>Counter: {{ count }}</h2>
      <button (click)="increment()">Increment</button>
      <button (click)="decrement()">Decrement</button>
      <button (click)="reset()">Reset</button>
    </div>

    <!-- Todo Section -->
    <div class="todo-section">
      <h2>Todo List</h2>
      <div class="todo-input">
        <input
          [(ngModel)]="newTodo"
          (keyup.enter)="addTodo()"
          placeholder="Add a new todo..."
        />
        <button (click)="addTodo()">Add</button>
      </div>
      <ul class="todo-list">
        <li
          *ngFor="let todo of todos"
          [class.completed]="todo.completed"
        >
          <span (click)="toggleTodo(todo.id)">{{ todo.text }}</span>
          <button (click)="deleteTodo(todo.id)">Delete</button>
        </li>
      </ul>
    </div>
  </header>
</div>
""",
            "src/app/app.component.css": """.app {
  text-align: center;
}

.app-header {
  background-color: #1976d2;
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
  background-color: #fff;
  border: none;
  border-radius: 5px;
  color: #1976d2;
  font-weight: bold;
}

.counter-section button:hover {
  background-color: #f0f0f0;
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
  border: 2px solid #fff;
  border-radius: 5px;
  background-color: #0d47a1;
  color: white;
}

.todo-input button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #fff;
  border: none;
  border-radius: 5px;
  color: #1976d2;
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
  background-color: #0d47a1;
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
"""
        },
        "package_updates": {
            "dependencies": {
                "@angular/animations": "^17.0.0",
                "@angular/common": "^17.0.0",
                "@angular/compiler": "^17.0.0",
                "@angular/core": "^17.0.0",
                "@angular/forms": "^17.0.0",
                "@angular/platform-browser": "^17.0.0",
                "@angular/platform-browser-dynamic": "^17.0.0",
                "rxjs": "~7.8.0",
                "tslib": "^2.3.0",
                "zone.js": "~0.14.2"
            },
            "devDependencies": {
                "@angular-devkit/build-angular": "^17.0.0",
                "@angular/cli": "^17.0.0",
                "@angular/compiler-cli": "^17.0.0",
                "typescript": "~5.2.2"
            },
            "scripts": {
                "ng": "ng",
                "start": "ng serve",
                "build": "ng build",
                "watch": "ng build --watch --configuration development",
                "test": "ng test"
            }
        }
    }
}

def improve_template(template_name, config):
    """템플릿 개선"""
    template_path = Path(template_name)

    if not template_path.exists():
        print(f"  ⚠️  {template_name} not found, skipping...")
        return False

    # 파일 생성
    if "files" in config:
        for file_path, content in config["files"].items():
            full_path = template_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

    # package.json 업데이트
    if "package_updates" in config:
        package_json_path = template_path / "package.json"

        if package_json_path.exists():
            with open(package_json_path, "r", encoding="utf-8") as f:
                package_data = json.load(f)

            # 업데이트
            if "dependencies" in config["package_updates"]:
                package_data["dependencies"] = config["package_updates"]["dependencies"]

            if "devDependencies" in config["package_updates"]:
                package_data["devDependencies"] = config["package_updates"]["devDependencies"]

            if "scripts" in config["package_updates"]:
                package_data["scripts"] = config["package_updates"]["scripts"]

            with open(package_json_path, "w", encoding="utf-8") as f:
                json.dump(package_data, f, indent=2, ensure_ascii=False)

    return True

def main():
    """메인 함수"""
    print("🔧 프론트엔드 템플릿 개선 시작...\n")

    improved = 0
    failed = 0

    for template_name, config in templates_to_improve.items():
        print(f"📝 {template_name} 개선 중...")
        if improve_template(template_name, config):
            improved += 1
            print(f"  ✅ 완료")
        else:
            failed += 1

    print(f"\n✅ 개선 완료!")
    print(f"  - 성공: {improved}개")
    print(f"  - 실패: {failed}개")

if __name__ == "__main__":
    main()
