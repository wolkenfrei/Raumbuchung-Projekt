#st.write ersetzt das print
#-->print schreibt ins Terminal - also für sich selber
#-->st.write schreibt in das gewünschte UI

#Start: 
# python -m venv .venv
# .venv\Scripts\activate
# streamlit run Raumbuchung.py

# Block 0 - Imports
import streamlit as st

# Block 1 - Titel und erste Anzeige (zeigt die Grundoberfläche der App)
st.title("Raumbuchung")
st.write("Das ist ein Raumbuchungssystem")