#!/usr/bin/env python3
"""Apply 2026-10-05 weekly re-verification findings to data/tools.json.
Only figures read on official pages this run enter the dataset.
Run: python3 verification-reports-2026-10-05/merge_updates.py
"""
import json, copy, os

BASE = os.path.expanduser("~/workspace/ai-video-voice-hub")
PATH = os.path.join(BASE, "data/tools.json")
DATE = "2026-10-05"

def tiers(*specs):
    return [{"plan": p, "price_usd": pr, "billing": b, "notes": n}
            for p, pr, b, n in specs]

def aff(has_program, commission, cookie_days, payout_min, apply_url, status):
    return {"has_program": has_program, "commission": commission,
            "cookie_days": cookie_days, "payout_min": payout_min,
            "apply_url": apply_url, "status": status}

def note(t, text):
    t["verification_notes"] = text

# ---- per-tool mutations (only from official pages read this run) ----
UPDATES = {}

def U(name, **kw): UPDATES[name] = kw

# ============ VIDEO BATCH ============
U("Pictory",
  verification_status="partially-verified", last_verified=DATE,
  source_urls=["https://pictory.ai/pricing", "https://pictory.ai/partner-with-pictory"],
  affiliate=aff(True,
    "Program confirmed on official partner page ('industry-leading affiliate commissions' claimed). No commission rate, cookie length, or payout minimum stated on official page — third-party 20–50% figures not used.",
    None, "", "https://pictory.ai/partner-with-pictory", "verified"),
  free_plan_details="No permanent free plan — 14-day free trial = 3 video projects (per official FAQ)")
# note set below

U("InVideo", last_verified=DATE,
  source_urls=["https://invideo.io/pricing", "https://invideo.io/make/affiliate-program/"])
# tiers unchanged (zero drift, verified)

U("Fliki", last_verified=DATE,
  verification_status="partially-verified",
  source_urls=["https://fliki.ai/pricing", "https://fliki.ai/affiliate-program"],
  affiliate=aff(True, "30% recurring lifetime commission", 30, "$50",
                "https://fliki.ai/affiliate-program", "verified"))

U("Lumen5", last_verified=DATE,
  verification_status="unverified",
  source_urls=["https://lumen5.com",
               "http://help.lumen5.com/en/category/account-settings-billing-information-fhjc3z/"],
  affiliate=aff(False, "", None, "", "", "none-found"))

U("VEED", last_verified=DATE,
  verification_status="unverified",   # prices JS-rendered, not readable this run
  source_urls=["https://www.veed.io/pricing", "https://www.veed.io/affiliate"],
  affiliate=aff(True, "20% initial + 20% recurring, with bonuses up to 50%",
                None, "", "https://www.veed.io/affiliate", "verified"))

U("Kapwing", last_verified=DATE,
  source_urls=["https://www.kapwing.com/pricing", "https://www.kapwing.com/affiliates",
               "https://kapwing.tapfiliate.com"])

U("Runway", last_verified=DATE,
  features=["Gen-4.5 / Gen-4 Turbo / Kling 3.0 / Nano Banana Pro / Seedance 2.5 video generation (per official pricing page, 2026-10-05)",
            "Text-to-video", "Image-to-video", "Inpainting", "Motion brush"],
  source_urls=["https://runwayml.com/pricing"])

U("Pika", last_verified=DATE,
  source_urls=["https://pika.art/pricing"])

U("Steve AI", last_verified=DATE,
  verification_status="unverified",
  source_urls=["https://www.steve.ai/pricing", "https://www.steve.ai/affiliate"],
  affiliate=aff(True,
    "Up to 40% commission ('Earn up to 40% in commission' — recurring NOT stated on official page); no earnings cap; monthly revenue reports; dedicated partner management; cookie and payout minimum not stated",
    None, "", "https://www.steve.ai/affiliate", "verified"))

U("FlexClip", last_verified=DATE,
  verification_status="partially-verified",
  source_urls=["https://www.flexclip.com/pricing", "https://www.flexclip.com/affiliates.html"])

# ============ AVATAR BATCH ============
U("HeyGen", last_verified=DATE,
  source_urls=["https://www.heygen.com/pricing", "https://www.heygen.com/en-gb/affiliate-program"],
  affiliate=aff(True,
    "35% commission for the first 3 months of each referred subscription (Creator & Team plans); 30-day last-click cookie; $30 min payout via PayPal; 60-day verification hold; monthly payouts",
    30, "$30 (PayPal)", "https://www.heygen.com/en-gb/affiliate-program", "verified"))

U("Synthesia", last_verified=DATE,
  source_urls=["https://www.synthesia.io/pricing",
               "https://www.synthesia.io/partners/affiliates",
               "https://www.synthesia.io/terms/affiliate-terms"],
  affiliate=aff(True,
    "25% commission on Starter and Creator plan payments; 60-day cookie; customer stays 'Qualified Customer' for 12 months from first purchase; $30 min payout (rolls over until met); monthly payment",
    60, "$30", "https://www.synthesia.io/partners/affiliates", "verified"))

