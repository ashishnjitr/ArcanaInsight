import os
import random
import streamlit as st

# Configure wide layout and page attributes
st.set_page_config(
    page_title="Arcana Insight | Mystical Tarot",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Deep cosmic styling mirroring the first layout
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% 15%, #18112d 0%, #0a0614 70%, #040208 100%);
        color: #e2e8f0;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Cosmic Header */
    .hero-container {
        text-align: center;
        padding: 2.2rem 1rem 1.2rem 1rem;
        max-width: 900px;
        margin: 0 auto;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.35rem 0.95rem;
        background: rgba(147, 51, 234, 0.14);
        border: 1px solid rgba(192, 132, 252, 0.3);
        border-radius: 9999px;
        font-size: 0.76rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: #d8b4fe;
        margin-bottom: 0.9rem;
    }
    .hero-title {
        font-family: 'Cinzel', serif;
        font-size: 2.7rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        background: linear-gradient(135deg, #ffffff 20%, #d8b4fe 60%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.4rem;
    }
    .hero-subtitle {
        color: #94a3b8;
        font-size: 1rem;
        max-width: 640px;
        margin: 0 auto 1.5rem auto;
        line-height: 1.5;
    }

    /* Query & Action Bar */
    .input-bar-wrap {
        background: rgba(18, 13, 33, 0.7);
        border: 1px solid rgba(168, 85, 247, 0.25);
        border-radius: 16px;
        padding: 1.4rem;
        backdrop-filter: blur(12px);
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    }

    /* Primary Tarot Cards Grid */
    .card-slot-wrap {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    .card-slot-tag {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #c084fc;
        background: rgba(147, 51, 234, 0.15);
        border: 1px solid rgba(168, 85, 247, 0.3);
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        margin-bottom: 0.6rem;
    }
    .mystic-card {
        width: 100%;
        max-width: 250px;
        height: 380px;
        background: linear-gradient(160deg, #1f1538 0%, #110b20 60%, #0a0614 100%);
        border: 1.5px solid rgba(216, 180, 254, 0.35);
        border-radius: 16px;
        padding: 1.1rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6), inset 0 0 18px rgba(168, 85, 247, 0.12);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .mystic-card:hover {
        transform: translateY(-5px);
        border-color: rgba(216, 180, 254, 0.7);
        box-shadow: 0 18px 40px rgba(147, 51, 234, 0.28);
    }
    .card-glyph-container {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.12) 0%, transparent 70%);
        border: 1px dashed rgba(168, 85, 247, 0.25);
        border-radius: 12px;
        margin: 0.6rem 0;
    }
    .card-symbol {
        font-size: 3rem;
        filter: drop-shadow(0 0 10px rgba(216, 180, 254, 0.5));
    }
    .card-name-title {
        font-family: 'Cinzel', serif;
        font-weight: 700;
        font-size: 1.05rem;
        color: #f8fafc;
        text-align: center;
        margin-top: 0.3rem;
    }
    .status-pill {
        display: inline-block;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        padding: 0.15rem 0.55rem;
        border-radius: 4px;
        text-transform: uppercase;
    }
    .status-upright {
        background: rgba(52, 211, 153, 0.18);
        color: #6ee7b7;
        border: 1px solid rgba(52, 211, 153, 0.4);
    }
    .status-reversed {
        background: rgba(248, 113, 113, 0.18);
        color: #fca5a5;
        border: 1px solid rgba(248, 113, 113, 0.4);
    }

    /* Narrative Output Box */
    .oracle-glass-box {
        background: rgba(18, 13, 33, 0.75);
        border: 1px solid rgba(168, 85, 247, 0.35);
        border-radius: 18px;
        padding: 2.2rem;
        margin-top: 1.5rem;
        backdrop-filter: blur(14px);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.55);
    }
    .oracle-glass-box h3 {
        font-family: 'Cinzel', serif;
        font-size: 1.6rem;
        color: #e9d5ff;
        margin-bottom: 0.9rem;
    }
    .oracle-glass-box h4 {
        font-family: 'Cinzel', serif;
        font-size: 1.15rem;
        color: #c084fc;
        margin-top: 1.3rem;
        margin-bottom: 0.5rem;
    }
    .oracle-glass-box p, .oracle-glass-box li {
        color: #cbd5e1;
        line-height: 1.7;
        font-size: 0.96rem;
    }

    /* Elemental Breakdown Chips */
    .element-chip {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: rgba(30, 24, 52, 0.6);
        border: 1px solid rgba(147, 51, 234, 0.25);
        border-radius: 8px;
        padding: 0.4rem 0.8rem;
        font-size: 0.8rem;
        color: #e2e8f0;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Comprehensive Archetypes Database with symbols and suits
TAROT_DECK = [
    {"name": "The Fool", "arcana": "Major", "element": "Air", "symbol": "🌌", "keywords": ["New Beginnings", "Innocence", "Leap of Faith", "Infinite Potential"], "reversed_keywords": ["Recklessness", "Hesitation", "Naivety", "Blind Risk"]},
    {"name": "The Magician", "arcana": "Major", "element": "Air", "symbol": "⚡", "keywords": ["Manifestation", "Willpower", "Resourcefulness", "Directed Focus"], "reversed_keywords": ["Trickery", "Scattered Focus", "Untapped Power", "Deception"]},
    {"name": "The High Priestess", "arcana": "Major", "element": "Water", "symbol": "🌙", "keywords": ["Intuition", "Sacred Mystery", "Inner Voice", "Subconscious"], "reversed_keywords": ["Suppressed Intuition", "Secrets", "Surface Thinking", "Superficiality"]},
    {"name": "The Empress", "arcana": "Major", "element": "Earth", "symbol": "🌿", "keywords": ["Abundance", "Sensory Creation", "Nurturing", "Fertile Ground"], "reversed_keywords": ["Creative Burnout", "Over-dependence", "Smothering", "Neglect"]},
    {"name": "The Emperor", "arcana": "Major", "element": "Fire", "symbol": "👑", "keywords": ["Structure", "Stability", "Clear Authority", "Strategic Order"], "reversed_keywords": ["Rigidity", "Domination", "Chaos", "Inflexibility"]},
    {"name": "The Hierophant", "arcana": "Major", "element": "Earth", "symbol": "🗝️", "keywords": ["Spiritual Lineage", "Tradition", "Shared Values", "Mentorship"], "reversed_keywords": ["Challenging Dogma", "Unconventional Way", "Personal Truth", "Rebellion"]},
    {"name": "The Lovers", "arcana": "Major", "element": "Air", "symbol": "💞", "keywords": ["Sacred Alignment", "Dual Harmony", "Core Values", "Conscious Choice"], "reversed_keywords": ["Value Conflict", "Misalignment", "Avoided Decisions", "Internal Friction"]},
    {"name": "The Chariot", "arcana": "Major", "element": "Water", "symbol": "🛡️", "keywords": ["Determination", "Directed Momentum", "Inner Triumph", "Willpower"], "reversed_keywords": ["Lack of Direction", "Powerlessness", "Scattered Energy", "Obstacles"]},
    {"name": "Strength", "arcana": "Major", "element": "Fire", "symbol": "🦁", "keywords": ["Compassion", "Quiet Resilience", "Emotional Fortitude", "Gentle Mastery"], "reversed_keywords": ["Self-doubt", "Exhaustion", "Impulsiveness", "Raw Vulnerability"]},
    {"name": "The Hermit", "arcana": "Major", "element": "Earth", "symbol": "🏮", "keywords": ["Soul Searching", "Introspection", "Solitary Wisdom", "Inner Guidance"], "reversed_keywords": ["Isolation", "Withdrawal", "Ignoring Truth", "Loneliness"]},
    {"name": "Wheel of Fortune", "arcana": "Major", "element": "Fire", "symbol": "🎡", "keywords": ["Karmic Shifts", "Inevitable Cycles", "Destiny", "Turning Points"], "reversed_keywords": ["Resisting Flow", "Repeated Mistakes", "Illusions of Control", "Stagnation"]},
    {"name": "Justice", "arcana": "Major", "element": "Air", "symbol": "⚖️", "keywords": ["Cause & Effect", "Clarity", "Truth", "Radical Accountability"], "reversed_keywords": ["Dishonesty", "Unfair Scrutiny", "Dodging Truth", "Unresolved Bias"]},
    {"name": "The Hanged Man", "arcana": "Major", "element": "Water", "symbol": "⏳", "keywords": ["Paradoxical Pause", "New Perspective", "Surrender", "Letting Go"], "reversed_keywords": ["Futile Struggle", "Stagnation", "Martyrdom", "Delaying Release"]},
    {"name": "Death", "arcana": "Major", "element": "Water", "symbol": "🦋", "keywords": ["Profound Metamorphosis", "Ending Cycles", "Pruning", "Rebirth"], "reversed_keywords": ["Clinging to Remains", "Fear of Rebirth", "Prolonged Endings", "Resistance"]},
    {"name": "Temperance", "arcana": "Major", "element": "Fire", "symbol": "⚗️", "keywords": ["Alchemy", "Synthesis", "Patience", "Finding Equanimity"], "reversed_keywords": ["Imbalance", "Internal Friction", "Impatience", "Overindulgence"]},
    {"name": "The Devil", "arcana": "Major", "element": "Earth", "symbol": "⛓️", "keywords": ["Shadow Patterns", "Unconscious Attachments", "Illusory Chains", "Temptation"], "reversed_keywords": ["Reclaiming Autonomy", "Breaking Free", "Shadow Integration", "Awakening"]},
    {"name": "The Tower", "arcana": "Major", "element": "Fire", "symbol": "⚡", "keywords": ["Breakthrough", "Shattered Illusion", "Liberating Truth", "Upheaval"], "reversed_keywords": ["Narrowly Averting", "Fear of Pain", "Delayed Inevitability", "Internal Tremor"]},
    {"name": "The Star", "arcana": "Major", "element": "Air", "symbol": "⭐", "keywords": ["Renewed Hope", "Spiritual Balm", "Clarity", "Inspiration"], "reversed_keywords": ["Temporary Discouragement", "Cynicism", "Bleak Outlook", "Disconnected Faith"]},
    {"name": "The Moon", "arcana": "Major", "element": "Water", "symbol": "🌕", "keywords": ["Subconscious Depth", "Intuitive Visions", "Unseen Undercurrents", "Dreamwork"], "reversed_keywords": ["Lifting Fog", "Revealed Deception", "Anxiety Calming", "Clear Sight"]},
    {"name": "The Sun", "arcana": "Major", "element": "Fire", "symbol": "☀️", "keywords": ["Radiant Joy", "Total Transparency", "Vitality", "Unambiguous Success"], "reversed_keywords": ["Muffled Optimism", "Temporary Burnout", "Delayed Warmth", "Over-extension"]},
    {"name": "Judgement", "arcana": "Major", "element": "Fire", "symbol": "🪽", "keywords": ["Higher Calling", "Awakening", "Self-reckoning", "Spiritual Absolution"], "reversed_keywords": ["Paralyzing Guilt", "Harsh Self-blame", "Ignoring the Call", "Doubt"]},
    {"name": "The World", "arcana": "Major", "element": "Earth", "symbol": "🌐", "keywords": ["Wholeness", "Integration", "Culmination", "Arriving Home"], "reversed_keywords": ["Loose Ends", "Unfinished Chapter", "Delayed Closure", "Premature Exit"]},

    # Selected Minor Arcana
    {"name": "Ace of Wands", "arcana": "Minor", "element": "Fire", "symbol": "🔥", "keywords": ["Creative Spark", "Primal Drive", "Initiative", "Sudden Inspiration"], "reversed_keywords": ["False Start", "Depleted Energy", "Creative Block", "Hesitation"]},
    {"name": "Three of Wands", "arcana": "Minor", "element": "Fire", "symbol": "🔭", "keywords": ["Expanding Horizon", "Foresight", "Enterprise", "Patience in Transit"], "reversed_keywords": ["Delays", "Playing Small", "Frustration", "Short-sightedness"]},
    {"name": "Ten of Wands", "arcana": "Minor", "element": "Fire", "symbol": "🪵", "keywords": ["Heavy Burdens", "Final Stretch", "Responsibility", "Endurance"], "reversed_keywords": ["Overwhelm", "Refusal to Delegate", "Baggage Release", "Breakdown"]},

    {"name": "Ace of Cups", "arcana": "Minor", "element": "Water", "symbol": "🌊", "keywords": ["Emotional Renewal", "Open Heart", "Intuitive Inflow", "Pure Receptivity"], "reversed_keywords": ["Emotional Depletion", "Closed Heart", "Repressed Feelings", "Wasted Care"]},
    {"name": "Five of Cups", "arcana": "Minor", "element": "Water", "symbol": "🍷", "keywords": ["Mourning Loss", "Spilled Emotion", "Grief", "Partial View"], "reversed_keywords": ["Acceptance", "Looking at What Remains", "Forgiveness", "Healing"]},
    {"name": "Ten of Cups", "arcana": "Minor", "element": "Water", "symbol": "🌈", "keywords": ["Emotional Fulfillment", "Deep Belonging", "Inner Concord", "Peace"], "reversed_keywords": ["Superficial Harmony", "Family Friction", "Unmet Hopes", "Disconnection"]},

    {"name": "Ace of Swords", "arcana": "Minor", "element": "Air", "symbol": "⚔️", "keywords": ["Mental Breakthrough", "Incisive Truth", "Clarity", "Intellectual Focus"], "reversed_keywords": ["Hostile Words", "Mental Fog", "Clouded Decision", "Sharp Retaliation"]},
    {"name": "Three of Swords", "arcana": "Minor", "element": "Air", "symbol": "💔", "keywords": ["Piercing Realization", "Sorrow", "Truth Cleansing", "Heartbreak"], "reversed_keywords": ["Lingering Bitterness", "Suppressed Pain", "Recovery Beginning", "Forgiveness"]},
    {"name": "Eight of Swords", "arcana": "Minor", "element": "Air", "symbol": "🪞", "keywords": ["Self-imposed Cage", "Analysis Paralysis", "Limiting Beliefs", "Entrapment"], "reversed_keywords": ["Reclaiming Agency", "Exit Found", "Shedding Limiting Beliefs", "Freedom"]},

    {"name": "Ace of Pentacles", "arcana": "Minor", "element": "Earth", "symbol": "🌱", "keywords": ["Tangible Seed", "Physical Foundation", "Pragmatic Prosperity", "Opportunity"], "reversed_keywords": ["Missed Opening", "Unstable Soil", "Mismanaged Resources", "Delay"]},
    {"name": "Four of Pentacles", "arcana": "Minor", "element": "Earth", "symbol": "🪙", "keywords": ["Resource Guarding", "Safe Boundaries", "Financial Control", "Security"], "reversed_keywords": ["Scarcity Fear", "Rigid Possession", "Fear of Flow", "Hoarding"]},
    {"name": "Ten of Pentacles", "arcana": "Minor", "element": "Earth", "symbol": "🏰", "keywords": ["Enduring Legacy", "Rooted Wealth", "Generational Safety", "Completeness"], "reversed_keywords": ["Family Division", "Fragile Foundation", "Short-sighted Greed", "Loss"]}
]

SPREAD_CONFIGS = {
    "Single Card Focus": [
        {"position": "The Present Core", "description": "The central anchor of your immediate inquiry"}
    ],
    "Threefold Trinity": [
        {"position": "Root & Precedent", "description": "Past foundations and underlying history"},
        {"position": "Active Crucible", "description": "Present forces and dynamic crossroads"},
        {"position": "Unfolding Horizon", "description": "Where current choices will naturally carry you"}
    ],
    "Mind, Heart, Spirit": [
        {"position": "The Conscious Mind", "description": "Logic, plans, mental assumptions, and strategies"},
        {"position": "The Emotional Heart", "description": "Subconscious fears, desires, and vulnerability"},
        {"position": "The Higher Spirit", "description": "Soul trajectory, universal alignment, and true self"}
    ],
    "The Crossroad": [
        {"position": "Core Tension", "description": "What is truly at stake beneath surface questions"},
        {"position": "The Familiar Route", "description": "Comfortable patterns and the default path"},
        {"position": "The Demanding Path", "description": "The transformative road calling for conscious bravery"},
        {"position": "The Catalyst", "description": "The integrative shift needed to make peace with the choice"}
    ]
}

def analyze_elements(drawn_cards):
    counts = {"Fire": 0, "Water": 0, "Air": 0, "Earth": 0}
    major_count = 0
    reversed_count = 0

    for card in drawn_cards:
        counts[card["element"]] = counts.get(card["element"], 0) + 1
        if card["arcana"] == "Major":
            major_count += 1
        if card["is_reversed"]:
            reversed_count += 1

    total = len(drawn_cards)
    insights = []

    if major_count >= (total / 2):
        insights.append(f"**Dominant Archetypal Shift:** {major_count} of {total} cards belong to the Major Arcana, pointing to macro-level evolution rather than everyday situational friction.")
    else:
        insights.append(f"**Practical Minor Arcana Focus:** {total - major_count} of {total} cards are Minor Arcana, meaning tangible habits, boundaries, and immediate decisions are where your power lives.")

    dominant_elem = max(counts, key=counts.get)
    element_descriptions = {
        "Fire": "Fire dominance brings urgency, raw momentum, passion, and calls for bold creative action.",
        "Water": "Water dominance points to intuitive currents, relationship dynamics, and unexpressed emotional currents.",
        "Air": "Air dominance demands intellectual objectivity, honest dialogue, and cutting through mental clutter.",
        "Earth": "Earth dominance emphasizes material stability, physical pacing, work discipline, and steady foundation building."
    }
    insights.append(f"**Primary Element ({dominant_elem}):** {element_descriptions[dominant_elem]}")

    if reversed_count > 0:
        insights.append(f"**Inward Inversions ({reversed_count} Reversed):** Cards drawn reversed show where energy is being internalized, resisted, or asking for quiet reflection rather than blunt force.")

    return insights

def deterministic_synthesis(question, spread_name, drawn_cards, element_insights):
    query_text = f"\"{question.strip()}\"" if question.strip() else "your current life trajectory"
    
    first = drawn_cards[0]
    last = drawn_cards[-1]
    first_state = "an internalized, reflective state" if first["is_reversed"] else "a direct, conscious presence"
    last_state = "demanding internal alignment before resolution" if last["is_reversed"] else "a clear, visible manifestation on the horizon"

    breakdown_items = []
    for c in drawn_cards:
        orientation = "Reversed" if c["is_reversed"] else "Upright"
        kws = c["reversed_keywords"] if c["is_reversed"] else c["keywords"]
        breakdown_items.append(
            f"<li><strong>{c['position_title']}</strong>: <em>{c['name']}</em> ({orientation})<br/>"
            f"<span style='color: #94a3b8; font-size: 0.88rem;'>Theme: {', '.join(kws[:3])} &bull; Element: {c['element']}</span></li>"
        )

    return f"""
    <div class="oracle-glass-box">
        <h3>The Oracle's Synthesis</h3>
        <p>In response to <strong>{query_text}</strong>, the archetypes have aligned within the <strong>{spread_name}</strong> spread.</p>
        
        <h4>Positional Archetypes</h4>
        <ul style="padding-left: 1.2rem; margin-bottom: 1.2rem;">
            {''.join(breakdown_items)}
        </ul>

        <h4>The Energetic Thread</h4>
        <p>The spread opens through <strong>{first['name']}</strong> in {first_state}. This establishes the root environment from which the rest of the dynamic unfolds. Notice how this tension seeks its eventual resolution in <strong>{last['name']}</strong>, which operates as {last_state}.</p>
        
        <p>Because there is a natural dialogue between <strong>{first['element']}</strong> and <strong>{last['element']}</strong>, the cards counsel that resolving this issue requires moving beyond initial reactions and embracing the quiet discipline of the final card.</p>

        <h4>Contemplative Inquiries</h4>
        <ul>
            <li>Where are you exerting effort against the grain instead of working with what is naturally unfolding?</li>
            <li>What truth highlighted by the most grounded card in this spread have you been hesitant to speak aloud?</li>
            <li>What is one small, deliberate boundary you can honor today to stabilize this energy?</li>
        </ul>
    </div>
    """

def ai_synthesis(api_key, question, spread_name, drawn_cards, element_insights):
    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)

        cards_summary = []
        for c in drawn_cards:
            orientation = "Reversed" if c["is_reversed"] else "Upright"
            kws = c["reversed_keywords"] if c["is_reversed"] else c["keywords"]
            cards_summary.append(
                f"- Position: {c['position_title']} ({c['position_desc']}) | Card: {c['name']} ({orientation}) | Element: {c['element']} | Keywords: {', '.join(kws)}"
            )

        prompt = f"""
You are a master Tarot reader, depth psychologist, and intuitive mentor.
Provide a rich, genuine, unscripted Tarot reading for the querent. Avoid fortune-telling gimmicks, generic horoscopes, or superficial platitudes. Speak directly, humanely, and with perceptive insight.

Querent Question: "{question.strip() if question.strip() else 'General energetic trajectory and personal evolution'}"
Spread Used: {spread_name}

Cards Drawn:
{chr(10).join(cards_summary)}

Systemic Elemental Balance:
{chr(10).join(element_insights)}

Guidelines:
1. Speak directly to the querent's question with grounded empathy and sharp psychological clarity.
2. Weave the cards together into a seamless narrative current rather than disconnected card by card summaries.
3. Explicitly explain what the reversed cards or dominant elements reveal about unexpressed subconscious currents.
4. Conclude with three sharp, introspective reflection questions tailored to this spread.
5. Format cleanly using HTML tags like <h4>, <p>, <ul>, <li> inside the response.
6. Do not use em dashes anywhere in your response.
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=1100
            )
        )
        return f'<div class="oracle-glass-box"><h3>The Oracle\'s Deep Synthesis</h3>{response.text}</div>'
    except Exception as e:
        st.warning(f"AI synthesis unavailable ({str(e)}). Switching to the native deterministic engine.")
        return deterministic_synthesis(question, spread_name, drawn_cards, element_insights)

# --- Hero Section (Mirroring Layout 1) ---
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-badge">✦ Archetypal Oracle & Insight Engine ✦</div>
        <div class="hero-title">Arcana Insight</div>
        <div class="hero-subtitle">
            Authentic, unscripted Tarot readings mapping the dialogue between ancient symbolism, elemental physics, and your genuine questions.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Spread Selector & Control Bar ---
with st.container():
    st.markdown('<div class="input-bar-wrap">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([3, 2, 1])

    with c1:
        user_query = st.text_input(
            "What question or crossroads is alive in your world right now?",
            placeholder="e.g., How can I navigate the tension between security and creative freedom?",
            key="user_query_input"
        )
    with c2:
        spread_type = st.selectbox(
            "Select Spread Structure",
            options=list(SPREAD_CONFIGS.keys()),
            index=1,
            key="spread_select"
        )
    with c3:
        st.write("")
        st.write("")
        draw_button = st.button("Cast Spread ✦", use_container_width=True)

    c_opt1, c_opt2 = st.columns([1, 2])
    with c_opt1:
        allow_reversals = st.checkbox("Allow Inversions (Reversed Cards)", value=True)
    with c_opt2:
        api_key_input = st.text_input(
            "Optional: Gemini API Key for conversational synthesis",
            type="password",
            value=os.environ.get("GEMINI_API_KEY", ""),
            placeholder="Paste your key or leave blank for the built-in symbolic engine"
        )
    st.markdown('</div>', unsafe_allow_html=True)

# Maintain state
if "reading_data" not in st.session_state:
    st.session_state.reading_data = None

# Draw Handler
if draw_button:
    spread_info = SPREAD_CONFIGS[spread_type]
    sampled = random.sample(TAROT_DECK, len(spread_info))
    cards_payload = []

    for idx, pos in enumerate(spread_info):
        card = dict(sampled[idx])
        card["position_title"] = pos["position"]
        card["position_desc"] = pos["description"]
        card["is_reversed"] = random.choice([True, False]) if allow_reversals else False
        cards_payload.append(card)

    st.session_state.reading_data = {
        "question": user_query,
        "spread_name": spread_type,
        "cards": cards_payload
    }

# --- Active Card Display Section ---
if st.session_state.reading_data:
    rd = st.session_state.reading_data
    cards = rd["cards"]
    num_cards = len(cards)

    st.markdown(
        f"""
        <div style="text-align: center; margin: 1.8rem 0 1.2rem 0;">
            <span style="font-family: 'Cinzel', serif; font-size: 1.3rem; color: #e9d5ff; font-weight: 600;">
                Reading: {rd['spread_name']}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Render cards in matching columns
    card_cols = st.columns(num_cards)
    for idx, card in enumerate(cards):
        with card_cols[idx]:
            is_rev = card["is_reversed"]
            status_text = "Reversed" if is_rev else "Upright"
            status_cls = "status-reversed" if is_rev else "status-upright"
            kws = card["reversed_keywords"] if is_rev else card["keywords"]

            # Visual representation with card art frame
            st.markdown(
                f"""
                <div class="card-slot-wrap">
                    <div class="card-slot-tag">{card['position_title']}</div>
                    <div class="mystic-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="status-pill {status_cls}">{status_text}</span>
                            <span style="font-size: 0.75rem; color: #94a3b8; font-weight: 600;">{card['element']}</span>
                        </div>
                        <div class="card-glyph-container">
                            <div class="card-symbol">{card['symbol']}</div>
                            <div class="card-name-title">{card['name']}</div>
                            <div style="font-size: 0.72rem; color: #a855f7; margin-top: 0.2rem;">{card['arcana']} Arcana</div>
                        </div>
                        <div style="font-size: 0.76rem; color: #cbd5e1; line-height: 1.35;">
                            <strong style="color: #e2e8f0;">Core Essence:</strong> {', '.join(kws[:3])}
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Systemic Energetic Blueprint
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    st.markdown("#### Systemic Archetypal Blueprint")
    element_insights = analyze_elements(cards)
    for insight in element_insights:
        st.markdown(f"- {insight}")

    # Narrative Output (AI or Deterministic)
    with st.spinner("Channeling archetypes and weaving narrative..."):
        if api_key_input.strip():
            rendered_html = ai_synthesis(
                api_key_input.strip(),
                rd["question"],
                rd["spread_name"],
                cards,
                element_insights
            )
        else:
            rendered_html = deterministic_synthesis(
                rd["question"],
                rd["spread_name"],
                cards,
                element_insights
            )

    st.markdown(rendered_html, unsafe_allow_html=True)

    # Journal / Contemplation area
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    st.subheader("Personal Journal & Intuitive Sparks")
    st.text_area(
        "Capture what resonated most deeply with your intuition:",
        placeholder="What did this spread illuminate that your conscious mind was trying to overlook?",
        height=120,
        key="journal_notes"
    )
