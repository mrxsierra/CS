---
title: HTML & CSS Deep Dive
tags: ['stack/frontend']
created: 2026-06-10
---

# HTML & CSS Deep Dive

## Overview
HTML and CSS are the foundation of every web interface. In frontend interviews, you're expected to demonstrate deep understanding of semantic markup, layout algorithms, accessibility, and modern CSS features — not just "make it look right."

## HTML — Semantic Structure & Accessibility

### Semantic HTML
Using correct elements conveys meaning to browsers, screen readers, and search engines.

| Element | Purpose | Avoid |
|---------|---------|-------|
| `<header>` | Introductory content / navigation | `<div class="header">` |
| `<nav>` | Navigation links | `<div class="nav">` |
| `<main>` | Primary page content (one per page) | `<div id="main">` |
| `<article>` | Self-contained composition | `<div class="post">` |
| `<section>` | Thematic grouping of content | `<div class="section">` |
| `<aside>` | Tangentially related content | `<div class="sidebar">` |
| `<figure>` | Self-contained content (diagrams, code) | `<div class="image">` |

### Accessibility (WCAG)
- **ARIA Roles**: `role="button"`, `role="alert"`, `role="dialog"` — only use when native HTML semantics are insufficient
- **Focus Management**: Ensure interactive elements are focusable (`tabindex`, `:focus-visible`)
- **Screen Readers**: `aria-label`, `aria-describedby`, `aria-live` for dynamic content
- **Color Contrast**: Minimum 4.5:1 for normal text, 3:1 for large text

### Interview Question: "Build an accessible dropdown"
```html
<label for="city">City</label>
<select id="city" aria-describedby="city-desc">
  <option>New York</option>
  <option>San Francisco</option>
</select>
<p id="city-desc">Select your primary city</p>
```

## CSS — Layout, Specificity & Modern Features

### The Box Model
```
┌─────────────────────────────┐
│          Margin             │
│  ┌───────────────────────┐  │
│  │       Border          │  │
│  │  ┌─────────────────┐  │  │
│  │  │    Padding       │  │  │
│  │  │  ┌───────────┐   │  │  │
│  │  │  │  Content  │   │  │  │
│  │  │  └───────────┘   │  │  │
│  │  └─────────────────┘  │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
```
- `box-sizing: border-box` — includes padding + border in width calculation (recommended)
- `box-sizing: content-box` — default; padding + border add to width

### Flexbox vs. Grid

| Property | Flexbox | Grid |
|----------|---------|------|
| Dimension | 1D (row **or** column) | 2D (rows **and** columns) |
| Use case | Navigation bars, centering, card rows | Page layouts, complex alignments |
| Main axis | `justify-content` | `justify-items` / `justify-content` |
| Cross axis | `align-items` | `align-items` / `align-content` |

### CSS Specificity (The Cascade)
Ranked from highest to lowest:
1. **Inline styles** (`style="..."`)
2. **IDs** (`#header`)
3. **Classes / Attributes / Pseudo-classes** (`.nav`, `[type]`, `:hover`)
4. **Elements / Pseudo-elements** (`div`, `::before`)

> **Avoid `!important`** — it breaks the cascade and makes debugging a nightmare.

### Modern CSS Features (2026)
- **CSS Custom Properties (Variables)**: `--primary: #6c63ff; color: var(--primary);`
- **Container Queries**: `@container (min-width: 400px) { ... }` — component-level responsiveness
- **`:has()` selector**: Parent-selector — `div:has(> p)` targets divs that directly contain `<p>`
- **`@layer`**: Explicit cascade layers to manage third-party CSS conflicts
- **View Transitions API**: Smooth page transitions with `document.startViewTransition()`

### Interview Question: "Center a div (the classic)"
```css
/* Method 1: Flexbox */
.parent { display: flex; justify-content: center; align-items: center; }

/* Method 2: Grid */
.parent { display: grid; place-items: center; }

/* Method 3: Absolute positioning + transform */
.child { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
```

### Interview Question: "Build a responsive card grid"
```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}
```
This creates a responsive grid where cards are at least 300px wide and expand to fill available space.

## Performance & Rendering
- **Critical Rendering Path**: HTML → DOM → CSSOM → Render Tree → Layout → Paint → Composite
- **`will-change`**: Hints the browser to prepare for changes — use sparingly
- **`content-visibility: auto`**: Defers off-screen rendering (lazy rendering)
- **`contain`**: Isolates a subtree to limit style/layout recalculation scope

## Common Interview Patterns
1. **Build a responsive navbar** — Hamburger menu on mobile, horizontal on desktop
2. **CSS art / shapes** — Triangles using borders, circles with `border-radius: 50%`
3. **Complex form styling** — Custom checkboxes, range sliders, file uploads
4. **Animation performance** — `transform` + `opacity` only (GPU-composited); avoid animating `width`, `height`, `top`, `left`

## Related Topics
- [[08_Stack_Deep_Dives/01_Frontend_Stack/02_JavaScript_TS|JavaScript & TypeScript]]
- [[08_Stack_Stack_Deep_Dives/01_Frontend_Stack/Index|Frontend Stack Index]]
- [[02_Role_Tracks/02_Frontend_Engineer|Frontend Engineer Track]]

## Resources
- [MDN HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [CSS Tricks Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)