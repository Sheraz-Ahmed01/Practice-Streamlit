import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.cache_data.clear()
st.set_page_config(layout="wide")
st.title("cricket app")

df=pd.read_csv("new_data.csv")

# st.dataframe(df,hide_index=True)

select=option_menu(
    menu_title=None,
    options=["Home","Player analysis","Country Insights","Comparison","Data Explorer","About"],
    icons=["house","person","globe","bar-chart","table","line"],
    orientation="horizontal",
    )


# with st.sidebar:
#    st.title("Navigation")
#    select_page=st.radio(
#        label="Choose a Page",
#        options=["Home","Player analysis","Country Insights"]
#    )


##_____Home_____##

if select=="Home":
    st.title("Cricket Analysis Dashboard")

    col1,col2,col3,col4=st.columns(4)

    col1.metric("**Total Players**",df['player'].nunique(),border=True,delta="sum of players",delta_arrow="off",delta_color="red")

    col2.metric("**Total Runs**",f"{df['Runs'].sum():,}",border=True,delta="Sum of Total Runs",delta_arrow="off",delta_color="red")

    col3.metric("**Total Countries**",df['country'].nunique(),border=True,delta="Number of Distinct Countries",delta_arrow="off",delta_color="red")

    col4.metric("**Total Matches**",f"{df['matches'].sum():,}",border=True,delta="Number of Matches Played",delta_arrow="off",delta_color="red")

    st.table(df.sample(10),hide_index=True,border=True)

##_____Player analysis_____##

elif select=="Player analysis":
    st.title("Player analysis")

    player=st.selectbox(label="**Select Player**",options=df['player'].unique())

    pdata=df[df['player']==player]

    df2=pdata[['100','50','matches','Inns','high_score','avg','4s','6s']]

    st.dataframe(df2,hide_index=True,row_height=100)

    df3=df2.T.reset_index()

    fig=px.bar(df3,x="index",y=df3.columns[1])

    df_pie=pdata[['100','50','6s','4s']]
    pie1=df_pie.T.reset_index()

    fig_pie=px.pie(pie1,names="index",values=pie1.columns[1])

    col1,col2=st.columns(2)
    with col1:
        col1.plotly_chart(fig,use_container_width=True)
    with col2:
        col2.plotly_chart(fig_pie,use_container_width=True)

elif select=="Country Insights":
    st.title("Country Insights")

    scountry=st.selectbox(label="Select a Country",options=df['country'].unique())

    col1,col2,col3,col4=st.columns(4)

    cdata=df[df["country"]==scountry]

    players=cdata["player"].nunique()
    total_runs=cdata['Runs'].sum()
    total_matches=cdata['matches'].sum()
    total_innings=cdata['Inns'].sum()

    col1.metric(label="**Total Players**",value=players,border=True)
    col2.metric(label="**Total Runs**",value=total_runs,border=True)
    col3.metric(label="**Total Matches**",value=total_matches,border=True)
    col4.metric(label="**Total Innings**",value=total_innings,border=True)

    df2=cdata[['player','Runs']]
    df3=cdata[['player','Runs','matches','100','6s']]
    df4=['Runs','matches','100','6s']

    fig=px.pie(df2,names="player",values="Runs")

    selectc=st.selectbox(label="Select Parameter",options=df4)

    fig2=px.bar(df3,x="player",y=selectc,color="player")

    st.plotly_chart(fig2,use_container_width=True)
    st.plotly_chart(fig,use_container_width=True)

elif select=="Comparison":
    st.title("Comparitive analysis")

    player=st.multiselect(label="Select Players",options=df['player'],default=df['player'].head(3))

    compare=df[df['player'].isin(player)]

    fig=px.scatter(data_frame=compare,x="strike_rate",y="avg",size="Runs",color="country",hover_name="player")
    st.plotly_chart(fig,use_container_width=True)

elif select=="Data Explorer":
    st.title("Data Explorer")

    st.dataframe(df,hide_index=True)

elif select=="About":
    st.title("About the Author")

    st.info("About This Project")

    st.text("Project by: Sheraz Ahmed")

    url="https://www.linkedin.com/in/sheraz-ahmed01/"

    st.link_button(label="Linkedin",url=url,icon="🔗")
  












