import streamlit as st

st.title("Methods 🛠️")

st.header("Study design")

st.markdown(
    """
    The data from ten patients enrolled in the clinical trial ACA NCT05097183 were used as the basis for this study. These patients presented with symptomatic severe aortic stenosis and underwent TAVI procedures between 2021 and 2023 at the Hospital Clínico Universitario de Valladolid. The primary reason for utilizing this database was that each patient underwent thoracic computed tomography (CT) scans both before and after the intervention. Patients with a horizontal aorta or severe aortic tortuosity were excluded from the study.
    """
)

st.header("Data acquisition")
st.markdown(
    """
    In the CT studies, a thoracic series with contrast was performed using three consecutive sections.
    """
)

st.header("Biomodel segmentation")
st.markdown(
    """
    To obtain the aortic biomodel, segmentation was performed on the CT image series using *3D Slicer* [^1]. Only the regions of the aortic root, the aortic arch along with the carotid and subclavian arteries were included. A Gaussian smoothing of **2mm** was applied to the outer surface to eliminate image noise. Subsequently, the segmented geometry was imported into Ansys Spaceclaim to position the virtual aortic valve model. The virtual aortic valve prosthesis was designed by reverse engineering based on the dimensions of the commercial prosthesis *ACCURATE neo™ M* by *Boston Scientific*. Different geometries were then created for each prosthesis placement height. The coronary arteries were used as a reference point when adjusting the neutral position of the prosthesis. The other cases are specified in the following table. The orientation of the prosthesis was adjusted to match the patient's original commissures.

    | Height     | Position |
    | ---------- | -------- |
    | Very low   | -10 mm   |
    | Low        | -5 mm    |
    | Neutral    | 0 mm     |
    | High       | 5 mm     |
    | Very high  | 10 mm    |
    """
)

st.header("Geometry discretization")
st.markdown(
    """
    The discretization of the fluid volume was performed using *Ansys Fluent Meshing*. The surface mesh consisted of hexagons. The geometry was modeled as a single fluid volume with velocity boundary conditions at the inlets (aortic root) and pressure boundary conditions at the outlets (subclavian arteries, carotid arteries, and descending aorta). A zero-velocity boundary condition was specified on the aortic walls. Additionally, three boundary layer cells were added to the walls with a transition ratio of 0.272 and a growth ratio of 1.2. The meshed volume consisted of polyhedrons with a growth ratio of 1.2 and a maximum cell length of 3.6 mm.
    """
)

st.header("Computational fluid dynamics simulation")
st.markdown(
    """
    The CFD simulations of the aortic biomodels for each patient were conducted using Ansys Fluent 2023R1. The **laminar** viscosity model was employed since the Reynolds number is below 2300. Additionally, a **steady-state** model of the systolic phase was selected because parameters of interest, such as velocity fields, pressures, and shear stresses, reach their peak during this cardiac cycle phase. Blood was characterized as an incompressible fluid with a constant density of 1060 kg/m³ and viscosity described by the Carreau model. The inlet boundary condition at the aortic root was set to a constant velocity profile of 0.5 m/s. The outlet boundary conditions were modeled as constant pressure profiles corresponding to the systolic phase.
    """
)
st.latex(
    r"Re = \frac{\rho v D}{\mu} = \frac{1060 \cdot 0.184 \cdot 0.02 }{0.0045} = 1040"
)

st.header("Data analysis")
st.markdown(
    """
    Data on velocities, pressures, and shear stresses were obtained from simulations for each patient. Averages and standard deviations were calculated for each prosthesis height group in order to construct a box plot.
    """
)
