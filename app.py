import os
import random
import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Arcana Insight | Authentic Tarot Engine",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling for Celestial Dark Mode
st.markdown(
    """
    <style>
    .main {
        background-color: #0d0f18;
        color: #e2e8f0;
    }
    .stButton>button {
        background: linear-gradient(135deg, #6366f1, #a855f7);
        color: white;
        border: none;
        padding: 0.65rem 1.8rem;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.4);
    }
    .tarot-card {
        background: #161a29;
        border: 1px solid #2d3748;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
        margin-bottom: 1rem;
        min-height: 260px;
    }
    .card-title {
        color: #e9d5ff;
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    .card-orientation {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .orientation-upright {
        color: #34d399;
    }
    .orientation-reversed {
        color: #f87171;
    }
    .element-tag {
        display: inline-block;
        padding: 0.15rem 0.55rem;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-top: 0.4rem;
        background-color: #242b42;
        color: #93c5fd;
    }
    .reading-summary-box {
        background: rgba(30, 27, 75, 0.45);
        border: 1px solid #4338ca;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Deck Archetypes & Elemental Attributes
TAROT_DECK = [
    # Major Arcana
    {"name": "The Fool", "arcana": "Major", "element": "Air", "keywords": ["New beginnings", "Spontaneity", "Leap of faith", "Infinite potential"], "reversed_keywords": ["Recklessness", "Hesitation", "Naivety", "Poor timing"]},
    {"name": "The Magician", "arcana": "Major", "element": "Air", "keywords": ["Resourcefulness", "Manifestation", "Willpower", "Focused intention"], "reversed_keywords": ["Manipulation", "Untapped talents", "Scattered focus", "Trickery"]},
    {"name": "The High Priestess", "arcana": "Major", "element": "Water", "keywords": ["Intuition", "Unconscious realm", "Sacred mystery", "Inner knowledge"], "reversed_keywords": ["Ignored gut feelings", "Surface secrets", "Disconnection", "Superficiality"]},
    {"name": "The Empress", "arcana": "Major", "element": "Earth", "keywords": ["Abundance", "Nurturing", "Sensory creation", "Organic growth"], "reversed_keywords": ["Creative burnout", "Over-dependence", "Smothering", "Neglect"]},
    {"name": "The Emperor", "arcana": "Major", "element": "Fire", "keywords": ["Structure", "Discipline", "Sound authority", "Strategic foundation"], "reversed_keywords": ["Rigidity", "Authoritarian control", "Disorganization", "Chaos"]},
    {"name": "The Hierophant", "arcana": "Major", "element": "Earth", "keywords": ["Tradition", "Spiritual lineage", "Shared values", "Mentorship"], "reversed_keywords": ["Challenging dogma", "Dogmatic restriction", "Unconventional path", "Rebellion"]},
    {"name": "The Lovers", "arcana": "Major", "element": "Air", "keywords": ["Sacred choice", "Alignment of values", "Harmony", "Deep duality"], "reversed_keywords": ["Value conflict", "Internal misalignment", "Disharmony", "Avoided decisions"]},
    {"name": "The Chariot", "arcana": "Major", "element": "Water", "keywords": ["Determination", "Directed momentum", "Overcoming tension", "Mastery"], "reversed_keywords": ["Lack of direction", "Powerlessness", "Aggression", "Scattered force"]},
    {"name": "Strength", "arcana": "Major", "element": "Fire", "keywords": ["Compassion", "Quiet resilience", "Emotional fortitude", "Patience"], "reversed_keywords": ["Self-doubt", "Exhaustion", "Impulsiveness", "Raw vulnerability"]},
    {"name": "The Hermit", "arcana": "Major", "element": "Earth", "keywords": ["Soul searching", "Introspection", "Solitary insight", "Inner truth"], "reversed_keywords": ["Isolation", "Loneliness", "Rejecting wisdom", "Withdrawal"]},
    {"name": "Wheel of Fortune", "arcana": "Major", "element": "Fire", "keywords": ["Karmic cycles", "Destiny shifts", "Inevitable change", "Turning points"], "reversed_keywords": ["Resisting flow", "Repeated patterns", "Temporary bad luck", "Control illusions"]},
    {"name": "Justice", "arcana": "Major", "element": "Air", "keywords": ["Cause and effect", "Objective clarity", "Truth", "Radical accountability"], "reversed_keywords": ["Bias", "Unfair scrutiny", "Dodging consequences", "Unresolved imbalance"]},
    {"name": "The Hanged Man", "arcana": "Major", "element": "Water", "keywords": ["Paradoxical surrender", "New perspective", "Voluntary pause", "Release"], "reversed_keywords": ["Stagnation", "Futile struggle", "Martyrdom", "Delaying the inevitable"]},
    {"name": "Death", "arcana": "Major", "element": "Water", "keywords": ["Profound metamorphosis", "Ending cycles", "Clearing ground", "Rebirth"], "reversed_keywords": ["Fear of shedding old skin", "Clinging to remnants", "Prolonged goodbyes", "Resisting transformation"]},
    {"name": "Temperance", "arcana": "Major", "element": "Fire", "keywords": ["Alchemy", "Synthesis", "Patience", "Finding the middle current"], "reversed_keywords": ["Extremes", "Internal friction", "Impatience", "Overindulgence"]},
    {"name": "The Devil", "arcana": "Major", "element": "Earth", "keywords": ["Unconscious attachments", "Shadow patterns", "Temptation", "Self-imposed limits"], "reversed_keywords": ["Breaking free", "Reclaiming autonomy", "Facing down vices", "Shedding illusion"]},
    {"name": "The Tower", "arcana": "Major", "element": "Fire", "keywords": ["Structural collapse", "Liberating breakthrough", "Shattered assumptions", "Raw truth"], "reversed_keywords": ["Averting disaster narrowly", "Prolonging brittle structures", "Internal upheaval", "Delayed shakeup"]},
    {"name": "The Star", "arcana": "Major", "element": "Air", "keywords": ["Renewed hope", "Authentic inspiration", "Spiritual balm", "Clarity"], "reversed_keywords": ["Temporary discouragement", "Bleak outlook", "Disconnected faith", " cynicism"]},
    {"name": "The Moon", "arcana": "Major", "element": "Water", "keywords": ["Illusion", "Vivid subconscious", "Anxiety", "Navigating foggy waters"], "reversed_keywords": ["Lifting fog", "Exposed deceits", "Calming the psyche", "Emerging clarity"]},
    {"name": "The Sun", "arcana": "Major", "element": "Fire", "keywords": ["Vitality", "Total transparency", "Radiant joy", "Unambiguous success"], "reversed_keywords": ["Clouded optimism", "Delayed realization", "Temporary burnout", "Muffled warmth"]},
    {"name": "Judgement", "arcana": "Major", "element": "Fire", "keywords": ["Awakening call", "Higher accountability", "Self-reckoning", "Absolution"], "reversed_keywords": ["Harsh self-criticism", "Ignoring the call", "Paralyzing guilt", "Lingering doubts"]},
    {"name": "The World", "arcana": "Major", "element": "Earth", "keywords": ["Wholeness", "Integration", "Culmination", "Arriving at the threshold"], "reversed_keywords": ["Loose ends", "Unfinished chapter", "Delayed closure", "Premature celebration"]},

    # Selected Minor Arcana Anchors (Wands: Fire, Cups: Water, Swords: Air, Pentacles: Earth)
    {"name": "Ace of Wands", "arcana": "Minor", "suit": "Wands", "element": "Fire", "keywords": ["Creative spark", "Sudden inspiration", "Primal drive", "Initiative"], "reversed_keywords": ["False start", "Creative block", "Depleted enthusiasm", "Delays"]},
    {"name": "Three of Wands", "arcana": "Minor", "suit": "Wands", "element": "Fire", "keywords": ["Foresight", "Expanding horizon", "Enterprise", "Patience during transit"], "reversed_keywords": ["Obstacles in transit", "Playing small", "Short-sighted plans", "Frustration"]},
    {"name": "Ten of Wands", "arcana": "Minor", "suit": "Wands", "element": "Fire", "keywords": ["Heavy burdens", "Nearing the finish", "Responsibility overload", "Endurance"], "reversed_keywords": ["Collapse from overwork", "Refusal to delegate", "Dropping unnecessary baggage", "Relief"]},

    {"name": "Ace of Cups", "arcana": "Minor", "suit": "Cups", "element": "Water", "keywords": ["Emotional renewal", "Open heart", "Intuitive flow", "Receptivity"], "reversed_keywords": ["Emotional depletion", "Guardedness", "Repressed feelings", "Wasted empathy"]},
    {"name": "Five of Cups", "arcana": "Minor", "suit": "Cups", "element": "Water", "keywords": ["Grief", "Mourning lost opportunity", "Spilled emotional energy", "Partial perspective"], "reversed_keywords": ["Acceptance", "Turning to what remains", "Moving past sorrow", "Emotional healing"]},
    {"name": "Ten of Cups", "arcana": "Minor", "suit": "Cups", "element": "Water", "keywords": ["Emotional fulfillment", "Domestic peace", "Deep alignment", "Wholesome belonging"], "reversed_keywords": ["Fractured harmony", "Unrealistic expectations", "External veneer", "Family friction"]},

    {"name": "Ace of Swords", "arcana": "Minor", "suit": "Swords", "element": "Air", "keywords": ["Mental breakthrough", "Cutting through illusions", "Unyielding truth", "Pure clarity"], "reversed_keywords": ["Mental confusion", "Hostile communication", "Weaponized words", "Clouded judgment"]},
    {"name": "Three of Swords", "arcana": "Minor", "suit": "Swords", "element": "Air", "keywords": ["Heartbreak", "Piercing clarity", "Sorrowful realization", "Releasing painful truth"], "reversed_keywords": ["Lingering bitterness", "Suppressed hurt", "Beginning recovery", "Forgiveness"]},
    {"name": "Eight of Swords", "arcana": "Minor", "suit": "Swords", "element": "Air", "keywords": ["Self-imposed cage", "Victim mindset", "Analysis paralysis", "Illusion of entrapment"], "reversed_keywords": ["Finding exit doors", "Reclaiming personal agency", "Shedding limiting beliefs", "Clarity"]},

    {"name": "Ace of Pentacles", "arcana": "Minor", "suit": "Pentacles", "element": "Earth", "keywords": ["Tangible opportunity", "Grounded seeds", "Material foundation", "Real prosperity"], "reversed_keywords": ["Missed investment", "Unstable footing", "Poor resource management", "Greed"]},
    {"name": "Four of Pentacles", "arcana": "Minor", "suit": "Pentacles", "element": "Earth", "keywords": ["Security", "Resource protection", "Cautious boundaries", "Financial control"], "reversed_keywords": ["Scarcity mindset", "Stifling rigidity", "Fear of letting go", "Greedy hoarding"]},
    {"name": "Ten of Pentacles", "arcana": "Minor", "suit": "Pentacles", "element": "Earth", "keywords": ["Legacy", "Long term stability", "Rooted wealth", "Generational foundation"], "reversed_keywords": ["Disputes over resources", "Fragile foundations", "Short term greed", "Loss of structure"]}
]

SPREAD_CONFIGS = {
    "Single Card Focus": [
        {"position": "Present Core", "description": "The dominant active energy and immediate focus point"}
    ],
    "Threefold Trinity (Past, Present, Horizon)": [
        {"position": "Root & Precedent", "description": "Underlying conditions and what brought you to this moment"},
        {"position": "The Present Crucible", "description": "The active crossroad and reality right in front of you"},
        {"position": "Unfolding Horizon", "description": "Where energy naturally flows if current patterns stay unchecked"}
    ],
    "Mind, Heart, Spirit Triad": [
        {"position": "The Mind (Intellect)", "description": "Your conscious thoughts, mental stories, and logic"},
        {"position": "The Heart (Emotions)", "description": "Your subconscious cravings, genuine feelings, and fears"},
        {"position": "The Spirit (True Purpose)", "description": "The higher perspective guiding you toward growth"}
    ],
    "The Crossroad Decision": [
        {"position": "The Underlying Tension", "description": "What is truly at stake beneath the surface"},
        {"position": "Path of Least Resistance", "description": "The automatic, comfortable, or habitual route"},
        {"position": "Path of Deeper Transformation", "description": "The demanding road that asks for deliberate growth"},
        {"position": "Integrative Insight", "description": "The catalyst required to reconcile both sides"}
    ]
}

def analyze_elements(drawn_cards):
    """Calculates elemental weights across drawn cards to find systemic imbalances."""
    element_counts = {"Fire": 0, "Water": 0, "Air": 0, "Earth": 0}
    major_count = 0
    reversed_count = 0

    for card in drawn_cards:
        elem = card["element"]
        element_counts[elem] = element_counts.get(elem, 0) + 1
        if card["arcana"] == "Major":
            major_count += 1
        if card["is_reversed"]:
            reversed_count += 1

    total = len(drawn_cards)
    insights = []

    # Arcana density check
    if major_count >= (total / 2):
        insights.append(
            f"**High Major Arcana Density ({major_count}/{total}):** The forces surrounding this situation are macroscopic and karmic. These are pivotal life lessons rather than transient daily concerns."
        )
    else:
        insights.append(
            f"**Practical Minor Arcana Weight ({total - major_count}/{total}):** The cards emphasize daily choices, behavioral mechanics, and tactical adjustments under your direct control."
        )

    # Orientation analysis
    if reversed_count >= (total / 2):
        insights.append(
            f"**Inward/Reversed Emphasis ({reversed_count}/{total} reversed):** Much of the energy is internalized, resisted, or asking for quiet unblocking rather than outward action."
        )

    # Dominant or absent elements
    dominant_elem = max(element_counts, key=element_counts.get)
    if element_counts[dominant_elem] > 1:
        elem_meanings = {
            "Fire": "ambition, momentum, passion, and raw impulse",
            "Water": "deep feelings, relationships, intuitive sensitivity, and vulnerability",
            "Air": "analytical thinking, objective truth, mental models, and communication",
            "Earth": "practical resources, career discipline, physical reality, and foundations"
        }
        insights.append(
            f"**Elemental Predominance ({dominant_elem}):** This spread is heavily saturated with {dominant_elem}, pointing directly to {elem_meanings[dominant_elem]}."
        )

    return insights

def deterministic_reading(question, spread_name, drawn_cards):
    """Generates a cohesive, non-generic reading using situational logic and cross-card synthesis."""
    narrative = []
    narrative.append(f"### The Oracle's Synthesis")
    if question.strip():
        narrative.append(f"**Addressing your inquiry:** *\"{question.strip()}\"*\n")
    else:
        narrative.append("**Addressing your current energetic landscape:**\n")

    narrative.append(f"Reading configuration: **{spread_name}.\n")

    # Systemic Card Overview
    narrative.append("#### Positional Breakdown")
    for card in drawn_cards:
        orientation = "Reversed" if card["is_reversed"] else "Upright"
        keywords = card["reversed_keywords"] if card["is_reversed"] else card["keywords"]
        narrative.append(
            f"- : ** (*{orientation}*)\n"
            f"  *Function:* {card['position_desc']}\n"
            f"  *Core Signatures:* {', '.join(keywords[:3])}\n"
        )

    # Narrative Synthesis
    narrative.append("#### The Cohesive Current")
    
    # Analyze interaction between first and last card
    first = drawn_cards[0]
    last = drawn_cards[-1]
    
    first_state = "internalized blockage or caution" if first["is_reversed"] else "direct dynamic force"
    last_state = "demanding internal renegotiation" if last["is_reversed"] else "clear outward manifestation"

    narrative.append(
        f"Looking at how the energy moves, the foundation set by **{first['name']}** represents a {first_state}. "
        f"This directly seeds the climate of the spread. Rather than viewing each position in isolation, notice how "
        f"the middle tension leads inevitably toward **{last['name']}** as an outcome {last_state}."
    )

    if first["element"] != last["element"]:
        narrative.append(
            f"There is an elemental transition at play from **{first['element']}** into **{last['element']}**, "
            f"showing that your initial instinct must adjust its style of engagement to resolve the core dilemma."
        )

    narrative.append("\n#### Direct Counsel")
    if any(c["is_reversed"] for c in drawn_cards):
        narrative.append(
            "- **Honor the Inversions:** The reversed cards in your reading show where your natural forward movement is catching on internal friction. Address the subtle hesitation before forcing external progress."
        )
    narrative.append(
        "- **Concrete Action:** Take the lesson of the most grounded card in your spread and translate it into a single, unambiguous step within the next 24 hours."
    )

    return "\n\n".join(narrative)

def generate_ai_synthesis(api_key, question, spread_name, drawn_cards, element_insights):
    """Leverages the modern google-genai library to weave deep, personalized interpretations."""
    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)

        cards_summary = []
        for c in drawn_cards:
            orientation = "Reversed" if c["is_reversed"] else "Upright"
            kws = c["reversed_keywords"] if c["is_reversed"] else c["keywords"]
            cards_summary.append(
                f"Position: {c['position_title']} ({c['position_desc']}) | Card: {c['name']} ({orientation}) | Element: {c['element']} | Arcana: {c['arcana']} | Themes: {', '.join(kws)}"
            )

        prompt = f"""
You are an authentic, deeply perceptive Tarot scholar and intuitive reader. 
Provide a nuanced, non-scripted, highly articulate Tarot reading. Avoid generic platitudes, fortune-telling clichés, or vague cosmic fluff. 
Speak like an observant mentor reading both the symbolism and the psychological reality of the querent.

Querent's Question / Area of Focus: "{question if question.strip() else 'General life direction and current crossroads'}"
Spread Used: {spread_name}

Cards Drawn:
{chr(10).join(cards_summary)}

Systemic Elemental Analysis:
{chr(10).join(element_insights)}

Guidelines for the response:
1. Address the querent's question directly with empathy, psychological depth, and tactical clarity.
2. Weave the cards together into an interconnected story showing how one card directly influences, complicates, or resolves the next.
3. Highlight what the reversed cards and elemental tensions reveal about subconscious patterns.
4. Conclude with three sharp, practical reflective questions the querent can take into their week.
5. Do not use em dashes anywhere in your text.
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=1000
            )
        )
        return response.text
    except Exception as e:
        st.warning(f"Unable to complete AI synthesis ({str(e)}). Falling back to the deterministic engine.")
        return deterministic_reading(question, spread_name, drawn_cards)

