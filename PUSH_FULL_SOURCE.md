# How to push the full application source (one-time, on your PC)

The connected Grok tools can write text files to GitHub, but **cannot** `git push` 200+ files without a local credential helper.

## Fastest path for ChatGPT

1. Keep this repo **public** (temporary).
2. In ChatGPT: attach `NEXORA_AI_COMPLETE_RELEASE.zip` + link to this repo.
3. After review: set repo back to **private**.

## Put full source on GitHub (so ChatGPT only needs the link)

On your computer (GitHub logged in via `gh auth login` or HTTPS):

```bash
git clone https://github.com/spetthayn/NEXORA-AI-PUBLIC.git
cd NEXORA-AI-PUBLIC
unzip /path/to/NEXORA_AI_COMPLETE_RELEASE.zip
# archive contains folder nexora-ai/
git add nexora-ai
git commit -m "feat: full Phase 0-8 application source"
git push origin main
```

Or attach the ZIP as a GitHub Release asset (Releases → New → upload ZIP).

SHA-256 of release ZIP:

```
c8a06375aa4580113a07c19b5920aab56539ca060956371dbecf28643d09b39d
```
