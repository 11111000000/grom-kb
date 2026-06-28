# 🐳 Локальная разработка ГРОМ38 — Nix + Docker + devShell

> **Цель:** полностью воспроизводимое локальное окружение для разработки ГРОМ38
> **Принцип:** Nix управляет dev-tools, Docker поднимает сервисы (БД, кэш), AI-агент имеет доступ ко всему

---

## 🎯 Принципы

### Дао локальной разработки

1. **Один источник правды** — `flake.nix` определяет все версии
2. **Воспроизводимость** — `nix develop` поднимает окружение из декларации
3. **Изоляция** — Docker для сервисов с состоянием (БД, кэш)
4. **Скорость** — hot-reload для всего (фронт, бэк)
5. **AI-friendly** — структура понятна агенту, есть MCP-серверы

### Чего мы НЕ делаем

- ❌ Не используем `nixpkgs` для сервисов (БД, кэш) — Docker быстрее
- ❌ Не используем Docker для dev-tools (Node, Python) — Nix быстрее
- ❌ Не запускаем production-сервисы локально (только stubs/mocks)

---

## 🏗 Архитектура локальной среды

```
┌─────────────────────────────────────────────────────────┐
│                  Nix devShell (flake.nix)                │
│  ┌─────────────────────────────────────────────────┐   │
│  │ Node.js 22 (Astro, Wrangler, pnpm)              │   │
│  │ Python 3.13 (AI-агент, scripts)                 │   │
│  │ Bun (тесты)                                     │   │
│  │ Wrangler CLI (Cloudflare Workers)                │   │
│  │ SQLite (D1 локально)                            │   │
│  │ just (команды)                                  │   │
│  │ air (hot-reload Go)                             │   │
│  │ gitleaks, shellcheck, editorconfig             │   │
│  │ git, gh, jq, yq                                 │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                  Docker Compose                         │
│  ┌────────────────┐  ┌─────────────────┐                │
│  │ PostgreSQL 16  │  │ Redis 7         │                │
│  │ (заказы,       │  │ (сессии,        │                │
│  │ бронирования)  │  │ кэш)            │                │
│  └────────────────┘  └─────────────────┘                │
│  ┌────────────────┐  ┌─────────────────┐                │
│  │ MailHog        │  │ MinIO           │                │
│  │ (тест. email)  │  │ (S3 mock)       │                │
│  └────────────────┘  └─────────────────┘                │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                Cloudflare Wrangler (local)              │
│  - Workers (AI-агент, API)                              │
│  - D1 (SQLite локально)                                 │
│  - R2 (MinIO как mock)                                  │
│  - Vectorize (in-memory)                                │
│  - Workers AI (свой mock или Ollama)                    │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Структура проекта

```
GromProject/                              # КОРЕНЬ
├── flake.nix                             # Nix devShell declaration
├── .envrc                                # direnv use flake
├── Justfile                              # команды (dev, build, deploy)
├── .gitignore
├── docker-compose.yml                    # локальные сервисы
├── docker-compose.override.yml           # overrides для dev
│
├── .devcontainer/                        # VSCode dev container
│   ├── devcontainer.json
│   └── Dockerfile
│
├── .env.example                          # шаблон env-переменных
├── .env.local                            # локальные env (в .gitignore)
│
├── apps/
│   ├── web/                              # Astro 5 фронт
│   │   ├── astro.config.mjs
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── tailwind.config.cjs
│   │   ├── src/
│   │   │   ├── pages/
│   │   │   ├── components/
│   │   │   ├── layouts/
│   │   │   ├── lib/
│   │   │   ├── content/                  # Markdown (блог, описания)
│   │   │   │   ├── blog/
│   │   │   │   ├── products/
│   │   │   │   └── tours/
│   │   │   └── styles/
│   │   └── public/
│   │
│   ├── worker/                           # Cloudflare Workers (бэк)
│   │   ├── wrangler.toml
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── src/
│   │   │   ├── index.ts                  # entry
│   │   │   ├── agent/                    # AI-агент
│   │   │   │   ├── chat.ts
│   │   │   │   ├── tools.ts
│   │   │   │   └── prompts.ts
│   │   │   ├── api/                      # REST API
│   │   │   │   ├── orders.ts
│   │   │   │   ├── bookings.ts
│   │   │   │   ├── products.ts
│   │   │   │   └── reviews.ts
│   │   │   ├── db/                       # D1 schema
│   │   │   │   ├── schema.sql
│   │   │   │   └── queries.ts
│   │   │   ├── webhooks/                 # РобоКасса, Telegram
│   │   │   │   ├── robokassa.ts
│   │   │   │   └── telegram.ts
│   │   │   ├── vectorize/                # поиск
│   │   │   │   └── index.ts
│   │   │   └── lib/
│   │   └── migrations/
│   │
│   └── agent/                            # Python AI-агент (внешний процесс)
│       ├── pyproject.toml
│       ├── uv.lock
│       ├── src/
│       │   ├── main.py
│       │   ├── tools/
│       │   │   ├── airtable.py
│       │   │   ├── orders.py
│       │   │   └── search.py
│       │   ├── mcp/
│       │   │   └── server.py
│       │   └── prompts/
│       └── tests/
│
├── packages/
│   ├── ui/                               # shadcn/ui компоненты
│   │   ├── package.json
│   │   ├── src/
│   │   └── tailwind.config.cjs
│   │
│   ├── db/                               # SQL миграции, seed
│   │   ├── migrations/
│   │   │   └── 0001_initial.sql
│   │   └── seed.sql
│   │
│   └── tsconfig/                         # shared tsconfig
│       └── base.json
│
├── scripts/
│   ├── seed-data.py                      # заполнение Airtable/Astro
│   ├── sync-airtable.ts                  # синхронизация каталога
│   ├── build-content.sh                  # сборка контента
│   └── deploy.sh                         # деплой на Selectel
│
├── docs/                                 # документация (Obsidian-экспорт)
│
└── .github/
    └── workflows/
        ├── ci.yml                        # линт, тесты, build
        └── deploy.yml                    # деплой
