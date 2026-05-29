# Stack Detection Guide

Prefer evidence order:
1. Manifest files
2. Lockfiles
3. Build/dependency files
4. Source layout and entry points
5. CI/CD configuration
6. Container/orchestration config
7. Documentation claims

Never let documentation claims override direct implementation evidence.

## Ecosystems
- Node.js / JavaScript / TypeScript: `package.json`, lockfiles, `tsconfig.json`, `vite.config.*`, `next.config.*`.
- Python: `pyproject.toml`, `requirements*.txt`, `Pipfile`, `setup.py`, app entry files.
- Go: `go.mod`, `go.sum`, `cmd/`, `main.go`.
- Rust: `Cargo.toml`, `Cargo.lock`, `src/main.rs`, workspace members.
- Java / Kotlin: `pom.xml`, `build.gradle*`, multi-module settings.
- .NET: `*.csproj`, `*.sln`, `Directory.Build.*`.
- PHP: `composer.json`, `composer.lock`, framework bootstrap files.
- Ruby: `Gemfile`, `Gemfile.lock`, app structure conventions.
- Swift: `Package.swift`, Xcode project/workspace files.
- Dart / Flutter: `pubspec.yaml`, `lib/main.dart`.
- Android: `app/build.gradle*`, `AndroidManifest.xml`.
- iOS: `Info.plist`, Xcode project/workspace structure.
- Docker-based apps: `Dockerfile`, `docker-compose.*`, env templates.

## Monorepos and polyglot repos
- Detect workspace tools (`pnpm-workspace.yaml`, `turbo.json`, `nx.json`, multi-module build files).
- Inspect package-level manifests under `apps/`, `packages/`, `services/`, or equivalent.
- Do not assume root manifest represents all services.
- Report stack per package/service when heterogeneous.
