# NASA FieldFarm : Harmonized 250 m Earth Observation Pipeline

Agro-ecological decision intelligence interface connecting multi-source satellite Earth Observation datasets with farm-level crop rotation planning and predictive crop modeling.

Harmonized onto a **Common 250 m Grid Canvas** (matching MODIS MOD13Q1 and ISRIC SoilGrids 2.0) with ground-truth validation against **DWD Climate Data Center (Cottbus Station, CC BY 4.0)**.

Designed in accordance with **Anti-Slop Craftsmanship Guidelines** and inspired by the technical card architecture of **AMX App** (`amxapp.com/#apps`).

---

## 12-Source Earth Observation Harmonization Matrix

| # | Source | Resolution & Temporal Scope | Used For | 250 m Resampling Method |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **NASA POWER** | ~50 km, Daily (1981–2026) | Frost, heat, FAO-56 reference ET, water balance, dry spells, heavy rain, trends | Bilinear / Topographic lapse-rate spline |
| **2** | **NASA SMAP L4** | 9 km, 3-hourly / Daily | Model input, root-zone soil moisture map and trend | Bilinear Interpolation |
| **3** | **NASA GPM IMERG** | ~11 km, Monthly | Model input, summer-rain map | Bilinear Interpolation |
| **4** | **NASA MODIS** | 250 m (NDVI), 500 m (ET), 1 km (LST) | Model target (crop greenness MOD13Q1), evaporative demand MOD16A2GF, LST MOD11A2 | Master 250 m Canvas Reference |
| **5** | **NASA ECOSTRESS** | 70 m (via AppEEARS) | Field-level summer water stress & Evaporative Stress Index (ESI) | Area-weighted spatial average |
| **6** | **NASA GRACE / GRACE-FO** | 0.5° JPL Mascons | Regional terrestrial water-storage trend | Bilinear Interpolation |
| **7** | **NASA GLDAS Noah 2.1** | 0.25°, 3-hourly temperature | Hot days, late frost, degree days (GDD) | Bilinear Interpolation |
| **8** | **NASA SRTM** | 30 m static topography | Slope %, aspect, terrain position index (TPI) | Zonal mean aggregation |
| **9** | **ESA Sentinel-2 L2A** | 10 m, 5-day revisit | Bare-soil duration months per field (BSI > 0.1) | Field zonal aggregation |
| **10** | **JRC EUCROPMAP** | 10 m pan-European (2018, 2022) | Training labels, multi-year crop rotation sequences | Spatial Mode (Majority class) |
| **11** | **ISRIC SoilGrids 2.0** | 250 m native grid | Sand %, clay %, organic carbon (SOC), pH, bulk density, AWC | Direct 1:1 Pixel Alignment |
| **12** | **DWD Climate Data Center** | Point Station (Cottbus ID 00880, CC BY 4.0) | Ground check of NASA POWER daily series | Point station quantile bias correction |

---

## Architecture Overview

1. **Harmonized 250 m Multi-Source Matrix**
   - 12 interactive remote sensing and station calibration tiles.
   - Dynamic DWD Ground Check validation banner with Pearson correlation, temperature bias adjustment, and precipitation agreement.
   - Common 250 m Grid Specification technical viewer.

2. **Problem Diagnosis Layer** (Farmer Crisis Diagnostics)
   - Volatile Weather: Heat waves and unpredictable monsoon timing (NASA POWER 2m Air Temp & GPM IMERG)
   - Vanishing Water: Groundwater and topsoil drying up (NASA SMAP L4 GWETTOP surface wetness & GRACE mascons)
   - Tired Soil: Monoculture nutrient mining and carbon depletion (MODIS NDVI vegetative cover & SoilGrids)

3. **Field Inputs & Localization**
   - Benchmark presets: **Cottbus Station (DWD Ground Check & Reference Station)**, Deccan Plateau, Punjab Plain, Gangetic Basin, Gujarat Coast.
   - Interactive Leaflet map with drag-to-locate and OpenStreetMap search.
   - Baseline crop selector, growing season selector, soil texture profile, and irrigation system.

4. **Rotation Strategy Analysis**
   - **Strategy A: Baseline Monocrop (Control Group)**: High ET demand, negative nitrogen balance, high vulnerability index.
   - **Strategy B: Drought-Resilient Rotation (Water-Optimization Path)**: Low crop water requirement (CWR < 400 mm), C4 photosynthetic cereal match (Sorghum / Pearl Millet) triggered when GWETTOP < 0.40.
   - **Strategy C: Legume Cover / Intercrop (Soil-Regeneration Path)**: Biological nitrogen fixation (BNF +40 to +80 kg N/ha), soil organic matter boost, continuous living green cover.

---

## Running the Application & Python Pipeline

### Web Application
Launch the local server:
```bash
python server.py
```
Then visit `http://localhost:8080`.

### Offline Python Pipeline & Model Training
Execute the standalone 12-source ingestion, ground-truthing, and machine learning pipeline:
```bash
python pipeline.py
```
This queries live NASA POWER daily records, synthesizes the 12 datasets, performs DWD Cottbus station validation, trains a Ridge spatio-temporal regressor for the MODIS NDVI target, and saves the output to `telemetry_250m.json`.

---

## Anti-Slop Implementation Notes
- **Zero Em Dashes (R-02)**: Strict punctuation hygiene using colons, commas, and parentheses.
- **Card Architecture (AMX style)**: Top hairline accent gradient, subtle radial ambient glow on hover, squircle icon badges, monospace spec footers.
- **Color Contrast (R-25)**: All text meets or exceeds WCAG AA (4.5:1 for body text, >16:1 for headings).
- **Accessibility (R-32, R-39)**: Keyboard navigable, skip link, accessible dialog focus trapping, Escape key listener, visible `focus-visible` indicators.
- **Complete UI States (R-27)**: Loading state, Empty state, and Error state with cause and recovery actions.
- **Light & Dark Theme (R-21, R-34)**: Fully functional, high-contrast theme toggle persisted across sessions.