```

---

## 🔧 Nix flake (devShell)

### `flake.nix`

```nix
{
  description = "ГРОМ38 — локальная разработка";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
    rust-overlay = {
      url = "github:oxalica/rust-overlay";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, rust-overlay }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [ rust-overlay.overlays.default ];
        };

        # Python 3.13 с uv
        python = pkgs.python313;
        uv = pkgs.uv;

        # Node.js 22 (LTS)
        node = pkgs.nodejs_22;

        # Bun (тесты)
        bun = pkgs.bun;
      in
      {
        devShells.default = pkgs.mkShell {
          name = "grom-dev";

          # Все пакеты для разработки
          packages = with pkgs; [
            # Языки
            node
            python
            uv
            bun
            go            # для будущих сервисов
            rustup        # для wrangler (написан на Rust)
            cargo
            deno          # для Cloudflare Workers
            
            # Node-пакеты (глобально)
            nodePackages.pnpm
            nodePackages.wrangler
            nodePackages.typescript
            nodePackages.tsx
            nodePackages.astro
            nodePackages."@cloudflare/workers-types"
            nodePackages."wrangler"
            
            # Python-пакеты (через uv)
            # (см. apps/agent/pyproject.toml)
            
            # Инструменты разработки
            just
            gnumake
            cmake
            pkg-config
            
            # Git
            git
            gh
            git-lfs
            
            # Контейнеры
            docker
            docker-compose
            podman          # альтернатива
            dive            # анализ образов
            
            # Линтеры/форматтеры
            shellcheck
            shfmt
            editorconfig-checker
            hadolint        # для Dockerfile
            tflint
            luacheck
            python311Packages.black
            python311Packages.ruff
            python311Packages.mypy
            python311Packages.pyright
            python311Packages.ipython
            python311Packages.jupyter
            
            # БД
            sqlite
            sqlite-interactive
            pgcli
            redis-cli
            postgresql_16
            
            # Сеть
            curl
            wget
            httpie
            mtr
            dig
            nmap
            
            # Безопасность
            gitleaks
            trivy           # сканирование уязвимостей
            
            # Мониторинг
            bottom
            bandwhich
            procs
            fd
            ripgrep
            bat
            eza
            zoxide
            fzf
            
            # Текстовые редакторы
            vim
            neovim
            helix
            
            # Браузер
            firefox
          ];

          # Переменные окружения
          env = {
            NODE_ENV = "development";
            PNPM_HOME = "${PWD}/.pnpm-home";
            PYTHONDONTWRITEBYTECODE = "1";
            PYTHONUNBUFFERED = "1";
            EDITOR = "hx";  # helix
            
            # Cloudflare
            CLOUDFLARE_ACCOUNT_ID = "dev-account";
            CLOUDFLARE_API_TOKEN = "dev-token";
            
            # Airtable
            AIRTABLE_API_KEY = "dev-key";
            AIRTABLE_BASE_ID = "appDev";
            
            # Resend (email)
            RESEND_API_KEY = "re_dev";
            
            # D1 локально
            D1_LOCAL = "true";
            D1_PATH = "${PWD}/.wrangler/state/d1";
            
            # S3/MinIO
            S3_ENDPOINT = "http://localhost:9000";
            S3_ACCESS_KEY = "minioadmin";
            S3_SECRET_KEY = "minioadmin";
            S3_BUCKET = "grom-files";
            
            # PostgreSQL (Docker)
            DATABASE_URL = "postgresql://grom:grom@localhost:5432/grom_dev";
            REDIS_URL = "redis://localhost:6379";
            
            # Ollama (для локального LLM)
            OLLAMA_HOST = "http://localhost:11434";
            
            # Robokassa (test)
            ROBOKASSA_MERCHANT = "grom-38";
            ROBOKASSA_TEST_MODE = "1";
          };

          # Shell hook (применяется при входе)
          shellHook = ''
            echo "🥾 ГРОМ38 dev shell"
            echo ""
            echo "📦 Команды:"
            echo "  just              — список всех команд"
            echo "  just dev          — запуск всех сервисов"
            echo "  just dev-web      — только Astro"
            echo "  just dev-worker   — только Workers"
            echo "  just dev-agent    — только AI-агент"
            echo "  just db           — миграции БД"
            echo "  just seed         — заполнить тестовые данные"
            echo "  just test         — все тесты"
            echo "  just build        — production build"
            echo "  just deploy       — деплой на Selectel"
            echo ""
            echo "🌐 URLs:"
            echo "  http://localhost:4321  — Astro dev"
            echo "  http://localhost:8787  — Wrangler dev (Workers)"
            echo "  http://localhost:8080  — MailHog (email UI)"
            echo "  http://localhost:9001  — MinIO Console"
            echo "  http://localhost:11434 — Ollama API"
            echo ""
          '';

          # uv venv для Python
          enterShell = ''
            mkdir -p .pnpm-home
            cd apps/agent && uv sync --frozen 2>/dev/null || uv sync
            cd ../..
          '';
        };

        # Формат Nix файлов
        formatter = pkgs.nixpkgs-fmt;
      }
    );
}
```

---

## 🐳 Docker Compose

### `docker-compose.yml`

```yaml
version: '3.9'

