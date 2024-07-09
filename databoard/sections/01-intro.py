import streamlit as st

st.title("Taviloc")
st.markdown(
    """
    **Aortic valve prostheses** are becoming an increasingly popular option for patients with severe aortic stenosis and high surgical risk [1].
    
    The TAVI placement process is typically a **manual** task, which means no two prostheses are positioned exactly the same way.
    **Height** of placement is a crucial factor to consider due to its potential impact on the conduction system and, consequently, the rate of permanent pacemaker implantation post-procedure [2]. Nevertheless, the effect of TAVI height on hemodynamic flow has not yet been studied.
    
    Currently, the influence of **prosthesis alignment** is an increasingly studied factor. For example, the ACA clinical trial is examining how commissural alignment affects various clinical parameters [3]. This has also been studied through CFD simulations, though only with virtual geometries and always limited to the aortic root and ascending aorta [4].
    
    This article aims to examine the **impact** of TAVI placement height and alignment on hemodynamic flow.
    """
)

st.markdown(
    """
    > 1. Waksman R, Rogers T, Torguson R, Gordon P, Ehsan A, Wilson SR, Goncalves J, Levitt R, Hahn C, Parikh P, Bilfinger T, Butzel D, Buchanan S, Hanna N, Garrett R, Asch F, Weissman G, Ben-Dor I, Shults C, Bastian R, Craig PE, Garcia-Garcia HM, Kolm P, Zou Q, Satler LF, Corso PJ. Transcatheter Aortic Valve Replacement in Low-Risk Patients With Symptomatic Severe Aortic Stenosis. Journal of the American College of Cardiology. 2018;72:2095–105.
    > 2. Schwerg M, Fulde F, Dreger H, Poller WC, Stangl K, Laule M. Optimized Implantation Height of the Edwards SAPIEN 3 Valve to Minimize Pacemaker Implantation After TAVI. J Interv Cardiol. 2016;29:370–4.
    > 3. Redondo A, Valencia-Serrano F, Santos-Martínez S, Delgado-Arana JR, Barrero A, Serrador A, Gutiérrez H, Sánchez-Lite I, Sevilla T, Revilla A, Baladrón C, Kim W-K, Carrasco-Moraleja M, San Román JA, Amat-Santos IJ. Accurate commissural alignment during ACURATE neo TAVI procedure. Proof of concept. Rev Esp Cardiol (Engl Ed). 2022;75:203–12.
    > 4. Oks D, Houzeaux G, Vázquez M, Neidlin M, Samaniego C. Effect of TAVR commissural alignment on coronary flow: A fluid-structure interaction analysis. Computer Methods and Programs in Biomedicine. 2023;242:107818.
    """
)

# st.image("assets/aorta-low.png", caption="Velocity pathlines from the aorta.")
