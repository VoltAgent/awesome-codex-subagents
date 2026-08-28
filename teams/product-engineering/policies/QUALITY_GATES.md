# Quality Gates

Use repository-native commands and only applicable gates:

1. format/static checks
2. lint
3. typecheck/compile
4. unit tests
5. integration tests
6. schema/migration validation
7. production build
8. startup/API smoke tests
9. E2E/browser runtime QA
10. independent correctness review
11. security review where applicable

Unavailable/skipped gates are BLOCKED or NOT_APPLICABLE, never PASS. Final completion requires no unresolved blocker/high review findings.
