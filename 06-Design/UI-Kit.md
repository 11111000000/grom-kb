# 🧩 UI-Kit

> Компоненты пользовательского интерфейса

---

## 🔘 Кнопки

### Типы

| Тип | Фон | Текст | Hover | Использование |
|---|---|---|---|---|
| Primary | `#f4b942` (Accent) | `#1e2f3a` | `#e0a830` | Главный CTA |
| Secondary | `#1e4a62` | `#ffffff` | `#0d2837` | Вторичный CTA |
| Outline | прозрачный | `#1e4a62` | `#f8fafc` | Третичный |
| Ghost | прозрачный | `#1e4a62` | `#f8fafc` | В навигации |
| Danger | `#ef4444` | `#ffffff` | `#dc2626` | Удаление |
| Disabled | `#dce8ef` | `#6e8b9e` | — | Неактивна |

### Размеры

| Размер | Высота | Padding | Шрифт |
|---|---|---|---|
| Small | 32px | 12px 16px | 14px |
| Default | 40px | 12px 24px | 16px |
| Large | 48px | 14px 28px | 16px |
| XL | 56px | 16px 32px | 18px |

### Скругления
- 8px — стандарт
- 12px — крупные
- 24px — pill (капсула)
- 9999px — круг

---

## 📝 Формы

### Input (текстовое поле)

```
Состояния:
- Default: border #dce8ef
- Focus: border #1e4a62, ring 3px #9fc2e8
- Error: border #ef4444
- Disabled: bg #f8fafc

Размеры:
- Default: 48px height
- Small: 36px height

Стиль:
- Скругление: 8px
- Padding: 12px 16px
- Шрифт: Inter Regular 16px
```

### Label
```
Шрифт: Inter Medium 500, 14px
Цвет: #4d6e82
Margin-bottom: 6px
```

### Helper text
```
Шрифт: Inter Regular 400, 12px
Цвет: #4d6e82 (default), #ef4444 (error)
Margin-top: 4px
```

### Checkbox / Radio
```
Размер: 20px
Цвет галочки: #ffffff
Фон checked: #1e4a62
Border unchecked: #dce8ef
```

---

## 🃏 Карточки

### Карточка товара

```
Структура:
┌─────────────────────┐
│  [Бейдж]            │  ← top-left: "Хит", "Новинка"
│                     │
│  [Фото товара]      │  ← aspect-ratio 1:1 или 4:3
│                     │
│                     │
├─────────────────────┤
│  Название           │  ← TT Norms Pro 18px
│                     │
│  Цена          ⭐   │  ← Inter SemiBold 20px + иконка
│                     │
│  [В корзину]        │  ← кнопка primary
└─────────────────────┘

Стиль:
- Фон: #ffffff
- Border-radius: 16px
- Border: 1px solid #dce8ef
- Hover: тень 0 4px 16px rgba(0,0,0,0.08)
- Transition: 0.2s ease
```

### Информационная карточка

```
Использование: преимущества, услуги
Фон: #ffffff
Padding: 24px
Скругление: 16px
Тень: 0 2px 8px rgba(0,0,0,0.04)
```

---

## 🏷 Бейджи

| Тип | Фон | Текст | Использование |
|---|---|---|---|
| Hit (Хит) | `#f4b942` | `#1e2f3a` | Популярный товар |
| New (Новинка) | `#22c55e` | `#ffffff` | Новый товар |
| Sale (Скидка) | `#ef4444` | `#ffffff` | Распродажа |
| Pre-order | `#3b82f6` | `#ffffff` | Под заказ |
| Out of stock | `#6e8b9e` | `#ffffff` | Нет в наличии |

**Размер:** height 24px, padding 0 12px, скругление 12px

---

## 🧭 Навигация

### Header
```
Высота: 80px (desktop), 64px (mobile)
Фон: #ffffff
Border-bottom: 1px solid #dce8ef
Sticky: да
Структура:
[Логотип] [Меню] ... [Поиск] [Избранное] [Корзина] [Профиль]
```

### Меню
```
Шрифт: Inter Medium 500, 16px
Цвет default: #1e2f3a
Цвет hover: #1e4a62
Цвет active: #1e4a62 + нижнее подчёркивание 2px
```

### Dropdown
```
Фон: #ffffff
Тень: 0 8px 24px rgba(0,0,0,0.12)
Скругление: 12px
Padding: 8px
Min-width: 240px
```

---

## 🪟 Модалки

```
Фон: rgba(30, 74, 98, 0.5) (backdrop)
Скругление: 16px
Padding: 32px
Max-width: 480px (default), 640px (large)
Центрирование: flexbox
Animation: fade + scale
```

---

## 🔔 Уведомления (Toast)

```
Позиция: top-right
Padding: 12px 16px
Скругление: 8px
Цвета:
- Success: #22c55e bg, #ffffff text
- Error: #ef4444 bg, #ffffff text
- Info: #3b82f6 bg, #ffffff text
- Warning: #eab308 bg, #1e2f3a text
Animation: slide-in-right
Duration: 4 сек
```

---

## 📊 Таблицы

```
Header: фон #f8fafc, текст #4d6e82, шрифт Medium 14px
Row: фон #ffffff, чётные row #f8fafc
Hover: фон #e8f1f7
Border-bottom: 1px solid #dce8ef
Padding: 12px 16px
```

---

## 🎚 Слайдер (Range)

```
Track: 4px height, bg #dce8ef
Заполнение: bg #f4b942
Thumb: 20px circle, bg #ffffff, border 2px #1e4a62
Hover: thumb увеличивается до 24px
```

---

## 🔢 Числовой input (Quantity)

```
Структура: [-] [  1  ] [+]
Кнопки: 40x40px
Input: 60px width, центрирование
Border: 1px solid #dce8ef
```

---

## 📱 Мобильные компоненты

### Bottom Sheet
```
Фон: #ffffff
Скругление top: 16px
Padding: 16px
Max-height: 90vh
Drag-handle: 4px × 40px, #dce8ef, центрирован
```

### Hamburger Menu
```
Размер: 24x24px
3 полоски: 2px height, 20px width, gap 4px
Цвет: #1e2f3a
```

---

## 🎯 Чек-лист компонента

Перед добавлением в UI-kit проверить:
- [ ] Адаптивность (mobile, tablet, desktop)
- [ ] Все состояния (default, hover, focus, disabled, error)
- [ ] Доступность (ARIA-атрибуты)
- [ ] Контраст (WCAG)
- [ ] Анимация (плавная, не раздражающая)
- [ ] Документация (как использовать)

---

## 🔗 Связанные документы

- [Brand-Identity](06-Design/Brand-Identity.md)
- [Color-Palette](06-Design/Color-Palette.md)
- [Typography](06-Design/Typography.md)
- [Buttons](Buttons.md) — детально
- [Forms](Forms.md) — детально

[⬅ MOC Design](06-Design/MOC-Design.md) | [⬅ Главная](00-Inbox/README.md)