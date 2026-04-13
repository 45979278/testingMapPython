import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Bodyshop Map",
    layout="wide"
)

st.title("Bodyshop Map")
st.write("Top‑down view")

warehouse_html = """
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
        border: 2px solid #333;
    }

    .zone {
        stroke: #333;
        stroke-width: 2;
        opacity: 0.85;
    }

    .receiving { fill: #81d4fa; }
    .storage   { fill: #c5e1a5; }
    .picking   { fill: #ffcc80; }
    .shipping  { fill: #ef9a9a; }

    .walkway {
        fill: #eeeeee;
        stroke: #999;
        stroke-dasharray: 6,6;
    }

    .label {
        font-size: 12px;
        font-weight: bold;
        pointer-events: none;
    }

    #person {
        fill: red;
        stroke: black;
        stroke-width: 1;
    }
</style>
</head>

<body>
<div id="map-container">

<svg id="warehouseMap" width="800" height="800" viewBox="0 0 200 200">

    <!-- Warehouse boundary -->
    <rect x="0" y="0" width="200" height="200"
          fill="none" stroke="black" stroke-width="2"/>

    <!-- Walkways -->
    <rect class="walkway" x="90" y="0" width="20" height="200"/>
    <rect class="walkway" x="0" y="95" width="200" height="20"/>

    <!-- Zones -->
    <rect class="zone receiving" x="0" y="0" width="80" height="80"/>
    <text class="label" x="10" y="20">Receiving</text>

    <rect class="zone storage" x="120" y="0" width="80" height="80"/>
    <text class="label" x="130" y="20">Storage</text>

    <rect class="zone picking" x="0" y="120" width="80" height="80"/>
    <text class="label" x="10" y="140">Picking</text>

    <rect class="zone shipping" x="120" y="120" width="80" height="80"/>
    <text class="label" x="130" y="140">Shipping</text>

    <!-- You are here -->
    <circle id="person" cx="100" cy="100" r="4"/>
    <text x="108" y="102" font-size="10">You</text>

</svg>
</div>

<script>
const svg = document.getElementById("warehouseMap");
const person = document.getElementById("person");

svg.addEventListener("click", function(event) {
    const rect = svg.getBoundingClientRect();
    const scaleX = 200 / rect.width;
    const scaleY = 200 / rect.height;

    const x = (event.clientX - rect.left) * scaleX;
    const y = (event.clientY - rect.top) * scaleY;

    person.setAttribute("cx", x);
    person.setAttribute("cy", y);
});
</script>

</body>
</html>
"""

html(warehouse_html, height=850)
