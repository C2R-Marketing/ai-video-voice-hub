The Lumen5 help-center read completes the picture — I now have results for all 10 tools. Compiling the report.

---

## Weekly re-verification results — AI video batch (10 tools), 2026-10-05

All data below was read from official pages this run. No third-party directories used; no invented figures. Previous dataset values are from the 2026-10-01 run (`~/workspace/ai-video-voice-hub/data/tools.json`).

### 1. Pictory — https://pictory.ai
- **pricing_status:** partially-verified (prices not extractable; title + plan structure confirmed)
- **plans:** Starter / Professional / Teams / Enterprise named on page; FAQ confirms Professional = 600 video minutes/mo (monthly) or 7,200 upfront (annual). Page title: "Pictory Pricing | From $25 per Month". No numeric per-plan prices rendered in text this run → dataset figures ($29/$25 annual, $59/$35 annual, $199/$119 annual) NOT re-confirmed; keep as re-verify badge.
- **free plan:** no permanent free plan — 14-day free trial = 3 video projects.
- **affiliate: NEW FINDING vs dataset.** Dataset said none-found. Official partner page **https://pictory.ai/partner-with-pictory** exists (surfaced via Pictory's own YouTube channel descriptions: "Join our FREE industry-leading Affiliate Partner Program"). Page confirms Marketing Partner track = affiliate with "industry leading affiliate commissions," but states **no numeric commission rate, no cookie length, no payout minimum**. Third-party directories claim 20–50% — NOT sources of truth, do not use. → has_program: **true**, commission: not stated on official page, cookie_days: not stated, payout_min: not stated.
- **source URLs read:** https://pictory.ai/pricing, https://pictory.ai/partner-with-pictory
- **notes:** No shutdown/pivot. Pricing page mostly FAQ text; prices JS-rendered.

### 2. InVideo — https://invideo.io
- **pricing_status:** verified — ZERO changes vs dataset
- **plans (all billed annually):** Starter $20/mo — 400 credits/seat/mo, 1 seat, no guest seats, Agent Two Lite only, Seedance 2.0 Fast & Mini, 200GB; Plus $36/mo — 2,000 credits/seat/mo, +10 guest seats, Seedance 2.0 4K + 2.5 1080p, 600GB ("Save $288/seat vs monthly"); Max $75/mo — 5,000 credits/seat/mo, +20 guest seats, 2,000GB ("Save $885/seat vs monthly"). Compare table confirms the same $20/$36/$75 annual figures. Unused credits don't roll over; downgrade → Free plan.
- **free plan:** yes (Free plan; paid plans downgrade to it on cancel).
- **affiliate:** https://invideo.io/make/affiliate-program/ re-verified: **50% on monthly plans, 25% on annual plans** (headline confirmed). Cookie/payout details sit in collapsed FAQ, not extractable → 120-day cookie / $30 payout-min carried from last run, not re-confirmed. Commission terms unchanged.
- **source URLs read:** https://invideo.io/pricing, https://invideo.io/make/affiliate-program/

### 3. Fliki — https://fliki.ai
- **pricing_status:** partially-verified (prices JS-rendered, not extractable)
- **plans:** Free — 3 credits/mo, 300 voices, 720p, watermark; Standard — 180 credits/mo, 1,000 voices (500 ultra-realistic), 1080p, ≤15 min, voice cloning, commercial rights; Premium — 600 credits/mo, 2,000+ voices, AI video clips, photo avatars, multiple voice cloning, brand kits, API; Enterprise — custom, billed yearly. ⚠️ **internal inconsistency on official page:** plan table says Premium "Videos upto 40 minutes"; pricing FAQ twice says Premium max **30 minutes** — flag vs dataset's "40 min". Active promo banner: code FLIKIEXPLAINER40 = 40% off annual plans (time-limited).
- **free plan:** yes — 3 credits/mo, 720p, watermark, no card required (FAQ also says 5 min/mo free audio+video; discrepancy noted).
- **affiliate:** https://fliki.ai/affiliate-program fully verified — **30% lifetime recurring commission, 30-day cookie, $50 minimum payout** (Wise, or PayPal for >$50), payouts 1st of each month, bonuses up to $1,000, free to join. Matches dataset exactly.
- **source URLs read:** https://fliki.ai/pricing, https://fliki.ai/affiliate-program

