# Universal Mechanical Polycomputation in Granular Matter
--------------------
This repository contains the source code for all the experiments in the paper

[Parsa, A., Witthaus, S., Pashine, N., O'Hern, C. S., Kramer-Bottiglio, R., \& Bongard, J. (2023, July). Universal Mechanical Polycomputation in Granular Matter. In Proceedings of the Genetic and Evolutionary Computation Conference, In press.](https://arxiv.org/abs/2305.17872)</br>

<p align="center">
  <img src="https://github.com/AtoosaParsa/gecco-2023/blob/main/overview.png"  width="1200">
</p>

The paper is accepted at the <a href="https://gecco-2023.sigevo.org/HomePage"> Genetic and Evolutionary Computation Conference (GECCO 2023). </a>


It was also accepted as a finalist at the <a href="https://www.human-competitive.org/awards"> Human-Competitive Awards (Humies 2023). </a>

## Experiments
### Examination of the parameter space

- All the codes for sweeping the parameter space are in the `parameter sweep` folder. Run `plotAll.py` for Figure 3 of the paper.

### Generalization
All the codes for the results in section 2.4 of the paper are in the `exp1 - single nand` folder.

- Run `evolveAfpo.py` to redo the experiments.
  
- Run `afpoPlots.py` and `plotInOut.py` for Figures 4, 5 and 6 of the paper.
 
- Code for the frequency sweep experiment from Figure 7 is in the `frequency sweep` folder.

### Distributed computation 

- Run `plotHeatmap.py` from the `exp2 - heatmaps` folder to recreate the heatmap in Figure 8.

### Polycomputation

Folder `exp3 -  polycomputation` contains all the codes from section 4 of the paper.

- Run `evolveAfpo.py` to redo the experiments.
  
- Run `afpoPlots.py` and `plotInOut.py` for Figures 9 and 10 of the paper.
  
- Folder `exp4 - heatmaps` contains codes to recreate Figure 11 showing the distribution of polycomputation.

### Robustness analysis

- Run `robustness.py` to redo the experiment and `plotRobustness.py` to make Figure 12. 




---

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
