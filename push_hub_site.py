#!/usr/bin/env python3
"""Push ~/workspace/ai-video-voice-hub/ to C2R-Marketing/ai-video-voice-hub via
GitHub git-database API: new branch off main + PR to main. Never pushes main directly."""
import base64, json, os, subprocess, sys

SITE_DIR = os.path.expanduser("~/workspace/ai-video-voice-hub")
OWNER, REPO = "C2R-Marketing", "ai-video-voice-hub"
GH = os.path.expanduser("~/workspace/skills/github/bin/gh-api")
BRANCH = sys.argv[1] if len(sys.argv) > 1 else "site/initial-launch"

def gh(method, path, body=None):
    cmd = [GH, method, path]
    tmp = None
    if body is not None:
        import tempfile
        tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(body, tmp); tmp.close()
        cmd.append("@" + tmp.name)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    finally:
        if tmp:
            os.unlink(tmp.name)
    if r.returncode != 0:
        print(f"FAILED {method} {path}\n{r.stderr[:2000]}", file=sys.stderr)
        sys.exit(1)
    return json.loads(r.stdout)

main = gh("GET", f"/repos/{OWNER}/{REPO}/commits/main")
main_sha = main["sha"]
base_tree = main["commit"]["tree"]["sha"]
print("main:", main_sha[:12])

entries = []
n = 0
for root, dirs, files in os.walk(SITE_DIR):
    dirs.sort()
    if ".git" in dirs:
        dirs.remove(".git")
    for fn in sorted(files):
        if fn.startswith("."):
            continue
        full = os.path.join(root, fn)
        rel = os.path.relpath(full, SITE_DIR)
        with open(full, "rb") as f:
            content = f.read()
        blob = gh("POST", f"/repos/{OWNER}/{REPO}/git/blobs",
                  {"content": base64.b64encode(content).decode(), "encoding": "base64"})
        entries.append({"path": rel, "mode": "100644", "type": "blob", "sha": blob["sha"]})
        n += 1
        if n % 25 == 0:
            print(f"  ...{n} blobs", flush=True)
print(f"created {n} blobs")

tree = gh("POST", f"/repos/{OWNER}/{REPO}/git/trees",
          {"base_tree": base_tree,
           "tree": [{"path": e["path"], "mode": e["mode"], "type": e["type"], "sha": e["sha"]}
                    for e in entries]})
print("tree:", tree["sha"][:12])

msg = ("Initial launch: AI video & voice alternatives hub\n\n"
       "- 14 static pages (10 comparison pages + index + privacy/about/contact)\n"
       "- 40-tool dataset with per-tool verification log (VERIFICATION.md)\n"
       "- Affiliate disclosure first on every page; CTAs to official sites until tracking links verified\n"
       "- AdSense wired (publisher ca-pub-5514918108951220, Auto Ads) + ads.txt + sitemap.xml + robots.txt\n"
       "- Canonicals, JSON-LD (ItemList + FAQPage), privacy page covers ad cookies")
commit = gh("POST", f"/repos/{OWNER}/{REPO}/git/commits",
            {"message": msg, "tree": tree["sha"], "parents": [main_sha]})
print("commit:", commit["sha"][:12])

gh("POST", f"/repos/{OWNER}/{REPO}/git/refs",
   {"ref": f"refs/heads/{BRANCH}", "sha": commit["sha"]})
print("branch:", BRANCH)

pr = gh("POST", f"/repos/{OWNER}/{REPO}/pulls",
        {"title": "Initial launch: AI video & voice alternatives hub",
         "head": BRANCH, "base": "main",
         "body": "Static hub site: 10 comparison pages, 40 verified tools, affiliate + AdSense monetization. See commit message for details."})
print("PR:", pr["html_url"])
