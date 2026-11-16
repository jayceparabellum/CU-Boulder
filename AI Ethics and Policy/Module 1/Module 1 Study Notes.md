# Module 1 Study Notes: Ethics, Policy, and Governance

**Course:** AI Ethics and Policy (CU Boulder / Coursera), instructor Casey Fiesler
**Sources covered:** 6 lecture transcripts; Calo (2017); UNESCO Recommendation on the Ethics of AI (2021); Lessig, *Code v2*, Ch. 7

> **How to use these notes.** These are summaries, explanations, and self-made practice questions. They do **not** answer the lab notebook prompts or pick quotes for the reading activities. That thinking is yours to do. Where a lecture includes a lab notebook prompt, these notes only say that a prompt comes up there.
>
> **Spelling note.** The lecture transcripts are auto-generated and misspell some names. These notes use the usual spelling and give the transcript's version in brackets the first time, e.g., Lyria Bennett Moses [transcript: "Lydia Bennett-Moses"].

---

## 1. Module Overview

Module 1 sets up the vocabulary and frameworks for the rest of the course. The course is not about what AI is, and it does not start from ethical theory. It is about **what happens after an ethical concern has been identified**: how institutions turn values into laws, standards, and practices, and why those efforts sometimes work and sometimes fail. The module separates four terms that people often mix up. **Ethics** identifies values. **Governance** is the whole ecosystem of policies, norms, laws, and institutions. **Policy** is the deliberate effort to steer that ecosystem. **Law/regulation** covers binding, state-enforced rules. Next comes a hard first problem: what counts as "AI," and does it need its own law at all? Then the module covers why societies govern technology (they respond to sociotechnical *change*, not to the technology itself) and why turning principles into rules is hard (principles are abstract and conflict with each other, plus the Collingridge dilemma and the pacing problem). It ends with Lessig's model, which says behavior is regulated by **law, norms, markets, and architecture (code)**. The point of that model is that governance happens in many places besides legislatures.

**How the lectures connect:**
- **L1-L2 (Course intro, Assignments):** What the course is for: frameworks rather than memorized laws; thinking rather than "right answers."
- **L3 (Ethics, Policy, Governance):** Defines the key terms. It points ahead to Calo (why "policy"), UNESCO (definition of ethics), and Lessig (broad definition of regulation).
- **L4 (What Are We Governing Anyway?):** The definition problem. Definitions act as governance tools. The lifecycle approach. The "law of the horse" debate (Easterbrook vs. Lessig, then Calo on robotics).
- **L5 (From Principles to Policy):** Why govern, and how to get from principles to rules. Rationales for regulation, ethics washing, conflicting principles (Asimov), the Collingridge dilemma, the pacing problem, soft law. This leads into "not all governance is law."
- **L6 (Lessig's Model):** The four modalities of regulation, "code is law," and how to apply them to AI. It ties back to L3 (the broad meaning of regulation) and L5 (Asimov's laws as architecture).

---

## 2. Lecture Notes

### Lecture 1: Introduction to the Course

**Key points**
- The course is *not* about what AI is, and it does not start from ethical theories or ask whether a particular use of AI is good or bad. It is about **what happens after an ethical concern is identified**: how people and institutions shape what comes next.
- Its central question: how do concerns like privacy, discrimination, labor, ownership, and environmental impact become laws, standards, or organizational practices, and why do those efforts succeed or fail?
- Working definitions: **ethics** helps us think about what *ought* to be done. **Policy** turns those goals and values into more specific courses of action. **Governance** is the process through which people and institutions make those choices and shape outcomes using policy tools.
- Law is one tool among many. The course is not only about law and is not about U.S. law in particular. It covers the U.S., EU, China, and other approaches, plus global questions of participation, power, and representation.
- The course is not only about generative AI. "AI" has existed as a term since the 1950s. The course covers LLMs and also hiring algorithms, facial recognition, workplace management systems, and other machine learning.
- The field moves fast, and the videos were recorded in summer 2026, so details will go out of date. The goal is **frameworks for interpreting whatever happens next**, not a list of laws to memorize.
- On learning: the aim is critical thinking, not memorization. There are often no clear right answers. Some of what the instructor says is interpretation, and disagreeing with her is a sign the class is working.

**Context:** Fiesler is an associate professor of information science at CU Boulder with an affiliation in computer science. She has a PhD in human-centered computing and a law degree. This is the third course in a sequence: (1) *Current Issues in Ethics and AI* (Bobby Schnabel); (2) *AI Ethics in Society's Future* (Fiesler). It is designed to stand alone.

### Lecture 2: Explanation of Assignments

**Key points**
- There are three components: **lab notebooks**, **quizzes**, and a **final exam**.
- **Lab notebooks:** a working record of your thinking. For each reading you give a quote you find insightful. During lectures you answer discussion-style prompts. You submit it as a PDF for peer review. It is graded on **completion and coherence, not correctness**. It is optional for non-credit learners but strongly encouraged.
- **Quizzes:** required for everyone, open book, and can be retaken as many times as you like. They are designed to draw attention to important ideas. Each ends with a few open-ended reflection questions, graded on completion, which help prepare you for the final.
- **Final exam:** for credit learners only, peer-reviewed, and builds on thinking from the notebooks and reflections.
- **Generative AI policy:** not banned, partly because the instructor does not think a ban can reasonably be enforced. Students are asked to think carefully about what they use it for. Since grading is on completion, there is no reason to outsource your thinking. The goal is your own perspective, and AI cannot do that for you.

### Lecture 3: Introduction: Ethics, Policy, and Governance

**Key points**
- Public conversations about AI harms often end with "**there should be a law**." The instinct makes sense, because many AI issues raise governance questions: What should AI be allowed to do? Who is responsible for harm? What transparency is owed? What risks are acceptable? Who decides?
- AI governance is hard because the technology evolves quickly, many policymakers understand it poorly, and there is uncertainty about consequences, future capabilities, harms, and even what counts as AI.
- **Ethics** means systematic reflection on what is good, right, fair, or just. UNESCO defines it as "a dynamic basis for the normative evaluation and guidance of AI." Ethics generates concerns, but on its own it **lacks enforcement mechanisms**.
- **Governance** is the broadest term. The *Oxford Handbook of AI Governance* defines it as the policies, norms, laws, and institutions that shape how AI is built and deployed. Governance is **not only something governments do**. It includes industry standards, organizational policies, procurement, technical architectures, professional norms, market incentives, and ethical norms. It is a **sociotechnical system**.
- **Policy** is narrower: deliberate processes through which institutions make decisions about collective problems and public priorities. Calo prefers "policy" to "governance" because governance is too flexible, and because policy implies exploration and planning in the public interest without assuming that every problem needs legislation right away. **Policy does not necessarily mean law.**
- **Law** is narrower still: legally binding rules enforced by a state (statutes, judicial decisions, other formal requirements).
- **Regulation** has two senses. (1) The narrow legal sense: agency rules that put a broad law into practice. Example: the U.S. **Clean Water Act** says water must be safe, and the **EPA** sets specific parts-per-million limits and permit paperwork. (2) Lessig's broad sense: anything that constrains behavior, including law, markets, social norms, and architecture/code.
- Summary: ethics helps societies identify values and concerns. Governance and policy put those values into practice and negotiate competing priorities under real-world constraints.

**Named frameworks / theories**
- **Consequentialism / utilitarianism:** focuses on outcomes. In AI debates this shows up as maximizing benefits and minimizing harms.
- **Deontology:** focuses on duties, rules, and rights. Some acts are wrong even if they produce good outcomes.
- **Virtue ethics** [transcript: "Relatioethics"]: focuses on the character and judgment of moral actors.
- **Ubuntu:** an African relational philosophy, often summarized as "I am because we are." It emphasizes interconnectedness, collective well-being, and relational responsibility. In AI debates it might bring forward shared benefit, *collective* privacy, and restorative rather than purely punitive responses to harm.
- Ethics can also just mean a **personal moral compass**. Different frameworks reach different conclusions, which is one reason ethics alone is hard to use as a basis for governance.

**Scholars / sources cited:** UNESCO Recommendation; Ryan Calo (ethics vs. policy; companies prefer flexible principles that are hard to enforce); *Oxford Handbook of AI Governance*; Lawrence Lessig (preview).

