#!/usr/bin/env python3
"""
템플릿 완성 스크립트
부족한 중요 도구들을 모든 카테고리에 추가합니다.
"""

import os
import json

# 부족한 중요 도구들을 카테고리별로 정리
missing_programs = {
    "web": [
        # 데이터베이스 관리 도구 (20)
        "PostgreSQL Admin", "MySQL Workbench", "MongoDB Compass", "Redis Desktop Manager", "DBeaver",
        "pgAdmin", "phpMyAdmin", "Adminer", "TablePlus", "Sequel Pro",
        "DataGrip", "HeidiSQL", "DbVisualizer", "SQLyog", "MySQL GUI Tools",
        "Robo 3T", "Studio 3T", "Redis Commander", "RedisInsight", "Postbird",

        # WebAssembly (10)
        "Blazor", "Emscripten", "AssemblyScript", "wasm-bindgen", "wasmtime",
        "Wasmer Runtime", "WASI", "wasm-pack", "Binaryen", "WABT",

        # Low-Code/No-Code (20)
        "Retool", "Bubble", "Webflow", "OutSystems", "Mendix",
        "Appian", "Zoho Creator", "Microsoft Power Apps", "Salesforce Lightning", "ServiceNow",
        "Airtable", "Notion API", "Coda", "ClickUp API", "Monday.com",
        "Zapier", "Make (Integromat)", "n8n", "Pipedream", "Autocode",
    ],

    "app": [
        # 데이터베이스 (20)
        "SQLite Browser", "Core Data Editor", "Realm Studio", "Firebase Firestore", "MongoDB Realm",
        "WatermelonDB Inspector", "SQLDelight", "ObjectBox", "Couchbase Mobile", "LevelDB",
        "IndexedDB", "LocalStorage Manager", "SecureStorage", "Keychain Services", "Android Keystore",
        "EncryptedSharedPreferences", "SQLCipher", "Secure Enclave", "Biometric Auth", "Face ID",

        # 앱 모니터링 & 크래시 리포팅 (15)
        "Crashlytics", "Sentry Mobile", "Bugsnag", "Instabug", "TestFairy",
        "AppDynamics Mobile", "New Relic Mobile", "Dynatrace Mobile", "Firebase Crashlytics", "Rollbar Mobile",
        "Airbrake", "Raygun", "Elmah", "LogRocket Mobile", "FullStory",

        # 딥링킹 & 유니버설 링크 (15)
        "Branch.io", "Firebase Dynamic Links", "Adjust Deep Linking", "AppsFlyer OneLink", "Singular",
        "Universal Links", "App Links", "URI Scheme", "Deferred Deep Linking", "Contextual Deep Linking",
        "App Indexing", "Firebase App Indexing", "Smart Banners", "QR Code Scanner", "Barcode Scanner",
    ],

    "backend": [
        # 데이터베이스 (30)
        "PostgreSQL", "MySQL", "MariaDB", "Oracle Database", "Microsoft SQL Server",
        "MongoDB", "CouchDB", "Cassandra", "ScyllaDB", "HBase",
        "DynamoDB", "Firebase Realtime DB", "Cloud Firestore", "Azure Cosmos DB", "FaunaDB",
        "Neo4j", "ArangoDB", "OrientDB", "JanusGraph", "TigerGraph",
        "InfluxDB", "TimescaleDB", "QuestDB", "ClickHouse", "Druid",
        "Elasticsearch", "Apache Solr", "Algolia", "Meilisearch", "Typesense",

        # 검색 & 인덱싱 (10)
        "OpenSearch", "Sphinx", "Manticore Search", "Xapian", "Whoosh",
        "Lucene", "Tantivy", "Bleve", "Sonic", "RediSearch",

        # 메시지 브로커 추가 (10)
        "Apache Kafka Streams", "Kafka Connect", "RabbitMQ Management", "MQTT", "AMQP",
        "Apache Flink", "Apache Storm", "Apache Samza", "AWS Kinesis", "Google Pub/Sub",
    ],

    "frontend": [
        # 데이터 페칭 & API (20)
        "TanStack Query", "Apollo Client GraphQL", "urql GraphQL", "Relay Modern", "GROQ",
        "REST Client", "HTTP Client", "Fetch Wrapper", "Ky", "Got",
        "Superagent", "Request", "node-fetch", "isomorphic-fetch", "cross-fetch",
        "wretch", "redaxios", "alova", "ofetch", "ohmyfetch",

        # 상태 관리 라이브러리 추가 (15)
        "Immer", "Redux Toolkit", "RTK Query", "Redux Saga", "Redux Observable",
        "MobX State Tree", "Zustand Persist", "Recoil Sync", "Jotai Utils", "Valtio Utils",
        "XState Viz", "Effector Logger", "Akita Query", "NGXS Logger", "RxDB",

        # 폼 밸리데이션 (15)
        "React Final Form", "Formik Yup", "React Hook Form Zod", "Vest.js", "Joi Validator",
        "Ajv", "Superstruct", "io-ts", "Runtypes", "Valibot",
        "class-validator", "Fonk", "Nope Validator", "Bandit", "Schema Inspector",
    ]
}

