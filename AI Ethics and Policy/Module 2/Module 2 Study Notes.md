# Module 2 Study Notes: Approaches to AI Governance

*CU Boulder / Coursera, AI Ethics and Policy (Casey Fiesler)*

> **Scope and integrity note.** These are self-study notes. They summarize the seven Module 2 lecture transcripts and four readings and explain the concepts. They do **not** answer the lab notebook lecture prompts (Prompts 1-7), the reading activities, or the quiz, and they don't pick "best quotes." The practice questions in Section 6 are original and written only for review.
>
> **About names.** The lecture files are auto-generated transcripts, so several scholars' names are garbled. Where these notes add a likely correct spelling, it is marked *(likely ...)*. Check those against the slides or reading list before you cite them.

---

## 1. Module Overview

Module 1 argued that governance is broader than legislation. Module 2 looks at formal governance more concretely. It asks **who** makes AI policy, **what tools** they use, and **how they organize** those tools. The two main organizing logics are **risk-based** governance (the EU AI Act and the NIST AI RMF) and **rights-based** governance (the Blueprint for an AI Bill of Rights). The module then looks at what happens when these approaches meet across borders. It ends with the layer that makes rules real or hollow: **soft law and standards**, and **assurance** (audits and impact assessments).

**How the lectures connect:**

- **L07 Actors** (who): power in the governance ecosystem is uneven.
- **L08 Tools** (how): sticks, carrots and sermons; ex ante vs. ex post; every tool has failure modes.
- **L09 Risk-based** (a way to organize the toolbox): tiers decide which tool applies when.
- **L10 Rights-based** (a different starting question): what protections do people have? This lecture shows that risk and rights blur.
- **L11 Global challenges**: fragmentation, the Brussels effect, and who writes "global" rules.
- **L12 Soft law and standards**: non-binding governance and how it gets "teeth."
- **L13 Assurance**: how we check whether governance claims are true.

The Alanoca et al. taxonomy runs through the whole module. It supplies the comparison dimensions (technology vs. application, horizontal vs. sectoral, ex ante vs. ex post, enforcement, stakeholder participation) that the lectures keep coming back to.

---

## 2. Lecture Notes

### L07: Who Makes AI Policy?

**Key points**
- "AI should be regulated," but **by whom**? Possible actors include legislatures, agencies, courts, countries, states, cities, the UN, standards bodies, company review boards, professional associations, civil society, builders and the public.
- **Government is not one actor.** Legislatures pass statutes, define rights and obligations, ban uses and set penalties. Agencies issue rules and guidance, investigate and enforce, and adapt their existing authority. Courts interpret statutes, assign liability and decide disputes after harm occurs.
- **U.S. states:** with no comprehensive federal AI law, states are debating hundreds of AI bills. This creates "laboratories" for experimentation, but also a patchwork, uneven protection and compliance complexity.
- **Governments govern beyond lawmaking.** They fund research, build infrastructure, buy and use AI, write national strategies, support standards and convene experts. One 2021 paper describes four roles for the state: **promoter of innovation, guarantor against risks, facilitator/moderator among stakeholders, and enabler of societal engagement**.
- **Procurement as governance** (Johnson and colleagues, city procurement): most government AI comes from third-party vendors. That makes procurement officers, IT managers and vendor-review teams "frontline AI governors."
- **Global networks can exclude.** The UN *Governing AI for Humanity* report found that 7 countries (Canada, France, Germany, Italy, Japan, UK, US) belonged to all seven sampled non-UN initiatives. 118 countries, mostly in the Global South, belonged to none.
- **Participation is not power.** Global South actors can still challenge dominant structures and raise digital sovereignty, extractive labor and data practices. The *paradox of participation*: formal inclusion can coexist with structures that limit whose knowledge counts.
- **Standards bodies are hidden actors.** They define what "accurate enough" or "meaningful human oversight" means in practice. The Ada Lovelace Institute's report on the EU AI Act notes that civil society faces barriers to taking part: time, cost, technical complexity, opacity and industry dominance.
- **Companies are both governed and governing.** They make technical, release and access choices, sit on standards bodies, lobby and shape public narratives. Wei and colleagues describe **regulatory capture**, including agenda-setting, academic, cultural and media capture, and especially **epistemic capture** (shaping what counts as knowledge or evidence). Power can mean getting policymakers to ask *your* question.
- **Other actors:** civil society, researchers (audits, benchmarks), journalists, **tech workers** (for example, protests over military contracts or police facial recognition) and **affected communities**, who have experiential knowledge.

**Frameworks:** the governance ecosystem; roles of the state; the paradox of participation; regulatory and epistemic capture. The closing checklist asks: who created a proposal, with what authority, who influenced it, who was consulted or missing, who complies, who enforces, and who can change the outcome?

**Cited:** Alanoca et al. (taxonomy; asymmetrical stakeholder representation); Johnson et al. (city procurement); UN *Governing AI for Humanity*; Marie-Therese Png *(transcribed "Peng")*; Ada Lovelace Institute (inclusive AI governance); Wei et al. (regulatory capture); an unnamed 2021 policy-document analysis (roles of the state).

### L08: AI Policy Tools

**Key points**
- **Goal vs. tool.** Transparency is a goal. A disclosure mandate, a public incident database or a procurement preference are tools for reaching it, and each targets different actors with different incentives.
- **Sticks, carrots and sermons**, from a book on policy instruments: regulation, economic means and information. Governments can *force*, *pay or make pay*, or *persuade*. Examples: a facial recognition ban (stick), grants for privacy-preserving research (carrot), a voluntary risk framework (closer to a sermon).
- **Choosing a tool is political** (Linder and Peters). The choice depends on how policymakers perceive the available tools, their institutional setting, their professional background and the political context. Choosing guidance over a ban encodes assumptions about power, responsibility and the role of the state.
- **Task-specific vs. general-purpose AI.** A credit model or retinopathy detector has a defined task. A GPAI model can be adapted to tutoring, hiring, therapy or surveillance, so its risk often appears only downstream. The lecture cites "Lang and colleagues" here, and L09 cites "Wang and colleagues" for the same idea. The key question is what the system is being *used* to do.
- **Families of tools:**
  - *Information tools* (sermons): notice, labeling, documentation, transparency reports, registries, incident reporting. Notice is weak without a way to challenge the decision or get review.
  - *Permission tools*: bans, moratoria, licensing, pre-market approval, deployment conditions.
  - *Accountability tools*: fines, liability, lawsuits, complaints, injunctions, discipline. These kick in after harm.
  - *Incentive tools* (carrots): grants, subsidies, tax incentives, procurement and contract terms. These resemble Lessig's "market" modality.
  - *Soft law*: standards, frameworks, voluntary commitments, codes of conduct.
  - *Technical tools*: Lessig's "code as law."
