---
type: concept
tags: [foundations, debugging, testing, quality]
created: 2026-06-10
---

# The Debugging & Test-First Mindset

Writing code is only $30\%$ of the job. The remaining $70\%$ is verification and maintenance. In the 2026-27 market, engineers are hired for their ability to fix systems, not just build them.

## 1. The Systematic Debugging Flow
When a bug occurs, do not start changing code randomly. Follow this framework:

```
  [Reproduce] ──► [Locate] ──► [Isolate] ──► [Fix] ──► [Verify]
```

1. **Reproduce**: Write a minimal failing test case that reliably triggers the bug. If you can't reproduce it, you can't prove you fixed it.
2. **Locate**: Examine stack traces, application logs, and resource usage timelines (CPU/Memory spikes).
3. **Isolate**: Narrow down the source of error by mocking upstream dependencies or isolating variables.
4. **Fix**: Apply a targeted patch that resolves the root issue without introducing side-effects.
5. **Verify**: Run the full test suite to confirm the bug is resolved and that overall code coverage remains intact.

## 2. Test-First Mindset (TDD & BDD)
A test-first approach ensures that your code is modular, verifiable, and documented by default.

### Unit Testing with Mocks
Isolation is key to effective unit testing. Use mocks to simulate external dependencies (Databases, APIs) so you only test the logic of the component in question.

```typescript
// Example: Mocking a Repository in Jest
import { UserService } from './UserService';
import { UserRepository } from './UserRepository';

jest.mock('./UserRepository');

describe('UserService', () => {
  it('should hash passwords before saving', async () => {
    const mockRepo = new UserRepository() as jest.Mocked<UserRepository>;
    const service = new UserService(mockRepo);
    
    await service.register('test@example.com', 'raw_password');
    
    expect(mockRepo.save).toHaveBeenCalledWith(
      expect.objectContaining({
        password: expect.not.stringContaining('raw_password')
      })
    );
  });
});
```

### Coverage Metrics
- **Line Coverage**: Percent of code lines executed by tests.
- **Branch Coverage**: Percent of logic branches (if/else) tested.
- **Function Coverage**: Percent of functions called by tests.
*Aim for $80\%+$ coverage on business logic.*

## 3. Advanced Verification Techniques
- **Integration Testing**: Testing how multiple components work together (e.g., API + Database).
- **Chaos Engineering**: Deliberately introducing failures (e.g., killing a server) to see how the system reacts.
- **Static Analysis**: Using linters (ESLint) and type-checkers (TypeScript) to catch bugs before execution.

## Role-Specific Applications
- **[[02_role_tracks/02_frontend_engineer|Frontend]]**: Unit testing components with React Testing Library, E2E testing with Playwright.
- **[[02_role_tracks/03_backend_engineer|Backend]]**: Mocking external services, testing database migrations, load testing.
- **[[02_role_tracks/05_devops_engineer|DevOps]]**: Testing infrastructure-as-code (Terratest), validating CI/CD pipeline health.

## Related Topics
- [[01_foundations/02_sdlc|SDLC & DevOps]]
- [[01_foundations/03_system_design|System Design]]
- [[01_foundations/07_language_internals/index|Language Internals]]
