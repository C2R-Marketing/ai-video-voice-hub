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

msg = ('Weekly re-verification: 2026-10-05\n\n- All 40 tools re-checked against official pages only (pricing + affiliate pages)\n- Pricing: verified 22 / partially-verified 9 / unverified 9 (JS-rendered or unreachable official pages keep the "being re-verified" badge; no tool deleted, no figures invented)\n- New affiliate programs found/verified this run: Pictory (program confirmed, no rates stated), Murf (20% recurring/24mo), Speechify (page live, rate undisclosed), Lovo (20%/24mo), Listnr (tiered 30/35/40%), Podcastle/Async (25%), Elai (25%/12mo), Vizard (25%), Flixier (50%/25%), Gling (20%/12mo), OpusClip (25%/1yr), Timebolt (20%), Descript ($25 flat)\n- Trust flags: Coqui domain hijacked by gambling spam (do not link coqui.ai); Vidnoz affiliate under construction; D-ID affiliate invite-only; Resemble AI pivoted to deepfake detection (no voice product); Synthesys pivoted to AI ad-video agent; PlayHT appears shut down (unconfirmed via official sources)\n- VERIFICATION.md appended with dated run section; site copy updated (verified October 5, 2026)\n- 14 pages rebuilt, all sanity checks pass, live site returns 200')
commit = gh("POST", f"/repos/{OWNER}/{REPO}/git/commits",
            {"message": msg, "tree": tree["sha"], "parents": [main_sha]})
print("commit:", commit["sha"][:12])

gh("POST", f"/repos/{OWNER}/{REPO}/git/refs",
   {"ref": f"refs/heads/{BRANCH}", "sha": commit["sha"]})
print("branch:", BRANCH)

pr = gh("POST", f"/repos/{OWNER}/{REPO}/pulls",
        {"title": "Weekly re-verification: 2026-10-05",
         "head": BRANCH, "base": "main",
         "body": "Weekly agentic re-verification of the 40-tool dataset against official pages only. No figures invented; unverified tools keep the re-verifying badge. Main agent reviews the diff and merges. See commit message for the full per-run summary."})
print("PR:", pr["html_url"])