**Lab notebook:** Prompt 1 comes up here. These notes do not answer it.

### Lecture 4: What Are We Governing Anyway?

**Key points**
- Defining AI for policy is hard, and **the definition you pick changes what gets regulated**. Definitions are not neutral. They are **governance tools** that decide what counts, what escapes oversight, and which harms, concerns, and funding priorities get attention.
- **UNESCO deliberately gives no single fixed definition.** It describes AI systems by their characteristics, capabilities, and lifecycle stages, because AI is a moving target. The capabilities in 2026 are very different from those in November 2021.
- AI as a category is unstable. The **classic CS joke** is that once something works reliably, people stop calling it AI. Examples: optical character recognition, spam filtering, autocomplete, simple recommender systems.
- **Krafft et al. (2020), "Defining AI in Policy versus Practice"** [transcript: "Kraft"]: researchers tend to define AI in **functional/technical** terms (performs computational tasks, learns from data). Policy documents tend to define it in terms of **human-like thinking or behavior**. Technical definitions cover more of today's systems. Human-like definitions point toward hypothetical future systems. The authors warn that this can over-emphasize future concerns (killer robots, superintelligence) at the expense of present issues (content moderation, predictive policing). This is the **today's harms vs. tomorrow's harms** tension.
- **Alternative: govern effects or the lifecycle rather than the technology.** Ask how the system was developed, what data was used, who was affected, how it is monitored, and what risks emerge over time. Governance can happen at each stage: data collection, design, training, deployment, procurement, monitoring, and decommissioning. Governance is rarely about banning or permitting a technology outright. More often it shapes processes, incentives, responsibilities, and accountability.
- **Does AI need its own law?** **Frank Easterbrook** criticized special "cyberlaw," which is the **"law of the horse"** argument: we do not create horse law. We apply general law to horses (tort if it kicks you, property for custody disputes, criminal law for theft). Technologies change, and general principles last.
- **Lessig's reply:** we do not need a separate legal system for every technology, but some technologies create **fundamentally new regulatory conditions**. What matters is *what the technology changes*. The internet changed the underlying **architecture** through which people interact, and that architecture itself regulates. Studying cyberlaw reveals how regulation works in general.
- **Calo (2015)** (*Robotics and the Lessons of Cyberlaw*) argues that robotics and AI put pressure on law through **emergence** (outcomes that are hard to predict), **social valence** (people respond socially to AI), and **embodiment** (robots act physically, e.g., driving, entering homes, assisting in surgery). These features complicate responsibility and accountability.
- Lessig's point applies to AI too: **AI itself regulates behavior.** Algorithmic moderation shapes speech, and automated decision systems govern jobs, loans, housing, and healthcare.
- The instructor's view: AI does introduce new challenges. She notes that in the book she co-authored, *Human-Computer Interaction and US Law*, the only technology-specific chapter is about AI.

**Lab notebook:** Prompt 2 comes up here. These notes do not answer it.

### Lecture 5: From Principles to Policy

**Key points**
- **UNESCO as a model of the ethics-to-policy move:** it starts with values (dignity, human rights, fairness, accountability, transparency, sustainability, human oversight) and then gives concrete recommendations (impact assessments, oversight, international cooperation). It goes from "what do we value?" to "what should institutions do?"
- **Ethics and governance solve different problems.** Ethics identifies values and shared expectations. It does not say what happens when those expectations are ignored. That gap leads to **ethics washing**: organizations publicly embrace principles while resisting binding accountability (connects to Calo). Many ethics debates therefore become governance debates about *how* to encourage, require, monitor, or enforce.
- **Why govern? We respond to change.** **Lyria Bennett Moses** [transcript: "Lydia Bennett-Moses"] argues regulation usually targets not the technology itself but the **changes** technology creates: new activities, risks, opportunities, concentrations of power, and vulnerabilities. **Matthijs Maas** [transcript: "Matai Moss"] builds on this: regulate **sociotechnical change** rather than "AI." Analogy: we do not regulate electricity because it exists. We regulate electrical infrastructure, workplace safety, environmental impact, and competition.
- **Common regulatory rationales** (drawn from Bennett Moses and Maas): (1) market failures; (2) risks to human health, safety, or the environment; (3) risks to moral interests, rights, or values; (4) threats to **social solidarity** (fair distribution of benefits and burdens); (5) threats to democratic processes; (6) preserving the **integrity of governance itself** (keeping institutions able to respond to new risks). If governance focuses on these changes, a precise definition of AI may not be needed.
- **Principles alone cannot guarantee ethical AI** (**Brent Mittelstadt** [transcript: "Middlestad"]). (a) Principles are abstract. They name values but not how to implement them, who is responsible, or what happens on violation. (b) AI development lacks the professional structures that medicine has (licensing, fiduciary duties, accountability). Software engineering has professional codes of ethics, but they **lack teeth**, partly because there is no licensure, and they are less grounded in practice. Principles therefore act as **aspirations**, not enforceable commitments.
- **Principles conflict:** transparency vs. security, privacy vs. safety, fairness by one metric vs. another. Turning principles into rules means deciding how to balance them, and that is often where policy begins.
- **Asimov's Three Laws of Robotics** (via legal scholar **Simon Chesterman**): a tiered priority system for handling conflicts. They are "laws" built into robots' positronic brains, not enforced by a state, so they resemble **architecture as regulation**. Asimov's **1942 story "Runaround"** shows a robot paralyzed by a rule conflict over how strong an "order" must be to override the Third Law. The later **Zeroth Law** (duty to humanity as a whole) proved impossible to put into practice. The lesson: even when people agree on high-level principles, reducing them to rules creates new problems.
- **The Collingridge dilemma** (David Collingridge, *The Social Control of Technology*, 1980), cited by Chesterman. **Information problem:** early on, intervention is easy but consequences are unknown. **Control problem:** by the time consequences are clear, the technology is entrenched and hard to change. Act too soon and you may regulate the wrong problem. Act too late and harms become entrenched.
- **The pacing problem** (**Gary Marchant** [transcript: "Gary Martin" / "Marchand"]): (1) existing legal frameworks assume a static technology, and (2) legislatures and agencies are structurally slow. Example from Marchant's 2025 law review article: after ChatGPT's release (Nov 2022), Congress held many hearings and introduced **100+ AI bills**, but very little has happened federally since.
- **Current landscape:** binding law exists in some places, such as the **EU AI Act** and **South Korea's AI Basic Act**, plus a patchwork of U.S. state laws. This produces a complex, divergent landscape (previewing **Alanoca et al.** [transcript: "Alan Okun"] in Module 2). There are worries that the EU AI Act may have been **too early**, since it was negotiated before general-purpose generative AI took off. Even so, the time between ChatGPT and the Act's passage in 2023 was long enough for foundation models to become embedded. Laws drafted in 2023 are already showing strain by 2026.
- **Marchant's proposed fix: soft law**, meaning measures that set substantive expectations but are **not directly enforceable by government** (more in Module 2). This is why the course looks beyond law to standards, industry norms, and architecture.

**Lab notebook:** Prompt 3 comes up here (it uses the UNESCO values section and policy areas). These notes do not answer it.

### Lecture 6: Lessig's Model of Regulation

**Key points**
- Here **regulation** means **any force that constrains behavior**, not only government rules. Behavior can be regulated even when no legislature has passed a law.
- **The "pathetic dot":** the regulated person, developer, or company at the center, acted on by four forces. Regulation is the **combined effect** of all four.
- **Speeding example (from the lecture):**
  - **Law:** a speed limit and the threat of a ticket or court. Works through the *threat of punishment*.
  - **Norms:** a "slow, children at play" sign, a neighbor's disapproving look, the shared view that speeding makes you a jerk. Works through *approval and disapproval*.
  - **Markets:** ticket costs, higher insurance premiums, fuel costs, not being able to afford a fast car. Works through *prices and incentives*.
  - **Architecture:** a speed governor in the car, speed bumps in the road. Works by shaping what is *possible, difficult, or impossible*.