- **Ex ante vs. ex post** (from Alanoca et al.): prevention before or at deployment vs. response after harm. Good governance needs both.
- **Soft law works in the shadow of hard law.** Customers, insurers, procurement, auditors, possible future regulation and courts give it force. Its failure mode is **ethics washing**.
- **Anti-regulatory AI** (a 2025 paper, building on Tim Wu's pushback against "code as law"): protective-sounding technologies such as PETs, bias constraints or alignment techniques can serve regulatory avoidance. Related failure modes: privacy washing and fair washing.
- **Strategic environment.** Firms may comply with the bare minimum or route around rules. The red-teaming-AI-policy paper calls this **behavior avoidance** (between legal avoidance and evasion). EU AI Act examples: narrow definitions, redesigning around benchmark requirements, "token humans" in the loop.

**Cited:** policy-instruments book (commonly known as *Carrots, Sticks & Sermons*, Bemelmans-Videc, Rist & Vedung; the lecture doesn't name it); Linder and Peters; Lang/Wang et al. (GPAI); Lessig; Tim Wu; the 2025 anti-regulatory AI paper; "You and colleagues" (red-teaming AI policy, transcribed name).

### L09: Risk-Based Approaches

**Key points**
- **Core question:** how risky is this system or use, and what level of oversight should follow? A playlist recommender, a hiring screen and medical triage shouldn't be governed the same way.
- **Regulatory triage:** scrutiny scales with the level and type of potential harm. Some uses are banned outright.
- **EU AI Act tiers:** unacceptable (ban), high (risk management, documentation, data governance, transparency, human oversight, accuracy and robustness, monitoring), limited/transparency (disclosure) and minimal (no special obligations). Risk-based logic is "a way of organizing the toolbox."
- **NIST AI RMF:** voluntary soft law. It bans nothing and creates no penalties or enforceable rights. Four functions: **Govern, Map, Measure, Manage**.
- **Colorado's AI law:** covers high-risk systems that make consequential decisions and targets algorithmic discrimination. It shows that laws keep changing after passage through implementation, amendments, contestation and enforcement timelines.
- **Where does the risk sit?** The same GPAI model has different stakes in a recipe tool than in medical advice, tutoring, hiring or benefits eligibility.
- **Three kinds of risk** ("Curie and colleagues"): **functional** (biased outputs, security holes, hallucinations, failures in high-stakes settings), **structural** (labor displacement, surveillance, disinformation, concentration of power) and **relational** (power and knowledge gaps between companies, regulators and communities).
- **Risk classification is political and ethical, not purely technical.** Grozdanovski and De Cooman *(likely spelling; transcribed "Groszynowski and de Koomen")* argue that many AI Act risks concern fundamental rights, which lack the statistical evidence base of physical safety risks. So the tiers reflect value judgments.
- **Martin Ebers** *(transcribed "Evers")*: the AI Act isn't always *truly* risk-based. A genuinely risk-based approach would be proportionate, evidence-based and flexible, and would weigh **benefits and the opportunity costs of not using AI**. Fiesler's caveat: speculative benefits don't erase real harms.
- **Risk and rights blur.** The AI Act is risk-based in architecture, but many of the risks it manages are rights risks. It is best seen as a risk framework that partly operationalizes rights.

**Cited:** EU AI Act overview; NIST AI RMF; Colorado AI Act; Curie et al.; Wang et al. (GPAI); Grozdanovski & De Cooman; Martin Ebers.

### L10: Rights-Based Approaches

**Key points**
- **Starting question:** what protections should people have when automated systems affect their lives? For a hiring example: are applicants protected from discrimination? Do they know AI is used? Can they understand and contest the decision? What recourse do they have?
- **Blueprint for an AI Bill of Rights** (White House OSTP, Biden administration, 2022): never law and non-binding. It came out shortly before ChatGPT's release, after a year of public input (listening sessions with impacted communities, researchers, civil society and industry). It has five principles, each with a technical companion that has no regulatory force.
- **The five principles:** Safe and Effective Systems; Algorithmic Discrimination Protections; Data Privacy; Notice and Explanation; Human Alternatives, Consideration, and Fallback.
- The Blueprint doesn't sort systems into tiers, but it still uses risk language (testing, risk identification, mitigation, monitoring, proportionality).
- **The EU AI Act puts rights at the heart of a risk framework** (a 2026 EU-funded paper). Rights act as **legal thresholds and procedural triggers**: they justify prohibitions, drive high-risk classification, trigger obligations, and require some deployers to run a **fundamental rights impact assessment (FRIA)** before use. UNESCO's recommendation similarly turns principles into policy recommendations.
- **A right can't implement itself.** Privacy needs tools such as minimization, limits on secondary use, consent rules, surveillance limits and remedies. Non-discrimination needs bias testing, audits, representative data, accessibility review, civil rights enforcement and reporting.
- **Contested concepts** (Andrew Selbst): fairness and privacy aren't variables that one measurement settles. Ask fairness for whom, in what context, against what baseline, with what trade-offs. Selbst also asks whether the *institution* is structured to recognize and respond to social harms.
- **"May and Sag"** (transcribed name): rights language in EU regulation can work **managerially**. It organizes administrative process, manages institutional risk and preserves regulatory stability. Invoking rights isn't the same as empowering people.
- **NYC Local Law 144** (automated employment decision tools): requires bias audits and published summaries. **Groves and colleagues** found narrow, ambiguous definitions; employers treating their tools as out of scope; auditors unable to get data; and no duty to stop using or fix a discriminatory tool. The result was visibility without accountability.
- **Synthesis:** risk-based governance helps prioritize. Rights-based governance keeps the focus on the person. Strong governance likely needs both. Questions to ask: who is protected, from what, who must act, what tool makes it real, who holds power, and is it enforceable or aspirational?

**Cited:** Blueprint for an AI Bill of Rights; a 2026 EU-funded paper on rights in the AI Act; UNESCO Recommendation; Andrew Selbst; "May and Sag"; Groves et al. (LL144).

### L11: Global AI Governance Challenges

**Key points**
- **AI is transnational.** Data, development, cloud hosting, fine-tuning, deployment and labor (data labeling, moderation, minerals, chips) are spread across jurisdictions. Harms cross borders too: misinformation, labor exploitation, surveillance, copyright and environmental costs.
- **"Apples to oranges"** (Alanoca et al.): regulations differ on many dimensions at once (technology vs. application, horizontal vs. sectoral, ex ante vs. ex post, maturity of the digital legal landscape).
- **EU:** a comprehensive, binding, risk-based AI Act that targets rights risks.
- **US:** fragmented. It relies on agencies, sectoral rules, state laws, voluntary frameworks, litigation and existing non-AI law, and it shifts between administrations. State examples: **Colorado** (high-risk AI and algorithmic discrimination), **California** (transparency on training data and frontier AI), **Illinois** (an early mover on AI in video interviews), **Utah** (targeted transparency and a sandbox). A 2026 paper calls this **polycentric governance**: multiple independent decision-makers at different scales.
- **China:** one of the most developed regimes. It has targeted rules on recommender algorithms, deep synthesis and generative AI, inside a broader regime of cybersecurity, data security, personal information, content and copyright law. The approach is centralized and state-centered (national security, information control, state capacity, plus industrial development). It is **vertical and iterative** rather than horizontal.
- **Shared words, different values.** Transparency can mean informing people so they can contest decisions, or making algorithms visible *to the state*. Agreeing that AI should be "fair" can hide sharp disagreement about what fairness requires.
- **Beyond the EU, US and China:** Brazil, India, Singapore, South Korea and Global South civil society. Governance is global in effect but not in authorship.
- **Capacity:** a 2026 paper on African AI strategies finds that the African Union's continental strategy frames AI as *shaping and applying* AI for local challenges (health, agriculture, transport, research, sustainable development). But pre-tertiary computing education often stresses digital literacy over the AI competencies those goals need. That is a gap between ambition and capacity.
- **Too many overlapping laws.** Laws define AI and classify risk differently and assign responsibility to different actors. The AI Act doesn't replace GDPR, copyright or product-safety law. In the U.S., a hiring tool may face different rules in NYC, Colorado and California.
- **The "regulatory game"** (Lancieri and colleagues, 2025): governments regulate; firms comply, withdraw or work around the rules; governments respond. Possible outcomes are coexisting local regimes, harmonization, the **Brussels effect**, or pure fragmentation. Fragmentation also allows **regulatory arbitrage**.
- **International efforts:** the OECD AI Principles, UNESCO's Recommendation, the G7 Hiroshima Process, the UN high-level advisory body, and the **Council of Europe Framework Convention on AI and Human Rights, Democracy and the Rule of Law**, often called the first binding international AI treaty. The treaty is broad, leaves detail to states, and focuses mainly on public authorities and private actors acting for them.
- **GDPR in 2018** is the Brussels-effect example: companies changed their privacy policies globally. Global governance can also **reproduce inequality** in data, labor, compute, energy and minerals.

**Cited:** Alanoca et al.; a 2026 paper on polycentric U.S. governance; a 2026 paper on African AI strategies; Lancieri et al. (2025); Bradford's Brussels effect (concept); Council of Europe Convention; OECD, UNESCO, G7, UN.

### L12: Soft Law and Standards

**Key points**
- **Hard law** is binding and backed by the state (statutes, regulations, court orders). **Soft law** creates expectations without direct enforceability: frameworks, standards, principles, codes of conduct, best practices, certifications, professional guidelines, public-private commitments. **Private governance** covers company and industry rules (internal RAI policies, ethics boards, pledges, model-release processes) and is covered more in a later module.
- **Why so much soft law?** The **pacing problem**: technology outruns law. Generative AI made parts of the AI Act look dated before it took effect. Soft law is faster, more flexible and draws more easily on technical expertise.
- **How soft law gets teeth:** procurement requirements (e.g., a city buys only from NIST-RMF-aligned vendors), contract clauses, certification, insurance, reputation (commitments become goalposts for journalists and civil society), and the **shadow of hard law**. Hagemann and colleagues (*Soft Law for Hard Problems*): the hard-law sword doesn't have to fall for soft law to shape behavior.
- **Standards translate principles.** "Transparent to whom, about what, when, in what format?" A 2025 piece distinguishes **technical standards** (safety, reliability, robustness, interoperability) from **ethical standards** (fairness, transparency, oversight, accountability). Standard-setting has broadened from technical robustness to include ethics.
- **Examples:** IEEE *Ethically Aligned Design*; the joint ISO/IEC trustworthy-AI standard; the OECD risk classification framework; IEEE's transparency standard for autonomous systems, which defines *levels* of transparency (from general principles of operation, to explanations of recent activity, to continuous user-adapted explanations).
- **"Shor and colleagues"** (transcribed name) studied designers using the IEEE transparency standard. Designers valued transparency but found it hard to implement and found the recommendations ill-fitted to their scenarios. The lesson is that standards bodies, developers and users need to engage more. A standard fails if people don't know it, understand it, have incentives to use it, or find it useful.
- NIST AI RMF is described as a "gold standard" for voluntary U.S. AI governance. It is a framework and best-practice guide, not a certification standard.
- **Critiques:** **ethics washing** (the appearance without the change); **proceduralism** (governance as a checklist: "we filled out the form," but did anything change?); and standards quietly encoding the priorities of whoever can afford to write them. The contrast is accountability vs. performance.
- **Bridge to L13:** standards define what good looks like. **Assurance** asks whether the organization actually did it.

**Cited:** Hagemann et al.; a 2025 piece on standards for human-centered AI; IEEE, ISO/IEC, OECD; Shor et al.

### L13: Assurances, Audits, and Impact Assessments

**Key points**
- **Assurance** covers processes that verify or support confidence in claims about a system, organization or practice: audits, impact assessments, documentation reviews, red-teaming reports, incident reporting. It applies to both soft and hard law.
- *AI Regulation Is Not All You Need*: legal requirements need operational practices to comply, test, document, monitor and govern across the lifecycle. Assurance moves governance from **claim to evidence**.
- **Defining an audit** (Birhane and colleagues; transcribed "Bearhan/Bierhein"): an **independent assessment of an identified audit target, evaluated against articulated expectations, with the objective of accountability**. **Deb Raji** puts audits at the intersection of evaluation and accountability, with the explicit goal of holding stakeholders accountable. Questions to ask: audited what, against what standard, by whom, with what consequence?
- Birhane et al. (2024) surveyed audits across academia, regulators, law firms, civil society, journalism, consultancies and companies. They call the landscape "muddled and imprecise," and only some audits lead to accountability outcomes.
- **Impact assessments** are broader and more anticipatory. **Selbst's definition of an AIA**: the developer anticipates, tests and investigates potential harms *before implementation*, documents the findings, and publicizes them or reports them to a regulator. As a tendency (not an absolute rule), audits evaluate against standards and impact assessments structure reflection and mitigation.
- **Stahl and colleagues (2023 systematic review):** impact assessments partly converge but disagree on content, structure and implementation. They work best as tools to stimulate reflection. Two goals: **early intervention** and **knowledge production** (documenting decisions, rationales, tests and trade-offs, which forces private information into existence).
- **Selbst's institutional critique:** assessments depend on the firm itself, so they get filtered through firm logics (liability avoidance, profit, routine, managerial compliance) and can become paperwork.
- **NYC LL144 revisited:** annual bias audit plus a public summary, including impact ratios. Groves et al. quote an auditor calling it a **"first pancake."** The problems: unclear definitions, narrow scope, limited data access, uncertainty over who counts as independent, and no required action by vendors. Audit mandates need a **theory of change** with enforceability. Visibility is not the same as accountability. Ask: *what happens if the results are bad?*
- **Internal vs. external auditors (Raji).** Internal auditors (in-house teams, contracted consultants) have **access without independence**. External auditors (regulators, journalists, academics) have **independence without access**. External auditors can represent non-users and affected people (in hiring, the customer is the employer but the affected party is the applicant). They rely on scraping, records requests, user reports, simulation, donated data and reverse engineering.
- **AI auditing is professionalizing** (a 2024 interview study): the field is new, diverse and lacks uniform standards. Auditors try to build trust, but little is known about how users perceive it. If audits are supposed to justify trust in AI, why should anyone trust the audit? Audits need their own standards, oversight, independence rules and consequences for poor quality.
- **What makes assurance meaningful:** clear scope, standards and expectations, independence, data access, stakeholder participation, public or regulatory visibility, and **consequences and remedies**.

**Cited:** *AI Regulation Is Not All You Need*; Birhane et al. (2024); Deb Raji; Andrew Selbst; Stahl et al. (2023); Groves et al. (LL144); a 2024 study of AI auditing professionals.

---

## 3. Reading Notes

### 3.1 Alanoca, Gur-Arieh, Zick & Klyman (2025), *Comparing Apples to Oranges: A Taxonomy for Navigating the Global Landscape of AI Regulation*

**Citation:** Sacha Alanoca, Shira Gur-Arieh, Tom Zick, and Kevin Klyman. 2025. In *Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT '25)*, Athens, Greece, pp. 914-937. https://doi.org/10.1145/3715275.3732059

**Central thesis.** AI governance has moved quickly from soft law to binding regulation, and "AI regulation" is now used loosely for very different things. That ambiguity misleads the public (a false sense of safety), fragments international cooperation, and raises the risk of **regulatory capture** because affected stakeholders can't follow the process. The authors propose a **taxonomy of binding AI regulation** that allows systematic comparison across jurisdictions and over time. Their aim is that it outlasts political change.

**Structure.**
1. Introduction. The opening context: Biden's EO 14110 revoked on day one of the second Trump administration, South Korea's AI Basic Act, and the EU's withdrawal of its AI Liability Directive.
2. "Beyond Regulatory Fragmentation": defines AI regulation and separates soft from hard law.
3. Related work. Prior work falls into three groups: descriptive trackers (OECD.AI, G'sell), comparative legal analyses (Halim & Gasser; Lévesque) and conceptual frameworks (CEIMIA's seven categories, which blur hard and soft law).
4. Methodology. Document collection, interviews with regulators and experts, iterative coding, and visualization built with designers.
5. Taxonomy criteria and limitations.
6. Analysis of five early movers.
7. Conclusion. Appendix tables encode each jurisdiction.

**Three motivating problems** (Introduction):
1. **Semantic ambiguity.** The UK's "pro-innovation approach to AI regulation," which has no binding requirements, and the EU AI Act, which is horizontal and risk-based with fines, both get called "AI regulation."
2. **Divergent strategies.** China and the U.S. lean technology-based. The EU, Canada and Brazil take a hybrid approach covering both applications and technology. This threatens **legal interoperability**.
3. **Opacity deters participation**, especially by civil society, which increases capture risk.

**Selection criteria.** The authors included only **binding, government-led** instruments with regulatory significance and maturity, diverse approaches and global influence. They distinguish *regulation* (concrete, enforceable rules implementing a law) from *policy* (intent and guiding principles). The five cases: the **EU AI Act**; **U.S. EO 14110** (included because of binding elements, notably compute reporting for frontier models); **Canada's AIDA**; **China's Interim Measures for Generative AI Services**; **Brazil's AI Bill 2338/2023**.

**Taxonomy design principles:** key legislative elements, commonality across documents, **measurability** (little discretion) and expert validation.

**The taxonomy's dimensions.** The text lists eleven metrics:

| Metric | What it captures |
|---|---|
| a. **Status** | Has the legislation been formally adopted? |
| b. **Novelty** | A new AI-specific law, or existing law adapted to AI? |
| c. **Maturity of the digital legal landscape** | How developed the surrounding digital and AI-adjacent law is (data protection, content moderation, etc.) |
| d. **Reach** | Who is targeted: industry, government agencies, individuals |
| e. **Enforcement** | Continued reporting; third-party audits; existing vs. new agency; liability; regulatory sandboxes |
| f. **Sanctions** | Criminal charges; fines; temporary injunctions |
| g. **Operationalization** | Standard setting; auditing; in-house technical expertise |
| h. **International cooperation** | Alignment with global frameworks (e.g., OECD principles) |
| i. **Stakeholder consultation** | Inclusion of civil society; inclusion of the private sector |
| j. **Regulatory approach** | **Ex ante** (preventive, e.g., pre-market approval) vs. **ex post** (after deployment, remedies, lawsuits) |
| k. **Regulation layer / focus** | **Technology-focused** (e.g., dual-use foundation models) vs. **application-focused** (e.g., social scoring) |

The abstract highlights six of these: technology vs. application focus, horizontal vs. sectoral coverage, ex ante vs. ex post, maturity, enforcement mechanisms and stakeholder participation. **Horizontal vs. vertical (sectoral)** coverage is analyzed in §6.3 rather than listed as its own metric.

**Key findings (Section 6):**
- **Stages of development.** The EU, U.S. and China had adopted frameworks. Brazil's bill had passed the Senate and was before the Chamber of Deputies. Canada's AIDA risked being permanently stalled (later described as stalled; EO 14110 was revoked). **Soft law came first everywhere**: China's Ethical Norms (2021) came before its GenAI measures (2023); the U.S. Blueprint (2022) came before EO 14110 (2023); the EU's Ethics Guidelines for Trustworthy AI (2019) came before the AI Act. Three reasons timelines differ: legislative depth (the AI Act's comprehensiveness takes long negotiation), the instrument type (executive orders skip legislatures), and centralization (China's CAC, a "cyber super-regulator," can act fast).
- **Maturity.** The EU and China are the most mature (EU: GDPR, DSA/DMA, Copyright Directive, Cyber Resilience Act, Product Liability Directive; China: algorithm-recommendation provisions 2021, deep synthesis 2022, GenAI measures 2023, PIPL). Brazil and Canada are in the middle (LGPD and the Internet Bill of Rights; PIPEDA and the Directive on Automated Decision-Making). The U.S. is at the low end federally, with a sectoral patchwork of privacy law (the paper cites the Children and Teens' Online Privacy Protection Act, GLBA and HIPAA), and the Blueprint and NIST RMF remain soft law.
- **Horizontal vs. vertical.** The EU, Canada and Brazil are mostly **horizontal**, with tiers based on **risk** (EU, Brazil) or **impact** (Canada). The U.S. is **vertical**: agencies extend sectoral law (DOJ/EEOC guidance on AI and the ADA; FTC on the FCRA). China sits in the middle: technology-specific rules issued by the CAC under broader statutes. No regime is pure. Horizontal regimes give unified, broad protection but less flexibility. Sectoral regimes adapt better but enforce less consistently.
- **Ex ante vs. ex post** (drawing on **Margot Kaminski**, *Regulating the Risks of AI*). Ex ante tools include impact assessments, licensing and pre-market checks, like chemicals or pharmaceuticals. Ex post tools are tort, product liability and consumer protection, which require proving causation and fault, and AI's opacity makes that hard. The EU emphasizes ex ante (conformity assessments). Brazil and Canada lean ex ante. The U.S. traditionally leans ex post (FTC, lawsuits, states), although EO 14110 added ex ante features for high-compute models. China is centralized ex ante (model registration, security assessments before release) with ex post penalties.
- **Technology vs. application.** The U.S. EO treats dual-use foundation models above a 10^26 training-compute threshold as inherently risky and subject to reporting. China targets GenAI and deep synthesis. The EU began application-level in its April 2021 draft. Generative AI arrived during the late-2022 trilogues and prompted added GPAI rules (documentation of energy use, training data and copyright policy), making the Act a **hybrid**. Canada and Brazil followed. The authors argue the two layers are complementary.
- **Enforcement models.** Centralized: the EU (AI Office), Canada (a proposed AI and Data Commissioner) and, at the extreme, China (CAC). Decentralized: the U.S. (AISI at NIST, operationalizing the RMF without binding authority) and Brazil (SIA, coordinated by data protection authority ANPD). The authors favor a **hybrid**: central coordination with decentralized execution.
- **Stakeholder participation** is the most opaque dimension. Representation of public and private stakeholders is asymmetrical, and civil society input is limited in drafting *and* in implementation, including at standards bodies (CEN, CENELEC, ETSI). Examples: of the **253 stakeholders consulted on Canada's AIDA, 216 were from business** (Clement 2023), despite Canada's civic tradition (the 2017 Montréal Declaration). In Brazil, **Google was accused of manipulating public opinion by promoting search entries that criticized Bill 2630**, an online-disinformation bill, during debates over Brazil's digital legislation. Capture risks include keeping systems out of "high-risk," setting compute thresholds just above current models, and convenient interpretations during standardization. Remedies: publish the composition of stakeholder input, fund civil society to build technical capacity, and pay for participation time.

**Appendix details worth knowing.** EU AI Act fines: up to **€35M or 7% of worldwide turnover** for prohibited practices; GPAI providers up to **3% or €15M**. Every Member State must set up at least one **regulatory sandbox** (Art. 57). The AI Office sits within DG CNECT. AIDA would create three criminal offences. Brazil's fines go up to BRL 50M or 2% of turnover. China's measures require a **safety assessment before a license**.

**Conclusion.** Not every "AI regulation" is equivalent. The EU AI Act and Brazil's bill stand out as comprehensive hybrids with both ex ante and ex post requirements and stronger civil society participation. The paper also challenges the narrative that **innovation and regulation are mutually exclusive**: China combines strict rules with frontier development (e.g., DeepSeek), even if its motives differ (e.g., censorship).

**Ties to lectures:** this paper supplies the module's comparison vocabulary. L07 uses its stakeholder and asymmetry point; L08 its ex ante/ex post distinction; L11 its "apples to oranges" framing and China's maturity. Its point about mislabeling soft law as hard law connects to L12's ethics-washing critique.

---

### 3.2 NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* (NIST AI 100-1, January 2023)

**Citation:** National Institute of Standards and Technology. 2023. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.100-1

**Central thesis.** AI risks differ from traditional software risks. They are **socio-technical**, emerging from technical features combined with social context, use and human behavior. Organizations need a flexible, voluntary, structured way to manage them that is integrated with enterprise risk management, so that AI becomes trustworthy and public trust follows.

**Nature and mandate.** The framework was directed by the **National AI Initiative Act of 2020**. It is intended to be **voluntary, rights-preserving, non-sector-specific and use-case agnostic**. It was developed through an RFI, three workshops, comments on a concept paper and two drafts. It is a **living document**, with formal review expected no later than 2028, and is accompanied by the online **AI RMF Playbook**. It uses the OECD/ISO definition of an AI system: an engineered or machine-based system that, for given objectives, generates outputs (predictions, recommendations, decisions) influencing real or virtual environments, with varying autonomy.

**Structure.**
- **Part 1, Foundational Information:** framing risk, challenges, audience, trustworthiness characteristics, and effectiveness.
- **Part 2, Core and Profiles:** the four functions with their categories and subcategories, plus profiles.
- **Appendices:** A (AI actor tasks), B (how AI risk differs from software risk), C (human-AI interaction), D (attributes of the RMF).

**Framing risk.**
- **Risk** is a composite of an event's *probability* and the *magnitude* of its consequences. Impacts can be positive or negative (adapted from ISO 31000).
- **Challenges:**
  - **Risk measurement**: third-party software, hardware and data; emergent risks; lack of reliable metrics, which can be gamed or oversimplified; lifecycle stage; lab vs. real world; inscrutability; human baselines.
  - **Risk tolerance**: the RMF doesn't prescribe it. It is contextual and set by law, norms and organizations.
  - **Risk prioritization**: eliminating all risk is counterproductive. Where risk is unacceptable (imminent significant impacts, severe harms occurring, catastrophic risk), development and deployment should **cease in a safe manner**. Human-facing systems and systems trained on sensitive data warrant higher initial priority.
  - **Organizational integration**: AI risk belongs inside enterprise risk management alongside cybersecurity and privacy. The RMF alone won't change incentives without senior-level commitment.
- **Residual risk** is the risk remaining after treatment. It should be documented.

**Audience.** **AI actors** across the lifecycle (an OECD term). Figure 2 adapts the OECD classification framework with the dimensions *Application Context, Data & Input, AI Model, Task & Output*, with **People & Planet** at the center and **TEVV** (test, evaluation, verification and validation) emphasized throughout. The People & Planet actors (civil society, standards organizations, researchers, affected communities) form a separate audience that *informs* the primary one.

**The seven trustworthiness characteristics (§3):**

| Characteristic | Key idea |
|---|---|
| **Valid and reliable** | The **base** and a necessary condition. Validation confirms requirements for the intended use; reliability means performing as required over time; includes accuracy and robustness (generalizability), which can be in tension |
| **Safe** | Doesn't endanger human life, health, property or the environment under defined conditions; build safety in early; ability to shut down or intervene |
| **Secure and resilient** | Withstands adverse events and degrades gracefully; resists adversarial examples, data poisoning and model or data exfiltration; security includes resilience plus protection protocols |
| **Accountable and transparent** | Drawn as a **vertical box spanning all the others**. "Accountability presupposes transparency." Transparency means information is available, tailored to the person's role; a transparent system isn't necessarily accurate or fair |
| **Explainable and interpretable** | Explainability = *how* (mechanisms); interpretability = *why* (meaning in context); transparency = *what happened* |
| **Privacy-enhanced** | Safeguards autonomy, identity and dignity; PETs, de-identification and aggregation; can trade off against accuracy |
| **Fair, with harmful bias managed** | Fairness is culturally variable. Three bias categories: **systemic, computational/statistical, human-cognitive**, each possible without discriminatory intent. Mitigating bias doesn't guarantee fairness |

Trade-offs are inevitable: interpretability vs. privacy, accuracy vs. interpretability, privacy vs. accuracy under data sparsity. They should be resolved transparently and justifiably. Trustworthiness is "only as strong as its weakest characteristics."

**The Core: four functions (§5).** The actions **are not a checklist** and not necessarily ordered. Most users start with GOVERN, then MAP, then MEASURE or MANAGE, and iterate.

| Function | Purpose | Categories |
|---|---|---|
| **GOVERN** (cross-cutting, infused throughout) | Build a risk-management culture; policies; accountability; link technical work to organizational values | G1 policies and processes (incl. legal requirements, inventories of AI systems, decommissioning); G2 accountability structures (roles, training, executive responsibility); G3 workforce diversity, equity, inclusion, accessibility; G4 a culture that considers and communicates risk (safety-first mindset, incident identification); G5 engagement with relevant AI actors (external feedback); G6 third-party software, data and supply-chain risks |
| **MAP** | Establish **context** to frame risks; leads to an initial **go/no-go** decision | M1 context established (purposes, laws, norms, risk tolerance, requirements); M2 system categorized; M3 capabilities, usage, benefits and costs vs. benchmarks; M4 risks and benefits mapped for all components, incl. third parties; M5 impacts on individuals, groups, communities, organizations and society characterized |
| **MEASURE** | Quantitative, qualitative or mixed methods to analyze, benchmark and monitor risk; test before and during deployment | ME1 methods and metrics (document what *can't* be measured; independent assessors); ME2 evaluation for each trustworthiness characteristic (2.1-2.13, incl. environmental impact and TEVV effectiveness); ME3 tracking risks over time (incl. hard-to-measure risks; feedback and appeal channels); ME4 feedback on whether measurement works |
| **MANAGE** | Allocate resources to mapped and measured risks; respond, recover, communicate | MA1 prioritize and respond (go or no-go; responses = **mitigate, transfer, avoid, accept**; document residual risk); MA2 maximize benefits and minimize harms (consider **non-AI alternatives**; mechanisms to **supersede, disengage, deactivate**); MA3 third-party risks (incl. pre-trained models); MA4 post-deployment monitoring, appeal and override, incident response, communication to affected communities |

**Profiles (§6).**
- **Use-case profiles**: e.g., a hiring profile or a fair housing profile.
- **Temporal profiles**: a *Current* profile vs. a *Target* profile; the gap drives action plans.
- **Cross-sectoral profiles**: e.g., LLMs, cloud services, acquisition.
- No templates are prescribed.

**Appendix B, risks that are new or heightened compared with traditional software:**
- data that is unrepresentative, or lacks ground truth
- drift, and the frequent maintenance it requires
- scale and complexity
- pre-trained models: statistical uncertainty, reproducibility problems
- emergent failure modes
- privacy risk from data aggregation
- opacity
- immature testing standards
- environmental costs

Existing frameworks don't adequately cover harmful bias, generative AI, ML-specific attacks (evasion, model extraction, membership inference) or third-party and off-label use.

**Appendix C, human-AI interaction.** Human roles must be clearly defined. Human-AI configurations range from fully autonomous to fully manual. AI can *amplify* human bias. Presenting information to people is complex. More research is needed on whether humans are empowered to challenge AI output, and data on override rates is useful.

**Appendix D, attributes.** The RMF aims to be risk-based, resource-efficient, **pro-innovation** and voluntary; consensus-driven; written in plain language; a common language; easy to use alongside other risk management; universally applicable; **outcome-focused and non-prescriptive**; built on existing standards; **law- and regulation-agnostic**; and a living document.

**Ties to lectures.** L09 uses it as the soft-law counterpart to the binding AI Act; both use risk language but work very differently. L12 calls it a "gold standard" of voluntary governance that gets teeth through procurement and contracts. The RMF itself admits that using the framework alone won't create incentives, which is the ethics-washing and proceduralism concern from L12. Alanoca et al. classify it as U.S. soft law, operationalized through NIST's AISI.

---

### 3.3 European Commission, *AI Act* overview page ("Shaping Europe's digital future")

**Citation:** European Commission. *AI Act* (policy overview of Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence). Page last updated 19 October 2026.

**Central thesis.** The AI Act is described as **the first comprehensive legal framework on AI worldwide**. It sets **risk-based** rules for AI developers and deployers so that Europeans can trust AI, protecting safety, fundamental rights and human-centric AI while supporting uptake, investment and innovation. It is part of a broader package that includes the AI Continent Action Plan, the AI Innovation Package and AI Factories. A voluntary **AI Pact** and an **AI Act Service Desk** support the transition.

**Why rules?** Most AI poses limited or no risk, but some systems create risks. Opacity can make it impossible to tell whether someone was unfairly disadvantaged, for example in hiring or a public benefit application. Existing law is insufficient.

**The four risk tiers:**

| Tier | Rule | Examples from the page |
|---|---|---|
| **Unacceptable risk** | **Banned**: "a clear threat to the safety, livelihoods and rights of people." Nine prohibited practices | (1) harmful AI manipulation and deception; (2) harmful exploitation of vulnerabilities; (3) **social scoring**; (4) individual criminal-offence risk assessment or prediction; (5) **untargeted scraping** of the internet or CCTV to build facial-recognition databases; (6) **emotion recognition in workplaces and education**; (7) biometric categorisation to deduce protected characteristics; (8) **real-time remote biometric identification for law enforcement in publicly accessible spaces**; (9) AI generating non-consensual intimate content or CSAM (e.g., "nudification" apps) |
| **High risk** | Allowed, but with **strict obligations before market entry** | Safety components in critical infrastructure (transport); **education** (exam scoring); product safety components (robot-assisted surgery); **employment** (CV-sorting); essential private and public services (**credit scoring**); remote biometric ID, emotion recognition and biometric categorisation (e.g., retroactively identifying a shoplifter); law enforcement (evaluating the reliability of evidence); **migration, asylum, border** (visa application examination); administration of justice and democratic processes (preparing court rulings) |
| **Transparency risk** (the lecture calls it "limited risk") | **Disclosure obligations** | People must know they're talking to a **chatbot**; GenAI output must be **identifiable**; **deepfakes** and AI text published to inform the public on matters of public interest must be clearly labelled |
| **Minimal or no risk** | **No new rules**; covers the vast majority of AI in the EU | AI-enabled video games, spam filters |

**High-risk obligations** (before market placement):
1. adequate risk assessment and mitigation
2. high-quality datasets to minimize discriminatory outcomes
3. activity **logging** for traceability
4. detailed **documentation** for authorities
5. clear information to deployers
6. appropriate **human oversight**
7. a high level of **robustness, cybersecurity and accuracy**

After market entry, authorities run **market surveillance**, deployers ensure human oversight and monitoring, providers keep **post-market monitoring**, and both providers and deployers report **serious incidents** and malfunctions.

**General-purpose AI (GPAI).** GPAI models perform a wide range of tasks and underlie many systems. Very capable or widely used models may carry **systemic risks**. All GPAI providers have rules on **transparency and copyright**. Providers of systemic-risk models must **assess and mitigate** those risks. The GPAI rules took effect in **August 2025**. Supporting instruments from July 2025:
- **Guidelines** on the scope of GPAI obligations
- the **GPAI Code of Practice**: *voluntary*, drafted by independent experts, covering transparency, copyright, and safety and security
- a **Template for the public summary of training content**: data sources, including large datasets and top domain names, plus processing information

The page also lists a voluntary **Code of Practice on Marking and Labelling of AI-generated Content** (with disclosure icons) and **Guidelines on transparency obligations**.

**Governance and enforcement.** From **2 August 2026**, the **AI Office** and Member State authorities implement, supervise and enforce the Act. The AI Office holds **enforcement powers over GPAI models**: it can request documentation, evaluate models, require corrections and fine. Advisory bodies are the **AI Board, the Scientific Panel and the Advisory Forum**. The page also mentions a July 2026 Cybersecurity and AI action plan, a planned EU model-evaluation capacity (targeted for 2027), a whistleblower tool and a complaints tool.

**Timeline:**

| Date | Milestone |
|---|---|
| 1 Aug 2024 | Entered into force |
| 2 Feb 2025 | Prohibited practices (1-8) and **AI literacy** obligations apply |
| 2 Aug 2025 | Governance rules and **GPAI obligations** apply |
| 19 Nov 2025 | "AI Omnibus" simplification proposal adopted (political agreement 7 May 2026; in force 27 July 2026) |
| 2 Aug 2026 | Act generally applicable; transparency rules; AI Office and national enforcement |
| Dec 2026 | Prohibition 9 (non-consensual intimate content and CSAM generation) takes effect (added by the Omnibus) |
| **2 Dec 2027** | High-risk rules for **Annex III** sensitive areas (biometrics, critical infrastructure, education, employment, migration, asylum, border control) |
| **2 Aug 2028** | High-risk rules for AI in **Annex I** regulated products (e.g., lifts, toys) |

**AI Omnibus amendments.** The Omnibus added the nudification and CSAM ban. It strengthened the AI Office and centralized oversight of systems built on GPAI models. It extended simplified rules (e.g., technical documentation) from SMEs to small mid-caps. It widened access to **regulatory sandboxes**, including an EU-level one, and clarified how the Act interacts with product-safety law such as the Machinery Regulation. The stated reason for delaying high-risk rules is that they should apply once support tools such as **harmonised standards** exist. The first harmonised standard was published on 19 Oct 2026.

**Ties to lectures.** L09's main example of risk-based governance (tiers determine which tool applies). L10 shows rights acting as thresholds and triggers, e.g., banned practices and FRIAs (the FRIA comes from the lecture, not this page). L08: GPAI breaks task-specific assumptions, which is why the Act added GPAI rules. L12: the delays tied to standards, and voluntary codes of practice, show soft law operationalizing hard law. L07: the standards bodies that write these standards are the "hidden actors." Alanoca et al. describe the Act as horizontal, mainly ex ante and hybrid (application plus technology). Watch the naming difference: the lecture says "limited risk" and the current page says "transparency risk."

---

### 3.4 White House OSTP (2022), *Blueprint for an AI Bill of Rights: Making Automated Systems Work for the American People*

**Citation:** White House Office of Science and Technology Policy. October 2022. *Blueprint for an AI Bill of Rights: Making Automated Systems Work for the American People*. Washington, DC.

**Assigned portion:** the introduction (Foreword, About this Framework, Listening to the American Public, the five principles, Applying the Blueprint, Definitions) plus one principle section of the Technical Companion. These notes summarize all five principles. To respect the reading activity, they don't select quotes or answer the prompt about your chosen section.

**Central thesis.** Automated systems bring great benefits, but they are too often used to **limit opportunities and access to critical resources**: unsafe patient-care systems, biased hiring and credit algorithms, unchecked data collection. These harms "are not inevitable." Five principles should guide the **design, use and deployment** of automated systems so they protect **civil rights, civil liberties, privacy and democratic values**. The document is a national, **sector-agnostic** values statement and toolkit.

**Legal status.** It is a **non-binding white paper** and "does not constitute U.S. government policy." It creates no enforceable rights, doesn't direct how statutes are interpreted, and doesn't limit lawful law-enforcement, national-security or intelligence activity. It acknowledges that some contexts, such as law enforcement and national security, may need adjusted or alternative safeguards.

**Process.** A year-long engagement:
- **six panel discussions**: consumer rights; criminal justice; equal opportunities and civil justice; AI and democratic values; social welfare and development; healthcare
- public **listening sessions** (two sessions on the biometrics RFI drew more than 300 participants)
- meetings with private-sector and civil-society stakeholders
- a **Request for Information on biometric technologies** (130 responses)
- a public email address

**Scope: a two-part test.** The Blueprint applies to (1) **automated systems** that (2) have the potential to **meaningfully impact the public's rights, opportunities, or access to critical resources or services**:
- **Rights**: civil rights, civil liberties and privacy (speech, voting, protection from discrimination, excessive punishment, unlawful surveillance).
- **Opportunities**: equitable access to education, housing, credit, employment.
- **Access**: healthcare, financial services, safety, social services, non-deceptive information, government benefits.

The test is technology-neutral on purpose, because harms can come from unsophisticated tools too. Measures should be **proportionate** to the extent and nature of the harm. The five principles are designed as **overlapping backstops**.

**The five principles (summaries):**

1. **Safe and Effective Systems.** "You should be protected from unsafe or ineffective systems." Practices:
   - consultation with diverse communities, stakeholders and domain experts
   - **pre-deployment testing**, risk identification and mitigation, and **ongoing monitoring** against the intended use and domain standards
   - outcomes that include the **possibility of not deploying or removing** a system
   - protection from foreseeable unintended uses and from inappropriate or irrelevant data use and its compounded reuse
   - **independent evaluation** with public reporting where possible

   *Companion examples:* a proprietary **sepsis-prediction model** that underperformed its claims and caused alert fatigue; automated moderation silencing Black users' counter-speech; item trackers misused for stalking; a **predictive policing feedback loop**; AI "nudification" apps; delivery-van AI cameras wrongly penalizing drivers. *Into practice:* EO 13960 (nine principles for federal AI), NHTSA as a model of safety regulation that coexists with innovation, the NIST AI RMF (then forthcoming), and **Idaho's 2019 pretrial risk assessment law** (must be shown free of bias, records open to inspection, no trade-secret shield in criminal discovery).

2. **Algorithmic Discrimination Protections.** "You should not face discrimination by algorithms and systems should be used and designed in an equitable way." **Algorithmic discrimination** means automated systems contributing to *unjustified* different treatment or impacts disfavoring people on a protected basis. Practices:
   - proactive **equity assessments** in design
   - **representative data** and guarding against **proxies**
   - **accessibility** for people with disabilities
   - pre-deployment and ongoing **disparity testing and mitigation**
   - organizational oversight
   - an independent, plain-language, public **algorithmic impact assessment**

   *Examples:* loan pricing that charged HBCU attendees more; a hiring tool that penalized résumés containing "women's"; a dropout-prediction model that used race directly; disparities in a federal recidivism tool; a sentiment analyzer biased against Jews and gay people; a healthcare algorithm that used cost as a proxy for need and underrated Black patients; remote proctoring flagging disabled students. *Into practice:* the DOJ redlining initiative, EEOC/DOJ guidance on AI and the ADA, a fix to the healthcare cost-proxy algorithm, industry's Algorithmic Bias Safeguards for the Workforce, Section 508 and WCAG, NIST SP 1270.

3. **Data Privacy.** "You should be protected from abusive data practices via built-in protections and you should have agency over how data about you is used." Practices:
   - **privacy by design and by default**; collect only data **strictly necessary** for the context
   - meaningful, brief, plain-language **consent**; no **dark patterns**; reform of notice-and-choice
   - **enhanced protections in sensitive domains** (health, work, education, criminal justice, finance, youth data)
   - freedom from **unchecked surveillance**: heightened oversight, and **no continuous surveillance** in education, work or housing where it limits rights
   - reporting that confirms your data decisions were respected

   The Blueprint calls privacy "foundational and cross-cutting." *Examples:* insurers using social media; a data-broker breach; facial recognition at public housing; employers surveilling union activity; CPAP data sent to insurers; the retailer that inferred a teen's pregnancy; location data revealing abortion-clinic visits. *Into practice:* the Privacy Act of 1974, the NIST Privacy Framework, New York's moratorium on biometrics in schools (after Lockport), labor-surveillance cost reporting, smartphone permission design.

4. **Notice and Explanation.** "You should know that an automated system is being used and understand how and why it contributes to outcomes that impact you." Practices:
   - accessible plain-language documentation; name the **responsible entity**
   - timely, up-to-date notice, including of significant changes
   - explanations that are **technically valid, meaningful, and calibrated to the level of risk**, even when the system isn't the sole input; in high-risk settings, fully transparent models
   - public reporting on the quality of notices

   *Examples:* an older disabled client cut off from Medicaid home care by an undisclosed algorithm; an algorithmic child-welfare risk assessment applied without notice; a gun-violence watch list with no explanation; a benefits system that changed its criteria invisibly. *Into practice:* Illinois BIPA, FCRA/ECOA "adverse action" notices (the CFPB says complexity doesn't excuse explanation), the California warehouse quota-notice law, NIST and DARPA explainable-AI research.

5. **Human Alternatives, Consideration, and Fallback.** "You should be able to opt out, where appropriate, and have access to a person who can quickly consider and remedy problems you encounter." Practices:
   - opt out to a human alternative where appropriate
   - timely human **fallback and escalation** when the system fails, errs, or you want to appeal
   - fallback that is accessible, equitable, effective, maintained, backed by operator training (including against **automation bias**) and not unreasonably burdensome
   - in sensitive domains (criminal justice, employment, education, health): human consideration before adverse or high-risk decisions, and meaningful oversight access
   - public reporting on timeliness and effectiveness

   *Examples:* signature-matching for mail ballots failing for some voters, which human **ballot curing** fixes; Colorado unemployment benefits requiring a smartphone; a fraud system seizing wages without review; a patient denied pain medication because her record was confused with her dog's; workers fired by automated HR. *Into practice:* healthcare Navigators, chatbots that escalate to humans, ballot-curing laws in at least 24 states.

**Key definitions** (from "Applying the Blueprint"):
- **Automated system**: any system, software or process that uses computation to determine outcomes, make or aid decisions, inform policy implementation, collect data, or interact with people. *Excludes passive computing infrastructure* (hosting, networking, storage, cybersecurity).
- **Communities**: neighborhoods, social networks, families, affinity groups, organizational ties, Indigenous communities. Harms should be evaluated and redressed at **both individual and community levels**.
- **Equity**: consistent, systematic, fair, just and impartial treatment, attentive to underserved communities.
- **Sensitive data and sensitive domains**: domains where activity can cause material harm to rights, autonomy and dignity (health, family planning, employment, education, criminal justice, finance). Youth data is always sensitive.
- **Surveillance technology**; **underserved communities**.

**Relationship to existing law.** Some protections are already constitutional or statutory (civil rights law, medical-device rules). Others would need new laws or policies. The Blueprint is consistent with the OECD 2019 AI Recommendation, EO 13960 and EO 13985 (racial equity), and draws on the **Fair Information Practice Principles (FIPPs)** from the 1973 HEW report *Records, Computers, and the Rights of Citizens*.

**Ties to lectures.** It is L10's central rights-based example: it starts from protections, not tiers, yet it still uses risk language. L13: its algorithmic impact assessment and independent-evaluation expectations are assurance tools, with the access and enforcement problems that come with them. Alanoca et al. classify it as U.S. soft law that preceded EO 14110. L12: it shows non-binding principles designed to seed standards (the companion is "a blueprint for the development of additional technical standards").

---

## 4. Comparison Tables

### 4.1 Risk-based vs. rights-based approaches

| Dimension | Risk-based | Rights-based |
|---|---|---|
| Starting question | How risky is this system or use, and how much oversight should follow? | What protections are people owed when automated systems affect them? |
| Unit of analysis | The system, use case or tier | The affected person or community |
| Organizing logic | Regulatory triage; proportionality; sorting into tiers | Entitlements and duties (safety, non-discrimination, privacy, notice, human fallback) |
| Typical tools | Bans (top tier), conformity and pre-market obligations, documentation, monitoring, disclosure | Notice, explanation, contestation, opt-out, audits and AIAs, civil rights enforcement, remedies |
| Exemplars | EU AI Act (binding); NIST AI RMF (voluntary); Colorado AI Act | Blueprint for an AI Bill of Rights (non-binding); Council of Europe Convention; UNESCO Recommendation |
| Strengths | Prioritizes scarce enforcement; avoids overregulating low-stakes AI | Keeps focus on people and on recourse; names values explicitly |
| Critiques | Risk categories are value judgments (Grozdanovski & De Cooman); not always "truly" risk-based or attentive to benefits (Ebers); hard to locate risk in GPAI | Rights don't implement themselves; contested concepts (Selbst); rights language can be managerial (L10); often aspirational and unenforceable |
| Overlap | The AI Act is risk-based in structure but uses rights as thresholds and triggers (FRIA) | The Blueprint uses risk language (testing, mitigation, proportionality, risk-calibrated explanations) |

### 4.2 EU vs. U.S. approaches (as described in the module)

| Dimension | European Union | United States |
|---|---|---|
| Main instrument | **AI Act**, a comprehensive binding regulation (Reg. 2024/1689) | No comprehensive federal AI law. Mix of agency action, sectoral law, state laws, litigation and voluntary frameworks (NIST AI RMF, Blueprint); EO 14110 issued 2023, revoked Jan 2025 |
| Coverage | **Horizontal**, across sectors | **Vertical/sectoral** (e.g., EEOC/DOJ on ADA, FTC on FCRA) |
| Timing | Mainly **ex ante** (pre-market obligations), with ex post remedies | Traditionally **ex post** (FTC, lawsuits, state rulemaking); EO 14110 added some ex ante measures |
| Layer | **Hybrid**: application tiers plus GPAI technology rules | Technology-focused at federal level (EO 14110's compute threshold for dual-use foundation models); states often application-focused (hiring, high-risk decisions) |
| Binding? | Hard law, with fines up to €35M / 7% of turnover | Federal frameworks mostly soft law; some binding state and local laws (Colorado, NYC LL144, Illinois, California, Utah) |
| Enforcement | Centralized coordination: AI Office (GPAI) plus Member State market-surveillance authorities | Decentralized: existing agencies; AISI at NIST without binding authority |
| Legal landscape | Very mature (GDPR, DSA, DMA, Copyright Directive, product liability) | Patchwork (HIPAA, GLBA, children's privacy, state privacy laws such as CCPA) |
| Governance pattern | Single regime, with overlap issues (GDPR, product safety) | **Polycentric**: a state "laboratory" model and compliance complexity |
| Global influence | **Brussels effect** potential (cf. GDPR 2018) | Influence through companies, NIST standards and international networks |

---

## 5. Glossary

- **Ada Lovelace Institute critique**: when standards bodies operationalize legal requirements, they can make rights-affecting decisions while civil society struggles to take part.
- **Adverse action notice**: a legally required notice (FCRA/ECOA) giving reasons when credit is denied. The Blueprint uses it as an example of notice and explanation.
- **AI actors** (NIST/OECD): those who play an active role in the AI lifecycle, including deployers and operators.
- **AI Office**: the EU-level body (within DG CNECT) that enforces GPAI rules and coordinates AI Act implementation.
- **AI Omnibus**: the 2025-26 EU simplification package. It delayed high-risk dates, added the nudification and CSAM ban, strengthened the AI Office and extended SME relief.
- **AI Pact**: a voluntary EU initiative encouraging early compliance with the AI Act.
- **Algorithmic discrimination** (Blueprint): automated systems contributing to unjustified different treatment or impacts disfavoring people on protected bases.
- **Algorithmic impact assessment (AIA)** (Selbst): the developer anticipates, tests and investigates harms before implementation, documents them, and publishes or reports them.
- **Anti-regulatory AI**: protective-sounding technical tools (PETs, bias constraints, alignment) that function as regulatory avoidance.
- **Assurance**: processes that verify or build confidence in claims about AI systems or organizations (audits, impact assessments, red-teaming reports, incident reporting).
- **Audit** (Birhane et al.): an independent assessment of an identified target against articulated expectations, with the objective of accountability.
- **Automated system** (Blueprint): computation used to determine outcomes, aid decisions, collect data or interact with people. Excludes passive computing infrastructure.
- **Automation bias**: over-reliance on automated outputs. The Blueprint calls for operator training to counter it.
- **Behavior avoidance**: firm conduct between legal avoidance and evasion, such as narrow definitions or token humans in the loop.
- **Brussels effect**: a large, high-capacity jurisdiction's strict rules become global defaults because firms value economies of scale (e.g., GDPR).
- **Ethics washing** (and privacy washing, fair washing): the appearance of responsibility without real change in behavior or accountability.
- **Epistemic capture**: industry shaping what counts as knowledge, evidence, expertise or a legitimate policy question.
- **Ex ante / ex post**: preventive measures before or at deployment vs. accountability after harm.
- **FIPPs**: Fair Information Practice Principles from the 1973 HEW report, which the Blueprint draws on.
- **Fundamental rights impact assessment (FRIA)**: an AI Act requirement for some deployers of high-risk systems to assess rights impacts before use.
- **General-purpose AI (GPAI)**: models that can perform many tasks and be adapted to many downstream uses. Under the AI Act, very capable or widely used models may carry **systemic risk**.
- **GPAI Code of Practice**: a voluntary EU tool (July 2025) for GPAI providers covering transparency, copyright, and safety and security.
- **Hard law / soft law**: binding, state-backed rules vs. non-binding expectations (standards, frameworks, codes, commitments).
- **Harmonised standards**: EU standards (developed by CEN, CENELEC and ETSI) that give legal certainty for AI Act compliance.
- **Horizontal / vertical (sectoral) regulation**: rules across all sectors vs. rules within specific domains.
- **Internal vs. external audit** (Raji): access without independence vs. independence without access.
- **Pacing problem**: law can't keep up with fast-changing technology.
- **Paradox of participation**: formal inclusion coexists with structures that limit whose knowledge and interests count.
- **Polycentric governance**: multiple independent decision-makers at different scales governing one issue (e.g., U.S. states).
- **Proceduralism**: governance reduced to completing forms and checklists without changing outcomes.
- **Profiles** (NIST): use-case, temporal (Current vs. Target) and cross-sectoral implementations of the RMF.
- **Proxy**: an attribute highly correlated with a protected characteristic that can produce discrimination indirectly.
- **Regulatory arbitrage**: moving activity to jurisdictions with weaker or easier-to-avoid rules.
- **Regulatory capture**: industry influence leading policy to serve private interests over public welfare.
- **Regulatory sandbox**: a supervised environment for testing AI under regulator oversight.
- **Residual risk** (NIST): risk remaining after risk treatment.
- **Risk** (NIST): a composite of the probability of an event and the magnitude of its consequences.
- **Risk tolerance** (NIST): readiness to bear risk to achieve objectives. The RMF doesn't prescribe it.
- **Sticks, carrots, sermons**: regulation, economic incentives and information as families of policy instruments.
- **TEVV**: test, evaluation, verification and validation, performed throughout the AI lifecycle.
- **Theory of change** (Groves et al.): an audit mandate needs a mechanism that turns findings into action and enforceability.
- **Trustworthiness characteristics** (NIST): valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy-enhanced; fair with harmful bias managed.
- **Unacceptable / high / transparency (limited) / minimal risk**: the four AI Act tiers.

---

## 6. Practice Questions (original, for self-study)

**Q1 (MC).** Which NIST AI RMF function is described as cross-cutting and infused throughout the other three?
a) Map b) Measure c) Govern d) Manage
> **Answer: c) Govern.** NIST describes GOVERN as cross-cutting. It applies to all stages, while Map, Measure and Manage can be applied to specific systems and lifecycle stages. *Source: NIST AI RMF §5 and Fig. 5.*

**Q2 (MC).** In NIST's Figure 4, which trustworthiness characteristic is the base and a "necessary condition" for the others?
a) Safe b) Valid and reliable c) Accountable and transparent d) Fair, with harmful bias managed
> **Answer: b).** Valid and reliable is the base. Accountable and transparent is drawn as a vertical box because it relates to all the others, which is a common distractor. *Source: NIST AI RMF §3, Fig. 4.*

