import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="Data Portfolio Dashboard", layout="wide")

st.title("📊 Project 4: Interactive Data Dashboard")
st.markdown("---")

# --- CREATE THE TABS ---
tab1, tab2, tab3 = st.tabs(["💼 Job Market (SQL)", "🎮 Overwatch Insights", "📈 Personal ETL"])

# ==========================================
# TAB 1: JOB MARKET (SQL)
# ==========================================
with tab1:
    st.subheader("Market Analytics Pipeline")
    db_path = r'Z:\Python\project_3\jobs.db'
    
    try:
        conn = sqlite3.connect(db_path)
        query = """
        SELECT required_skill, AVG(salary) as avg_salary, COUNT(*) as job_count 
        FROM job_postings 
        GROUP BY required_skill
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        col1, col2 = st.columns(2)
        col1.metric("Total Jobs in DB", int(df['job_count'].sum()))
        highest_paid = df.sort_values(by='avg_salary', ascending=False).iloc[0]['required_skill']
        col2.metric("Top Earning Skill", highest_paid)
        
        fig = px.bar(df, x='required_skill', y='avg_salary', color='required_skill', title="Salary Breakdown")
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Database connection error: {e}")

# ==========================================
# TAB 2: OVERWATCH INSIGHTS
# ==========================================
with tab2:
    st.subheader("Gameplay Performance Matrix")
    st.markdown("### Focus: Target Character Performance (Anran)")
    
    # Placeholder for your Project 2 loop insights
    st.info("💡 Strategic Rule Engine: Logic flags a critical performance bottleneck when encountering high-mobility counters (Sombra). Recommendation profile: Initiate immediate character swap protocol.")
    
    # We can add a quick mock dataframe to show how data looks here
    mock_data = pd.DataFrame({
        'Matchup': ['Win-Rate (Standard)', 'Win-Rate (vs Sombra)'],
        'Percentage': [62, 38]
    })
    fig2 = px.pie(mock_data, values='Percentage', names='Matchup', color_discrete_sequence=['#2ecc71', '#e74c3c'])
    st.plotly_chart(fig2)

# ==========================================
# TAB 3: PERSONAL ETL
# ==========================================
with tab3:
    st.subheader("Automated Financial ETL Pipeline")
    st.write("This pipeline ingests raw banking CSV exports, drops unnecessary columns, fixes date schemas, and flags transaction anomalies.")
    st.success("Pipeline status: Operational (Awaiting DB migration)")