U("Colossyan", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://www.colossyan.com/pricing", "https://www.colossyan.com/affiliate-program/"],
  pricing_tiers=tiers(
    ("Free (Starter)", 0, "monthly", "20 NEO min/mo, 15 custom avatars + 3 voices, 10 interactive videos/mo, 15 auto-translations/mo"),
    ("Professional", 59, "annual-monthly", "$59/mo billed annually; 30 NEO + 10 NEO2 min/mo, up to 3 editors, $30/mo per additional member, watermark removal, 5 SCORM/mo; monthly-billing rate not shown"),
    ("Enterprise", None, "custom", "Contact sales")),
  free_plan_details="Starter free plan: 20 NEO min/month, no card required",
  affiliate=aff(True,
    "Starts at 25% recurring, up to 50% at higher tiers; commissions paid for up to a year per referral; 90-day cookie; monthly payouts (Wise preferred, PayPal under conditions)",
    90, "", "https://www.colossyan.com/affiliate-program/", "verified"))

U("Elai", last_verified=DATE,
  verification_status="unverified",
  source_urls=["https://elai.io/pricing", "https://elai.io/partners/",
               "https://elai.io/affiliate-partner-terms-conditions/"],
  strengths=["25% affiliate commission for the first 12 months (verified on official elai.io partner pages, 2026-10-05)"],
  affiliate=aff(True,
    "25% of referred plan payments for the first 12 months the customer stays (monthly: 25% of monthly payment; annual: 25% of annual payment); Enterprise plans excluded; paid monthly via Rewardful; no stated min payout; last-click attribution (day count not stated on official page)",
    None, "", "https://elai.io/partners/", "verified"))

U("D-ID", last_verified=DATE,
  verification_status="unverified",
  source_urls=["https://www.d-id.com/pricing", "https://www.d-id.com/affiliate-terms/"],
  affiliate=aff(True,
    "INVITE-ONLY (open to selected D-ID users at D-ID's sole discretion). Affiliation Fee = LOWER of the referred user's first two consecutive months' net subscription fees (minus 6% processor fee), payable once aggregate reaches $30 within 12 months. Sharing must be personal and non-commercial — no mass outreach, blogs, social posts, or coupon sites. Terms last updated June 2023.",
    None, "$30 (aggregate within 12 mo)", "https://www.d-id.com/affiliate-terms/", "verified"))

U("DeepBrain AI", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://www.deepbrain.io/pricing", "https://www.deepbrain.io/affiliate"],
  pricing_tiers=tiers(
    ("AI Studios Free", 0, "monthly", "3 videos, 1 min each, 720p, 16 generative credits"),
    ("AI Studios Personal", 24, "monthly", "Unlimited videos, 30-min max, 1080p, 60 generative credits/mo"),
    ("AI Studios Team", 55, "monthly", "Per seat/mo; 4K, 60-min max, 150 credits/seat/mo"),
    ("Interactive Avatar (LiveAvatar) Free", 0, "monthly", "2 credits"),
    ("Interactive Avatar Standard", 99, "monthly", "100 credits, 1 credit per 5 min"),
    ("Enterprise", None, "custom", "AI Studios + LiveAvatar; contact sales")),
  free_plan_details="AI Studios Free (3 videos, 1 min each, 720p) + LiveAvatar Free (2 credits)",
  affiliate=aff(True, "40% recurring commission for the referral's first 6 months; 60-day cookie, first-click attribution; $30 min payout via PayPal; 1-month fraud review then monthly payout",
                60, "$30", "https://www.deepbrain.io/affiliate", "verified"))
# note: 20% off with annual billing

U("Hour One", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://hourone.ai/pricing"],
  pricing_tiers=tiers(
    ("Free Trial", 0, "monthly", "3 min total publishing time, 100+ avatars, 1 editor + 1 viewer, business email required, no expiry"),
    ("Lite", 30, "monthly", "$24/mo billed annually; 10 min/mo"),
    ("Business", 112, "monthly", "$96/mo billed annually; 20/30/40-min options"),
    ("Enterprise", None, "custom", "Unlimited minutes, cinematic avatar, API, SSO")),
  free_plan_details="Free trial account: 3 min total publishing time",
  weaknesses=["Affiliate page returned HTTP 500 on 2026-10-05 — affiliate program status inconclusive, terms not re-confirmed"],
  affiliate=aff(True, "20% of Net Revenue for the first 12 months of each customer's contract (carried from 2026-10-01 — NOT re-confirmed this run; official affiliate page returned HTTP 500 on 2026-10-05, program existence inconclusive)",
                60, "$250", "https://hourone.ai/affiliate-program/", "unverified"))

