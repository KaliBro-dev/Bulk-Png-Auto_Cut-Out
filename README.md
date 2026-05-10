# 🪄 MarifClipper Studio — Pure JS Client-Side PNG Auto-Cut Tool

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Platform](https://img.shields.io/badge/platform-GitHub%20Pages-blue)
![Tech](https://img.shields.io/badge/tech-HTML5%20Canvas%20%7C%20Vanilla%20JS-indigo)
![License](https://img.shields.io/badge/license-MIT-green)

**Live Demo:** [View Live Studio on GitHub Pages/](https://kalibro-dev.github.io/Bulk-Png-Auto_Cut-Out/))

--

## 📌 Executive Summary & Operational Context

**MarifClipper Studio** is a highly interactive, lightweight, zero-dependency client-side application engineered to automate background removal and creative shape clipping for digital assets. 

Built originally to solve real-world operational bottlenecks in fast-paced graphic and print production environments (such as batch processing design assets at **Dar Al Maarif**), this tool strips away the complexity of heavyweight desktop software. Staff can instantly remove backgrounds via smart tolerance flood-matching or apply precise vector clipping masks in seconds.

### 🎯 Key Academic & Professional Evidence (UWL Portfolio Submission)
* **Real-World Problem Solving:** Demonstrates client-side automation that drastically reduces manual editing time.
* **Zero Backend Infrastructure:** Utilizes client-side browser capabilities entirely, making it 100% cost-free, secure (files never leave the user's device), and statically hostable.
* **Algorithmic Application:** Implements Euclidean distance calculations across RGBA pixel matrices directly within the HTML5 Canvas API.

---

## 🚀 Features

1. **Magic Auto-Cut (Flood Matching Engine)**
   * Reads raw pixel image data (`Uint8ClampedArray`).
   * Calculates Euclidean distance between the sampled background click and surrounding RGB channels.
   * Dynamically alters the Alpha channel (`A = 0`) based on strict/loose tolerance sliders.

2. **Creative Vector Masking**
   * Uses programmatic pathing to apply clean, non-destructive clipping masks.
   * Preset shapes include **Circle Badges**, **Rounded Boxes**, **Hexagons**, and **Promo Stars**.

3. **Secure Client-Side Execution**
   * High-speed `FileReader` API loading.
   * Full privacy: Images are processed entirely in the local browser memory; no data is sent to external APIs or servers.

``
