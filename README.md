```
   _____                           _____ __             __
  / ___/____ _   _____  _________ / ___// /_____ ______/ /__
  \__ \/ __ \ | / / _ \/ ___/ __ \\__ \/ __/ __ `/ ___/ //_/
 ___/ / /_/ / |/ /  __/ /  / / / /__/ / /_/ /_/ / /__/ ,<
/____/\____/|___/\___/_/  /_/ /_/____/\__/\__,_/\___/_/|_|
```

# sovern-cli ⚡

**Rent a slice of a GPU. Spin up a notebook or SSH box. Get back to the fun part.**

The official command-line tool for [SovernStack](https://sovernstack.com): fractional GPU compute, billed by the hour, built for people who train and ship models.

No dashboard. No clicking. Just your terminal and a GPU.

---

## Install

```bash
pip install sovern
```

## Get your API key

You'll need a SovernStack API key so the CLI knows it's really you. API keys are free.

1. Head to [app.sovernstack.com](https://app.sovernstack.com) and sign in (or create an account if you're new).
2. Open the **Integrations** tab and create an API key.
3. Keep it secret, keep it safe. Don't commit it, don't paste it in screenshots, and don't put it in a public repo. Treat it like a password. Keys can be revoked or expire, so if something stops working, check your key first.

## Quick start

From zero to a GPU-backed Jupyter notebook in a few commands:

```bash
# 1. Log in with your SovernStack API key
sovern login --token <your-api-key>

# 2. See which nodes and GPUs have free capacity (and what they cost)
sovern compute

# 3. Launch a GPU notebook on a node
sovern notebook create --node kl-1 --name finetune-experiment --gpus 1 --slices 4

# 4. Done for now? Stop it so billing stops
sovern notebook stop <notebook-id>
```

Prefer a shell? Swap step 3 for `sovern ssh create` (see below).

## What can it do?

### Account

```bash
sovern whoami
```

Shows which user and API key you're logged in as. Handy as a quick check that your credentials work.

### Compute

```bash
sovern compute
```

Lists every node with its vCPUs, total and available RAM, and GPUs. Each GPU is split into VRAM **slices**, and you choose how many slices you want per GPU when you create or start something. Pricing is shown per slice per hour.

Availability is a snapshot. Someone else may claim the resources before your create call lands, in which case you'll get a capacity error and can pick another node.

### Notebooks

GPU-backed (or CPU-only) Jupyter notebooks.

```bash
# Create and start (returns a notebook URL once it's active)
sovern notebook create --node kl-1 --name my-notebook --gpus 1 --slices 4

# CPU-only: leave out --gpus and --slices
sovern notebook create --node kl-1 --name cpu-notebook

# List, optionally filtered by status (active, stopped, error, pending, all)
sovern notebook list --status active

# Inspect one
sovern notebook get <notebook-id>

# Stop (releases resources and stops billing; the record is kept)
sovern notebook stop <notebook-id>

# Restart a stopped or errored notebook (you can pick a different node or resources)
sovern notebook start <notebook-id> --node kl-1 --gpus 1 --slices 4

# Delete permanently
sovern notebook delete <notebook-id>
```

### SSH sessions

GPU-backed (or CPU-only) SSH sessions.

```bash
# Create and start (returns host, port, and your private key)
sovern ssh create --node kl-1 --name training-box --gpus 1 --slices 4

# List, optionally filtered by status (active, stopped, failed, pending, all)
sovern ssh list --status active

# Inspect one (host and port only appear while the session is active)
sovern ssh get <session-id>

# Stop / restart / delete
sovern ssh stop <session-id>
sovern ssh start <session-id> --node kl-1 --gpus 1 --slices 4
sovern ssh delete <session-id>

# Lost your key? Generate a new one for an active session
sovern ssh regen-key <session-id>

# Cut off access without stopping the session (billing continues)
sovern ssh revoke-key <session-id>
```

> **Your private key is shown only once.** It is never stored on our side, so save it as soon as it appears (for example to a file with `chmod 600`). If you lose it, run `sovern ssh regen-key`. Restarting a session keeps the existing key working.

## Good to know

**Slices.** When you ask for GPUs, `--slices` (at least 1) is applied to each GPU. For a CPU-only notebook or session, omit `--gpus` and `--slices` (or set `--gpus 0`).

**Billing.** You're billed per hour while a notebook or session is `active`, at the rate locked in when the resources were reserved.

- GPU workloads: the sum of `price_per_slice_hour` for each GPU assigned, multiplied by the number of slices.
- CPU-only workloads: a flat default hourly rate.
- If your credit doesn't cover at least one hour at the computed rate, the request is rejected.

**Always stop what you're not using.** `stop` releases resources and ends billing. Stopped items keep their record and can be restarted later.

**Create calls can be slow.** Creating or starting a notebook or session is synchronous and can take a while, so give it a moment. Creating is not idempotent: if a command times out, run `sovern notebook list` or `sovern ssh list` before retrying so you don't end up with duplicates.

**Rate limits.** 120 requests per minute on all endpoints, with a stricter limit on create, start, stop, delete, and key regeneration or revocation. If you hit a limit, wait and retry. Capacity data is cached for about 10 seconds, so polling `sovern compute` more often than that won't tell you anything new.

**Scope.** This version covers Compute, Notebooks, and SSH. Other SovernStack services aren't available through the CLI yet.

## Why sovern-cli?

Because clicking through a dashboard every time you need a GPU is a vibe-killer.

SovernStack lets you rent only the slice of VRAM you actually need instead of paying for a whole card that sits there mostly idle. This CLI brings that same "take what you need, nothing more" energy to your terminal.

Built by people who got tired of watching Colab disconnect mid-training at 2am. 🫠

## Contributing

Found a bug? Got an idea? Want to add something cool? We'd love your help.

Read [CONTRIBUTING.md](CONTRIBUTING.md) to get set up, and check out issues tagged [`good first issue`](../../issues?q=label%3A%22good+first+issue%22) if you're not sure where to start.

## License

MIT. Go wild. See [LICENSE](LICENSE) for the details.
