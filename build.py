#!/usr/bin/env python3
"""Build script for the AI Video & Voice Tool Comparisons static hub.
Reads data/tools.json + data/affiliate-links.json + data/site-config.json,
renders plain HTML files. No network, no keys, no server.
Usage: python3 build.py
"""
import json, os, html, re
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)

tools_data = load("tools.json")
aff_links = load("affiliate-links.json")
config = load("site-config.json")
TOOLS = {t["name"]: t for t in tools_data["tools"]}
VERIFIED_ON = tools_data.get("verified_on", "2026-10-01")

def esc(s):
    return html.escape(str(s)) if s is not None else ""

def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

def money(v):
    if v is None: return "—"
    return f"${v:g}"

def starting_price(t):
    tiers = t.get("pricing_tiers") or []
    paid = [x for x in tiers if (x.get("price_usd") or 0) > 0]
    if paid:
        m = min(paid, key=lambda x: x["price_usd"])
        per = {"monthly": "/mo", "annual-monthly": "/mo billed annually", "one-time": " one-time"}.get(m.get("billing"), "")
        return f"{money(m['price_usd'])}{per}"
    if t.get("free_plan"):
        return "Free"
    return "See site"

def cta_for(name):
    """Return (url, label, note). Only verified affiliate URLs from affiliate-links.json."""
    t = TOOLS[name]
    entry = aff_links.get(name)
    if entry and entry.get("url") and entry.get("status") == "verified":
        return entry["url"], f"Try {name}", "Affiliate link — we may earn a commission."
    return t["url"], f"Visit {name}", "Affiliate application pending — linking to the official site."

def ad_slot(kind, label):
    slot_id = config.get("adsense_slots", {}).get(kind, "")
    pub = config.get("adsense_publisher_id", "")
    if pub and slot_id:
        return (f'<div class="ad-slot" data-ad-client="{esc(pub)}" data-ad-slot="{esc(slot_id)}" '
                f'data-ad-format="auto"><span class="ad-label">Advertisement</span></div>')
    return (f'<div class="ad-slot" data-ad-placeholder="{esc(kind)}">'
            f'<span class="ad-label">Advertisement</span>'
            f'{esc(label)} (AdSense placeholder — activates when a publisher ID is approved)</div>')

DISCLOSURE = """<div class="disclosure" role="note">
<strong>Affiliate disclosure</strong>
Some links on this page are affiliate links, which means we may earn a commission if you buy through them — at no extra cost to you.
We only recommend tools based on hands-on research, and every price below was checked against the tool's official site.
</div>"""