# Sidebar: Controls & Options
with st.sidebar:
    st.title("Settings")
    st.markdown("Customize your draw and reading engine.")

    spread_choice = st.selectbox(
        "Choose Spread Type",
        options=list(SPREAD_CONFIGS.keys()),
        index=1
    )

    allow_reversals = st.checkbox("Allow Reversed Cards", value=True, help="Simulates genuine physical deck randomization where cards can land upside down.")

    st.markdown("---")
    st.subheader("Deep Synthesis Engine")
    st.markdown("You can run readings entirely offline, or connect your Gemini API key for tailored conversational analysis.")
    api_key_input = st.text_input("Gemini API Key (Optional)", type="password", value=os.environ.get("GEMINI_API_KEY", ""))

    st.markdown("---")
    st.caption("Arcana Insight balances classical Tarot archetypes, elemental alchemy, and psychological inquiry.")

# Main Interface
st.title("Arcana Insight")
st.markdown("A purposeful, non-scripted Tarot engine that treats cards as living archetypes interacting with your specific reality.")

col1, col2 = st.columns([3, 1])
with col1:
    user_query = st.text_input(
        "What inquiry, dilemma, or decision do you bring to the cards?",
        placeholder="e.g., Should I pivot my career toward independent consulting this quarter?"
    )