services:
  # PostgreSQL (для dev — production на Selectel Managed PG)
  postgres:
    image: postgres:16-alpine
    container_name: grom-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: grom
      POSTGRES_PASSWORD: grom
      POSTGRES_DB: grom_dev
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./packages/db/migrations:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U grom"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis (для сессий, кэша)
  redis:
    image: redis:7-alpine
    container_name: grom-redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # MinIO (S3 mock)
  minio:
    image: minio/minio:latest
    container_name: grom-minio
    restart: unless-stopped
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    ports:
      - "9000:9000"  # S3 API
      - "9001:9001"  # Console UI
    volumes:
      - minio_data:/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 10s
      retries: 3

  # MailHog (email mock)
  mailhog:
    image: mailhog/mailhog:latest
    container_name: grom-mailhog
    restart: unless-stopped
    ports:
      - "1025:1025"  # SMTP
      - "8025:8025"  # Web UI

  # Ollama (локальный LLM)
  ollama:
    image: ollama/ollama:latest
    container_name: grom-ollama
    restart: unless-stopped
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  # Adminer (DB UI)
  adminer:
    image: adminer:latest
    container_name: grom-adminer
    restart: unless-stopped
    ports:
      - "8081:8080"
    environment:
      ADMINER_DEFAULT_SERVER: postgres
      ADMINER_DESIGN: pepa-linha-dark
    depends_on:
      postgres:
        condition: service_healthy

