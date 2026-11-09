# Chiral Coarse-Quantum Language (CQL) Simulation

[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8233--7191-green)](https://orcid.org/0009-0003-8233-7191)

**Author**: Xiaohui Li (李小辉)  
**Affiliation**: Independent Researcher, Baoji, China  
**Email**: danceluck@163.com  
**Data & Code**: https://github.com/xiaohui-li-lab/2026-11-8/

This repository accompanies the paper:

> **Human Language as the Reason for Describing Microscopic Quanta and the Macroscopic Cosmos: A Chiral Coarse-Quantum Framework**

## Project Overview

The CQL hypothesis proposes that human language functions as a coarse-grained chiral quantum layer mediating between fine-grained quantum configurations and macroscopic cosmic order. This repository provides:

1. A combinatorial simulation of binary chiral chains (`L`/`R`).
2. Coarse-graining of chains into symbolic tokens.
3. Demonstration that a 6-monomer chain yields 2^6 = 64 configurations (I Ching hexagrams).
4. Analysis of vocabulary growth, Shannon entropy, and chiral parity.
5. Extensible scaffold for future semantic-network and cosmic-handedness benchmarks.

## Repository Structure




├── data/ # Generated simulation outputs (CSV) 
├── figures/ # Generated figures (PNG/PDF) 
├── notebooks/ # Jupyter notebooks for interactive exploration 
├── scripts/ # Command-line runnable scripts 
├── src/ # Reusable Python modules 
├── README.md # This file
└── requirements.txt # Python dependencies


Bash

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/xiaohui-li-lab/2026-11-8.git
cd 2026-11-8
2. Install dependencies
Bash
pip install -r requirements.txt
3. Run the command-line simulation
Bash
python scripts/chiral_language_simulation.py --max_length 14 --n_samples 50000
4. Run the Jupyter notebook
Bash
jupyter notebook notebooks/chiral_language_simulation.ipynb
Main Outputs
data/cql_simulation_N*.csv — Simulation statistics per chain length.
figures/cql_results_N*.png — Four-panel figure:
Exponential vocabulary growth.
Shannon entropy of coarse-grained tokens.
Mean absolute chiral parity.
Sampling coverage of configuration space.
Theoretical Background
A binary chiral alphabet {L, R} produces 2^N distinct length-N strings.
For N = 6, this yields 64 states, corresponding to the 64 hexagrams of the I Ching.
Coarse-graining maps micro-configurations to discrete lexical tokens, modeling how language encodes complex quantum states.
Future Benchmarks
This repository will be extended to include:

Semantic parity asymmetry in word-association networks (Small World of Words, ConceptNet).
Correlation between molecular parity-violating energy differences (PVEDs) and lexical valence.
Large-scale cosmic handedness analysis using galaxy-spin catalogues.
Citation
If you use this code, please cite:

Bibtex
@article{li2026cql,
  title={Human Language as the Reason for Describing Microscopic Quanta and the Macroscopic Cosmos: A Chiral Coarse-Quantum Framework},
  author={Li, Xiaohui},
  journal={arXiv preprint},
  year={2026}
}
License
This project is released under the MIT License.

Disclaimer
The CQL hypothesis is a speculative theoretical framework. The simulations provided here are proof-of-concept and do not constitute empirical proof. Predictions in the paper are offered as falsifiable targets for future research.

Yaml

---

## 如何将上述文件上传到 GitHub（详细步骤）

### 如果您已有 `xiaohui-li-lab` 仓库

```bash
# 1. 克隆仓库到本地
git clone https://github.com/xiaohui-li-lab/2026-11-8.git
cd xiaohui-li-lab

# 2. 创建目录结构
mkdir -p data figures notebooks scripts src

# 3. 把上面的文件分别保存为：
#    requirements.txt
#    README.md
#    src/chiral_language.py
#    scripts/chiral_language_simulation.py
#    notebooks/chiral_language_simulation.ipynb

# 4. 安装依赖并测试
pip install -r requirements.txt
python scripts/chiral_language_simulation.py

# 5. 提交并推送
git add .
git commit -m "Add CQL simulation code, notebooks, and documentation"
git push origin main