with col2:
    st.write("")
    st.write("")
    draw_button = st.button("Draw the Cards", use_container_width=True)

# Session State for Readings
if "current_reading" not in st.session_state:
    st.session_state.current_reading = None

if draw_button:
    selected_spread = SPREAD_CONFIGS[spread_choice]
    num_cards = len(selected_spread)

    # True random sampling without replacement from the deck
    sampled_indices = random.sample(range(len(TAROT_DECK)), num_cards)
    drawn = []

    for i, idx in enumerate(sampled_indices):
        card_data = dict(TAROT_DECK[idx])
        card_data["position_title"] = selected_spread[i]["position"]
        card_data["position_desc"] = selected_spread[i]["description"]
        card_data["is_reversed"] = random.choice([True, False]) if allow_reversals else False
        drawn.append(card_data)

    st.session_state.current_reading = {
        "question": user_query,
        "spread_name": spread_choice,
        "cards": drawn
    }

# Display Active Reading
if st.session_state.current_reading:
    reading = st.session_state.current_reading
    cards = reading["cards"]

    st.markdown("---")
    st.subheader(f"Drawn Spread: {reading['spread_name']}")

    # Render Card Grid
    cols = st.columns(len(cards))
    for idx, card in enumerate(cards):
        with cols[idx]:
            is_rev = card["is_reversed"]
            orient_label = "Reversed" if is_rev else "Upright"
            orient_class = "orientation-reversed" if is_rev else "orientation-upright"
            kws = card["reversed_keywords"] if is_rev else card["keywords"]

            st.markdown(
                f"""
                <div class="tarot-card">
                    <div style="font-size: 0.8rem; color: #a5b4fc; margin-bottom: 0.2rem;">
                        {card['position_title']}
                    </div>
                    <div class="card-title">{card['name']}</div>
                    <div class="card-orientation {orient_class}">{orient_label}</div>
                    <div class="element-tag">{card['element']} | {card['arcana']}</div>
                    <div style="margin-top: 0.9rem; font-size: 0.85rem; color: #cbd5e1; line-height: 1.4;">
                        <strong>Energy:</strong> {card['position_desc']}
                    </div>
                    <div style="margin-top: 0.6rem; font-size: 0.8rem; color: #94a3b8;">
                        <strong>Signatures:</strong> {', '.join(kws[:3])}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Run Elemental and Structural Pattern Diagnosis
    st.markdown("### Energetic & Elemental Blueprint")
    element_insights = analyze_elements(cards)
    for insight in element_insights:
        st.markdown(f"- {insight}")

    # Generate Synthesized Reading
    st.markdown("---")
    with st.spinner("Synthesizing archetypes and cross-currents..."):
        if api_key_input.strip():
            reading_text = generate_ai_synthesis(
                api_key_input.strip(),
                reading["question"],
                reading["spread_name"],
                cards,
                element_insights
            )
        else:
            reading_text = deterministic_reading(
                reading["question"],
                reading["spread_name"],
                cards
            )

    st.markdown(
        f"""
        <div class="reading-summary-box">
            {reading_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Contemplation & Journaling Prompt
    st.markdown("---")
    st.markdown("#### Querent's Sacred Reflection")
    st.text_area(
        "Record your personal gut reaction, intuitive sparks, or action steps here:",
        placeholder="What did this spread illuminate that your conscious mind was trying to overlook?",
        height=120
    )