volumes:
  postgres_data:
  redis_data:
  minio_data:
  ollama_data:

networks:
  default:
    name: grom-net
```

### `docker-compose.override.yml` (для dev)

```yaml
# Переопределения для удобства разработки
services:
  postgres:
    command: postgres -c log_statement=all -c log_min_duration_statement=0
  
  minio:
    environment:
      MINIO_BROWSER_REDIRECT_URL: http://localhost:9001
```

---

## 📜 Justfile (команды)

```just
# ГРОМ38 — Justfile
set shell := ["bash", "-uc"]
set dotenv-load := true

# === Dev команды ===

# Показать все команды
default:
    @just --list

# Запустить все сервисы
dev:
    @echo "🚀 Запуск всех сервисов..."
    docker compose up -d
    @echo "⏳ Ждём готовности PostgreSQL..."
    @just _wait-postgres
    @just db-migrate
    @just seed
    @echo ""
    @echo "✅ Все сервисы запущены:"
    @echo "  PostgreSQL: localhost:5432"
    @echo "  Redis:      localhost:6379"
    @echo "  MinIO:      localhost:9000 (console: 9001)"
    @echo "  MailHog:    localhost:8025"
    @echo "  Ollama:     localhost:11434"
    @echo "  Adminer:    localhost:8081"

# Остановить все сервисы
down:
    docker compose down

# Очистить всё (volumes!)
clean:
    docker compose down -v
    rm -rf .wrangler/state
    rm -rf node_modules apps/*/node_modules packages/*/node_modules
    rm -rf .pnpm-home

# Перезапустить
restart:
    @just down
    @just dev

# === Сервисы по отдельности ===

# Только Astro (фронт)
dev-web:
    cd apps/web && pnpm dev

# Только Workers (бэк)
dev-worker:
    cd apps/worker && pnpm dev

# Только Python AI-агент
dev-agent:
    cd apps/agent && uv run python -m src.main

# Локальный LLM (если нужно)
dev-llm:
    docker compose up -d ollama
    @echo "📥 Загрузка модели Qwen2.5-7B-Instruct (4-bit)..."
    docker compose exec ollama ollama pull qwen2.5:7b

# === БД ===

# Миграции
db-migrate:
    @echo "📦 Применение миграций..."
    psql $DATABASE_URL -f packages/db/migrations/0001_initial.sql
    @echo "✅ Миграции применены"

# Seed данные
seed:
    @echo "🌱 Заполнение тестовыми данными..."
    cd apps/agent && uv run python -m src.scripts.seed_data

# Откатить миграции (внимание!)
db-reset:
    @echo "⚠️  Сброс БД..."
    docker compose exec postgres dropdb -U grom grom_dev
    docker compose exec postgres createdb -U grom grom_dev
    @just db-migrate
    @just seed

# Подключиться к БД
db-shell:
    psql $DATABASE_URL

# Adminer UI
db-ui:
    @echo "🌐 Adminer: http://localhost:8081"
    @echo "   Server: postgres, User: grom, Pass: grom, DB: grom_dev"

# === Тесты ===

