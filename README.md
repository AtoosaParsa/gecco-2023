# Universal Mechanical Polycomputation in Granular Matter

This repository contains the source code for all the experiments in the following paper:

[Parsa, A., Witthaus, S., Pashine, N., O'Hern, C. S., Kramer-Bottiglio, R., \& Bongard, J. (2023, July). Universal Mechanical Polycomputation in Granular Matter. In Proceedings of the Genetic and Evolutionary Computation Conference (pp. 193-201).](https://dl.acm.org/doi/abs/10.1145/3583131.3590520)

</br>

<p align="center">
  <img src="https://github.com/AtoosaParsa/gecco-2023/blob/main/overview.png"  width="700">
</p>

</br>
</br>

- [Watch a video summary here!](https://youtu.be/nL7L85-D9Uo)

- The paper is accepted at the <a href="https://gecco-2023.sigevo.org/HomePage"> Genetic and Evolutionary Computation Conference (GECCO 2023). </a>

- It is also accepted as a finalist for the <a href="https://www.human-competitive.org/awards"> Human-Competitive Awards (Humies 2023). </a>

</br>

## Experiments
### 1. Examination of the parameter space

- All the codes for sweeping the parameter space are in the `parameter sweep` folder. Run `plotAll.py` for Figure 3 of the paper.

### 2. Generalization
All the codes for the results in section 2.4 of the paper are in the `exp1 - single nand` folder.

- Run `evolveAfpo.py` to redo the experiments.
  
- Run `afpoPlots.py` and `plotInOut.py` for Figures 4, 5 and 6 of the paper.
 
- Code for the frequency sweep experiment from Figure 7 is in the `frequency sweep` folder.

### 3. Distributed computation 

- Run `plotHeatmap.py` from the `exp2 - heatmaps` folder to recreate the heatmap in Figure 8.

### 4. Polycomputation

Folder `exp3 -  polycomputation` contains all the codes from section 4 of the paper.

- Run `evolveAfpo.py` to redo the experiments.
  
- Run `afpoPlots.py` and `plotInOut.py` for Figures 9 and 10 of the paper.
  
- Folder `exp4 - heatmaps` contains codes to recreate Figure 11 showing the distribution of polycomputation.

### 5. Robustness analysis

- Run `robustness.py` to redo the experiment and `plotRobustness.py` to make Figure 12. 


## Notes about the code

- `evolveAfpo.py` launches an evolutionary algorithm (Age-Fitness Pareto Optimization) with two or three objectives. `constants.py` contains the algorithm's parameters such as population size and number of generations.
- `switch_float.py` is the main simulator file. It simulators the 2D granular material taking as input the stiffness matrix and some gate parameters such as the positions of the ports, frequency of vibrations, and phase offset.


Bibtex
------------
<pre>
@article{parsa2023universal,
&ensp; &nbsp; &nbsp; title={Universal Mechanical Polycomputation in Granular Matter},
&ensp; &nbsp; &nbsp; author={Parsa, Atoosa and Witthaus, Sven and Pashine, Nidhi and O'Hern, Corey S and Kramer-Bottiglio, Rebecca and Bongard, Josh},
&ensp; &nbsp; &nbsp; journal={arXiv preprint arXiv:2305.17872},
&ensp; &nbsp; &nbsp; year={2023}
}
</pre>
