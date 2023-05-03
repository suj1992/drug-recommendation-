import streamlit as st
import pickle
import pandas as pd


drug = pd.read_pickle('drug.pkl')

st.title('Drug Recommendation System')

pres_for = st.selectbox('Prescribe for', drug['Prescribed_for'].unique())



if st.button('Recommend Drugs'):
    result = []
    def recommend(Prescribed_for):
        x = list(
            drug[drug['Prescribed_for'] == pres_for].sort_values('popularity_score', ascending=False).head(10)[
                'drugName'].unique())
        for i in x:
            result.append(i)
    recommend('prescribe')
    st.subheader('Recommended Medicines are:')
    count = 0
    for i in result:
        X=i
        count = count+1
        st.text(str(count)+". "+str(X))
