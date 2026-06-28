# 🧬 Schema.org аудит

> Микроразметка и структурированные данные

---

## 📋 Что есть (типы)

| Тип | Где | Статус |
|---|---|---|
| Organization | Главная | ⚠️ есть, но с ошибками |
| WebSite | Главная | ✅ корректно |
| BreadcrumbList | Карточки | ✅ корректно |
| Product | Карточки товаров | 🔴 критические ошибки |
| Offer | Карточки | 🔴 ошибки |
| Brand | Карточки | ✅ есть |
| ImageObject | Все фото | ✅ есть |

---

## 🚨 Критические ошибки (исправить немедленно)

### 1. `itemCondition: "UsedCondition"` для новых товаров

```json
❌ НЕПРАВИЛЬНО:
{
  "itemCondition": "https://schema.org/UsedCondition"
}
```

```json
✅ ПРАВИЛЬНО:
{
  "itemCondition": "https://schema.org/NewCondition"
}
```

**Влияние:** Google может показывать предупреждение в Search Console и понизить рейтинг.

---

### 2. `publisher.telephone` = строка `"ГРОМ"`

```json
❌ НЕПРАВИЛЬНО:
{
  "publisher": {
    "telephone": "ГРОМ"  // ← это не телефон!
  }
}
```

```json
✅ ПРАВИЛЬНО: убрать поле или поставить реальный номер
{
  "publisher": {
    "telephone": "+79025761917"
  }
}
```

---

### 3. Пустые `Product.description`

```json
❌ НЕПРАВИЛЬНО:
{
  "Product": {
    "name": "Лезвие \"ГРОМ\" неокрашенное",
    "description": ""
  }
}
```

**Решение:** заполнить описания для всех 6 товаров.

---

### 4. `Offer.seller.name = "ГРОМ"` (без организационно-правовой формы)

```json
⚠️ ЛУЧШЕ:
{
  "seller": {
    "name": "ООО «ГРОМ»",
    "url": "https://гром38.рф"
  }
}
```

---

## 🟡 Средние проблемы

### 5. `priceValidUntil: "2027-12-31"` — слишком далеко

Лучше указывать `2026-12-31` или вообще убрать (Google считает валидность 1 год).

### 6. `OfferCount: 2`, `highPrice: 6600`, `lowPrice: 6600` — дубль

Если у товара один вариант по одной цене, `AggregateOffer` не нужен — достаточно `Offer`.

### 7. Нет `AggregateRating` при 0 отзывов

✅ Правильно — не выводить, если 0. Но **план**: запустить сбор отзывов и добавить через 2-3 месяца.

---

## 🔵 Чего не хватает (потенциал)

### `FAQPage` (для категорий и карточек)

```json
{
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Как выбрать размер лезвия?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Под ботинок 38-42 — лезвие 480 мм, под 43-46 — 520 мм..."
    }
  }]
}
```

### `HowTo` (для статей блога)

```json
{
  "@type": "HowTo",
  "name": "Как установить лезвие ГРОМ",
  "step": [...]
}
```

### `LocalBusiness` (для контактов)

```json
{
  "@type": "SportingGoodsStore",
  "name": "ГРОМ",
  "address": {...},
  "geo": {"latitude": 52.52, "longitude": 103.90},
  "openingHours": "Mo-Sa 10:00-17:00"
}
```

### `VideoObject` (для видео-обзоров)

### `Review` (для отзывов с фото)

---

## ✅ Исправленный шаблон Product

```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Лезвие «ГРОМ» неокрашенное",
  "description": "Стальное лезвие для открытого льда. Подходит для ботинок NNN/SNS...",
  "image": [
    "https://гром38.рф/wp-content/uploads/2026/03/lg-1.webp",
    "https://гром38.рф/wp-content/uploads/2026/03/lg-2.webp"
  ],
  "sku": "003",
  "mpn": "GROM-BLD-003",
  "brand": {
    "@type": "Brand",
    "name": "ГРОМ",
    "logo": "https://гром38.рф/logo.svg"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://гром38.рф/product/lezvie-grom-neokrashennoe/",
    "priceCurrency": "RUB",
    "price": "6600",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "seller": {
      "@type": "Organization",
      "name": "ООО «ГРОМ»",
      "url": "https://гром38.рф"
    }
  }
}
```

---

## 🛠 План внедрения

### P0 (на этой неделе)
1. Исправить `itemCondition` во всех 6 товарах
2. Убрать/исправить `publisher.telephone`
3. Добавить `seller.name = "ООО «ГРОМ»"`

### P1 (в течение месяца)
4. Добавить `LocalBusiness` на страницу контактов
5. Добавить `FAQPage` на категории
6. Подготовить шаблоны для будущих типов

### P2 (по мере наполнения)
7. `AggregateRating` после сбора 5+ отзывов
8. `Review` для каждого отзыва с фото
9. `VideoObject` для видео-обзоров

---

## 🔗 Связанные документы

- [SEO-Audit](SEO-Audit.md) — общий SEO-аудит
- [Technical-Audit](Technical-Audit.md) — технические баги
- [Технический фикс Schema](../07-Technical/Schema-Fix.md)
- [Bugs-Баги](Bugs-Баги.md) — все баги

[⬅ MOC Audit](MOC-Audit.md) | [⬅ Главная](../00-Inbox/README.md)