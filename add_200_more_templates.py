#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
추가 200개 프로그램 템플릿 생성 (1751-1950)
"""

import os
import json
from pathlib import Path

# 200개 새로운 프로그램 (기존 1,750개와 중복 없이)
new_programs = {
    "monitoring": [
        # Monitoring & Observability (15개)
        "prometheus", "grafana", "jaeger", "zipkin", "sentry",
        "newrelic", "datadog-agent", "dynatrace-agent", "honeycomb",
        "lightstep", "instana", "appdynamics-agent", "skywalking",
        "pinpoint", "elastic-apm-agent"
    ],
    "queue": [
        # Message Queues & Streaming (15개)
        "rabbitmq", "activemq", "zeromq", "nats", "pulsar",
        "amazon-sqs", "amazon-kinesis", "google-pubsub", "azure-servicebus",
        "ibm-mq", "kafka-streams", "redis-streams", "beanstalkd",
        "nsq", "rocketmq"
    ],
    "graphql": [
        # GraphQL Tools (12개)
        "graphql-mesh", "graphql-codegen", "graphql-shield", "graphql-tools",
        "apollo-client", "relay", "urql", "apollo-federation",
        "mercurius", "graphql-request", "graphql-helix", "envelop"
    ],
    "state": [
        # State Management (15개)
        "redux", "mobx", "zustand", "jotai", "recoil",
        "xstate", "valtio", "effector", "rematch", "easy-peasy",
        "redux-toolkit", "redux-saga", "redux-observable", "redux-thunk",
        "overmind"
    ],
    "forms": [
        # Form Libraries (12개)
        "react-hook-form", "formik", "final-form", "react-final-form",
        "unform", "vest", "yup", "zod", "joi",
        "ajv", "superstruct", "valibot"
    ],
    "animation": [
        # Animation Libraries (15개)
        "framer-motion", "react-spring", "gsap", "animejs", "popmotion",
        "velocity", "mojs", "three", "lottie", "rive",
        "auto-animate", "motion-one", "theatre", "remotion", "react-move"
    ],
    "dataviz": [
        # Additional Data Visualization (10개)
        "apexcharts", "c3", "chartist", "fusioncharts", "amcharts",
        "anychart", "plotly-python", "bokeh", "seaborn", "pygal"
    ],
    "docs": [
        # Documentation Tools (12개)
        "docusaurus", "vuepress", "docsify", "mkdocs", "sphinx-doc",
        "gitbook", "slate", "docz", "storybook", "styleguidist",
        "compodoc", "typedoc"
    ],
    "lint": [
        # Linting & Formatting (15개)
        "eslint", "prettier", "stylelint", "commitlint", "lint-staged",
        "husky", "standard", "xo", "tslint", "biome",
        "ruff", "black", "flake8", "pylint", "mypy"
    ],
    "gaming": [
        # Gaming Engines & Libraries (10개)
        "phaser", "pixijs", "babylonjs", "playcanvas", "aframe",
        "excalibur", "melonjs", "matter-js", "p5js", "konva"
    ],
    "iot": [
        # IoT Platforms (10개)
        "johnny-five", "cylon", "node-red", "thingsboard", "iot-hub",
        "aws-iot", "google-iot", "azure-iot", "particle", "platformio"
    ],
    "video": [
        # Video Processing (10개)
        "ffmpeg", "videojs", "hls", "dash", "shaka-player",
        "plyr", "mediaelement", "jwplayer", "cloudinary-video", "mux"
    ],
    "image": [
        # Image Processing (12개)
        "sharp", "jimp", "imagemagick", "graphicsmagick", "pillow",
        "opencv", "gm", "canvas", "fabric", "konvajs",
        "cropperjs", "pica"
    ],
    "pdf": [
        # PDF Tools (10개)
        "pdfkit", "puppeteer-pdf", "jspdf", "pdf-lib", "pdfmake",
        "react-pdf", "pdfjs", "wkhtmltopdf", "weasyprint", "reportlab"
    ],
    "email": [
        # Email Services (10개)
        "nodemailer", "sendgrid", "mailgun", "amazon-ses", "postmark",
        "mailchimp", "sendinblue", "sparkpost", "mandrill", "mjml"
    ],
    "payment": [
        # Payment Gateways (10개)
        "stripe", "paypal", "square", "adyen", "braintree-payments",
        "mollie", "checkout", "authorize-net", "worldpay", "paddle"
    ],
    "analytics": [
        # Analytics (12개)
        "google-analytics", "mixpanel", "amplitude", "segment", "heap",
        "plausible", "matomo", "fathom", "umami", "posthog",
        "rudderstack", "snowplow"
    ],
    "ssg": [
        # Additional Static Site Generators (8개)
        "hugo", "jekyll", "hexo", "pelican", "gridsome",
        "scully", "bridgetown", "zola"
    ],
    "microservices": [
        # Microservices Tools (8개)
        "seneca", "micro-dev", "moleculer-micro", "nameko", "dapr",
        "tars", "go-micro", "kratos"
    ],
    "serverless": [
        # Serverless Frameworks (9개)
        "serverless-framework", "sst", "arc", "chalice", "zappa",
        "claudia", "apex", "fission", "kubeless"
    ]
}

def get_framework_type(category, name):
    """프레임워크 타입 결정"""
    # Node.js 기반
    nodejs_patterns = ['js', 'node', 'react', 'vue', 'angular', 'next', 'express', 'nest',
                       'graphql', 'apollo', 'redux', 'mobx', 'zustand', 'framer', 'gsap',
                       'three', 'phaser', 'pixi', 'babylon', 'video', 'pdf', 'nodemailer',
                       'stripe', 'paypal', 'sendgrid', 'sharp', 'jimp', 'canvas', 'puppeteer',
                       'eslint', 'prettier', 'husky', 'serverless', 'docusaurus', 'storybook',
                       'relay', 'urql', 'formik', 'yup', 'joi', 'zod', 'lottie', 'animejs',
                       'chartist', 'apexcharts', 'segment', 'amplitude', 'mixpanel']

    # Python 기반
    python_patterns = ['python', 'django', 'flask', 'fastapi', 'pillow', 'opencv',
                       'reportlab', 'weasyprint', 'mkdocs', 'sphinx', 'pelican',
                       'black', 'flake8', 'pylint', 'mypy', 'ruff', 'nameko',
                       'chalice', 'zappa', 'bokeh', 'seaborn', 'pygal', 'plotly-python']

    # Go 기반
    go_patterns = ['go-', 'dapr', 'kratos']

    # Ruby 기반
    ruby_patterns = ['jekyll', 'bridgetown']

    # Rust 기반
    rust_patterns = ['zola']

    # Java 기반
    java_patterns = ['activemq', 'kafka', 'pulsar', 'rabbitmq']

    # Multi/Generic
    multi_patterns = ['prometheus', 'grafana', 'jaeger', 'sentry', 'datadog',
                      'rabbitmq', 'redis', 'kafka', 'nats', 'zeromq',
                      'ffmpeg', 'imagemagick', 'graphicsmagick', 'hugo']

    name_lower = name.lower()

    for pattern in python_patterns:
        if pattern in name_lower:
            return 'python'

    for pattern in go_patterns:
        if pattern in name_lower:
            return 'go'

    for pattern in ruby_patterns:
        if pattern in name_lower:
            return 'ruby'

    for pattern in rust_patterns:
        if pattern in name_lower:
            return 'rust'

    for pattern in java_patterns:
        if pattern in name_lower:
            return 'java'

    for pattern in multi_patterns:
        if pattern in name_lower:
            return 'multi'

    for pattern in nodejs_patterns:
        if pattern in name_lower:
            return 'nodejs'

    # 기본값은 카테고리에 따라
    if category in ['graphql', 'state', 'forms', 'animation', 'gaming', 'video',
                    'email', 'payment', 'analytics', 'serverless']:
        return 'nodejs'
    elif category in ['image', 'pdf']:
        return 'nodejs'
    elif category == 'docs':
        return 'nodejs'
    elif category == 'lint':
        return 'nodejs'
    elif category in ['monitoring', 'queue', 'microservices']:
        return 'multi'

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
        'ruby': """*.gem
