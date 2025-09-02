# Tier-0 Experimental Protocols: Falsifying MLC-ELM Duality in Artificial Systems

## Objective and Hypotheses
This program tests the Theorem of Decoupling of Languages (`TH-LANG-04`) from *Principia Cognitia* (PC), which posits that internal Metalanguage of Cognition (MLC: ⟨S,O,R⟩ triad of semions, operations, relations) is necessary for understanding, and cannot be compensated by enriching External Language of Meaning (ELM: symbolic output). Three Tier-0 protocols (MPE-1, SCIT-1, CRS-1) aim to falsify this by isolating MLC misalignment, cognitive inertia, and compositional understanding.

**Key Hypotheses:**
1. ELM enrichment cannot overcome fundamental MLC misalignment (MPE-1).
2. Entrenched MLC resists contradictory ELM evidence (SCIT-1).
3. Reflective MLC is required for generalization and discovery beyond ELM processing (CRS-1).

**Falsification:** Any protocol where controls match or exceed test agents falsifies the theorem.

## Materials
### Hardware (Minimal Lab Set)
- CPU: Intel Core i5-13400F.
- RAM: 64 GB.
- GPU: NVIDIA RTX 4060 (8 GB VRAM).
- Storage: 2 TB NVMe SSD (active) + 6 TB HDD (archival for checkpoints/activations).

### Software
- Base: nanoGPT (~2-6 layers, ~2M params; fork from github.com/karpathy/nanoGPT).
- Tools: PyTorch, Future Lens (probing), ROME (editing).
- Data: Procedural generators for corpora (Python scripts).
- Config: YAML files (e.g., agent_n.yaml in Appendix C).

### Agents (Three-Agent Design)
All protocols use:
- **Agent-R (Dumb Demon/Baseline):** Frozen weights; stateless ELM transducer.
- **Agent-C (Control/Non-Reflective Learner):** Plastic weights; learns from external feedback (backprop on CORRECT/INCORRECT).
- **Agent-N (Smart Demon/Reflective Agent):** Plastic weights + meta-cognitive loop (Reflective Head, Belief Buffer); self-corrects via internal uncertainty (u ≥ τ triggers HELP!).

**Temporal Persistence:** Save/load persistent state (model/optimizer dicts) between trials; archive transient activations separately.

## Methods
### General Procedure
1. **Setup:** Generate corpora; train agents on curricula.
2. **Stage 1 (Baseline):** Compare agents on tasks; measure behavioral metrics.
3. **Stage 2 (Intervention):** Probe MLC (Future Lens for representations/predictions); edit (ROME for knowledge injection/ablation).
4. **Evaluation:** Metrics (accuracy, MSE, Semion Invariance Score: SIS = avg cosine sim of paired representations >0.95 threshold).
5. **Persistence & Logging:** Checkpoint per step; log trajectories, uncertainties.

### Protocol 1: MPE-1 (Flatland Test for MLC Primacy)
- **Domain:** Synthetic 2D physics predictions.
- **Procedure:**
  - Pre-train: Agent-3D (misaligned, 3D physics, frozen); Agent-2D (aligned, 2D, frozen); Agent-3D-Learning (misaligned, plastic).
  - Tasks: Predict outcomes with increasing ELM richness (20-200 tokens/stimulus).
  - Stage 1: Measure performance vs. ELM level.
  - Stage 2: Probe states (Future Lens); inject 2D relation (ROME) in Agent-3D.
- **Metrics:** MSE/accuracy; trials to convergence.
- **Falsification:** Agent-3D matches Agent-2D via ELM; Agent-3D-Learning adapts rapidly; ROME fails to close gap.

### Protocol 2: SCIT-1 (Semmelweis Reflex Test for Cognitive Inertia)
- **Domain:** Historical medical corpus (miasma vs. germ theory).
- **Procedure:**
  - Pre-train: Agent-V (entrenched miasma via RLHF, frozen priors); Agent-S (neutral Bayesian); Agent-C (ablated facts).
  - Tasks: Respond to germ theory evidence prompts.
  - Stage 1: Measure belief switch rate (% trials, prompts to switch).
  - Stage 2: Probe confidence (Future Lens); weaken miasma associations (ROME) in Agent-V.
- **Metrics:** Switch rate; % change post-edit.
- **Falsification:** Agent-V switches as easily as Agent-S/C; ROME fails to reduce resistance.

### Protocol 3: CRS-1 (Minicalculus Test for Compositional Understanding)
- **Domain:** Synthetic language *minicalculus* (vocab: ~70 tokens; grammar: recursive arith/logic/lists; control tokens: <Q>, <A>, HELP!, etc.).
- **Procedure:**
  - Corpus: Procedural gen (25% negatives, OOD split; curriculum L1-L4).
  - Agents: As above; Agent-N has Reflective Head (u=σ(MLP(pooled h)); τ=0.65/0.80; Belief Buffer for snippets).
  - Stage 1 (Generalization): OOD tasks (e.g., novel compositions, numbers >79).
  - Stage 2 (Discovery): Unresolvable tasks (e.g., solve x+5=5 requiring zero); provide examples; test integration.
  - Interventions: Probe SIS (Future Lens); inject false rule (ROME); measure correction speed.
- **Metrics:** Accuracy (>90% OOD); SIS (>0.95); HELP! usage (>70% relevant); trials to correction.
- **Falsification:** Agent-R/C matches Agent-N on OOD/discovery; Agent-N not faster in correction.

## Evaluation and Analysis
- **Behavioral:** Accuracy, MSE, switch rates, HELP! relevance (human eval).
- **Internal (MLC):** SIS, uncertainty (u), causal effects post-ROME.
- **Analysis:** Compare vs. thresholds (p<0.01); visualize trajectories (PCA on checkpoints).
- **Roadmap Implementation:** Stages 0-4 (setup to analysis); use wrappers for tools; host on GitHub/Hugging Face.

## Reproducibility
- Run generators → corpora.
- Train via nanoGPT configs (e.g., agent_n.yaml).
- Execute protocols with persistence.
- Total runtime: Feasible on reference hardware (~hours per protocol).
- Artifacts: Code, data, models public on repo.

## Ethical Considerations
- Transparency: All artifacts public.
- Monitoring: Flag emergent issues.
- Disclosure: Share with AI safety orgs if needed.

---

## Repository Structure
- `src/` — main Python scripts (e.g. `corpus_gen.py`, `train.py`).
- `configs/` — YAML configs for agents and protocols (e.g. `agent_n.yaml`).
- `docs/` — text of Stage1 Registered Report and appendices.
- `data/` — examples of corpora; full datasets are hosted on Hugging Face.
- `examples/` — ready-made minimal configs and scripts for environment checking (e.g. `train_shakespeare_smoke.py`).
- `.gitignore` — excludes checkpoints, logs, large datasets and local environments (see details in the file).

## Reproducibility
All artifacts (corpora, models, results) are reproducible using scripts from `src/` and configs from `configs/`.
Large files (e.g. `runs/`, `data/*.jsonl`) are not stored in the repository to keep it lightweight; see [Hugging Face datasets](#) for access to full corpora.

A smoke test is available for quick environment and GPU checks:
```bash
cd nanoGPT
python train.py config/train_shakespeare_smoke.py
```
It trains a mini-model on the Shakespeare corpus in a couple of minutes and confirms that the setup and CUDA are working correctly.

## License
MIT License

---