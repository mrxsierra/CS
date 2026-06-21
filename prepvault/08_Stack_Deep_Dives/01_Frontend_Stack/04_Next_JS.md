---
title: Next.js & Server Side Patterns
tags: ['stack/frontend']
created: 2026-06-10
---

# Next.js & Server Side Patterns

## Overview
Next.js is the dominant React framework for production applications. In 2026 interviews, you're expected to understand its rendering strategies, data fetching patterns, and how it bridges client and server — not just "it's a React framework."

## The App Router (Next.js 13+)

### File-Based Routing
```
app/
├── page.tsx          → /
├── layout.tsx        → Root layout (wraps all pages)
├── about/
│   └── page.tsx      → /about
├── blog/
│   ├── page.tsx      → /blog
│   └── [slug]/
│       └── page.tsx  → /blog/:slug
├── api/
│   └── posts/
│       └── route.ts  → /api/posts (API route)
└── not-found.tsx     → 404 page
```

### Layouts — Persistent State
Layouts maintain state across navigations — they don't re-mount:
```tsx
// app/layout.tsx — Root layout (required)
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        <nav>{/* persistent nav */}</nav>
        {children}
        <footer>{/* persistent footer */}</footer>
      </body>
    </html>
  );
}
```

## Rendering Strategies

| Strategy | When | Data Freshness | Bundle Size |
|----------|------|----------------|-------------|
| **SSR** (Dynamic) | Personalized content per request | Always fresh | Full JS sent |
| **SSG** (Static) | Marketing pages, blogs | Build-time only | Minimal |
| **ISR** (Incremental Static Regeneration) | Content that changes periodically (CMS) | Revalidates on demand | Minimal |
| **RSC** (Server Components) | Data-heavy pages, DB access | Per request | Zero client JS |

### Server Components vs. Client Components
```tsx
// Server Component (default in App Router)
async function Post({ id }: { id: string }) {
  const post = await db.post.findUnique({ where: { id } }); // Direct DB!
  return <article>{post.title}</article>; // Zero JS sent to browser
}

// Client Component — marked with 'use client'
'use client';
function LikeButton({ postId }: { postId: string }) {
  const [liked, setLiked] = useState(false);
  return <button onClick={() => setLiked(!liked)}>❤️</button>;
}
```

### Data Fetching Patterns
```tsx
// Parallel fetching in Server Components
async function Dashboard() {
  const [user, posts, analytics] = await Promise.all([
    getUser(), getPosts(), getAnalytics()
  ]);
  return <div>{/* render */}</div>;
}

// Streaming with Suspense
function Page() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<Skeleton />}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```

## Caching & Revalidation
- **`fetch()`** is cached by default (Deduplicated + Persistent HTTP cache)
- **`revalidate`**: `fetch(url, { next: { revalidate: 60 } })` — ISR-style revalidation
- **`noStore()`**: Opt-out of caching for dynamic data
- **`unstable_cache`**: Custom cache with tags for manual revalidation

## Advanced Patterns

### Middleware — Edge Functions
```tsx
// middleware.ts — runs at the edge before every request
export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');
  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}

export const config = { matcher: ['/dashboard/:path*', '/admin/:path*'] };
```

### Route Handlers (API Routes in App Router)
```tsx
// app/api/posts/route.ts
export async function GET() {
  const posts = await db.post.findMany();
  return Response.json(posts);
}

export async function POST(request: Request) {
  const body = await request.json();
  const post = await db.post.create({ data: body });
  return Response.json(post, { status: 201 });
}
```

### Image & Font Optimization
```tsx
import Image from 'next/image';
// Automatic: lazy loading, responsive sizes, WebP conversion, CLS prevention
<Image src="/hero.jpg" alt="Hero" width={1200} height={600} priority />

import { Inter } from 'next/font/google';
const inter = Inter({ subsets: ['latin'], display: 'swap' });
```

## Common Interview Questions

1. **"How does Next.js differ from a plain React SPA?"** — SSR/SSG/ISR, file-based routing, API routes, middleware, image optimization, RSC

2. **"What is the difference between Server Components and Client Components?"** — Server Components render on the server, send zero JS to the client, can access DBs/files directly. Client Components hydrate in the browser, use hooks/state/effects.

3. **"How do you handle authentication in Next.js?"** — Middleware for route protection, Server Component checks for SSR, `next-auth` for OAuth providers, JWT or session cookies

4. **"Explain how ISR works."** — At build time, pages are generated statically. On first request after `revalidate` time, the server serves the cached page and triggers a background regeneration. 

## Related Topics
- [[08_Stack_Deep_Dives/01_Frontend_Stack/03_React|React Mastery]]
- [[08_Stack_Deep_Dives/01_Frontend_Stack/Index|Frontend Stack Index]]
- [[02_Role_Tracks/02_Frontend_Engineer|Frontend Engineer Track]]

## Resources
- [Next.js Official Docs](https://nextjs.org/docs)
- [Next.js Learn Course](https://nextjs.org/learn)