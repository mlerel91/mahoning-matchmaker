import streamlit as st
import time

# --- UI CONFIG ---
st.set_page_config(page_title="Mahoning Matchmaker", layout="centered")

# --- FINAL VISIBILITY FIX (FORCING BRIGHTNESS) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* NEON YELLOW TITLES */
    .marquee-title {
        color: #FFFF00 !important; 
        text-align: center;
        font-size: 50px;
        font-weight: 900;
        text-shadow: 4px 4px #FF0000 !important;
        border-bottom: 5px solid #FFFF00;
        margin-bottom: 20px;
    }

    /* FORCE ALL TEXT TO PURE WHITE */
    h1, h2, h3, p, span, label, div, .stMarkdown { 
        color: #FFFFFF !important; 
        opacity: 1 !important;
        text-shadow: none !important;
    }

    /* INPUT BOX - HIGH CONTRAST */
    .stTextInput input {
        color: #FFFFFF !important;
        background-color: #111111 !important;
        border: 3px solid #FFFF00 !important;
        font-size: 1.5rem !important;
    }

    /* THE BUTTON - PURE RED */
    .stButton button {
        background-color: #FF0000 !important;
        color: #FFFFFF !important;
        border: 2px solid #FFFFFF !important;
        font-size: 28px !important;
        font-weight: 900 !important;
        width: 100%;
        height: 3.5em;
    }
    </style>
""", unsafe_allow_html=True)

# --- THE CURATED SEARCH ENGINE ---
def deep_curate(movie):
    m = movie.lower().strip()
    
    # 1. FOLK HORROR (The Witch / Midsommar)
    if any(word in m for word in ["witch", "midsommar", "folk", "woods"]):
        return {
            "pair": "THE BLOOD ON SATAN'S CLAW (1971)",
            "why": "We're leaning into the 'Folk Horror' aesthetic. We follow the modern dread of your pick with the 35mm godfather of rural occult cinema. Both explore the evil hiding in the soil."
        }
    
    # 2. 80s NEON / VAMPIRES (Lost Boys)
    elif any(word in m for word in ["lost boys", "fright night", "vampire"]):
        return {
            "pair": "NEAR DARK (1987)",
            "why": "The ultimate sunset-to-midnight vampire arc. We start with the neon-glam of the 80s and end with the gritty, dusty, 35mm road-movie vibes of Kathryn Bigelow's masterpiece."
        }
    
    # 3. KIDS / FAMILY (Lego Movie / Shrek)
    elif any(word in m for word in ["lego", "shrek", "toy", "disney", "kids", "pixar"]):
        return {
            "pair": "THE IRON GIANT (1999)",
            "why": "A night of animated soul. We pair your high-energy favorite with the 35mm masterpiece about choosing your own destiny. It’s a perfect family double-feature for the lot."
        }

    # 4. SCI-FI HORROR (Alien / The Thing)
    elif any(word in m for word in ["alien", "thing", "space", "predator"]):
        return {
            "pair": "EVENT HORIZON (1997)",
            "why": "Deep space dread. We move from the isolation of your pick into the cosmic chaos of the 90s. This double-feature makes the night sky above the screen feel very dangerous."
        }

    # 5. SMART FALLBACK (No more Monster Squad!)
    else:
        return {
            "pair": "A MYSTERY 35MM EXHUMED FEATURE",
            "why": "Our archives are researching your unique pick! To match its specific energy, we are programming a Secret Exhumed Films classic that shares its DNA. Expect the unexpected!"
        }

# --- APP LAYOUT ---
st.markdown('<div class="marquee-title">MAHONING MATCHMAKER</div>', unsafe_allow_html=True)

user_movie = st.text_input("1. WHAT MOVIE ARE WE RESEARCHING?", placeholder="e.g. The Witch")
is_35mm = st.toggle("MUST BE 35MM FILM?", value=True)

if st.button("SEARCH & PROGRAM NIGHT"):
    if user_movie:
        with st.status("🧠 Searching film DNA...", expanded=True) as status:
            time.sleep(1)
            st.write(f"Analyzing tone and era for '{user_movie}'...")
            time.sleep(1)
            result = deep_curate(user_movie)
            status.update(label="Night Programmed!", state="complete", expanded=False)
            
        # THE REVEAL
        st.markdown(f"""
        <div style="border: 5px solid #FF0000; padding: 30px; background-color: #050505; margin-top:20px;">
            <h1 style="color: #FFFF00 !important; text-align: center;">THE PROGRAM</h1>
            <p style="font-size: 26px;"><b>FEATURE 1:</b> {user_movie.upper()}</p>
            <p style="font-size: 26px; color: #FF0000 !important;"><b>FEATURE 2:</b> {result['pair']}</p>
            <hr style="border-color: #FFFF00;">
            <p style="font-size: 20px;"><b>WHY RICO CHOSE THIS:</b> {result['why']}</p>
            <p style="color: #FFFF00 !important; font-weight: bold; padding: 10px; border: 1px dashed #FFFF00;">
                🍿 RICO SAYS: "Get to the snack bar early for the themed intermission specials!"
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Enter a movie title so we can start the search!")
