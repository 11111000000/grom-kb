# 🛠 Технологический стек (проверено)

> Подробное описание технологий (обновлено после эпистемического аудита 26.06.2026)

---

## 🎨 Frontend

### Текущий (точно)
- **HTML5** — генерируется WordPress
- **CSS3** — тема Bono 1.10.8, **402 571 байт (402 КБ)** ✅ подтверждено
- **JavaScript** — jQuery (WordPress legacy) + Elementor scripts
- **Шрифты** — Google Fonts (Roboto), wpshop-core (иконочный), swiper-icons

### Планируемый
- **CSS3** — modern, с custom properties
- **JavaScript** — vanilla JS / Alpine.js (без jQuery)
- **Шрифты** — локально (Inter, TT Norms Pro, Unbounded)
- **Сборка** — Vite или PostCSS

---

## ⚙️ Backend

### Текущий (точно)
- **PHP** — 7.4+ (рекомендуется 8.1+)
- **MySQL** — 5.7+ (рекомендуется 8.0)
- **WordPress** — последняя версия
- **WooCommerce** — 10.8.1 ✅
- **Elementor Pro** — конструктор

### Планируемый (если делать новый сайт)
- **Next.js / Nuxt.js** — статический сайт с серверным рендерингом
- **Headless CMS** — Strapi или Directus
- **База данных** — PostgreSQL или MySQL
- **API** — REST или GraphQL
- **Хостинг** — Vercel / Netlify + отдельный backend

---

## 🛒 E-commerce

### Текущий (точно)
- **WooCommerce** — основной движок магазина
- **Robokassa** — платёжная система (merchantLogin="grom-38") ✅
- **Woo Custom Product Addons Pro** — доп. поля

### Подтверждённые данные из кода:
- Подпись Robokassa: `8d4f676c2137083fcbef8f18a7a8a7df` ⚠️
- Виджет в HTML (не безопасно)
- Подключается на каждой карточке (тяжело)

### Планируемый
- **WooCommerce** (оставляем, если не меняем стек)
- **Robokassa** — оставляем
- **СДЭК API** — расчёт доставки
- **Почта России API** — расчёт доставки
- **«МойСклад»** — учёт товаров

---

## 🔌 Плагины WordPress (11, подтверждено)

### Активные

| Плагин | Назначение | Статус | Приоритет |
|---|---|---|---|
| akismet | Антиспам | ✅ оставить | — |
| all-in-one-seo-pack-pro | SEO | 🟡 заменить | P1 |
| bwd-dual-buttons | Кнопки | 🔴 удалить | P1 |
| cookie-bar | Cookie | 🔴 заменить | P0 (спам-текст) |
| customer-email-verification | Email | 🟡 настроить | P2 |
| elementor + elementor-pro | Конструктор | ✅ оставить | — |
| google-analytics-for-wordpress | GA | ✅ оставить | — |
| max-ru-connect | MAX | ✅ оставить | — |
| robokassa | Оплата | ✅ оставить | — |
| woocommerce | Магазин | ✅ оставить | — |
| woo-custom-product-addons-pro | Доп. поля | 🟡 оценить | P2 |

### Будем добавлять
- **WP Rocket** — кэширование (P0)
- **Imagify** — оптимизация изображений (P0)
- **Yoast SEO** или **RankMath** — SEO (P1)
- **СДЭК** — доставка (P0)
- **WP Mail SMTP** — отправка email (P0)

---

## 📄 Контент (проверено)

### Товары (6 SKU)
| SKU | Название | Цена | Размеры | Описание | Отзывы |
|---|---|---|---|---|---|
| 001 | Озёрные коньки неокрашенные | 7 800 ₽ | 460, 520 мм | ✅ 1217 симв. | ✅ 109 |
| 002 | Озёрные коньки окрашенные | 9 200 ₽ | 460, 520 мм | ✅ 1217 симв. | ✅ 109 |
| 003 | Лезвие неокрашенное | 6 600 ₽ | 480, 520 мм | ❌ пусто | 0 |
| 004 | Лезвие окрашенное | 8 000 ₽ | 480, 520 мм | ❌ пусто | 0 |
| 005 | Чехол | 1 200 ₽ | — | ⚠️ зашифровано | 0 |
| 006 | Крепление | 1 200 ₽ | — | ⚠️ зашифровано | 0 |

