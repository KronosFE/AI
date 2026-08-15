# -*- coding: utf-8 -*-
"""Quantum logic gates — one robust page per gate (matrix, interactive circuit,
basis-state action, Qiskit code, plain-English mechanism). Data-driven."""

CAT = "quantum-gates"

# gate spec: key -> dict(title, slug, sym, lede, matrix(rows), action[(in,out)], mech, qiskit, tags, related)
SINGLE = {
 "identity-gate": dict(title="Identity Gate (I)", sym="I",
   lede="The identity gate leaves a qubit unchanged — the do-nothing operation and the algebraic anchor for every other gate.",
   matrix=[["1","0"],["0","1"]],
   action=[("|0⟩","|0⟩"),("|1⟩","|1⟩")],
   mech="I is the 2×2 identity matrix. It is Hermitian and unitary, its own inverse, and commutes with every gate. In practice it marks an idle time-step on a wire (where a real qubit still decoheres), so compilers track it for timing and error budgeting.",
   qiskit="from qiskit import QuantumCircuit\nqc = QuantumCircuit(1)\nqc.id(0)",
   tags=["single-qubit","Hermitian","Clifford"], related=[("pauli-x-gate","Pauli-X"),("quantum-gate-basics","Gate basics")]),
 "pauli-x-gate": dict(title="Pauli-X Gate (NOT)", sym="X",
   lede="The Pauli-X gate is the quantum NOT — it flips |0⟩ and |1⟩ and rotates the Bloch vector 180° about the x-axis.",
   matrix=[["0","1"],["1","0"]],
   action=[("|0⟩","|1⟩"),("|1⟩","|0⟩"),("|+⟩","|+⟩"),("|−⟩","−|−⟩")],
   mech="X is the bit-flip. On the Bloch sphere it is a π rotation about x. It is Hermitian (X=X†) and its own inverse (X²=I), and it is a member of the Clifford group. Together with Z it generates the bit/phase structure every error-correction code tracks.",
   qiskit="qc = QuantumCircuit(1)\nqc.x(0)   # |0> -> |1>",
   tags=["single-qubit","Pauli","Clifford","Hermitian"], related=[("pauli-y-gate","Pauli-Y"),("pauli-z-gate","Pauli-Z"),("cnot-gate","CNOT")]),
 "pauli-y-gate": dict(title="Pauli-Y Gate", sym="Y",
   lede="The Pauli-Y gate combines a bit flip and a phase flip — a 180° rotation of the Bloch vector about the y-axis.",
   matrix=[["0","−i"],["i","0"]],
   action=[("|0⟩","i|1⟩"),("|1⟩","−i|0⟩")],
   mech="Y = iXZ. It is Hermitian and unitary, a Pauli and a Clifford generator. On the Bloch sphere it is a π rotation about y, mapping the x-axis to −x and z to −z while leaving y fixed.",
   qiskit="qc = QuantumCircuit(1)\nqc.y(0)",
   tags=["single-qubit","Pauli","Clifford","Hermitian"], related=[("pauli-x-gate","Pauli-X"),("pauli-z-gate","Pauli-Z")]),
 "pauli-z-gate": dict(title="Pauli-Z Gate (Phase Flip)", sym="Z",
   lede="The Pauli-Z gate flips the phase of |1⟩ while leaving |0⟩ alone — a 180° rotation about the z-axis.",
   matrix=[["1","0"],["0","−1"]],
   action=[("|0⟩","|0⟩"),("|1⟩","−|1⟩"),("|+⟩","|−⟩"),("|−⟩","|+⟩")],
   mech="Z is the phase-flip. Diagonal in the computational basis, it does nothing you can measure directly on |0⟩/|1⟩ populations, but it swaps |+⟩ and |−⟩ — which is why phase errors are invisible without a basis change. Hermitian, Clifford, Z²=I.",
   qiskit="qc = QuantumCircuit(1)\nqc.z(0)",
   tags=["single-qubit","Pauli","Clifford","Hermitian"], related=[("s-gate","S gate"),("t-gate","T gate"),("hadamard-gate","Hadamard")]),
 "hadamard-gate": dict(title="Hadamard Gate (H)", sym="H",
   lede="The Hadamard gate creates superposition — it turns a definite |0⟩ or |1⟩ into an equal blend, and is the doorway to nearly every quantum algorithm.",
   matrix=[["1/√2","1/√2"],["1/√2","−1/√2"]],
   action=[("|0⟩","|+⟩ = (|0⟩+|1⟩)/√2"),("|1⟩","|−⟩ = (|0⟩−|1⟩)/√2"),("|+⟩","|0⟩"),("|−⟩","|1⟩")],
   mech="H maps the computational basis to the ± basis and back — it is its own inverse. Geometrically it is a 180° rotation about the diagonal (x+z)/√2 axis. A layer of H on every qubit builds the uniform superposition that Grover, Deutsch–Jozsa, and phase estimation all begin from.",
   qiskit="qc = QuantumCircuit(1)\nqc.h(0)   # |0> -> (|0>+|1>)/sqrt(2)",
   tags=["single-qubit","Clifford","Hermitian","superposition"], related=[("pauli-z-gate","Pauli-Z"),("quantum-superposition","Superposition"),("grovers-algorithm","Grover")]),
 "s-gate": dict(title="S Gate (Phase, √Z)", sym="S",
   lede="The S gate is a quarter-turn phase gate — the square root of Z — adding a 90° phase to |1⟩.",
   matrix=[["1","0"],["0","i"]],
   action=[("|0⟩","|0⟩"),("|1⟩","i|1⟩"),("|+⟩","|+i⟩")],
   mech="S = √Z applies a π/2 phase. It is Clifford but not Hermitian (S† = S³). With H and CNOT it generates the whole Clifford group — the classically simulable backbone that error correction is built on.",
   qiskit="qc = QuantumCircuit(1)\nqc.s(0)    # phase +pi/2\nqc.sdg(0)  # S-dagger",
   tags=["single-qubit","Clifford","phase"], related=[("pauli-z-gate","Pauli-Z"),("t-gate","T gate")]),
 "t-gate": dict(title="T Gate (π/8, ⁴√Z)", sym="T",
   lede="The T gate is the non-Clifford π/8 gate — the ingredient that lifts a quantum computer from classically simulable to universal.",
   matrix=[["1","0"],["0","e^{iπ/4}"]],
   action=[("|0⟩","|0⟩"),("|1⟩","e^{iπ/4}|1⟩")],
   mech="T applies a π/4 phase (T²=S, T⁴=Z). It is the canonical non-Clifford gate: Clifford+T is universal, and by the Gottesman–Knill theorem Clifford-only circuits are classically efficient, so T-count is the standard measure of a fault-tolerant algorithm's cost.",
   qiskit="qc = QuantumCircuit(1)\nqc.t(0)\nqc.tdg(0)  # T-dagger",
   tags=["single-qubit","non-Clifford","universal","phase"], related=[("s-gate","S gate"),("magic-state-distillation","Magic states"),("clifford-t-universality","Clifford+T")]),
 "rx-gate": dict(title="Rx(θ) Rotation Gate", sym="Rx",
   lede="Rx(θ) rotates a qubit by an arbitrary angle θ about the x-axis — a continuous, parametric bit-axis rotation.",
   matrix=[["cos(θ/2)","−i·sin(θ/2)"],["−i·sin(θ/2)","cos(θ/2)"]],
   action=[("|0⟩","cos(θ/2)|0⟩ − i·sin(θ/2)|1⟩")],
   mech="Rx(θ)=exp(−iθX/2). At θ=π it is X (up to global phase). Parametric rotations Rx/Ry/Rz are the tunable knobs of variational circuits (VQE, QAOA) and of pulse-level calibration on real hardware.",
   qiskit="from numpy import pi\nqc = QuantumCircuit(1)\nqc.rx(pi/2, 0)",
   tags=["single-qubit","parametric","rotation"], related=[("ry-gate","Ry gate"),("rz-gate","Rz gate"),("variational-quantum-eigensolver","VQE")]),
 "ry-gate": dict(title="Ry(θ) Rotation Gate", sym="Ry",
   lede="Ry(θ) rotates a qubit about the y-axis by θ — the real-valued rotation that moves amplitude between |0⟩ and |1⟩ without adding a phase.",
   matrix=[["cos(θ/2)","−sin(θ/2)"],["sin(θ/2)","cos(θ/2)"]],
   action=[("|0⟩","cos(θ/2)|0⟩ + sin(θ/2)|1⟩")],
   mech="Ry(θ)=exp(−iθY/2) has purely real entries, so it prepares real superpositions with controllable amplitude — the workhorse of amplitude-encoding and of most variational ansätze.",
   qiskit="qc = QuantumCircuit(1)\nqc.ry(0.7, 0)",
   tags=["single-qubit","parametric","rotation"], related=[("rx-gate","Rx gate"),("rz-gate","Rz gate")]),
 "rz-gate": dict(title="Rz(θ) Rotation Gate", sym="Rz",
   lede="Rz(θ) rotates a qubit about the z-axis — a pure phase between |0⟩ and |1⟩, often free or nearly free on hardware.",
   matrix=[["e^{−iθ/2}","0"],["0","e^{iθ/2}"]],
   action=[("|0⟩","e^{−iθ/2}|0⟩"),("|1⟩","e^{iθ/2}|1⟩")],
   mech="Rz(θ)=exp(−iθZ/2). On many platforms z-rotations are 'virtual' — implemented by shifting the phase reference of later pulses — so they cost no time and no error, making Rz the cheapest parametric gate.",
   qiskit="qc = QuantumCircuit(1)\nqc.rz(0.5, 0)",
   tags=["single-qubit","parametric","rotation","virtual"], related=[("rx-gate","Rx gate"),("ry-gate","Ry gate"),("s-gate","S gate")]),
 "phase-gate": dict(title="Phase Gate P(φ)", sym="P",
   lede="The general phase gate P(φ) adds an arbitrary phase φ to |1⟩ — the parametric family that contains S (φ=π/2) and T (φ=π/4).",
   matrix=[["1","0"],["0","e^{iφ}"]],
   action=[("|0⟩","|0⟩"),("|1⟩","e^{iφ}|1⟩")],
   mech="P(φ) equals Rz(φ) up to a global phase. It is the diagonal building block of the quantum Fourier transform, where controlled-P gates apply the fractional phases that encode the transform.",
   qiskit="qc = QuantumCircuit(1)\nqc.p(0.3, 0)",
   tags=["single-qubit","parametric","phase"], related=[("s-gate","S gate"),("t-gate","T gate"),("quantum-fourier-transform","QFT")]),
 "sqrt-x-gate": dict(title="√X Gate (SX)", sym="√X",
   lede="The √X gate is the square root of NOT — apply it twice and you get a bit flip. It is a native gate on much of today's superconducting hardware.",
   matrix=[["(1+i)/2","(1−i)/2"],["(1−i)/2","(1+i)/2"]],
   action=[("|0⟩","half-flip toward |1⟩")],
   mech="SX = √X performs a π/2 rotation about x. Because it is a hardware-native basis gate on many superconducting processors, transpilers decompose arbitrary single-qubit gates into SX and Rz.",
   qiskit="qc = QuantumCircuit(1)\nqc.sx(0)",
   tags=["single-qubit","native","rotation"], related=[("pauli-x-gate","Pauli-X"),("rx-gate","Rx gate")]),
}