**Q3 (MC).** Under the EU AI Act overview, CV-sorting software used in recruitment is classified as:
a) Unacceptable risk b) High risk c) Transparency risk d) Minimal risk
> **Answer: b) High risk.** "AI tools for employment, management of workers and access to self-employment" are high-risk. Emotion recognition *in the workplace* is a separate, prohibited practice. *Source: EU AI Act overview.*

**Q4 (MC).** Which of these is a prohibited practice in the Commission's list?
a) Credit scoring b) Spam filtering c) Untargeted scraping of internet or CCTV images to build facial recognition databases d) Chatbots that don't disclose they are AI
> **Answer: c).** (a) is high-risk, (b) is minimal risk, and (d) breaks a transparency obligation but isn't a banned practice. *Source: EU AI Act overview.*

**Q5 (MC).** In Alanoca et al.'s taxonomy, U.S. EO 14110's reporting requirement for dual-use foundation models above a compute threshold best illustrates which regulatory layer?
a) Application-focused b) Technology-focused c) Ex post d) Sectoral
> **Answer: b) Technology-focused.** It treats a type of technology as inherently risky regardless of use. (It is also an ex ante feature, but the question asks about the layer.) *Source: Alanoca et al. §§5.1(k), 6.5.*

**Q6 (MC).** Raji's distinction between internal and external auditors is best summarized as:
a) Internal = independent; external = high access b) Internal = access without independence; external = independence without access c) Both lack access d) External auditors are always regulators
> **Answer: b).** External auditors include regulators, journalists and academics, and often rely on scraping, records requests or reverse engineering. *Source: L13.*

