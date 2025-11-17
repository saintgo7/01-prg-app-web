#!/usr/bin/env python3
"""
추가 프로그램 템플릿 생성 스크립트
각 카테고리별로 50개씩, 총 200개의 프로그램 템플릿을 추가합니다.
"""

import os
import json

# 각 카테고리별 추가 프로그램 리스트 (각 50개씩)
additional_programs = {
    "web": [
        # CMS & Content Management (20)
        "WordPress", "Joomla", "Drupal", "Typo3", "Concrete5", "ModX", "SilverStripe", "Bolt CMS", "Grav", "October CMS",
        "Kirby", "Statamic", "ProcessWire", "Cockpit", "Textpattern", "ExpressionEngine", "Contao", "DotCMS", "Magnolia", "Liferay",

        # E-commerce Platforms (15)
        "WooCommerce", "Shopify Polaris", "BigCommerce", "Magento 2", "Shopware", "PrestaShop", "Lightspeed", "Wix eCommerce", "Squarespace Commerce", "Ecwid",
        "3dcart", "Volusion", "Shift4Shop", "X-Cart", "osCommerce",

        # API Gateways & Management (10)
        "Kong", "Tyk", "AWS API Gateway", "Azure API Management", "Apigee", "MuleSoft", "WSO2", "KrakenD", "Express Gateway", "Traefik",

        # Serverless Frameworks (5)
        "Serverless Framework", "AWS SAM", "Azure Functions", "Google Cloud Functions", "OpenFaaS",
    ],

    "app": [
        # Mobile Development Tools (15)
        "Xcode", "Android Studio", "Visual Studio App Center", "Expo", "Fastlane", "CocoaPods", "Gradle", "Maven", "App Store Connect", "Google Play Console",
        "TestFlight", "Firebase App Distribution", "Bitrise", "CodeMagic", "CircleCI Mobile",

        # Mobile UI Libraries (15)
        "SwiftUI Components", "Material Design Components", "Cupertino Widgets", "React Native UI Toolbox", "Flutter Widgets", "Ant Design Mobile RN", "React Native Vector Icons", "Flutter Icons", "Ionicons", "Material Icons",
        "FontAwesome Mobile", "Feather Icons", "React Native Maps", "Flutter Maps", "Mapbox Mobile",

        # Mobile Payment (10)
        "Stripe Mobile", "PayPal SDK", "Apple Pay", "Google Pay", "Square SDK", "Braintree", "Razorpay", "In-App Purchase", "RevenueCat", "Adapty",

        # Mobile Push Notifications (10)
        "OneSignal", "Firebase Cloud Messaging", "Pusher", "Airship", "Pushwoosh", "Batch", "CleverTap", "Leanplum", "Notifee", "React Native Push Notification",
    ],

    "backend": [
        # Microservices Tools (15)
        "Docker", "Kubernetes", "Istio", "Consul", "Linkerd", "Envoy", "NGINX", "HAProxy", "Traefik", "Caddy",
        "Nomad", "Rancher", "OpenShift", "Docker Swarm", "Mesos",

        # Caching Systems (10)
        "Redis", "Memcached", "Varnish", "Hazelcast", "Apache Ignite", "Ehcache", "Caffeine", "Guava Cache", "Coherence", "Infinispan",

        # Logging & Monitoring (15)
        "ELK Stack", "Splunk", "Graylog", "Fluentd", "Logstash", "Kibana", "Grafana Loki", "Papertrail", "Loggly", "Sumo Logic",
        "DataDog", "New Relic APM", "AppDynamics", "Dynatrace", "Elastic APM",

        # Task Queues (10)
        "BullMQ", "Bull", "Bee-Queue", "Kue", "Agenda", "node-resque", "Celery", "Sidekiq", "Resque", "Delayed Job",
    ],

    "frontend": [
        # Design Systems (15)
        "Atlassian Design System", "Carbon Design System", "Polaris", "Lightning Design System", "Ant Design System", "Material Design System", "Fluent UI", "Blueprint UI", "Evergreen UI", "Elastic UI",
        "Adobe Spectrum", "Shopify Polaris", "IBM Carbon", "Primer", "Base Web",

        # Icon Libraries (15)
        "Font Awesome", "Material Icons", "Feather Icons", "Heroicons", "Lucide", "Ionicons", "Bootstrap Icons", "Remix Icon", "Tabler Icons", "Phosphor Icons",
        "Octicons", "CoreUI Icons", "Iconly", "Iconoir", "Clarity Icons",

        # Data Visualization Libraries (10)
        "D3.js", "Recharts", "Visx", "Victory", "Nivo", "Chart.js", "ECharts", "Highcharts", "Plotly.js", "ApexCharts",

        # Frontend Performance (10)
        "Lighthouse", "WebPageTest", "GTmetrix", "PageSpeed Insights", "Webpack Bundle Analyzer", "React DevTools Profiler", "Chrome DevTools", "Web Vitals", "Perfume.js", "SpeedCurve",
    ]
}

