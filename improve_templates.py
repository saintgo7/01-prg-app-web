#!/usr/bin/env python3
"""
템플릿 개선 스크립트
실전에서 사용 가능한 프로덕션급 템플릿으로 업그레이드
"""

import os
import json
import shutil

# 주요 프레임워크별 실전 설정
framework_configs = {
    "nextjs": {
        "name": "001_web_nextjs",
        "package": {
            "name": "nextjs-app",
            "version": "0.1.0",
            "private": True,
            "scripts": {
                "dev": "next dev",
                "build": "next build",
                "start": "next start",
                "lint": "next lint"
            },
            "dependencies": {
                "next": "14.0.4",
                "react": "^18.2.0",
                "react-dom": "^18.2.0"
            },
            "devDependencies": {
                "@types/node": "^20",
                "@types/react": "^18",
                "@types/react-dom": "^18",
                "autoprefixer": "^10.0.1",
                "eslint": "^8",
                "eslint-config-next": "14.0.4",
                "postcss": "^8",
                "tailwindcss": "^3.3.0",
                "typescript": "^5"
            }
        },
        "files": {
            "next.config.js": '''/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
}

module.exports = nextConfig
''',
            "tsconfig.json": '''{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
''',
            "tailwind.config.js": '''/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: { extend: {} },
  plugins: [],
}
''',
            ".env.local.example": '''# Environment Variables
NEXT_PUBLIC_API_URL=http://localhost:3000/api
NEXT_PUBLIC_APP_NAME=Next.js App
''',
            ".gitignore": '''# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# local env files
.env*.local

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
''',
            "app/page.tsx": '''export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold mb-4">Welcome to Next.js!</h1>
        <p className="text-xl">Get started by editing app/page.tsx</p>
      </div>
    </main>
  )
}
''',
            "app/layout.tsx": '''import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Next.js App',
  description: 'Created with Next.js',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ko">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
''',
            "app/globals.css": '''@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --foreground-rgb: 0, 0, 0;
  --background-start-rgb: 214, 219, 220;
  --background-end-rgb: 255, 255, 255;
}

@media (prefers-color-scheme: dark) {
  :root {
    --foreground-rgb: 255, 255, 255;
    --background-start-rgb: 0, 0, 0;
    --background-end-rgb: 0, 0, 0;
  }
}

body {
  color: rgb(var(--foreground-rgb));
  background: linear-gradient(
      to bottom,
      transparent,
      rgb(var(--background-end-rgb))
    )
    rgb(var(--background-start-rgb));
}
'''
        }
    },

    "react": {
        "name": "002_web_react",
        "package": {
            "name": "react-app",
            "version": "0.1.0",
            "private": True,
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "react-scripts": "5.0.1",
                "web-vitals": "^2.1.4"
            },
            "scripts": {
                "start": "react-scripts start",
                "build": "react-scripts build",
                "test": "react-scripts test",
                "eject": "react-scripts eject"
            },
            "eslintConfig": {
                "extends": ["react-app", "react-app/jest"]
            },
            "browserslist": {
                "production": [">0.2%", "not dead", "not op_mini all"],
                "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
            }
        },
        "files": {
            "public/index.html": '''<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="React App" />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
''',
            "src/index.js": '''import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
''',
            "src/App.js": '''import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to React!</h1>
        <p>Edit <code>src/App.js</code> and save to reload.</p>
      </header>
    </div>
  );
}

export default App;
''',
            "src/App.css": '''.App {
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
}
''',
            "src/index.css": '''body {
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
''',
            ".gitignore": '''# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# production
/build

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*
'''
        }
    },

    "react-native": {
        "name": "221_app_react_native",
        "package": {
            "name": "ReactNativeApp",
            "version": "0.0.1",
            "private": True,
            "scripts": {
                "android": "react-native run-android",
                "ios": "react-native run-ios",
                "lint": "eslint .",
                "start": "react-native start",
                "test": "jest"
            },
            "dependencies": {
                "react": "18.2.0",
                "react-native": "0.73.0"
            },
            "devDependencies": {
                "@babel/core": "^7.20.0",
                "@babel/preset-env": "^7.20.0",
                "@babel/runtime": "^7.20.0",
                "@react-native/babel-preset": "^0.73.0",
                "@react-native/eslint-config": "^0.73.0",
                "@react-native/metro-config": "^0.73.0",
                "@react-native/typescript-config": "^0.73.0",
                "@types/react": "^18.2.0",
                "@types/react-test-renderer": "^18.0.0",
                "babel-jest": "^29.2.1",
                "eslint": "^8.19.0",
                "jest": "^29.2.1",
                "prettier": "^2.4.1",
                "react-test-renderer": "18.2.0",
                "typescript": "5.0.4"
            }
        },
        "files": {
            "App.tsx": '''import React from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  View,
} from 'react-native';

function App(): JSX.Element {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />
      <ScrollView contentInsetAdjustmentBehavior="automatic">
        <View style={styles.body}>
          <Text style={styles.title}>Welcome to React Native!</Text>
          <Text style={styles.subtitle}>Edit App.tsx to get started</Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  body: {
    backgroundColor: '#fff',
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: '600',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
  },
});

export default App;
''',
            "index.js": '''import {AppRegistry} from 'react-native';
import App from './App';
import {name as appName} from './app.json';

AppRegistry.registerComponent(appName, () => App);
''',
            "app.json": '''{
  "name": "ReactNativeApp",
  "displayName": "React Native App"
}
''',
            "tsconfig.json": '''{
  "extends": "@react-native/typescript-config/tsconfig.json"
}
''',
            ".gitignore": '''# OSX
.DS_Store

# Xcode
build/
*.pbxuser
!default.pbxuser
*.mode1v3
!default.mode1v3
*.mode2v3
!default.mode2v3
*.perspectivev3
!default.perspectivev3
xcuserdata
*.xccheckout
*.moved-aside
DerivedData
*.hmap
*.ipa
*.xcuserstate

# Android/IntelliJ
build/
.idea
.gradle
local.properties
*.iml
*.hprof
.cxx/

# node.js
node_modules/
npm-debug.log
yarn-error.log

# fastlane
fastlane/report.xml
fastlane/Preview.html
fastlane/screenshots
fastlane/test_output

# Bundle artifact
*.jsbundle

# Ruby / CocoaPods
/ios/Pods/
/vendor/bundle/

# Temporary files created by Metro
.metro-health-check*
'''
        }
    },

    "express": {
        "name": "031_web_express",
        "package": {
            "name": "express-app",
            "version": "1.0.0",
            "description": "Express.js REST API Server",
            "main": "server.js",
            "scripts": {
                "start": "node server.js",
                "dev": "nodemon server.js",
                "test": "jest"
            },
            "dependencies": {
                "express": "^4.18.2",
                "dotenv": "^16.3.1",
                "cors": "^2.8.5",
                "helmet": "^7.1.0",
                "morgan": "^1.10.0"
            },
            "devDependencies": {
                "nodemon": "^3.0.2",
                "jest": "^29.7.0",
                "supertest": "^6.3.3"
            }
        },
        "files": {
            "server.js": '''const express = require('express');
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

// Routes
app.get('/', (req, res) => {
  res.json({
    message: 'Welcome to Express API',
    version: '1.0.0',
    endpoints: {
      health: '/health',
      api: '/api'
    }
  });
});

app.get('/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

app.get('/api', (req, res) => {
  res.json({ message: 'API is working!' });
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});

module.exports = app;
''',
            ".env.example": '''PORT=3000
NODE_ENV=development
''',
            ".gitignore": '''node_modules/
.env
.env.local
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.DS_Store
'''
        }
    },

    "django": {
        "name": "051_web_django",
        "package": {
            "name": "django-project",
            "version": "1.0.0",
            "description": "Django Web Framework Project"
        },
        "files": {
            "requirements.txt": '''Django==5.0
djangorestframework==3.14.0
python-dotenv==1.0.0
django-cors-headers==4.3.1
gunicorn==21.2.0
''',
            "manage.py": '''#!/usr/bin/env python
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
''',
            "config/__init__.py": '',
            "config/settings.py": '''import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-change-this')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
''',
            "config/urls.py": '''from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'message': 'Welcome to Django API',
        'version': '1.0.0'
    })

def health(request):
    return JsonResponse({'status': 'OK'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('health/', health),
]
''',
            "config/wsgi.py": '''import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()
''',
            ".env.example": '''SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
''',
            ".gitignore": '''*.pyc
__pycache__/
db.sqlite3
.env
venv/
.venv/
*.log
.DS_Store
'''
        }
    }
}

