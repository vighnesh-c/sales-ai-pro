# =============================================
# SALES AI WEB APP - ULTIMATE VERSION
# WITH IMAGES + LOGOS + STUNNING UI ✅
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pickle
import os

# =============================================
# PAGE CONFIGURATION
# =============================================

st.set_page_config(
    page_title="Sales AI Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================
# ALL IMAGES & LOGOS (Online URLs - No Download!)
# =============================================

LOGO_URL = "https://img.icons8.com/fluency/96/artificial-intelligence.png"
BRAIN_URL = "https://img.icons8.com/fluency/64/brain.png"
CHART_URL = "https://img.icons8.com/fluency/64/combo-chart.png"
ROCKET_URL = "https://img.icons8.com/fluency/64/rocket.png"
TROPHY_URL = "https://img.icons8.com/fluency/64/trophy.png"
MONEY_URL = "https://img.icons8.com/fluency/64/money-bag.png"
ROBOT_URL = "https://img.icons8.com/fluency/64/bot.png"
FIRE_URL = "https://img.icons8.com/fluency/64/fire-element.png"
SHIELD_URL = "https://img.icons8.com/fluency/64/shield.png"
STAR_URL = "https://img.icons8.com/fluency/64/star.png"
UPLOAD_URL = "https://img.icons8.com/fluency/96/upload-to-cloud.png"
PREDICT_URL = "https://img.icons8.com/fluency/96/crystal-ball.png"
CHAT_URL = "https://img.icons8.com/fluency/96/chat.png"
DATA_URL = "https://img.icons8.com/fluency/96/data-configuration.png"
BANNER_URL = "https://img.icons8.com/fluency/200/combo-chart--v2.png"

# =============================================
# STUNNING CSS STYLING
# =============================================

st.markdown("""
<style>
/* ── Main background ── */
.stApp {
    background: linear-gradient(
        135deg,
        #050510 0%,
        #0a0a1a 30%,
        #0d0d2a 60%,
        #0a0a1a 100%
    );
}

/* ── Animated gradient header ── */
.main-header {
    font-size: 52px;
    font-weight: 900;
    background: linear-gradient(
        90deg,
        #00d2ff,
        #7b2ff7,
        #ff6b6b,
        #00d2ff
    );
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    padding: 10px 0;
    letter-spacing: 2px;
}

/* ── Sub header ── */
.sub-header {
    font-size: 14px;
    color: #606090;
    text-align: center;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

/* ── Feature cards ── */
.feature-card {
    background: linear-gradient(
        135deg,
        rgba(30,30,60,0.8),
        rgba(20,20,50,0.9)
    );
    border: 1px solid rgba(100,100,200,0.3);
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

/* ── Glowing metric cards ── */
div[data-testid="metric-container"] {
    background: linear-gradient(
        135deg,
        rgba(30,30,60,0.9),
        rgba(20,20,50,0.9)
    );
    border: 1px solid rgba(0,210,255,0.2);
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 0 20px rgba(0,210,255,0.05);
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #050510,
        #0a0a1a
    );
    border-right: 1px solid rgba(100,100,200,0.2);
}

/* ── Navigation radio ── */
section[data-testid="stSidebar"] .stRadio label {
    color: #a0a0d0 !important;
    font-size: 14px !important;
    padding: 6px 0 !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(
        90deg, #00d2ff, #7b2ff7
    );
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 30px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1px;
    width: 100%;
    transition: all 0.3s;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(123,47,247,0.5);
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(30,30,60,0.8);
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    color: #8080b0;
    border-radius: 10px;
    padding: 8px 20px;
    font-size: 14px;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(
        90deg,
        rgba(0,210,255,0.15),
        rgba(123,47,247,0.15)
    );
    color: #00d2ff !important;
}

/* ── Chat messages ── */
.stChatMessage {
    background: rgba(30,30,60,0.8) !important;
    border: 1px solid rgba(100,100,200,0.3) !important;
    border-radius: 16px !important;
    padding: 8px !important;
    margin: 8px 0 !important;
    backdrop-filter: blur(10px) !important;
}
.stChatMessage p {
    font-size: 15px !important;
    line-height: 1.8 !important;
    color: #e0e0ff !important;
}
.stChatMessage li {
    margin-bottom: 8px !important;
    color: #c0c0e0 !important;
    line-height: 1.7 !important;
}

/* ── Divider ── */
hr { border-color: rgba(100,100,200,0.2); }

/* ── Headings ── */
h1, h2, h3 { color: #e0e0ff !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #050510; }
::-webkit-scrollbar-thumb {
    background: #3a3a6a;
    border-radius: 2px;
}
</style>
""", unsafe_allow_html=True)

# =============================================
# STUNNING HEADER WITH LOGO
# =============================================

col_logo, col_title, col_logo2 = st.columns([1, 4, 1])

with col_logo:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(LOGO_URL, width=80)

with col_title:
    st.markdown(
        '<p class="main-header">⚡ Sales AI Pro</p>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="sub-header">✦ Next Generation AI Powered Sales Intelligence Platform ✦</p>',
        unsafe_allow_html=True
    )

with col_logo2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(BRAIN_URL, width=80)

st.divider()

# =============================================
# SIDEBAR WITH LOGO
# =============================================

with st.sidebar:
    # Logo and branding
    st.markdown("""
    <div style='text-align:center; padding:15px 0'>
    """, unsafe_allow_html=True)

    st.image(LOGO_URL, width=70)

    st.markdown("""
        <div style='font-size:22px; font-weight:800;
        background:linear-gradient(90deg,#00d2ff,#7b2ff7);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        margin-top:8px'>Sales AI Pro</div>
        <div style='color:#505080; font-size:11px;
        letter-spacing:3px; margin-top:2px'>
        INTELLIGENCE PLATFORM</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "🧭 Navigate",
        [
            "🏠 Home",
            "📊 Data Overview",
            "📈 Charts",
            "🤖 AI Predictions",
            "💬 AI Assistant"
        ]
    )

    st.divider()

    # Live data status
    if 'df' in st.session_state:
        df_side = st.session_state['df']
        st.markdown(f"""
        <div style='background:linear-gradient(
        135deg,rgba(0,210,255,0.1),
        rgba(123,47,247,0.1));
        border:1px solid rgba(0,210,255,0.3);
        border-radius:12px; padding:14px;
        text-align:center'>
            <div style='color:#00d2ff; font-size:11px;
            letter-spacing:2px'>✅ DATA LOADED</div>
            <div style='color:#e0e0ff; font-size:24px;
            font-weight:800; margin:6px 0'>
            {len(df_side):,}</div>
            <div style='color:#8080b0; font-size:12px'>
            rows × {len(df_side.columns)} columns</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background:rgba(30,30,60,0.5);
        border:1px solid rgba(100,100,200,0.2);
        border-radius:12px; padding:14px;
        text-align:center'>
            <div style='color:#505080; font-size:13px'>
            ⚪ No data loaded</div>
            <div style='color:#404060; font-size:11px;
            margin-top:4px'>Upload a file to begin</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Tech stack badges
    st.markdown("""
    <div style='text-align:center'>
        <div style='color:#505080; font-size:11px;
        letter-spacing:2px; margin-bottom:10px'>
        POWERED BY</div>
        <div style='display:flex; flex-wrap:wrap;
        gap:6px; justify-content:center'>
            <span style='background:rgba(0,210,255,0.1);
            border:1px solid rgba(0,210,255,0.3);
            color:#00d2ff; font-size:10px; padding:3px 8px;
            border-radius:20px'>Python</span>
            <span style='background:rgba(123,47,247,0.1);
            border:1px solid rgba(123,47,247,0.3);
            color:#7b2ff7; font-size:10px; padding:3px 8px;
            border-radius:20px'>Streamlit</span>
            <span style='background:rgba(255,107,107,0.1);
            border:1px solid rgba(255,107,107,0.3);
            color:#ff6b6b; font-size:10px; padding:3px 8px;
            border-radius:20px'>Scikit-learn</span>
            <span style='background:rgba(0,255,136,0.1);
            border:1px solid rgba(0,255,136,0.3);
            color:#00ff88; font-size:10px; padding:3px 8px;
            border-radius:20px'>Groq AI</span>
            <span style='background:rgba(255,200,0,0.1);
            border:1px solid rgba(255,200,0,0.3);
            color:#ffc800; font-size:10px; padding:3px 8px;
            border-radius:20px'>Plotly</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =============================================
# HELPER FUNCTIONS
# =============================================

def load_data(uploaded_file):
    file_name = uploaded_file.name
    file_type = file_name.split(".")[-1].lower()
    try:
        if file_type == "csv":
            try:
                df = pd.read_csv(uploaded_file)
            except:
                df = pd.read_csv(
                    uploaded_file, encoding="latin1"
                )
        elif file_type in ["xlsx", "xls"]:
            df = pd.read_excel(uploaded_file)
        elif file_type == "json":
            df = pd.read_json(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None


def safe_sum(df, col):
    if col in df.columns:
        return df[col].sum()
    return 0


def safe_max(df, col):
    if col in df.columns:
        return df[col].max()
    return 0


def get_data_summary(df):
    summary = f"Dataset: {len(df)} rows, "
    summary += f"{len(df.columns)} columns.\n"
    summary += f"Columns: {', '.join(df.columns.tolist())}\n\n"
    num_cols = df.select_dtypes(
        include=[np.number]
    ).columns.tolist()
    if num_cols:
        summary += "Stats:\n"
        for col in num_cols[:6]:
            try:
                summary += f"- {col}: "
                summary += f"Total={df[col].sum():,.2f}, "
                summary += f"Avg={df[col].mean():,.2f}, "
                summary += f"Max={df[col].max():,.2f}\n"
            except:
                pass
    txt_cols = df.select_dtypes(
        include=['object']
    ).columns.tolist()
    if txt_cols:
        summary += "\nTop values:\n"
        for col in txt_cols[:4]:
            try:
                top = df[col].value_counts().index[0]
                cnt = df[col].value_counts().iloc[0]
                summary += f"- {col}: '{top}' ({cnt}x)\n"
            except:
                pass
    return summary


def load_model():
    try:
        if (os.path.exists("model.pkl") and
                os.path.exists("features.pkl")):
            with open("model.pkl", "rb") as f:
                model = pickle.load(f)
            with open("features.pkl", "rb") as f:
                features = pickle.load(f)
            return model, features
    except:
        pass
    return None, None

# =============================================
# HOME PAGE
# =============================================

if page == "🏠 Home":

    # Hero banner
    st.markdown("""
    <div style='background:linear-gradient(
    135deg,rgba(0,210,255,0.05),
    rgba(123,47,247,0.05));
    border:1px solid rgba(100,100,200,0.2);
    border-radius:24px; padding:40px;
    text-align:center; margin-bottom:30px'>
        <div style='font-size:56px; margin-bottom:10px'>
        ⚡</div>
        <div style='font-size:28px; font-weight:800;
        color:#e0e0ff; margin-bottom:10px'>
        Welcome to Sales AI Pro</div>
        <div style='font-size:15px; color:#8080b0;
        line-height:2; max-width:600px; margin:0 auto'>
        The most advanced AI-powered sales intelligence
        platform. Upload your data and get instant
        analysis, predictions, and AI insights.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature cards with icons
    col1, col2, col3, col4 = st.columns(4)

    features = [
        (DATA_URL, "Data Analysis",
         "Instant stats, quality check & column info",
         "#00d2ff"),
        (CHART_URL, "Visual Charts",
         "Beautiful interactive charts & graphs",
         "#7b2ff7"),
        (PREDICT_URL, "AI Predictions",
         "ML powered sales forecasting",
         "#ff6b6b"),
        (CHAT_URL, "AI Assistant",
         "Chat with AI about your data",
         "#00ff88"),
    ]

    for col, (img, title, desc, color) in zip(
        [col1, col2, col3, col4], features
    ):
        with col:
            st.image(img, width=60)
            st.markdown(f"""
            <div style='background:linear-gradient(
            135deg,rgba(30,30,60,0.8),
            rgba(20,20,50,0.9));
            border:1px solid rgba(100,100,200,0.2);
            border-radius:16px; padding:16px;
            margin-top:8px'>
                <div style='color:{color};
                font-weight:700; font-size:15px;
                margin-bottom:8px'>{title}</div>
                <div style='color:#8080b0;
                font-size:13px; line-height:1.6'>
                {desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    # Upload section
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📁 Upload Your Sales Data")
        uploaded_file = st.file_uploader(
            "Drop your file here",
            type=["csv", "xlsx", "xls", "json"],
            help="CSV, Excel or JSON"
        )

        if uploaded_file is not None:
            df = load_data(uploaded_file)
            if df is not None:
                st.session_state['df'] = df
                st.session_state['filename'] = (
                    uploaded_file.name
                )
                st.success(
                    f"✅ {uploaded_file.name} loaded!"
                )

                st.divider()
                st.subheader("⚡ Quick Stats")
                c1, c2, c3, c4 = st.columns(4)

                num_cols = df.select_dtypes(
                    include=[np.number]
                ).columns.tolist()

                with c1:
                    st.metric("📋 Records",
                              f"{len(df):,}")
                with c2:
                    st.metric("📊 Columns",
                              len(df.columns))
                with c3:
                    if len(num_cols) > 0:
                        v = df[num_cols[0]].sum()
                        st.metric(
                            f"💰 {num_cols[0]}",
                            f"{v:,.0f}"
                        )
                with c4:
                    if len(num_cols) > 1:
                        v = df[num_cols[1]].sum()
                        st.metric(
                            f"📈 {num_cols[1]}",
                            f"{v:,.0f}"
                        )

                st.info(
                    "✅ Use the sidebar to explore!"
                )

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image(UPLOAD_URL, width=120)
        st.markdown("""
        <div style='background:rgba(30,30,60,0.8);
        border:1px solid rgba(100,100,200,0.2);
        border-radius:16px; padding:16px;
        margin-top:16px'>
            <div style='color:#a0a0d0; font-size:13px;
            line-height:2'>
            ✅ CSV files<br>
            ✅ Excel (xlsx/xls)<br>
            ✅ JSON files<br>
            ✅ Any column names<br>
            ✅ Auto error handling
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Stats banner
    col1, col2, col3, col4 = st.columns(4)
    stats = [
        (FIRE_URL, "100%", "Free to Use"),
        (SHIELD_URL, "Secure", "Local Processing"),
        (ROCKET_URL, "Fast", "Instant Analysis"),
        (STAR_URL, "AI", "Powered Assistant"),
    ]
    for col, (img, val, label) in zip(
        [col1, col2, col3, col4], stats
    ):
        with col:
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image(img, width=40)
            with c2:
                st.markdown(f"""
                <div style='color:#e0e0ff;
                font-weight:700; font-size:16px'>
                {val}</div>
                <div style='color:#606080;
                font-size:12px'>{label}</div>
                """, unsafe_allow_html=True)

# =============================================
# DATA OVERVIEW PAGE
# =============================================

elif page == "📊 Data Overview":

    col1, col2 = st.columns([1, 8])
    with col1:
        st.image(DATA_URL, width=50)
    with col2:
        st.header("Data Overview")

    if 'df' not in st.session_state:
        st.warning("⚠️ Upload a file first!")
        st.info("👈 Go to Home page")
    else:
        df = st.session_state['df']

        st.markdown(f"""
        <div style='background:rgba(0,210,255,0.05);
        border:1px solid rgba(0,210,255,0.2);
        border-radius:12px; padding:12px 20px;
        color:#8080b0; font-size:14px;
        margin-bottom:20px'>
            📄 <b style='color:#00d2ff'>
            {st.session_state['filename']}</b>
            &nbsp;·&nbsp; {len(df):,} rows
            &nbsp;·&nbsp; {len(df.columns)} columns
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs([
            "📋 Data Table",
            "📈 Statistics",
            "🔍 Quality Check"
        ])

        with tab1:
            num_rows = st.slider(
                "Rows to show", 5,
                min(100, len(df)), 10
            )
            st.dataframe(
                df.head(num_rows),
                use_container_width=True
            )

        with tab2:
            st.dataframe(
                df.describe(),
                use_container_width=True
            )
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes.values,
                'Non-Null': df.count().values,
                'Nulls': df.isnull().sum().values,
                'Unique': df.nunique().values
            })
            st.dataframe(
                col_info,
                use_container_width=True
            )

        with tab3:
            c1, c2, c3 = st.columns(3)
            missing = df.isnull().sum().sum()
            dups = df.duplicated().sum()
            num_c = len(df.select_dtypes(
                include=[np.number]).columns)

            with c1:
                st.metric(
                    "Missing Values", missing,
                    delta="✅ Clean!" if missing == 0
                    else "⚠️ Fix needed"
                )
            with c2:
                st.metric(
                    "Duplicates", dups,
                    delta="✅ None!" if dups == 0
                    else "⚠️ Found"
                )
            with c3:
                st.metric("Numeric Columns", num_c)

            if missing == 0 and dups == 0:
                st.success(
                    "✅ Perfect data quality!"
                )

# =============================================
# CHARTS PAGE
# =============================================

elif page == "📈 Charts":

    col1, col2 = st.columns([1, 8])
    with col1:
        st.image(CHART_URL, width=50)
    with col2:
        st.header("Charts & Analysis")

    if 'df' not in st.session_state:
        st.warning("⚠️ Upload a file first!")
    else:
        df = st.session_state['df']
        num_cols = df.select_dtypes(
            include=[np.number]
        ).columns.tolist()
        PT = "plotly_dark"

        def styled_fig(fig):
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(30,30,60,0.4)',
                font_color='#e0e0ff',
                title_font_color='#00d2ff'
            )
            return fig

        if 'Category' in df.columns and \
                'Sales' in df.columns:
            st.subheader("📦 Sales by Category")
            cat = df.groupby(
                'Category'
            )['Sales'].sum().reset_index()
            fig = px.bar(
                cat, x='Category', y='Sales',
                color='Category',
                title='Sales by Category',
                template=PT, text_auto=True,
                color_discrete_sequence=
                px.colors.sequential.Plasma
            )
            st.plotly_chart(
                styled_fig(fig),
                use_container_width=True
            )

        if 'Region' in df.columns and \
                'Sales' in df.columns:
            st.subheader("🌍 Sales by Region")
            c1, c2 = st.columns(2)
            reg = df.groupby(
                'Region'
            )['Sales'].sum().reset_index()
            with c1:
                fig2 = px.pie(
                    reg, values='Sales',
                    names='Region',
                    title='Region Distribution',
                    template=PT,
                    color_discrete_sequence=
                    px.colors.sequential.Plasma
                )
                st.plotly_chart(
                    styled_fig(fig2),
                    use_container_width=True
                )
            with c2:
                fig3 = px.bar(
                    reg, x='Region', y='Sales',
                    color='Sales',
                    title='Region Comparison',
                    template=PT,
                    color_continuous_scale='Plasma'
                )
                st.plotly_chart(
                    styled_fig(fig3),
                    use_container_width=True
                )

        if 'Profit' in df.columns and \
                'Sales' in df.columns:
            st.subheader("💰 Profit vs Sales")
            fig4 = px.scatter(
                df, x='Sales', y='Profit',
                color='Category' if 'Category'
                in df.columns else None,
                title='Profit vs Sales Scatter',
                template=PT, opacity=0.7,
                color_discrete_sequence=
                px.colors.sequential.Plasma
            )
            st.plotly_chart(
                styled_fig(fig4),
                use_container_width=True
            )

        if 'Product Name' in df.columns and \
                'Sales' in df.columns:
            st.subheader("🏆 Top 10 Products")
            top = df.groupby(
                'Product Name'
            )['Sales'].sum().nlargest(
                10
            ).reset_index()
            fig5 = px.bar(
                top, x='Sales',
                y='Product Name',
                orientation='h',
                title='Top 10 Products',
                template=PT,
                color='Sales',
                color_continuous_scale='Plasma'
            )
            st.plotly_chart(
                styled_fig(fig5),
                use_container_width=True
            )

        # Custom chart builder
        st.divider()
        c1, c2 = st.columns([1, 8])
        with c1:
            st.image(STAR_URL, width=40)
        with c2:
            st.subheader("Custom Chart Builder")

        col1, col2, col3 = st.columns(3)
        with col1:
            x_col = st.selectbox(
                "X axis", df.columns.tolist()
            )
        with col2:
            y_col = st.selectbox("Y axis", num_cols)
        with col3:
            chart_type = st.selectbox(
                "Type",
                ["Bar", "Line", "Scatter", "Pie"]
            )

        if st.button("📊 Generate Chart"):
            try:
                if chart_type == "Bar":
                    fig = px.bar(
                        df, x=x_col, y=y_col,
                        template=PT,
                        color_discrete_sequence=
                        ['#00d2ff']
                    )
                elif chart_type == "Line":
                    fig = px.line(
                        df, x=x_col, y=y_col,
                        template=PT
                    )
                elif chart_type == "Scatter":
                    fig = px.scatter(
                        df, x=x_col, y=y_col,
                        template=PT,
                        color_discrete_sequence=
                        ['#7b2ff7']
                    )
                elif chart_type == "Pie":
                    fig = px.pie(
                        df, names=x_col,
                        values=y_col,
                        template=PT
                    )
                st.plotly_chart(
                    styled_fig(fig),
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Try different columns!")

# =============================================
# AI PREDICTIONS PAGE
# =============================================

elif page == "🤖 AI Predictions":

    col1, col2 = st.columns([1, 8])
    with col1:
        st.image(PREDICT_URL, width=50)
    with col2:
        st.header("AI Sales Predictions")

    if 'df' not in st.session_state:
        st.warning("⚠️ Upload a file first!")
    else:
        df = st.session_state['df']
        model, features = load_model()

        if model is None:
            st.error("❌ Run model.py first!")
        else:
            # Model cards
            c1, c2, c3 = st.columns(3)
            cards = [
                (ROBOT_URL, "Random Forest",
                 "ML Algorithm", "#00ff88", "#1e3a1e",
                 "#3a6a3a"),
                (CHART_URL, f"{len(features)} Features",
                 "Input Variables", "#00d2ff", "#1e1e3a",
                 "#3a3a6a"),
                (SHIELD_URL, "Model Ready",
                 "Trained & Saved", "#ff6b6b", "#3a1e1e",
                 "#6a3a3a"),
            ]
            for col, (img, val, lbl, clr, bg, bd) in \
                    zip([c1, c2, c3], cards):
                with col:
                    ci, ct = st.columns([1, 2])
                    with ci:
                        st.image(img, width=50)
                    with ct:
                        st.markdown(f"""
                        <div style='background:
                        linear-gradient(135deg,{bg},{bg});
                        border:1px solid {bd};
                        border-radius:12px;
                        padding:12px'>
                            <div style='color:{clr};
                            font-weight:700'>{val}</div>
                            <div style='color:#808080;
                            font-size:12px'>{lbl}</div>
                        </div>
                        """, unsafe_allow_html=True)

            st.divider()
            st.subheader("🔮 Make a Prediction")

            input_values = {}
            cols = st.columns(3)
            for i, feat in enumerate(features[:6]):
                with cols[i % 3]:
                    try:
                        if feat in df.columns:
                            mn = float(df[feat].min())
                            mx = float(df[feat].max())
                            av = float(df[feat].mean())
                        else:
                            mn, mx, av = 0.0, 1000.0, 100.0
                        input_values[feat] = \
                            st.number_input(
                                f"{feat}",
                                min_value=mn,
                                max_value=mx,
                                value=av
                            )
                    except:
                        input_values[feat] = 0.0

            if st.button(
                "🔮 Predict Sales Now!",
                type="primary"
            ):
                try:
                    inp = pd.DataFrame([input_values])
                    for c in features:
                        if c not in inp.columns:
                            inp[c] = 0
                    inp = inp[features]
                    pred = model.predict(inp)[0]

                    st.markdown(f"""
                    <div style='background:linear-gradient(
                    135deg,rgba(0,255,136,0.1),
                    rgba(0,210,255,0.05));
                    border:2px solid rgba(0,255,136,0.4);
                    border-radius:24px; padding:30px;
                    text-align:center; margin:20px 0'>
                        <div style='color:#80c080;
                        font-size:12px; letter-spacing:3px'>
                        🤖 AI PREDICTION</div>
                        <div style='font-size:52px;
                        font-weight:900; color:#00ff88;
                        margin:10px 0'>${pred:,.2f}</div>
                        <div style='color:#508050;
                        font-size:13px'>
                        Predicted Sales Amount</div>
                    </div>
                    """, unsafe_allow_html=True)

                    mx_s = float(safe_max(df, 'Sales'))
                    if mx_s == 0:
                        mx_s = 5000.0

                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=pred,
                        title={
                            'text': "Sales Meter",
                            'font': {'color': '#e0e0ff'}
                        },
                        number={
                            'font': {'color': '#00ff88'},
                            'prefix': '$'
                        },
                        gauge={
                            'axis': {
                                'range': [0, mx_s],
                                'tickcolor': '#606080'
                            },
                            'bar': {'color': "#00ff88"},
                            'bgcolor': 'rgba(30,30,60,0.8)',
                            'bordercolor': '#3a3a6a',
                            'steps': [
                                {'range': [0, mx_s*0.33],
                                 'color': 'rgba(255,50,50,0.2)'},
                                {'range': [mx_s*0.33, mx_s*0.66],
                                 'color': 'rgba(255,200,0,0.2)'},
                                {'range': [mx_s*0.66, mx_s],
                                 'color': 'rgba(0,255,136,0.2)'}
                            ]
                        }
                    ))
                    fig.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        font_color='#e0e0ff',
                        height=350
                    )
                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )
                except Exception as e:
                    st.error(f"Error: {e}")

# =============================================
# AI ASSISTANT PAGE
# =============================================

elif page == "💬 AI Assistant":

    col1, col2 = st.columns([1, 8])
    with col1:
        st.image(CHAT_URL, width=50)
    with col2:
        st.header("AI Sales Assistant")

    st.markdown("""
    <div style='background:linear-gradient(
    135deg,rgba(123,47,247,0.08),
    rgba(0,210,255,0.05));
    border:1px solid rgba(123,47,247,0.3);
    border-radius:16px; padding:16px 24px;
    margin-bottom:24px'>
        <div style='display:flex; align-items:center;
        gap:12px'>
            <div style='font-size:28px'>🤖</div>
            <div>
                <div style='color:#e0e0ff; font-weight:600'>
                AI Sales Analyst</div>
                <div style='color:#8080b0; font-size:13px'>
                Powered by Llama 3.3 via Groq •
                Ask anything about your data</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if 'df' not in st.session_state:
        st.warning("⚠️ Upload a file first!")
    else:
        df = st.session_state['df']

        api_key = st.text_input(
            "🔑 Groq API Key:",
            type="password",
            help="Get free at console.groq.com"
        )

        if api_key:
            if 'messages' not in st.session_state:
                st.session_state['messages'] = []

            for msg in st.session_state['messages']:
                with st.chat_message(msg['role']):
                    st.markdown(msg['content'])

            user_input = st.chat_input(
                "💬 Ask about your sales data..."
            )

            if user_input:
                with st.chat_message("user"):
                    st.markdown(user_input)

                st.session_state['messages'].append({
                    "role": "user",
                    "content": user_input
                })

                try:
                    data_summary = get_data_summary(df)
                except:
                    data_summary = (
                        f"Data: {len(df)} rows, "
                        f"cols: "
                        f"{', '.join(df.columns.tolist())}"
                    )

                try:
                    from groq import Groq
                    client = Groq(api_key=api_key)
                    response = \
                        client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {
                                    "role": "system",
                                    "content": (
                                        "You are an expert "
                                        "sales data analyst. "
                                        "Give clear formatted "
                                        "answers with bullet "
                                        "points. Be concise "
                                        "and insightful."
                                    )
                                },
                                {
                                    "role": "user",
                                    "content": (
                                        f"Data:\n"
                                        f"{data_summary}\n\n"
                                        f"Q: {user_input}"
                                    )
                                }
                            ],
                            max_tokens=1024
                        )

                    ai_resp = (
                        response.choices[0].message.content
                    )

                    with st.chat_message("assistant"):
                        st.markdown(ai_resp)

                    st.session_state['messages'].append({
                        "role": "assistant",
                        "content": ai_resp
                    })

                except Exception as e:
                    st.error(f"API Error: {str(e)}")
                    st.info("Check your Groq API key!")

        else:
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image(ROBOT_URL, width=120)
            with c2:
                st.markdown("""
                <div style='background:rgba(30,30,60,0.8);
                border:1px solid rgba(100,100,200,0.2);
                border-radius:16px; padding:20px'>
                    <div style='color:#00d2ff;
                    font-weight:700; margin-bottom:12px'>
                    🔑 Get FREE Groq API Key</div>
                    <div style='color:#a0a0c0;
                    font-size:14px; line-height:2.2'>
                    1. Go to console.groq.com<br>
                    2. Sign up with Google<br>
                    3. Click API Keys<br>
                    4. Create → sales-project<br>
                    5. Copy & paste above ✅
                    </div>
                </div>
                """, unsafe_allow_html=True)