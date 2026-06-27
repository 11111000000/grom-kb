# 🧬 Schema.org — технический фикс

> Пошаговое руководство по исправлению микроразметки

---

## 🎯 Зачем

Schema.org помогает Google и Яндексу:
- Лучше понять структуру страницы
- Формировать расширенные сниппеты
- Улучшать позиции в выдаче

---

## 🚨 Текущие ошибки

### 1. UsedCondition для новых товаров

**Файл:** все 6 карточек товаров
**Найти:** `grep -r "UsedCondition" /wp-content/themes/bono/`
**Заменить на:** `NewCondition`

### 2. publisher.telephone = "ГРОМ"

**Файл:** `header.php` или подобный
**Удалить поле** или заменить на реальный номер

### 3. Пустой Product.description

**Файл:** каждый товар в админке WP
**Заполнить** в поле "Описание товара"

---

## ✅ Эталонный шаблон Product

```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Лезвие «ГРОМ» неокрашенное",
  "description": "Стальное лезвие для открытого льда, разработанное и произведённое в Ангарске. Подходит для лыжных ботинок NNN и SNS. Длина 480 мм для ботинок 38-42.",
  "image": [
    "https://гром38.рф/wp-content/uploads/2026/03/lg-1-1200x.webp",
    "https://гром38.рф/wp-content/uploads/2026/03/lg-2-1200x.webp",
    "https://гром38.рф/wp-content/uploads/2026/03/lg-3-1200x.webp"
  ],
  "sku": "003",
  "mpn": "GROM-BLD-003-UN",
  "brand": {
    "@type": "Brand",
    "name": "ГРОМ",
    "logo": "https://гром38.рф/wp-content/uploads/2026/logo-grom.svg"
  },
  "category": "Лезвия для озёрных коньков",
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
    },
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingDestination": {
        "@type": "DefinedRegion",
        "addressCountry": "RU"
      },
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "handlingTime": {
          "@type": "QuantitativeValue",
          "minValue": 1,
          "maxValue": 2,
          "unitCode": "DAY"
        },
        "transitTime": {
          "@type": "QuantitativeValue",
          "minValue": 3,
          "maxValue": 7,
          "unitCode": "DAY"
        }
      }
    }
  }
}
```

---

## 🏢 Organization (footer / главная)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "ООО «ГРОМ»",
  "alternateName": "ГРОМ",
  "url": "https://гром38.рф",
  "logo": {
    "@type": "ImageObject",
    "url": "https://гром38.рф/wp-content/uploads/2026/logo-grom.svg",
    "width": 600,
    "height": 200
  },
  "description": "Российский производитель озёрных коньков (байсов) из Ангарска",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Проспект Карла Маркса, 87/10",
    "addressLocality": "Ангарск",
    "addressRegion": "Иркутская область",
    "postalCode": "665832",
    "addressCountry": "RU"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+7-902-576-19-17",
    "contactType": "customer service",
    "areaServed": "RU",
    "availableLanguage": "Russian"
  },
  "sameAs": [
    "https://vk.com/grom38",
    "https://t.me/grom38",
    "https://youtube.com/@grom38"
  ],
  "foundingDate": "2025",
  "founder": {
    "@type": "Person",
    "name": "Основатель ГРОМ"
  }
}
```

---

## 🏬 LocalBusiness (для контактов)

```json
{
  "@context": "https://schema.org",
  "@type": "SportingGoodsStore",
  "name": "ГРОМ",
  "image": "https://гром38.рф/wp-content/uploads/2026/shop-photo.webp",
  "url": "https://гром38.рф",
  "telephone": "+7-902-576-19-17",
  "email": "info@grom38.ru",
  "priceRange": "₽₽",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Проспект Карла Маркса, 87/10",
    "addressLocality": "Ангарск",
    "addressRegion": "Иркутская область",
    "postalCode": "665832",
    "addressCountry": "RU"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 52.520564311032416,
    "longitude": 103.90419704561606
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "10:00",
      "closes": "17:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "10:00",
      "closes": "15:00"
    }
  ]
}
```

---

## ❓ FAQPage (для категорий)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Как выбрать размер лезвия?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Под ботинок 38-42 размера выбирайте лезвие 480 мм, под 43-46 — 520 мм. Наш калькулятор размера поможет определить точно."
      }
    },
    {
      "@type": "Question",
      "name": "Какие ботинки подходят для байсов ГРОМ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Любые лыжные ботинки с креплениями NNN или SNS. Это все ботинки для конькового хода от Salomon, Atomic, Fischer, Rossignol и др."
      }
    },
    {
      "@type": "Question",
      "name": "Сколько по времени доставка?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "По РФ — 3-7 дней СДЭК. По Ангарску — самовывоз в день заказа."
      }
    }
  ]
}
```

---

## 🍞 BreadcrumbList (везде)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Главная",
      "item": "https://гром38.рф"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Каталог",
      "item": "https://гром38.рф/product-category/grom/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Лезвие «ГРОМ» неокрашенное",
      "item": "https://гром38.рф/product/lezvie-grom-neokrashennoe/"
    }
  ]
}
```

---

## 🛠 Как внедрять

### Вариант 1: Вручную в `header.php`

```php
<?php if (is_product()): ?>
<script type="application/ld+json">
<?php echo json_encode(get_product_schema()); ?>
</script>
<?php endif; ?>
```

### Вариант 2: Плагин

- **Schema Pro** — платный, хороший
- **RankMath** — бесплатный, с Schema
- **WP SEO Structured Data Schema** — бесплатный

### Вариант 3: В коде темы

В `functions.php`:

```php
function get_product_schema() {
  global $product;
  return [
    '@context' => 'https://schema.org/',
    '@type' => 'Product',
    'name' => $product->get_name(),
    'description' => $product->get_description(),
    // ...
  ];
}
```

---

## ✅ Проверка после внедрения

### Инструменты
1. **Google Rich Results Test** — https://search.google.com/test/rich-results
2. **Schema.org Validator** — https://validator.schema.org/
3. **Яндекс.Вебмастер** — https://webmaster.yandex.ru/
4. **Google Search Console** — Улучшения → Товары

### Чек-лист
- [ ] Все товары проходят Rich Results Test без ошибок
- [ ] Organization отображается
- [ ] FAQPage валидна
- [ ] BreadcrumbList работает
- [ ] Нет ошибок в Search Console
- [ ] Нет предупреждений в Вебмастере

---

## 🔗 Связанные документы

- [Schema-Audit](02-Audit/Schema-Audit.md)
- [SEO-Tech](07-Technical/SEO-Tech.md) — техническое SEO
- [Баги](02-Audit/Bugs-Баги.md)

[⬅ MOC Tech](07-Technical/MOC-Tech.md) | [⬅ Главная](00-Inbox/README.md)