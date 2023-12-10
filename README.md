# This final project is built upon Dr. Wilbur's 2022 paratransit project presented at the ICCPS conference
nohup ../../../../../../../Applications/Julia-1.9.app/Contents/Resources/julia/bin/julia bin/sim_proc.jl > logs/simulation1.log & 

# Priority score calculation 
Using census data for income and vehicle ownership, a priority score is calculated for each census tract, heuristic_by_track.csv

# Priority score tagging
Each bus request is tagged with a priority score, based on what census tract its pick-up location falls under, data/CARTA/processed/para_transit_trips_2021.csv

# Incorperating priority score into Dr. Wilbur's MCTS routing algorithm

# iccps-2022-paratransit-public
Please follow the instructions below.

Setup data:
* data link: https://drive.google.com/file/d/1VgtalQ5nongWwxrrfeoC2_NMLyCvyglq/view?usp=sharing
* Unzip data directory and place at top level: paratransit-mdp/data.

Main simulation executable is bin/sim_proc.jl.

Data preparation is int dataprep/ directory. Summary of data preparation steps:
* dataprep/prepare_trips.ipynb: prepares trips for the simulations in data/CARTA/processed
* dataprep/chains.ipynb: prepares test set and generative demand model data in data/CARTA/processed
* dataprep/travel_time_matrix.ipynb: generates the travel time matrix in data/travel_time_matrix
* dataprep/travel_time_matrix_congestion.ipynb: creates the congested travel time matrix.
* dataprep/paper_figs.ipynb: formats results for latex to be presented in the paper.

paratransit-mdp/ICAPS directory contains the source code for the ICAPS baseline (DRLSA).
