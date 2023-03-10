import streamlit as st
import pandas as pd
import numpy as np



def main():
    url ='http://raw.githubusercontent.com/Ahmedhassan676/positive_pump/main/slip.csv'
    df_slip = pd.read_csv(url)
    
    html_temp="""
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black"; text-align:center> RagaBOLLAAAAA test Wun </h2>
    </div>
    
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    s1 = st.selectbox('Single or double acting?',('Single Acting','Double Acting'), key = 'type')
    
    d = st.number_input('Insert piston/plunger diameter (mm)', key = 'd')
    rpm = st.number_input('Insert stroke speed (stroke/min)', key = 'rpm')
    num = st.selectbox('Insert  number of pistons/plungers',(1,2,3,4), key = 'number_pistons')
    st_len = st.number_input('Insert stroke length (mm)', key = 'st_len')
    vis = st.number_input('Insert fluid viscosity (C.st)', key = 'vis')
    if s1 == 'Single Acting':
        if st.button("Reveal pump capacity"):
                try:
                    A = np.pi*np.power(d,2)*0.25
                    Q = A*rpm*num*st_len*0.00000006    
                    slip=7.204*np.exp(0.0002*vis)
                    Q_corrected = Q*(1-slip*0.01)
                    st.success('Your pump capacity is {} m3/hr / ({} L/hr)'.format(round(Q_corrected,3),round(Q_corrected*1000,2)))
                except (ValueError, TypeError, UnboundLocalError): st.write('Please Check your dataset(s)')

    else: 
        d_r = st.number_input('Insert rod diameter (mm)', key = 'rod_diameter') 
        a = np.pi*np.power(d_r,2)*0.25
        try:
                    A = np.pi*np.power(d,2)*0.25
                    Q = (2*A-a)*rpm*num*st_len*0.00000006  
                    slip=7.204*np.exp(0.0002*vis)
                    Q_corrected = Q*(1-slip*0.01)
                    st.success('Your pump capacity is {} m3/hr / ({} L/hr)'.format(round(Q_corrected,3),round(Q_corrected*1000,2)))
        except (ValueError, TypeError, UnboundLocalError): st.write('Please Check your dataset(s)')


if __name__ == '__main__':
    main()
