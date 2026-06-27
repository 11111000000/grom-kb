# ⚡ Производительность

> Оптимизация скорости загрузки сайта

---

## 📊 Целевые метрики

### Core Web Vitals (Google)

| Метрика | Цель | Текущее |
|---|---|---|
| LCP (Largest Contentful Paint) | < 2.5 сек | 🟡 проверить |
| FID (First Input Delay) | < 100 мс | 🟡 проверить |
| CLS (Cumulative Layout Shift) | < 0.1 | 🟡 проверить |
| TTFB (Time To First Byte) | < 800 мс | 🟡 проверить |
| FCP (First Contentful Paint) | < 1.8 сек | 🟡 проверить |

### Lighthouse

| Категория | Цель | Текущее |
|---|---|---|
| Performance | > 90 | 🟡 проверить |
| Accessibility | > 95 | 🟡 проверить |
| Best Practices | > 95 | 🟡 проверить |
| SEO | > 95 | 🟡 проверить |

---

## 🖼 Оптимизация изображений

### Что есть
- Hero: gr.webp (173 КБ) — оптимально ✅
- Логотип: gr-1.webp (28 КБ) — ОК
- Товарные: JPG 1-2 МБ — нужно оптимизировать ⚠️

### Что делать
1. **Конвертировать в WebP/AVIF** — экономия 30-50%
2. **Responsive images** — `srcset` для разных экранов
3. **Lazy-loading** — для фото ниже первого экрана
4. **CDN** — раздача с ближайшего сервера
5. **Compression** — lossless для фото, lossy для контента

### Плагины
- **Imagify** — автоконвертация
- **ShortPixel** — оптимизация
- **EWWW Image Optimizer** — бесплатный

---

## 💾 Кэширование

### Уровни
1. **Браузер** — Cache-Control заголовки
2. **Сервер** — WP Rocket или W3 Total Cache
3. **CDN** — Cloudflare или аналог
4. **Object cache** — Redis или Memcached

### Что кэшировать
- HTML страницы
- CSS и JS файлы
- Изображения
- API ответы

### Что НЕ кэшировать
- Корзина
- Личный кабинет
- Checkout
- Admin-панель

---

## 📦 Минификация

### CSS
- ✅ Уже минифицирован (402 КБ → нужно < 100 КБ)
- Critical CSS inline
- Остальное async

### JavaScript
- Elementor Pro: 200+ КБ
- jQuery: 90 КБ
- WooCommerce: 50+ КБ
- Robokassa widget: 50+ КБ

**Цель:** общий JS < 200 КБ

### Действия
- Удалить неиспользуемые скрипты
- Подключать Robokassa только на странице оплаты
- Defer/async для некритичных скриптов

---

## 🌐 CDN

### Что отдавать через CDN
- Статические файлы (CSS, JS, изображения)
- Шрифты (локально)
- Видео (если будут)

### Сервисы для РФ
- **Cloudflare** — бесплатный план
- **Selectel** — российский CDN
- **Timeweb CDN** — российский

---

## 🖼 Шрифты

### Проблема
- Google Fonts загружает с задержкой
- Privacy concerns

### Решение
1. **Локально** — положить шрифты в `/wp-content/fonts/`
2. **Preload** — `<link rel="preload" as="font">`
3. **Subset** — загружать только нужные символы
4. **font-display: swap** — показать fallback

---

## 🗜 Сжатие

### Gzip / Brotli
- Включить на сервере
- Экономия: 60-80% для текстовых файлов

### Настройки
```
nginx:
gzip on;
gzip_types text/css application/javascript image/svg+xml;
gzip_min_length 1000;
```

---

## 📊 Мониторинг

### Инструменты
- **PageSpeed Insights** — Google
- **GTmetrix** — детальный отчёт
- **WebPageTest** — водопад загрузки
- **Chrome DevTools** — локальная отладка

### Периодичность
- Проверять каждую неделю
- Настроить алерты (если Lighthouse < 80)

---

## 📋 Чек-лист оптимизации

### Срочно (P0)
- [ ] Оптимизировать все изображения
- [ ] Включить Gzip
- [ ] Включить кэширование
- [ ] Удалить дубль MAX-кнопки

### Важно (P1)
- [ ] Подключить CDN
- [ ] Перевести шрифты локально
- [ ] Удалить неиспользуемые плагины
- [ ] Минифицировать CSS/JS

### Желательно (P2)
- [ ] Service Worker (PWA)
- [ ] AMP для товаров
- [ ] HTTP/3

---

## 🔗 Связанные документы

- [Stack](07-Technical/Stack.md) — стек
- [Image-Optimization](Image-Optimization.md) — изображения
- [Caching](Caching.md) — кэширование
- [Hosting](Hosting.md) — хостинг

[⬅ MOC Tech](07-Technical/MOC-Tech.md) | [⬅ Главная](00-Inbox/README.md)