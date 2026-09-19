# sncloud-fixture-fastapi

An **SN Cloud acceptance fixture** for DEC-001 AC-01:

> Representative fixtures for every advertised framework deploy through the real execution path
> without requiring a Dockerfile or provider-specific repository configuration.

This repository is deliberately minimal. It contains **no Dockerfile**, no compose file, no
platform/provider configuration and no build scripts beyond what its framework normally uses —
so that a successful deployment demonstrates the platform's own detection and the builder's own
build, not configuration written for the occasion.

Represented framework: **`fastapi`**
