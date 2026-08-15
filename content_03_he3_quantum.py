# -*- coding: utf-8 -*-
"""Helium-3 for Quantum Computing — the isotope-demand angle that ties Kronos's
breeder product to the quantum industry. Public, no economics."""
CAT="he3-quantum"

P = {
 "helium-3-for-quantum-computing": dict(title="Why Quantum Computing Needs Helium-3",
   lede="Nearly every leading qubit runs near absolute zero — and the coldest, most reliable route there is a helium-3/helium-4 dilution refrigerator. Helium-3 is the scarce ingredient, and Kronos's breeder makes it.",
   pts=["Superconducting and spin qubits operate at ~10–20 millikelvin — a temperature only dilution refrigeration reaches continuously.",
        "The cooling power comes from diluting helium-3 into helium-4; every dilution fridge needs a helium-3 charge.",
        "Helium-3 is scarce on Earth (a tritium-decay byproduct); the U.S. strategic auction ended in 2009 and quantum-era demand keeps rising.",
        "Kronos's Hyperion breeder produces helium-3 independently of the tritium blanket — a domestic supply aligned with quantum's growth."],
   body="A quantum computer is only as stable as its refrigerator. Thermal noise destroys the delicate superpositions that qubits rely on, so the industry runs its processors at temperatures colder than deep space. The dilution refrigerator — the standard tool for reaching and holding millikelvin temperatures — depends on a working fluid of helium-3 mixed into helium-4. As quantum computers scale from hundreds to thousands of qubits, each system's helium-3 demand grows, against a supply that has been constrained since the 2009 auction. This is the demand-side case for the Kronos breeder: it is a domestic helium-3 source whose output scales with exactly the industry that needs it.",
   related=[("dilution-refrigerator","Dilution refrigerator"),("superconducting-qubits","Superconducting qubits"),("millikelvin-cooling","Millikelvin cooling")]),
 "dilution-refrigerator": dict(title="The Dilution Refrigerator",
   lede="The dilution refrigerator is the machine that keeps qubits colder than deep space — and it runs on helium-3.",
   pts=["Reaches ~2–10 mK continuously, unlike one-shot coolers.","Cooling comes from the enthalpy of mixing helium-3 into helium-4 across a phase boundary.","The helium-3 is circulated and recovered in a closed loop — but an initial charge is required per machine.","Scaling qubit counts drives larger fridges and more helium-3."],
   body="Below about 0.87 K, a helium-3/helium-4 mixture separates into two phases: a helium-3-rich phase floating on a dilute phase. Forcing helium-3 across that boundary into the dilute phase absorbs heat — the same way evaporation cools, but effective all the way down to a few millikelvin. A dilution refrigerator circulates helium-3 through this mixing chamber continuously, which is why it can hold a quantum processor at its operating temperature for weeks. The helium-3 charge is the enabling consumable, and it is the isotope Kronos's breeder produces.",
   related=[("helium-3-for-quantum-computing","He-3 for QC"),("millikelvin-cooling","Millikelvin cooling"),("superconducting-qubits","Superconducting qubits")]),
 "millikelvin-cooling": dict(title="Millikelvin Cooling for Qubits",
   lede="Why qubits need temperatures a hundredth of a degree above absolute zero — and what that requires.",
   pts=["Superconducting qubit energy gaps correspond to ~100–200 mK; operating well below that suppresses thermal excitation.","Thermal photons and quasiparticles are dominant error sources; cold means quiet.","Multi-stage cooling: pulse tube (~4 K) → still → mixing chamber (~10 mK).","Every stage below ~1 K relies on the helium-3 dilution cycle."],
   body="A qubit is a two-level system with a tiny energy gap. If the surrounding temperature is comparable to that gap, random thermal energy flips the qubit and erases the computation. Keeping the environment at ~10–20 mK makes thermal excitation exponentially unlikely, protecting coherence. Reaching that regime and holding it under the heat load of control wiring is the job of the dilution refrigerator — and thus of helium-3.",
   related=[("dilution-refrigerator","Dilution refrigerator"),("decoherence","Decoherence"),("superconducting-qubits","Superconducting qubits")]),
 "superconducting-qubits": dict(title="Superconducting Qubits",
   lede="The most widely deployed qubit today — Josephson-junction circuits that behave as artificial atoms, operating in a dilution refrigerator.",
   pts=["Built from Josephson junctions; the transmon is the dominant design.","Operate at ~10–20 mK inside a dilution fridge.","Fast gates (tens of ns) but relatively short coherence — error correction is essential.","Used by several of the largest quantum-computing programs."],
   body="Superconducting qubits are lithographically fabricated circuits whose lowest two energy levels serve as |0⟩ and |1⟩. They are fast and manufacturable with semiconductor-style processes, which is why they anchor many large quantum roadmaps — but they demand deep cryogenics, tying the whole approach to helium-3 supply.",
   related=[("dilution-refrigerator","Dilution refrigerator"),("transmon-qubit","Transmon"),("spin-qubits","Spin qubits")]),
 "spin-qubits": dict(title="Spin Qubits",
   lede="Qubits encoded in the spin of a single electron or nucleus — compact, silicon-compatible, and also cryogenic.",
   pts=["Encode information in electron/nuclear spin in quantum dots or donors.","Silicon-CMOS compatible — a manufacturing advantage.","Long coherence in isotopically purified silicon.","Still operate at sub-kelvin temperatures — dilution-fridge territory."],
   body="Spin qubits promise dense, foundry-compatible quantum processors. Isotopically enriched silicon-28 removes magnetic nuclear noise, extending coherence. Like superconducting qubits, they run cold — reinforcing that helium-3 cooling underpins multiple competing hardware paths, not just one.",
   related=[("superconducting-qubits","Superconducting qubits"),("trapped-ion-qubits","Trapped-ion qubits"),("millikelvin-cooling","Millikelvin cooling")]),
 "trapped-ion-qubits": dict(title="Trapped-Ion Qubits",
   lede="Qubits stored in the electronic states of individual ions held by electromagnetic fields — long coherence and high-fidelity gates.",
   pts=["Ions confined in Paul traps; states manipulated with lasers.","Excellent coherence and gate fidelity; all-to-all connectivity.","Slower gates and harder scaling than solid-state qubits.","Cryogenic operation improves vacuum and stability."],
   body="Trapped ions offer some of the highest gate fidelities demonstrated. Their coherence is outstanding, though scaling to many ions and speeding up gates are active challenges. Cryogenic ion traps improve vacuum quality and coherence, adding to the industry's cold-infrastructure demand.",
   related=[("superconducting-qubits","Superconducting qubits"),("spin-qubits","Spin qubits")]),
 "topological-qubits": dict(title="Topological Qubits",
   lede="A hardware-level approach to error resistance — storing information non-locally so that local noise can't easily corrupt it.",
   pts=["Encode information in non-local (topological) degrees of freedom.","Aim for intrinsic protection against local errors.","Still experimental; materials and readout are hard.","Also require deep cryogenics."],
   body="Topological qubits seek to bake error protection into the physics itself, potentially reducing the overhead of error correction. The approach is promising but unproven at scale, and — like the others — lives in the millikelvin regime.",
   related=[("quantum-error-correction-overview","Error correction"),("superconducting-qubits","Superconducting qubits")]),
 "helium-3-supply": dict(title="The Helium-3 Supply Problem",
   lede="Helium-3 is scarce, strategically managed, and increasingly demanded — the supply gap Kronos's breeder is positioned to fill.",
   pts=["Primary terrestrial source: decay of tritium in weapons stockpiles.","U.S. federal auction ended in 2009; allocations are managed.","Demand spans quantum computing, neutron detection, and medical imaging.","Kronos breeds helium-3 independently of the tritium blanket."],
   body="Helium-3 does not occur in useful quantities in the atmosphere; on Earth it comes almost entirely from the beta decay of tritium. That ties supply to a shrinking, tightly-controlled stockpile even as quantum computing, homeland-security neutron detectors, and lung MRI all compete for it. A fusion breeder that produces helium-3 as a designed product — rather than a byproduct — is a structural answer to that shortage. This is the strategic-product thesis behind Hyperion.",
   related=[("helium-3-for-quantum-computing","He-3 for QC"),("neutron-detection","Neutron detection")],
   gate="Helium-3's strategic value is real, but Kronos treats it as strategic optionality, not the bankable base case — tritium supply is the primary near-term product."),
 "neutron-detection": dict(title="Helium-3 in Neutron Detection",
   lede="Helium-3 is the gold-standard gas for detecting neutrons — a homeland-security and scientific need that competes with quantum computing for the same scarce isotope.",
   pts=["He-3 has a large neutron-capture cross-section, making efficient, low-background detectors.","Used at ports and borders for radiation screening.","The same supply feeds quantum cryogenics — hence the competition.","Kronos supply eases both demands."],
   body="Helium-3 proportional counters are the benchmark for thermal-neutron detection, valued for sensitivity and gamma rejection. Their deployment in security screening was a major driver of the post-2009 supply squeeze — the same squeeze now felt by the quantum industry.",
   related=[("helium-3-supply","He-3 supply"),("helium-3-for-quantum-computing","He-3 for QC")]),
}

def register(add,F):
    for slug,d in P.items():
        body=[("h2","In brief"),("ul",d["pts"]),("h2","How it works"),("p",d["body"]),
              ("clip","c5-strategic-isotopes.mp4")] if False else \
             [("h2","In brief"),("ul",d["pts"]),("h2","The detail"),("p",d["body"])]
        add(dict(slug=slug,title=d["title"],cat=CAT,lede=d["lede"],body=body,
                 related=d["related"],gate=d.get("gate"),seo_type="TechArticle"))