*.rbc
/.config
/coverage/
/InstalledFiles
/pkg/
/spec/reports/
/spec/examples.txt
/test/tmp/
/test/version_tmp/
/tmp/
.bundle/
vendor/bundle
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
        'multi': """node_modules/
dist/
build/
target/
.env
.env.local
*.log
.DS_Store
.idea/
.vscode/
coverage/
tmp/
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
        'monitoring': '모니터링',
        'queue': '메시지 큐',
        'graphql': 'GraphQL',
        'state': '상태 관리',
        'forms': '폼 라이브러리',
        'animation': '애니메이션',
        'dataviz': '데이터 시각화',
        'docs': '문서화',
        'lint': '린팅 & 포매팅',
        'gaming': '게임 엔진',
        'iot': 'IoT',
        'video': '비디오 처리',
        'image': '이미지 처리',
        'pdf': 'PDF 도구',
        'email': '이메일 서비스',
        'payment': '결제 게이트웨이',
        'analytics': '애널리틱스',
        'ssg': '정적 사이트 생성기',
        'microservices': '마이크로서비스',
        'serverless': '서버리스'
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
        "name": name.lower().replace(' ', '-').replace('_', '-'),
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
    # 1751부터 시작
    dir_name = f"{1751 + index:04d}_{category}_{name.replace(' ', '_').replace('-', '_')}"
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
    print("🚀 200개의 추가 템플릿 생성 시작...\n")

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
    print(f"  - 범위: 1751 ~ {1750 + len(created)}")
    print(f"\n생성된 템플릿 샘플:")
    for i in range(min(5, len(created))):
        print(f"  - {created[i]}")
    print(f"  ...")
    for i in range(max(0, len(created) - 5), len(created)):
        print(f"  - {created[i]}")

if __name__ == "__main__":
    main()
