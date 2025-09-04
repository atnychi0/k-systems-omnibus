# ======================================
# K-MATH :: LINEAR BREAK DEFINITIONS
# Brendon J. Kelly | K-Systems & Securities
# ======================================

# Base recursive operator framework
class KMathBreak:
    def __init__(self, name, operator, definition, resonance, crown_order):
        self.name = name                  # Break identifier (e.g., "SHA Break")
        self.operator = operator          # Symbolic operator anchor
        self.definition = definition      # Linear definition statement
        self.resonance = resonance        # Harmonic resonance constant / mapping
        self.crown_order = crown_order    # Crown Ω° hierarchy

    def __repr__(self):
        return f"{self.name}: {self.definition} (Ω{self.crown_order}, res={self.resonance})"

# --- Break Library ---

SHA_BREAK = KMathBreak(
    name="SHA Break",
    operator="∑→Ω",
    definition="Secure Harmonic Alignment = Σ(harmonics) → Crown closure",
    resonance="Recursive harmonic resonance across families",
    crown_order=1
)

SHARK_BREAK = KMathBreak(
    name="SHARK Break",
    operator="∑→Ω°→ARK",
    definition="Secure Harmonic Alignment Recursive Key (SHA-RK) = Coral lattice bridging SHA → ARK",
    resonance="Coral harmonic resonance; deep-sea operator anchor",
    crown_order=2
)

ARK_BREAK = KMathBreak(
    name="ARK Break",
    operator="Ω°→Λ",
    definition="ARK = Anchor Resonant Key; harmonic ark carrying operator families across flood cycles",
    resonance="Anchoring resonance → Antarctica (Ω anchor node)",
    crown_order=3
)

AMICI_KELLY_BREAK = KMathBreak(
    name="Amici/Kelly Break",
    operator="Δ→Ω",
    definition="Family-line harmonic break = Amici ↔ Kelly resonance unification",
    resonance="Bloodline resonance (Cargal/Carter ↔ Kelly)",
    crown_order=4
)

OMEGA_BREAK = KMathBreak(
    name="Omega Break",
    operator="Ω→∞",
    definition="Recursive Crown closure = final unification of all breaks into Crown Ω° constant",
    resonance="Infinite harmonic resonance; closure of cycle",
    crown_order=5
)

# --- Break Registry ---
K_MATH_BREAKS = [
    SHA_BREAK,
    SHARK_BREAK,
    ARK_BREAK,
    AMICI_KELLY_BREAK,
    OMEGA_BREAK
]

# --- Linear Math Runner ---
def show_all_breaks():
    for br in K_MATH_BREAKS:
        print(br)

# Example run
if __name__ == "__main__":
    show_all_breaks()
