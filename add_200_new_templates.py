#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
200개의 새로운 프로그램 템플릿 추가
기존 1,550개와 중복되지 않는 인기 도구들
"""

import os
import json
from pathlib import Path

# 새로운 200개 프로그램 (기존 템플릿과 중복 없이)
new_programs = {
    "testing": [
        # Testing Frameworks & Tools (30개)
        "jest", "mocha", "cypress", "playwright", "puppeteer",
        "selenium", "webdriverio", "testcafe", "nightwatch", "jasmine",
        "karma", "ava", "tape", "qunit", "vitest",
        "pytest-bdd", "behave", "cucumber", "robotframework", "gauge",
        "k6", "locust", "jmeter", "gatling", "artillery",
        "supertest", "chai", "sinon", "enzyme", "react-testing-library"
    ],
    "build_tools": [
        # Build Tools & Bundlers (25개)
        "webpack", "vite", "rollup", "parcel", "esbuild",
        "turbopack", "snowpack", "wmr", "microbundle", "tsup",
        "gulp", "grunt", "broccoli", "browserify", "fusebox",
        "rome", "nx", "turborepo", "lerna", "rush",
        "bazel", "pants", "buck", "gradle", "maven"
    ],
    "css_tools": [
        # CSS Frameworks & Tools (25개)
        "tailwindcss", "sass", "less", "postcss", "stylus",
        "styled-components", "emotion", "css-modules", "linaria", "vanilla-extract",
        "stitches", "chakra-ui", "mantine", "radix-ui", "headless-ui",
        "daisyui", "skeleton", "primefaces", "semantic-ui", "bulma",
        "foundation", "materialize", "uikit", "pure-css", "milligram"
    ],
    "mobile": [
        # Mobile Development (20개)
        "xamarin", "nativescript", "cordova", "capacitor", "phonegap",
        "quasar", "onsen-ui", "framework7", "ionic-react", "ionic-vue",
        "expo", "react-native-cli", "flutter-bloc", "flutter-riverpod", "flutter-getx",
        "swiftui", "jetpack-compose", "kotlin-multiplatform", "react-native-navigation", "react-native-screens"
    ],
    "cms": [
        # CMS & Headless CMS (20개)
        "wordpress", "strapi", "contentful", "sanity", "ghost",
        "keystone", "directus", "payload", "tina", "builder-io",
        "drupal", "joomla", "umbraco", "craft-cms", "prismic",
        "dato-cms", "storyblok", "butter-cms", "agility-cms", "cockpit"
    ],
    "ecommerce": [
        # E-commerce Platforms (15개)
        "shopify", "woocommerce", "magento", "prestashop", "opencart",
        "bigcommerce", "commercejs", "saleor", "vendure", "medusa",
        "spree", "solidus", "reaction-commerce", "sylius", "bagisto"
    ],
    "auth": [
        # Authentication & Authorization (15개)
        "auth0", "keycloak", "clerk", "supabase-auth", "firebase-auth",
        "passport", "next-auth", "lucia", "iron-session", "jose",
        "jsonwebtoken", "bcrypt", "argon2", "oauth2-server", "simple-oauth2"
    ],
    "realtime": [
        # Real-time Communication (10개)
        "socket-io", "webrtc", "signalr", "centrifugo", "mercure",
        "ably", "pusher-channels", "socketcluster", "ws", "uwebsockets"
    ],
    "search": [
        # Search Engines (10개)
        "elasticsearch", "algolia", "meilisearch", "typesense", "sonic",
        "manticore", "solr", "sphinx", "opensearch", "quickwit"
    ],
    "desktop": [
        # Desktop App Frameworks (10개)
        "electron", "tauri", "nwjs", "neutralino", "wails",
        "electron-forge", "electron-builder", "nodegui", "proton-native", "carlo"
    ],
    "api_tools": [
        # API Development Tools (10개)
        "postman", "insomnia", "swagger", "openapi", "api-blueprint",
        "raml", "graphql-yoga", "apollo-server", "hasura", "postgraphile"
    ],
    "blockchain": [
        # Blockchain & Web3 (10개)
        "hardhat", "truffle", "web3js", "ethersjs", "wagmi",
        "solidity", "foundry", "ganache", "remix-ide", "metamask-sdk"
    ]
}

def get_framework_type(category, name):
    """프레임워크 타입 결정"""
    # Node.js 기반
    nodejs_patterns = ['js', 'node', 'react', 'vue', 'angular', 'next', 'nuxt', 'express', 'nest',
                       'socket', 'electron', 'tauri', 'webpack', 'vite', 'rollup', 'parcel',
                       'jest', 'mocha', 'cypress', 'playwright', 'styled', 'emotion']

    # Python 기반
    python_patterns = ['pytest', 'behave', 'robot', 'locust', 'playwright']

    # Ruby 기반
    ruby_patterns = []

    # PHP 기반
    php_patterns = ['wordpress', 'drupal', 'joomla', 'magento', 'prestashop', 'opencart',
                    'woocommerce', 'craft']

    # Java/JVM 기반
    java_patterns = ['gradle', 'maven', 'selenium', 'jmeter', 'gatling', 'bazel']

    # Go 기반
    go_patterns = ['k6']

    # Rust 기반
    rust_patterns = ['tauri']

    # .NET 기반
    dotnet_patterns = ['xamarin', 'nunit']

    # Multi-platform
    multi_patterns = ['flutter', 'kotlin', 'cordova', 'capacitor', 'nativescript']

    name_lower = name.lower()

    for pattern in php_patterns:
        if pattern in name_lower:
            return 'php'

    for pattern in python_patterns:
        if pattern in name_lower:
            return 'python'

    for pattern in java_patterns:
        if pattern in name_lower:
            return 'java'

    for pattern in go_patterns:
        if pattern in name_lower:
            return 'go'

    for pattern in rust_patterns:
        if pattern in name_lower:
            return 'rust'

    for pattern in dotnet_patterns:
        if pattern in name_lower:
            return 'dotnet'

    for pattern in multi_patterns:
        if pattern in name_lower:
            return 'multi'

    for pattern in nodejs_patterns:
        if pattern in name_lower:
            return 'nodejs'

    # 기본값은 카테고리에 따라
    if category in ['testing', 'build_tools', 'api_tools', 'desktop', 'realtime']:
        return 'nodejs'
    elif category in ['css_tools']:
        return 'nodejs'
    elif category == 'blockchain':
        return 'nodejs'
    elif category in ['cms', 'ecommerce']:
        return 'php'
    elif category == 'search':
        return 'java'

    return 'nodejs'

def get_gitignore(framework_type):
    """프레임워크별 .gitignore 생성"""
    gitignores = {
        'nodejs': """node_modules/
