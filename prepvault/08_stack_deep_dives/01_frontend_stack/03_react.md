---
title: React Mastery
tags: ['stack/frontend']
created: 2026-06-10
---

# React Mastery

## Overview
React is the #1 framework tested in frontend interviews. You need to demonstrate deep understanding of its core architecture (not just API usage): reconciliation, fiber, hooks, and rendering behavior.

## Core Architecture

### Virtual DOM & Reconciliation
React maintains a lightweight representation of the real DOM in memory. When state changes, it:
1. Renders a new Virtual DOM tree
2. **Diffs** it against the previous tree (reconciliation)
3. Calculates the minimal set of DOM mutations
4. Applies them in a **commit phase**

**Keys** are essential for correct reconciliation — they help React identify which children changed:
```jsx
{items.map(item => <ListItem key={item.id} item={item} />)}
// Bad: {items.map((item, i) => <ListItem key={i} item={item} />)}
```
Using index as key breaks reconciliation when items are reordered or removed.

### React Fiber (React 16+)
The Fiber architecture enables **interruptible rendering**:
- **Rendering** can be paused and resumed (time-slicing)
- Priority-based scheduling — urgent updates (user input) beat background ones (data loading)
- Enables Concurrent Features: `startTransition`, `useDeferredValue`, `Suspense`

## Hooks — Deep Understanding

### `useState`
State is stored per-component-instance. The setter triggers a re-render.
```javascript
const [count, setCount] = useState(0);
// Functional update to avoid stale closures:
setCount(prev => prev + 1);
```

### `useEffect`
Runs **after** the browser paints. Three dependency patterns:
| Dependencies | Runs |
|-------------|------|
| `[]` | Once on mount (cleanup on unmount) |
| `[dep1, dep2]` | When any dependency changes |
| Omitted | Every render (rarely correct) |

**Cleanup function**: Return a function from useEffect to unsubscribe / cancel / clean up:
```javascript
useEffect(() => {
  const subscription = source.subscribe();
  return () => subscription.unsubscribe(); // runs on unmount + before re-run
}, []);
```

### `useMemo` & `useCallback`
Optimization tools — not free. Use only when computation is expensive or referential equality matters.
```javascript
const sortedList = useMemo(() => {
  return items.sort((a, b) => a.name.localeCompare(b.name));
}, [items]);

const handleClick = useCallback(() => {
  dispatch({ type: 'CLICK' });
}, [dispatch]);
```

### Custom Hooks
Extract reusable stateful logic:
```javascript
function useWindowSize() {
  const [size, setSize] = useState({ width: window.innerWidth, height: window.innerHeight });
  useEffect(() => {
    const handler = () => setSize({ width: window.innerWidth, height: window.innerHeight });
    window.addEventListener('resize', handler);
    return () => window.removeEventListener('resize', handler);
  }, []);
  return size;
}
```

## State Management Landscape

| Solution | Best for | Notes |
|----------|----------|-------|
| **`useState` + lifting** | Simple parent-child sharing | No extra deps |
| **Context API** | Global themes, auth, locale | Causes re-renders in all consumers |
| **Zustand** | Small to medium apps | Minimal boilerplate, no provider needed |
| **Redux Toolkit** | Large apps with complex state | RTK Query for data fetching |
| **TanStack Query** | Server state / caching | Auto cache invalidation, background refetching |

## React Server Components (RSC) — 2026 Standard
- **Server Components** run on the server, send zero JS to the client
- **Client Components** are marked with `'use client'` — they hydrate in the browser
- **Benefits**: Smaller bundles, direct DB access, automatic code splitting

```tsx
// This is a Server Component (default in Next.js App Router)
async function PostList() {
  const posts = await db.posts.findMany(); // Direct DB access!
  return (
    <div>
      {posts.map(post => <PostCard key={post.id} post={post} />)}
    </div>
  );
}
```

## Common Interview Questions

### "Build a search autocomplete"
```javascript
function SearchAutocomplete() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  
  // Debounce the API call
  useEffect(() => {
    if (query.length < 2) return;
    const timer = setTimeout(async () => {
      const res = await fetch(`/api/search?q=${query}`);
      setResults(await res.json());
    }, 300);
    return () => clearTimeout(timer); // cancel stale requests
  }, [query]);
  
  return ( /* render results with keyboard navigation */ );
}
```

### "Why does `useEffect` run twice in development?"
React 18 Strict Mode intentionally double-invokes effects in development to help find bugs with missing cleanup functions.

### "How does React batch state updates?"
In React 18, all state updates (including inside `setTimeout`, Promises, and native events) are automatically batched. In React 17, only event handlers batched.

## Performance Patterns
- **`React.memo`**: Prevents re-render if props haven't changed (shallow comparison)
- **Virtualization**: `react-window` or `@tanstack/virtual` for long lists
- **Code Splitting**: `React.lazy(() => import('./Component'))` + `<Suspense>`
- **`useTransition`**: Mark non-urgent state updates as interruptible

## Related Topics
- [[08_stack_deep_dives/01_frontend_stack/04_next_js|Next.js & Server Side Patterns]]
- [[08_stack_deep_dives/01_frontend_stack/02_javascript_ts|JavaScript & TypeScript]]
- [[08_stack_deep_dives/01_frontend_stack/index|Frontend Stack Index]]
- [[02_role_tracks/02_frontend_engineer|Frontend Engineer Track]]

## Resources
- [React Official Docs](https://react.dev)
- [React 18 Deep Dive (Dan Abramov)](https://react.dev/blog/2022/03/29/react-v18)
- [Beta React Docs](https://react.dev)