### Страницы (33 HTML-файла)
- `/` — главная
- `/магазин-спортивного-инвентаря/` — лендинг
- `/product-category/гром/` — каталог
- `/product/*/` — 6 карточек
- `/контакты/` — контакты
- `/страница-в-разработке/` — заглушка
- `/публичная-оферта/`
- `/cart/`, `/my-account/`, `/favorite/`
- 9× `index.html@p=*.html` — пагинация (?p=)
- `index.html@page_id=89.html` — копия магазина

---

## 🎨 Дизайн-инструменты

### Текущие
- Elementor (встроен в WP)

### Планируемые
- **Figma** — дизайн и прототипы
- **FigJam** — мудборды
- **Coolors** — палитры
- **Google Fonts** — подбор шрифтов

---

## 📊 Аналитика

### Подключено
- ✅ Яндекс.Метрика (с webvisor, ecommerce)
- ✅ Google Analytics 4
- ✅ Yandex Verification
- ✅ Google Verification

### Не настроено (но доступно)
- ❌ Ecommerce события в GA4
- ❌ Цели в Метрике
- ❌ UTM-разметка
- ❌ Hotjar / Microsoft Clarity

---

## 🔐 Безопасность

### Текущее
- SSL: требуется проверка
- Бэкапы: требуется настройка
- Защита админки: требуется усиление
- Антиспам: Akismet

### Найденные проблемы
- ⚠️ **Robokassa `signature` в HTML-коде** — утечка данных
- ⚠️ **Отключена валидация форм** — нет защиты
- ⚠️ **Открытый wp-admin** — стандартный риск WP

### Планируемое
- 2FA для админки
- Ограничение попыток входа
- Регулярные бэкапы (ежедневно)
- WAF

---

## 🚀 Хостинг

### Текущий
- Неизвестно (проверить у хостера)
- Домен: `xn--38-glc0bjl.xn--p1ai` (IDN для гром38.рф)

### Требования
- PHP 8.1+
- MySQL 8.0+
- SSD
- SSL
- Бэкапы
- Поддержка РФ

---

## 📦 Реальные данные из кода (проверено)

### robots.txt
```
User-agent: *
Disallow: /wp-content/uploads/wc-logs/
Disallow: /wp-content/uploads/woocommerce_transient_files/
Disallow: /wp-content/uploads/woocommerce_uploads/
Disallow: /*?add-to-cart=
Disallow: /*?*add-to-cart=
Disallow: /wp-admin/
Disallow: /wp-includes
Disallow: /wp-content/plugins
Disallow: /wp-content/cache
Disallow: /wp-content/themes
Disallow: /trackback
Disallow: */trackback
Disallow: */feed
Disallow: /*?*       ⚠️ КРИТИЧНО — блокирует ВСЕ параметры
Disallow: /tag

Sitemap: https://xn--38-glc0bjl.xn--p1ai/video-sitemap.xml
Sitemap: https://xn--38-glc0bjl.xn--p1ai/sitemap.xml
Sitemap: https://xn--38-glc0bjl.xn--p1ai/sitemap.rss
```

### Schema.org (пример, SKU 001)
```json
{
  "@type": "Product",
  "name": "Озёрные коньки \"ГРОМ\" неокрашенные (байсы/нордики)",
  "sku": "001",
  "description": "Нордики или как их ещё называют - байсы. ...",
  "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.00", "reviewCount": 109},
  "offers": {"@type": "Offer", "price": "7800.00", "priceCurrency": "RUB", "availability": "https://schema.org/InStock"}
}
```

### Robokassa
- merchantLogin: `grom-38`
- signature: `8d4f676c2137083fcbef8f18a7a8a7df` (в HTML!)

---

## 🔗 Связанные документы

- [[Performance]] — производительность
- [[SEO-Tech]] — SEO-техника
- [[Schema-Fix]] — фикс микроразметки
- [[../02-Audit/Epistemic-Audit]] — коррекция данных

[[MOC-Tech|⬅ MOC Tech]] | [[../README|⬅ Главная]]