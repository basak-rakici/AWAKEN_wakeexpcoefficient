# AWAKEN Wake Expansion Coefficient Study

This repository contains the code and data analysis for investigating wake expansion in wind farms using the AWAKEN (American WAKE ExperimeNt) dataset. The study focuses on understanding how atmospheric stability and turbulence intensity influence the wake expansion coefficient (k_w) and wind turbine power predictions.

## Overview

Wind turbine wakes significantly affect downstream turbine performance, wind farm power output, and turbine loading. Simplified engineering wake models, like the Jensen model, are widely used due to computational efficiency but often assume a constant wake expansion coefficient. This study evaluates how:

Turbulence intensity (TI)

Atmospheric boundary layer (ABL) stability

Farm-to-farm interactions

affect wake expansion and recovery at the King Plains and Armadillo Flats wind farms.

Three modeling cases were considered:

Conventional k_w – constant wake expansion coefficient (0.075)

TI-informed k_w – calculated as 0.41 × TI

Calibrated k_w – optimized using SCADA power data

The analysis is performed using FLORIS, leveraging LiDAR and SCADA data from AWAKEN to characterize inflow conditions, turbine power, and wake behavior.

## Repository Contents
Repository Structure

DataAnalysis.ipynb: Performs stability and TI checks, identifies time periods of interest, and analyzes inflow conditions.

WakeExpansionCoeff.ipynb: Implements wake expansion coefficient cases, calculates power errors and RMSE, and visualizes velocity fields and wake effects.

KingPlainsData/: Contains input data, including SCADA data for King Plains, turbine specifications for Armadillo Flats and King Plains wind farms, and sonic anemometer and LiDAR data for A1, A2, B, and E36 sites.

requirements.txt

## Key Findings

Stable ABL conditions lead to reduced wake recovery, making conventional k_w assumptions less accurate.

Unstable ABL promotes faster wake recovery; conventional k_w performs reasonably well.

Calibrated k_w provides the best match to SCADA data, highlighting the importance of site- and stability-dependent parameterization.

## Data Availability

All code and processed datasets used for this study are available in this repository: AWAKEN_wakeexpcoefficient

## References

Bodini, N., Abraham, A., Doubrawa, P., Letizia, S., Thedin, R., Agarwal, N., Carmo, B., Cheung, L., Corrêa Radünz, W., Gupta, A., Goldberger, L., Hamilton, N., Herges, T., Hirth, B., Iungo, G. V., Jordan, A., Kaul, C., Klein, P., Krishnamurthy, R., … Wharton, S. (2024). An international benchmark for wind plant wakes from the American WAKE ExperimeNt (AWAKEN). Journal of Physics: Conference Series, 2767(9), 092034. https://doi.org/10.1088/1742-6596/2767/9/092034
Puccioni, M., Iungo, G. V., Moss, C., Solari, M. S., Letizia, S., Bodini, N., & Moriarty, P. (2023). LiDAR Measurements to Investigate Farm-to-Farm Interactions at the AWAKEN Experiment. Journal of Physics: Conference Series, 2505(1), 012045. https://doi.org/10.1088/1742-6596/2505/1/012045
AWAKEN Consortium. (2023). AWAKEN benchmark dataset and documentation. Retrieved November 1, 2025, from https://awaken-benchmark.readthedocs.io/en/latest/
Peña, A., Réthoré, P.-E., & van der Laan, M. P. (2016). On the application of the Jensen wake model using a turbulence-dependent wake decay coefficient: The Sexbierum case. Wind Energy, 19(4), 763–776. https://doi.org/10.1002/we.1863
Göçmen, T., Laan, P. van der, Réthoré, P.-E., Diaz, A. P., Larsen, G. Chr., & Ott, S. (2016). Wind turbine wake models developed at the technical university of Denmark: A review. Renewable and Sustainable Energy Reviews, 60, 752–769. https://doi.org/10.1016/j.rser.2016.01.113
National Renewable Energy Laboratory. (n.d.). FLORIS wake models. https://nrel.github.io/floris/wake_models.html
C. M. St. Martin, J. K. Lundquist, A. Clifton, G. S. Poulos, and S. J. Schreck, “Wind turbine power production and annual energy production depend on atmospheric stability and turbulence,” Wind Energ. Sci., vol. 1, no. 2, pp. 221–236, Nov. 2016, doi: 10.5194/wes-1-221-2016.
Radünz, W., Carmo, B., Lundquist, J. K., Letizia, S., Abraham, A., Wise, A. S., Sanchez Gomez, M., Hamilton, N., Rai, R. K., & Peixoto, P. S. (2025). Influence of simple terrain on the spatial variability of a low-level jet and wind farm performance in the AWAKEN field campaign. Wind and the atmosphere/Atmospheric physics. https://doi.org/10.5194/wes-2024-166
