# Mohrs Circle Stress Analysis Tool
### Live Demo:

👉 https://mohrs-circle-project.streamlit.app/

## 🔴 Problem
Mohr’s Circle is a core concept in Mechanics of Materials (or Engineering Mechanics II), but it’s often taught purely on paper.
That makes it difficult to build intuition around how stresses change with rotation and how normal and shear stresses relate geometrically.

As a student, I wanted a way to:

* Visualize Mohr’s Circle dynamically

* See how stress components change as the material is rotated

* Reinforce theory with an interactive, visual tool

Creating a tool like this strengthened my understanding behind the fundamental concepts of mechanics, and also helped me understand how crucial it is for measurements, values, etc.. to be accurate before an engineer takes action

## 🟢 Solution
I built an interactive Mohr’s Circle visualization tool that allows users to:

* Input normal stresses (σₓ, σᵧ) and shear stress (τₓᵧ)

* Automatically compute:

  * Principal stresses

  * Maximum shear stress

  * Average stress

* Rotate the stress element using a slider

* See real-time updates to:

  * σₓ′, σᵧ′, and τ′

  * The corresponding point and line on Mohr’s Circle

* Export the visualization as a PNG for reports or notes

This project prioritizes clarity, correctness, and interactivity rather than solving an industry-scale problem.

## 🛠 Tech Stack

* Python

* NumPy – numerical computations

* Matplotlib – Mohr’s Circle plotting

* Streamlit – interactive UI & deployment

* Streamlit Cloud – hosting and sharing

## 💥 Impact & Learning Outcomes

While this tool isn’t designed for production engineering use, it served as a foundational learning project that helped me:

* Apply engineering theory programmatically

* Work with scientific Python libraries

* Build stateful interactive applications

* Translate mathematical models into visual systems

* Understand how user input propagates through calculations and visualizations

This project laid the groundwork for future Python-based engineering and data projects.

## 🎥 Demo Preview

![MohrsCircle](https://github.com/user-attachments/assets/30b4f6ff-4ad4-4816-9f4d-18c78df31170)


## 🚀 Deployment

The app is deployed using Streamlit Cloud and runs entirely in the browser.
No local setup is required.

