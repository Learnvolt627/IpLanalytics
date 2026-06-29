import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv("IPL_trimmed.csv")

st.set_page_config(page_title="IPL Dashboard" , layout="wide")
st.title("IPL Analytics Dashboard (2008-2025)")

#sidebar filter

df['season']=df['season'].astype(str)
df['season']=df['season'].str.extract(r'(\d{4})$')
df['season']=pd.to_numeric(df['season'], errors='coerce')
season=sorted(df['season'].dropna().unique())
selected_season=st.sidebar.selectbox("Selected Season",["All"]+ list(season))

if selected_season != "All":
    df=df[df['season']==selected_season]

col1,col2=st.columns(2)

#top run scorers
with col1:
    st.subheader("Top 10 Run Scorers")
    top_batters = df.groupby('batter')['runs_batter'].sum().nlargest(10).reset_index()
    fig1=px.bar(top_batters, x='runs_batter', y='batter', orientation='h',color='runs_batter', color_continuous_scale='Blues')
    st.plotly_chart(fig1,use_container_width=True)

#top wicket takers

with col2:
    st.subheader("Top 10 wicket takers")
    top_bowlers=df[df['striker_out']==True].groupby('bowler')['striker_out'].count().nlargest(10).reset_index()
    
    top_bowlers.columns=['bowler', 'wickets']
    fig2 =px.bar(top_bowlers, x='wickets', y='bowler', orientation='h',color='wickets', color_continuous_scale='Reds')
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 =st.columns(2)

#Team wins per seasons

with col3:
    st.subheader("Team wins by seasons")
    wins=df.drop_duplicates('match_id').groupby(['season','batting_team'])['match_won_by'].count().reset_index()
    fig3=px.bar(wins, x='season', y='match_won_by', color='batting_team')
    st.plotly_chart(fig3, use_container_width=True)


with col4:
    st.subheader("Toss Decision vs Match Outcome")
    toss= df.drop_duplicates('match_id').copy()
    toss['toss_winner_won_match']=toss['toss_winner']== toss['match_won_by']
    toss_summary= toss.groupby('toss_decision')['toss_winner_won_match'].value_counts().reset_index()
    fig4= px.bar(toss_summary, x='toss_decision', y='count', color='toss_winner_won_match',barmode='group', labels={'toss_winner_won_match': 'Toss Winner Won Match'})
    st.plotly_chart(fig4, use_container_width=True)