**Q7 (MC).** Which statement about the Blueprint for an AI Bill of Rights is accurate?
a) It created enforceable rights against federal agencies b) It sorts AI systems into four risk tiers c) It is a non-binding white paper whose scope covers automated systems that could meaningfully affect rights, opportunities or access d) It applies only to machine learning systems
> **Answer: c).** The legal disclaimer says it creates no enforceable rights. It uses a two-part scope test, not tiers. It covers "automated systems" broadly, not only ML. *Source: Blueprint, Legal Disclaimer and "Applying the Blueprint."*

**Q8 (MC).** In the "sticks, carrots, sermons" typology, a city that buys only from vendors providing audit logs is mainly using:
a) A stick b) A carrot (economic/procurement incentive) c) A sermon d) A ban
> **Answer: b).** Procurement changes incentives through the government's purchasing power. The lecture links it to Lessig's market modality. *Source: L08; L07 (procurement).*

**Q9 (Short answer).** Explain the difference between *epistemic capture* and ordinary lobbying, with one example of how it might work in AI policy.
> **Answer:** Lobbying pushes for a particular rule. Epistemic capture shapes what counts as knowledge, evidence, expertise or a legitimate question, and so shapes the debate itself. Example: companies promoting their own benchmarks as the measure of "safety," which pulls debate into technical detail where they have the most expertise and makes political questions (who bears the harm, whether to deploy at all) harder to raise. *Source: L07 (Wei et al.).*