# DevOps, AI/ML, Data 등 새로운 카테고리 추가
new_categories = {
    "devops": [
        # CI/CD (20)
        "Jenkins", "GitLab CI", "CircleCI", "Travis CI", "GitHub Actions",
        "Azure Pipelines", "AWS CodePipeline", "Google Cloud Build", "Bamboo", "TeamCity",
        "Drone CI", "Concourse CI", "Buildkite", "Semaphore CI", "Buddy",
        "Codefresh", "Harness", "Spinnaker", "Argo CD", "Flux CD",

        # 버전 관리 (15)
        "Git", "GitHub", "GitLab", "Bitbucket", "Azure DevOps",
        "Gitea", "Gogs", "SourceForge", "Mercurial", "SVN",
        "Perforce", "Plastic SCM", "Fossil", "Darcs", "Bazaar",

        # 인프라 as 코드 (20)
        "Terraform", "Pulumi", "CloudFormation", "ARM Templates", "CDK",
        "Ansible", "Chef", "Puppet", "SaltStack", "Vagrant",
        "Packer", "Consul Template", "Helm", "Kustomize", "Jsonnet",
        "Kapitan", "Skaffold", "Tilt", "Garden", "Draft",

        # 모니터링 & 옵저버빌리티 (25)
        "Prometheus", "Grafana", "Jaeger", "Zipkin", "OpenTelemetry",
        "Datadog Agent", "New Relic Agent", "Elastic APM Agent", "Dynatrace OneAgent", "AppDynamics Agent",
        "Nagios", "Zabbix", "Icinga", "Sensu", "Cacti",
        "Netdata", "Telegraf", "StatsD", "Graphite", "InfluxDB OSS",
        "Loki", "Tempo", "Cortex", "Thanos", "VictoriaMetrics",
    ],

    "data": [
        # 데이터 처리 (20)
        "Apache Spark", "Apache Flink", "Apache Beam", "Databricks", "Snowflake",
        "Pandas", "NumPy", "Dask", "Vaex", "Polars",
        "Apache Airflow", "Prefect", "Dagster", "Luigi", "Kedro",
        "dbt", "Great Expectations", "Pandera", "Soda", "Monte Carlo",

        # 데이터 시각화 (15)
        "Tableau", "Power BI", "Looker", "Metabase", "Superset",
        "Redash", "Apache Zeppelin", "Jupyter", "Observable", "Streamlit",
        "Plotly Dash", "Bokeh", "Altair", "Seaborn", "Matplotlib",

        # ETL/ELT (15)
        "Apache NiFi", "Talend", "Informatica", "Fivetran", "Stitch",
        "Airbyte", "Singer", "Meltano", "dlt", "Estuary Flow",
        "Hevo Data", "Skyvia", "Integrate.io", "Matillion", "Rivery",
    ],

    "ai_ml": [
        # ML 프레임워크 (20)
        "TensorFlow", "PyTorch", "Keras", "scikit-learn", "XGBoost",
        "LightGBM", "CatBoost", "JAX", "MXNet", "Caffe",
        "Theano", "Chainer", "ONNX", "TensorFlow Lite", "PyTorch Mobile",
        "Core ML", "ML Kit", "TensorFlow.js", "ONNX Runtime", "OpenVINO",

        # NLP (15)
        "Hugging Face Transformers", "spaCy", "NLTK", "Gensim", "FastText",
        "AllenNLP", "Flair", "Stanford NLP", "TextBlob", "Pattern",
        "LangChain", "LlamaIndex", "Haystack", "Semantic Kernel", "AutoGen",

        # Computer Vision (15)
        "OpenCV", "PIL/Pillow", "scikit-image", "ImageAI", "Detectron2",
        "YOLO", "Mask R-CNN", "FastAI", "MMDetection", "Kornia",
        "Albumentations", "imgaug", "augly", "DALI", "torchvision",
    ],

    "database": [
        # SQL 데이터베이스 (20)
        "PostgreSQL", "MySQL", "MariaDB", "SQLite", "Oracle DB",
        "MS SQL Server", "DB2", "CockroachDB", "YugabyteDB", "TiDB",
        "Vitess", "Citus", "Greenplum", "Amazon Aurora", "Google Cloud SQL",
        "Azure SQL", "PlanetScale", "Neon", "Supabase DB", "Railway DB",

        # NoSQL (20)
        "MongoDB", "Redis", "Cassandra", "Elasticsearch", "Couchbase",
        "DynamoDB", "Firebase", "Neo4j", "ArangoDB", "RavenDB",
        "OrientDB", "MarkLogic", "Riak", "Voldemort", "HBase",
        "ScyllaDB", "Apache Ignite", "Hazelcast", "Memcached", "Aerospike",

        # Time-Series (10)
        "InfluxDB", "TimescaleDB", "Prometheus TSDB", "QuestDB", "ClickHouse",
        "Druid", "OpenTSDB", "KairosDB", "Graphite", "VictoriaMetrics",
    ],

    "security": [
        # 보안 도구 (20)
        "OWASP ZAP", "Burp Suite", "Nmap", "Wireshark", "Metasploit",
        "Snyk", "SonarQube", "Checkmarx", "Veracode", "Fortify",
        "HashiCorp Vault", "AWS Secrets Manager", "Azure Key Vault", "CyberArk", "1Password",
        "LastPass", "Bitwarden", "KeePass", "Let's Encrypt", "Certbot",

        # 인증/인가 (15)
        "Okta", "Auth0", "Cognito", "Firebase Auth", "FusionAuth",
        "Keycloak", "Ory", "SuperTokens", "Authelia", "Authentik",
        "Gluu", "WSO2 Identity", "Ping Identity", "OneLogin", "JumpCloud",

        # 방화벽 & 보안 (15)
        "ModSecurity", "Fail2Ban", "UFW", "iptables", "pfSense",
        "Cloudflare WAF", "AWS WAF", "Azure Firewall", "Imperva", "Akamai",
        "Sucuri", "Wordfence", "Qualys", "Tenable", "Rapid7",
    ],

    "cloud": [
        # AWS 서비스 (20)
        "AWS EC2", "AWS S3", "AWS Lambda", "AWS RDS", "AWS DynamoDB",
        "AWS ECS", "AWS EKS", "AWS Fargate", "AWS CloudFront", "AWS Route53",
        "AWS SQS", "AWS SNS", "AWS API Gateway", "AWS Cognito", "AWS Amplify",
        "AWS AppSync", "AWS Step Functions", "AWS EventBridge", "AWS CloudWatch", "AWS X-Ray",

        # Azure 서비스 (15)
        "Azure VMs", "Azure Blob Storage", "Azure Functions", "Azure SQL", "Azure Cosmos DB",
        "Azure AKS", "Azure App Service", "Azure CDN", "Azure DNS", "Azure Service Bus",
        "Azure API Management", "Azure AD", "Azure Logic Apps", "Azure Monitor", "Azure DevOps",

        # GCP 서비스 (15)
        "GCP Compute Engine", "GCP Cloud Storage", "GCP Cloud Functions", "GCP Cloud SQL", "GCP Firestore",
        "GCP GKE", "GCP App Engine", "GCP Cloud CDN", "GCP Cloud DNS", "GCP Pub/Sub",
        "GCP Cloud Run", "GCP BigQuery", "GCP Dataflow", "GCP Cloud Monitoring", "GCP Cloud Build",
    ]
}

