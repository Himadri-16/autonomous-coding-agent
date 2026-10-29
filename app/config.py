"""Central settings. Limits live here so they are easy to find and tune."""
import os

from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "")  # chosen in Step 2

# --- Agent limits ---
MAX_ITERATIONS = 5  # max write -> run -> fix loops per task

# --- Sandbox limits (applied to the Docker container) ---
SANDBOX_TIMEOUT_SEC = 10  # kill the run after this many seconds
SANDBOX_MEMORY = "256m"  # RAM cap
SANDBOX_CPUS = 0.5  # CPU cap
SANDBOX_NETWORK = "none"  # no internet inside the sandbox
