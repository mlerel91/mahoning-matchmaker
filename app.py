import streamlit as st
import time
import random

# --- UI CONFIG ---
st.set_page_config(page_title="Mahoning Matchmaker", layout="centered")

# --- ULTRA-HIGH CONTRAST CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    h1, h2, h3, p, span, label, div { color: #FFFFFF !important; opacity: 1 !important; }
    .marquee-title {
        color: #FFFF00 !important; 
        text-align: center; font-size: 55px; font-weight: 900;
        text-shadow: 4px 4px #FF0000 !important;
        border-bottom: 5px solid #FFFF00; margin-bottom: 20px;
    }
    .stTextInput input {
        color: #FFFFFF !important; background-color: #111111 !important;
        border: 3px solid #FFFF00 !important; font-size: 1.5rem !important;
    }
    .stButton button {
        background-color: #FF0000 !important; color: #FFFFFF !important;
        border: 2px solid #FFFFFF !important; font-size: 28px !important;
        font-weight: 900 !important; width: 100%; height: 3.5em;
    }
    /* Toggle visibility fix */
    .stToggle p { color: #FFFFFF !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- THE DEEP CUT VAULT ---
# This dictionary maps mainstream genres to rare 35mm titles the Mahoning loves
VAULT_35MM = {
    "horror": [
        ("THE PROWLER (1981)", "If you like slashers, this is the gold standard of practical gore. Tom Savini's best work on a gritty 35mm print."),
        ("PIECES (1982)", "The ultimate 'you have to see it to believe it' sleazy slasher. It's exactly what the Mahoning lot was built for."),
        ("RAW FORCE (1982)", "Zombies, cannibal monks, and martial arts. This is a legendary 'Exhumed' style print that defies logic.")
    ],
    "sci-fi": [
        ("X-TRO (1982)", "A bizarre, dark British sci-fi that makes 'Alien' look like a Disney movie. Rare 35mm grain adds to the dread."),
        ("WORLD ON A WIRE (1973)", "Fassbinder's synth-heavy simulation masterpiece. Deeply cool, deeply weird."),
        ("FORBIDDEN WORLD (1982)", "A Roger Corman masterpiece of goopy monsters and cheap sets. Pure drive-in joy.")
    ],
    "family": [
        ("THE LAST UNICORN (1982)", "A hauntingly beautiful animated feature that feels more magical on a flickering 35mm projection."),
        ("THE NEVERENDING STORY (1984)", "The 35mm colors in the Nothing are unbeatable. A childhood dream on a massive screen."),
        ("RAD (1986)", "The ultimate BMX ballyhoo. We're bringing the bikes to the lot for this one!")
    ]
}

def curate_deep_cut(movie, is_35mm):
    m = movie.lower()
    
    # SPECIAL MAPPING FOR WICKED / OZ
    if any(x in m for x in ["wicked", "oz", "wizard"]):
        if is_35mm:
            return ("RETURN TO OZ (1985)", "The 'Deep Cut' Oz experience. This 35mm print is dark, weird, and features the Wheelers. It's the gritty sequel Dorothy deserved.")
        return ("THE WIZARD OF OZ (1939)", "The Technicolor classic. We're pairing the new with the original for a high-energy yellow brick road night.")

    # GENERAL CATEGORY LOGIC
    if any(x in m for x in ["witch", "horror", "scary", "blood", "halloween"]):
        selection = random.choice(VAULT_35MM["horror"])
    elif any(x in m for x in ["space", "alien", "robot", "sci-fi"]):
        selection = random.choice(VAULT_35MM["sci-fi"])
    elif any(x in m for x in ["kids", "lego", "shrek", "disney", "cartoon"]):
        selection = random.choice(VAULT_35MM["family"])
    else:
        selection = ("BIG TROUBLE IN LITTLE CHINA (1986)", "The Mahoning staple. If Rico is programming, Jack Burton is usually involved.")

    return selection

# --- APP ---
st.markdown('<div class="marquee-title">MAHONING MATCHMAKER</div>', unsafe_allow_html=True)

user_movie = st.text_input("ENTER THE MAIN FEATURE:", placeholder="e.g. Wicked")

# THE TOGGLE YOU NEEDED
st.write("### 📽️ THE FORMAT SELECTOR")
is_35mm = st.toggle("LOCK IN 35MM DEEP CUTS?", value=True)

if st.button("CURATE THE VAULT"):
    if user_movie:
        with st.status("🎞️ Threading the projector...", expanded=True) as status:
            time.sleep(1)
            pair_title, pair_why = curate_deep_cut(user_movie, is_35mm)
            status.update(label="Reels Loaded!", state="complete", expanded=False)
            
        st.markdown(f"""
        <div style="border: 5px solid #FFFF00; padding: 30px; background-color: #050505; margin-top:20px;">
            <h1 style="color: #FF0000 !important; text-align: center;">OFFICIAL PROGRAM</h1>
            <p style="font-size: 26px;"><b>FEATURE 1:</b> {user_movie.upper()}</p>
            <p style="font-size: 26px; color: #FFFF00 !important;"><b>FEATURE 2:</b> {pair_title}</p>
            <hr style="border-color: #FFFF00;">
            <p style="font-size: 20px;"><b>THE CURATION:</b> {pair_why}</p>
            <p style="color: #FFFF00 !important; font-style: italic; border: 1px dashed #FFFF00; padding: 10px;">
                🍿 RICO'S NOTE: "Check the cigarette burns for the reel change. That's the 35mm magic!"
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Input a movie for the projectionist!")