TWO = {
 "cnot-gate": dict(title="CNOT Gate (Controlled-X)", sym="X", qubits=2,
   lede="The CNOT flips the target qubit if the control is |1⟩ — the two-qubit gate that creates entanglement and anchors nearly every quantum circuit.",
   matrix=[["1","0","0","0"],["0","1","0","0"],["0","0","0","1"],["0","0","1","0"]],
   circ={"qubits":2,"cols":[[{"g":"X","c":0,"t":1}]]},
   action=[("|00⟩","|00⟩"),("|01⟩","|01⟩"),("|10⟩","|11⟩"),("|11⟩","|10⟩")],
   mech="CNOT (CX) is Clifford and, with H, turns a product state into a Bell state: H on the control then CNOT gives (|00⟩+|11⟩)/√2. With arbitrary single-qubit gates it is universal. It is the standard entangler and the syndrome-extraction workhorse of error correction.",
   qiskit="qc = QuantumCircuit(2)\nqc.h(0)\nqc.cx(0, 1)   # Bell state",
   tags=["two-qubit","Clifford","entangling"], related=[("pauli-x-gate","Pauli-X"),("cz-gate","CZ"),("bell-states","Bell states"),("toffoli-gate","Toffoli")]),
 "cz-gate": dict(title="CZ Gate (Controlled-Z)", sym="Z", qubits=2,
   lede="The CZ gate applies a phase flip to |11⟩ — a symmetric, entangling gate that is native to many hardware platforms.",
   matrix=[["1","0","0","0"],["0","1","0","0"],["0","0","1","0"],["0","0","0","−1"]],
   circ={"qubits":2,"cols":[[{"g":"Z","c":0,"t":1}]]},
   action=[("|00⟩","|00⟩"),("|01⟩","|01⟩"),("|10⟩","|10⟩"),("|11⟩","−|11⟩")],
   mech="CZ is symmetric in its two qubits and diagonal, so it commutes cleanly and maps to CNOT via a Hadamard on the target. It is the entangling gate of measurement-based (cluster-state) quantum computing and a common native two-qubit gate.",
   qiskit="qc = QuantumCircuit(2)\nqc.cz(0, 1)",
   tags=["two-qubit","Clifford","entangling","symmetric"], related=[("cnot-gate","CNOT"),("pauli-z-gate","Pauli-Z"),("cluster-states","Cluster states")]),
 "swap-gate": dict(title="SWAP Gate", sym="×", qubits=2,
   lede="The SWAP gate exchanges the states of two qubits — essential for routing information across hardware where qubits aren't all connected.",
   matrix=[["1","0","0","0"],["0","0","1","0"],["0","1","0","0"],["0","0","0","1"]],
   circ={"qubits":2,"cols":[[{"g":"×","c":0,"t":1}]]},
   action=[("|01⟩","|10⟩"),("|10⟩","|01⟩")],
   mech="SWAP = three CNOTs. On hardware with limited connectivity, chains of SWAPs move a logical qubit next to its partner before a two-qubit gate — the dominant overhead the transpiler tries to minimize.",
   qiskit="qc = QuantumCircuit(2)\nqc.swap(0, 1)",
   tags=["two-qubit","Clifford","routing"], related=[("cnot-gate","CNOT"),("iswap-gate","iSWAP"),("qubit-routing","Qubit routing")]),
 "iswap-gate": dict(title="iSWAP Gate", sym="iX", qubits=2,
   lede="The iSWAP swaps two qubits and adds an i phase — a natural entangling gate for superconducting and spin qubits.",
   matrix=[["1","0","0","0"],["0","0","i","0"],["0","i","0","0"],["0","0","0","1"]],
   circ={"qubits":2,"cols":[[{"g":"iX","c":0,"t":1}]]},
   action=[("|01⟩","i|10⟩"),("|10⟩","i|01⟩")],
   mech="iSWAP arises directly from the exchange (XX+YY) interaction that couples many physical qubits, so it is often the true native gate; √iSWAP plus single-qubit rotations is universal.",
   qiskit="qc = QuantumCircuit(2)\nqc.iswap(0, 1)",
   tags=["two-qubit","native","entangling"], related=[("swap-gate","SWAP"),("cnot-gate","CNOT")]),
 "toffoli-gate": dict(title="Toffoli Gate (CCX)", sym="X", qubits=3,
   lede="The Toffoli gate flips the target only when both controls are |1⟩ — a reversible AND, and a universal gate for classical logic on a quantum computer.",
   matrix=None,
   circ={"qubits":3,"cols":[[{"g":"X","c":0,"t":2}],[{"g":"X","c":1,"t":2}]]},
   action=[("|110⟩","|111⟩"),("|111⟩","|110⟩"),("|100⟩","|100⟩")],
   mech="CCX computes a reversible AND into the target, so it implements classical boolean logic reversibly and underlies quantum arithmetic (adders, modular multipliers in Shor). It decomposes into 6 CNOTs plus T gates — its T-count is a key fault-tolerance cost.",
   qiskit="qc = QuantumCircuit(3)\nqc.ccx(0, 1, 2)  # Toffoli",
   tags=["three-qubit","universal-classical","arithmetic"], related=[("cnot-gate","CNOT"),("fredkin-gate","Fredkin"),("shors-algorithm","Shor")]),
 "fredkin-gate": dict(title="Fredkin Gate (CSWAP)", sym="×", qubits=3,
   lede="The Fredkin gate is a controlled-SWAP — it exchanges two targets only when the control is |1⟩, a reversible, conservative logic primitive.",
   matrix=None,
   circ={"qubits":3,"cols":[[{"g":"×","c":0,"t":1}],[{"g":"×","c":0,"t":2}]]},
   action=[("|100⟩... controls swap of targets","conditional SWAP")],
   mech="CSWAP is universal for reversible classical computation and is the heart of the SWAP test — a routine that estimates the overlap ⟨ψ|φ⟩ between two quantum states, used across quantum machine learning.",
   qiskit="qc = QuantumCircuit(3)\nqc.cswap(0, 1, 2)  # Fredkin",
   tags=["three-qubit","reversible","swap-test"], related=[("toffoli-gate","Toffoli"),("swap-gate","SWAP"),("quantum-kernel-methods","Quantum kernels")]),
}

