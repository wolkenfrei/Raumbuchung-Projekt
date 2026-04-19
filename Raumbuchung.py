# st.write ersetzt print
# -> print schreibt ins Terminal
# -> st.write zeigt etwas in der App an

# Start:
# python -m venv .venv
# .venv\Scripts\activate
# streamlit run Raumbuchung.py

# Block 0 - Imports
import streamlit as st  # Streamlit für die Web-App

# Block 1 - Titel und erste Anzeige
st.set_page_config(page_title="Wolkis Raumbuchungssystem")  # Name im Browser-Tab
st.title("Raumbuchung")  # Überschrift
st.write("Das ist ein Raumbuchungssystem")  # kurzer Beschreibungstext

# Block 2 - Daten
raeume = ["Raum A", "Raum B", "Raum C", "Raum D"]  # verfügbare Räume

# Plätze werden im session_state gespeichert, damit Buchungen erhalten bleiben
if "plaetze" not in st.session_state:
    st.session_state.plaetze = {
    "Raum A": {"Platz 1 (Fenster)":True, "Platz 2 (Fenster)":True, "Platz 3":True},
    "Raum B": {"Platz 1 (Fenster)":True, "Platz 2 (Fenster)":True, "Platz 3":True, "Platz 4":True},
    "Raum C": {"Platz 1 (Fenster)":True},
    "Raum D": {"Platz 1 (Fenster)":True, "Platz 2 (Fenster)":True, "Platz 3":True, "Platz 4":True}
} # alle Plätze starten als frei (True)

plaetze = st.session_state.plaetze  # aktuelle Daten holen

# Block 3 - Eingaben
ausgewaehlter_raum = st.selectbox("Bitte Raum auswählen:", raeume)  # Raum auswählen

# passende Plätze zum Raum holen (nur die Namen)
plaetze_im_raum = list(plaetze[ausgewaehlter_raum].keys())

ausgewaehlter_platz = st.selectbox(
    "Bitte Platz auswählen:", plaetze_im_raum
)  # Platz auswählen

# Block 4 - Logik
buchung = st.button("Buchen")  # Button für die Buchung

if buchung:
    # prüfen, ob der Platz noch frei ist
    if plaetze[ausgewaehlter_raum][ausgewaehlter_platz]:
        # Platz auf belegt setzen
        plaetze[ausgewaehlter_raum][ausgewaehlter_platz] = False

        st.success(f"""**Buchung erfolgreich:**
Raum: {ausgewaehlter_raum}
Platz: {ausgewaehlter_platz}""")
    else:
        # Platz war schon belegt
        st.error("Dieser Platz ist bereits belegt")

# Block 5 - Ausgabe
