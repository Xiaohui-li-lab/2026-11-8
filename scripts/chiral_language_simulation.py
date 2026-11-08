#!/usr/bin/env python3
"""
Standalone runner for CQL simulation.
Usage:
    python scripts/chiral_language_simulation.py --max_length 14 --n_samples 50000
"""

import argparse
import os
import sys
import matplotlib.pyplot as plt
import numpy as np

# Ensure src/ is on path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from chiral_language import simulate_ensemble, combinatorial_proof, chain_to_hexagram

def main():
    parser = argparse.ArgumentParser(description='Chiral Coarse-Quantum Language Simulation')
    parser.add_argument('--max_length', type=int, default=12, help='Maximum chain length')
    parser.add_argument('--n_samples', type=int, default=100_000, help='Samples per length')
    parser.add_argument('--block_size', type=int, default=2, help='Coarse-graining block size')
    parser.add_argument('--p_left', type=float, default=0.5, help='Probability of L monomer')
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    parser.add_argument('--outdir', type=str, default='figures', help='Output directory for figures')
    args = parser.parse_args()
    
    os.makedirs(args.outdir, exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    print("=" * 60)
    print("Chiral Coarse-Quantum Language (CQL) Simulation")
    print("Author: Xiaohui Li")
    print("=" * 60)
    
    df = simulate_ensemble(
        max_length=args.max_length,
        n_samples=args.n_samples,
        block_size=args.block_size,
        p_left=args.p_left,
        seed=args.seed
    )
    
    df.to_csv(f'data/cql_simulation_N{args.max_length}_M{args.n_samples}.csv', index=False)
    print(f"\nData saved to data/cql_simulation_N{args.max_length}_M{args.n_samples}.csv")
    
    # Demonstrate I Ching mapping
    print("\n--- I Ching / Hexagram Demo ---")
    rng = np.random.default_rng(args.seed)
    for _ in range(5):
        hex_chain = ''.join(rng.choice(['L', 'R'], size=6))
        print(chain_to_hexagram(hex_chain))
    
    # Plotting
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Vocabulary growth
    ax = axes[0, 0]
    ax.plot(df['N'], np.log2(df['max_possible_vocab']), 'k--', label='Theoretical max $2^N$')
    ax.plot(df['N'], np.log2(df['vocab_size']), 'bo-', label=f'Observed vocab (block={args.block_size})')
    ax.set_xlabel('Chain length N')
    ax.set_ylabel(r'$\log_2$ vocabulary size')
    ax.set_title('Exponential Growth of Chiral Vocabulary')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Entropy
    ax = axes[0, 1]
    ax.plot(df['N'], df['entropy_bits'], 'rs-', label='Shannon entropy H(W)')
    ax.plot(df['N'], df['N'], 'g--', label='Max entropy = N bits')
    ax.set_xlabel('Chain length N')
    ax.set_ylabel('Entropy (bits)')
    ax.set_title('Information Content of Coarse-Grained Tokens')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Parity decay
    ax = axes[1, 0]
    ax.plot(df['N'], df['mean_abs_parity'], 'm^-', label=r'Mean $|\tau|$')
    ax.plot(df['N'], 1 / df['N'], 'c--', label=r'$1/N$ reference')
    ax.set_xlabel('Chain length N')
    ax.set_ylabel('Mean absolute parity')
    ax.set_title('Chiral Parity Averaging in Long Chains')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Capacity ratio
    ax = axes[1, 1]
    ratio = df['vocab_size'] / df['max_possible_vocab']
    ax.bar(df['N'], ratio, color='teal', alpha=0.7)
    ax.set_xlabel('Chain length N')
    ax.set_ylabel('Observed vocab / max vocab')
    ax.set_title('Sampling Coverage of Chiral Configuration Space')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fig_path = os.path.join(args.outdir, f'cql_results_N{args.max_length}_M{args.n_samples}.png')
    plt.savefig(fig_path, dpi=300)
    print(f"Figure saved to {fig_path}")
    plt.show()

if __name__ == '__main__':
    main()
