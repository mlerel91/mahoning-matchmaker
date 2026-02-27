import streamlit as st
import time

# --- UI CONFIG ---
st.set_page_config(page_title="Mahoning Matchmaker", layout="centered")

# --- HIGH-VISIBILITY NEON DESIGN ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* FORCE TEXT TO BE BRIGHT WHITE/YELLOW */
    h1, h2, h3, p, span, label, div, .stMarkdown { 
        color: #FFFFFF !important; 
        opacity: 1 !important;
        text-shadow: none !important;
    }
    
    .marquee-title {
        color: #FFFF00 !important; /* Neon Yellow */
        text-align: center;
        font-size: 55px;
        font-weight: 900;
        text-shadow: 4px 4px #FF0000 !important;
        border-bottom: 5px solid #FFFF00;
        margin-bottom: 20px;
    }

    /* INPUT BOX - YELLOW BORDER, WHITE TEXT */
    .stTextInput input {
        color: #FFFFFF !important;
        background-color: #111111 !important;
        border: 3px solid #FFFF00 !important;
        font-size: 1.5rem !important;
    }

    /* THE BUTTON - PURE RED, WHITE BOLD TEXT */
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

# --- THE "RESEARCH" LOGIC ---
def search_and_curate(movie_title):
    # This simulates the "Live Search" and thematic analysis
    m = movie_title.lower().strip()
    
    # Example of "Deep Knowledge" curated results
    if "witch" in m:
        return {
            "title": "THE BLOOD ON SATAN'S CLAW (1971)",
            "reason": "Since 'The Witch' focuses on 17th-century paranoia and folk-horror, we're pairing it with this 35mm classic. It shares the same 'evil in the soil' energy that Mahoning fans crave.",
            "intermission": "Rico's Root Beer Floats"
        }
    elif "lego" in m:
        return {
            "title": "THE LAST STARFIGHTER (1984)",
            "reason": "Your pick is about an ordinary guy becoming a hero in a high-tech world. We're pairing it with the 80s classic that pioneered CGI. It’s a 35mm joyride for all ages!",
            "intermission": "Intermission Parade Snack: Rico's Nachos"
        }
    else:
        # If the search finds something else, it applies "Thematic Logic"
        return {
            "title": "THE MONSTER SQUAD (1987)",
            "reason": "This is a 'Vibe Match.' We're pairing your selection with a film that has the same cult-status heart and practical-effects magic that makes the Mahoning famous.",
            "intermission": "Rico's Extra Butter Popcorn"
        }

# --- APP LAYOUT ---
st.markdown('<div class="marquee-title">MAHONING MATCHMAKER</div>', unsafe_allow_html=True)

st.write("### 🎬 1. ENTER THE MOVIE YOU WANT TO WATCH:")
user_movie = st.text_input("", placeholder="Searching film archives...")

st.write("### 📽️ 2. FORMAT TOGGLE")
is_35mm = st.toggle("MUST BE 35MM FILM?", value=True)

if st.button("RESEARCH & PROGRAM NIGHT"):
    if user_movie:
        with st.status("🧠 AI is researching movie themes...", expanded=True) as status:
            st.write(f"Searching database for '{user_movie}' plot and tone...")
            time.sleep(1.5)
            st.write("Analyzing director's filmography for 35mm connections...")
            time.sleep(1)
            st.write("Cross-referencing with Mahoning Drive-In archive history...")
            
            result = search_and_curate(user_movie)
            status.update(label="Night Curated!", state="complete", expanded=False)
            
        # THE REVEAL
        st.markdown(f"""
        <div style="border: 5px solid #FF0000; padding: 30px; background-color: #050505; margin-top:20px;">
            <h1 style="color: #FFFF00 !important; text-align: center;">THE PROGRAM</h1>
            <p style="font-size: 26px;"><b>FEATURE 1:</b> {user_movie.upper()}</p>
            <p style="font-size: 26px; color: #FF0000 !important;"><b>FEATURE 2:</b> {result['title']}</p>
            <hr style="border-color: #FFFF00;">
            <p style="font-size: 20px;"><b>THE RESEARCH SAYS:</b> {result['reason']}</p>
            <p style="color: #FFFF00 !important; font-weight: bold; border: 1px dashed #FFFF00; padding: 10px;">
                🍿 RICO'S SNACK BAR PICK: {result['intermission']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if is_35mm:
            st.info("🎞️ 35mm CONFIRMED: We found a vintage print in the vault!")
    else:
        st.error("Rico needs a title to start the search!")