**Q10 (Short answer).** Why does general-purpose AI challenge risk-based regulation designed for task-specific systems? How did the EU AI Act respond?
> **Answer:** A GPAI model can be adapted to thousands of downstream uses. The provider can't foresee them all and the deployer may not understand the model, so risk often appears only at integration and isn't located "in" the model. The AI Act, originally application-focused (April 2021 draft), added GPAI provisions during the late-2022 trilogues after generative AI spread: transparency and copyright duties for all GPAI providers, plus risk assessment and mitigation for systemic-risk models. That made it a hybrid. *Sources: L08, L09; Alanoca et al. §6.5; EU AI Act overview.*

**Q11 (Short answer).** Using NYC Local Law 144, explain the difference between *visibility* and *accountability* in assurance.
> **Answer:** LL144 requires annual bias audits and public summaries (impact ratios), which makes disparities visible. But Groves et al. found narrow and ambiguous definitions, employers treating tools as out of scope, limited auditor access to data, unclear independence, and no duty to fix or stop using a biased tool. Without consequences, remedies and enforcement, an audit produces information but not accountability. Mandates need a "theory of change." *Source: L10, L13 (Groves et al.).*

**Q12 (Short answer).** Give two critiques of the claim that risk tiers are objective. Name the scholars the lecture attributes them to.
> **Answer:** (1) Grozdanovski and De Cooman: many AI Act risks concern fundamental rights (privacy, equality, due process, expression), which lack the statistical base of physical safety risks, so tiering reflects value judgments. (2) Martin Ebers: the Act isn't always truly risk-based. A genuine approach would be proportionate, evidence-based and flexible, and would count benefits and the opportunity costs of not using AI. (Fiesler adds that speculative benefits don't erase real harms.) *Source: L09.*

