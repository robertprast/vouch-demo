# Threat model — vouch-demo

> Seeded by [vouch](https://github.com/robertprast/vouch) at onboarding, modeled on
> the containerd threat-model doc. This is a **starting point** — the maintainer
> edits it to reflect reality. It gives researchers (and their agents) the trust
> boundaries to aim at, so reports land on real seams instead of noise.

vouch id: `vh_0d44f7fda3`

## Assets (what an attacker wants)
- Integrity and confidentiality of data `vouch-demo` processes on behalf of its callers.
- The privileges `vouch-demo` runs with (and any it can escalate to).
- Secrets/credentials it holds or brokers.

## Trust boundaries (where privilege changes hands)
- **Untrusted input → parser/handler.** Any data crossing the boundary from a less-
  trusted caller (network request, file, CLI arg, env) into `vouch-demo`'s logic.
- **`vouch-demo` → OS / other services.** Where it shells out, opens files/sockets, or
  calls another service — a confused-deputy or injection surface.
- **Privilege transitions.** Any point where a check decides *who* an action runs as
  or *what* it may touch.

## Entry points (attack surface to enumerate)
- Public APIs / CLI subcommands / RPC handlers.
- Deserialization, template, path, and command construction sites.
- Anything that consumes attacker-controlled names, ids, or URLs.

## In scope
- Memory safety, injection (command/path/template), authz bypass, confused-deputy,
  SSRF, secret exposure, privilege escalation.

## Out of scope (unless chained to the above)
- Findings requiring an already-privileged local attacker.
- Best-practice/hardening nits with no demonstrated impact.

## Disclosure
See [`SECURITY.md`](./SECURITY.md). Report privately; hand off with `vh_0d44f7fda3`.
