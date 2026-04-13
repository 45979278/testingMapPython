import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Bodyshop Map",
    layout="wide"
)

st.title("Bodyshop Map")
st.write("Top‑down")

bodyshop_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<style>
    body {
        margin: 0;
        background: #f4f4f4;
        font-family: Arial, sans-serif;
    }

    #map-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    svg {
        background: #ffffff;
        border: 2px solid #123456;
    }

    /* Roads / corridors */
    .road {
        fill: none;
        stroke: #669999;            /* Laguna Seca Blue */
        stroke-width: 6;
        stroke-linecap: round;
    }

    /* Labels */
    .label {
        font-size: 11px;
        font-weight: bold;
        fill: #4c6e91;              /* Arctic Race Blue */
        pointer-events: none;
    }

    /* Start & person */
    #person {
        fill: #008b8b;              /* Snapper Rocks Blue */
        stroke: #123456;
        stroke-width: 1.5;
    }

    .start-label {
        fill: #123456;
        font-size: 11px;
        font-weight: bold;
    }
</style>
</head>

<body>
<div id="map-container">

<svg id="map" width="900" height="800" viewBox="0 0 200 200">

    <!-- Warehouse boundary -->
    <rect x="0" y="0" width="200" height="200" fill="none"
          stroke="#123456" stroke-width="2"/>

    <!-- ================= METAL FINISH (PARALLEL HORIZONTAL ROADS) ================= -->

    <line class="road" x1="10" y1="40" x2="190" y2="40"/>
    <line class="road" x1="10" y1="55" x2="190" y2="55"/>

    <text class="label" x="12" y="35">Metal Finish</text>
    <text class="label" x="12" y="70">Metal Finish</text>

    <!-- ================= VERTICAL FRAMING SPINE ================= -->

    <line class="road" x1="160" y1="55" x2="160" y2="180"/>

    <!-- Framing sections (RIGHT SIDE) -->
    <text class="label" x="165" y="80">Framing 3</text>
    <text class="label" x="165" y="110">Framing 2</text>
    <text class="label" x="165" y="140">Framing 1</text>

    <!-- Sideframe sections (LEFT SIDE) -->
    <text class="label" x="110" y="80">Sideframe Outer</text>
    <text class="label" x="110" y="110">Sideframe Middle</text>
    <text class="label" x="110" y="140">Sideframe Inner</text>

    <!-- ================= START LINE ================= -->

    <line class="road" x1="10" y1="170" x2="160" y2="170"/>

    <text class="start-label" x="12" y="165">Start</text>

    <!-- You are here -->
    <circle id="person" cx="20" cy="170" r="4"/>
    <text class="label" x="26" y="172">You</text>

</svg>
</div>

<script>
const svg = document.getElementById("map");
const person = document.getElementById("person");

svg.addEventListener("click", function(e) {
    const rect = svg.getBoundingClientRect();
    const scaleX = 200 / rect.width;
    const scaleY = 200 / rect.height;

    const x = (e.clientX - rect.left) * scaleX;
    const y = (e.clientY - rect.top) * scaleY;

    person.setAttribute("cx", x);
    person.setAttribute("cy", y);
});
</script>

</body>
</html>
"""

html(bodyshop_html, height=900)