# 기존 카테고리와 새 카테고리 합치기
all_programs = {**missing_programs, **new_categories}

def get_package_json(name, category, description):
    """package.json 템플릿 생성"""
    return {
        "name": name.lower().replace(" ", "-").replace("(", "").replace(")", "").replace(".", "").replace("/", "-"),
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
{num:04d}

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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        h1 {{
            color: white;
            border-bottom: 2px solid rgba(255,255,255,0.3);
            padding-bottom: 10px;
        }}
        .info {{
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
            backdrop-filter: blur(10px);
        }}
        code {{
            background: rgba(0,0,0,0.3);
            padding: 2px 8px;
            border-radius: 3px;
        }}
        .badge {{
            display: inline-block;
            background: rgba(255,255,255,0.2);
            padding: 5px 10px;
            border-radius: 20px;
            margin: 5px;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <h1>🚀 {name} 템플릿</h1>
    <div class="info">
        <h2>환영합니다!</h2>
        <p>이것은 <strong>{name}</strong> 프로젝트 템플릿입니다.</p>
        <p>시작하려면 <code>npm install</code>을 실행하세요.</p>
        <div>
            <span class="badge">✨ Modern</span>
            <span class="badge">⚡ Fast</span>
            <span class="badge">🎨 Beautiful</span>
        </div>
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

console.log('🚀 Welcome to {name}!');
console.log('=' .repeat(50));

// 여기에 코드를 작성하세요
function init() {{
    console.log('✅ {name} initialized successfully');
    console.log('📦 Ready to use!');
}}

init();

// 예제 기능
function exampleFeature() {{
    return {{
        name: '{name}',
        version: '1.0.0',
        status: 'active'
    }};
}}

console.log('📊 Project Info:', exampleFeature());
"""

def create_template(category, name, num):
    """개별 프로그램 템플릿 생성"""
    # 디렉토리 이름 생성
    clean_name = name.lower().replace(" ", "_").replace("(", "").replace(")", "").replace(".", "").replace("/", "_").replace("-", "_")
    dir_name = f"{num:04d}_{category}_{clean_name}"

    # 디렉토리 생성
    os.makedirs(dir_name, exist_ok=True)

    # 설명 생성
    descriptions = {
        "web": f"{name} 웹 프레임워크/라이브러리를 사용한 프로젝트 템플릿",
        "app": f"{name} 모바일/데스크톱 앱 프레임워크를 사용한 프로젝트 템플릿",
        "backend": f"{name} 백엔드 프레임워크/도구를 사용한 프로젝트 템플릿",
        "frontend": f"{name} 프론트엔드 라이브러리/도구를 사용한 프로젝트 템플릿",
        "devops": f"{name} DevOps 도구를 사용한 프로젝트 템플릿",
        "data": f"{name} 데이터 처리/분석 도구를 사용한 프로젝트 템플릿",
        "ai_ml": f"{name} AI/ML 프레임워크를 사용한 프로젝트 템플릿",
        "database": f"{name} 데이터베이스를 사용한 프로젝트 템플릿",
        "security": f"{name} 보안 도구를 사용한 프로젝트 템플릿",
        "cloud": f"{name} 클라우드 서비스를 사용한 프로젝트 템플릿"
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
    print("=" * 70)
    print("🔥 완전한 템플릿 컬렉션 생성 시작")
    print("=" * 70)

    # 기존 디렉토리 번호 확인
    existing_dirs = [d for d in os.listdir('.') if os.path.isdir(d) and d[0].isdigit()]
    if existing_dirs:
        max_num = max([int(d.split('_')[0]) for d in existing_dirs])
        counter = max_num + 1
    else:
        counter = 1021

    total_added = 0

    for category, program_list in all_programs.items():
        print(f"\n📁 {category.upper()} 카테고리에 {len(program_list)}개 추가 중...")
        for i, program in enumerate(program_list, 1):
            create_template(category, program, counter)
            counter += 1
            total_added += 1

    print("\n" + "=" * 70)
    print(f"✅ 완료! {total_added}개의 템플릿이 추가되었습니다.")
    print("=" * 70)

    # 카테고리별 통계
    print("\n📊 카테고리별 추가 통계:")
    for category, program_list in all_programs.items():
        print(f"  • {category.upper()}: {len(program_list)}개")

    print(f"\n🎉 총 템플릿 수: 1,020 + {total_added} = {1020 + total_added}개")

if __name__ == "__main__":
    main()
