#!/bin/bash
#**********************
# Description:
# Example batch script to be used as a template for running the ASPECT model.
# Modify as needed for your own individual ASPECT cases.
#
# Written 240717 for use on Oscar (RHEL9.2 | SLURM 23.11.1). 
# Author: Paul Hall (paul_hall@brown.edu)
#
#**********************
# SLURM JOB INFORMATION
#**********************
# Walltime requested for job (24 hrs)
#SBATCH --time=60:00:00

# Request use of 32 cores and 4GB of memory per core on 1 nodes (32 cores total)
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G

# Define Oscar partition to use
#SBATCH --partition=batch

# Job Name
#SBATCH -J ASPECT

# SLURM output (*.out) and error (*.err) file names
# Use '%x' for Job Name,'%A' for array-job ID, '%j' for job ID and '%a' for task ID`
#SBATCH -e %x-%j.err
#SBATCH -o %x-%j.out

#********************
# COMMANDS TO EXECUTE
#********************
# load required modules 
module purge
module load hpcx-mpi/4.1.5rc2s
module load openblas/0.3.23-u6k5fey
module load netlib-lapack/3.11.0-jdzmstx

# configure environment (set environment variables to point to dependencies)
source /oscar/data/deeps/shared/opt/aspect/depends/configuration/enable.sh 

# run ASPECT (note: change parameter-file.prm to whatever parameter file you are using
# for your case)
srun --mpi=pmix /oscar/data/deeps/shared/opt/aspect/aspect/build/aspect /users/hclau/TPW/param/param_2.0-1e23.dat
