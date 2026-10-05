All three batches are complete. Here is the full synthesized 10-tool verification report for 2026-10-05.

---

# Hub Weekly Re-verification — Voice tools (10 tools), 2026-10-05

All figures below were read from official pages **this run**. Where a page was unreadable, the tool is marked unverified — nothing was filled from memory or third-party directories. No files written.

## Batch A

### 1. ElevenLabs — https://elevenlabs.io
- **pricing_status: unverified** — entire elevenlabs.io domain policy-blocked in this environment; no official page could be read. Prior (2026-10-01) figures cannot be re-verified.
- plans / free plan: unverified.
- affiliate: has_program **yes, but unverified** — official page exists at https://elevenlabs.io/affiliates (confirmed by multiple third-party references), but no commission rate, cookie length, or payout minimum could be read from an official page. (Third-party consensus — NOT treated as truth: 22% recurring/12 months on Starter/Creator/Pro/Scale, 11% on Business, 90-day cookie, $5 payout min via PartnerStack.)
- **Action needed: live-browser check of `elevenlabs.io/pricing` and `elevenlabs.io/affiliates` by an eligible agent.**

### 2. Murf — https://murf.ai
- **pricing_status: partially-verified** — official page read: https://murf.ai/pricing. Only TTS API figures rendered in text fetch: **$10/mo free API credit** ("$10 FREE, every month"; purchased credit never expires) and **$0.01 per 1,000 characters** (Falcon model). Studio tiers (Free/Creator/Business/Enterprise) are JS-rendered tabs — **prices NOT verified this run**; do not backfill.
- free plan: partially — $10/mo free API credit confirmed; Studio free-plan details not readable.
- affiliate: **yes, fully verified** — https://murf.ai/partner-with-us/affiliate (echoed on official help page help.murf.ai):
  - commission: **20% recurring per referral, up to 24 months from signup**
  - cookie_days: **90** ("attributed for 90 days")
  - payout_min: **not stated** on official page
  - runs via PartnerStack; monthly payouts via PayPal or Stripe; commission-only (no referral discounts)
- notes: pricing page now organized around TTS API / Voice Agents / Content Studio / Dub products. Recommend live-browser check of the Studio tier tabs.

### 3. PlayHT — https://play.ht
- **pricing_status: unverified** — `play.ht/pricing` failed: DNS resolution failure ("browser.open requires a resolvable public HTTP(S) URL").
- affiliate: **none-found** — no official-domain affiliate page surfaced, and the domain is unreachable.
- **🚨 RED FLAG — product appears discontinued.** Third-party reports (converging but not official): PlayHT rebranded to PlayAI; Meta acquired the team (July 2025); the standalone service was shut down and accounts/cloned voices were reportedly deleted on 2025-12-31; both play.ht and play.ai fail DNS. The DNS failure observed this run is consistent with a shutdown. **Treat as possibly dead; do not publish any pricing (figures floating online are stale). Recommend flagging/removing pending live confirmation via an official Meta/company statement.**