**Q13 (Short answer).** List three mechanisms that give soft law "teeth," and the related failure mode.
> **Answer:** Any three of: procurement requirements; contract clauses; certification schemes; insurance requirements; reputation and public commitments used as goalposts; the shadow of future hard law (Hagemann et al.: the sword doesn't need to fall). Failure modes: ethics washing (appearance without change) and proceduralism (box-checking). *Source: L12; L08.*

**Q14 (Short answer).** Name the four NIST MANAGE risk-response options and one MANAGE mechanism for systems that behave inconsistently with their intended use.
> **Answer:** Mitigate, transfer, avoid, accept (MANAGE 1.3). MANAGE 2.4 calls for mechanisms to **supersede, disengage, or deactivate** such systems, with assigned responsibilities. MANAGE 2.1 also asks organizations to consider non-AI alternatives. *Source: NIST AI RMF Table 4.*

**Q15 (Short answer).** Alanoca et al. argue that loose use of "AI regulation" creates risks. Name two, and give one piece of evidence they cite about unequal stakeholder participation.
> **Answer:** Any two of: a false sense of safety (people think soft law protects them like hard law); standards watered down to the lowest common denominator; fragmented international coordination and reduced legal interoperability; deterred civil society participation, which raises capture risk. Evidence: of 253 stakeholders consulted on Canada's AIDA, 216 were from business (Clement 2023). Also: Google was accused in Brazil of using its search engine to campaign against disinformation Bill 2630. *Source: Alanoca et al. §§1, 2, 6.7.*

---
*End of notes.*