def _mk(slug, d, is_two=False):
    body=[]
    if d.get("matrix"):
        body.append(("h2","Matrix"))
        body.append(("matrix",("Unitary matrix", d["matrix"])))
    body.append(("h2","Circuit symbol"))
    if is_two and d.get("circ"):
        body.append(("circuit", d["circ"]))
    else:
        body.append(("circuit", {"qubits":1,"cols":[[{"g":d["sym"],"t":0}]]}))
    body.append(("h2","Action on basis states"))
    body.append(("truth",(["input","output"], d["action"])))
    body.append(("h2","How it works"))
    body.append(("p", d["mech"]))
    body.append(("h2","In code (Qiskit)"))
    body.append(("code",("python", d["qiskit"])))
    tags="".join(f'<span class="chip">{t}</span>' for t in d["tags"])
    body.append(("html", f'<div style="margin-top:14px">{tags}</div>'))
    return dict(slug=slug, title=d["title"], cat=CAT, lede=d["lede"], body=body,
                related=d["related"], seo_type="DefinedTerm")

def register(add, F):
    for slug,d in SINGLE.items(): add(_mk(slug,d,is_two=False))
    for slug,d in TWO.items():    add(_mk(slug,d,is_two=True))
    # a hub / basics page
    add(dict(slug="quantum-gate-basics", title="Quantum Logic Gates — How to Read Them", cat=CAT,
        lede="A one-page primer on reading quantum gates: unitaries, circuit symbols, the Bloch sphere, and why reversibility matters.",
        body=[("h2","A gate is a unitary matrix"),
              ("p","Every quantum gate on n qubits is a 2ⁿ×2ⁿ unitary matrix U with U†U = I. Unitarity guarantees the operation is reversible and preserves total probability — the defining constraint that separates quantum logic from classical, irreversible logic like AND and OR."),
              ("h2","Reading a circuit"),
              ("p","Time flows left to right; each horizontal line is a qubit. A box is a single-qubit gate; a filled dot joined to a box (or ⊕) is a control. The example below shows a Hadamard building superposition, then a CNOT entangling the two qubits into a Bell state."),
              ("circuit", {"qubits":2,"cols":[[{"g":"H","t":0}],[{"g":"X","c":0,"t":1}]]}),
              ("h2","Universality"),
              ("p","A small set of gates can approximate any unitary to arbitrary accuracy. Two common universal sets are {Clifford + T} and {single-qubit rotations + CNOT}. This is why the gates in this section are enough, in principle, to run any quantum algorithm."),
              ("clip","f5-quantum-verdict.mp4")],
        related=[("hadamard-gate","Hadamard"),("cnot-gate","CNOT"),("clifford-t-universality","Clifford+T universality")],
        seo_type="TechArticle"))