U("Tavus", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://www.tavus.io/pricing", "https://www.tavus.io/lp/partnerships"],
  pricing_tiers=tiers(
    ("Developer Basic", 0, "monthly", "Free; 25 min conversational video/mo, 5 min video generation, 25 stock replicas"),
    ("Developer Starter", 59, "monthly", "$59/mo + pay-as-you-go; 100 CVI min, 10 video-gen min, 3 custom replica trainings/mo"),
    ("Developer Growth", 397, "monthly", "$397/mo + pay-as-you-go; 1,250 CVI min, 100 video-gen min, 7 replica trainings/mo"),
    ("Developer Enterprise", None, "custom", "Contact sales"),
    ("PALs Free", 0, "monthly", "15 min voice/video calls"),
    ("PALs Plus", 20, "monthly", "150 min"),
    ("PALs Max", 50, "monthly", "500 min")),
  free_plan_details="Developer Basic + PALs Free tiers",
  affiliate=aff(False,
    "No public self-serve program. Official Referral Partnerships page is contact-based with no published rates ('Earn commission for every customer you refer' — no numbers). Do not invent a rate.",
    None, "", "https://www.tavus.io/lp/partnerships", "none-found"))

U("Vidnoz", last_verified=DATE,
  verification_status="partially-verified",
  source_urls=["https://www.vidnoz.com/pricing.html", "https://www.vidnoz.com/affiliate-program-waitlist.html"],
  affiliate=aff(False, "Program UNDER CONSTRUCTION — waitlist only per official page (affiliate-program-waitlist.html). Any Vidnoz tracking link may be dead/earning nothing.",
                None, "", "https://www.vidnoz.com/affiliate-program-waitlist.html", "none-found"))

U("Synthesys", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://synthesys.io/pricing"],
  pricing_tiers=tiers(
    ("Starter", 29, "monthly", "$20/mo billed annually ($240/yr); 3,500 credits/mo"),
    ("Pro", 59, "monthly", "$41/mo billed annually ($492/yr); 8,000 credits"),
    ("Agency", 119, "monthly", "$83/mo billed annually ($996/yr); 17,000 credits"),
    ("Max", 199, "monthly", "$139/mo billed annually ($1,668/yr); 30,000+ credits"),
    ("Credit packs", 10, "one-time", "$10/1,000 credits; $25/2,750 credits; $50/6,000 credits")),
  free_plan_details="No free plan listed",
  strengths=["Full commercial rights on paid plans"],
  affiliate=aff(False,
    "No current affiliate page on official site — only a stale ~2023 official blog mention (40% lifetime recurring, $100 threshold via Paykickstart); treat as unverified.",
    None, "", "", "unverified"))

# ============ VOICE BATCH ============
U("ElevenLabs", last_verified=DATE,
  verification_status="unverified",
  source_urls=[],
  affiliate=aff(True,
    "Official affiliate page exists at elevenlabs.io/affiliates but the whole domain was policy-blocked in this environment on 2026-10-05 — no commission rate, cookie, or payout verified against an official page. Third-party 22%/90-day claims not used.",
    None, "", "https://elevenlabs.io/affiliates", "unverified"))

U("Murf", last_verified=DATE,
  verification_status="partially-verified",
  source_urls=["https://murf.ai/pricing", "https://murf.ai/partner-with-us/affiliate"],
  affiliate=aff(True,
    "20% recurring per referral for up to 24 months from signup; 90-day attribution; payouts monthly via PartnerStack (PayPal/Stripe); commission-only, no referral discounts; payout minimum not stated",
    90, "", "https://murf.ai/partner-with-us/affiliate", "verified"))

U("PlayHT", last_verified=DATE,
  verification_status="unverified",
  source_urls=[],
  affiliate=aff(False, "", None, "", "", "none-found"))

U("Speechify", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://speechify.com/pricing", "https://speechify.com/pricing-api/",
               "https://speechify.com/affiliates"],
  pricing_tiers=tiers(
    ("Free (Reader)", 0, "monthly", "Listen up to 1.5x, 10 basic voices, TTS only"),
    ("Premium (Reader)", 29, "monthly", "1000+ voices, 60+ languages, up to 5x speed, Scan & Listen, AI Summaries & Chats, Drive/Dropbox/OneDrive, Voice Typing, AI Podcasts, Voice AI Assistant; annual price not shown"),
    ("Free (API)", 0, "monthly", "500K chars/mo, then pauses"),
    ("API Starter", 10, "monthly", "1.9M chars, then $10/1M chars"),
    ("API Pro", 99, "monthly", "13.5M chars, then $8/1M chars"),
    ("API Scale", 499, "monthly", "78M chars, then $6/1M chars"),
    ("Enterprise", None, "custom", "Contact sales")),
  free_plan_details="Free Reader + Free API tier (500K chars/mo)",
  affiliate=aff(True,
    "Rate not disclosed on official page ('compelling commission structure… high payouts'). Covers Premium, VoiceOver Studio Basic, Studio Pro. Qualified action = signup AND paid-plan purchase within 60 days of click (60-day attribution window). Payout minimum not stated. Old third-party 50/50 revenue-share claim is stale.",
    60, "", "https://speechify.com/affiliates", "verified"))

