#!/usr/bin/env python3
"""
프로그램 템플릿 생성 스크립트
각 카테고리별로 200개씩, 총 800개의 프로그램 템플릿을 생성합니다.
"""

import os
import json

# 카테고리별 프로그램 리스트 (각 200개씩)
programs = {
    "web": [
        # Frontend Frameworks (20)
        "Next.js", "React", "Vue", "Angular", "Svelte", "Nuxt.js", "Gatsby", "Remix", "SvelteKit", "Astro",
        "Solid.js", "Qwik", "Preact", "Inferno", "Alpine.js", "Lit", "Stencil", "Marko", "Elder.js", "Eleventy",
        # Full-stack (10)
        "Blitz.js", "RedwoodJS", "Meteor", "Sails.js", "AdonisJS", "Feathers", "LoopBack", "Total.js", "Egg.js", "ThinkJS",
        # Node.js (20)
        "Express", "Koa", "Fastify", "Hapi", "Nest.js", "Restify", "Polka", "Micro", "Moleculer", "Marble.js",
        "Graphback", "ActionHero", "FoalTS", "ts.ED", "Marble", "Alosaur", "Oak", "Opine", "Abc", "Servest",
        # Python (20)
        "Django", "Flask", "FastAPI", "Tornado", "Pyramid", "Bottle", "CherryPy", "web2py", "TurboGears", "Dash",
        "Streamlit", "Gradio", "Reflex", "Flet", "Sanic", "Quart", "Starlette", "BlackSheep", "Masonite", "Falcon",
        # Ruby (15)
        "Ruby on Rails", "Sinatra", "Hanami", "Padrino", "Grape", "Cuba", "Roda", "Camping", "Ramaze", "NYNY",
        "Scorched", "Hobbit", "Brooklyn", "Nancy", "Lattice",
        # PHP (20)
        "Laravel", "Symfony", "CodeIgniter", "Slim", "Lumen", "Phalcon", "Yii", "CakePHP", "FuelPHP", "Fat-Free",
        "Laminas", "Flight", "Kohana", "PHPixie", "Aura", "Nette", "Lithium", "Pop PHP", "Silex", "Zend",
        # Java/JVM (20)
        "Spring Boot", "Spring MVC", "Micronaut", "Quarkus", "Vert.x", "Spark Java", "Javalin", "Play Framework", "Grails", "Dropwizard",
        "Vaadin", "Struts", "JSF", "Wicket", "GWT", "Blade", "ActFramework", "Jooby", "Pippo", "Ratpack",
        # Go (20)
        "Gin", "Echo", "Fiber", "Chi", "Beego", "Revel", "Iris", "Buffalo", "Gorilla", "Martini",
        "Goji", "GoFrame", "Macaron", "Aero", "Flamego", "Goyave", "Utron", "Tango", "Golf", "Web.go",
        # Rust (10)
        "Actix-web", "Rocket", "Axum", "Warp", "Tide", "Poem", "Salvo", "Thruster", "Gotham", "Nickel",
        # .NET (10)
        "ASP.NET Core", "Nancy", "ServiceStack", "Carter", "Giraffe", "Saturn", "WebSharper", "Suave", "Frank", "NancyFx",
        # Other Languages (15)
        "Phoenix", "Plug", "Cowboy", "Scotty", "Yesod", "Snap", "Servant",
        "Ktor", "http4k", "Vapor", "Kitura", "Perfect", "Ceylon", "Scala HTTP", "ZIO HTTP",
        # Static Site Generators (20)
        "Hugo", "Jekyll", "Hexo", "VuePress", "Docusaurus", "MkDocs", "Gridsome", "Pelican", "Middleman", "Nanoc",
        "Bridgetown", "Zola", "Cobalt", "Publii", "Lektor", "Nikola", "Wyam", "StaticGen", "Assemble", "Metalsmith",
    ] + [f"Web Tool {i}" for i in range(1, 21)],  # 추가 웹 도구 20개

    "app": [
        # Cross-platform Mobile (20)
        "React Native", "Flutter", "Ionic", "Xamarin", "NativeScript", "Capacitor", "Cordova", "Framework7", "Onsen UI", "Quasar",
        "Tauri", "Electron", "NW.js", "Neutralinojs", "Wails", "Proton Native", "React Native Windows", "React Native macOS", "Kotlin Multiplatform", "Compose Multiplatform",
        # iOS Native (20)
        "SwiftUI", "UIKit", "Vapor Backend", "Perfect", "Kitura", "SwiftNIO", "Alamofire", "Kingfisher", "SnapKit", "RxSwift",
        "Combine", "Core Data", "Realm Swift", "GRDB", "SQLite.swift", "Moya", "PromiseKit", "ReactiveCocoa", "Hero", "Lottie iOS",
        # Android Native (20)
        "Jetpack Compose", "Android SDK", "Kotlin", "Material Components", "ConstraintLayout", "Room", "Retrofit", "OkHttp", "Dagger", "Hilt",
        "RxJava", "Coroutines", "Flow", "LiveData", "ViewModel", "Navigation Component", "WorkManager", "Paging", "Glide", "Coil",
        # Desktop (20)
        "Electron App", "Tauri Desktop", "Flutter Desktop", "Qt", "GTK", "wxWidgets", "FLTK", "ImGui", "Avalonia", "UNO Platform",
        "WPF", "WinForms", "JavaFX", "Swing", "SWT", "Tkinter", "PyQt", "Kivy", "BeeWare", "Fyne",
        # Game Dev (20)
        "Unity", "Unreal Engine", "Godot", "Cocos2d", "libGDX", "MonoGame", "Phaser", "Pygame", "LÖVE", "Defold",
        "GameMaker", "Construct", "RPG Maker", "GDevelop", "Heaps", "HaxeFlixel", "PlayCanvas", "Three.js Game", "Babylon.js", "A-Frame",
        # AR/VR (10)
        "ARKit", "ARCore", "Vuforia", "Wikitude", "8th Wall", "AR.js", "WebXR", "Unity AR", "MRTK", "OpenXR",
        # Mobile Backend (20)
        "Firebase", "Supabase", "Appwrite", "Parse", "AWS Amplify", "Azure Mobile", "Backendless", "Kuzzle", "LoopBack Mobile", "Realm",
        "Back4App", "Kinvey", "CloudBoost", "Deployd", "Hoodie", "PouchDB", "CouchDB", "MongoDB Mobile", "SQLite Mobile", "Couchbase Lite",
        # UI Kits (20)
        "Material-UI Mobile", "Ant Design Mobile", "React Native Paper", "React Native Elements", "NativeBase", "Shoutem UI", "UI Kitten", "RNUI Lib", "Teaset", "React Native UI",
        "Flutter Material", "Flutter Cupertino", "GetWidget", "VelocityX", "Bruno", "Flutter Neumorphic", "Flukit", "Fish Redux", "GetX UI", "Provider UI",
        # Testing (10)
        "Appium", "Detox", "Espresso", "XCTest", "Maestro", "Cavy", "Calabash", "EarlGrey", "KIF", "Robotium",
        # State Management (10)
        "Redux Mobile", "MobX Mobile", "Zustand Mobile", "Recoil Mobile", "Jotai Mobile", "Provider", "Riverpod", "BLoC", "GetX", "MobX Flutter",
        # Analytics (10)
        "Firebase Analytics", "Mixpanel", "Amplitude", "Segment", "Countly", "Flurry", "App Annie", "Adjust", "AppsFlyer", "Branch",
        # Animation (10)
        "Lottie Mobile", "Rive", "Reanimated", "Gesture Handler", "Animated API", "React Spring Mobile", "Framer Mobile", "Motion", "Flare", "Hero",
        # Storage (10)
        "AsyncStorage", "MMKV", "Realm Mobile", "SQLite", "WatermelonDB", "PouchDB Mobile", "Hive", "Shared Preferences", "Keychain", "Keystore",
    ],

    "backend": [
        # Node.js (25)
        "Express.js", "Koa.js", "Fastify", "Hapi.js", "Nest.js", "Restify", "Sails.js", "Total.js", "Adonis.js", "Feathers.js",
        "LoopBack", "Meteor Backend", "Derby.js", "Strapi Backend", "Keystone.js", "Polka", "Micro Backend", "Next.js API", "Blitz.js Backend", "Redwood.js",
        "Marble.js Backend", "Tsed", "Routing Controllers", "TypeGraphQL", "TypeORM Backend",
        # Python (25)
        "Django Backend", "Flask Backend", "FastAPI Backend", "Tornado", "Pyramid Backend", "Bottle", "CherryPy", "Sanic", "Quart", "Starlette Backend",
        "aiohttp", "Falcon Backend", "Hug", "Responder", "Molten", "API Star", "Masonite Backend", "web2py Backend", "TurboGears Backend", "Dash Backend",
        "Connexion", "Eve", "Vibora", "Bocadillo", "Emmett",
        # Java/JVM (25)
        "Spring Boot Backend", "Micronaut Backend", "Quarkus Backend", "Vert.x Backend", "Dropwizard", "Spark Java Backend", "Javalin Backend", "Play Backend", "Grails Backend", "Helidon",
        "Ktor Backend", "http4k Backend", "Jooby", "Ratpack", "Pippo", "ActFramework", "Blade Backend", "Bootique", "JHipster", "Lagom",
        "Armeria", "Light-4j", "Restlet", "Jersey", "RESTEasy",
        # Go (20)
        "Gin Backend", "Echo Backend", "Fiber Backend", "Chi", "Beego", "Revel Backend", "Iris Backend", "Buffalo Backend", "GoFrame", "Macaron",
        "Gorilla Mux", "Goji", "Martini", "Aero", "Flamego", "Goyave", "Utron", "Tango", "Golf", "Goa",
        # Rust (15)
        "Actix-web Backend", "Rocket Backend", "Axum Backend", "Warp Backend", "Tide Backend", "Poem Backend", "Salvo Backend", "Thruster", "Gotham", "Nickel.rs",
        "Tower", "Hyper", "Conduit", "Rouille", "Iron",
        # PHP (20)
        "Laravel Backend", "Symfony Backend", "CodeIgniter", "Slim Backend", "Lumen Backend", "Phalcon", "Yii2", "CakePHP", "Zend", "FuelPHP",
        "Fat-Free", "Flight", "Silex", "Kohana", "PHPixie", "Aura", "Nette", "Lithium", "Pop PHP", "Laminas",
        # Ruby (10)
        "Rails Backend", "Sinatra Backend", "Hanami Backend", "Padrino Backend", "Grape Backend", "Cuba", "Roda Backend", "Camping", "Ramaze", "Scorched",
        # .NET (10)
        "ASP.NET Core Backend", "NancyFx Backend", "ServiceStack", "Carter Backend", "Giraffe Backend", "Saturn", "Suave", "WebSharper", "OpenRasta", "Simple.Web",
        # ORMs (20)
        "Prisma", "TypeORM", "Sequelize", "Mongoose", "Knex.js", "Objection.js", "Bookshelf.js", "Waterline", "MikroORM", "Drizzle ORM",
        "SQLAlchemy", "Django ORM", "Peewee", "Tortoise ORM", "Pony ORM", "Hibernate", "jOOQ", "Exposed", "MyBatis", "GORM",
        # API (10)
        "GraphQL", "Apollo Server", "Hasura", "PostGraphile", "tRPC", "gRPC", "Thrift", "Protocol Buffers", "REST", "Swagger",
        # Message Queues (10)
        "RabbitMQ", "Kafka", "Redis Pub/Sub", "NATS", "Pulsar", "SQS", "Pub/Sub", "Service Bus", "ActiveMQ", "ZeroMQ",
        # Auth (10)
        "Passport.js", "Auth0", "Keycloak", "OAuth2", "JWT", "NextAuth.js", "Supertokens", "Ory", "AuthJS", "Lucia",
    ],

    "frontend": [
        # Frameworks (20)
        "React Frontend", "Vue.js", "Angular Frontend", "Svelte Frontend", "Solid.js", "Preact", "Inferno", "Lit Frontend", "Alpine.js", "Stimulus",
        "Qwik Frontend", "Marko", "Mithril", "Riot.js", "Hyperapp", "Aurelia", "Ember.js", "Backbone.js", "Knockout.js", "Polymer",
        # Meta Frameworks (10)
        "Next.js Frontend", "Nuxt.js", "SvelteKit Frontend", "Remix Frontend", "Astro Frontend", "Gatsby Frontend", "Blitz.js Frontend", "RedwoodJS Frontend", "Fresh", "Analog",
        # UI Libraries (30)
        "Material-UI", "Ant Design", "Chakra UI", "Mantine", "shadcn/ui", "Radix UI", "Headless UI", "daisyUI", "NextUI", "PrimeReact",
        "Bootstrap", "Tailwind UI", "Flowbite", "Semantic UI", "Bulma", "Foundation", "Materialize", "UIkit", "Pure.css", "Skeleton",
        "PrimeNG", "NG-ZORRO", "Angular Material", "Vuetify", "Quasar Frontend", "Element Plus", "Naive UI", "Vant", "PrimeVue", "Buefy",
        # CSS (20)
        "Tailwind CSS", "Bootstrap CSS", "Sass", "Less", "Styled Components", "Emotion", "CSS Modules", "PostCSS", "Stylus", "Stitches",
        "Vanilla Extract", "Linaria", "Compiled", "StyleX", "Panda CSS", "UnoCSS", "Windi CSS", "Twin.macro", "Theme UI", "Twind",
        # State Management (20)
        "Redux", "MobX", "Zustand", "Recoil", "Jotai", "Valtio", "XState", "Effector", "Rematch", "Easy Peasy",
        "Pinia", "Vuex", "Harlem", "NgRx", "Akita", "NGXS", "Elf", "Nano Stores", "Overmind", "Storeon",
        # Build Tools (20)
        "Vite", "Webpack", "Rollup", "Parcel", "esbuild", "Turbopack", "SWC", "Rspack", "Snowpack", "wmr",
        "Browserify", "Brunch", "FuseBox", "Poi", "Neutrino", "Rome", "Biome", "tsup", "Bun", "Nx",
        # Testing (30)
        "Jest", "Vitest", "Mocha", "Jasmine", "Karma", "AVA", "Tape", "uvu", "Node-tap", "Playwright",
        "Cypress", "TestCafe", "Puppeteer", "Selenium", "WebdriverIO", "Nightwatch", "CodeceptJS", "Cucumber", "Protractor", "Casper.js",
        "Testing Library", "Enzyme", "Vue Test Utils", "Angular Testing", "Storybook", "Chromatic", "Percy", "Applitools", "BackstopJS", "Wraith",
        # Animation (20)
        "Framer Motion", "React Spring", "GSAP", "Anime.js", "Three.js", "Motion One", "Lottie", "Rive Frontend", "Remotion", "Theatre.js",
        "Mo.js", "Popmotion", "Velocity.js", "Animate.css", "Vivus", "ScrollReveal", "AOS", "Particles.js", "Typed.js", "Chart.js",
        # Data Fetching (10)
        "Axios", "Fetch API", "SWR", "React Query", "RTK Query", "Apollo Client", "urql", "Relay", "tRPC Frontend", "GraphQL Request",
        # Form (10)
        "React Hook Form", "Formik", "Final Form", "Yup", "Zod", "VeeValidate", "Vuelidate", "Angular Forms", "Vest", "joi",
        # Routing (10)
        "React Router", "TanStack Router", "Wouter", "Vue Router", "Angular Router", "Svelte Routing", "Page.js", "Navigo", "Director", "Reach Router",
    ],
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
    print("프로그램 템플릿 생성 시작")
    print("=" * 60)

    counter = 1

    for category, program_list in programs.items():
        print(f"\n{category.upper()} 카테고리 생성 중...")
        for i, program in enumerate(program_list, 1):
            create_template(category, program, counter)
            counter += 1

    print("\n" + "=" * 60)
    print(f"완료! 총 {counter-1}개의 프로그램 템플릿이 생성되었습니다.")
    print("=" * 60)

    # 카테고리별 통계
    print("\n카테고리별 통계:")
    for category, program_list in programs.items():
        print(f"  - {category.upper()}: {len(program_list)}개")

if __name__ == "__main__":
    main()
