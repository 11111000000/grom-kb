# Аудит нового сайта (обновление)

**Дата:** 2026-06-29 (обновление)
**URL:** https://11111000000.github.io/gromproject/
**Версия:** Astro 5 + Tailwind, 7 тем, мобильная навигация
**Метод:** Lighthouse snapshot, curl, анализ DOM, проверка БД

---

## TL;DR

| Категория | Было | Стало | Статус |
|---|---|---|---|
| Техника | 6.5/10 | **9/10** | ✅ SEO-теги, favicon, robots, sitemap |
| SEO | 7/10 | **9/10** | ✅ Canonical, hreflang, OG, уникальные descriptions |
| UX | 5/10 | **8/10** | ✅ Мобильная навигация, 7 тем, переключатели |
| Контент/доступность | 6/10 | **8/10** | ✅ Контраст, heading order, labels |
| Эпистемика (данные) | 4/10 | **4/10** | ⏳ Требует БД (отдельно) |
| **Среднее** | **5.7/10** | **7.6/10** | **+1.9 ↑** |

---

## 1. Технический аудит

### ✅ Исправлено
- robots.txt добавлен ✓
- sitemap.xml добавлен (15 URL) ✓
- Favicon SVG (молния на тёмном фоне) ✓
- site.webmanifest добавлен ✓
- Preload критических шрифтов (Inter 600/700) ✓

### ✅ Базовые метрики (без изменений)
- Astro 5 + статический build (15 страниц)
- Tailwind purged CSS: 24 KB
- GZIP: HTML 42KB → 9KB
- Lighthouse Best Practices: 100/100
- TTFB: 425ms

### ⏳ Остаётся (требует работы с сервером/CDN)
- **Заголовки безопасности** — CSP, HSTS, X-Frame-Options (требуют настройки GitHub Pages или прокси)
- **Изображения** — 449KB JPEG без WebP (требует конвертации фото)
- **301 redirect** — GitHub Pages редиректит `/catalog` → `/catalog/` ( особенность GH Pages)

---

## 2. SEO-аудит

### ✅ Исправлено
- **Schema.org JSON-LD** — Organization (главная), Product (6 товаров), BreadcrumbList (все подстраницы) ✓
- **Canonical URL** — добавлен на все страницы ✓
- **Hreflang** — ru/en/zh + x-default ✓
- **Open Graph** — og:title, og:description, og:url, og:site_name, og:locale ✓
- **Twitter Card** — summary_large_image ✓
- **Meta description** — уникальный для каждой из 8 страниц ✓
- **Title** — уникальный (было и осталось) ✓

### ✅ Сводка по страницам

| URL | Title | Description | Canonical | Hreflang | OG |
|---|---|---|---|---|---|
| / | ✓ | ✓ уникальный | ✓ | ✓ | ✓ |
| /catalog/ | ✓ | ✓ уникальный | ✓ | ✓ | ✓ |
| /product/001/ | ✓ | ✓ уникальный | ✓ | ✓ | ✓ |
| /about/ | ✓ | ✓ уникальный | ✓ | ✓ | ✓ |
| /contacts/ | ✓ | ✓ уникальный | ✓ | ✓ | ✓ |
| /technology/ | ✓ | ✓ уникальный | ✓ | ✓ | ✓ |
| /tours/ | ✓ | ✓ уникальный | ✓ | ✓ | ✓ |
| /tours/baikal/ | ✓ | ✓ уникальный | ✓ | ✓ | ✓ |

---

## 3. UX-аудит

### ✅ Исправлено
- **Мобильная навигация** — hamburger-меню с slide-down drawer ✓
- **7 цветовых тем** — light, night, taiga, ice, polar, sunrise, ember ✓
- **Переключатели** — полупрозрачный фон融入 хедер на всех темах ✓
- **Языковой переключатель** — сохраняет текущий путь при переключении ✓
- **Белая полоса внизу** — убран лишний mt-12 у футера ✓

### ✅ Accessibility
- **Color contrast** — `text-frost-dark/50-80` теперь использует `var(--text)` с opacity 0.85 ✓
- **Heading order** — добавлен `sr-only` h2 перед h3 в catalog и technology ✓
- **Select labels** — добавлены `for`/`id` на label/select в калькуляторе ✓

### ⏳ Остаётся
- **Badges "ХИТ"** — нет определения (P2, косметика)

---

## 4. Эпистемический аудит (ПРАВДА ДАННЫХ)

> ⏳ **Требует работы с БД** — не исправлялось в текущей сессии

### Остаётся (все пункты требуют БД)
- Хардкод в Astro-файлах дублирует БД
- Число отзывов "109" — реальность 5 (ЛОЖЬ)
- Характеристики товаров не существуют в БД
- Описания в БД отличаются от описаний на сайте
- Склонения "км/кг" не переводятся на английский

---

## 5. Итоговый план

### ✅ Исправлено (14 пунктов)
1. ~~Мобильная навигация~~ → hamburger + slide-down drawer
2. ~~Хардкод `?lang=ru`~~ → используется текущий `lang`
3. ~~Schema.org JSON-LD~~ → Organization (главная), Product (6 товаров), BreadcrumbList (все подстраницы)
4. ~~robots.txt + sitemap.xml~~ → добавлены в public/
5. ~~Canonical URL~~ → на всех страницах
6. ~~Hreflang~~ → ru/en/zh + x-default
7. ~~Open Graph / Twitter Card~~ → на всех страницах
8. ~~Meta description~~ → уникальный на каждой странице
9. ~~Контраст текста~~ → opacity 0.85 для muted классов
10. ~~Heading order~~ → sr-only h2 перед h3
11. ~~Label для select~~ → for/id связка
12. ~~Preload шрифтов~~ → Inter 600/700
13. ~~Favicon + manifest~~ → SVG + webmanifest
14. ~~Schema.org BreadcrumbList~~ → все подстраницы (каталог, товары, туры, о бренде, контакты, технология)

### ⏳ Остаётся (требует отдельной работы)
- **WebP версии фото** — конвертация 6 JPEG → WebP
- **Данные из БД** — синхронизация хардкода с PostgreSQL (раздел 5 аудита)
- **Заголовки безопасности** — CSP, HSTS (требует настройки GH Pages)

## 6. Теги

`#audit` `#seo` `#ux` `#accessibility` `#i18n` `#mobile` `#astro` `#tailwind` `#fixed` `#remaining-db` `#remaining-webp`
