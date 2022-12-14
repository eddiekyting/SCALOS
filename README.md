# <img src= "doc/picture/UW-S-20D_silhouette_top.png" height="60"></img>Supersonic Configuration At Low Speeds (SCALOS)
[![Python Package using Conda](https://github.com/eddiekyting/SCALOS/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/eddiekyting/SCALOS/actions/workflows/python-package-conda.yml)  [![Jekyll site CI](https://github.com/eddiekyting/SCALOS/actions/workflows/jekyll-docker.yml/badge.svg)](https://github.com/eddiekyting/SCALOS/actions/workflows/jekyll-docker.yml)  <br />
This is a class project for CSE 583 at UW but will eventually be puslished for public use. 
The goal of the project is to take the standard corrected Kirsten Wind Tunnel data for post process and data visualizatoin. 
This project is by Kuang-Ying"Eddie" Ting, Xiaohai"Bob" Hu, and Yiju Hu. 

## Project Background 
Most of the supersonic commercial aircraft designs investigated to date have been optimized at cruise conditions and the designs often neglect the low-speed impact on their takeoff, approach, and landing characteristics. 
The goal of the SCALOS proejct is to study on how the shapes and configurations of long-range commercial supersonic aircraft affect the handling qualities, dynamic, stability, and control at low speeds. 
Such configuration can become quite nonlinear aerodynamically at relatively low angles of attack. 
In the design of such aircraft it is important to investigate this nonlinear behavior from a flight safety perspective. 
Numerous wind tunnel tests and CFD simulations have been used to date and more are planned. 
Methods of active control of such configuration, using a variety of control surfaces, canards, and engine control techniques, are being developed and evaluated. Reference papers are linked below. 

<img src= "doc/picture/DSS_all.png" ></img> 

<img src= "doc/picture/Polar.png"></img> 

## Project Ojective 
This project aims to analyze the experimental wind tunnel data for design space and trade-off study of supersonic airliner/ business jet at low speeds. 
The goal of this class project is to extract the commercial wind tunnel standard corrected data for look-up/search, process, and visualization. 
The future direction for this repository includes custom wind tunnel data corrections, model regressions, data reduction, and dynamic data augmentation. 
The detailed project proposal could be found [here](doc/CSE583_ProjectProposal.pdf).

### Target Users
The target users are researches, engineers, and student who are interested in aerodynammic configuration of supersonic configuration desgin at low speeds. 
The detailed target audiences description and user senario are [here](doc/Design.md).


### Package Capabilities
The package incldues the following capabilities. 

    1. Search/Look up
    2. Data Process 
        i. Data Extract
        ii. Data Interpolation and Derivative
    3. Data visulization 

The choice of packages selections are decided in early phase of project during technology review which is documented [here](doc/CSE583_TechnologyReview.pdf).
The following section briefly explains the fucntions purpose and outputs but reader should refer to `doc/README.md` for detail [doucmentation](doc/README.md).

A tutorial example is in `/scalos/sandbox/example` which is [here](/scalos/sandbox/example.ipynb) 

### Search / Lookup 
This function allows user to input and look up configurations in the run logs and return test entires and run numbers correspoding to the inputs. 

The name convetion is 
    
    F + A + W + N + V + H + C

where F is forebody fuselage; A is aft-body fuselage; W is outboard wing; N is nacelle; V is vertical tail; H is horizontal tail; and lastly, C is carnad. 
The modulated wind tunnel model components are tabualted below. 
    
    Designation     Description
    F15             2015 forward body
    F15.L           2015 forward body extended version 
    A15             2015 afterward body (low-mount only) 
    A20             2020 afterward body (Mid- and T-tail capability)  
    W15             2015 outboard wing 
    W17             2017 outboard wing 
    W20             2020 outboard wing  
    W20.OG          2020 outboard wing with OGEE leading edge
    W20.ALT         2020 outboard wing with alternate leading edge
    LEXX            XX$^\circ$ simple hing LE deflection (delta crank preserved) 
    N20.B           2020 bottom mounted nacelles
    N20.T           2020 top mounted nacelles
    V15             2015 vertical tail 
    V20             2020 vertical tail  
    VF1             Ventral fin
    DF1             Dorsal fin 
    H15             2015 horizontal stabilizer (low-mount only)
    H15.A           2015 RUAV horizontal stabilizer (low-mount only) 
    H20.L           2020 low mounted horizontal stabilizer 
    H20.M           2020 cruciform horizontal stabilizer 
    H20.T           2020 top mounted horizontal stabilizer 
    C15.F           2015 forward positioned canard
    C15.M           2015 mid positioned canard
    C15.A           2015 afterward positioned canard
    C18.F           2018 forward positioned canard
    C18.M           2018 mid positioned canard
    C18.A           2018 afterward positioned canard
    A.U             Aileron spoilers (roll-control speed brakes) 
    SSD             Spoiler-slot deflector
    FS              Mid-chord spoilers
    CS              Clam shell speed brakes
    FTDXD           Forward trip dots (10 inch behind nose trip ring) 

### Data Extract 
The data extract function allows user to input test entires and run number from search and look up and extract corresponding sub data set in data frame. 

### Data Process 
The data process clean up the data for alignment, trucntion and intperolation. This function allows two different set of data with different length and with respect to different location to be manipulated for data process, i.e., subtraction, addition, derivatives, etc. 
The derivative function computes the data derivaties with respect to longitudinal or lateral direction. 

### Visualization 
The visulization allows user to visual the data and compare different set of data. 

## Repository Structure 
The data structure of this project 

    .
    ????????? LICENSE
    ????????? README.md
    ????????? data
    ??????? ????????? data.csv
    ??????? ????????? finaldata_uw2298.csv
    ??????? ????????? finaldata_uw2320.csv
    ??????? ????????? finaldata_uw2326.csv
    ??????? ????????? finaldata_uw2331.csv
    ??????? ????????? runlogs
    ???????     ????????? autosort_runlog2298.xlsx
    ???????     ????????? autosort_runlog2320.xlsx
    ???????     ????????? autosort_runlog2326.xlsx
    ???????     ????????? autosort_runlog2331.xlsx
    ???????     ????????? runlogs.csv
    ????????? doc
    ??????? ????????? CSE583_ProjectProposal.pdf
    ??????? ????????? CSE583_TechnologyReview.pdf
    ??????? ????????? Design.md
    |   ????????? README.md
    ??????? ????????? picture
    ???????     ????????? UW-S-20B_silhouette_left.png
    ???????     ????????? UW-S-20D_silhouette_top.png
    ????????? environment.yml
    ????????? scalos
        ????????? __init__.py
        ????????? sandbox
        ??????? ????????? chart1.html
        ??????? ????????? chart_run2298.html
        ??????? ????????? script_development.ipynb
        ??????? ????????? script_test.ipynb
        ??????? ????????? unit_test.ipynb
        ????????? src
        ??????? ????????? __init__.py
        ??????? ????????? data_plot.py
        ??????? ????????? data_prep.py
        ??????? ????????? data_process.py
        ??????? ????????? runlog_search.py
        ??????? ????????? user_input.py
        ????????? tests
            ????????? __init__.py
            ????????? test_data_cleanup.py
            ????????? test_data_extract.py
            ????????? test_data_interp_der.py
            ????????? test_data_plt.py
            ????????? test_runlog_cleanup.py
            ????????? test_runlog_search.py
        
The `data` and its subfolder `runlogs` directories include experimental run logs and data sets from the KWT data (more data will be uploaded). 
The data here is standard KWT corrected data without any custom corrections.
The final data will be re-processed with final SCALOS-specific tare, intereferene and wall effects corrections. 
The absolute levels of some paramters are expected to shift slightly, but this is note expected to  impact the comparative results and increments.
The `ref` directory contains all the published literatures related to SCALOS's work at the University of Washington. 
The `scalos` directory includes `src`, `tests`, and `sandbox` subfolders for modules, tests, and examples, respectively. 
The `src` folder has modules of `search`, `data_prep`, `data_process`, and `data_plot` with corresponding unittests in `tests` folder.  
The `sandbox` folder provides examples in Jupyter notebooks for new users. 
The `doc` directory archieves all the documentation regarding this project.  



## Installation
[1] Install the latest version of Anaconda for your system from [here](https://docs.anaconda.com/anaconda/install/). Please make sure to **install the Python 3.9 version**. The dependencies should also work for other Python versions. Project aim to support Linux and MacOS, so make sure you have access to a machine with either of these operating systems.

[2] Execute the following steps to setup the repository and install the required dependencies.
```
conda create -n scalos python=3.9
git clone https://github.com/eddiekyting/SCALOS.git
cd SCALOS
conda env update -n scalos -f environment.yml
conda activate scalos
```
[3] Now head over to SCALOS directory



## Run log and Data 
There are several entries for the KWT. Each entries contains a run log and a data set. Run log contains detailed information on the run corresponding to the data file which contains data points. The detailed inforamtion on the run log and data are described in subsection. 

    Year   Month  Entry    Run   Data Collection 
    2020   Jul    uw2292   152   Force, moment, and flow visualziation 
    2020   Aug    uw2295    23   Force and moment
    2020   Sep    uw2298   133   Force and moment
    2021   Jun    uw2320   148   Force and moment
    2021   Aug    uw2324    54   Flow visualziation 
    2021   Sep    uw2326   255   Force and moment
    2021   Nov    uw2331   150   Force, moment, and flow visualziation

### Run log 
    Each 
    1.  RUN NO:         Run number for specific entry 
    2.  WT.\nTARE\nRUN: Wind off for weight tare
    3.  CONFIGURATION:  Tested model configuration specification 
                        (wing, fuselage, nacelle, vertical tail, horizontal tail, canard)                  
    5.  TYPE OF RUN:    Pitch run (P) or yaw run (Y)
    4.  a:              Pich angle (deg) = angle of attack 
    5.  Y:              Yaw angle (deg)
    6.  qnom (psi):     Nominal dynamic pressure 
    7.  FLAP L/R:       Wing flap deflection of left/right
    8.  AIL L/R:        Wing aileron deflection of left/right
    9.  STAB:           All moving horizontal tail deflection
    10. RUD:            Veritcal tail deflection 
    11. CAN:            Canard deflection 
    12. LE IB/OB:       Leading edge deflection of inboard/outboard
    13. TRIP DEF:       Turbulence trip dot definition 
    14. DATE:           Test date
### Data 
 
    1.  RUN:            Run number for given entry 
    2.  TEST:           Entry number
    3.  TP:             Test points collected                   
    4.  ALPHAC (deg):   Pich angle (deg) = angle of attack 
    5.  BETA (deg):     Sideslip angle (deg) = - Yaw angle (PSI)
    6.  PSI (deg):      Yaw angle (deg) = - Sideslip angle (BETA)
    7.  QC (psi):       Corrected dynamic pressure 
    8.  RE_MAC:         Reynold numbers (RE) with repect to test letter mean aerodynamic chord (MAC)
    9.  TEMPTS (F):     Tempearture during tests
    10. CL:             Nondimensional lift coeffeicetint, CL = L/(1/2 rho v^2 S), with respect to test letter specification 
    11. CD:             Nondimensional drag coeffeicetint, CD = D/(1/2 rho v^2 S), with respect to test letter specification 
    12. CY:             Nondimensional side force coeffeicetint, CY = Y/(1/2 rho v^2 S), with respect to test letter specification  
    13. CM:             Nondimensional pitch moment coeffeicetint, CM = M/(1/2 rho v^2 S c), with respect to test letter specification 
    14. CR:             Nondimensional roll moment coeffeicetint, CR = R/(1/2 rho v^2 S b), with respect to test letter specification 
    15. CN:             Nondimensional yaw moment coeffeicetint, CN = N/(1/2 rho v^2 S b), with respect to test letter specification 
    16. WA:             Wind axis, number after axis specified the center of gravity location on percentage of the mean aerodynamic chord
    17. SA:             Stability axis, number after axis specified the center of gravity location on percentage of the mean aerodynamic chord
    18. BA:             Body axis, number after axis specified the center of gravity location on percentage of the mean aerodynamic chord
    19. LOD:            Lift over drag, Nondimensional lift coeffeicetint divided by nondimensional drag coeffeicetint. 


## Bug Report
If you would like to report a bug or issue , please submit a detailed report at [this link](https://github.com/eddiekyting/SCALOS/issues/new).


## Citing SCALOS

If you use SCALOS in your research or wish to refer to the dataset published, please use the following BibTeX entry.

```BibTeX
 @article{ting_mavriplis_soltani_nelson_livne_2022, 
 title=         {Supersonic configurations at low speeds (SCALOS): Model geometry and aerodynamic results}, 
 DOI=           {10.2514/6.2022-1800}, 
 journal=       {AIAA SCITECH 2022 Forum}, 
 author=        {Ting, Kuang-Ying and Mavriplis, Nicolas and Soltani, Reza and Nelson, Chester P. and Livne, Eli}, 
 year=          {2022}} 
```

## Acknowledgement 
Support by NASA, Award/Contract \#80NSSC19K1661, under the Commercial Supersonic Technology (CST) program, Supersonic Configurations at Low Speeds, with Sarah Langston as the NASA technical grant monitor is gratefully acknowledged. The authors would like to thank Peter Coen, Lori Ozoroski, Sriram Rallabhandi, Melissa Carter, and Sarah Langston from NASA for the opportunity to conduct this needed research for supersonic aircraft. The authors would also like to thank the staff and crew of the University of Washington???s Kirsten Wind Tunnel (KWT), the 2020-2022 UW senior capstone design project teams, Anwar Moustafa and Colton Hill from class 2021, and Josh Ignacio from class 2022 for their assistance and contributions.

The authors would also like to thank Dr. David Beck and Erin Wilson from University of Washington for their support, guidance, and feedback in the development of this package.

## References
1. Nelson, C. P., Ting, K.-Y., Mavriplis, N., Soltani, R., and Livne, E., ???Supersonic Configurations at LowSpeeds (SCALOS): Project Background and Progress atUniversity ofWashington,??? AIAA Scitech 2022 Forum, 2022, p. 1803. https://doi.org/10.2514/6.2022-1803.
2. Ting, K.-Y., Mavriplis, N., Soltani, R., Nelson, C., and Livne, E., ???Supersonic Configurations at Low Speeds (SCALOS): Model Geometry and Aerodynamic Results,??? AIAA Scitech 2022 Forum, 2022, p. 1800. https://doi.org/10.2514/6.2022-1800.
3. Mavriplis, N., Ting, K.-Y., Moustafa, A., Hill, C., Soltani, R., Nelson, C., and Livne, E., ???Supersonic Configurations at Low Speeds (SCALOS): Test / Simulation Correlation Studies,??? AIAA Scitech 2022 Forum, 2022, p. 1801. https://doi.org/10.2514/6.2022-1801.
4. Ting, K.-Y., Mavriplis, N., Soltani, R., Nelson, C. P., and Livne, E., ???Supersonic Configurations at Low Speeds (SCALOS): The Aerodynamic Effects of Control Surfaces,??? AIAA SciTech 2022 Forum, 2023. (Submitted on Dec 12, 2022).
5. Ting, K.-Y., Mavriplis, N., Soltani, R., Nelson, C. P., and Livne, E., ???Supersonic Configurations at Low Speeds (SCALOS): Longitudinal Aerodynamics: Configuration Variations and Control Surfaces Effects,??? AIAA SciTech 2022 Forum, 2023. (Submitted on Dec 12, 2022).
6. Mavriplis, N., Ting, K.-Y., Soltani, R., Nelson, C. P., and Livne, E., ???Supersonic Configurations at Low Speeds (SCALOS): CFD Aid Data Reduction,??? AIAA SciTech 2022 Forum, 2023. Abstract Accepted. (Submitted on Dec 12, 2022).
7. Nelson, C. P., Ting, K.-Y., Ignacio, J. Mavriplis, N., Soltani, R., and Livne, E., ???Supersonic Configurations at Low Speeds (SCALOS): Configuration Comparison of SCALOS to the Existing Designs,??? AIAA SciTech 2023 Forum, 2023. (Submitted on Dec 12, 2022).
