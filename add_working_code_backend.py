#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
백엔드 주요 템플릿에 실제 동작하는 코드 추가
Express, Django, Flask
"""

import os
import json
from pathlib import Path

templates_to_improve = {
    "031_web_express": {
        "files": {
            "src/server.js": """const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(helmet());
app.use(cors());
app.use(morgan('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// In-memory database (for demo purposes)
let todos = [];
let todoId = 1;

// Routes
app.get('/', (req, res) => {
  res.json({
    message: 'Welcome to Express API',
    version: '1.0.0',
    endpoints: {
      todos: '/api/todos',
      health: '/health'
    }
  });
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// Get all todos
app.get('/api/todos', (req, res) => {
  res.json({ todos, count: todos.length });
});

// Get single todo
app.get('/api/todos/:id', (req, res) => {
  const todo = todos.find(t => t.id === parseInt(req.params.id));
  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  res.json(todo);
});

// Create todo
app.post('/api/todos', (req, res) => {
  const { title, description } = req.body;

  if (!title) {
    return res.status(400).json({ error: 'Title is required' });
  }

  const newTodo = {
    id: todoId++,
    title,
    description: description || '',
    completed: false,
    createdAt: new Date().toISOString()
  };

  todos.push(newTodo);
  res.status(201).json(newTodo);
});

// Update todo
app.put('/api/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const todoIndex = todos.findIndex(t => t.id === id);

  if (todoIndex === -1) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  const { title, description, completed } = req.body;
  const updatedTodo = {
    ...todos[todoIndex],
    title: title !== undefined ? title : todos[todoIndex].title,
    description: description !== undefined ? description : todos[todoIndex].description,
    completed: completed !== undefined ? completed : todos[todoIndex].completed,
    updatedAt: new Date().toISOString()
  };

  todos[todoIndex] = updatedTodo;
  res.json(updatedTodo);
});

// Delete todo
app.delete('/api/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const todoIndex = todos.findIndex(t => t.id === id);

  if (todoIndex === -1) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  const deletedTodo = todos.splice(todoIndex, 1)[0];
  res.json({ message: 'Todo deleted', todo: deletedTodo });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Internal Server Error',
    message: process.env.NODE_ENV === 'development' ? err.message : undefined
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Express server running on http://localhost:${PORT}`);
  console.log(`📝 Environment: ${process.env.NODE_ENV || 'development'}`);
});

module.exports = app;
""",
            ".env.example": """# Server Configuration
NODE_ENV=development
PORT=3000

# Database (if needed)
DATABASE_URL=

# API Keys (if needed)
API_KEY=

# CORS
CORS_ORIGIN=http://localhost:3000
"""
        },
        "package_updates": {
            "dependencies": {
                "express": "^4.18.2",
                "cors": "^2.8.5",
                "helmet": "^7.1.0",
                "morgan": "^1.10.0",
                "dotenv": "^16.3.1"
            },
            "devDependencies": {
                "nodemon": "^3.0.2"
            },
            "scripts": {
                "start": "node src/server.js",
                "dev": "nodemon src/server.js",
                "test": "echo 'Run tests'"
            }
        }
    },
    "051_web_django": {
        "files": {
            "manage.py": """#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)
""",
            "config/settings.py": """import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-production')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# CORS
CORS_ALLOW_ALL_ORIGINS = DEBUG
""",
            "config/urls.py": """from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
""",
            "config/__init__.py": "",
            "config/wsgi.py": """import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()
""",
            "api/models.py": """from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
""",
            "api/serializers.py": """from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
""",
            "api/views.py": """from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Welcome to Django REST API',
        'version': '1.0.0',
        'endpoints': {
            'todos': '/api/todos/',
            'admin': '/admin/'
        }
    })

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
""",
            "api/urls.py": """from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', views.api_root),
    path('', include(router.urls)),
]
""",
            "api/__init__.py": "",
            "api/admin.py": """from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created_at']
    list_filter = ['completed', 'created_at']
    search_fields = ['title', 'description']
""",
            "api/apps.py": """from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
""",
            "requirements.txt": """Django>=5.0,<5.1
djangorestframework>=3.14.0
django-cors-headers>=4.3.0
python-dotenv>=1.0.0
""",
            ".env.example": """# Django Configuration
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3
"""
        },
        "package_updates": {
            "scripts": {
                "start": "python manage.py runserver",
                "migrate": "python manage.py migrate",
                "makemigrations": "python manage.py makemigrations",
                "createsuperuser": "python manage.py createsuperuser",
                "test": "python manage.py test"
            }
        }
    },
    "052_web_flask": {
        "files": {
            "app.py": """from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///todos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

CORS(app)
db = SQLAlchemy(app)

# Models
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to Flask API',
        'version': '1.0.0',
        'endpoints': {
            'todos': '/api/todos',
            'health': '/health'
        }
    })

@app.route('/health')
def health():
    return jsonify({'status': 'OK', 'timestamp': datetime.utcnow().isoformat()})

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return jsonify({
        'todos': [todo.to_dict() for todo in todos],
        'count': len(todos)
    })

@app.route('/api/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify(todo.to_dict())

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    todo = Todo(
        title=data['title'],
        description=data.get('description', '')
    )
    db.session.add(todo)
    db.session.commit()

    return jsonify(todo.to_dict()), 201

@app.route('/api/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.get_json()

    if 'title' in data:
        todo.title = data['title']
    if 'description' in data:
        todo.description = data['description']
    if 'completed' in data:
        todo.completed = data['completed']

    db.session.commit()
    return jsonify(todo.to_dict())

@app.route('/api/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted', 'id': id})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True') == 'True'
    app.run(host='0.0.0.0', port=port, debug=debug)
""",
            "requirements.txt": """Flask>=3.0.0
Flask-CORS>=4.0.0
Flask-SQLAlchemy>=3.1.0
python-dotenv>=1.0.0
""",
            ".env.example": """# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=dev-secret-key-change-in-production
DEBUG=True

# Server
PORT=5000

# Database
DATABASE_URL=sqlite:///todos.db
"""
        },
        "package_updates": {
            "scripts": {
                "start": "python app.py",
                "dev": "flask run --debug",
                "test": "python -m pytest"
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
            if "scripts" in config["package_updates"]:
                package_data["scripts"] = config["package_updates"]["scripts"]

            if "dependencies" in config["package_updates"]:
                package_data["dependencies"] = config["package_updates"]["dependencies"]

            if "devDependencies" in config["package_updates"]:
                package_data["devDependencies"] = config["package_updates"]["devDependencies"]

            with open(package_json_path, "w", encoding="utf-8") as f:
                json.dump(package_data, f, indent=2, ensure_ascii=False)

    return True

def main():
    """메인 함수"""
    print("🔧 백엔드 템플릿 개선 시작...\n")

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