### 4. Lumen5 — https://lumen5.com
- **pricing_status:** unverified — https://lumen5.com/pricing **failed to fetch this run** (upstream_fetch_failed, no HTTP status). Company is NOT shut down: homepage renders fine, AI video maker operating normally ("Try for free", enterprise positioning). Not a pivot — just an unreadable pricing page.
- **free plan:** yes — official help KB: "best known for our Free plan", "Community Plan which is free forever."
- **affiliate:** has_program **false**, verified on official source. Lumen5's own help center (http://help.lumen5.com/en/category/account-settings-billing-information-fhjc3z/) states verbatim: **"Lumen5 does not have an affiliate or referral program at this time."** Note: several third-party directories (xAmplify, Affpaying, getlasso) claim a Lumen5 affiliate program — these are contradicted by the official KB and must not be used.
- **source URLs read:** https://lumen5.com (homepage), http://help.lumen5.com/en/category/account-settings-billing-information-fhjc3z/

### 5. VEED — https://www.veed.io
- **pricing_status:** unverified — https://www.veed.io/pricing is JS-rendered; only "Trusted by millions of teams" extractable. No tier prices read. Dataset's figures (Free $0 / Lite $19 / Pro $49) and the flagged $49-vs-older-$29 Pro discrepancy remain unresolvable this run → keep re-verify badge.
- **free plan:** yes per dataset; not re-confirmed this run.
- **affiliate:** https://www.veed.io/affiliate fully verified — **20% initial commission + 20% recurring on subscription payments, bonus commissions up to 50%** + cash incentives; signup and payouts via Impact.com (PayPal/bank transfer/wire); perks: free VEED Pro + 3,000 AI credits. Cookie length not stated on page. Matches dataset exactly.
- **source URLs read:** https://www.veed.io/pricing, https://www.veed.io/affiliate

### 6. Kapwing — https://www.kapwing.com
- **pricing_status:** verified — ZERO changes vs dataset
- **plans:** Free $0 — 10 credits, watermarked exports, 720p, 4-min exports, 5GB; Pro **$24/mo monthly / $16/mo billed annually** ($192/yr) — 1,000 credits/mo, no watermark, 4K, 200GB, 1,000 min auto-subtitles/mo, dubbing 50 min/mo; Business **$64/mo monthly / $50/mo billed annually** ($600/yr) — 4,000 credits/mo, custom voice clones, 800GB, auto-subtitling up to 4,000 min/mo, dubbing 200 min/mo; Enterprise — custom. All read directly on the page, including the annual-discount FAQ.
- **free plan:** yes — confirmed as above.
- **affiliate:** verified on TWO official sources: https://www.kapwing.com/affiliates (30-day attribution window, tiered standard→VIP→Super, no earnings cap, Tapfiliate-run) and the official affiliate portal https://kapwing.tapfiliate.com — **25% / 30% / 35% tiered recurring** (Standard 0–12 conversions/90d, Gold 12–24, Platinum 25+), "recurring rewards", free to join. ⚠️ Portal page self-contradiction: "Earn a minimum of 25%... and up to 25% for our top affiliates" while tiers show Platinum = 35% (likely typo; use 25/30/35 from the tier table). Matches dataset.
- **source URLs read:** https://www.kapwing.com/pricing, https://www.kapwing.com/affiliates, https://kapwing.tapfiliate.com

### 7. Runway — https://runwayml.com
- **pricing_status:** verified — ZERO price changes vs dataset
- **plans:** Free $0 — 125 one-time credits (never expire), 5GB; Standard **$15/mo monthly / $12/mo billed annually** ($144/yr) — 625 credits/mo, 20GB; Pro **$35/mo monthly / $28/mo billed annually** ($336/yr) — 2,250 credits/mo, 100GB; Max **$95/mo monthly / $76/mo billed annually** ($912/yr) — 9,500 credits/mo, 1-month credit rollover, 500GB, HDR/ProRes. Note: official page now lists models as **Gen-4.5, Gen-4 Turbo, Kling 3.0, Nano Banana Pro, Seedance 2.5** — dataset's "Gen-3/Gen-4" feature text is stale.
- **free plan:** yes — confirmed as above.
- **affiliate:** none found — no affiliate/partner program located on official pages.
- **source URLs read:** https://runwayml.com/pricing