- Governance discussions often focus only on law, but many effective forms of governance happen without legislation.
- **Langdon Winner, "Do Artifacts Have Politics?":** discusses the story from *The Power Broker* that **Robert Moses** designed New York bridges too low for buses. As a result, Black residents, who were less likely to own cars, could not reach public beaches, which amounted to de facto segregation. Can a bridge be racist? Politics are built into architecture when it prevents certain people from doing certain things. Other physical examples: speed bumps, benches with bars that stop people from sleeping on them.
- **Digital architecture** includes software, hardware, protocols, interfaces, and design choices. **"Code is law"** does not mean software replaces law. It means code regulates behavior in a similar way. Examples: authentication requirements, platform posting limits, and **DRM** (if the threat of punishment does not stop copying, make copying technically impossible).
- **Applied to AI**, for a company deciding whether to deploy a risky AI system: **law** (privacy, anti-discrimination, liability, consumer protection); **markets** (customers avoiding harmful products, investors pushing to reduce risk, insurers raising premiums); **norms** (professional expectations, media scrutiny, public criticism, employee collective action, academic criticism); **architecture/code** (safety guardrails, content filters, adversarial technical measures against bad actors).
- When ethics or a personal moral compass is not enough, especially when doing the right thing conflicts with self-interest such as making money, people reach for "there should be a law." But the other modalities can work just as well, and **many more people have power over them**, including the public through markets and norms.

**Lab notebook:** Prompt 4 comes up here. These notes do not answer it.

---

## 3. Reading Notes

### Reading 1: Calo, "Artificial Intelligence Policy: A Primer and Roadmap"

**Citation:** Ryan Calo, *Artificial Intelligence Policy: A Primer and Roadmap*, 51 U.C. Davis Law Review 399 (2017). Written for the UC Davis Law Review's 50th-anniversary symposium, *Future-Proofing Law: From rDNA to Robots*. Calo was at the University of Washington School of Law at the time.

**Central thesis:** AI's techniques, terminology, and hopes and fears are not new. What *is* new is (1) practical breakthroughs in machine learning driven by much more computing power and data, and (2) policymakers finally paying attention. Calo offers a **roadmap, "not the road itself"**: a map of the key AI policy questions that describes each challenge "without prejudging the policy outcome." He deliberately uses the frame of **policy** rather than ethics or governance. He argues that fear of an AI apocalypse is a distraction with real opportunity costs.

**Structure**
- **Part I: Background.** (A) What is AI? (B) Where is it developed and deployed? (C) Why "policy"?
- **Part II: Key questions.** (A) Justice and equity; (B) Use of force; (C) Safety and certification; (D) Privacy and power; (E) Taxation and displacement of labor; (F) Cross-cutting questions: institutional configuration and expertise, investment and procurement, removing hurdles to accountability, mental models of AI.
- **Part III: On the AI apocalypse.** Then a conclusion.

**Key arguments**

