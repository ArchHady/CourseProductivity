import pandas as pd
import streamlit as st
import plotly.express as px 

st.set_page_config(layout= 'wide', page_title= 'Productivity Project')
df=pd.read_csv("Cleaned_df.csv",index_col=0)
html_title = """<h1 style="color:white;text-align:center;"> Garment Employees Productivity EDA Project </h1>"""
st.markdown(html_title, unsafe_allow_html=True)
st.image("https://www.activtrak.com/wp-content/uploads/2024/08/blog-header-how-to-measure-team-productivity-q3-24.jpg")
st.dataframe(df)
page = st.sidebar.radio('pages',['univariant', 'bivariant', 'multivariant'])
if page =='univariant':
    st.title('univariant')
    for col in df.columns:
        st.plotly_chart(px.histogram(data_frame=df,x=col,title=col))
elif page =='bivariant':
    st.title('bivariant')
    st.plotly_chart(px.scatter(data_frame=df, x="team", y="actual_productivity"))
    st.plotly_chart(px.box(data_frame=df, x="department", y="actual_productivity"))
    prod_per_month = df.groupby("month")["actual_productivity"].mean().sort_values(ascending = False).reset_index()
    st.plotly_chart(px.bar(data_frame=prod_per_month, x="month", y="actual_productivity"))
elif page =='multivariant':
    st.title('multivariant')
    prod_per_month_per_dep = df.groupby(["month",'department'])["actual_productivity"].mean().sort_values(ascending = False).reset_index()
    st.plotly_chart(px.bar(data_frame=prod_per_month_per_dep, x="department", y="actual_productivity",color="month", barmode="group", height = 500))

