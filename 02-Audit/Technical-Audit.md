# ⚙️ Технический аудит

> Стек, плагины, производительность, совместимость

---

## 🛠 Стек

| Слой | Технология | Версия |
|---|---|---|
| CMS | WordPress | — |
| Тема | Bono (WPSHOP) | 1.10.8 |
| Конструктор | Elementor + Elementor Pro | — |
| Магазин | WooCommerce | 10.8.1 |
| PHP | — | — |
| БД | MySQL | — |

**Размер CSS:** 402 КБ (минимизированный)
**Шрифты:** wpshop-core (иконочный), Roboto (Google Fonts), swiper-icons

---

## 🔌 Плагины

### Активные
| Плагин | Назначение | Оценка |
|---|---|---|
| akismet | Антиспам | ✅ стандарт |
| all-in-one-seo-pack-pro | SEO | 🟡 избыточный |
| bwd-dual-buttons | Двойные кнопки | 🟡 декоративный |
| cookie-bar | Cookie-уведомление | 🔴 спамный текст |
| customer-email-verification | Верификация email | 🟡 снижает конверсию |
| elementor / elementor-pro | Конструктор | ✅ основной |
| google-analytics-for-wordpress | GA | ✅ стандарт |
| max-ru-connect | MAX-кнопка | 🟡 дублируется |
| robokassa | Оплата | ✅ рабочий |
| woocommerce | Магазин | ✅ рабочий |
| woo-custom-product-addons-pro | Доп. поля | 🟡 избыточный |

**Итого:** 11 плагинов. Из них 5 избыточных/проблемных.

---

## 📊 Производительность

**Hero-картинка:** 173 КБ (gr.webp 1376×768) — оптимально ✅
**Логотип:** 28 КБ (gr-1.webp 200×182) — растровый, не SVG ⚠️
**Товарные фото:** 1-2 МБ оригиналы, есть ресайзы ✅
**CSS:** 402 КБ — избыточно для витрины из 6 товаров ⚠️

### Потенциальные проблемы
- Elementor Pro добавляет 200+ КБ JS
- WooCommerce blocks CSS загружается на всех страницах
- Robokassa widget загружается на каждой карточке

---

## 🚨 Технические баги

### Критические (P0)
1. **Schema.org `itemCondition: UsedCondition`** для новых товаров → Google может понизить в выдаче
2. **Meta description отключён темой** → пустой сниппет в Яндексе/Google
3. **Cookie-бар со спам-текстом** (замена кириллицы на латиницу) → антиспам обход
4. **Email `vandex` вместо `yandex`** на странице контактов → потеря писем
5. **Валидация форм отключена JS-патчем** → нет защиты от мусорных заявок
6. **Кнопка MAX продублирована** в body и в footer

### Средние (P1)
7. Schema.org `publisher.telephone` = `"ГРОМ"` (плейсхолдер)
8. Вариативный товар без выбранного размера → `variation_id=0`
9. Robokassa-виджет на каждой карточке, нет lazy-load
10. Нет `<meta name="theme-color">` адаптации

### Низкие (P2)
11. Elementor inline CSS дублируется
12. Robokassa `signature` в HTML → безопасность
13. WP speculationrules prefetch грузит много лишнего

---

## 🔗 Связанные документы

- [[../07-Technical/Stack|Стек — детали]]
- [[../07-Technical/Performance|Производительность]]
- [[Bugs-Баги]] — все баги
- [[Critical-Issues]] — только критические

[[MOC-Audit|⬅ MOC Audit]] | [[../README|⬅ Главная]]