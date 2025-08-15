# Import Dict and List from typing
from typing import Dict, List

# Type hint the roster of codenames and number of missions
roster: Dict[str, int] = {
  "Chuck": 37,
  "Devin": 2,
  "Steven": 4
}

# Unpack the values and add type hints for the new list
agents: List[str] = [
  f"Agent {agent}, {missions} missions" \
  for agent, missions in roster.items()
]