U("Resemble AI", last_verified=DATE,
  verification_status="partially-verified",
  source_urls=["https://www.resemble.ai/pricing"],
  pricing_tiers=tiers(
    ("Flex", 0, "monthly", "$0/mo pay-as-you-go credits (never expire): Detect audio $0.035/sec, images $0.035/image, video $0.070/sec, Intelligence $0.025/sec, Watermarker encode $0.00050/call, decode $0.00020/call, Agent Detection $1/1,000 sessions; 1 seat"),
    ("Team", 350, "monthly", "$350/mo monthly / $280/mo billed annually"),
    ("Business", 1000, "monthly", "$1,000/mo monthly / $800/mo billed annually"),
    ("Enterprise", None, "custom", "Contact sales")),
  free_plan_details="Flex tier: $0/mo pay-as-you-go credits",
  affiliate=aff(False, "", None, "", "", "none-found"))

U("WellSaid Labs", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://www.wellsaid.io/pricing"],
  pricing_tiers=tiers(
    ("Trial", 0, "monthly", "3 download min/mo, no commercial rights, no credit card"),
    ("Starter", 19, "monthly", "$19/mo billed monthly; $10/mo billed annually ($120/yr, save 47%; 240 min/yr)"),
    ("Pro", 49, "monthly", "$49/mo billed monthly; $33/mo billed annually ($396/yr; 180 min/mo, 2,160 min/yr)"),
    ("Business", 160, "annual-monthly", "$160/user/mo billed annually ($1,920/yr/user; 2,880 min/yr/user, up to 5 seats)"),
    ("Enterprise", None, "custom", "Contact sales")),
  free_plan_details="Trial: 3 download minutes/month, no commercial usage rights, no card required",
  affiliate=aff(False,
    "No public affiliate program on official pages. Third-party press mentions a June 2025 'WellSaid Partner Program,' but it is B2B API co-selling with no wellsaid.io page — not a public affiliate program.",
    None, "", "", "none-found"))

U("Lovo", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://lovo.ai/pricing", "https://lovo.ai/affiliate-program"],
  pricing_tiers=tiers(
    ("Basic", 24, "monthly", "$24/mo ($288/yr); 2 hrs/mo generation, 500+ voices, 5 clones, 120 min/mo auto subtitles, 30 GB, 10 projects, 1080p export"),
    ("Pro", 24, "monthly", "$24/mo ($288/yr); 5 hrs/mo, unlimited clones, Pro V2 voices, AI writer/SFX, team collab, priority queue, 100 GB, 50 projects"),
    ("Pro+", 75, "monthly", "$75/mo ($900/yr); 20 hrs/mo, 300 min/mo subtitles, priority support, unlimited projects, 400 GB"),
    ("Enterprise", None, "custom", "Contact sales")),
  free_plan_details="Free-tier terms not stated on official page ('Start now for free' CTAs only) — unverified",
  affiliate=aff(True,
    "20% recurring for 24 months on all new customers; no minimums; paid monthly; approval ~1 week; cookie and payout minimum not stated on official page",
    None, "", "https://lovo.ai/affiliate-program", "verified"))

U("Podcastle", last_verified=DATE,
  verification_status="partially-verified",
  source_urls=["https://podcastle.ai/pricing", "https://podcastle.ai/affiliate", "https://async.com/pricing"],
  free_plan_details="Free: lifetime quotas (no card required) — 10 AI credits lifetime, 1 hr lifetime media minutes to AI chat, 1 hr lifetime remote recording, 2 hr lifetime transcription (shared), ~15 min (~12k chars) lifetime TTS, 2 GB storage, 720p max, watermarked",
  affiliate=aff(True,
    "Async Affiliate Program (in-house, not via a network): 25% commission on every eligible subscription (no tiers stated); cookie length and payout minimum not stated on official page",
    None, "", "https://podcastle.ai/affiliate", "verified"))

U("Listnr", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://listnr.tech/pricing", "https://listnr.AI/affiliate"],
  pricing_tiers=tiers(
    ("Free", 0, "monthly", "1,000 credits one-time grant (not a monthly quota), 1,000+ voices preview, 142+ languages/accents, Studio access; no credit card"),
    ("Individual", 19, "monthly", "$19/mo ($190/yr — 2 months free on yearly); 20,000 credits/mo ~2 hrs voice, 50 GB, 50 videos/mo, unlimited downloads/exports, commercial rights"),
    ("Solo", 39, "monthly", "$39/mo ($390/yr); 50,000 credits/mo ~5 hrs, 100 GB, 150 videos/mo"),
    ("Agency", 99, "monthly", "$99/mo ($990/yr); 250,000 credits/mo ~25 hrs, 250 GB, 250 videos/mo"),
    ("Custom/Enterprise", None, "custom", "Custom proposal")),
  free_plan_details="Free: 1,000 credits one-time grant to start, no credit card",
  affiliate=aff(True,
    "Tiered: 30% starter / 35% at 30 active referrals / 40% at 50+ customers — recurring across a 12-month commission period; managed via Tolt; cookie and payout minimum not stated on official page",
    None, "", "https://listnr.AI/affiliate", "verified"))