*Part I: Background*
- **No consensus definition.** AI is "best understood as a set of techniques aimed at approximating some aspect of human or animal cognition using machines." It is an **umbrella term**. Early "good old fashioned AI" relied on symbolic systems and underdelivered, which contributed to the **"AI Winter"** of the late 1980s. Researchers then shifted to data-driven approaches aimed at specific **domains** (e.g., speech-to-text, chess) rather than holistic intelligence.
- **Machine learning** means a system's capacity to improve its performance at a task over time (citing Surden). Most ML techniques are decades old. The recent jump in effectiveness comes from faster computers plus more data. Deep learning uses many-layered structures to extract features from large datasets.
- **Where AI is developed:** industry, academia, and the military, with industry in the lead. Industry hires scientists away from universities and has unmatched compute and data. As of 2017, roughly **seven companies** (Google, Facebook, IBM, Amazon, Microsoft, Apple, Baidu) held capabilities far ahead of everyone else. Calo distinguishes **disembodied AI** (data in, data out) from **robotics/cyber-physical systems**, which act physically, and says the law may treat the two differently. He uses a generous definition that includes everyday systems (autocorrect, Google Images) and focuses on what is different about contemporary AI.
- **History of policy attention:** JFK declined calls for a robots-and-labor conference. No Federal Automation Commission was formed. The first congressional hearings on AI were in 2016. The Obama White House held workshops and published three reports. Japan and the EU were further ahead.
- **Why "policy"? (central to Lecture 3)**
  - *Against ethics as the frame:* ethics is "notoriously malleable and contested." Both Kant and Bentham "get to say 'should.'" Official policy has **finality** once issued (he cites H.L.A. Hart's "rule of recognition"). Even with moral consensus, ethics **lacks a hard enforcement mechanism**. The handful of dominant companies "are going to prefer ethical standards over binding rules" because no penalties attach to changing or ignoring them. History also shows industry ethics codes being struck down as **restraints on trade**: the DOJ sued the National Society of Professional Engineers (NSPE) in the 1970s over a bidding canon, and the FTC sued it in the 1990s over advertising restrictions. Codes for structural engineers, chiropractors, and doctors were challenged too. Calo does not reject ethics principles, but says we should look at who writes them and why, and at their effects.
  - *Against governance as the frame:* it is flexible, perhaps **too flexible** ("not entirely clear what is being governed and by whom"). Governance literature often assumes authority will or should **devolve to non-state actors** (e.g., internet governance through ICANN and IETF). That **tacitly hands responsibility to industry**.
  - *For policy:* policy "admits of the possibility of new laws, but does not require them." It conveys exploration and planning, the finality of law, and the **primacy of public interest**. Industry may try to influence policy, but setting it is not industry's role.

*Part II: Key policy questions*
- **A. Justice and equity** (the most developed area, often framed as fairness, accountability, transparency, "FAT").
  - *Inequality in application:* AI that does not work well for everyone. Examples: a camera warning that a Taiwanese-American blogger was blinking; image recognition labeling a Black couple as gorillas; translation that genders engineers male and nurses female (Turkish gender-neutral "o" translated as "he is a doctor" / "she is a nurse"); Facebook ad tools that excluded users by race; the Princeton Review price discrimination that hit Asian Americans; an algorithm rejecting an Asian man's passport photo for "closed eyes." Causes include underrepresentation in training data and **selective application** to marginalized groups. Predictive-policing heat maps lead to disproportionate harassment of Black residents, while police do not turn such tools inward to predict officer misconduct. Policy questions: what is best practice for reducing bias, and which mechanism (anti-discrimination law, consumer protection, industry standards) should incentivize it? How do we spread AI's risks and benefits evenly?
  - *Consequential decision-making:* systems that make or help make decisions about people, often against a backdrop of **procedural guarantees** (U.S. due process and equal protection; the EU right to human involvement and a pending right to explanation). Algorithms are already used for policing, parole, and sentencing. Three facets: (1) list what values a procedure is trying to advance, including built-in tradeoffs (FRCP's "just, speedy, and inexpensive"; Sixth Amendment trial rights vs. speed); (2) decide which values can be carried over to machines. Deep learning may show correlation without causation ("what will happen but not why"), so it may be a poor basis for warrants, testimony, or findings of fact. Prosecutorial discretion, the rule of lenity, and pardons may not be mechanizable at all. Some decisions (e.g., ending life support) raise dignity concerns. (3) Design and vetting in practice. **Efficiency** is underdeveloped as a value ("justice delayed is justice denied"). There are accuracy tradeoffs too: making a system more transparent or less biased can reduce accuracy, and accuracy is part of fairness. Rolling a die is transparent and unbiased but not fair.
- **B. Use of force:** autonomous weapons. International consensus says humans should never give up **"meaningful human control"** over a kill decision, but what that means is unsettled (monitoring? target selection? defensive systems?). Responsibility questions remain even with human control, e.g., algorithmic target selection for drone strikes. Elish's concern: humans placed "in the loop" only to absorb liability (the moral crumple zone idea).
- **C. Safety and certification.** (1) *Setting and validating safety thresholds:* "safer than humans" is an inadequate standard for driverless cars. Safer than humans unaided or assisted? Overall or in every condition? How much safer? These are policy questions, not technical ones. Verification has a **"who"** (government, third-party, or self-certification) and a **"how"** (unit testing, fault injection, virtualization, supervision). Indirect harms (high-speed trading, cognitive radio, disinformation). Courts set safety policy through liability, which emergent AI complicates, and markets through insurance. (2) *Certification:* autopilots do not go to flight school. What about surgical robots, or AI that gives legal, medical, or financial advice? (FDA classifying apps as medical devices; parking-ticket "robot lawyers.") (3) *Cybersecurity:* with cyber-physical systems, "bones instead of bits" are at stake. AI changes offense and defense (DARPA's Cyber Grand Challenge). **Adversarial machine learning** creates a new attack surface.
- **D. Privacy and power.** Privacy discourse has moved from individual control of information to the **power** institutions gain from information. Here AI works "only too well."
  - *Pattern recognition problem:* AI can **"derive the intimate from the available"** (e.g., Target inferring a pregnancy). Consumers cannot foresee the consequences of sharing, so notice and choice breaks down. Citizens cannot resist surveillance. Two Fourth Amendment doctrines are under strain: no reasonable expectation of privacy (1) in public and (2) in information given to third parties. Courts are responding (*United States v. Jones*, which required a warrant for GPS tracking; *Carpenter* was pending in 2017). But *Florida v. Jardines* reaffirms no expectation of privacy in contraband, and some argue an AI scan is not a "search" until a human sees the result. That raises the question: do we want **perfect enforcement**? Granular knowledge also enables manipulation: digital market manipulation, bots extracting personal information, political micro-targeting.
  - *Data parity problem:* ML rewards data access. Per Levendowski, practitioners can build datasets, buy them, or use "low-friction" sources such as public-domain content, which carry bias risks. Only big players can do the first two. Fewer firms than "a human has fingers" hold most of the data, which hurts competition and public research and bends ML toward profit. Calo calls this a privacy issue because firms **invoke privacy to refuse to share data**, which is a reason to be skeptical of industry ethics codes. Government data sharing is limited by free speech concerns (*Sorrell v. IMS Health*). Technical options include differential privacy and federated learning. The question is how to democratize AI without sacrificing privacy.
- **E. Taxation and displacement of labor:** the truck driver example. Many expect automation to move faster and touch more sectors than before. Responses: the Obama White House's thicker safety net, new jobs, universal basic income, better data. Taxes: "robots do not pay taxes" (IRS letter). Bill Gates says they should. Critics call a robot tax a tax on innovation.
- **F. Cross-cutting questions.**
  - *Institutional configuration and expertise:* AI policy today is **piecemeal** (agencies, states, cities). This has federalism-style benefits (experimentation, sensitivity to context), while others call for an "**FDA for algorithms**" (Tutt). Calo calls the "law is too slow" view **misguided**. Some laws do go stale (ECPA, 1986), but that is not inevitable and is often political. The FTC's technology-neutral "unfair and deceptive practices" standard keeps working. **The better-grounded problem is the government's lack of expertise.** Without its own experts, the state must rely on self-interested firms or freeze up. Options: a Federal Advisory Committee on AI, a **Federal Robotics Commission**, reviving the **Office of Technology Assessment**, expanding the CRS or OSTP, or technical staff in every branch.
  - *Investment and procurement:* government can steer AI by funding research (including social-science research on AI's impacts) and through **what it buys**. Procurement and contract terms can push whole markets toward better privacy and security.
  - *Removing hurdles to accountability:* proprietary systems resist scrutiny (e.g., *Loomis*, where a defendant could challenge risk scores but not the algorithm). Barriers include **trade secret law, the Computer Fraud and Abuse Act, and the DMCA anti-circumvention provision**.
  - *Mental models of AI:* policymakers should hold accurate mental models and help educate the public. Decades of fiction show AI as a threatening substitute for people, though not everywhere: Japan has *Astro Boy*, where the robot is a hero. AI as a **social agent** (Alexa, Siri, chatbots) creates risks of influencing children, disrupting civic discourse, and reducing solitude.

*Part III: On the AI apocalypse*
- Calo's view: AI is not an existential threat in the foreseeable future, and too much attention **distracts from immediate harms**. Bostrom's *Superintelligence* is the usual source for the worry, and Musk and Hawking have voiced it. Critics say there is no path to general human-level intelligence and no reason a superintelligence would seek domination (LeCun: computers do not have testosterone). Three scenarios: (1) AI wakes up and kills us (science fiction); (2) AI kills us by accident pursuing an arbitrary goal (the **paperclip** example; Sorcerer's Apprentice; King Midas). Calo finds a system that is simultaneously so primitive and so powerful unlikely. (3) Bad actors use AI, which is more worrying, but the path to existential threat is narrow. He grants that a low-probability, high-loss risk merits *some* attention. The strongest argument is **opportunity cost**: Domingos says the real problem is that AI is "too stupid" and has "already" taken over, and Barocas warns of an **"AI Policy Winter."**

*Conclusion:* there is reason for hope. We have more policymaking tools, interdisciplinary collaboration, and **timing**: AI caught policymakers' attention early enough in its life cycle to be channeled toward the public interest.

**Key terms (Calo)**
- **AI:** an umbrella set of techniques for approximating aspects of human or animal cognition with machines.
- **Machine learning:** a system's capacity to improve its performance at a task over time.
- **AI Winter / AI Spring:** the late-1980s funding collapse and the current resurgence.
- **Narrow/weak AI vs. strong AI / AGI:** single-domain systems vs. systems that work across domains.
- **Disembodied AI vs. cyber-physical systems:** AI that processes data vs. AI that acts physically.
- **Policy:** Calo's preferred frame. It allows new laws without requiring them, and stresses planning, finality, and public interest.
- **Inequality in application:** AI that works worse for some groups or is applied selectively to them.
- **Consequential decision-making:** AI used in material decisions about people, often under procedural guarantees.
- **Meaningful human control:** the contested standard for human involvement in lethal force decisions.
- **Adversarial machine learning:** deliberately tricking ML systems.
- **Pattern recognition problem:** AI deriving sensitive facts from innocuous data.
- **Data parity problem:** concentration of data in a few firms, which shapes who can do AI.
- **Perfect enforcement:** the question of whether a society should catch every violation.
- **AI Policy Winter:** Barocas's term for policy attention lost to apocalypse talk.

**Ties to lectures:** L3 uses Calo's case for "policy" over "ethics" and "governance" and his point that companies prefer unenforceable principles. L5 picks up on ethics washing. L4 cites Calo's 2015 "emergence / social valence / embodiment" paper, which this essay cites in n.33. Calo's skepticism about "law is too slow" can be compared with Marchant's pacing problem (L5): Calo puts the deeper problem in **lack of expertise** and politics. His "market through insurance" and procurement points line up with Lessig's market modality (L6).

---

### Reading 2: UNESCO, Recommendation on the Ethics of Artificial Intelligence

**Citation:** UNESCO, *Recommendation on the Ethics of Artificial Intelligence*. Adopted 23 November 2021 by the General Conference at its 41st session (Paris, 9-24 Nov 2021). Published 2022 (SHS/BIO/PI/2021/1). The mandate came from 40 C/Resolution 37 (Nov 2019).

**Central thesis / purpose:** a **globally accepted, standard-setting normative instrument** grounded in international law and human rights. It aims to articulate values and principles **and to put them into practice through concrete policy recommendations**, with strong emphasis on inclusion, gender equality, and protection of the environment and ecosystems (para. 6). It is **voluntary**: Member States are asked to apply it "on a voluntary basis," using legislative or other measures that fit their constitutional practice. It is addressed to Member States both as AI actors and as regulators, and it guides all AI actors.

**Structure:** Preamble; I. Scope of application; II. Aims and objectives; III. Values and principles (III.1 Values, III.2 Principles); IV. Areas of policy action (11 policy areas); V. Monitoring and evaluation; VI. Utilization and exploitation; VII. Promotion; VIII. Final provisions.

**Key content**

*Preamble:* acknowledges AI's positive and negative effects. Concerns include embedded and amplified bias, the need for algorithmic transparency, and impacts on dignity, rights, gender equality, democracy, and the environment. It stresses that low- and middle-income countries (**LMICs**), including LDCs, LLDCs, and SIDS, have been **underrepresented** in AI ethics debates. It says addressing risks "should not hamper innovation" but should encourage ethically conducted research. It lists many prior human rights instruments (UDHR 1948 onward).

*I. Scope (paras. 1-4):*
- Approaches AI ethics as "**systematic normative reflection**" based on a holistic, multicultural, evolving framework that gives societies a basis to *accept or reject* AI. It treats ethics as "a **dynamic basis for the normative evaluation and guidance** of AI technologies," with human dignity, well-being, and harm prevention as the "compass."
- **Deliberately offers no single definition of AI**, "since such a definition would need to change over time." It addresses AI systems as systems with "the capacity to process data and information in a way that resembles intelligent behaviour," typically involving reasoning, learning, perception, prediction, planning, or control. Three elements: (a) AI systems as information-processing technologies with varying degrees of **autonomy**, including machine learning (deep, reinforcement) and machine reasoning (planning, search, optimization), possibly in cyber-physical systems; (b) ethical questions arise across **all stages of the AI system life cycle**, from research and design through deployment, maintenance, trade, financing, monitoring, end-of-use, disassembly, and termination. **AI actors** are anyone involved in at least one stage, natural or legal persons. (c) AI raises **new types of ethical issues** (decision-making, labor, privacy, democracy, dual use, etc.), including reproducing biases and possibly, in the long term, challenging humans' sense of experience and agency.
- Pays special attention to UNESCO's core domains: **education, science, culture, and communication/information**.

*II. Aims and objectives (paras. 5-8):* make AI work for the good of humanity and prevent harm. Move from principles to "**practical realization**." Enable shared, multi-stakeholder responsibility through global, intercultural dialogue. Objectives: a universal framework to guide State legislation and policy; embed ethics across the life cycle; protect human rights, dignity, and gender equality; safeguard present and future generations and the environment; encourage pluralistic dialogue; promote equitable access and benefit-sharing, especially for LMICs.

*III. Values and principles (paras. 9-47):*
- **Values vs. principles (para. 10):** values are "motivating ideals" that inspire desirable behavior and are the foundations of principles. **Principles "unpack" the values more concretely so they can be operationalized.**
- **Tensions (para. 11):** all values and principles are desirable, but they may conflict in practice. That requires **contextual assessment** under **proportionality**. Any limits on rights must have a lawful basis and be reasonable, necessary, and proportionate.
- **Trustworthiness (para. 12)** is described as an *outcome* of putting the principles into practice. All policy actions aim to promote it.
- **Four values:**
  1. *Respect, protection and promotion of human rights, fundamental freedoms, and human dignity:* the intrinsic, equal worth of every person. No one is to be harmed or subordinated. No objectification of people (including vulnerable people) when they interact with AI.
  2. *Environment and ecosystem flourishing:* reduce environmental impact, including carbon footprint. Comply with environmental law and **precaution**.
  3. *Ensuring diversity and inclusiveness:* active participation by everyone. Do not restrict lifestyle choices. Overcome, and never exploit, infrastructure and skills gaps in LMICs.
  4. *Living in peaceful, just and interconnected societies:* solidarity. Every human "belongs to a greater whole." AI should not segregate, objectify, or turn groups against each other.
- **Ten principles:**
  1. *Proportionality and Do No Harm:* AI use must not exceed what is necessary for legitimate aims. The choice to use AI must be justified as appropriate and proportional, rights-respecting, context-appropriate, and scientifically grounded. **Final human determination** for irreversible or life-and-death decisions. AI **should not be used for social scoring or mass surveillance**.
  2. *Safety and security:* avoid unwanted harms (safety risks) and vulnerabilities to attack (security risks).
  3. *Fairness and non-discrimination:* social justice, inclusive access, multilingualism, addressing digital divides. Technologically advanced countries have a "**responsibility of solidarity**" toward the least advanced. **Effective remedy** against biased algorithmic decisions.
  4. *Sustainability:* continuous assessment of human, social, cultural, economic, and environmental impact (e.g., against the SDGs).
  5. *Right to privacy and data protection:* data protection frameworks, privacy impact assessments, **privacy by design**.
  6. *Human oversight and determination:* it must always be possible to attribute ethical and legal responsibility to physical persons or legal entities. Oversight includes **inclusive public oversight**. Humans may cede control in limited contexts, but AI "can never replace ultimate human responsibility." As a rule, life-and-death decisions should not be ceded to AI.
  7. *Transparency and explainability:* preconditions for rights, liability regimes, and the ability to challenge decisions. Should be appropriate to context and **balanced against privacy, safety, security**. People should be told when AI informs a decision and should be able to request reasons and make submissions to a human reviewer. In serious human rights cases this may require sharing code or datasets. **Explainability** means making outcomes intelligible, including how each algorithmic building block contributes.
  8. *Responsibility and accountability:* responsibility is ultimately attributable to AI actors according to their role. Oversight, impact assessment, audit, due diligence, **whistle-blower protection**, auditability, and traceability.
  9. *Awareness and literacy:* public education, digital skills, and media/information literacy, so people can make informed decisions and be protected from undue influence.
  10. *Multi-stakeholder and adaptive governance and collaboration:* respect data sovereignty under international law. Broad stakeholder participation. Open standards and interoperability. Adapt to shifting technology. Meaningful participation of marginalized groups and respect for Indigenous Peoples' self-governance of their data.

*IV. Areas of policy action (paras. 48-130):* these "operationalize the values and principles." Member States are at different levels of **readiness** (a "dynamic status"). UNESCO will develop a **readiness assessment methodology** and an **Ethical Impact Assessment (EIA)** methodology.
1. **Ethical Impact Assessment:** frameworks to assess benefits and risks and their effects on rights, labor, and the environment. Due diligence. Enforceable transparency protocols. Broad testing before market release. Public authorities required to run EIAs that are transparent, multi-stakeholder, and externally reviewable.
2. **Ethical Governance and Stewardship:** inclusive, multi-stakeholder governance with anticipation, monitoring, enforcement, and **redress**. **Soft governance** such as **certification** that does not unduly burden small firms. Self-assessment of whether adopting AI is appropriate at all (prohibit if it would violate rights). An independent **AI Ethics Officer**. Liability frameworks, with **no legal personality for AI systems**. **Policy prototypes and regulatory sandboxes**. Building judicial capacity. International safety and transparency standards with measurable, testable levels. Requirements to disclose and combat stereotyping.
3. **Data Policy:** data quality, privacy safeguards (including against surveillance), data-subject rights (access, erasure), protection for sensitive data (biometric, genetic, health, criminal), open data, data trusts, gold-standard datasets, a **digital commons** approach.
4. **Development and International Cooperation:** AI ethics in international forums, AI for development, research participation and leadership for LMICs.
5. **Environment and Ecosystems:** assess carbon, energy, and raw-material impacts. AI for environmental protection, with local and Indigenous participation. Favor data-, energy-, and resource-efficient methods. Apply the **precautionary principle**, and do not use AI where environmental impacts are disproportionate.
6. **Gender:** a transversal gender perspective in EIAs, gender action plans, funding, STEM participation, avoiding gender stereotyping, harassment-free environments.
7. **Culture:** heritage and endangered or Indigenous languages, NLP's impact on linguistic nuance, avoiding concentration in cultural markets, making local content discoverable, research on **AI and intellectual property**.
8. **Education and Research:** AI literacy, prerequisite skills, AI ethics curricula, strict limits on AI that monitors or predicts learners, research ethics training, interdisciplinary research, researcher access to private data.
9. **Communication and Information:** freedom of expression in automated content generation, moderation, and curation. Notice of removal and **appeal mechanisms**. Media and information literacy against mis/disinformation.
10. **Economy and Labour:** labor-market impact, upskilling and reskilling, safety nets, examining tax regimes, competitive markets, preventing abuse of dominant positions, respecting ethical standards when exporting AI.
11. **Health and Social Well-being:** safe, proven health AI. Final diagnosis and treatment decisions made by humans. Ethics committee review. Mental health research. Guidelines for human-robot interaction. Users should be able to tell whether they are interacting with an AI and to refuse. Awareness of **anthropomorphization**. Engaging children and young people.

*V. Monitoring and evaluation:* qualitative and quantitative monitoring. UNESCO methodologies (EIA, readiness, ex ante/ex post evaluation). Possible mechanisms: ethics commission, AI ethics observatory, regulatory sandboxes. *VI-VIII:* stakeholders should take "all feasible steps." UNESCO (with COMEST, IBC, IGBC) promotes the Recommendation, and civil society is an important advocate. The Recommendation is to be read as a whole, and nothing in it overrides international law.

**Key terms (UNESCO)**
- **AI system:** a system that processes data and information in a way that resembles intelligent behavior (reasoning, learning, perception, prediction, planning, control). Deliberately not defined in fixed terms.
- **AI system life cycle:** from research and design through deployment, maintenance, monitoring, end-of-use, and termination.
- **AI actor:** any natural or legal person involved in at least one life-cycle stage.
- **Ethics (UNESCO sense):** systematic normative reflection, "a dynamic basis for the normative evaluation and guidance" of AI.
- **Values vs. principles:** motivating ideals vs. more concrete statements that can be operationalized.
- **Proportionality:** AI use should not exceed what is necessary for a legitimate aim.
- **Ethical Impact Assessment (EIA):** a structured assessment of an AI system's benefits, risks, and rights impacts across its life cycle.
- **Readiness assessment:** UNESCO's methodology for a State's capacity to implement the Recommendation.
- **Soft governance:** non-binding mechanisms such as certification.
- **Regulatory sandbox / policy prototype:** safe environments for testing rules before formal adoption.
- **Privacy by design:** building privacy protections into systems from the start.
- **LMICs / LDCs / LLDCs / SIDS:** low- and middle-income countries, least developed countries, landlocked developing countries, small island developing States.

**Ties to lectures:** L3 takes its definition of ethics from UNESCO. L4 uses UNESCO's refusal to define AI and its lifecycle framing as examples of governance that does not depend on a definition. L5 uses UNESCO as the model of moving from values to policy, and its admission that principles conflict (para. 11) echoes L5's discussion of conflicting principles. As a *voluntary* instrument, UNESCO also shows the enforcement gap of ethics-based approaches (Calo, Mittelstadt) and connects to soft law (Marchant).

---

### Reading 3: Lessig, *Code: Version 2.0*, Chapter 7, "What Things Regulate"

**Citation:** Lawrence Lessig, *Code: Version 2.0*, Chapter 7, "What Things Regulate," pp. 120-137. (The extracted text also includes the first pages of Chapter 8, "The Limits in Open Code.")

**Central thesis:** to understand how behavior, especially behavior in cyberspace, is regulated, we need a general model that looks beyond government. Behavior is constrained by **four modalities: law, social norms, the market, and architecture (code)**. Regulation is their *sum*. They interact, and **law can regulate directly or indirectly by changing the other three**. In cyberspace, **code** is a newly powerful and newly urgent regulator and threat to liberty. **Indirect regulation through code can be invisible**, which undermines transparency and political accountability.

**Structure**
1. **Opening: Mill and threats to liberty.**
2. **"A Dot's Life":** the four-modality model (smoking example), applied to cyberspace.
3. **"On Governments and Ways to Regulate":** the constraints are plastic; law can change them; direct vs. indirect regulation (many examples).
4. **"The Problems of Indirection":** *New York v. United States*, *Rust v. Sullivan*, and post-*Shelley* segregation. Transparency.
5. **"Where This Leads":** the "West Coast Code vs. East Coast Code" letter. Worries about invisible and easier regulation.

**Key arguments**
- **Mill's method:** John Stuart Mill (*On Liberty*, 1859) saw liberty threatened not only by government but by **norms**: stigma and intolerance. Modern libertarians focus on government alone. Mill focused on *liberty*, whatever the source of the threat. Threats change over time: norms in 19th-century England, state suppression of speech in early-20th-century America, the market for the labor movement. Lessig argues that in the 21st century the newly urgent threat is **code**, "the instructions embedded in the software or hardware that makes cyberspace what it is," its "built environment" or **architecture**. Code is added to the list of threats, not substituted for the others.
- **The pathetic dot and smoking:** *law* (age limits, ID checks, where smoking is banned); *norms* (ask before smoking in someone's car, no need to ask at a picnic, never during a meal); *market* (price and quality of cigarettes; more choice means less constraint); *architecture* (nicotine-treated cigarettes are more addictive, so more constraint; smokeless cigarettes, less; strong odor, more). The dot's regulation is the **sum** of the four. Constraints "can support or oppose" each other: technology can undermine or support norms and laws.
- **How each constrains:** **norms** through community **stigma**; **markets** through **price**; **architecture** through **physical burdens**; **law** through threatened **punishment**. Law and norms work mostly through **ex post** sanctions. Architecture constrains in the moment, as a condition of access.
- **In cyberspace:** *law* (copyright, defamation, obscenity: "Legislatures enact; prosecutors threaten; courts convict"); *norms* (flaming for off-topic politics in alt.knitting, being "toaded" in a MUD for spoofing, bozo filters); *markets* (pricing, busy signals: AOL's switch from hourly to flat-rate pricing; advertisers reward popular sites); *code* (passwords, traceable "mouse droppings," encryption available or not). Code "embeds certain values or makes certain values impossible." Quoting Ethan Katsh, the code writer is the "architect." William Mitchell notes that cyberspace's bargains are built into software and access controls.
- **The constraints are plastic, and law can change them.** *Car radio theft:* a life sentence (law) vs. radios coded to work only in one car (architecture). Same goal, different costs. Efficiency and values may line up (code is cheaper, and a life sentence would be barbaric). But they may not: **life in prison for a parking ticket** might be efficient yet unjust. The regulator must weigh both **efficiency and values**. "Law-talk" wrongly treats the other three constraints as fixed.
  - *Law regulating the market:* law creates the market (contracts, property, currency) and shapes it with **taxes** (cigarettes, alcohol) and **subsidies** (tobacco production, child care).
  - *Law regulating architecture:* the **Americans with Disabilities Act** requires accessible building design.
  - *Architecture as regulation (examples):* **Napoleon III** rebuilt Paris in 1853 with wide boulevards to prevent barricades. **L'Enfant**'s Washington design, with a mile of difficult terrain between the White House and the Capitol. **Constitutional courts** placed away from capitals (Karlsruhe, Brno). **Speed bumps**. **Robert Moses**'s low Long Island bridges blocking buses, so African Americans who relied on public transit could not easily reach beaches ("invidious yet familiar"). An **airline** parking Monday-morning flights farther from baggage claim. A **hotel** installing mirrors by slow elevators. **Ralph Nader**'s push to make law force safer car design. **Neal Katyal** on architecture and crime (street lights; the 2000 Sydney Olympics; Crime Prevention Through Environmental Design). The 1933 World's Fair motto: "Science Explores: Technology Executes: Man Conforms."
  - *Law regulating norms:* **education** (Thurgood Marshall: education teaches citizenship and obeying the law). Debates over sex education show law trying to change norms. Law can damage norms as well as improve them.
- **Direct vs. indirect regulation.** Direct: law tells people how to behave and threatens punishment. Indirect: law modifies another modality. Polk Wagner: legal policy proposals that do not predict the technological response "are deeply incomplete." The interaction is **dynamic**, and the regulator seeks an "equilibrium." Examples:
  - *Seatbelts:* mandate (direct); education campaigns (norms); insurance subsidies (market); automatic belts or ignition locks (code).
  - *Disability discrimination:* anti-discrimination law; education; hiring subsidies; building codes.
  - *Drugs:* harsh prison terms, which per **Tracey Meares** can **weaken the community norms** that would otherwise discourage drug use. This is an indirect effect that can outweigh the direct one, which Lessig calls a "**Laffer Curve for criminal law**." Also education campaigns, border seizures (market), and spraying paraquat (code). The net effect cannot be deduced a priori.
  - *Abortion:* despite *Roe*, government regulates indirectly: *Rust v. Sullivan* (norms within medical care), *Maher v. Roe* (funding, i.e., market), *Hodgson v. Minnesota* (a 48-hour wait, i.e., the "code" of time).
- **The problems of indirection.** *New York v. United States* (Low Level Radioactive Waste Policy Amendments Act, 1985): Congress could not **commandeer** states by forcing them to regulate or "take title" to waste. The case's holding is narrow, but it shows why indirection matters: **"Indirection misdirects responsibility."** It muddies accountability. "If transparency is a value in constitutional government, indirection is its enemy." *Rust:* the government buried its policy in doctors' words, trading on professional authority, and patients did not even realize it was a policy choice. *Post-Shelley v. Kraemer (1948):* racially restrictive covenants (e.g., 25% of south Chicago properties) were at least transparent about their racism. Once struck down, they were replaced by **architecture and zoning** (highways, railroad tracks) that kept segregation going while it looked like "choice." The government "gets the benefit of what would clearly be an illegal and controversial regulation without even having to admit any regulation exists." Not all indirect regulation is improper (street lighting, speed bumps), and speed bumps do not hide where they came from. **The issue is transparency/publicity:** "The state has no right to hide its agenda."
- **Where this leads:** a reader's letter preferred "West Coast Code" (Silicon Valley) to "East Coast Code" (government) because programmers do not carry guns and badges. Lessig says the writer still sees the **real similarity**: private firms regulate their customers too. Government can regulate *indirectly by regulating code writers*, often avoiding political consequences. Two worries: a regime that makes **invisible** regulation easier (hard to resist bad regulation) and one that makes regulation **easier** in general (we do not yet understand the values at risk). The opening of Ch. 8 restates the key criticism: code-based regulation risks being **invisible**. People experience its controls "as nature," which may weaken democratic resolve.

**Key terms (Lessig)**
- **Regulation (Lessig's sense):** any constraint on behavior. It can also *enable* behavior.
- **Pathetic dot:** the regulated individual at the center of the four constraints.
- **Four modalities:** law (punishment), norms (stigma), market (price), architecture/code (physical or technical burdens).
- **Code:** the software and hardware that make up cyberspace; its architecture.
- **"Code is law"** (Lessig's phrase, discussed in the lecture): code regulates behavior in a way that works like law.
- **Plasticity:** the constraints are not fixed and can be changed, including by law.
- **Direct vs. indirect regulation:** law commanding behavior vs. law changing norms, markets, or architecture to change behavior.
- **Indirection / commandeering:** using another structure of constraint to achieve an end, which can misdirect responsibility.
- **Transparency / publicity:** the principle that state regulation should be visible and owned.
- **Laffer Curve for criminal law:** extreme sanctions that backfire by eroding the norms that would otherwise support the goal.
- **West Coast Code vs. East Coast Code:** private software code vs. government legal code.

**Ties to lectures:** L6 is built on this chapter (pathetic dot, four modalities, "code is law," Robert Moses). L3 previews Lessig's broad definition of regulation. L4 uses Lessig's case for cyberlaw against Easterbrook's "law of the horse." L5 calls Asimov's laws regulation through architecture. The lecture's AI applications (guardrails, content filters, investor and insurer pressure, employee activism) extend the chapter to AI. Lessig's transparency worry fits with the course's later themes of accountability (cf. Calo's barriers to accountability; UNESCO's transparency principle).

---

## 4. Glossary

| Term | Definition (with source) |
|---|---|
| **Ethics** | Systematic reflection on what is good, right, fair, or just. UNESCO calls it "a dynamic basis for the normative evaluation and guidance" of AI. It identifies values but lacks enforcement. (L3, UNESCO) |
| **Governance** | The broadest term: the policies, norms, laws, and institutions that shape how AI is built and deployed (*Oxford Handbook of AI Governance*). Not limited to government. (L3) |
| **Policy** | Deliberate processes through which institutions decide on collective problems and public priorities. Can include, but does not require, law. (L3, Calo) |
| **Law** | Legally binding rules enforced by a state: statutes, judicial decisions, formal requirements. (L3) |
| **Regulation (narrow)** | Agency rules that put broad laws into practice (e.g., EPA rules under the Clean Water Act). (L3) |
| **Regulation (Lessig)** | Any force that constrains behavior: law, norms, markets, architecture. (L3, L6, Lessig) |
| **Ethics washing** | Publicly embracing ethical principles while resisting binding accountability. (L5, cf. Calo) |
| **Consequentialism / utilitarianism** | Ethics judged by outcomes: maximize benefit, minimize harm. (L3) |
| **Deontology** | Ethics of duties, rules, and rights. Some acts are wrong whatever the outcome. (L3) |
| **Virtue ethics** | Ethics focused on the character and judgment of moral actors. (L3) |
| **Ubuntu** | African relational philosophy ("I am because we are"): interconnectedness, collective well-being, restorative approaches. (L3) |
| **Definitions as governance tools** | Choosing a definition decides what is covered, what escapes oversight, and which harms get attention. (L4) |
| **AI effect / "stops being AI"** | Once something works reliably, people stop calling it AI (OCR, spam filters, autocomplete). (L4) |
| **Lifecycle approach** | Governing AI across stages (data, design, training, deployment, procurement, monitoring, decommissioning) instead of by a fixed definition. (L4, UNESCO) |
| **Law of the horse** | Easterbrook's argument against technology-specific law: apply general legal principles instead. (L4) |
| **Emergence / social valence / embodiment** | Calo's (2015) features of robotics and AI that put pressure on existing law. (L4) |
| **Sociotechnical change** | Maas's proposed object of governance: the changing social world around a technology, not the technology itself. (L5) |
| **Regulatory rationales** | Market failure; health, safety, and environmental risk; risks to rights and values; social solidarity; democratic processes; integrity of governance. (L5) |
| **Collingridge dilemma** | Early on, control is easy but information is scarce. Later, information is available but control is hard. (L5) |
| **Pacing problem** | Law assumes static technology and institutions move slowly, so law lags technology (Marchant). (L5) |
| **Soft law** | Measures that set substantive expectations but are not directly enforceable by government. (L5) |
| **Asimov's Three (and Zeroth) Laws** | Fictional tiered robot rules. They show how hard it is to turn principles into operational rules. (L5) |
| **Pathetic dot** | Lessig's regulated subject, acted on by four constraints. (L6, Lessig) |
| **Four modalities** | Law (punishment), norms (stigma/approval), market (price), architecture/code (what is possible). (L6, Lessig) |
| **Code is law** | Software and hardware regulate behavior in a way that works like law. (L6, Lessig) |
| **Direct vs. indirect regulation** | Law commanding behavior vs. law changing another modality to steer behavior. (Lessig) |
| **Indirection** | Regulating through another modality in a way that can hide responsibility and reduce accountability. (Lessig) |
| **Do Artifacts Have Politics?** | Langdon Winner's essay on politics built into artifacts (e.g., Moses's bridges). (L6) |
| **DRM** | Digital rights management: a technical block on copying, i.e., architecture as copyright enforcement. (L6) |
| **AI (Calo)** | An umbrella set of techniques approximating aspects of human or animal cognition using machines. (Calo) |
| **Machine learning** | A system's capacity to improve its performance at a task over time. (Calo) |
| **Data parity problem** | A few firms control most data, which shapes competition, research, and AI's goals. (Calo) |
| **Pattern recognition problem** | AI's ability to "derive the intimate from the available." (Calo) |
| **Meaningful human control** | The contested standard for human involvement in lethal force decisions. (Calo) |
| **AI Policy Winter** | Barocas's warning that apocalypse talk could drain attention from real AI policy. (Calo) |
| **AI system life cycle / AI actor** | UNESCO's stages of an AI system, and anyone involved in at least one of them. (UNESCO) |
| **Proportionality and Do No Harm** | UNESCO principle: AI use limited to what is necessary for legitimate aims. No social scoring or mass surveillance. (UNESCO) |
| **Ethical Impact Assessment (EIA)** | UNESCO's structured assessment of AI benefits, risks, and rights impacts. (UNESCO) |
| **Regulatory sandbox** | A controlled setting for testing rules or systems before formal adoption. (UNESCO) |

---

## 5. Practice Questions (original, for self-study)

**Q1 (MC).** A city requires every vendor selling AI tools to its police department to submit bias audit results as a condition of the contract. Under Calo's roadmap, this is best described as:
A) Removing hurdles to accountability through trade secret reform
B) Using **procurement** to channel AI toward the public interest
C) Certification of AI as a licensed professional
D) An industry ethics code

**Answer: B.** Calo says government can shape AI "through what it decides to purchase" and can use contracts to require good practices, which can move the whole market. (A) is about laws like trade secrecy, the CFAA, and the DMCA that block outside scrutiny. *Source: Calo, Part II.F.2.*

**Q2 (Short answer).** Calo gives two reasons for preferring "policy" over "governance." Name them.

**Answer:** (1) Governance is **too flexible**: it is unclear what is governed and by whom. (2) Governance literature tends to assume authority will or should **devolve to non-state actors**, which **hands responsibility to industry** (as with ICANN and IETF), even though industry should not set public policy. *Explanation:* by contrast, policy allows for new laws without requiring them and stresses planning, finality, and public interest. *Source: Calo, Part I.C; L3.*

**Q3 (MC).** Krafft et al. (2020) found that policy documents, compared with AI researchers, were more likely to define AI in terms of:
A) Statistical optimization
B) Human-like thinking or behavior
C) Lifecycle stages
D) Specific applications like spam filtering

