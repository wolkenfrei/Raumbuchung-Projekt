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
st.set_page_config(page_title="Wolkis Raumbuchungssystem") # Tab Namen angepasst
st.title("Raumbuchung") # Titel der App
st.write("Das ist ein Raumbuchungssystem") # Beschreibung

# Block 2 - Daten
raeume = ["Raum A", "Raum B", "Raum C", "Raum D"] # Grundlage! Liste mit allen verfügbaren Räumen

plaetze = {
    "Raum A": ["Platz 1 (Fenster)", "Platz 2 (Fenster)", "Platz 3"],
    "Raum B": ["Platz 1 (Fenster)", "Platz 2 (Fenster)", "Platz 3", "Platz 4"],
    "Raum C": ["Platz 1 (Fenster)"],
    "Raum D": ["Platz 1 (Fenster)", "Platz 2 (Fenster)", "Platz 3", "Platz 4"]
} # Jedem Raum wird eine Liste von Plätzen zugeordnet (Dictionary)

# Block 3 - Eingaben
ausgewaehlter_raum = st.selectbox("Bitte Raum auswählen:", raeume) #Selectbox - Auswahl eines Raums aus der Liste. Ergebnis wird in de

# Block 5 - Ausgabe
st.write("Ausgewählter Raum:", ausgewaehlter_raum) # Ausgabe was ausgewählt worden ist.
