# Security policy

`robertprast/vouch-demo` uses **coordinated disclosure** via GitHub's private reporting, orchestrated
with [vouch](https://github.com/robertprast/vouch) — an open-source, non-profit
coordination commons built to help maintainers, not to sell anything.

## Reporting a vulnerability

**Do not open a public issue for security bugs.** Report privately:

- Use **[Report a vulnerability](https://github.com/robertprast/vouch-demo/security/advisories/new)**
  (this repo has Private Vulnerability Reporting enabled), **or**
- Hand off from your own coding agent with the vouch id below — vouch re-verifies
  your PoC against the shipping code, drafts the advisory + a fix, and files the
  private report for you. You never submit a token; it uses your local `gh` login.

```
vouch id:  vh_0d44f7fda3
handoff:   /vouch vh_0d44f7fda3      (in Claude Code / Codex)
```

## What happens next

1. You file a **private** report — nothing is public.
2. The maintainer **opts in**: a temporary private fork is created and you're added
   as an advisory collaborator, so we fix it together, in the open-with-us.
3. On publish you're **credited**. You keep your own writeup.

Both sides watch the finding move from *reported → opted-in → private fork → fix →
published* on the vouch hub. The hub never sees a token or your exploit.