### 8. Pika — https://pika.art
- **pricing_status:** verified — ZERO changes vs dataset
- **plans (annual saves 20%):** Free $0 — credit packs only, no watermark, no commercial license; Starter **$10/mo / $8/mo annual** — 900 credits/mo, no commercial license; Creator **$35/mo / $28/mo annual** — 3,150 credits/mo, commercial license Yes; Fancy **$95–$880/mo / $76–$704/mo annual** — 8,550+ credits/mo. All read directly from the official compare table.
- **free plan:** yes — confirmed as above.
- **affiliate:** none found on official pages.
- **source URLs read:** https://pika.art/pricing

### 9. Steve AI — https://www.steve.ai
- **pricing_status:** unverified (numeric prices JS-rendered, not extractable)
- **plans:** tier structure confirmed — Free / Basic / Starter / Pro / Enterprise. Page title: "Steve AI Pricing: Free, $19 Plans and more". Feature matrix: Free — 5 voice-overs, 80 animation characters, 1M assets, 50 AI Avatar min/mo, 50 AI Speech min/mo; Basic — 720p, 20 voice-overs, 100 characters, 75 min/mo; Starter — 1080p, 30 voice-overs, 200 characters, 150 min/mo; Pro — 2K, 40+ voice-overs, 300+ characters, 400 min/mo; Enterprise — 4K, custom. No per-plan dollar prices in readable text → dataset keeps empty tiers + re-verify badge.
- **free plan:** yes — confirmed as above.
- **affiliate:** https://www.steve.ai/affiliate verified — program exists; **"Earn up to 40% in commission"**, no earnings cap, monthly revenue reports, dedicated partner management. ⚠️ Nuance vs dataset: page does NOT explicitly say "recurring" — dataset's "Up to 40% recurring" should be softened to "up to 40% (recurring not stated)". Cookie_days and payout_min not stated on page.
- **source URLs read:** https://www.steve.ai/pricing, https://www.steve.ai/affiliate

### 10. FlexClip — https://www.flexclip.com
- **pricing_status:** partially-verified (prices JS-rendered; only FAQ extractable)
- **plans:** Free / Plus / Business confirmed by name (stock-video limits: Free 1/project, Plus 5/project, Business unlimited). Numeric prices not readable this run → dataset's Plus $19.99/mo ($11.99/mo annual) and Business $29.99/mo ($19.99/mo annual) from prior cross-checks are NOT re-confirmed → keep re-verify badge.
- **free plan:** yes — confirmed by plan names/FAQ on official page.
- **affiliate:** https://www.flexclip.com/affiliates.html fully verified — **35%+ commission by default** (raised for valuable partners), **90-day cookie tracking**, program runs on the **Awin** platform, payouts via Awin's global options; payout minimum not stated on official page. Matches dataset exactly.
- **source URLs read:** https://www.flexclip.com/pricing, https://www.flexclip.com/affiliates.html

## Headline counts for the parent
- **Prices changed:** 0 (no price moves detected on any readable official page)
- **Tools newly fully-verified on pricing this run:** 4 — InVideo, Kapwing, Runway, Pika (all match dataset exactly; zero drift)
- **Tools newly partially-verified/unverified:** Pictory (partially — plan structure confirmed, prices JS-rendered), Fliki (partially — structure confirmed, prices JS-rendered), VEED (unverified — JS-rendered), Steve AI (unverified — JS-rendered), FlexClip (partially — names only), Lumen5 (unverified — pricing page fetch failed)
- **Affiliate newly found:** Pictory — official partner page exists (program confirmed, but NO rates/terms stated; do not invent)
- **Revenue/trust items:** (1) Lumen5 officially states it has NO affiliate program — any third-party claims to the contrary are wrong; (2) Fliki's official page contradicts itself on Premium max video length (40 min in plan table vs 30 min in FAQ); (3) Kapwing's own affiliate portal contradicts itself ("up to 25%" vs 35% Platinum tier); (4) Steve AI's "recurring" commission qualifier is not stated on the official page — dataset nuance needed; (5) Runway's model lineup changed (Gen-4.5/Turbo, Kling 3.0, Nano Banana Pro, Seedance 2.5) — feature text is stale; (6) no tool shut down or pivoted away from its product this week; live sites all reachable.

I wrote no files. The per-tool structured data above is ready for the parent to merge into `data/tools.json` (with `last_verified: 2026-10-05`) and `VERIFICATION.md`.