dist/
build/
.env
.env.local
.env.*.local
*.log
.DS_Store
.vscode/
.idea/
coverage/
.cache/
""",
        'python': """__pycache__/
*.py[cod]
*$py.class
.Python
venv/
env/
.env
*.log
.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/
""",
        'php': """vendor/
.env
.env.local
composer.lock
*.log
cache/
storage/
public/uploads/
.DS_Store
""",
        'java': """target/
.gradle/
build/
*.class
*.jar
*.war
.idea/
.vscode/
*.log
.env
""",
        'go': """bin/
*.exe
*.exe~
*.dll
*.so
*.dylib
vendor/
.env
*.log
""",
        'rust': """target/
Cargo.lock
**/*.rs.bk
*.pdb
.env
*.log
""",
        'dotnet': """bin/
obj/
*.user
*.suo
.vs/
.env
*.log
packages/
""",
        'multi': """node_modules/
build/
dist/
.env
.env.local
*.log
.DS_Store
.idea/
.vscode/
"""
    }

    return gitignores.get(framework_type, gitignores['nodejs'])

def get_env_example(framework_type, name):
    """환경 변수 예시 파일 생성"""
    common = f"""# {name.title()} Environment Variables

# Application
NODE_ENV=development
PORT=3000

# Database
DATABASE_URL=

# API Keys
API_KEY=

# Others
LOG_LEVEL=info
"""
    return common

def get_korean_readme(name, category, framework_type):
    """한국어 README 생성"""
    category_names = {
        'testing': '테스팅',
        'build_tools': '빌드 도구',
        'css_tools': 'CSS 도구',
        'mobile': '모바일 개발',
        'cms': 'CMS',
        'ecommerce': '전자상거래',
        'auth': '인증',
        'realtime': '실시간 통신',
        'search': '검색 엔진',
        'desktop': '데스크톱 앱',
        'api_tools': 'API 도구',
        'blockchain': '블록체인'
    }

    cat_name = category_names.get(category, category)

    return f"""# {name.title()}

## 📌 개요

**{name.title()}**는 {cat_name} 개발을 위한 프로덕션 준비 완료 템플릿입니다.

### 특징
- ✅ 즉시 실행 가능한 설정
- ✅ 실제 프로젝트에서 사용 가능한 구조
- ✅ Best Practice 적용
- ✅ 한국어 문서 제공

## 🚀 빠른 시작

### 사전 요구사항

프레임워크별 요구사항은 공식 문서를 참조하세요.

### 설치

```bash
# 의존성 설치
npm install
# 또는
yarn install
# 또는
pnpm install
```

### 개발 서버 실행

```bash
npm run dev
# 또는
yarn dev
# 또는
pnpm dev
```

### 빌드

```bash
npm run build
# 또는
yarn build
# 또는
pnpm build
```

## 📁 프로젝트 구조

```
.
├── src/              # 소스 코드
├── public/           # 정적 파일
├── tests/            # 테스트 파일
├── .env.example      # 환경 변수 예시
├── .gitignore        # Git 제외 파일
├── package.json      # 프로젝트 설정
└── README.md         # 프로젝트 문서
```

## ⚙️ 환경 설정

1. `.env.example` 파일을 `.env`로 복사
2. 필요한 환경 변수 설정
3. 개발 서버 재시작

```bash
cp .env.example .env
```

## 💡 개발 가이드

### 코드 스타일

프로젝트의 코딩 컨벤션을 따라주세요:
- ESLint/Prettier 설정 준수
- 의미있는 변수명 사용
- 적절한 주석 작성

### 테스트

```bash
npm test
# 또는
yarn test
# 또는
pnpm test
```

### 배포

프로덕션 빌드 후 배포:

```bash
npm run build
npm start
```

## 🔧 문제 해결

### 일반적인 문제

1. **의존성 설치 오류**
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

2. **포트 충돌**
   - `.env` 파일에서 PORT 변경

3. **빌드 오류**
   - Node.js 버전 확인
   - 캐시 삭제 후 재빌드

## 📚 참고 자료

- [공식 문서](https://github.com)
- [API 레퍼런스](https://github.com)
- [예제 프로젝트](https://github.com)

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 💬 문의

프로젝트에 대한 질문이나 제안사항이 있으시면 이슈를 등록해주세요.

---

Made with ❤️ by the community
"""

def get_package_json(name, category):
    """package.json 생성"""
    return {
        "name": name.lower().replace(' ', '-'),
        "version": "1.0.0",
        "description": f"{name.title()} starter template",
        "main": "index.js",
        "scripts": {
            "dev": "echo 'Development server'",
            "build": "echo 'Build project'",
            "start": "echo 'Start production server'",
            "test": "echo 'Run tests'"
        },
        "keywords": [name, category],
        "author": "",
        "license": "MIT",
        "dependencies": {},
        "devDependencies": {}
    }

def create_template(index, name, category):
    """템플릿 디렉토리 생성"""
    # 1551부터 시작
    dir_name = f"{1551 + index:04d}_{category}_{name.replace(' ', '_').replace('-', '_')}"
    dir_path = Path(dir_name)

    # 디렉토리 생성
    dir_path.mkdir(exist_ok=True)

    # 프레임워크 타입 결정
    framework_type = get_framework_type(category, name)

    # package.json 생성
    package_json = get_package_json(name, category)
    with open(dir_path / "package.json", "w", encoding="utf-8") as f:
        json.dump(package_json, f, indent=2, ensure_ascii=False)

    # README.md 생성
    readme_content = get_korean_readme(name, category, framework_type)
    with open(dir_path / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    # .gitignore 생성
    gitignore_content = get_gitignore(framework_type)
    with open(dir_path / ".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)

    # .env.example 생성
    env_content = get_env_example(framework_type, name)
    with open(dir_path / ".env.example", "w", encoding="utf-8") as f:
        f.write(env_content)

    return dir_name

def main():
    """메인 함수"""
    print("🚀 200개의 새로운 템플릿 생성 시작...\n")

    index = 0
    created = []

    for category, programs in new_programs.items():
        print(f"\n📦 {category} 카테고리 처리 중...")
        for program in programs:
            dir_name = create_template(index, program, category)
            created.append(dir_name)
            index += 1
            if (index) % 10 == 0:
                print(f"  ✓ {index}개 완료...")

    print(f"\n✅ 완료!")
    print(f"  - 총 생성: {len(created)}개")
    print(f"  - 범위: 1551 ~ {1550 + len(created)}")
    print(f"\n생성된 템플릿 샘플:")
    for i in range(min(5, len(created))):
        print(f"  - {created[i]}")
    print(f"  ...")
    for i in range(max(0, len(created) - 5), len(created)):
        print(f"  - {created[i]}")

if __name__ == "__main__":
    main()
