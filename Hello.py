
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set the title and sidebar layout of the app
st.set_page_config(page_title="Streamlit Matplotlib App", layout="wide")

# Define the available operations
operations = ['Line Plot', 'Bar Plot', 'Scatter Plot', 'Histogram', 'Pie Chart']

# Display a selectbox to choose the operation
operation = st.sidebar.selectbox("Select an Operation", operations)

# Perform the selected operation
if operation == 'Line Plot':
    st.header("Line Plot")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    st.pyplot()

elif operation == 'Bar Plot':
    st.header("Bar Plot")
    x = ['A', 'B', 'C', 'D', 'E']
    y = [10, 7, 5, 8, 12]
    plt.bar(x, y)
    st.pyplot()

elif operation == 'Scatter Plot':
    st.header("Scatter Plot")
    x = np.random.randn(100)
    y = np.random.randn(100)
    plt.scatter(x, y)
    st.pyplot()

elif operation == 'Histogram':
    st.header("Histogram")
    data = np.random.randn(1000)
    plt.hist(data, bins=30)
    st.pyplot()

elif operation == 'Pie Chart':
    st.header("Pie Chart")
    labels = ['A', 'B', 'C', 'D', 'E']
    sizes = [15, 30, 45, 10, 5]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot()