**Answer: B.** The lecture's point is that human-like definitions point toward hypothetical future systems and may pull attention away from present harms (content moderation, predictive policing) toward killer robots and superintelligence. *Source: L4.*

**Q4 (Short answer).** Explain the difference between the two halves of the Collingridge dilemma, and say how the EU AI Act shows *both* risks.

**Answer:** The **information problem**: early on, intervention is easy but we know little about long-term consequences. The **control problem**: once consequences are clear, the technology is entrenched and hard to change. The EU AI Act moved quickly to avoid being too late, but there are concerns it was **too early**, since it was negotiated before general-purpose generative AI took off (information problem). Even so, foundation models had already become embedded across sectors before it passed in 2023 (control problem). *Source: L5.*

**Q5 (MC).** Which statement best matches Calo's view of the claim that "law is too slow to keep up with technology"?
A) It is accurate and inevitable, so soft law is the only answer.
B) It is misguided. Some laws do go stale, but that is often political, and the better-grounded problem is government's **lack of technical expertise**.
C) It is accurate only for the U.S.
D) It is irrelevant because AI does not need new law.

**Answer: B.** Calo points to ECPA (1986) as a law that aged badly, but notes the FTC's technology-neutral "unfair and deceptive" standard keeps working. *Explanation:* contrast this with Marchant's pacing problem (L5), which emphasizes structural slowness and recommends soft law. Being able to compare the two views is a good test of understanding. *Source: Calo, Part II.F.1; L5.*