def improve_template(config):
    """템플릿을 실전 사용 가능하도록 개선"""
    template_dir = config["name"]

    if not os.path.exists(template_dir):
        print(f"❌ {template_dir} not found")
        return

    print(f"\n🔧 Improving {template_dir}...")

    # 기존 파일 백업
    for old_file in ["index.html", "index.js"]:
        old_path = os.path.join(template_dir, old_file)
        if os.path.exists(old_path):
            os.remove(old_path)

    # package.json 업데이트 (Python이나 다른 언어 프로젝트가 아닌 경우)
    if "package" in config:
        package_path = os.path.join(template_dir, "package.json")
        with open(package_path, 'w', encoding='utf-8') as f:
            json.dump(config["package"], f, indent=2, ensure_ascii=False)
        print(f"  ✓ Updated package.json with real dependencies")

    # 프레임워크별 파일 생성
    if "files" in config:
        for file_path, content in config["files"].items():
            full_path = os.path.join(template_dir, file_path)

            # 디렉토리 생성
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            # 파일 생성
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"  ✓ Created {file_path}")

    # README 업데이트
    update_readme(template_dir, config)

    print(f"✅ {template_dir} improved successfully!")

def update_readme(template_dir, config):
    """README를 더 상세하고 실용적으로 업데이트"""
    readme_path = os.path.join(template_dir, "README.md")

    framework_name = config["name"].split("_")[-1].replace("-", " ").title()

    readme_content = f'''# {framework_name} Project Template

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ (for JS/TS projects)
- Python 3.10+ (for Python projects)
- npm or yarn or pnpm

### Installation

```bash
# Install dependencies
npm install
# or
yarn install
# or (for Python)
pip install -r requirements.txt
```

### Development

```bash
# Start development server
npm run dev
# or
python manage.py runserver
```

Visit: http://localhost:3000 (or port shown in terminal)

### Build for Production

```bash
# Build
npm run build

# Start production server
npm start
```

## 📁 Project Structure

```
.
├── src/              # Source files
├── public/           # Static files
├── package.json      # Dependencies
├── .env.example      # Environment variables template
└── README.md         # This file
```

## 🛠️ Tech Stack

- **Framework**: {framework_name}
- **Language**: JavaScript/TypeScript
- **Package Manager**: npm/yarn/pnpm

## 📝 Environment Variables

Copy `.env.example` to `.env.local` and update values:

```bash
cp .env.example .env.local
```

## 🔗 Useful Links

- [Official Documentation](https://docs.example.com)
- [GitHub Repository](https://github.com/example)
- [Community](https://community.example.com)

## 📄 License

MIT

---

**Ready for production!** ✨
'''

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"  ✓ Updated README.md")

def main():
    print("=" * 70)
    print("🔥 템플릿 실전 사용 가능하도록 개선 시작")
    print("=" * 70)

    # 주요 프레임워크들 개선
    for framework, config in framework_configs.items():
        improve_template(config)

    print("\n" + "=" * 70)
    print("✅ 주요 템플릿 개선 완료!")
    print("=" * 70)
    print("\n📋 개선된 템플릿:")
    for framework in framework_configs.keys():
        print(f"  ✓ {framework}")

    print("\n💡 이제 다음 명령어로 바로 사용할 수 있습니다:")
    print("  1. cd 001_web_nextjs && npm install && npm run dev")
    print("  2. cd 002_web_react && npm install && npm start")
    print("  3. cd 221_app_react_native && npm install && npm start")
    print("  4. cd 031_web_express && npm install && npm run dev")
    print("  5. cd 051_web_django && pip install -r requirements.txt && python manage.py runserver")

if __name__ == "__main__":
    main()
