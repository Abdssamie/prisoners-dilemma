Prisoner's Dilemma Simulation in Python
This repository provides an implementation of the classic game theory scenario known as the Prisoner's Dilemma in Python. The simulation demonstrates how two players, each facing the decision to cooperate or defect, can achieve different outcomes based on their choices.

Features:
# Strategies for the Iterated Prisoner's Dilemma

A collection of strategies for the **Iterated Prisoner's Dilemma (IPD)** simulation, ranging from simple to complex decision-making algorithms.

---

## Strategies and Descriptions

| **Name**                     | **Abbreviation**   | **Description**                                                                                                                                                                |
|-------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unconditional Cooperator** | `Cu`              | Always cooperates.                                                                                                                                                            |
| **Unconditional Defector**   | `Du`              | Always defects.                                                                                                                                                               |
| **Random**                   | `Random`          | Cooperates with a 50% probability.                                                                                                                                             |
| **Probability p Cooperator** | `Cp`              | Cooperates with a fixed probability `p` (0 ≤ p ≤ 1).                                                                                                                          |
| **Tit for Tat**              | `TFT`             | Cooperates initially, then mimics the opponent's last move.                                                                                                                   |
| **Suspicious Tit for Tat**   | `STFT`            | Starts with defection, then mimics the opponent's last move.                                                                                                                  |
| **Generous Tit for Tat**     | `GTFT`            | Cooperates initially and after opponent cooperates. Post-defection, cooperates with a probability based on game payoffs (R, P, T, S).                                         |
| **Gradual Tit for Tat**      | `GrdTFT`          | Similar to TFT, but increases defection punishment and later apologizes with cooperation.                                                                                     |
| **Imperfect TFT**            | `ImpTFT`          | Mimics the opponent’s last move with high, but less than 100%, probability.                                                                                                   |
| **Tit for Two Tats**         | `TFTT`            | Defects only if the opponent defects twice consecutively.                                                                                                                     |
| **Two Tits for Tat**         | `TTFT`            | Defects twice after the opponent defects once.                                                                                                                                |
| **Omega Tit for Tat**        | `ΩTFT`            | Plays TFT unless "deadlock" or "randomness" thresholds are exceeded, switching to unconditional defection in the latter case.                                                 |
| **GRIM Trigger**             | `GRIM`            | Cooperates until the opponent defects once, then defects permanently.                                                                                                         |
| **Discriminating Altruist**  | `DA`              | Cooperates with those who have never defected against it. Otherwise, it refuses to engage.                                                                                    |
| **Pavlov**                   | `WSLS`            | Cooperates if both players’ last moves match; otherwise, defects.                                                                                                             |
| **Adaptive Pavlov**          | `APavlov`         | Uses TFT initially, then adjusts based on categorizing the opponent.                                                                                                          |
| **Reactive**                 | `R(y, p, q)`      | Cooperates with probability `y` initially, and adjusts probabilities (`p`, `q`) based on the opponent’s actions.                                                             |
| **Memory-One**               | `S(p, q, r, s)`   | Cooperates based on probabilities tied to previous round outcomes: (C, C), (C, D), (D, C), (D, D).                                                                            |
| **Zero Determinant (ZD)**    | `ZD`              | Memory-one strategies that enforce a linear relationship between the player's and opponent’s payoffs.                                                                         |
| **Equalizer**                | `SET-n`           | A ZD strategy that ensures the opponent's average payoff remains fixed at `n`.                                                                                               |
| **Extortionary**             | `Extort-n`        | A ZD strategy ensuring one gains more relative to the opponent’s payoff over punishment.                                                                                      |
| **Generous**                 | `Gen-n`           | A ZD strategy that sacrifices personal payoff to ensure the opponent’s average payoff remains above the reward level.                                                         |
| **Good**                     | `GOOD`            | Ensures mutual reward when used by both players, forming a Nash equilibrium. Any deviation harms both players' payoffs.                                                       |

---

## Key Terms

- **C**: Cooperation  
- **D**: Defection  
- **R, P, T, S**: Reward, Punishment, Temptation, and Sucker payoffs, respectively.  
- **Memory-One Strategies**: Use outcomes of the previous round to make decisions.  
- **Zero Determinant (ZD) Strategies**: Allow manipulation of long-term payoffs via fixed linear equations.

---

## Summary of Strategy Categories

1. **Unconditional Strategies**: Always cooperate or defect (e.g., `Cu`, `Du`).  
2. **Tit for Tat Variants**: Mimic opponent behavior with modifications (`TFT`, `STFT`, `GTFT`).  
3. **Probability-Based**: Use fixed or adjustable probabilities for cooperation (`Cp`, `R`, `S`).  
4. **Reactive Strategies**: Depend on opponent’s last action (`WSLS`, `GRIM`).  
5. **Advanced Memory-One**: Use history of payoffs for decision-making (`ZD`, `GOOD`, `Extort-n`).

This structured list provides a detailed yet summarized view of the strategies for easy understanding and reference.

Bash
git clone https://github.com/Abdessamie/Abdssamie/GameTheorySimulation.git
Use code with caution.

Install dependencies:

Bash
pip install -r requirements.txt
Use code with caution.

Run the simulation:

Bash
python simulate.py
Use code with caution.

Usage:
You can modify the strategies for both players and experiment with different parameters to observe how cooperation or defection unfolds in the Prisoner's Dilemma. The simulation is designed to be modular, making it easy to add new strategies or modify the payoff matrix.

Example Output:
The output of each round includes the players' decisions and their resulting payoffs. After multiple rounds, the simulation will output the cumulative scores and a final analysis of the strategy's effectiveness.

License:
This project is licensed under the MIT License - see the LICENSE file for details.