**Q6 (MC).** A city installs bright street lighting and redesigns a park to improve sightlines in order to reduce crime. In Lessig's terms, this is:
A) Direct regulation through law
B) Regulation through norms
C) Indirect regulation through **architecture**, and not the troubling kind
D) Market regulation

**Answer: C.** Lessig cites Katyal and Crime Prevention Through Environmental Design. He says a requirement that streets be well lit is an indirect regulation that "no one would think … improper," because its purpose is not hidden. His concern is with *non-transparent* indirection. *Source: Lessig Ch. 7.*

**Q7 (Short answer).** According to Lessig, why were racially restrictive covenants, though "awful," arguably *less* troubling on one dimension than the zoning and highway placement that replaced them after *Shelley v. Kraemer*?

**Answer:** The covenants were **transparent**: they openly stated their racist purpose and no one could pretend otherwise. The architectural replacements (highways without crossings, railroad tracks, zoning) kept segregation in place while hiding the link between regulation and result. Segregation then looked like individual "choice," so the government got the effect of an illegal regulation "without even having to admit any regulation exists." *Source: Lessig Ch. 7, "The Problems of Indirection."*

**Q8 (MC).** Tracey Meares's argument, as Lessig presents it, is that extremely harsh drug sentences:
A) Are the most efficient deterrent
B) Can **weaken the community social structures** whose norms would otherwise discourage drug use, an indirect effect that may outweigh the direct one
C) Raise drug prices and so reduce demand
D) Are unconstitutional under *New York v. United States*

