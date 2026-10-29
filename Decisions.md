# Decisions

Every major choice, with what we rejected and why. New entries are added as we build.

---

## D1. Orchestration framework: LangGraph

**Chosen:** LangGraph.

**Why:** The agent is a loop with a condition (write, run, check, fix, repeat). LangGraph models this directly as a graph with shared state and conditional edges. The flow is easy to see, test and draw.

**Rejected:**
- *Plain Python while-loop:* works, but gives no clear structure, state handling or visual graph. Weaker as a portfolio piece for agentic roles.
- *LangChain classic agents (AgentExecutor / ReAct):* less control over the exact flow. LangChain now points people to LangGraph for agents.
- *CrewAI / AutoGen:* built for multi-agent teams. Our problem is one agent in one loop, so they add weight we do not need.

---

## D2. Sandbox method: Docker container

**Chosen:** Run each piece of generated code in a fresh Docker container with no network, a memory cap, a CPU cap, a timeout, and a non-root user.

**Why:** The code is written by an LLM, so we must treat it as untrusted. Docker gives real isolation and simple resource limits, and it is a common tool that employers know.

**Rejected:**
- *`exec()` / `eval()` in our own process:* the generated code could read our API key, delete files or crash the server. No isolation at all.
- *Plain `subprocess`:* separate process, but it still runs on our machine with our permissions, files and network.
- *E2B (hosted sandbox):* good option, but depends on an external service, account and usage limits. We want the project to run fully on a laptop.
- *gVisor / Firecracker:* stronger isolation, but too much setup for this project.

---

## D3. API layer: FastAPI

**Chosen:** FastAPI.

**Why:** Quick to build, automatic request validation, and automatic docs page at `/docs` for demos.

**Rejected:**
- *Flask:* fine, but no built-in validation or docs.
- *CLI only:* simpler, but an API is closer to how this would be used in a real product.

---

## D4. How we decide a task is solved

**Chosen:** The agent writes the code and its own tests. A task is "solved" when those tests pass in the sandbox. For the evaluation (Results in README), we will use our own separate tests that the agent never sees.

**Why:** Tests written by the agent can be wrong or too easy, so passing them alone is not proof. Separate hidden tests give an honest success rate.

**Rejected:**
- *User must supply tests for every task:* more reliable, but makes the agent less useful and harder to demo.
- *Judge by "code runs without error":* far too weak. Wrong code can still run.

---

## D5. Starting limits (to be tuned with real runs)

| Limit | Start value | Reason |
|---|---|---|
| Max iterations | 5 | Enough for most fixes. Stops endless loops and controls API cost. |
| Sandbox timeout | 10 s | Stops infinite loops in generated code. |
| Sandbox memory | 256 MB | Enough for small tasks. Limits damage from runaway code. |
| Sandbox CPU | 0.5 core | Keeps the host machine responsive. |
| Network | none | Generated code should never reach the internet. |

These are first guesses. We will change them only if real runs show a problem, and note the change here.

---

## D6. LLM provider and model

**Provider chosen:** Groq (fast inference, free tier is enough for development).

**Model:** To be decided in Step 2, after checking Groq's current model list.