# Все тесты
test:
    @just test-web
    @just test-worker
    @just test-agent

# Тесты фронта
test-web:
    cd apps/web && pnpm test

# Тесты воркера
test-worker:
    cd apps/worker && pnpm test

# Тесты агента
test-agent:
    cd apps/agent && uv run pytest

# E2E тесты
test-e2e:
    cd apps/web && pnpm test:e2e

# === Линт ===

# Линт всего
lint:
    @just lint-web
    @just lint-worker
    @just lint-agent
    @just lint-nix

lint-web:
    cd apps/web && pnpm lint

lint-worker:
    cd apps/worker && pnpm lint

lint-agent:
    cd apps/agent && uv run ruff check .

lint-nix:
    nixpkgs-fmt --check .

# Форматирование
fmt:
    @just fmt-web
    @just fmt-worker
    @just fmt-agent
    @just fmt-nix

fmt-web:
    cd apps/web && pnpm fmt

fmt-worker:
    cd apps/worker && pnpm fmt

fmt-agent:
    cd apps/agent && uv run ruff format .

fmt-nix:
    nixpkgs-fmt .

# === Build ===

# Production build фронта
build-web:
    cd apps/web && pnpm build
    @echo "✅ Build: apps/web/dist/"

# Production build воркера
build-worker:
    cd apps/worker && pnpm build
    @echo "✅ Build: apps/worker/dist/"

# Все build
build:
    @just build-web
    @just build-worker

# === Deploy ===

# Деплой фронта на Cloudflare Pages
deploy-web:
    @just build-web
    @echo "🚀 Deploying to Cloudflare Pages..."
    cd apps/web && wrangler pages deploy ./dist --project-name=grom-web
    @echo "✅ Done: https://grom38.ru"

# Деплой воркера на Cloudflare Workers
deploy-worker:
    @just build-worker
    @echo "🚀 Deploying to Cloudflare Workers..."
    cd apps/worker && wrangler deploy
    @echo "✅ Done: https://api.grom38.ru"

# === Утилиты ===

# Логи всех сервисов
logs:
    docker compose logs -f

# Логи конкретного сервиса
logs-postgres:
    docker compose logs -f postgres

logs-minio:
    docker compose logs -f minio

# Использование ресурсов
stats:
    docker stats

# Очистить логи Docker
prune:
    docker system prune -f

# === Внутренние ===

_wait-postgres:
    @while ! docker compose exec -T postgres pg_isready -U grom >/dev/null 2>&1; do \
        sleep 1; \
    done
    @echo "✅ PostgreSQL ready"

# Проверка здоровья всех сервисов
health:
    @echo "🔍 Проверка здоровья..."
    @docker compose ps
    @echo ""
    @curl -s -o /dev/null -w "Astro:    %{http_code}\n" http://localhost:4321 || true
    @curl -s -o /dev/null -w "Worker:   %{http_code}\n" http://localhost:8787 || true
    @curl -s -o /dev/null -w "MailHog:  %{http_code}\n" http://localhost:8025 || true
    @curl -s -o /dev/null -w "MinIO:    %{http_code}\n" http://localhost:9000 || true
    @curl -s -o /dev/null -w "Ollama:   %{http_code}\n" http://localhost:11434 || true
```

---

## ⚙️ Astro конфиг (для локальной разработки)

### `apps/web/astro.config.mjs`

```javascript
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import airtable from '@astrojs/airtable';

// Переменные окружения
const AIRTABLE_API_KEY = process.env.AIRTABLE_API_KEY;
const AIRTABLE_BASE_ID = process.env.AIRTABLE_BASE_ID;