U("Coqui", last_verified=DATE,
  verification_status="unverified",
  source_urls=["https://coqui.ai"],
  affiliate=aff(False, "", None, "", "", "none-found"))

# ============ EDITING BATCH ============
U("Submagic", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://submagic.co/pricing", "https://www.submagic.co/affiliate"],
  pricing_tiers=tiers(
    ("Starter", 19, "monthly", "$19/mo monthly / $12/mo billed annually; 45 credits = 15 videos/mo, 2-min duration, 1080p, no watermark"),
    ("Pro", 39, "monthly", "$39/mo monthly / $23/mo billed annually; 120 credits = 40 videos/mo, 5-min duration, Storyblocks B-roll, AI zooms/clean audio"),
    ("Business", 69, "monthly", "$69/mo monthly / $41/mo billed annually; 300 credits = 100 videos/mo, 30-min duration, 4K/60fps, brand assets"),
    ("Custom", None, "custom", "Custom quote: custom videos/minutes/members, SSO, dedicated success")),
  affiliate=aff(True,
    "30% recurring for life; payouts on the 7th of each month via PayPal; $50 minimum; promo-code sales also tracked; cookie length not stated on official page",
    None, "$50", "https://www.submagic.co/affiliate", "verified"))

U("Captions", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://captions.ai/pricing", "https://www.captions.ai/affiliates"],
  affiliate=aff(False,
    "No affiliate program on official pages — https://www.captions.ai/affiliates returns 404. Third-party directories conflict (20% recurring/12mo vs 25%) and are not used.",
    None, "", "", "none-found"))

U("Vizard", last_verified=DATE,
  verification_status="unverified",
  source_urls=["https://vizard.ai/pricing",
               "https://help.vizard.ai/en/articles/8771871-how-to-join-the-affiliate-program",
               "https://vizard.ai/affiliate"])

U("OpusClip", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://www.opus.pro/pricing", "https://www.opus.pro/affiliate"],
  pricing_tiers=tiers(
    ("Free", 0, "monthly", "Watermarked captions, 1080p renders, exports expire after 3 days"),
    ("Starter", 15, "monthly", "Virality Score, animated captions, 9:16 output, 1 brand template, 30-day export window"),
    ("Pro", 29, "monthly", "Everything in Starter + 4K, scheduling, 6 social connections, 2-seat workspace, 100GB storage, API, XML export"),
    ("Business", None, "custom", "Customized capacity, seats, API, MSA")),
  affiliate=aff(True,
    "25% recurring through the first year of each referred subscriber; paid automatically on the 15th of each month to PayPal; $20 minimum; approval ~1 week; no paid-media ads allowed; cookie length not stated on official page",
    None, "$20", "https://www.opus.pro/affiliate", "verified"))

U("Riverside", last_verified=DATE,
  verification_status="partially-verified",
  source_urls=["https://riverside.fm/pricing", "https://riverside.getrewardful.com/terms"],
  free_plan_details="Free-plan status AMBIGUOUS on 2026-10-05: a third-party review claims Riverside's own Sep 10, 2026 article says the free plan was replaced by 14-day trials, but the official pricing FAQ still reads as listing free-plan-like structure — NOT confirmed from official pages. Verify the live signup flow before publishing.",
  affiliate=aff(True,
    "Program exists (tracked via Rewardful or Impact; applications reviewed for brand fit; contact affiliates@riverside.com). Commission rate, cookie length, and payout minimum are NOT publicly disclosed — detailed in affiliate dashboard or separate agreement.",
    None, "", "https://riverside.getrewardful.com/terms", "verified"))

U("Descript", last_verified=DATE,
  verification_status="partially-verified",
  source_urls=["https://www.descript.com/pricing", "https://www.descript.com/affiliate",
               "https://www.descript.com/affiliate-terms"],
  pricing_tiers=tiers(
    ("Free", 0, "monthly", "60 media min/mo, 100 one-time AI credits, 720p watermarked exports"),
    ("Hobbyist", None, "monthly", "Per person/mo (dollar price JS-gated, not extractable); 10 media hrs/mo, 400 AI credits, 1080p watermark-free"),
    ("Creator", None, "monthly", "Per person/mo (dollar price JS-gated); 30 media hrs/mo, 800 AI credits, 4K, full Underlord AI suite"),
    ("Business", None, "monthly", "Per person/mo (dollar price JS-gated); 40 media hrs/mo, 1500 AI credits, Brand Studio, translate/dub 30+ languages"),
    ("Enterprise", None, "custom", "Contact sales")),
  free_plan_details="Free: 60 media min/month, 100 one-time AI credits",
  affiliate=aff(True,
    "$25 flat one-time payment per new qualifying subscription (Creator/Pro eligible products); 30-day cookie; initial term only, no renewals; via PartnerStack; $100,000/yr per-affiliate cap (official affiliate terms, last updated Feb 28, 2024)",
    30, "", "https://www.descript.com/affiliate-terms", "verified"))