**Answer: B.** Lessig calls this a "Laffer Curve for criminal law." The lesson is that modalities interact, and the net effect "cannot be deduced a priori." *Source: Lessig Ch. 7.*

**Q9 (Short answer).** UNESCO distinguishes "values" from "principles." What is the relationship, and why does it matter for operationalization?

**Answer:** Values are **motivating ideals** that inspire desirable behavior and are the **foundation** of principles (e.g., human rights and dignity, environmental flourishing, diversity and inclusiveness, peaceful and interconnected societies). Principles **unpack the values more concretely** (e.g., proportionality, transparency, human oversight) so they can be put into policy statements and actions. The policy areas then turn the principles into specific measures. This layered structure is UNESCO's way of moving from ethics to policy. *Source: UNESCO para. 10, para. 48; L5.*

**Q10 (MC).** Which is TRUE of the UNESCO Recommendation?
A) It gives a single, precise technical definition of AI.
B) It is binding on all Member States with sanctions for non-compliance.
C) It is applied by Member States on a **voluntary basis** and deliberately avoids a fixed definition of AI.
D) It addresses only governments, not private companies.

**Answer: C.** UNESCO says a single definition "would need to change over time." It asks States to apply the Recommendation voluntarily, and it gives guidance to all AI actors, including private ones. *Explanation:* the voluntary status illustrates the enforcement gap of principle-based approaches discussed by Calo and Mittelstadt. *Source: UNESCO Preamble & para. 2, 4; L4.*