export default defineConfig({
  site: 'http://localhost:4321',
  output: 'static',  // Полная статика
  adapter: undefined,  // без адаптера (статика)

  integrations: [
    tailwind({ applyBaseStyles: true }),
    mdx(),
    sitemap(),
    // Кастомная интеграция для Airtable
    airtable({
      apiKey: AIRTABLE_API_KEY,
      baseId: AIRTABLE_BASE_ID,
      tables: ['products', 'tours', 'reviews'],
    }),
  ],

  vite: {
    server: {
      hmr: { overlay: false },
    },
    optimizeDeps: {
      exclude: ['wrangler'],
    },
  },

  server: {
    port: 4321,
    host: '0.0.0.0',  // для Docker
  },
});
```

---

## 🐍 Python AI-агент (локально)

### `apps/agent/pyproject.toml`

```toml
[project]
name = "grom-agent"
version = "0.1.0"
description = "AI-агент для ГРОМ38"
requires-python = ">=3.13"
dependencies = [
    "fastmcp>=0.4.0",
    "httpx>=0.27",
    "pydantic>=2.6",
    "sqlalchemy>=2.0",
    "asyncpg>=0.29",
    "redis>=5.0",
    "boto3>=1.34",  # S3 (MinIO)
    "openai>=1.30",  # для Workers AI proxy
    "anthropic>=0.20",
    "langchain>=0.1",
    "langchain-anthropic>=0.1",
    "playwright>=1.40",
    "beautifulsoup4>=4.12",
    "markdownify>=0.11",
    "pyairtable>=2.3",
    "resend>=0.7",
    "loguru>=0.7",
    "tenacity>=8.2",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.23",
    "pytest-cov>=4.1",
    "ruff>=0.3",
    "mypy>=1.8",
    "ipython>=8.20",
    "ipdb>=0.13",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### `apps/agent/src/main.py`

```python
"""
ГРОМ38 AI-агент
Локально подключается к Workers через MCP
"""
import asyncio
import logging
from contextlib import asynccontextmanager

from fastmcp import FastMCP

from src.tools import airtable, orders, search
from src.config import settings

logger = logging.getLogger(__name__)

# MCP сервер
mcp = FastMCP("grom-agent", host="0.0.0.0", port=8765)

# Инструменты
@mcp.tool()
async def search_products(query: str, limit: int = 5) -> list[dict]:
    """Поиск товаров в каталоге через Airtable"""
    return await airtable.search_products(query, limit)

@mcp.tool()
async def create_order(product_id: str, size: str, customer_phone: str) -> dict:
    """Создать заказ через API"""
    return await orders.create(product_id, size, customer_phone)

@mcp.tool()
async def get_product_info(sku: str) -> dict:
    """Получить информацию о товаре по артикулу"""
    return await airtable.get_by_sku(sku)

# === Запуск ===

@asynccontextmanager
async def lifespan():
    logger.info("🚀 ГРОМ AI-агент запущен")
    logger.info(f"   ENV: {settings.env}")
    logger.info(f"   Airtable: {settings.airtable_base_id}")
    yield
    logger.info("🛑 ГРОМ AI-агент остановлен")

if __name__ == "__main__":
    mcp.run(transport="sse")  # или "stdio" для Claude Desktop
```

---

## 🌐 Cloudflare Workers (локально через Wrangler)

### `apps/worker/wrangler.toml`

```toml
name = "grom-api"
main = "src/index.ts"
compatibility_date = "2024-12-01"

# Локальное окружение
[env.dev]
name = "grom-api-dev"
vars = { ENVIRONMENT = "development" }

# D1 (локальная SQLite)
[d1_databases](d1_databases.md)
binding = "DB"
database_name = "grom-db"
database_id = "local-db-id"  # для dev не нужен
# Для локальной работы Wrangler создаст SQLite в .wrangler/state/

# R2 (S3 mock через MinIO)
[r2_buckets](r2_buckets.md)
binding = "FILES"
bucket_name = "grom-files"
# Локально Wrangler эмулирует R2 без MinIO,
# но для интеграционных тестов можно использовать MinIO

# Vectorize (локально in-memory)
[vectorize](vectorize.md)
binding = "VECTORIZE"

# Workers AI (локально — Ollama proxy)
[ai]
binding = "AI"

# Secrets (для dev — в .dev.vars)
# ROBOKASSA_KEY = ...
# AIRTABLE_KEY = ...
# RESEND_KEY = ...
```

### `apps/worker/.dev.vars`

```bash
# Локальные секреты (в .gitignore!)
ROBOKASSA_MERCHANT_LOGIN="grom-38"
ROBOKASSA_TEST_MODE="1"
ROBOKASSA_PASSWORD="dev-password"

AIRTABLE_API_KEY="dev-key"
AIRTABLE_BASE_ID="appDev"

RESEND_API_KEY="re_dev"

DATABASE_URL="postgresql://grom:grom@localhost:5432/grom_dev"
REDIS_URL="redis://localhost:6379"

OLLAMA_URL="http://localhost:11434"
```

---

## 🚀 Быстрый старт

### Первый запуск

```bash
# 1. Клонировать
git clone https://github.com/za4d/GromProject.git
cd GromProject

# 2. Включить Nix (один раз)
# Nix установлен? direnv установлен?
direnv allow
# → загружается dev shell (Node 22, Python 3.13, Wrangler, pnpm, just, ...)

# 3. Скопировать .env
cp .env.example .env.local
cp apps/worker/.dev.vars.example apps/worker/.dev.vars
# Отредактировать под себя

# 4. Запустить все сервисы
just dev
# → Docker поднимает PostgreSQL, Redis, MinIO, MailHog, Ollama
# → миграции применяются
# → seed данные

# 5. В отдельных терминалах:
just dev-web      # Astro на :4321
just dev-worker   # Workers на :8787
just dev-agent    # Python агент на :8765
```

### Повседневная работа

```bash
# Войти в dev shell
cd ~/Projects/GromProject
# (direnv автоматически активирует)

# Все сервисы работают (just dev)
just health       # проверить

# Frontend
just dev-web      # или открыть http://localhost:4321

# Backend (Workers)
just dev-worker   # или открыть http://localhost:8787

# БД
just db-shell     # psql
just db-ui        # http://localhost:8081 (Adminer)

# Email
# http://localhost:8025 (MailHog UI)

# S3
# http://localhost:9001 (MinIO Console)
# minioadmin / minioadmin

# Тесты
just test
just lint

# Production build
just build

# Deploy
just deploy-web    # Cloudflare Pages
just deploy-worker # Cloudflare Workers
```

---

## 🔄 Переменные окружения (`.env.example`)

```bash
# === Environment ===
NODE_ENV=development
ENVIRONMENT=development

# === URLs ===
PUBLIC_SITE_URL=http://localhost:4321
PUBLIC_API_URL=http://localhost:8787
PUBLIC_AGENT_URL=http://localhost:8765

# === Airtable ===
AIRTABLE_API_KEY=keyXXXXXXXXXXXXXX
AIRTABLE_BASE_ID=appXXXXXXXXXXXXXX
AIRTABLE_TABLE_PRODUCTS=Products
AIRTABLE_TABLE_TOURS=Tours
AIRTABLE_TABLE_REVIEWS=Reviews

# === Cloudflare ===
CLOUDFLARE_ACCOUNT_ID=your-account-id
CLOUDFLARE_API_TOKEN=your-api-token
CLOUDFLARE_R2_BUCKET=grom-files

# === Robokassa (test) ===
ROBOKASSA_MERCHANT_LOGIN=grom-38
ROBOKASSA_PASSWORD=your-password-1
ROBOKASSA_TEST_MODE=1
ROBOKASSA_CALLBACK_URL=http://localhost:8787/webhooks/robokassa

# === Resend (email) ===
RESEND_API_KEY=re_xxx
RESEND_FROM_EMAIL=noreply@grom38.ru

# === Database (Docker) ===
DATABASE_URL=postgresql://grom:grom@localhost:5432/grom_dev
REDIS_URL=redis://localhost:6379

# === Ollama (local LLM) ===
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen2.5:7b

# === Telegram Bot (опционально) ===
TELEGRAM_BOT_TOKEN=your-bot-token

# === Logging ===
LOG_LEVEL=DEBUG
LOG_FORMAT=json
```

---

## 🤖 MCP-серверы для AI-агента

### `mcp.json` (в корне)

```json
{
  "mcpServers": {
    "grom-database": {
      "command": "uv",
      "args": ["--directory", "./apps/agent", "run", "python", "-m", "src.mcp.database"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      }
    },
    "grom-airtable": {
      "command": "uv",
      "args": ["--directory", "./apps/agent", "run", "python", "-m", "src.mcp.airtable"],
      "env": {
        "AIRTABLE_API_KEY": "${AIRTABLE_API_KEY}",
        "AIRTABLE_BASE_ID": "${AIRTABLE_BASE_ID}"
      }
    },
    "grom-robokassa": {
      "command": "uv",
      "args": ["--directory", "./apps/agent", "run", "python", "-m", "src.mcp.payments"],
      "env": {
        "ROBOKASSA_MERCHANT_LOGIN": "${ROBOKASSA_MERCHANT_LOGIN}"
      }
    },
    "grom-content": {
      "command": "uv",
      "args": ["--directory", "./apps/agent", "run", "python", "-m", "src.mcp.content"],
      "env": {
        "CONTENT_PATH": "./apps/web/src/content"
      }
    }
  }
}
```

---

## 📊 VSCode интеграция (`.vscode/settings.json`)

```json
{
  "extensions.recommendations": [
    "astro-build.astro-vscode",
    "bradlc.vscode-tailwindcss",
    "ms-python.python",
    "ms-python.mypy-type-checker",
    "rust-lang.rust-analyzer",
    "denoland.vscode-deno",
    "editorconfig.editorconfig",
    "tamasfe.even-better-toml",
    "redhat.vscode-yaml"
  ],
  "python.defaultInterpreterPath": "${workspaceFolder}/apps/agent/.venv/bin/python",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[astro]": {
    "editor.defaultFormatter": "astro-build.astro-vscode"
  },
  "nix.enableLanguageServer": true,
  "nix.formatterPath": "nixpkgs-fmt"
}
```

---

## 📋 Чек-лист готовности

### Команда разработчика
- [ ] Установить Nix (https://nixos.org/download.html)
- [ ] Установить direnv + shell hook
- [ ] Установить Docker + docker compose
- [ ] Клонировать репозиторий
- [ ] `direnv allow` в корне
- [ ] Скопировать `.env.example` → `.env.local`
- [ ] `just dev` для запуска всех сервисов
- [ ] `just health` для проверки
- [ ] Открыть http://localhost:4321 в браузере

### Проверка
- [ ] `just test` — все тесты проходят
- [ ] `just lint` — нет ошибок линтера
- [ ] `just build` — production build работает
- [ ] `just dev-web` — Astro с hot-reload
- [ ] `just dev-worker` — Wrangler с hot-reload
- [ ] `just dev-agent` — Python агент
- [ ] БД доступна через `just db-shell` и Adminer
- [ ] Email mock работает (MailHog)
- [ ] S3 mock работает (MinIO)
- [ ] Ollama отвечает

### Деплой (на prod)
- [ ] `just deploy-web` — фронт на Cloudflare Pages
- [ ] `just deploy-worker` — бэк на Cloudflare Workers
- [ ] БД на Selectel Managed PostgreSQL
- [ ] Secrets в Cloudflare Workers
- [ ] Airtable в production

---

## 🔗 Связанные документы

- [Stack-Recommendation](Stack-Recommendation.md) — финальный стек
- [Hosting-RF-Recommendation](Hosting-RF-Recommendation.md) — Selectel
- [../09-Decisions/ADR-001](../09-Decisions/ADR-001.md) — редизайн
- [ADR-008](ADR-008.md) — финальное решение по стеку (нужно создать)

[⬅ MOC Tech](MOC-Tech.md) | [⬅ Главная](../00-Inbox/README.md)