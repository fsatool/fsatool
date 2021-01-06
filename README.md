# FSATOOL

A fast sampling and analysis tool for biomolecules

## Installation

- First compile the CUDA version of `pmemd`
- Path Amber source file `./configure patch`
- Install `make install`

## Usage

- Using the **FSATOOL** sampling module
  - The arguments `sim` has the same format as amber, for example

    ```sh
    ./fsatool sim -i sim.in -o sim.out -p prmtop -c sim.rst -r md.rst -o prod.mdcrd
    ```

- Extract the trajectory file based on each temperature

    ```sh
    ./fsatool extract -i extract.in
    ```

- Using the Markov State Model(MSM) module

    ```sh
    ./fsatool msm -i msm.in
    ```

  - Using the submodule of MSM, for example: `cluster`

    ```sh
    ./fsatool msm cluster -i cluster.in
    ```

## Uninstallation

- Clean the file `make clean`
- Unpatch the amber source file `./configure unpatch`

## Contributors
  - Zhang Haomiao
  - Zhang Haozhe
  - Shu Zirui
  - Liao Jun