**Q11 (Short answer).** Using Easterbrook and Lessig, explain the "law of the horse" debate. Then explain how Calo's 2015 framework adds to the case that AI may need special attention.

**Answer:** Easterbrook argued against technology-specific law. We do not create "horse law," we apply tort, property, and criminal law to situations involving horses, because general principles outlast changing technologies. Lessig agreed we do not need a new legal system for every technology, but argued some technologies change the underlying **architecture** of interaction, and that architecture itself regulates. So what matters is *what the technology changes*, and studying cyberlaw reveals how regulation works in general. Calo (2015) argues robotics and AI put pressure on law through **emergence** (hard-to-predict outcomes), **social valence** (people respond socially), and **embodiment** (physical action), all of which complicate responsibility. *Source: L4.*

**Q12 (MC).** Lyria Bennett Moses and Matthijs Maas both suggest that the real object of AI governance is:
A) The underlying algorithms
B) The **sociotechnical changes** AI creates (new risks, opportunities, concentrations of power, vulnerabilities)
C) Only market failures
D) The definition of intelligence

**Answer: B.** The electricity analogy: we regulate infrastructure, safety, and competition, not electricity as such. One consequence is that a precise definition of AI may not be needed if governance targets the changes. *Source: L5.*

**Q13 (Short answer).** Give two reasons, from the lecture's discussion of Mittelstadt, why AI ethics principles often work as aspirations rather than enforceable commitments.

**Answer:** (1) Principles are **abstract**. They name values but not how to implement them, who is responsible, or what happens when they are ignored. (2) AI development lacks the **institutional structures of professional ethics** found in medicine (licensing, fiduciary duties, accountability). Software engineering codes exist but **lack teeth**, partly because there is no licensure, and they are less grounded in practice. A third point the lecture adds: principles can **conflict** (e.g., transparency vs. security), so they must be balanced when turned into rules. *Source: L5.*

**Q14 (MC).** Calo labels the concentration of training data among a few firms a *privacy* issue mainly because:
A) Large datasets always contain personal data
B) Firms **invoke consumer privacy as a reason to refuse to share data**, so a privacy principle in an industry ethics code can shield a company from obligations to share
C) Differential privacy is impossible at scale
D) The Fourth Amendment governs private data

**Answer: B.** This is one reason Calo urges "a healthy dose of skepticism" toward industry ethics codes. He wants data parity *without* sacrificing privacy (e.g., through differential privacy and federated learning). *Source: Calo, Part II.D.2.*

**Q15 (Short answer).** In Asimov's laws, the lecture finds both a lesson about operationalizing principles and a link to Lessig. Explain both.

**Answer:** *Operationalization:* the laws are a **tiered priority system** meant to resolve conflicts between principles. Yet in "Runaround" (1942) a robot is paralyzed because it is unclear how strong an "order" (Second Law) must be to override self-preservation (Third Law). The later Zeroth Law (duty to humanity) "in theory" solved problems, but "in practice" no one could decide what it required. Even agreed principles become hard to apply once reduced to rules. *Lessig link:* the laws were not enforced by a state but **built into the robots' positronic brains**. That is regulation through **architecture/code**, not law. *Source: L5 (via Chesterman), L6.*

---

*End of Module 1 notes.*
