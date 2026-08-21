import pickle

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ------------------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="MovieMatch — Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------------------
# THEME — "late-night cinema" palette
#   ink navy background, marquee gold accent, velvet-red rating accent
# ------------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700;800&display=swap');

:root{
  --bg:#090c15;
  --side:#101627;
  --panel:#171e32;
  --panel2:#1d2640;
  --line:#34405d;
  --gold:#f5c84b;
  --gold2:#ffd96a;
  --text:#f7f8fb;
  --muted:#b9c2d7;
  --red:#ff5555;
}

/* ===== STREAMLIT SHELL ===== */
.stApp{background:var(--bg)!important;color:var(--text)!important;font-family:'Inter',sans-serif!important;}
[data-testid="stAppViewContainer"]{background:var(--bg)!important;}
[data-testid="stHeader"]{background:var(--bg)!important;border-bottom:1px solid #151c2d!important;}
[data-testid="stToolbar"]{background:transparent!important;}
[data-testid="stDecoration"]{display:none!important;}
[data-testid="stAppViewContainer"] .main .block-container{
  max-width:1420px!important;
  padding:1.6rem 2.5rem 3.5rem!important;
}

/* ===== SIDEBAR / MAIN BALANCE ===== */
section[data-testid="stSidebar"]{
  width:320px!important;
  min-width:320px!important;
  background:linear-gradient(180deg,#111729 0%,#0d1220 100%)!important;
  border-right:1px solid #303951!important;
}
section[data-testid="stSidebar"]>div:first-child{padding:1.25rem 1.2rem 2rem!important;}
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"]{gap:.55rem!important;}

/* ===== SIDEBAR TEXT ===== */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4{color:var(--gold)!important;}
section[data-testid="stSidebar"] label{color:#dce2ef!important;font-weight:700!important;}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stSlider label,
section[data-testid="stSidebar"] .stRadio label{color:#dce2ef!important;}

/* ===== SIDEBAR INPUTS ===== */
section[data-testid="stSidebar"] div[data-baseweb="select"]{
  background:#1a2135!important;border:1px solid #3b4665!important;border-radius:9px!important;
}
section[data-testid="stSidebar"] div[data-baseweb="select"] *{color:#f7f8fb!important;}
section[data-testid="stSidebar"] [data-testid="stSlider"] [role="slider"]{background:var(--red)!important;border-color:var(--red)!important;}
section[data-testid="stSidebar"] [data-testid="stSlider"] div[data-baseweb="slider"]>div>div{background:#3b4660!important;}

/* ===== GRID / LIST: FORCE VISIBILITY ===== */
section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"]{
  display:flex!important;gap:18px!important;align-items:center!important;
}
section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"]>label{
  color:#f7f8fb!important;opacity:1!important;background:transparent!important;
  display:flex!important;align-items:center!important;gap:7px!important;
  padding:4px 0!important;
}
section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"]>label *{
  color:#f7f8fb!important;opacity:1!important;visibility:visible!important;
}
section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"]>label p{
  color:#f7f8fb!important;font-weight:700!important;font-size:.9rem!important;
  margin:0!important;
}
section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"]>label:has(input:checked) p{color:var(--gold)!important;}

/* ===== CTA ===== */
section[data-testid="stSidebar"] .stButton>button{
  width:100%!important;height:50px!important;margin:.35rem 0 .7rem!important;
  background:linear-gradient(135deg,var(--gold),var(--gold2))!important;
  color:#151922!important;border:0!important;border-radius:11px!important;
  font-weight:800!important;box-shadow:0 10px 24px rgba(245,200,75,.16)!important;
}
section[data-testid="stSidebar"] .stButton>button *{color:#151922!important;}

/* ===== VISIBLE WATCHLIST PANEL ===== */
.watchlist-panel{
  margin-top:.35rem;
  background:linear-gradient(145deg,#151d31,#1b2440);
  border:1px solid #3b4665;
  border-radius:13px;
  overflow:hidden;
}
.watchlist-head{
  padding:13px 15px;
  color:var(--gold)!important;
  font-weight:800;
  border-bottom:1px solid #35405d;
  background:#192139;
}
.watchlist-empty{padding:15px;color:#b9c2d7!important;font-size:.82rem;line-height:1.45;}
.watch-item{
  padding:10px 14px;
  color:#f7f8fb!important;
  border-bottom:1px solid #2c3550;
  font-size:.84rem;
  line-height:1.25;
}
.watch-item:last-child{border-bottom:0;}

/* ===== HERO ===== */
.marquee-lights{display:flex;justify-content:center;gap:9px;margin:.2rem 0 .55rem;}
.marquee-lights span{width:7px;height:7px;border-radius:50%;background:var(--gold);box-shadow:0 0 8px rgba(245,200,75,.65);}
.hero-title{
  text-align:center!important;color:var(--gold)!important;
  font-family:'Bebas Neue',sans-serif!important;font-size:4.15rem!important;
  letter-spacing:.06em!important;line-height:1!important;margin:0!important;
}
.hero-sub{text-align:center;color:#c0c8da!important;font-size:1rem;line-height:1.5;margin:.65rem auto 1.35rem!important;}

/* ===== FILM STRIP ===== */
.filmstrip{
  height:21px!important;margin:1.1rem 0 1.55rem!important;border-radius:5px!important;
  border:1px solid #303a57!important;background-color:#182038!important;
  background-image:radial-gradient(circle at center,#080c15 5px,transparent 5.5px)!important;
  background-size:26px 21px!important;
}

/* ===== METRICS ===== */
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #171e32, #1d2640) !important;
    border: 1px solid #394462 !important;
    border-radius: 14px !important;
    min-height: 108px !important;
    padding: 1rem 1.2rem !important;
    box-shadow: 0 8px 22px rgba(0, 0, 0, 0.18) !important;
}

div[data-testid="stMetric"] label {
    color: #FFFFFF !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #FFFFFF !important;
}

div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
    color: #D1D5DB !important;
}

/* ===== INFO PANEL ===== */
[data-testid="stAlert"]{
  background:#17233e!important;border:1px solid #3a4b6f!important;color:#f7f8fb!important;border-radius:0!important;
}
[data-testid="stAlert"] *{color:#f7f8fb!important;}

/* ===== RESULT HEADING ===== */
.results-heading{
  background:linear-gradient(90deg,#17233d,#141b2d)!important;
  border:1px solid #35405d!important;border-radius:12px!important;
  padding:13px 18px!important;margin:1rem 0 1.2rem!important;
}
.results-heading h3{color:var(--gold)!important;margin:0!important;font-size:1.15rem!important;}

/* ===== MOVIE CARDS ===== */
.movie-card{
  position:relative;min-height:150px;
  background:linear-gradient(145deg,#171e32,#1d2640)!important;
  border:1px solid #394462!important;border-radius:14px!important;
  padding:1.15rem 1.1rem 1rem 1.25rem!important;margin:.15rem 0 .5rem!important;
  box-shadow:0 8px 20px rgba(0,0,0,.15)!important;
}
.movie-card:hover{border-color:var(--gold)!important;transform:translateY(-2px);}
.rank-badge{
  position:absolute;top:-10px;left:-10px;width:37px;height:37px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;background:var(--gold)!important;
  color:#151922!important;font-weight:800;border:2px solid var(--bg)!important;
}
.card-title{color:#f8f9fc!important;font-family:'Bebas Neue',sans-serif!important;font-size:1.5rem!important;}
.card-year{color:#aeb8ce!important;}
.genre-pill{display:inline-block;background:rgba(255,85,85,.12)!important;color:#ff8e88!important;border:1px solid rgba(255,85,85,.35)!important;border-radius:999px;padding:.15rem .6rem;font-size:.72rem;font-weight:700;margin:.35rem 0 .5rem;}
.stars{color:var(--gold)!important;}.stars .empty{color:#4e5873!important;}.rating-num{color:#b9c2d7!important;}
.pop-label{color:#aeb8ce!important;}.overview-txt{color:#c9d0df!important;line-height:1.55;}

/* ===== CHECKBOX ===== */
[data-testid="stCheckbox"] label,
[data-testid="stCheckbox"] label *{color:#f5c84b!important;opacity:1!important;font-weight:700!important;visibility:visible!important;}

/* ===== EXPANDER ===== */
[data-testid="stExpander"]{background:#151d31!important;border:1px solid #3a4563!important;border-radius:10px!important;}
[data-testid="stExpander"] summary,[data-testid="stExpander"] summary *{color:#f7f8fb!important;opacity:1!important;}

/* ===== DOWNLOAD BUTTON ===== */
.stDownloadButton>button{background:#151d31!important;color:var(--gold)!important;border:1px solid var(--gold)!important;border-radius:9px!important;}
.stDownloadButton>button *{color:var(--gold)!important;}

/* ===== PLOT ===== */
.js-plotly-plot{background:#111729!important;border:1px solid #34405d!important;border-radius:13px!important;padding:4px!important;}

/* ===== MOBILE ===== */
@media(max-width:900px){
  section[data-testid="stSidebar"]{width:280px!important;min-width:280px!important;}
  [data-testid="stAppViewContainer"] .main .block-container{padding:1rem!important;}
  .hero-title{font-size:2.8rem!important;}
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# LOAD THE TRAINED MODEL BUNDLE (cached so it only loads once)
# ------------------------------------------------------------------------------
@st.cache_resource
def load_bundle(path="movies1.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)


bundle = load_bundle()
df = bundle["df"]
nn_model = bundle["nn_model"]
genre_feature_names = bundle["genre_feature_names"]
POPULARITY_WEIGHT = bundle["popularity_weight"]
RATING_WEIGHT = bundle["rating_weight"]


# ------------------------------------------------------------------------------
# RECOMMENDATION FUNCTION (same core logic as the notebook — untouched)
# ------------------------------------------------------------------------------
def recommend_by_genre(genre, top_n=10, min_vote_count=100):
    query = np.zeros(len(genre_feature_names) + 2)
    genre_idx = genre_feature_names.index(genre)
    query[genre_idx] = 1
    query[-2] = POPULARITY_WEIGHT
    query[-1] = RATING_WEIGHT
    query = query.reshape(1, -1)

    distances, indices = nn_model.kneighbors(query, n_neighbors=min(200, len(df)))
    candidates = df.iloc[indices[0]].copy()

    candidates = candidates[
        candidates["genre_list"].apply(lambda g: genre in g)
        & (candidates["vote_count"] >= min_vote_count)
    ]
    candidates = candidates.sort_values(["weighted_rating", "popularity"], ascending=[False, False])

    return candidates[[
        "title", "genre", "release_year", "vote_average",
        "vote_count", "popularity", "weighted_rating", "overview",
    ]].head(top_n).reset_index(drop=True)


# ------------------------------------------------------------------------------
# SMALL UI HELPERS
# ------------------------------------------------------------------------------
def star_html(rating_out_of_10: float) -> str:
    filled = int(round(rating_out_of_10 / 2))
    filled = max(0, min(5, filled))
    stars = "★" * filled + "<span class='empty'>" + "★" * (5 - filled) + "</span>"
    return f"<span class='stars'>{stars}</span><span class='rating-num'>{rating_out_of_10:.1f}/10</span>"


def pop_bar_html(value: float, max_value: float) -> str:
    pct = 0 if max_value <= 0 else max(4, min(100, round(value / max_value * 100)))
    return (
        "<div class='pop-label'><span>Popularity</span><span>" + f"{value:.1f}" + "</span></div>"
        f"<div class='pop-bar-bg'><div class='pop-bar-fill' style='width:{pct}%;'></div></div>"
    )


if "favorites" not in st.session_state:
    st.session_state.favorites = set()
if "show_results" not in st.session_state:
    st.session_state.show_results = False


# ------------------------------------------------------------------------------
# SIDEBAR — "ticket booth"
# ------------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🎟️ Build Your Screening")
    selected_genre = st.selectbox("Genre", sorted(genre_feature_names))
    top_n = st.slider("Number of picks", min_value=5, max_value=25, value=10)
    min_votes = st.slider("Minimum audience votes", 0, 2000, 100, step=50)
    min_year, max_year = int(df["release_year"].min()), int(df["release_year"].max())
    year_range = st.slider("Release year range", min_year, max_year, (min_year, max_year))
    sort_by = st.selectbox(
        "Sort by",
        ["Best Match", "Highest Rated", "Most Popular", "Newest First", "Oldest First"],
    )
    view_mode = st.radio("Layout", ["Grid", "List"], horizontal=True)
    run_clicked = st.button("🎬  Get Recommendations", type="primary", width="stretch")

    st.markdown("<div class='filmstrip'></div>", unsafe_allow_html=True)
    watch_items = sorted(st.session_state.favorites)
    if watch_items:
        items_html = "".join(f"<div class='watch-item'>🍿 {t}</div>" for t in watch_items)
    else:
        items_html = "<div class='watchlist-empty'>Nothing saved yet.<br>Use <b>Add to Watchlist</b> on a recommendation.</div>"
    st.markdown(
        f"<div class='watchlist-panel'><div class='watchlist-head'>🍿 Your Watchlist ({len(watch_items)})</div>{items_html}</div>",
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------------------------
# HERO
# ------------------------------------------------------------------------------
st.markdown("<div class='marquee-lights'>" + "<span></span>" * 18 + "</div>", unsafe_allow_html=True)
st.markdown("<h1 class='hero-title'>🎬 MovieMATCH</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='hero-sub'>Nearest-neighbour picks, ranked by rating &amp; popularity — pick a genre and roll the reel.</p>",
    unsafe_allow_html=True,
)
st.markdown("<div class='filmstrip'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# LIBRARY STATS
# ------------------------------------------------------------------------------
c1, c2, c3, c4 = st.columns(4, gap="large")
c1.metric("Films in Library", f"{len(df):,}")
c2.metric("Genres Tracked", f"{len(genre_feature_names)}")
c3.metric("Avg. Rating", f"{df['vote_average'].mean():.1f} / 10")
c4.metric("Now Screening", selected_genre)

# ------------------------------------------------------------------------------
# MAIN CONTENT
# ------------------------------------------------------------------------------
if run_clicked:
    st.session_state.show_results = True

if st.session_state.show_results:
    results = recommend_by_genre(selected_genre, top_n=top_n * 3, min_vote_count=min_votes)
    results = results[
        (results["release_year"] >= year_range[0]) & (results["release_year"] <= year_range[1])
    ].copy()

    sort_map = {
        "Highest Rated": ("vote_average", False),
        "Most Popular": ("popularity", False),
        "Newest First": ("release_year", False),
        "Oldest First": ("release_year", True),
    }
    if sort_by in sort_map:
        col, asc = sort_map[sort_by]
        results = results.sort_values(col, ascending=asc)
    results = results.head(top_n).reset_index(drop=True)

    if results.empty:
        st.warning("No movies match these filters. Try loosening the vote count or year range.")
    else:
        st.markdown(f"<div class='results-heading'><h3>Top {len(results)} {selected_genre} picks for you</h3></div>", unsafe_allow_html=True)

        # --- interactive chart: rating vs popularity for this result set ---
        fig = px.scatter(
            results,
            x="vote_average",
            y="popularity",
            size="vote_count",
            color="weighted_rating",
            hover_name="title",
            size_max=38,
            color_continuous_scale=["#5B6288", "#C1443C", "#E8B94D"],
            labels={"vote_average": "Rating", "popularity": "Popularity", "weighted_rating": "Score"},
        )
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#F2F0E8", family="Inter"),
            margin=dict(l=10, r=10, t=10, b=10),
            height=320,
            coloraxis_colorbar=dict(title="Score"),
        )
        fig.update_xaxes(gridcolor="#2A2F4A", zerolinecolor="#2A2F4A")
        fig.update_yaxes(gridcolor="#2A2F4A", zerolinecolor="#2A2F4A")
        st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})

        st.download_button(
            "⬇️ Export these picks as CSV",
            data=results.to_csv(index=False).encode("utf-8"),
            file_name=f"{selected_genre.lower()}_recommendations.csv",
            mime="text/csv",
        )

        st.markdown("<div class='filmstrip'></div>", unsafe_allow_html=True)

        max_pop = results["popularity"].max()
        n_cols = 1 if view_mode == "List" else 2
        cols = st.columns(n_cols, gap="large")

        for i, row in results.iterrows():
            with cols[i % n_cols]:
                with st.container():
                    st.markdown(
                        f"""
                        <div class="movie-card">
                            <div class="rank-badge">{i + 1}</div>
                            <div class="card-title">{row['title']} <span class="card-year">({int(row['release_year'])})</span></div>
                            <div class="genre-pill">{row['genre']}</div>
                            <div>{star_html(row['vote_average'])}</div>
                            {pop_bar_html(row['popularity'], max_pop)}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    fav_key = f"fav_{selected_genre}_{row['title']}_{i}"
                    is_fav = st.checkbox(
                        "🍿 Add to Watchlist",
                        value=row["title"] in st.session_state.favorites,
                        key=fav_key,
                    )
                    if is_fav:
                        st.session_state.favorites.add(row["title"])
                    else:
                        st.session_state.favorites.discard(row["title"])

                    with st.expander("Movie Overview"):
                        st.markdown(f"<div class='overview-txt'>{row['overview']}</div>", unsafe_allow_html=True)
                        st.caption(f"👥 {int(row['vote_count']):,} votes  ·  📈 weighted score {row['weighted_rating']:.1f}")

else:
    st.info("Set your preferences in the sidebar and click **🎬 Get Recommendations** to roll the reel.")

    st.markdown("<div class='filmstrip'></div>", unsafe_allow_html=True)
    st.markdown("#### 📊 What's in the library")

    exploded = df.explode("genre_list")
    genre_counts = (
        exploded["genre_list"].value_counts().sort_values(ascending=True).reset_index()
    )
    genre_counts.columns = ["genre", "count"]

    fig2 = go.Figure(
        go.Bar(
            x=genre_counts["count"],
            y=genre_counts["genre"],
            orientation="h",
            marker=dict(
                color=genre_counts["count"],
                colorscale=[[0, "#5B6288"], [0.5, "#C1443C"], [1, "#E8B94D"]],
            ),
        )
    )
    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F2F0E8", family="Inter"),
        margin=dict(l=10, r=10, t=10, b=10),
        height=360,
        xaxis_title="Number of films",
    )
    fig2.update_xaxes(gridcolor="#2A2F4A")
    fig2.update_yaxes(gridcolor="#2A2F4A")
    st.plotly_chart(fig2, width="stretch", config={"displayModeBar": False})