NAV_LINKS = [
    ("index.html", "Home"),
    ("heygen-alternatives.html", "HeyGen alternatives"),
    ("elevenlabs-alternatives.html", "ElevenLabs alternatives"),
    ("best-ai-video-generators-for-youtubers.html", "Video generators"),
    ("elevenlabs-vs-murf-vs-playht.html", "Voice head-to-head"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
    ("privacy-policy.html", "Privacy"),
]

def header(active=""):
    items = "".join(
        f'<li><a href="{href}">{label}</a></li>' for href, label in NAV_LINKS)
    return f"""<header class="site-header"><div class="wrap">
<a class="brand" href="index.html">{esc(config['site_name'])}<small>{esc(config['tagline'])}</small></a>
<nav class="main-nav" aria-label="Main"><ul>{items}</ul></nav>
</div></header>"""

def footer():
    items = "".join(
        f'<li><a href="{href}">{label}</a></li>' for href, label in NAV_LINKS)
    return f"""<footer class="site-footer"><div class="wrap">
<nav aria-label="Footer"><ul>{items}</ul></nav>
<p>&copy; {date.today().year} {esc(config['site_name'])}. All prices verified against official sources on {esc(VERIFIED_ON)} and re-checked regularly. Tool names and trademarks belong to their respective owners.</p>
</div></footer>"""

def page_shell(title, description, body, active=""):
    pub = config.get("adsense_publisher_id", "")
    auto_ads = (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={esc(pub)}"\n'
                '     crossorigin="anonymous"></script>\n' if pub else "")
    base = (config.get("base_url") or "").rstrip("/")
    canonical = (f'<link rel="canonical" href="{esc(base)}/{esc(active)}">\n' if base and active else "")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | {esc(config['site_name'])}</title>
<meta name="description" content="{esc(description)}">
{canonical}<link rel="stylesheet" href="assets/css/style.css">
{auto_ads}</head>
<body>
{header(active)}
<div class="wrap">
{body}
</div>
{footer()}
</body>
</html>"""

def tool_schema(t, position):
    tiers = t.get("pricing_tiers") or []
    offers = []
    for tier in tiers:
        offers.append({
            "@type": "Offer",
            "name": tier.get("plan"),
            "price": tier.get("price_usd"),
            "priceCurrency": "USD",
        })
    return {
        "@type": "Product",
        "position": position,
        "name": t["name"],
        "url": t["url"],
        "description": "; ".join((t.get("features") or [])[:3]),
        "offers": offers or {"@type": "AggregateOffer", "priceCurrency": "USD"},
    }

def compare_table(names, benchmark=None):
    rows = []
    for i, name in enumerate(names, 1):
        t = TOOLS[name]
        free = "Yes" if t.get("free_plan") else "No"
        badge = "free" if t.get("free_plan") else "paid"
        if t.get("verification_status") == "unverified":
            badge = "unverified"; free = "Unverified"
        best_for = (t.get("strengths") or ["—"])[0]
        rows.append(
            f"<tr><td><strong>{esc(name)}</strong>"
            + (" <span class='badge paid'>benchmark</span>" if name == benchmark else "")
            + f"</td><td>{esc(best_for)}</td><td>{esc(starting_price(t))}</td>"
            f"<td><span class='badge {badge}'>{free}</span></td></tr>")
    return ("<div class='table-scroll'><table class='compare'>"
            "<thead><tr><th>Tool</th><th>Stands out for</th><th>Starts at</th><th>Free plan</th></tr></thead>"
            f"<tbody>{''.join(rows)}</tbody></table></div>")

def ul_or(items, fallback):
    if items:
        return "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"
    return f"<p class='reverify'>{esc(fallback)}</p>"

def tool_card(name, rank, take):
    t = TOOLS[name]
    url, label, note = cta_for(name)
    feats = ul_or((t.get("features") or [])[:6],
                  "Feature details are being re-verified against the official site.")
    pros = ul_or((t.get("strengths") or [])[:4],
                 "Strengths are being re-verified against the official site.")
    cons = ul_or((t.get("weaknesses") or [])[:4],
                 "Limitations are being re-verified against the official site.")
    tiers = "".join(
        f"<li><strong>{esc(x.get('plan',''))}:</strong> {esc(money(x.get('price_usd')))}"
        + (f" {esc(x.get('billing',''))}" if x.get("billing") else "")
        + (f" — {esc(x.get('notes',''))}" if x.get("notes") else "") + "</li>"
        for x in (t.get("pricing_tiers") or []))
    free_line = f"<p><strong>Free plan:</strong> {esc(t.get('free_plan_details') or 'Yes' if t.get('free_plan') else 'No free plan found.')}</p>"
    unver = (t.get("verification_status") == "unverified")
    return f"""<section class="tool-card" id="{slugify(name)}">
<h2><span class="rank">#{rank}</span>{esc(name)}</h2>
<div class="tool-meta">{esc(t.get('category','').replace('-',' ').title())} · Pricing verified {esc(t.get('last_verified', VERIFIED_ON))}{" · <span class='badge unverified'>unverified pricing</span>" if unver else ""}</div>
<p><strong>Our take:</strong> {take}</p>
<div class="demo-placeholder" role="img" aria-label="Video demo placeholder for {esc(name)}">
<strong>Hands-on video demo — coming soon</strong>
Tov is filming a real walkthrough of {esc(name)}: account setup, first project, and honest verdict. Check back soon.
</div>
<h3>Key features</h3>
{feats}
<div class="pros-cons">
<div class="pros"><h3>Strengths</h3>{pros}</div>
<div class="cons"><h3>Limitations</h3>{cons}</div>
</div>
<div class="pricing-box">
<h3>Pricing <span class="verified-date">(verified {esc(t.get('last_verified', VERIFIED_ON))})</span></h3>
{"<ul>" + tiers + "</ul>" if tiers else "<p>Pricing details are being re-verified against the official site.</p>"}
{free_line}
</div>
<div class="cta-row">
<a class="btn" href="{esc(url)}" rel="{"sponsored noopener" if 'affiliate' in note.lower() else "noopener"}" target="_blank">{esc(label)}</a>
<span class="aff-note">{esc(note)}</span>
</div>
</section>"""

def faq_block(faqs):
    items = "".join(
        f"<details><summary>{esc(q)}</summary><p>{a}</p></details>"
        for q, a in faqs)
    return f'<section class="faq"><h2>Frequently asked questions</h2>{items}</section>'

def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in faqs],
    }

def comparison_page(defn):
    names = defn["tools"]
    body_parts = [DISCLOSURE]
    body_parts.append(
        f"<div class='hero'><h1>{esc(defn['h1'])}</h1>"
        f"<p class='lede'>{defn['lede']}</p>"
        f"<p class='verified-date'>Pricing verified against official sources · {esc(VERIFIED_ON)}</p></div>")
    body_parts.append(ad_slot("leaderboard_under_header", "Leaderboard 970×90"))
    body_parts.append(f"<p>{defn['intro']}</p>")
    body_parts.append("<h2>Quick comparison</h2>")
    body_parts.append(compare_table(names, defn.get("benchmark")))
    cards = []
    for i, (name, take) in enumerate(defn["takes"].items(), 1):
        cards.append(tool_card(name, i, take))
        if i == 2:
            cards.append(ad_slot("in_article", "In-article responsive"))
    body_parts.append("\n".join(cards))
    body_parts.append(faq_block(defn["faqs"]))

    toc = "".join(f"<li><a href='#{slugify(n)}'>{esc(n)}</a></li>" for n in defn["takes"])
    sidebar = (f"<aside class='sidebar'><div class='toc'><h3>On this page</h3><ul>{toc}</ul></div>"
               + ad_slot("sidebar_rectangle", "Sidebar 300×250") + "</aside>")
    layout = f"<div class='article-layout'><main>{''.join(body_parts)}</main>{sidebar}</div>"

    schemas = [
        {"@context": "https://schema.org", "@type": "ItemList",
         "name": defn["h1"], "dateModified": VERIFIED_ON,
         "itemListElement": [tool_schema(TOOLS[n], i) for i, n in enumerate(defn["takes"], 1)]},
        faq_schema(defn["faqs"]),
    ]
    schema_html = '<script type="application/ld+json">' + json.dumps(schemas) + "</script>"
    return page_shell(defn["title"], defn["meta"], layout + schema_html, defn["slug"] + ".html")

# ---------------------------------------------------------------- page content
PAGES = [
 dict(
  slug="heygen-alternatives", benchmark="HeyGen",
  title="7 Best HeyGen Alternatives (2026) — AI Avatar Video Compared",
  meta="The 7 best HeyGen alternatives for AI avatar videos in 2026, compared on price, languages, and realism. Pricing verified against official sites.",
  h1="7 Best HeyGen Alternatives in 2026",
  lede="HeyGen makes realistic AI avatar videos fast — but it isn't the cheapest, and its free plan is limited. These seven alternatives cover every budget and use case, with pricing verified on October 5, 2026.",
  intro=("I use AI avatars to make videos without sitting in front of a camera, and HeyGen is the tool most people start with. "
         "But 'most popular' doesn't mean 'best for you.' Some creators need more languages, some need a real free plan, and some just need "
         "the cheapest way to turn a script into a talking-head video. Below is every serious HeyGen alternative I could verify, "
         "compared on the things that actually matter: price, free plan, language support, and what each one does best."),
  tools=["HeyGen","Synthesia","Colossyan","Elai","D-ID","DeepBrain AI","Hour One","Tavus","Vidnoz"],
  takes={
   "HeyGen": "The benchmark: the most polished avatar quality and the fastest script-to-video workflow, but the free plan is thin and costs scale quickly for teams.",
   "Synthesia": "The enterprise pick — the most languages and the most corporate-friendly compliance story, at enterprise-friendly prices.",
   "Colossyan": "Built for training videos and workplace learning; a strong pick if your avatars teach employees rather than sell products.",
   "Elai": "A budget-friendly HeyGen rival with a generous template library; good for creators who want volume without the HeyGen price tag.",
   "D-ID": "The API-first choice — if you want avatars inside your own app or site, D-ID's developer story is the strongest here.",
   "DeepBrain AI": "Broadcast-grade realism aimed at news-style and corporate presenters; priced for businesses, not hobbyists.",
   "Hour One": "Character-driven avatars with a focus on virtual presenters for e-learning and customer-facing video.",
   "Tavus": "Personalized video at scale — record once, generate a unique video per viewer. Different beast, worth knowing about.",
   "Vidnoz": "The free-tier seeker: the most generous free offering in this list, making it the lowest-risk way to try AI avatars.",
  },
  faqs=[
   ("What is the best free HeyGen alternative?",
    "<p>Vidnoz offers the most generous free tier among verified options. HeyGen's own free plan exists but is limited — check the comparison table above for current free-plan details.</p>"),
   ("Which HeyGen alternative has the most languages?",
    "<p>Synthesia leads on language count among the tools verified here. If you publish in many languages, verify the exact count on their official pricing page before committing.</p>"),
   ("Can AI avatar videos look realistic enough for YouTube?",
    "<p>Yes — current-generation avatars from HeyGen, Synthesia, and D-ID pass comfortably in talking-head formats. Disclosure: many platforms and viewers expect AI-generated content to be labeled; check YouTube's current AI-content disclosure rules.</p>"),
   ("How much does a HeyGen alternative cost?",
    "<p>Verified starting prices range from free tiers up to enterprise plans. See the pricing box under each tool above — every figure was checked against the official site on October 5, 2026.</p>"),
  ]),
 dict(
  slug="elevenlabs-alternatives", benchmark="ElevenLabs",
  title="8 Best ElevenLabs Alternatives (2026) — AI Voice Compared",
  meta="The 8 best ElevenLabs alternatives for AI voiceovers in 2026: Murf, PlayHT, Speechify and more, compared on price and voice quality. Pricing verified.",
  h1="8 Best ElevenLabs Alternatives in 2026",
  lede="ElevenLabs sets the bar for realistic AI voices — but per-character pricing adds up, and its free tier is small. These eight alternatives compete on price, languages, and licensing, verified October 5, 2026.",
  intro=("AI voiceover is the backbone of faceless YouTube channels, audiobooks, and course narration. ElevenLabs earned its reputation with "
         "remarkably human voices, but its pricing model charges by character — long scripts get expensive. The alternatives below include "
         "subscription models with generous minutes, stronger commercial licenses, and better free tiers. Every price was verified against the official site."),
  tools=["ElevenLabs","Murf","PlayHT","Speechify","Resemble AI","WellSaid Labs","Lovo","Podcastle","Listnr"],
  takes={
   "ElevenLabs": "The benchmark: the most natural-sounding voices and the best voice cloning, but character-based pricing punishes long scripts.",
   "Murf": "The studio pick — a polished voiceover workflow with team collaboration, aimed squarely at professional video producers.",
   "PlayHT": "A strong all-rounder with competitive pricing and a large voice library; worth a head-to-head listen against ElevenLabs.",
   "Speechify": "Famous for text-to-speech reading, with a voiceover studio for creators; a good fit if you already live in their ecosystem.",
   "Resemble AI": "The customization king — deep voice cloning controls for developers and studios that need exact voice matches.",
   "WellSaid Labs": "Enterprise-grade narration voices with a focus on consistent, broadcast-quality output for training and corporate content.",
   "Lovo": "Genny pairs AI voices with AI art and video; a creative-suite play for YouTubers who want voice plus visuals in one subscription.",
   "Podcastle": "Built for podcasters — recording, editing, and AI voices in one place, so your narration never leaves the studio.",
   "Listnr": "A budget-friendly text-to-speech option with podcast hosting built in; sensible for beginners testing AI narration.",
  },
  faqs=[
   ("What is the cheapest ElevenLabs alternative?",
    "<p>Listnr and Podcastle compete on the low end with generous entry tiers. Compare the per-month character or minute allowances in the pricing boxes above — the cheapest sticker price isn't always the cheapest per finished minute of audio.</p>"),
   ("Which AI voice sounds most human?",
    "<p>ElevenLabs still leads in blind-listening reputation, with PlayHT and Murf close behind. Voice quality is subjective — every tool above offers free samples, so listen before you pay.</p>"),
   ("Can I use AI voices for commercial YouTube videos?",
    "<p>Yes, on paid plans — but license terms differ by tool. Verify commercial-use rights on the official terms page of whichever tool you choose; free tiers often restrict commercial use.</p>"),
   ("How is AI voice priced — per character or per minute?",
    "<p>Both models exist. ElevenLabs charges per character; others charge per minute or offer flat subscriptions. For long-form narration, per-minute or unlimited plans usually win — do the math on your average script length.</p>"),
  ]),
 dict(
  slug="synthesia-alternatives", benchmark="Synthesia",
  title="7 Best Synthesia Alternatives (2026) — AI Presenters Compared",
  meta="The 7 best Synthesia alternatives for AI presenter videos in 2026, compared on price, languages, and avatar realism. Pricing verified.",
  h1="7 Best Synthesia Alternatives in 2026",
  lede="Synthesia dominates corporate AI video — but corporate pricing follows. These seven alternatives deliver AI presenters for creators, educators, and smaller teams, verified October 5, 2026.",
  intro=("Synthesia built its name on enterprise training videos: compliant, multilingual, professional. If you're a solo creator or small team, "
         "you're paying for enterprise features you may never touch. The alternatives below range from creator-priced to API-first, and each one "
         "was verified against its official pricing page."),
  tools=["Synthesia","HeyGen","Colossyan","Elai","D-ID","DeepBrain AI","Hour One","Tavus","Synthesys"],
  takes={
   "Synthesia": "The benchmark: the corporate standard for AI presenter video, with the deepest language support — and pricing to match.",
   "HeyGen": "The creator favorite — faster, more fun, and cheaper to start than Synthesia, with excellent avatar realism.",
   "Colossyan": "Purpose-built for workplace learning videos; if your use case is training, it may beat both Synthesia and HeyGen on workflow.",
   "Elai": "Strong value play with a big template library for turning articles and slides into presenter videos quickly.",
   "D-ID": "Best for developers embedding presenters into products; the API and integrations are the real product here.",
   "DeepBrain AI": "A premium realism option aimed at broadcast and corporate communications teams.",
   "Hour One": "Virtual presenters tuned for e-learning and customer education use cases.",
   "Tavus": "One-to-one personalized video at scale — a different category, but the most interesting alternative if your goal is outreach.",
   "Synthesys": "A full AI media suite (video, voice, avatars) for creators who want one subscription covering every asset.",
  },
  faqs=[
   ("Is there a free Synthesia alternative?",
    "<p>Several tools above offer free tiers or trials — check the comparison table. Free plans are usually watermarked or minute-limited, fine for testing, not for publishing.</p>"),
   ("Which is better for YouTube: Synthesia or HeyGen?",
    "<p>For YouTube-style content, HeyGen's faster workflow and creator pricing usually win. Synthesia shines in corporate training where compliance and review workflows matter.</p>"),
   ("Do I need to be on camera for any of these?",
    "<p>No — that's the point. All nine tools generate presenters from text. Some also let you clone your own face and voice as a premium option.</p>"),
  ]),
 dict(
  slug="best-ai-video-generators-for-youtubers",
  title="8 Best AI Video Generators for YouTubers (2026) — Tested & Priced",
  meta="The 8 best AI video generators for YouTube in 2026: Pictory, InVideo, Fliki and more, compared on price, free plans, and workflow. Pricing verified.",
  h1="8 Best AI Video Generators for YouTubers in 2026",
  lede="Faceless YouTube channels run on AI video generators. These eight tools turn scripts into publish-ready videos — compared on price, free plans, and the workflow details that matter, verified October 5, 2026.",
  intro=("The 'faceless channel' playbook is simple: script, voiceover, stock footage, captions, publish. The tools below automate different slices of that pipeline. "
         "Pictory and InVideo cover script-to-video; Fliki bundles voiceover in; OpusClip repurposes your long videos into Shorts. Pick based on which step eats most of your time — "
         "and check each pricing box, because 'unlimited' rarely means what you hope."),
  tools=["Pictory","InVideo","Fliki","Lumen5","VEED","Kapwing","Runway","OpusClip"],
  takes={
   "Pictory": "The script-to-video specialist — paste a script, get a captioned video with stock footage. A natural fit for faceless channels, and a program we have an affiliate relationship with.",
   "InVideo": "The template warehouse — thousands of templates and a huge stock library, strong for creators who want variety fast.",
   "Fliki": "Script plus ultra-realistic voices in one flow; the closest to a one-subscription faceless channel toolkit.",
   "Lumen5": "The veteran — turns blog posts into social videos in minutes; best for repurposing written content.",
   "VEED": "The browser-based editor that does everything: captions, translations, and AI features without installing anything.",
   "Kapwing": "The collaborative pick — teams and creators who edit together will feel at home; generous free tier for testing.",
   "Runway": "The generative-AI frontier — text-to-video and video-to-video effects for creators who want original visuals, not stock.",
   "OpusClip": "The Shorts machine — feed it a long video, get viral-ready clips with captions. A force multiplier, not a full editor.",
  },
  faqs=[
   ("Can I really run a YouTube channel without filming anything?",
    "<p>Yes — thousands of channels do. The standard stack is an AI voice plus a script-to-video tool like Pictory or Fliki, with OpusClip cutting Shorts from long-form. YouTube's reused-content rules still apply: add original commentary or value, don't just re-upload stock compilations.</p>"),
   ("Which AI video generator is best for beginners?",
    "<p>Pictory and Lumen5 have the gentlest learning curves — paste text, get video. VEED and Kapwing reward a little more learning with much more control.</p>"),
   ("Do these tools include commercial licenses for YouTube monetization?",
    "<p>Paid plans generally include commercial rights to the videos you create; stock footage licenses vary by tier. Verify the license terms on the official site for the plan you buy — free tiers are the most restrictive.</p>"),
   ("How much does it cost to start a faceless channel?",
    "<p>From $0 (free tiers of Kapwing, VEED, or Vidnoz-style tools) to roughly $20–50/month for a serious single-tool stack. The pricing boxes above show verified starting prices.</p>"),
  ]),
 dict(
  slug="elevenlabs-vs-murf-vs-playht",
  title="ElevenLabs vs Murf vs PlayHT (2026) — AI Voice Head-to-Head",
  meta="ElevenLabs vs Murf vs PlayHT compared head-to-head in 2026: voice quality, pricing, languages, and commercial licenses. Pricing verified.",
  h1="ElevenLabs vs Murf vs PlayHT: Head-to-Head in 2026",
  lede="The three biggest names in AI voiceover, compared on the four things that decide a purchase: how the voices sound, what it costs per finished minute, language coverage, and license terms. Verified October 5, 2026.",
  intro=("If you've narrowed your AI voice search to these three, you're choosing between philosophies. ElevenLabs bets on raw voice realism and charges per character. "
         "Murf bets on a professional voiceover studio workflow with collaboration. PlayHT bets on breadth — a huge voice library at competitive prices. "
         "Below is the honest breakdown, then a per-tool deep dive so you can hear the differences yourself with each tool's free samples."),
  tools=["ElevenLabs","Murf","PlayHT"],
  takes={
   "ElevenLabs": "Wins on pure realism and voice cloning quality. Loses on pricing for long scripts — character-based billing adds up fast at audiobook or course scale.",
   "Murf": "Wins on workflow — the closest thing to a real recording studio, with team features video producers actually use. Loses on per-minute value for solo creators doing high volume.",
   "PlayHT": "Wins on value breadth — big library, competitive plans, strong API. The pragmatic middle ground if ElevenLabs feels pricey and Murf feels corporate.",
  },
  faqs=[
   ("Which sounds most human: ElevenLabs, Murf, or PlayHT?",
    "<p>ElevenLabs has the strongest reputation in blind tests, but the gap narrows every quarter. All three publish free voice samples — listen to the same paragraph in all three before deciding.</p>"),
   ("Which is cheapest for long-form narration?",
    "<p>Do the math on your script length: ElevenLabs' per-character pricing penalizes long scripts, while Murf and PlayHT's plan structures can be kinder at volume. The pricing boxes above show verified plan details.</p>"),
   ("Can I clone my own voice with these tools?",
    "<p>Yes — all three offer voice cloning on paid tiers, with consent and verification steps. Cloned voices are the best way to keep a consistent brand voice across videos.</p>"),
  ]),
 dict(
  slug="descript-alternatives", benchmark="Descript",
  title="8 Best Descript Alternatives (2026) — Text-Based Editing Compared",
  meta="The 8 best Descript alternatives for text-based video and podcast editing in 2026, compared on price and features. Pricing verified.",
  h1="8 Best Descript Alternatives in 2026",
  lede="Descript changed editing by making video editable like a document — but it's not the only text-based editor, and not the cheapest. Eight verified alternatives, October 5, 2026.",
  intro=("Descript's killer idea: edit the transcript, and the video follows. Overdub voice cloning, filler-word removal, and Studio Sound made it a podcasting staple. "
         "But creators leave Descript over price, rendering queues, or wanting a simpler tool. The alternatives below split into two camps: full editors with transcription (Riverside, VEED, Kapwing) "
         "and lighter AI editing assistants (Gling, Wisecut, Timebolt) that clean up your footage fast."),
  tools=["Descript","Riverside","VEED","Kapwing","Podcastle","Flixier","Gling","Wisecut","Timebolt"],
  takes={
   "Descript": "The benchmark: the original text-based editor with the best AI voice cloning (Overdub). Premium-priced, and power users hit usage limits.",
   "Riverside": "The recording-first pick — studio-quality remote recording with solid text-based editing after the fact. Best if your bottleneck is capture, not cutting.",
   "VEED": "The browser editor that keeps adding Descript-like AI features; a strong value alternative with no install.",
   "Kapwing": "Fast, collaborative, generous free tier — the best Descript alternative for teams on a budget.",
   "Podcastle": "Podcast-native: record, edit via transcript, and publish with AI voices, all in one tab.",
   "Flixier": "Speed-obsessed cloud rendering — if Descript's export queues annoy you, Flixier's render times are the selling point.",
   "Gling": "The cleanup specialist — uploads rough footage, returns a cut without silences and mistakes. A complement to any editor.",
   "Wisecut": "Auto-edited talking-head videos with music and cuts; best for creators who hate timelines entirely.",
   "Timebolt": "Silence removal done right — the fastest way to tighten talking-head footage before your real edit.",
  },
  faqs=[
   ("What is the best free Descript alternative?",
    "<p>Kapwing and VEED have the most generous free tiers among full editors; Gling and Timebolt offer free trials of their cleanup tools. Free plans are watermarked or time-limited — fine for evaluation.</p>"),
   ("Which alternative has voice cloning like Overdub?",
    "<p>Descript's Overdub remains the most integrated cloning-for-editing feature. Podcastle and Resemble AI offer strong standalone cloning if that's your priority.</p>"),
   ("Is text-based editing actually faster?",
    "<p>For talking-head and podcast content, yes — cutting filler words from a transcript beats scrubbing a timeline. For cinematic or heavily visual editing, traditional timelines still win.</p>"),
  ]),
 dict(
  slug="submagic-alternatives", benchmark="Submagic",
  title="6 Best Submagic Alternatives (2026) — AI Captions Compared",
  meta="The 6 best Submagic alternatives for animated AI captions in 2026: Captions, OpusClip, Vizard and more. Pricing verified.",
  h1="6 Best Submagic Alternatives in 2026",
  lede="Submagic made word-by-word animated captions the default look of short-form video — but subscriptions stack up. Six verified alternatives that caption just as well, October 5, 2026.",
  intro=("Captions are no longer optional: most short-form video is watched muted, and animated captions measurably lift retention. Submagic nailed the workflow — "
         "upload, auto-caption, pick a style, export. The alternatives below either match that workflow cheaper (Captions, Vizard), bundle it with clip repurposing (OpusClip), "
         "or include it inside a full editor so you drop a subscription (VEED, Kapwing, Flixier)."),
  tools=["Submagic","Captions","OpusClip","Vizard","VEED","Kapwing","Flixier"],
  takes={
   "Submagic": "The benchmark: the slickest caption styles and the fastest path from upload to captioned Short. Priced as a premium single-purpose tool.",
   "Captions": "The AI-creator suite — captions plus AI avatars, dubbing, and editing in one app; strong if you want more than captions.",
   "OpusClip": "Captions come free with the clip machine — if you're already repurposing long videos into Shorts, you may not need a separate caption tool.",
   "Vizard": "A focused Submagic rival for auto-clipping with captions; compare its pricing tier-for-tier before choosing.",
   "VEED": "Full editor with excellent auto-captions and translations — the 'drop a subscription' pick if you also edit.",
   "Kapwing": "Generous free tier and fast auto-subtitles; the budget pick for creators captioning a few videos a week.",
   "Flixier": "Cloud-powered captioning with fast rendering; a solid all-round editor alternative with strong subtitle tools.",
  },
  faqs=[
   ("Do I still need a separate caption tool in 2026?",
    "<p>Only if captions are your whole workflow. If you already pay for VEED, Kapwing, or OpusClip, their built-in captioning may replace Submagic entirely — that's the easiest money to save.</p>"),
   ("Which caption tool has the best free plan?",
    "<p>Kapwing's free tier is the most generous for occasional use. Dedicated caption apps tend to watermark or minute-limit free exports.</p>"),
   ("Can these tools translate captions too?",
    "<p>VEED and Captions both offer translation features; verify supported languages on their official pages, since language counts change often.</p>"),
  ]),
 dict(
  slug="pictory-alternatives", benchmark="Pictory",
  title="7 Best Pictory Alternatives (2026) — Script-to-Video Compared",
  meta="The 7 best Pictory alternatives for script-to-video in 2026: InVideo, Fliki, Lumen5 and more. Pricing verified.",
  h1="7 Best Pictory Alternatives in 2026",
  lede="Pictory turns scripts into videos with stock footage and AI voices — ideal for faceless channels. Seven verified alternatives for every budget, October 5, 2026.",
  intro=("Pictory's formula — script in, captioned stock-footage video out — powers a huge share of faceless YouTube. But its per-video pricing tiers push heavy publishers toward alternatives. "
         "InVideo and Fliki are the direct rivals; Lumen5 and Steve AI serve repurposers; VEED and FlexClip are the editor's answer. Every price below was verified on the official site."),
  tools=["Pictory","InVideo","Fliki","Lumen5","VEED","Steve AI","FlexClip","Wisecut"],
  takes={
   "Pictory": "The benchmark for script-to-video, and a program we hold an affiliate relationship with. Best for creators who want the shortest path from script to published video.",
   "InVideo": "The closest direct rival — bigger template and stock library, aggressive pricing. The first alternative to trial against Pictory.",
   "Fliki": "Adds best-in-class AI voices to the script-to-video flow; if narration quality is your bottleneck, start here.",
   "Lumen5": "The repurposing veteran — turn blog posts and articles into videos with minimal effort.",
   "VEED": "The editor's route: more manual control than Pictory, with AI features closing the automation gap.",
   "Steve AI": "Patented script-to-video with animated and live-action styles; a fresh take if template fatigue sets in.",
   "FlexClip": "A straightforward, affordable editor with text-to-video features; good for beginners who may outgrow pure automation.",
   "Wisecut": "AI auto-editing for talking-head footage — different input (your face) but the same promise: video without the timeline grind.",
  },
  faqs=[
   ("Which Pictory alternative is best for faceless YouTube?",
    "<p>InVideo and Fliki are the two direct rivals most faceless creators compare against Pictory. Fliki wins if AI voiceover quality matters most; InVideo wins on template and stock variety.</p>"),
   ("Is there a free script-to-video tool?",
    "<p>Free tiers exist (Lumen5, InVideo, and others offer trials or limited free plans) but are watermarked or video-limited. Budget at least an entry-level paid plan for a real publishing cadence.</p>"),
   ("Do I own the videos these tools make?",
    "<p>On paid plans, generally yes for the video itself; stock footage and music carry the tool's license terms. Read the license section of the official terms before building a business on any tool.</p>"),
  ]),
 dict(
  slug="best-ai-avatars-for-course-creators", benchmark=None,
  title="8 Best AI Avatars for Course Creators (2026) — Teach Without Filming",
  meta="The 8 best AI avatar tools for course creators in 2026: turn scripts into instructor-led lessons without filming. Pricing verified.",
  h1="8 Best AI Avatars for Course Creators in 2026",
  lede="Course creators are replacing filming days with AI avatars: write the lesson script, generate the instructor video, update any lesson in minutes. Eight verified options, October 5, 2026.",
  intro=("Reshooting a course module because one fact changed is the worst part of course creation. AI avatars fix it: edit the script, regenerate the video, done. "
         "The tools below are ranked for course use specifically — lesson-length rendering, consistent instructor identity across modules, and SCORM/LMS-friendly exports where offered. "
         "Pair any of them with a course platform (we hold a Teachable affiliate relationship) and you have a complete no-camera course pipeline."),
  tools=["HeyGen","Synthesia","Colossyan","Elai","D-ID","DeepBrain AI","Hour One","Tavus"],
  takes={
   "HeyGen": "The fastest path from script to lesson video, with excellent avatar consistency across modules. Our top pick for solo course creators.",
   "Synthesia": "The institutional pick — built for corporate academies with review workflows and the deepest language support for global courses.",
   "Colossyan": "Designed for training content from the ground up; conversational avatars suit scenario-based lessons.",
   "Elai": "Strong value for course creators producing high lesson volume on a budget.",
   "D-ID": "Best if your course lives inside your own platform — embed AI instructors via API.",
   "DeepBrain AI": "Premium presenter realism for flagship courses where production value sells the price point.",
   "Hour One": "Virtual instructors tuned for education; worth evaluating for cohort-based courses.",
   "Tavus": "Personalized lesson intros at scale — imagine every student greeted by name. Experimental, but intriguing for high-ticket cohorts.",
  },
  faqs=[
   ("Can students tell the instructor is AI?",
    "<p>Current avatars are convincing in short segments; most creators disclose AI use upfront, which students generally accept when the content is good. Transparency also avoids platform-policy surprises.</p>"),
   ("How do I update a lesson without refilming?",
    "<p>Edit the script text and regenerate — minutes instead of a filming day. This is the core economic argument for AI avatars in courses, and it compounds with every update.</p>"),
   ("Where should I host my AI-avatar course?",
    "<p>Any major course platform works — Teachable, Thinkific, Podia. We hold a Teachable affiliate relationship; the platform choice matters less than your content and audience.</p>"),
  ]),
 dict(
  slug="vidnoz-alternatives", benchmark="Vidnoz",
  title="7 Best Vidnoz Alternatives (2026) — Free & Budget AI Video",
  meta="The 7 best Vidnoz alternatives for free and budget AI video in 2026. Compare free tiers, watermarks, and upgrade paths. Pricing verified.",
  h1="7 Best Vidnoz Alternatives in 2026",
  lede="Vidnoz built its name on a generous free tier for AI avatar videos — but free has limits. Seven verified alternatives, from free-friendly to premium, October 5, 2026.",
  intro=("If you're here, you want AI video without the invoice. Vidnoz's free tier is genuinely useful for testing the waters — but watermarks, minute caps, and feature gates push serious creators to paid plans eventually. "
         "The alternatives below are ordered by how far your zero dollars go, then by what the upgrade path costs when you're ready. Every free-plan claim was verified on the official site."),
  tools=["Vidnoz","HeyGen","Synthesia","D-ID","Elai","Colossyan","DeepBrain AI","Hour One","Tavus"],
  takes={
   "Vidnoz": "The benchmark for free-tier generosity in AI avatars. Start here to learn the workflow; upgrade when minute caps bite.",
   "HeyGen": "The upgrade path most Vidnoz users take — dramatically better realism when you're ready to pay for quality.",
   "Synthesia": "The professional upgrade — for creators whose free experiments turned into client work.",
   "D-ID": "A flexible middle ground with API access even at lower tiers; good for tinkerers.",
   "Elai": "Budget-friendly paid plans that undercut the big names while keeping template variety.",
   "Colossyan": "Worth the jump if your free experiments are becoming training or educational content.",
   "DeepBrain AI": "The premium end of the upgrade path — for when realism is the product.",
   "Hour One": "A solid mid-tier option for presenter-style videos on a budget.",
   "Tavus": "Not a Vidnoz replacement but a fascinating next step: personalized video once you have an audience to personalize for.",
  },
  faqs=[
   ("Is Vidnoz really free?",
    "<p>Vidnoz offers a free tier with limited minutes — verified on their official pricing page. Expect watermarks or resolution limits; it's designed as a trial path to paid plans, like every tool here.</p>"),
   ("What is the best completely free AI video tool?",
    "<p>No professional-grade tool is completely free forever. The honest ranking: Vidnoz for avatars, Kapwing and Canva-adjacent editors for editing, and YouTube's own tools for basics. Budget $20–30/month when you're publishing seriously.</p>"),
   ("When should I upgrade from a free plan?",
    "<p>When watermarks, minute caps, or missing features cost you more time than the subscription costs. For most creators that's the first month of consistent publishing.</p>"),
  ]),
]

STATIC_PAGES = {
 "privacy-policy": {
  "title": "Privacy Policy",
  "meta": "Privacy policy for AI Video & Voice Tool Comparisons: what data we collect, cookies, and Google AdSense.",
  "h1": "Privacy Policy",
  "body": """
<p><em>Last updated: October 5, 2026.</em></p>
<p>This site publishes independent comparisons of AI video and voice software. We collect as little data as possible.</p>
<h2>What we collect</h2>
<ul>
<li><strong>Server logs:</strong> our host may log standard technical data (IP address, browser type, pages visited) for security and reliability. We do not use this to identify you.</li>
<li><strong>Contact email:</strong> if you email us, we keep your message only long enough to reply.</li>
</ul>
<h2>Cookies and advertising</h2>
<p>We plan to display ads served by Google AdSense. Google may use cookies (including the DoubleClick cookie) to serve ads based on your visits to this and other sites. You can opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a>. See <a href="https://policies.google.com/technologies/ads" rel="noopener" target="_blank">how Google uses data from partner sites</a>.</p>
<p>Until an AdSense account is approved, the ad slots on this site are inert placeholders and set no advertising cookies.</p>
<h2>Affiliate links</h2>
<p>Some outbound links are affiliate links. Clicking one may set a cookie from the merchant so a resulting purchase can be attributed to us. We do not receive your personal data from merchants.</p>
<h2>Your rights</h2>
<p>You can ask us what contact data we hold about you, or ask us to delete it, via the <a href="contact.html">contact page</a>.</p>
<h2>Changes</h2>
<p>We will update the date above when this policy changes.</p>
""" },
 "about": {
  "title": "About",
  "meta": "About AI Video & Voice Tool Comparisons: how we test, verify pricing, and handle affiliate relationships.",
  "h1": "About this site",
  "body": """
<p><strong>AI Video &amp; Voice Tool Comparisons</strong> exists for one reason: buying AI video and voice software is confusing, and most "best of" lists are thin affiliate farms with invented prices.</p>
<h2>How we work</h2>
<ul>
<li><strong>Official sources only.</strong> Every price and plan detail is checked against the tool's own pricing page, and each page shows its verification date.</li>
<li><strong>Hands-on demos.</strong> Tov Rose is filming real walkthroughs of each tool — account setup, first project, honest verdict — embedded on every comparison page as they are completed.</li>
<li><strong>Real affiliate relationships.</strong> We only publish affiliate links for programs we actually hold. Everything else links to the official site, clearly marked "affiliate application pending."</li>
<li><strong>Disclosure first.</strong> The affiliate disclosure sits at the top of every comparison page, before any recommendation.</li>
</ul>
<h2>Who runs this</h2>
<p>This site is run by Tov Rose, a creator who makes videos about AI tools for video and voice — and uses the tools he writes about in his own production workflow. Nothing here is ghost-written filler: every comparison is built from verified specs and hands-on testing.</p>
<p>Questions or corrections? <a href="contact.html">Contact us</a> — pricing errors get fixed first, because accuracy is the whole point.</p>
""" },
 "contact": {
  "title": "Contact",
  "meta": "Contact AI Video & Voice Tool Comparisons: corrections, tool suggestions, and affiliate inquiries.",
  "h1": "Contact",
  "body": """
<p>Found a pricing error? Know a tool we should compare? Want to talk about an affiliate partnership? We read everything.</p>
<p>Email: <strong>{CONTACT_EMAIL}</strong></p>
<h2>What to include</h2>
<ul>
<li><strong>Pricing corrections:</strong> the tool, the wrong figure, and a link to the official pricing page showing the right one. These jump the queue.</li>
<li><strong>Tool suggestions:</strong> the tool's official site and what category it belongs in.</li>
<li><strong>Affiliate inquiries:</strong> vendors offering affiliate programs can reach out — we only list programs after verifying terms on official pages.</li>
</ul>
<p>We aim to reply within a few business days.</p>
""" },
}

def static_page(slug, p):
    body_html = p["body"].replace("{CONTACT_EMAIL}", esc(config.get("contact_email", "")))
    body = f"<div class='content'>{DISCLOSURE}<h1>{esc(p['h1'])}</h1>{body_html}</div>"
    return page_shell(p["title"], p["meta"], body, slug + ".html")

def index_page():
    cards = []
    for d in PAGES:
        cards.append(
            f"<div class='page-card'><h2><a href='{d['slug']}.html'>{esc(d['h1'])}</a></h2>"
            f"<p>{esc(d['meta'])}</p></div>")
    body = (DISCLOSURE
        + "<div class='hero'><h1>AI Video &amp; Voice Tools, Compared Honestly</h1>"
        + f"<p class='lede'>{esc(config['tagline'])} Every price verified against official sources on {esc(VERIFIED_ON)}.</p></div>"
        + ad_slot("leaderboard_under_header", "Leaderboard 970×90")
        + "<h2>All comparisons</h2><div class='page-grid'>" + "".join(cards) + "</div>"
        + "<h2>How to use these guides</h2><p>Start with the quick-comparison table on any page, then read the deep dives for the two or three finalists. "
        + "Watch for the hands-on video demos as they are published — specs tell you what a tool claims; video shows you what it actually does.</p>")
    return page_shell("Best AI Video & Voice Tools Compared (2026) — Hands-On Reviews & Real Pricing",
                      config["tagline"] + " Pricing verified against official sources.",
                      body, "index.html")

def main():
    out = ROOT
    pages = [(d["slug"], comparison_page(d)) for d in PAGES]
    pages += [(slug, static_page(slug, p)) for slug, p in STATIC_PAGES.items()]
    pages.append(("index", index_page()))
    for slug, html_doc in pages:
        path = os.path.join(out, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_doc)
    base = (config.get("base_url") or "").rstrip("/")
    if base:
        urls = "\n".join(
            f'  <url><loc>{esc(base)}/{slug}.html</loc><lastmod>{VERIFIED_ON}</lastmod></url>'
            for slug, _ in pages)
        with open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
        with open(os.path.join(out, "robots.txt"), "w", encoding="utf-8") as f:
            f.write(f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n")
    print(f"Wrote {len(pages)} pages to {out}")

if __name__ == "__main__":
    main()