### 4. Speechify — https://speechify.com
- **pricing_status: verified** — pages read: https://speechify.com/pricing, https://speechify.com/pricing-api/, https://speechify.com/affiliates
- Reader plans: **Free $0** (listen up to 1.5x, 10 basic voices, TTS only); **Premium $29/month** (MOST POPULAR: 1000+ voices, 60+ languages, up to 5x speed, Scan & Listen, AI Summaries & Chats, Drive/Dropbox/OneDrive integrations, Voice Typing, AI Podcasts, Voice AI Assistant). Annual price not shown on page read.
- API plans: **Free $0/mo** (500K chars/mo then pauses); **Starter $10/mo** (1.9M chars, then $10/1M); **Pro $99/mo** (13.5M chars, then $8/1M); **Scale $499/mo** (78M chars, then $6/1M); **Enterprise custom**. All self-serve plans month-to-month, dollar-balance usage, top-ups never expire. Voice agents enterprise-only.
- free plan: yes — Free Reader + Free API tier (500K chars/mo) verified.
- affiliate: **yes, verified** — https://speechify.com/affiliates (covers Premium, VoiceOver Studio Basic, Studio Pro):
  - commission: **not stated** on official page ("compelling commission structure… high payouts" but no rate — do not republish the old blog's 50/50 revenue-share claim as current)
  - cookie_days: page defines a "qualified action" as signup **and paid-plan purchase within 60 days of clicking** — a 60-day attribution window (cookie not explicitly labeled)
  - payout_min: **not stated**

## Batch B

### 5. Resemble AI — https://www.resemble.ai
- **pricing_status: partially-verified** — sources read: https://www.resemble.ai/pricing, homepage.
- **🚨 PIVOT CONFIRMED.** Homepage is now "Multimodal Deepfake Detection and Watermarking for Enterprise." The old consumer voice-cloning tiers (~$29/$99) are **gone** from the official site; third-party pages still listing them are stale. Current pricing page ("Deepfake Detection & AI Security Pricing"): **Flex $0/mo** (pay-as-you-go credits, never expire: Detect audio $0.035/sec, images $0.035/image, video $0.070/sec, Intelligence $0.025/sec, Watermarker encode $0.00050/call, decode $0.00020/call, Agent Detection $1/1,000 sessions; 1 seat); **Team $350/mo** monthly / $280/mo annual; **Business $1,000/mo** / $800/mo annual; **Enterprise custom**.
- free plan: yes — $0 Flex tier (pay-as-you-go credits; not a TTS tier).
- affiliate: **none-found** — no "affiliate" mention on official homepage; no official affiliate page in search; only enterprise reseller reference (Carahsoft, not an affiliate program).
- **Recommendation: flag/remove Resemble AI from the voice-comparison hub** — it sells no voice-creation product at all now.

### 6. WellSaid Labs — https://www.wellsaid.io
- **pricing_status: verified** — pages read: https://www.wellsaid.io/pricing, homepage.
- plans: **Trial (Free) $0** (3 download min/mo, no commercial rights, no credit card); **Starter $19/mo** monthly / **$10/mo annual** ($120/yr, save 47% — 240 min/yr); **Pro $49/mo** / **$33/mo annual** ($396/yr, 180 min/mo or 2,160 min/yr); **Business $160/user/mo** annual ($1,920/yr/user, 2,880 min/yr/user, up to 5 seats); **Enterprise custom**. "Pricing is for new customers" disclaimer present.
- free plan: yes — Trial tier verified.
- affiliate: **none-found** (unchanged from prior). Note: third-party press mentions a June 2025 "WellSaid Partner Program," but it is B2B API co-selling, and no official wellsaid.io page exists for it — not a public affiliate program.
- notes: change since prior — Creator tier appears rebranded to Starter with lower entry pricing ($19/mo). Pricing page stable.

### 7. Lovo — https://lovo.ai
- **pricing_status: verified** — pages read: https://lovo.ai/pricing, http://LOVO.ai/affiliate-program
- plans: **Basic $24/mo** ($288/yr; 2 hrs/mo generation, 500+ voices, 5 clones, 120 min/mo auto subtitles, 30 GB, 10 projects, 1080p export); **Pro $24/mo** ($288/yr; 5 hrs/mo, unlimited clones, Pro V2 voices, AI writer/SFX, team collab, priority queue, 100 GB, 50 projects); **Pro+ $75/mo** ($900/yr; 20 hrs/mo, 300 min/mo subtitles, priority support, unlimited projects, 400 GB); **Enterprise custom**. Page shows "SAVE UP TO 50% WITH YEARLY" banner — a promo that may expire.
- free plan: **not verified from official page text** ("Start now for free" CTAs but no stated free-tier terms readable). Third-party claims of a 14-day Pro trial are not official.
- affiliate: **yes** — official page "Join our Affiliate Program & Earn Commission | LOVO AI":
  - commission: **20% recurring for 24 months** on all new customers
  - cookie_days: **not stated** on official page (do not use third-party 60-day claim)
  - payout_min: **not stated**
  - terms: no minimums, paid monthly, tracking, support & training, free signup, approval ~1 week, custom links for podcast/YouTube/Instagram
- notes: matches prior terms (20% / 24 months) — fully re-verified. Hub copy should note "promotional pricing shown as of 2026-10-05" given the yearly-discount banner.

## Batch C

### 8. Podcastle — https://podcastle.ai
- **pricing_status: partially-verified** — sources read: https://podcastle.ai/pricing, https://podcastle.ai/affiliate, https://async.com/pricing.
- **Rebrand confirmed this run: the product is now "Async."** `podcastle.ai/pricing` renders *"Pricing | Async"* (assets from m.async.com); identical page at `async.com/pricing`. Affiliate page: *"Join Async Affiliates."* The platform is now a credit-based AI media platform (video/image/avatar/music), not just podcasting.
- plans (structure visible, but **price cards are JS-rendered — no "$" anywhere in fetched text, so dollar amounts NOT verified this run**): Free — $0/mo (plan named Free; FAQ: no credit card required to sign up with Free plan; quotas: 10 AI credits lifetime, 1 hr lifetime media minutes to AI chat, 1 hr lifetime remote recording, 2 hr lifetime transcription (shared video+audio), 15 min lifetime AI clips/reframe/subtitles, TTS ~15 min (~12k chars) lifetime, 2 GB storage, 1-file export limit, up to 720p, watermarked); Essentials — price unverified (450 AI credits/mo, 10 hrs transcription/mo, 2 hrs remote recording, up to Full HD); Pro — price unverified (1,200 credits/mo, 25 hrs transcription/mo, 20 hrs remote recording, up to 4K); Teams — price unverified (3,000 credits/mo, 100 hrs transcription/mo, 50 hrs remote recording, up to 4K); Enterprise custom.
- free plan: yes — lifetime quotas above, no credit card.
- affiliate: **yes** — "Async Affiliate Program" (in-house, not via a network), https://podcastle.ai/affiliate: **25% commission** on every eligible subscription (no tiers stated); cookie_days **unknown** (not stated); payout_min **unknown**; perks: early access, affiliate Discord, banners/assets, tracking dashboard.
- notes: old podcast-only tier line is gone; model is now credits. One third-party page claimed Essentials $11.99/mo monthly / $19.99/mo annual (internally contradictory "inverted" structure) — do not backfill from it. Hub listing copy/URLs should become "Async (formerly Podcastle)". **Async's dollar prices need a live-browser check before publishing.**

### 9. Listnr — https://listnr.tech
- **pricing_status: verified** — sources read: https://listnr.tech/pricing, https://listnr.AI/affiliate
- plans: **Free $0** (no credit card; 1,000 credits **to start**, one-time grant — not a monthly quota; 1,000+ voices preview; 142+ languages/accents; Studio access; limited downloads/exports); **Individual $19/mo** (annual $190 — "2 months free on yearly plans"; 20,000 credits/mo ~2 hrs voice, 50 GB, 50 videos/mo, unlimited downloads/exports, unlimited audio embeds, commercial rights, 1,000+ voices); **Solo $39/mo** (annual $390; 50,000 credits/mo ~5 hrs, 100 GB, 150 videos/mo); **Agency $99/mo** (annual $990; 250,000 credits/mo ~25 hrs, 250 GB, 250 videos/mo); **Custom/Enterprise** custom proposal. FAQ: yearly = 10 months charged up front; upgrades prorated immediately; downgrades take effect end of cycle; cancellations revert to free; generally no partial-month refunds.
- free plan: yes — 1,000 credits to start, no credit card.
- affiliate: **yes** — official "Listnr Affiliate Programme," https://listnr.AI/affiliate (portal: listnr.tolt.io): commission **tiered — 30% starter / 35% at 30 active referrals / 40% at 50+ customers**, accruing across a **12-month commission period** (recurring); cookie_days **unknown**; payout_min **unknown** (handled by Tolt).
- notes: stable; Listnr now operates on two official domains — listnr.tech (pricing) and listnr.AI (affiliate); same branding/product JSON-LD on both. Hub affiliate link may need updating to the listnr.AI target.

### 10. Coqui — https://coqui.ai
- **pricing_status: unverified — no official pricing exists anymore.**
- plans: none. free plan: n/a.
- affiliate: **none-found.**
- official source read: https://coqui.ai (fetched this run).
- **🚨 RED FLAG: coqui.ai no longer belongs to Coqui AI.** The domain now serves an Indonesian gambling/slot spam site (*"UNIKBET: Link Situs Slot Maxwin Hari Ini Platform Situs Toto 4D Terbaru 2026"*). The domain is expired, parked, and hijacked. Coqui the company shut down in January 2024 (founder announcement; open-source TTS survives only via the community fork idiap/coqui-ai-TTS — not a commercial, affiliate-able product). **Recommendation: remove Coqui from the hub and do NOT link coqui.ai from any hub page** — it currently resolves to gambling spam. No replacement affiliate link is possible.

## Summary table

| Tool | Pricing status | Free plan | Affiliate | Headline |
|---|---|---|---|---|
| ElevenLabs | unverified (domain policy-blocked) | unverified | yes but unverified | Needs live-browser check |
| Murf | partially-verified (API figures only) | partial (API credit) | **yes — 20% recurring / 24 mo, 90-day cookie** | Studio tiers need live check |
| PlayHT | unverified (domain DNS fails) | unverified | none-found | **Appears shut down (Meta/PlayAI acquisition)** — flag for removal |
| Speechify | verified | yes | **yes — page live, rate undisclosed, 60-day attribution** | Fully verified; old 50/50 claim is stale |
| Resemble AI | partially-verified | yes ($0 Flex) | none-found | **Pivoted to deepfake detection — flag for removal** |
| WellSaid Labs | verified | yes (3 min/mo trial) | none-found | Starter $19 / Pro $49 rebrand confirmed |
| Lovo | verified | not verified | **yes — 20% recurring / 24 mo** | Cookie/payout-min still undisclosed |
| Podcastle/Async | partially-verified (prices JS-rendered) | yes (lifetime quotas) | **yes — 25% commission** | **Rebranded to "Async"**; dollar prices need live check |
| Listnr | verified | yes (1,000 credits to start) | **yes — tiered 30/35/40%, 12-mo recurring** | Stable; affiliate moved to listnr.AI |
| Coqui | unverified (domain hijacked) | n/a | none-found | **Remove — domain serves gambling spam** |

## Aggregate counts
- Prices fully verified: **4** (Speechify, WellSaid Labs, Lovo, Listnr)
- Prices partially verified: **3** (Murf, Resemble AI, Podcastle/Async)
- Prices newly unverified: **3** (ElevenLabs, PlayHT, Coqui)
- Affiliate programs newly verified: **4** (Murf, Speechify, Lovo, Listnr) + Podcastle/Async re-verified post-rebrand (25%)
- Failures/blocked pages: ElevenLabs (policy-blocked domain), PlayHT (DNS failure), Async (JS-rendered price cards), Murf Studio tiers (JS-rendered)

## Items needing live-browser follow-up (eligible agent)
1. `elevenlabs.io/pricing` + `elevenlabs.io/affiliates` (whole domain policy-blocked here)
2. Async (formerly Podcastle) pricing dollar figures (JS-rendered cards)
3. Murf Studio tier prices (JS-rendered tabs)
4. PlayHT shutdown confirmation — look for an official Meta/PlayAI statement before delisting