def get_package_json(name, category, description):
    """package.json 템플릿 생성"""
    return {
        "name": name.lower().replace(" ", "-").replace("(", "").replace(")", "").replace(".", ""),
        "version": "1.0.0",
        "description": description,
        "main": "index.js",
        "scripts": {
            "start": "node index.js",
            "dev": "nodemon index.js",
            "test": "echo \"No tests specified\" && exit 0"
        },
        "keywords": [category, name.lower()],
        "author": "",
        "license": "MIT"
    }

def get_readme_content(name, category, description, num):
    """README.md 템플릿 생성"""
    return f"""# {name}

## 카테고리
{category.upper()}

## 설명
{description}

## 번호
{num:03d}

## 시작하기

### 설치
```bash
npm install
```

### 개발 서버 실행
```bash
npm run dev
```

### 프로덕션 빌드
```bash
npm run build
```

## 기능
- {name} 기반 프로젝트
- 모던 개발 환경 설정
- 기본 템플릿 제공

## 기술 스택
- {name}
- Node.js
- npm/yarn

## 문서
- 공식 문서: [링크 추가 필요]
- GitHub: [링크 추가 필요]

## 라이선스
MIT

## 기여
기여를 환영합니다!
"""

def get_index_html(name):
    """index.html 템플릿 생성"""
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - 템플릿</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            line-height: 1.6;
        }}
        h1 {{
            color: #333;
            border-bottom: 2px solid #0066cc;
            padding-bottom: 10px;
        }}
        .info {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        code {{
            background: #e8e8e8;
            padding: 2px 6px;
            border-radius: 3px;
        }}
    </style>
</head>
<body>
    <h1>{name} 템플릿</h1>
    <div class="info">
        <h2>환영합니다!</h2>
        <p>이것은 <strong>{name}</strong> 프로젝트 템플릿입니다.</p>
        <p>시작하려면 <code>npm install</code>을 실행하세요.</p>
    </div>
    <script src="index.js"></script>
</body>
</html>
"""

def get_index_js(name):
    """index.js 템플릿 생성"""
    return f"""/**
 * {name} 프로젝트
 * 기본 진입점 파일
 */

console.log('Welcome to {name}!');

// 여기에 코드를 작성하세요
function init() {{
    console.log('{name} initialized successfully');
}}

init();
"""

def create_template(category, name, num):
    """개별 프로그램 템플릿 생성"""
    # 디렉토리 이름 생성
    clean_name = name.lower().replace(" ", "_").replace("(", "").replace(")", "").replace(".", "").replace("/", "_")
    dir_name = f"{num:03d}_{category}_{clean_name}"

    # 디렉토리 생성
    os.makedirs(dir_name, exist_ok=True)

    # 설명 생성
    descriptions = {
        "web": f"{name} 웹 프레임워크/라이브러리를 사용한 프로젝트 템플릿",
        "app": f"{name} 모바일/데스크톱 앱 프레임워크를 사용한 프로젝트 템플릿",
        "backend": f"{name} 백엔드 프레임워크/도구를 사용한 프로젝트 템플릿",
        "frontend": f"{name} 프론트엔드 라이브러리/도구를 사용한 프로젝트 템플릿"
    }

    description = descriptions.get(category, f"{name} 프로젝트 템플릿")

    # README.md 생성
    readme_path = os.path.join(dir_name, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(get_readme_content(name, category, description, num))

    # package.json 생성
    package_json_path = os.path.join(dir_name, "package.json")
    with open(package_json_path, "w", encoding="utf-8") as f:
        json.dump(get_package_json(name, category, description), f, indent=2, ensure_ascii=False)

    # index.html 생성
    index_html_path = os.path.join(dir_name, "index.html")
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(get_index_html(name))

    # index.js 생성
    index_js_path = os.path.join(dir_name, "index.js")
    with open(index_js_path, "w", encoding="utf-8") as f:
        f.write(get_index_js(name))

    print(f"✓ Created: {dir_name}")

def main():
    """메인 함수"""
    print("=" * 60)
    print("추가 프로그램 템플릿 생성 시작")
    print("=" * 60)

    # 기존 디렉토리 번호 확인
    existing_dirs = [d for d in os.listdir('.') if os.path.isdir(d) and d[0].isdigit()]
    if existing_dirs:
        max_num = max([int(d.split('_')[0]) for d in existing_dirs])
        counter = max_num + 1
    else:
        counter = 821

    for category, program_list in additional_programs.items():
        print(f"\n{category.upper()} 카테고리에 {len(program_list)}개 추가 중...")
        for i, program in enumerate(program_list, 1):
            create_template(category, program, counter)
            counter += 1

    print("\n" + "=" * 60)
    print(f"완료! {counter - 821}개의 추가 프로그램 템플릿이 생성되었습니다.")
    print("=" * 60)

    # 카테고리별 통계
    print("\n카테고리별 추가 통계:")
    for category, program_list in additional_programs.items():
        print(f"  - {category.upper()}: {len(program_list)}개 추가")

if __name__ == "__main__":
    main()