# note: annual billing saves up to 35% over monthly

U("Flixier", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://flixier.com/help/pricing-plans-explained", "https://flixier.com/affiliate-program"],
  affiliate=aff(True,
    "50% commission on monthly plans / 25% on annual plans; 120-day cookie; payouts monthly; managed via FirstPromoter; payout threshold not stated on official page",
    120, "", "https://flixier.com/affiliate-program", "verified"))

U("Wisecut", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://wisecut.ai/pricing", "https://www.wisecut.video/"],
  affiliate=aff(False,
    "No affiliate program page, terms, or signup on official pages (wisecut.video or wisecut.ai). Third-party claims are stale/conflicting (15% via Impact, 938+ days old) and not used.",
    None, "", "", "none-found"))

U("Gling", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://gling.ai/pricing", "https://affiliates.gling.ai/signup"],
  affiliate=aff(True,
    "20% commission on all payments within the first 12 months; tracked via Rewardful; payouts monthly via Wise; $100 minimum payment threshold (rolls over); cookie length not stated on official pages",
    None, "$100", "https://affiliates.gling.ai/signup", "verified"))

U("Timebolt", last_verified=DATE,
  verification_status="verified",
  source_urls=["https://www.timebolt.io/pricing", "https://www.timebolt.io/affiliate-zone"],
  affiliate=aff(True,
    "Standard: 20% of the first payment (annual and lifetime pay full commission up front in one transaction); Partner Creator: 20% on every payment including renewals for as long as the customer stays (entry: 20k+ YouTube subs OR 20 paying customers referred); payouts via PayPal on the 15th of each month via ThriveCart; affiliates must be paid customers; cookie not stated. (Note: an older official blog post describes 10% + 5% coupon — the current affiliate-zone page (20%) is treated as current.)",
    None, "", "https://www.timebolt.io/affiliate-zone", "verified"))

