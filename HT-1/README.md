# Hoja de Trabajo 1: Agents & Environments

## Summary

This assignment explores agent rationality, environment classification, and performance metric design — grounded in two real-world Guatemalan scenarios and a practical Python implementation.

- **Intelligent Traffic Metrics (Guatemala City)**: Designed two composite performance metrics for an AI-controlled traffic light system. Rather than naive approaches (car count, average speed), the analysis builds up iteratively to a **Fluidity Index (IDF)** for vehicular flow and a **Pedestrian Safety Index (ISP)** — each backed by formal cost functions. A conflict scenario (rainy payday weekend near a busy main road) demonstrates how optimizing IDF can push ISP into critical failure.

- **PEAS Analysis (Solar Panel Cleaning Robot, Zacapa)**: Full PEAS breakdown for an autonomous robot operating on rails in a desert solar farm. Performance indicators include cleaning quality ($\Delta P = P_{\text{post}} - P_{\text{pre}}$), cleaning time, water consumption, and panel throughput. Environment classification: **Partially Observable**, **Stochastic**, **Continuous**, **Benign**.

- **Autonomous Agent Concepts**: Discussion of perception, rationality, inference, state representation, and parameter adjustment — all framed around the solar robot scenario.

- **Simple Reflex Agent (Python)**: A temperature regulation agent that reads a simulated environment and applies condition-action rules to maintain the 18–25°C comfort range.

## Deliverables

| File | Description |
| :--- | :---------- |
| `Informe.pdf` | Full report: metric derivations with 6 formal equations, PEAS analysis, environment classification, and agent modeling. |
| `Informe.tex` | Original LaTeX source for the report. |
| `main.py` | Simple Reflex Agent: simulates 10 iterations of temperature regulation. |

## Agent Design (main.py)

Three classes/functions:

- **`Environment`**: Initializes temperature randomly in [10, 30]°C. `get_percept()` returns the current temperature; `update(action)` adjusts it by ±1 per step using Python 3.10+ `match/case`.
- **`Agent`**: Stateless reflex agent. `act(temp)` returns `"enfriar"` (cool) if temp > 25, `"calentar"` (heat) if temp < 18, or `"esperar"` (wait) otherwise.
- **`main()`**: Runs a 10-iteration loop, printing each step's initial temperature, action taken, and resulting temperature.

The agent has no memory — every decision is based solely on the current percept, making it a textbook Simple Reflex Agent. The contrast with the complex, partially observable systems analyzed in the report (traffic lights, desert robot) is intentional.

## Execution

Requires Python 3.10+ (uses `match/case` syntax).

```bash
python3 main.py
```
