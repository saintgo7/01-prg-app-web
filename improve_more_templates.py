#!/usr/bin/env python3
"""
추가 템플릿 개선 스크립트
더 많은 주요 프레임워크를 실전 사용 가능하도록 개선
"""

import os
import json

additional_configs = {
    "vue": {
        "name": "003_web_vue",
        "package": {
            "name": "vue-app",
            "version": "0.1.0",
            "private": True,
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview"
            },
            "dependencies": {
                "vue": "^3.3.11"
            },
            "devDependencies": {
                "@vitejs/plugin-vue": "^4.5.2",
                "vite": "^5.0.8"
            }
        },
        "files": {
            "index.html": '''<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/svg+xml" href="/vite.svg">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
''',
            "vite.config.js": '''import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
})
''',
            "src/main.js": '''import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

createApp(App).mount('#app')
''',
            "src/App.vue": '''<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <p>{{ description }}</p>
    <button @click="count++">Count: {{ count }}</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('Welcome to Vue 3!')
const description = ref('Edit src/App.vue to get started')
const count = ref(0)
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
''',
            "src/style.css": ''':root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}
''',
            ".gitignore": '''node_modules
dist
.DS_Store
*.local
'''
        }
    },

    "angular": {
        "name": "004_web_angular",
        "package": {
            "name": "angular-app",
            "version": "0.0.0",
            "scripts": {
                "ng": "ng",
                "start": "ng serve",
                "build": "ng build",
                "watch": "ng build --watch --configuration development",
                "test": "ng test"
            },
            "private": True,
            "dependencies": {
                "@angular/animations": "^17.0.0",
                "@angular/common": "^17.0.0",
                "@angular/compiler": "^17.0.0",
                "@angular/core": "^17.0.0",
                "@angular/forms": "^17.0.0",
                "@angular/platform-browser": "^17.0.0",
                "@angular/platform-browser-dynamic": "^17.0.0",
                "@angular/router": "^17.0.0",
                "rxjs": "~7.8.0",
                "tslib": "^2.3.0",
                "zone.js": "~0.14.2"
            },
            "devDependencies": {
                "@angular-devkit/build-angular": "^17.0.0",
                "@angular/cli": "^17.0.0",
                "@angular/compiler-cli": "^17.0.0",
                "typescript": "~5.2.2"
            }
        },
        "files": {
            "angular.json": '''{
  "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
  "version": 1,
  "newProjectRoot": "projects",
  "projects": {
    "angular-app": {
      "projectType": "application",
      "schematics": {},
      "root": "",
      "sourceRoot": "src",
      "prefix": "app",
      "architect": {
        "build": {
          "builder": "@angular-devkit/build-angular:browser",
          "options": {
            "outputPath": "dist/angular-app",
            "index": "src/index.html",
            "main": "src/main.ts",
            "polyfills": ["zone.js"],
            "tsConfig": "tsconfig.app.json",
            "assets": ["src/favicon.ico", "src/assets"],
            "styles": ["src/styles.css"],
            "scripts": []
          }
        },
        "serve": {
          "builder": "@angular-devkit/build-angular:dev-server",
          "options": {},
          "configurations": {
            "development": {
              "buildTarget": "angular-app:build:development"
            }
          },
          "defaultConfiguration": "development"
        }
      }
    }
  }
}
''',
            "tsconfig.json": '''{
  "compileOnSave": false,
  "compilerOptions": {
    "outDir": "./dist/out-tsc",
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "esModuleInterop": true,
    "sourceMap": true,
    "declaration": false,
    "experimentalDecorators": true,
    "moduleResolution": "node",
    "importHelpers": true,
    "target": "ES2022",
    "module": "ES2022",
    "useDefineForClassFields": false,
    "lib": ["ES2022", "dom"]
  },
  "angularCompilerOptions": {
    "enableI18nLegacyMessageIdFormat": false,
    "strictInjectionParameters": true,
    "strictInputAccessModifiers": true,
    "strictTemplates": true
  }
}
''',
            "src/index.html": '''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <title>Angular App</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <app-root></app-root>
</body>
</html>
''',
            "src/main.ts": '''import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
''',
            "src/app/app.module.ts": '''import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
''',
            "src/app/app.component.ts": '''import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div class="app">
      <h1>Welcome to Angular!</h1>
      <p>Edit src/app/app.component.ts to get started</p>
    </div>
  `,
  styles: [`
    .app {
      text-align: center;
      padding: 40px;
      font-family: Arial, sans-serif;
    }
    h1 { color: #dd0031; }
  `]
})
export class AppComponent {
  title = 'angular-app';
}
''',
            "src/styles.css": '''/* Global Styles */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
''',
            ".gitignore": '''/node_modules
/dist
/tmp
/out-tsc
.DS_Store
'''
        }
    },

    "flutter": {
        "name": "222_app_flutter",
        "files": {
            "pubspec.yaml": '''name: flutter_app
description: A new Flutter project.
publish_to: 'none'
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0

flutter:
  uses-material-design: true
''',
            "lib/main.dart": '''import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text('You have pushed the button this many times:'),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
''',
            ".gitignore": '''# Miscellaneous
*.class
*.log
*.pyc
*.swp
.DS_Store

# IntelliJ related
*.iml
*.ipr
*.iws
.idea/

# Flutter/Dart/Pub related
**/doc/api/
.dart_tool/
.flutter-plugins
.flutter-plugins-dependencies
.packages
.pub-cache/
.pub/
build/

# Android related
**/android/**/gradle-wrapper.jar
**/android/.gradle
**/android/captures/
**/android/gradlew
**/android/gradlew.bat
**/android/local.properties
**/android/**/GeneratedPluginRegistrant.java

# iOS/XCode related
**/ios/**/*.mode1v3
**/ios/**/*.mode2v3
**/ios/**/*.moved-aside
**/ios/**/*.pbxuser
**/ios/**/*.perspectivev3
**/ios/**/*sync/
**/ios/**/.sconsign.dblite
**/ios/**/.tags*
**/ios/**/.vagrant/
**/ios/**/DerivedData/
**/ios/**/Icon?
**/ios/**/Pods/
**/ios/**/.symlinks/
**/ios/**/profile
**/ios/**/xcuserdata
**/ios/.generated/
**/ios/Flutter/App.framework
**/ios/Flutter/Flutter.framework
**/ios/Flutter/Flutter.podspec
**/ios/Flutter/Generated.xcconfig
**/ios/Flutter/ephemeral
**/ios/Flutter/app.flx
**/ios/Flutter/app.zip
**/ios/Flutter/flutter_assets/
**/ios/Flutter/flutter_export_environment.sh
**/ios/ServiceDefinitions.json
**/ios/Runner/GeneratedPluginRegistrant.*
'''
        }
    },

    "fastapi": {
        "name": "448_backend_fastapi_backend",
        "files": {
            "main.py": '''from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title="FastAPI Application",
    description="FastAPI REST API Server",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic 모델
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# 루트 엔드포인트
@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# Health check
@app.get("/health")
async def health():
    return {"status": "OK"}

# CRUD 예제
items_db = {}

@app.post("/items/")
async def create_item(item: Item):
    item_id = len(items_db) + 1
    items_db[item_id] = item
    return {"id": item_id, **item.dict()}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
''',
            "requirements.txt": '''fastapi==0.108.0
uvicorn[standard]==0.25.0
pydantic==2.5.3
python-dotenv==1.0.0
''',
            ".env.example": '''APP_NAME=FastAPI Application
DEBUG=True
HOST=0.0.0.0
PORT=8000
''',
            ".gitignore": '''__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/
.env
.venv
*.log
.DS_Store
'''
        }
    }
}

