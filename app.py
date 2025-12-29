import streamlit as st
import numpy as np
import io
from main import eqns, slider, o_plot

st.title("\tMy Stress-Analysis Tool!")
st.write("**Assumptions: _plane stress conditions, counterclockwise is positive, units of Pascals (MPa, GPa, etc..)_**")

# Initialize session state variables
if "theta_slider" not in st.session_state:
    st.session_state.theta_slider = 0.0

if "show_circle" not in st.session_state:
    st.session_state.show_circle = False

st.divider()

# Divide layout into columns
cols = st.columns([1, 1, 2])

# Input fields for stress values
with cols[0]:
    s_x = st.number_input(
        "Enter σₓ:",
        min_value=-1e15,
        max_value=1e15,
        value=0.0,
        step=2.0,
        help="Normal stress in the x-direction.",
    )

    s_y = st.number_input(
        "Enter σᵧ:",
        min_value=-1e15,
        max_value=1e15,
        value=0.0,
        step=2.0,
        help="Normal stress in the y-direction.",
    )

    t_xy = st.number_input(
        "Enter τₓᵧ:",
        min_value=-1e15,
        max_value=1e15,
        value=0.0,
        step=2.0,
        help="Shear stress in the xy-plane.",
    )

# Mohr's Circle Plot and Slider
with cols[2]:
    theta_p = np.degrees(0.5 * np.arctan2(2 * t_xy, s_x - s_y))

    if st.button(label="**Mohrs Circle**", use_container_width=True):
        st.session_state.show_circle = True

    if st.session_state.show_circle:
        st.session_state.theta_slider = np.radians(
            st.slider(
                "Angle (θ°), initially adjusted to principal angle:",
                min_value=0.0,
                max_value=180.0,
                value=abs(theta_p - 90),
                step=0.1,
            )
        )

        theta_slider = st.session_state.theta_slider

        r, s_avg, s_min, s_max, s_x, s_y, t_xy = eqns(s_x, s_y, t_xy)
        circle_x, circle_y, sx_prime, sy_prime, t_prime, theta_slider = slider(
            r, s_avg, theta_slider, s_x, s_y, t_xy
        )
        fig = o_plot(
            r, s_avg, s_max, s_min, s_x, s_y, t_xy, circle_x, circle_y, sx_prime, sy_prime, t_prime
        )

        st.pyplot(fig)

        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)

        st.download_button(
            label="Download Mohr's Circle as PNG",
            data=buf,
            file_name="mohrs_circle.png",
            mime="image/png",
        )

with cols[1]:
    theta_slider = st.session_state.theta_slider

    r, s_avg, s_min, s_max, s_x, s_y, t_xy = eqns(s_x, s_y, t_xy)
    circle_x, circle_y, sx_prime, sy_prime, t_prime, theta_slider = slider(
        r, s_avg, theta_slider, s_x, s_y, t_xy
    )

    st.text_input(
        "Max Stress",
        value=f"{s_max:.2f}",
        help="Stress is max and min when shear is 0",
        disabled=True,
    )

    st.text_input(
        "Min Stress",
        value=f"{s_min:.2f}",
        help="Stress is min when shear is 0",
        disabled=True,
    )

    st.text_input(
        "Max Shear Stress",
        value=f"{r:.2f}",
        help="Max shear stress is the radius of the Mohr's Circle",
        disabled=True,
    )

    st.text_input(
        "Shear (τ') at angle θ",
        value=f"{t_prime:.2f}",
        help="Shear when the principal angle is changed",
        disabled=True,
    )

    st.text_input(
        "Stress (σₓ') at angle θ",
        value=f"{sx_prime:.2f}",
        help="Stress in x when the principal angle is changed",
        disabled=True,
    )

    st.text_input(
        "Stress (σᵧ') at angle θ",
        value=f"{sy_prime:.2f}",
        help="Stress in y when the principal angle is changed",
        disabled=True,
    )