# ============ VERIFICATION NOTES (per-tool, dated) ============
NOTES = {
 "Pictory": f"2026-10-05: plan structure confirmed (Starter/Professional/Teams/Enterprise); prices JS-rendered, not extractable — carried tiers are not re-confirmed. Page title: 'Pictory Pricing | From $25 per Month'. NEW: official partner page pictory.ai/partner-with-pictory confirms an affiliate program, but no rates/terms stated.",
 "InVideo": f"2026-10-05: verified — zero drift. Annual-monthly prices $20/$36/$75 re-confirmed on compare table; Free plan exists; unused credits don't roll over. Affiliate 50%/25% re-confirmed; cookie/payout carried from 2026-10-01 (in collapsed FAQ, not re-extracted).",
 "Fliki": f"2026-10-05: structure confirmed, prices JS-rendered (not re-confirmed). Official page self-conflict: plan table says Premium 'Videos upto 40 minutes', FAQ twice says 30 minutes max — flagged. Active promo banner: FLIKIEXPLAINER40 = 40% off annual plans (time-limited). Affiliate 30% lifetime/30-day/$50 re-verified exactly.",
 "Lumen5": f"2026-10-05: pricing page failed to fetch (no HTTP status) — pricing stays unverified. Homepage renders normally; company operating (not shut down). Official help center states verbatim: 'Lumen5 does not have an affiliate or referral program at this time' — contradicts third-party directories claiming one.",
 "VEED": f"2026-10-05: pricing page JS-rendered — prices not extractable; Lite/Pro figures carried from prior runs, not re-confirmed → status unverified. Affiliate 20%+20%/bonuses up to 50% via Impact re-verified exactly.",
 "Kapwing": f"2026-10-05: verified — zero drift. Pro $24/mo ($16/mo annual), Business $64/mo ($50/mo annual) re-confirmed incl. annual-discount FAQ. Affiliate portal self-contradiction: tiers show 25/30/35% (Platinum 35%) but page copy says 'up to 25%' for top affiliates (likely typo — use tier table).",
 "Runway": f"2026-10-05: verified — zero price drift. Feature text updated: official model lineup is now Gen-4.5, Gen-4 Turbo, Kling 3.0, Nano Banana Pro, Seedance 2.5 (dataset's 'Gen-3/Gen-4' was stale).",
 "Pika": f"2026-10-05: verified — zero drift. Annual saves 20% re-confirmed on compare table.",
 "Steve AI": f"2026-10-05: tier structure confirmed (Free/Basic/Starter/Pro/Enterprise), but dollar prices JS-rendered — pricing stays unverified. Affiliate: program verified; 'up to 40% commission' — recurring NOT stated on the official page (dataset nuance corrected).",
 "FlexClip": f"2026-10-05: plan names Free/Plus/Business confirmed; numeric prices JS-rendered (FAQ only) — carried figures not re-confirmed. Affiliate 35%+/90-day cookie/Awin platform re-verified exactly.",
 "HeyGen": f"2026-10-05: verified — prices and FAQ content-level re-verified, no changes. Affiliate terms re-verified (35%/3mo, 30-day cookie, $30 PayPal min, 60-day verification hold).",
 "Synthesia": f"2026-10-05: verified — Basic free (500 credits/mo), Starter $29/mo, Pro $89/mo, Enterprise re-confirmed. Plan renamed Creator → Pro vs older data. Affiliate terms fully re-verified.",
 "Colossyan": f"2026-10-05: verified — PLAN LINEUP CHANGED since 2026-10-01: 'Business' ($88/$70) is gone; Professional is the mid tier at $59/mo (annual, per FAQ) and Starter is free. Affiliate re-verified (25%→50% tiered, up to a year, 90-day cookie).",
 "Elai": f"2026-10-05: pricing page loaded but plan cards JS-rendered — pricing stays unverified. Affiliate FULLY VERIFIED on official pages (25%/first 12 months, monthly via Rewardful, Enterprise excluded). Pricing needs a live-browser check.",
 "D-ID": f"2026-10-05: pricing page JS-rendered — pricing stays unverified (same as 2026-10-01). Affiliate: INVITE-ONLY with non-commercial-sharing terms (affiliation fee = lower of first two months' net fees minus 6%, $30 aggregate threshold). Do NOT present D-ID as an open affiliate program.",
 "DeepBrain AI": f"2026-10-05: FULLY VERIFIED (was unverified). AI Studios Free $0 / Personal $24/mo / Team $55/seat/mo / Enterprise; LiveAvatar Free $0 / Standard $99/mo / Enterprise; 20% off with annual billing. Affiliate 40%/6mo/60-day/$30 re-confirmed exactly.",
 "Hour One": f"2026-10-05: pricing FULLY VERIFIED (was unverified): Free Trial $0 (3 min total) / Lite $30 ($24 annual) / Business $112 ($96 annual) / Enterprise. Affiliate: hourone.ai/affiliate-program returned HTTP 500 — program existence INCONCLUSIVE; prior terms (20%/12mo/$250) carried as unverified. Needs a live-browser check.",
 "Tavus": f"2026-10-05: verified — Developer Basic free / Starter $59+PAYG / Growth $397+PAYG (1,250 CVI min — older third-party '500' figure is stale) / Enterprise; PALs Free/Plus $20/Max $50. No public self-serve affiliate program — referral partnerships are contact-based; no rate listed.",
 "Vidnoz": f"2026-10-05: structure confirmed (credit-based plans, 3,200+ templates, 1,800–1,900+ avatars); dollar prices JS-rendered — their own blog posts contradict each other on prices, so no verified price. Affiliate program UNDER CONSTRUCTION (official waitlist) — tracking links likely dead. Pricing needs a live-browser check.",
 "Synthesys": f"2026-10-05: verified — Starter $29 ($20 annual) / Pro $59 ($41) / Agency $119 ($83) / Max $199 ($139) / credit packs. PIVOT: now an 'AI Video Agent' for ad creation (UGC ads, TV commercials, faceless stories) — not a classic avatar/presenter tool; hub copy is stale. No current affiliate page on official site (stale ~2023 blog mention unverified).",
 "ElevenLabs": f"2026-10-05: whole elevenlabs.io domain policy-blocked in this environment — no official page readable. Pricing and affiliate stay unverified. Live-browser check spawned 2026-10-05 (pending).",
 "Murf": f"2026-10-05: pricing page read — TTS API figures verified ($10/mo free credit; Falcon $0.01/1,000 chars); Studio tiers JS-rendered (prices not re-confirmed). Affiliate FULLY VERIFIED: 20% recurring/24mo, 90-day cookie, PartnerStack, monthly payouts.",
 "PlayHT": f"2026-10-05: play.ht/pricing DNS resolution failed (domain unreachable) — pricing stays unverified. Third-party reports of PlayAI rebrand + Meta acquisition + shutdown remain unconfirmed via official sources. Tool NOT removed per policy; recommend live confirmation of shutdown status before delisting.",
 "Speechify": f"2026-10-05: FULLY VERIFIED — Reader Free $0 / Premium $29/mo; API Free $0 / Starter $10 / Pro $99 / Scale $499 / Enterprise. Affiliate page live; rate undisclosed (old 50/50 claim stale); 60-day attribution window.",
 "Resemble AI": f"2026-10-05: PIVOT RE-CONFIRMED — homepage is now 'Multimodal Deepfake Detection and Watermarking for Enterprise'; consumer voice tiers are GONE from the official site. Current pricing read: Flex $0 / Team $350 ($280 annual) / Business $1,000 ($800 annual) / Enterprise. No affiliate program on official pages. Recommend removing from voice comparisons (kept per no-delete policy).",
 "WellSaid Labs": f"2026-10-05: verified — Trial $0 / Starter $19 ($10 annual) / Pro $49 ($33 annual) / Business $160/user/mo annual / Enterprise. Creator tier rebranded to Starter with lower entry pricing. No public affiliate program (June 2025 'Partner Program' is B2B co-selling).",
 "Lovo": f"2026-10-05: FULLY VERIFIED (was unverified) — Basic $24 / Pro $24 / Pro+ $75 / Enterprise; 'SAVE UP TO 50% WITH YEARLY' promo banner (may expire). Free-tier terms not stated on page. Affiliate 20% recurring/24mo re-verified.",
 "Podcastle": f"2026-10-05: REBRAND RE-CONFIRMED — product is now 'Async' (pricing page renders 'Pricing | Async'; async.com mirrors podcastle.ai/pricing). Tier structure read (Free/Essentials/Pro/Teams/Enterprise, credit-based) but dollar prices JS-rendered. Affiliate: 25% in-house program verified on official page. Dollar prices need a live-browser check.",
 "Listnr": f"2026-10-05: FULLY VERIFIED (was unverified) — Free (1,000 one-time credits) / Individual $19 / Solo $39 / Agency $99 / Custom; yearly = 10 months charged up front. Affiliate tiered 30/35/40% over 12 months re-verified; official affiliate now at listnr.AI (operates on both listnr.tech and listnr.AI).",
 "Coqui": f"2026-10-05: RED FLAG — coqui.ai no longer belongs to Coqui AI; the domain now serves an Indonesian gambling/slot spam site (UNIKBET) — domain expired, parked, hijacked. Coqui shut down Jan 2024 (founder announcement); only the community fork idiap/coqui-ai-TTS survives (non-commercial, not affiliate-able). Tool kept per no-delete policy but DO NOT link coqui.ai from hub pages (gambling spam). Recommend delisting.",
 "Submagic": f"2026-10-05: verified — Starter $19 ($12 annual) / Pro $39 ($23) / Business $69 ($41) / Custom; credit allowances (45/120/300 = 15/40/100 videos) read on page. Affiliate 30% for life, $50 PayPal min re-verified.",
 "Captions": f"2026-10-05: verified — unchanged (Free $0 / Max $24.99 / Frontier $69.99); footnote: iOS plans only; unused credits roll over up to 3x monthly allowance. No affiliate program (official /affiliates 404).",
 "Vizard": f"2026-10-05: pricing page JS-gated ($0 rendered for paid tiers) — pricing stays unverified. Affiliate 25% (first 12 payments within 12 months), 60-day cookie, $50 min re-verified exactly.",
 "OpusClip": f"2026-10-05: verified — Free $0 / Starter $15 / Pro $29 / Business custom; per-minute credit counts not rendered. Brand now 'multi-model AI video platform' with Agent Opus. Affiliate 25% first year, $20 min, 15th-monthly PayPal re-verified.",
 "Riverside": f"2026-10-05: plan names/prices read via official FAQ (Pro $29→$24 annual / Grow $39→$34 / Webinar $99→$79 / Business) but plan cards JS-gated → partially-verified. Free-plan status AMBIGUOUS (third-party claims Sep 2026 article replaced free plan with trials — not confirmed from official pages). Affiliate program exists; terms undisclosed publicly.",
 "Descript": f"2026-10-05: plan structure, media hours, and AI credits read on official page (only dollar figures JS-gated) → partially-verified. Annual saves up to 35%. Affiliate $25 flat/30-day cookie re-verified on official terms (Feb 2024).",
 "Flixier": f"2026-10-05: verified — Free $0 / Starter $19 / Creator $39 / Business $69; yearly saves up to 56%. Affiliate 50%/25% re-verified; 120-day cookie.",
 "Wisecut": f"2026-10-05: verified — Free $0 / Starter+ $23.25/mo annual ($279/yr) / Professional+ $83.25/mo annual ($999/yr); credit system (300/1,200 credits/mo); annual saves up to 30%; monthly equivalents not shown. No affiliate program on official pages.",
 "Gling": f"2026-10-05: verified — Free $0 / Plus $20 ($10 annual) / Pro $40 ($20) / Elite $100 ($50). Affiliate 20%/12mo, $100 Wise min re-verified.",
 "Timebolt": f"2026-10-05: verified — Free $0 / Pro $17/mo ($97/yr, $347 lifetime) / Teams $97/seat/yr / Vault custom; UMCHECK $0.03/min pay-per-use. Affiliate: current official page says 20% (older blog says 10% — current page used).",
}

def main():
    with open(PATH) as f:
        data = json.load(f)
    tools = data["tools"]
    byname = {t["name"]: t for t in tools}
    applied, missing = [], []
    for name, kw in UPDATES.items():
        t = byname.get(name)
        if not t:
            missing.append(name); continue
        for k, v in kw.items():
            t[k] = v
        note(t, NOTES[name])
        applied.append(name)
    data["verified_on"] = DATE
    with open(PATH, "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"applied={len(applied)} missing={missing}")

if __name__ == "__main__":
    main()