def improve_template(config):
    """템플릿 개선"""
    template_dir = config["name"]

    if not os.path.exists(template_dir):
        print(f"❌ {template_dir} not found")
        return

    print(f"\n🔧 Improving {template_dir}...")

    # 기존 파일 제거
    for old_file in ["index.html", "index.js"]:
        old_path = os.path.join(template_dir, old_file)
        if os.path.exists(old_path):
            os.remove(old_path)

    # package.json 업데이트
    if "package" in config:
        package_path = os.path.join(template_dir, "package.json")
        with open(package_path, 'w', encoding='utf-8') as f:
            json.dump(config["package"], f, indent=2, ensure_ascii=False)
        print(f"  ✓ Updated package.json")

    # 파일 생성
    if "files" in config:
        for file_path, content in config["files"].items():
            full_path = os.path.join(template_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Created {file_path}")

    # README 업데이트
    framework_name = template_dir.split("_")[-1].replace("-", " ").title()
    readme_content = f'''# {framework_name} Project

## 🚀 Quick Start

```bash
# Install dependencies
npm install  # or: pip install -r requirements.txt / flutter pub get

# Run development server
npm run dev  # or: python main.py / flutter run
```

## 📦 What's Included

- Production-ready configuration
- Real dependencies
- Working example code
- Best practices setup

## 🛠️ Commands

```bash
npm run dev      # Start development
npm run build    # Build for production
npm start        # Start production server
```

## 📖 Documentation

Check the official documentation for more details.

---
**Ready to use!** ✨
'''

    readme_path = os.path.join(template_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"  ✓ Updated README.md")

    print(f"✅ {template_dir} improved!")

def main():
    print("=" * 70)
    print("🔥 추가 템플릿 개선 시작")
    print("=" * 70)

    for framework, config in additional_configs.items():
        improve_template(config)

    print("\n" + "=" * 70)
    print("✅ 추가 템플릿 개선 완료!")
    print("=" * 70)

    print("\n📋 개선된 템플릿:")
    for framework in additional_configs.keys():
        print(f"  ✓ {framework}")

if __name__ == "__main__":
    main()
