# -*- coding: utf-8 -*-
"""Digital Twins — predictive twins of BOTH Kronos machines (breeder + burner).
Public, honest gates, no economics."""
CAT="digital-twins"

P = {
 "the-interactive-3d-model": dict(title="The Interactive 3D Model",
   lede="Today, both Kronos machines live as an interactive 3D model you can open, rotate, and take apart — the working seed of the digital twin to come.",
   pts=["A browser-based, component-by-component 3D model of both machines — breeder (Hyperion) and burner.",
        "Every component is clickable, with real dimensions and the design parameters behind it.",
        "Runs the actual physics in the browser — not a cartoon, a computable model.",
        "Open to everyone; Kronos team members sign in for full engineering detail."],
   body="The 3D model is where the design becomes tangible. Rather than a static render, it is an explorable model of both machines: open the spherical-tokamak breeder or the tandem-mirror burner, pull them apart layer by layer, click any component to see its dimensions and the design point behind it, and run the physics live. It is the public face of the design record — and, deliberately, the first version of a system that grows into a full predictive twin once the machines are built and instrumented.",
   body_extra_link=True,
   related=[("from-3d-model-to-digital-twin","3D model → digital twin"),("the-breeder-digital-twin","Breeder twin"),("the-burner-digital-twin","Burner twin")]),
 "from-3d-model-to-digital-twin": dict(title="From 3D Model to Digital Twin",
   lede="The interactive 3D model and the predictive digital twin are the same system at two stages of maturity — one for today's design, one for tomorrow's operating machine.",
   pts=["Now (design stage): an interactive, physics-computable 3D model of both machines.",
        "Next: sensor hooks and real-time state estimation, so the model tracks a real machine.",
        "Then (FOAK ~2030): a live predictive twin running inside the control loop.",
        "Same model, growing fidelity and live data — not a rebuild."],
   body="A digital twin is not a different artifact from the 3D model — it is the 3D model plus three things it does not yet need while the machines are on paper: a live sensor feed, real-time state estimation that keeps it locked to the physical machine, and fast surrogate models so it can predict inside a control loop. Kronos builds the model first because everything the twin will do — explore the design space, rehearse operations, forecast maintenance — starts from the same computable model. As Hyperion and the burner move from paper to first-of-a-kind operation around 2030, the model gains data and becomes the twin.",
   related=[("the-interactive-3d-model","The 3D model"),("digital-twin-overview","Digital twin overview"),("real-time-state-estimation","State estimation")],
   gate="The twin capabilities (live data, in-loop prediction) arrive with the hardware. Today the model is validated against published simulation and prior experiments, not a running Kronos machine."),
 "digital-twin-overview": dict(title="The Kronos Digital Twin",
   lede="A digital twin is a live, physics-faithful software model of a real machine — Kronos runs one for each of its two machines, from design through operation.",
   pts=["A twin mirrors the real machine's state in software, updated from sensors in real time.","It runs faster than real time via surrogate models, so it can predict before the machine acts.","One twin for the breeder (Hyperion), one for the burner (Aegis / MetroVolt).","Used for design exploration, operator training, control, and predictive maintenance."],
   body="The digital twin is where Kronos's simulation codes, machine-learning surrogates, and real-time control converge. It is not a single program but a hierarchy: high-fidelity physics for design, fast surrogates for real-time prediction, and a data-assimilation layer that keeps the twin locked to the real machine's measured state. Because both Kronos machines are still on paper today, the twins currently serve design and verification; at first-of-a-kind operation (~2030) they become the operational brain.",
   related=[("the-breeder-digital-twin","Breeder twin"),("the-burner-digital-twin","Burner twin"),("surrogate-models","Surrogate models")],
   gate="No machine is built yet, so the twins are validated against published simulation and prior-experiment data — not yet against a running Kronos device. That validation closes at the gates."),
 "the-breeder-digital-twin": dict(title="The Breeder Digital Twin (Hyperion)",
   lede="A predictive twin of the Hyperion spherical-tokamak breeder — its plasma, magnets, blanket, and isotope output modeled together.",
   pts=["Models the D–T plasma equilibrium, heating, and stability of the spherical tokamak.","Tracks tritium breeding and helium-3 production as the strategic-product output.","Couples plasma, neutronics, and the center-stack magnet/shield in one model.","Drives design trade-offs today; will run operations at FOAK."],
   body="The breeder twin represents Hyperion end to end: the negative-triangularity plasma at Q ≈ 3.424 and 88.7 MW, the high-field REBCO magnets at 16.84 T peak, the neutron flux, and the resulting tritium and helium-3 production. Because Hyperion is sized to an isotope-supply requirement rather than to electricity, its twin's key outputs are material production rates and component lifetimes, not a power curve. It lets Kronos explore the 25,000-plus configuration design space and pick operating points before any steel is cut.",
   related=[("digital-twin-overview","Twin overview"),("the-burner-digital-twin","Burner twin"),("the-plasma-state-observer","Plasma state observer")]),
 "the-burner-digital-twin": dict(title="The Burner Digital Twin (Aegis / MetroVolt)",
   lede="A predictive twin of the D–³He tandem-mirror burner — central cell, high-field plugs, expander, and direct-energy converter.",
   pts=["Models the long central cell, 26.49 T plug throats, and ~53× expander.","Tracks the low-neutron D–³He burn (f_n ≈ 5.44%) and direct-conversion output.","One model serving both housings — Aegis (fixed defense) and MetroVolt (data centers).","Central to closing the end-plug density question at the gates."],
   body="The burner twin is structurally different from the breeder's: not a tokamak but a linear tandem mirror. It models the axial confinement set by the high-field plugs, the ambipolar potential, the expander fanning field lines from 26.49 T down to ~0.5 T, and the staged direct-energy converter that turns charged particles straight into electricity. Its highest-value job is stress-testing the burner's one real physics gate — end-plug density — across operating scenarios before hardware commits to them.",
   related=[("digital-twin-overview","Twin overview"),("the-breeder-digital-twin","Breeder twin"),("direct-energy-conversion-model","DEC model")],
   gate="The tandem-mirror burner has a real physics gate at the end-plug density; the twin quantifies it but cannot retire it — only the 2032 test burner can."),
 "real-time-state-estimation": dict(title="Real-Time State Estimation",
   lede="A twin is only useful if it tracks the real machine — state estimation fuses noisy sensors into a best current estimate, continuously.",
   pts=["Combines diagnostics (magnetics, interferometry, spectroscopy) into a coherent plasma state.","Uses Kalman/particle filters and ML observers.","Runs inside the control loop's latency budget.","Feeds both the controller and the predictive twin."],
   body="Dozens of diagnostics each see the plasma partially and noisily. State estimation is the mathematics — Kalman filters, particle filters, and learned observers — that fuses them into a single best estimate of the plasma's shape, current, density, and temperature, fast enough to act on. It is the bridge between raw sensors and a twin that can be trusted.",
   related=[("the-plasma-state-observer","Plasma state observer"),("kalman-filter","Kalman filter"),("twin-in-the-loop-control","Twin-in-the-loop")]),
 "twin-in-the-loop-control": dict(title="Twin-in-the-Loop Control",
   lede="When the digital twin runs inside the control loop, the plant can be steered by predicting the next state before it happens.",
   pts=["The twin predicts the plasma's response to candidate actuator moves.","A model-predictive controller picks the move that keeps the plasma in its safe envelope.","Requires surrogates fast enough to evaluate many futures per control step.","The architecture Kronos targets for disruption-free operation."],
   body="Classic controllers react to what already went wrong. A twin-in-the-loop controller simulates the immediate future under several candidate actions and chooses the best — model-predictive control powered by a fast twin. The enabling ingredient is surrogate models that run millions of times faster than first-principles physics, so many futures can be evaluated inside a single control step.",
   related=[("model-predictive-control","MPC"),("surrogate-models","Surrogates"),("real-time-state-estimation","State estimation")]),
 "physics-vs-data-driven-twins": dict(title="Physics-Based vs Data-Driven Twins",
   lede="A good twin blends first-principles physics with data-driven learning — each covers the other's weakness.",
   pts=["Physics models extrapolate but are slow and imperfect.","Data-driven models are fast but only trust-worthy where they've seen data.","Hybrid twins use physics for structure, ML for speed and calibration.","Uncertainty quantification says how far the twin can be trusted."],
   body="Pure physics is principled but too slow for real-time and carries modeling error; pure machine learning is fast but blind outside its training distribution. Kronos's twins are hybrid: physics provides the backbone and conservation laws, learned surrogates provide speed, and data assimilation calibrates the twin to the real machine — with uncertainty quantification flagging where the twin is guessing.",
   related=[("surrogate-models","Surrogates"),("uncertainty-quantification","Uncertainty quantification"),("digital-twin-overview","Twin overview")]),
 "predictive-maintenance-twin": dict(title="Predictive Maintenance with the Twin",
   lede="By tracking cumulative damage and drift, the twin forecasts when components will need service — before they fail.",
   pts=["Tracks first-wall dpa, magnet strain, and cyclic fatigue over time.","Flags divergence between expected and observed behavior.","Schedules maintenance around availability, not surprises.","Especially valuable for the breeder's neutron-loaded components."],
   body="Every operating hour accumulates wear the twin can integrate — neutron damage to the first wall, thermal and mechanical cycling of the magnets, erosion of plasma-facing surfaces. By comparing predicted and measured behavior, the twin distinguishes normal aging from an emerging fault and turns unplanned outages into scheduled service, protecting the availability that firm power depends on.",
   related=[("the-breeder-digital-twin","Breeder twin"),("uncertainty-quantification","Uncertainty quantification")]),
 "what-if-scenario-simulation": dict(title="What-If Scenario Simulation",
   lede="The twin lets engineers and operators try changes in software first — new operating points, fault responses, and upgrades — with zero risk to hardware.",
   pts=["Explore operating points across the design space before committing.","Rehearse fault and disruption responses safely.","Train operators on a faithful model.","Evaluate upgrades before installing them."],
   body="Because the twin is a faithful model, any change can be tried virtually: a new operating point, a different control policy, a component upgrade, or the machine's response to a fault. This is how a design-stage company de-risks decisions — and how an operating plant will qualify changes before they touch the real machine.",
   related=[("twin-in-the-loop-control","Twin-in-the-loop"),("digital-twin-overview","Twin overview")]),
}

def register(add,F):
    for slug,d in P.items():
        body=[("h2","In brief"),("ul",d["pts"]),("h2","The detail"),("p",d["body"])]
        if d.get("body_extra_link"):
            body.append(("html",'<p style="margin-top:18px"><a href="https://kronosfusionenergy.com/3D_Model" '
                         'style="display:inline-block;border:1px solid var(--gold);border-radius:6px;padding:9px 16px;'
                         'font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--gold)">'
                         'Launch the live 3D model &rarr;</a></p>'))
        add(dict(slug=slug,title=d["title"],cat=CAT,lede=d["lede"],body=body,
                 related=d["related"],gate=d.get("gate"),seo_type="TechArticle"))
