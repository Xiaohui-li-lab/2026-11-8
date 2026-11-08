"""
Chiral Coarse-Quantum Language (CQL) Simulation Core
Author: Xiaohui Li
Email: danceluck@163.com
ORCID: 0009-0003-8233-7191
"""

import numpy as np
import pandas as pd
from collections import Counter
from typing import List, Tuple, Dict
import itertools

def generate_chiral_chain(length: int, p_left: float = 0.5, seed: int = None) -> str:
    """
    Generate a single chiral chain of L/R monomers.
    
    Parameters
    ----------
    length : int
        Number of monomers in the chain.
    p_left : float
        Probability of drawing L (left-handed). Default 0.5 for neutral generation.
    seed : int, optional
        Random seed for reproducibility.
    
    Returns
    -------
    str
        A string composed of 'L' and 'R'.
    """
    rng = np.random.default_rng(seed)
    return ''.join(rng.choice(['L', 'R'], size=length, p=[p_left, 1 - p_left]))

def coarse_grain(chain: str, block_size: int = 2) -> str:
    """
    Coarse-grain a chiral chain into symbols by non-overlapping blocks.
    
    Example
    -------
    'LLRRLL' with block_size=2 -> 'aa bb aa' if L='a', R='b'.
    
    Parameters
    ----------
    chain : str
        Input chiral chain of L/R.
    block_size : int
        Length of each coarse-graining block.
    
    Returns
    -------
    str
        Space-separated coarse-grained symbol sequence.
    """
    if len(chain) % block_size != 0:
        chain = chain[:len(chain) - (len(chain) % block_size)]
    
    symbol_map = {block: f"s{sum((c == 'R') * (2 ** i) for i, c in enumerate(block))}"
                  for block in itertools.product('LR', repeat=block_size)}
    
    blocks = [chain[i:i+block_size] for i in range(0, len(chain), block_size)]
    symbols = [symbol_map[tuple(block)] for block in blocks]
    return ' '.join(symbols)

def chain_to_hexagram(chain6: str, mapping: Dict[str, str] = None) -> str:
    """
    Map a 6-monomer chiral chain to an I Ching hexagram line pattern.
    L -> Yin (broken line, 0), R -> Yang (solid line, 1).
    """
    if len(chain6) != 6:
        raise ValueError("Hexagram chain must have length 6.")
    lines = ['Yin' if c == 'L' else 'Yang' for c in chain6]
    if mapping:
        return mapping.get(chain6, f"Custom:{''.join(lines)}")
    return f"Hexagram[{chain6}]: " + ' | '.join(lines)

def simulate_ensemble(max_length: int = 12,
                      n_samples: int = 100_000,
                      block_size: int = 2,
                      p_left: float = 0.5,
                      seed: int = 42) -> pd.DataFrame:
    """
    Simulate an ensemble of chiral chains and compute coarse-grained statistics.
    
    Parameters
    ----------
    max_length : int
        Maximum chain length.
    n_samples : int
        Number of random chains per length.
    block_size : int
        Block size for coarse-graining.
    p_left : float
        Probability of L monomer.
    seed : int
        Base random seed.
    
    Returns
    -------
    pd.DataFrame
        Columns: N, vocab_size, entropy_bits, mean_abs_parity, max_possible_vocab.
    """
    rng = np.random.default_rng(seed)
    records = []
    
    for N in range(1, max_length + 1):
        vocab = Counter()
        parities = []
        
        for j in range(n_samples):
            chain = ''.join(rng.choice(['L', 'R'], size=N, p=[p_left, 1 - p_left]))
            parity = (chain.count('L') - chain.count('R')) / N
            parities.append(abs(parity))
            
            cg = coarse_grain(chain, block_size)
            vocab[cg] += 1
        
        probs = np.array(list(vocab.values())) / n_samples
        entropy = -np.sum(probs * np.log2(probs))
        max_vocab = 2 ** N
        
        records.append({
            'N': N,
            'vocab_size': len(vocab),
            'entropy_bits': entropy,
            'mean_abs_parity': np.mean(parities),
            'max_possible_vocab': max_vocab,
            'block_size': block_size,
            'p_left': p_left
        })
        
        print(f"N={N:02d}: vocab={len(vocab):5d}, H={entropy:.3f} bits, <|τ|>={np.mean(parities):.3f}")
    
    return pd.DataFrame(records)

def combinatorial_proof(N: int) -> int:
    """
    Return 2^N, the number of distinct length-N chiral strings.
    """
    return 2 ** N

if __name__ == '__main__':
    df = simulate_ensemble(max_length=12, n_samples=10_000)
    print("\nFirst rows:")
    print(df.head())
