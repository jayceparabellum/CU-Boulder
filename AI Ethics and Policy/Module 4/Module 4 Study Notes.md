# Module 4 Study Notes: Governing AI Impacts
*AI Ethics and Policy (CU Boulder / Coursera), instructor Casey Fiesler*

> **What these notes are.** Summaries of the five Module 4 lectures and four assigned readings, a glossary, and original self-study practice questions. They do **not** answer the lab notebook prompts or the reading-activity prompts, and they do not pick quotes for those activities. Where a lecture assigns a lab notebook prompt, the notes only say that one exists.
>
> **Spelling note.** The lecture transcripts are auto-generated and misspell some names. These notes use the standard spellings and give the transcript spelling once, in brackets (for example, Barocas [transcript: "Barakas"]). A few papers are mentioned in lecture without author names. Where the notes add a likely attribution, it is marked *(attribution added; not stated in lecture)*.

---

## 1. Module Overview

Module 3 looked at the **inputs** to AI: privacy, copyright, and authenticity of data. Module 4 turns to **impacts**: what happens when AI systems are deployed, who is helped, and who is harmed. The module does not try to list every possible AI harm. It works through a few categories of impact that governance often tries to address.

The five lectures form a single argument:
1. **Bias and discrimination (L22).** Bias is a governance problem, not only a technical bug. Systems turn historical inequality into decisions about people.
2. **Legitimacy (L23).** Asks a prior question: should automation be used for a given decision *at all*? This brings in procedural justice, contestability, and the limits of "human in the loop."
3. **Labor (L24)** and **4. environment (L25).** Both widen the lens to *externalities*, meaning costs pushed onto people outside the decision. Hidden labor and material infrastructure are both part of AI's foundation.
5. **Responsibility and liability (L26).** Asks who answers for harm once it happens, how responsibility gets spread out among many actors, and how humans in the loop can become "moral crumple zones."

Several threads run through every lecture:
- Who has power, and who is affected?
- Transparency is necessary but not sufficient.
- Individual remedies need to be paired with systemic oversight.
- The "human in the loop" can be a weak safeguard, or even a place where blame lands.

The readings support the lectures directly: Barocas, Hardt & Narayanan for L23, AI Now for L24, Brookings for L25, and Elish for L26 (and also L23).

---

## 2. Lecture Notes

### Lecture 22: Bias and Discrimination

**Key points**
- AI bias becomes a **governance problem** when automated systems turn historical patterns, social inequality, or flawed institutional practices into decisions about rights, opportunities, and access to resources. The governance questions include: who is affected, who has power, which errors matter, what safeguards are needed, and when a system should not be used at all.
- **Definitions:**
  - In a legal context, **bias** is an inclination or predisposition that compromises impartiality.
  - **Discrimination** is the outward manifestation of unfair treatment. Legally it usually concerns specific characteristics such as race, gender, religion, national origin, age, and disability.
  - In technology, bias can come from unrepresentative data, flawed design assumptions, organizational culture, or the context where the system is applied.
- The **Blueprint for an AI Bill of Rights** (from an earlier module) defines **algorithmic discrimination** as automated systems contributing to unjustified different treatment or impacts that disfavor people based on protected classifications. In the US these include religion, age, national origin, disability, veteran status, and genetic information.
- **Three mechanisms of algorithmic bias:**
  1. **Training on the past.** Models reproduce past human bias and past social conditions. Example: a hiring model trained on a company's history of hiring mostly men can learn to reward male-associated career paths, schools, hobbies, or wording, even if gender is never an input. "The past is still present."
  2. **Choosing the wrong target.** A model predicts whatever target variable the designers pick. Example: predicting job tenure may really measure who has historically survived a hostile or inflexible workplace, not who is a good employee. Predictions can also be self-fulfilling.
  3. **Proxies.** Removing a protected attribute does not remove it from the model's world. Being president of a women-in-STEM group, or attending Smith College, can stand in for gender. Neighborhood, language, and medical costs can stand in for race.
- **Fairness depends on context.** Conventional algorithmic fairness is often Western-centric in its categories, values, data assumptions, methods, and legal background. In India, a fairness analysis should account for **caste**, and data may overrepresent digitally rich users (often middle-class men). Fairness cannot be a universal checklist, so ask "**fair according to whom?**"
- **Belief versus action (Hellman).** A fairness score tells us what to believe, but policy depends on what we *do* with it. Differences in error rates matter because they show **who bears the burden of mistakes**. If data reflects prior injustice, using it in a new domain makes that injustice worse.
- **Policy responses:**
  - Existing **anti-discrimination law** (employment, housing, education) still applies when an institution uses AI.
  - Because discrimination is hard to see, policy increasingly requires **audits and impact assessments**.
  - The trend: algorithmic discrimination is treated less as an individual complaint after the fact and more as something organizations must **anticipate, test for, document, mitigate, and monitor**.
- **Closing point.** Transparency mandates and fairness metrics mean little if people cannot use them to challenge, correct, or change a system. This leads into L23's question: when should automated systems shape consequential decisions at all?

**Examples and cases**
- Standard examples of the concern:
  - hiring systems that disadvantage women;
  - facial recognition that performs worse on darker-skinned faces;
  - a healthcare algorithm that underestimates Black patients' needs;
  - predictive policing that sends more police to neighborhoods already heavily policed;
  - systems that work better in one country or culture than another.
- **Allegheny Family Screening Tool**, from Virginia Eubanks, *Automating Inequality*:
  - A child-welfare screening model that predicts parental risk of harming a child.
  - It draws on administrative data: public schools, prior referrals, benefits, housing, mental health, unemployment, and drug and alcohol services.
  - Poor families who rely on public services leave more administrative traces, so the system risks "**confusing parenting while poor with poor parenting**." What it detects is partly poverty, surveillance, and prior contact with institutions.
  - The governance question is not statistical quality. It is whether the evidence reflects unequal scrutiny, and whether the system gives more power over people least able to contest it.
- **Healthcare cost-as-proxy study** (Obermeyer et al., named in the Barocas/Hardt/Narayanan reading):
  - The model used healthcare **costs** as a proxy for healthcare **need**.
  - Black patients had less access to care, so they generated lower costs than white patients with similar illness, and their need was underestimated.
  - The data encodes unequal access, and the model carries that inequality forward.
- **Ableism:**
  - speech recognition failing for people with atypical speech;
  - interfaces that ignore screen-reader compatibility;
  - automated proctoring that flags disability accommodations as suspicious.

**Scholars and papers cited**
- Solon Barocas and Andrew Selbst, *Big Data's Disparate Impact* [transcript: "Barakas"]. Data mining inherits the prejudice of prior decision makers, reflects broader social inequality, and finds patterns that are already patterns of exclusion. The resulting discrimination is often an **emergent property** of the system, not an explicit instruction, so it is hard to identify and hard to fix.
- Virginia Eubanks, *Automating Inequality*.
- *Reimagining Algorithmic Fairness in India and Beyond* (Sambasivan et al., 2021) *(attribution added; not stated in lecture)*. Based on interviews and analysis of AI deployments in India. Warns that focusing only on fair model outputs can backfire when the distance between models and oppressed communities is large.
- Deborah Hellman, *Measuring Algorithmic Fairness*.
- Blueprint for an AI Bill of Rights.

*(Lab notebook prompt 1 is assigned here. Not addressed in these notes.)*

---

### Lecture 23: Automated Decision-Making Legitimacy

**Key points**
- **Legitimacy can come before fairness.** A system could be completely fair across groups and still be inappropriate to use. "More fair automation is still not always legitimate automation."
- **Automated decision-making** is broader than a machine making the final call alone. It includes systems that score, flag, classify, recommend, triage, or generate information that a human relies on, such as a risk score given to a judge or a caseworker's list of families to screen. So the key question is **how AI shaped the decision process**.
- **Procedural justice** is about fairness of *process*, not outcome:
  - Are there clear rules?
  - Is the decision based on relevant information?
  - Do people know what is happening?
  - Can they challenge mistakes?
  - Is there an accountable decision maker who can respond?
  Automation tends to make decisions harder to understand and challenge, and easier for institutions to present as neutral.
- **The reading's three forms of automation:**
  1. **Automating pre-existing rules** (for example, cutting applicants who lack a required credential). The legitimacy question is whether the rule was translated into code correctly. Automation can reduce inconsistency or introduce errors, and writing code to operationalize rules is itself **a type of policymaking**.
  2. **Replicating human judgment** (learning from past human decisions, such as resumes). This gives a "**veneer of objectivity**" to subjective judgment, and the result can be "both too much like human decision makers and too different from them."
  3. **Predictive optimization** (learning decision rules from data by predicting a target such as creditworthiness, job performance, medical need, or risk). This can be acceptable in low-stakes uses like some credit-card fraud detection. In consequential uses, decision makers must **affirmatively justify** the system: how the target relates to legitimate goals, whether it was validated, whether there is recourse, and what procedural protections exist.
- **Citron's technological due process.** Automated government systems merge **rulemaking** (setting general rules) and **adjudication** (applying rules to individuals). Programmers inevitably change rules when they embed them in code, in ways that officials, courts, and the public cannot review.
- **Diagnosing failures.** When a benefits system cuts someone off, the cause could be:
  - the person really no longer qualifies;
  - data was entered wrongly;
  - data came from the wrong database;
  - the rule was coded incorrectly.
  To the affected person these all look the same. For governance they are different: a factual error needs **correction**, a coding error needs an **audit**, and a hidden policy change needs **accountability**. If people cannot tell why a decision happened, they cannot challenge it, and institutions cannot govern it.
- **Notice and explanation** (a Blueprint principle). People should know an automated system is being used and how and why it affects outcomes. This right makes other rights possible. Still, neither notice nor explanation is enough unless there is something you can **do** with it.
- **Contestability** (*The Right to Contest AI*):
  - The right to challenge decisions with significant effects is a core **rule-of-law** principle.
  - AI decisions can be inscrutable and vulnerable to automation bias.
  - Contesting lets an individual say "this doesn't make sense, look again." That matters for accuracy, dignity, legitimacy, and accountability, and it can reveal hidden patterns of failure.
  - Contestation fails if it is too costly, too hard to use, or too shallow. It must be designed into the whole human, machine, and organizational system.
- **Problems with "human in the loop":**
  - Questions to ask: What does the human actually do? Do they understand the system and have the relevant information? Are they trained on **automation bias**? Are they allowed to disagree? Are they penalized for slowing things down? Are they there just so the institution can say a person was involved?
  - **The MABA-MABA trap** ("Men Are Better At / Machines Are Better At"): the assumption that adding a human to a machine automatically gives the best of both. Human-machine systems can instead combine the **worst** of both and add handoff, interface, organizational, and accountability problems.
  - Autonomous vehicle example: a human handed control during a split-second emergency is "in the loop" but may be set up to fail.
- **Richer alternatives:**
  - The Blueprint principle of **human alternatives, consideration, and fallback**: the ability to opt out where appropriate, and access to a person who can quickly consider and fix problems. The fallback must be accessible, equitable, maintained, staffed by trained operators, and must not place an unreasonable burden on the public.
  - Many people lack the time, money, knowledge, legal support, or emotional bandwidth to contest decisions, and some harms are visible only **in aggregate**.
  - So Margot Kaminski [transcript: "Kaminsky"] argues for **binary governance**: **individual rights** (contestation catches concrete errors and gives voice) plus **systemic accountability** (oversight catches patterns no single case reveals).
- **Conclusion.** Legitimacy is not "the system is accurate" or even "equally accurate across groups." It depends on the decision being made, the type of automation, the stakes, and the safeguards and remedies available.

**Examples and cases**
- **International Baccalaureate grading during COVID:**
  - Exams were canceled and an algorithmic model assigned grades.
  - Some students got lower grades than they and their teachers expected, and feared losing scholarships or admissions.
  - Using school context in the model may have disadvantaged high-performing students from historically lower-performing schools.
  - Routes to challenge were limited at first, and the system was not fully disclosed.
- **Benefits-termination scenario** (a hypothetical illustrating Citron's argument).
- **Autonomous-vehicle handoff** (the MABA-MABA example).

**Scholars and papers cited**
- Barocas, Hardt & Narayanan, *Fairness and Machine Learning*, Ch. 2 (assigned reading).
- Danielle Citron, *Technological Due Process*.
- *The Right to Contest AI* (Kaminski & Urban; the reading cites it as Columbia Law Review 2021).
- The 2023 paper on problems with humans in the loop, which named the MABA-MABA trap (likely Crootof, Kaminski & Price, "Humans in the Loop," 2023) *(attribution added; not stated in lecture)*.
- Margot Kaminski, binary governance.
- Blueprint for an AI Bill of Rights (notice and explanation; human alternatives, consideration, and fallback).

*(Lab notebook prompt 2 is assigned here. Not addressed in these notes.)*

---

### Lecture 24: AI and Labor Governance

**Key points**
- **Externalities.** An externality is a usually unintended cost or benefit of an activity, imposed on people who were not part of the decision. AI's benefits are often visible at the point of use, while its costs fall on others: workers, labelers, people managed by algorithms, and communities and environments. The governance question is how hidden or displaced costs become **visible, accountable, and governable**.
- **Reframe the question.** Instead of "Will AI take our jobs?", ask "**How does AI reorganize work, and who has power when that happens?**" The lecture covers three dimensions:
  1. **AI depends on hidden labor**: labeling, evaluation, moderation.
  2. **AI manages labor**: monitoring, evaluating performance, setting pay.
  3. **AI changes the demand for labor**: automation, de-skilling, displacement, new jobs.
- **The Luddites as a governance lesson** (Brian Merchant, *Blood in the Machine*):
  - They were skilled 19th-century English textile workers who often understood the machines well.
  - They objected to how machines were used *against* them: to depress wages, evade labor laws, degrade quality, and profit at workers' expense.
  - They tried governance first: petitions, fair wages, enforcement of labor law, limits on abusive payment practices. Croppers proposed taxing cloth to fund people unemployed by machines, an early version of robot-tax ideas.
  - Lesson: technology conflicts intensify when people have **no meaningful institutional way to respond**.
- **Brishen Rogers** [transcript: "Brishan"]:
  - Labor and employment law does not have to respond only after the fact. It can **shape which technologies employers develop and deploy**.
  - Employers have broad rights to collect workplace data and implement technology regardless of worker preferences.
  - Technology tends to encourage **power-augmenting** uses (control, cutting labor costs) over pure productivity gains. These choices are not neutral.
- **Hidden labor ("ghost work").** Mary Gray and Siddharth Suri's term for human work that makes automated systems appear more autonomous than they are: data labeling, content moderation, model evaluation, annotation, RLHF, and maintenance.
  - It is hard to govern because supply chains are **global**: which country's labor law applies, and who is accountable?
  - Benefits and burdens are geographically uneven. Low pay, surveillance, and psychological harm in one region support products monetized elsewhere.
  - Many governments emphasize AI's economic potential over workers' rights, so unions pursue **informal regulation** through alliances and public scrutiny. The actors' strike from Module 3 is an example of collective bargaining in the shadow of regulation.
- **Algorithmic management.**
  - AI Now (the reading) frames workplace surveillance as a **worker power** issue, fundamentally about **control**. AI Now is a policy advocacy institute focused on concentrated power in tech, which shapes its framing. Theories of power help decide which tools fit.
  - The **six Rs** (from a 2020 paper describing algorithms at work as a new "contested terrain of control"): algorithms **direct** workers (**restricting, recommending**), **evaluate** them (**recording, rating**), and **discipline** them (**replacing, rewarding**).
  - Examples: shift scheduling; warehouse systems that tell workers where to walk and how fast; call-center systems that record tone; platforms that nudge drivers or withhold information; wellness programs collecting health data.
  - Algorithms are often not just assisting management but **becoming management**, more comprehensive and more opaque than earlier control.
- **Transparency is necessary but insufficient.** Knowing about harmful practices is not the power to stop them. Disclosing wage-lowering does not replace rules requiring fair, livable wages. AI Now favors **bright-line rules and red lines**: limits, bans, bargaining rights, wage rules.
- **Gig work:**
  - Control is built into the app: task allocation, pricing, metrics, **deactivation**.
  - The tension: workers are classified as independent contractors yet heavily directed and disciplined.
  - Deactivation functions like being fired. **Washington State** created deactivation protections, appeals, and compensation for wrongful deactivation.
  - Passing a law is not the same as making it usable: appeals require evidence such as earnings data.
- **FairShare** (a 2026 paper):
  - A computational tool built with a drivers' union. It calculates lost wages from pre-deactivation earnings and produces **arbitration-ready reports**.
  - It cut documentation time by more than 95% in parts of the workflow.
  - It also created new problems: consent frictions and the need for ongoing technical support.
  - Lessons: **policy implementation is a design problem**, and worker-support tools still need careful design for infrastructure, trust, and maintenance.
- **Changing demand for labor:**
  - Possible effects: displacement, eliminated tasks, shifting skill value, intensified work, de-skilling (moving judgment from workers to systems), augmenting some while replacing others, new occupations, new dependencies.
  - **Felten and colleagues** [transcript: "Felton"]: AI exposure varies across occupations and tasks, and it is uncertain whether generative AI will automate or complement work. Policy cannot rest on predicting job loss. Governments should improve measurement and build broad, flexible labor policy that does not target one occupation, and policy will need to differ across regions.
  - Proposed responses: reskilling, cushioning transition costs, and a **robot or automation tax** (gains from replacing workers fund transitions or public investment). Other approaches target **who has a voice** in adoption and how productivity gains are shared.
  - **A 2023 MIT policy memo**: generative AI's effects on inequality are **not inevitable**. It distinguishes an **automation path** (displacement and surveillance) from a **human-complementary path** (augmenting workers so they can do more valuable, expert work). Policy levers include tax policy, limits on workplace surveillance, and worker voice.
- **Worker voice is a governance mechanism, not only an ethical value.** It works through unions, collective bargaining, whistleblower protections, participatory audits, and rights to consultation and contestation. AI Now stresses **collective rights**, not just individual rights. FairShare is an example of infrastructure that helps organizers contest algorithms.
- **Closing (back to the Luddites).** Technological change becomes a governance crisis when people must accept systems that reshape their livelihoods without say, protection, or accountability. Labor governance should shape deployment up front, not just manage disruption afterward.

**Examples and cases**
- Luddites and the croppers' cloth-tax proposal; the "data janitors" of South Africa and Kenya (from a 2024 paper); the actors' strike; warehouse, call-center, and wellness monitoring; Uber and DoorDash deactivation; Washington State deactivation protections; FairShare.

**Scholars and papers cited**
- Brian Merchant, *Blood in the Machine*.
- Brishen Rogers, political economy and law of workplace technological change.
- Mary Gray and Siddharth Suri, *Ghost Work*.
- The 2024 paper on data janitors in South Africa and Kenya (authors not named in lecture). It describes remote, insecure, closely monitored, low-paid, precarious work; workers who may not know the purpose of their tasks; psychological harm; and responsibility diffused through contractors and platforms.
- AI Now Institute (reading).
- The 2020 "contested terrain of control" / six Rs paper (Kellogg, Valentine & Christin, "Algorithms at Work," 2020) *(attribution added; not stated in lecture)*.
- The 2026 FairShare paper.
- Felten et al. on generative AI and labor policy.
- The 2023 MIT policy memo on the automation versus human-complementary paths.

*(Lab notebook prompt 3 is assigned here. Not addressed in these notes.)*

---

### Lecture 25: AI and Environmental Governance

**Key points**
- **AI is physical.** It depends on data centers, energy grids, cooling systems, chips, minerals, land, and hardware supply chains: "concrete and lithium and electricity and labor and political decisions." Environmental impacts are **governance problems**: what gets built, where, who decides, who benefits and who is harmed, and what information is available. Costs can be pushed onto communities, grids, ecosystems, and future generations.
- **Infrastructure chain.** Data centers store and serve data and models. They need electricity for servers and cooling, often water for cooling, chips from global supply chains, and rare minerals, and they eventually produce **e-waste**. This connects AI to **environmental regulation** and **environmental justice**.
- **Brookings (the reading).** Few requirements exist to accurately record energy or water use. Demand may outpace efficiency gains. **Transparency** would help decision makers understand impacts and protect communities from resource strain. In short, we know AI has a footprint but lack the information to govern it.
- **Life-cycle view** (a 2026 paper proposes eight stages):
  1. hardware manufacturing
  2. infrastructure construction
  3. dataset creation and preprocessing
  4. model experimentation and R&D
  5. model training
  6. post-training adaptation
  7. deployment and inference
  8. end of life and decommissioning

  Focusing only on training, or only on energy and water, misses burdens pushed into other places and communities.
- **Context and location matter:**
  - Carbon footprint depends on how much electricity is used and **where it comes from** (a clean grid versus a fossil-heavy grid).
  - Water-intensive cooling in a **water-stressed region** has very different local effects.
  - A data center's water use can look tiny next to national agricultural use but still strain a stressed local system.
  - Water governance is **local** (municipal systems, drought, community needs), so communities need **facility-level** data: how much water, seasonal variation, direct versus indirect use, and interaction with local infrastructure.
- **A global view and "AI colonialism"** (a 2025 paper on artificial intelligence colonialism):
  - Benefits concentrate among elites and companies mainly in the **Global North**, while labor exploitation, resource extraction, and environmental damage shift to the **Global South**.
  - So "sustainable" needs specifics: **for whom, where, and at what life-cycle stage**.
- **E-waste** (Wang and colleagues):
  - Generative AI and LLM-related e-waste could reach **1.2 to 5 million tons from 2020 to 2030**, depending on the scenario.
  - **Circular economy** strategies (decoupling growth from consumption of finite resources) could reduce this substantially.
  - Fast server replacement may make business sense, but the companies often don't bear the environmental cost, which is a case for regulation.
  - Tools: e-waste rules, right to repair, extended producer responsibility, procurement standards, recycling mandates, hardware life-cycle reporting.
- **Efficiency versus sufficiency:**
  - Efficiency (better models, carbon-aware scheduling, better chips) is good but **is not the same as sustainability**.
  - **Jevons paradox** [transcript: "Jevin's"], used by **Luccioni** and colleagues [transcript: "Lucione"]: efficiency lowers cost, which can increase demand and total consumption. Cheaper queries could lead to generative AI in every search box and workflow, raising total resource use.
  - **Sufficiency** asks how much we actually need, which uses are worth the cost, and where to avoid unnecessary computation. Governance should address both.
  - **Ebert and colleagues** propose **user rights to select environmentally optimized models and to opt out of unnecessary generative AI integration**, which covers both efficiency and sufficiency, alongside more specific transparency requirements.
- **Data centers as local politics.** A 2025 report tracked data-center development in Chile, the US, Mexico, the Netherlands, and South Africa. Similar organizing is spreading across the US.
- **Policy toolbox.** No single environmental AI tool exists, and different problems need different tools:
  - **Make impacts visible:** required reporting, disclosure, impact assessments.
  - **Reduce impacts or set limits:** efficiency standards, water-use limits, clean-energy requirements, e-waste rules, siting restrictions in water-stressed regions, and (as soft law) procurement standards favoring lower-impact systems.
  - **Shift incentives:** electricity pricing, removing tax breaks for high-impact facilities, tax incentives for lower-impact designs, requiring companies to internalize local infrastructure costs.
  - **Give communities a voice:** public hearings, consultations, local permitting, public access to environmental information.
- **Takeaway.** Environmental impacts are governance problems about **visibility, accountability, and power**. Labor and environment are both part of AI's fundamental infrastructure, which is why the two lectures sit side by side.

**Examples and cases**
- **Google's proposed data center in Santiago, Chile:**
  - The country was in prolonged drought, and residents worried about water use.
  - Resistance included hiring an environmental lawyer, protests, community rallying, and engaging with Google.
  - Google agreed to reduce water consumption, and an **environmental tribunal ruled that Chile's Environmental Evaluation Agency had mishandled the approval**.
  - The case shows three forms of governance interacting: **formal law** (permitting), **corporate governance** (Google's choices), and **community governance** (organizing and pressure).

**Scholars and papers cited**
- Brookings (reading).
- The 2026 eight-stage life-cycle paper.
- The 2025 AI colonialism paper.
- Wang et al. on generative AI e-waste.
- Luccioni et al. on the Jevons paradox.
- Ebert et al. on user rights.
- The 2025 multi-country data-center report.

*(Lab notebook prompt 4 is assigned here; it draws on the earlier "stick / carrot / sermon" policy-tool categories. Not addressed in these notes.)*

---

### Lecture 26: Responsibility and Liability

**Key points**
- **Shift from impact to responsibility:** who is responsible, who had control, what could have prevented the harm, what remedy exists, and how to keep responsibility from disappearing into system complexity.
- **Responsibility versus liability:**
  - **Responsibility** is who is connected to a harm, causally or morally.
  - **Liability** is who is **legally answerable** for it.
  - Liability provides **redress** after harm (lawsuits). It is also a **governance tool that shapes incentives beforehand**: companies that expect liability for foreseeable harms have reasons to test, warn, and avoid uses they cannot control.
  - Much AI governance is **ex ante** (risk assessments, red teaming). Ex-ante tools are not enough because harm still happens, and liability helps determine what happens when prevention fails.
- **Helen Nissenbaum's four barriers to accountability** in computerized societies (1990s):
  1. **The problem of many hands**: different actors design, train, integrate, deploy, and use the system.
  2. **The bug problem**: failures are treated as unavoidable glitches rather than foreseeable or preventable.
  3. **Blaming the computer**: "the algorithm decided," as if that ends the discussion.
  4. **Ownership without liability**: companies control, sell, and profit from software while disclaiming responsibility for its harms.

  AI intensifies all four because systems are more complex, more widely deployed, more opaque, and used in high-stakes settings.
- **Autonomous vehicles and the 2018 Uber crash in Tempe, Arizona:**
  - Many possible actors: manufacturer, automated-driving-system developer, testing company, software vendor, safety driver, fleet deployer, and the regulator that allowed public-road testing.
  - The system **detected the pedestrian but misclassified her** and failed to predict her path.
  - **Emergency braking was suppressed**, and the system relied on the human operator.
  - The factory-installed forward collision warning and automatic emergency braking were **disabled during autonomous operation**.
  - The **NTSB concluded that Uber failed to manage anticipated safety risks and removed a layer of safety redundancy**.
  - Harm comes from interactions among design, organizational decisions, human behavior, and regulation. **AI design choices are ways of allocating risk.**
- **The Moral Machine experiment and its critique:**
  - Thousands of people worldwide judged stylized AV crash dilemmas, a real-world version of the trolley problem.
  - The paper "Why the Moral Machine Is a Monster" argues that encoding such preferences **turns code into policy**. If cars systematically spared children over the elderly, the elderly might fear leaving home. Always favoring law-abiding people would create "the death penalty for jaywalking."
  - The scenario is unrealistic. Real AV choices concern braking speed, room given to cyclists, and when to alert a human. But the same point holds: **engineering questions become policy questions** that decide who bears risk.
- **Remedies for Robots** (Mark Lemley and Bryan Casey [transcript: "Mark Limley and Brian Casey"]):
  - Legal remedies are designed for people and organizations. An AI system does not understand or obey a court order.
  - A remedy aimed at changing AI behavior must be **translated into design and code**: retraining, restricting settings, adding warnings, or taking the system offline.
  - So AI remedies are not only about compensation after harm. They can also change the **technical and organizational conditions** that made the harm possible.
- **Crashworthy code** (Bryan Choi [transcript: "Brian Choi"]):
  - Cars aren't expected to be crash-proof, but they should reduce harm when crashes happen (seatbelts, airbags, brakes).
  - In complex cyber-physical systems, code failures are **statistically inevitable**, so ask whether the developer designed the system to **fail safely**: redundancies, warnings, fallbacks, monitoring, and containment of foreseeable failures.
  - This is why Uber's **disabled emergency braking** matters so much.
- **Moral crumple zone** (Madeleine Clare Elish, the reading):
  - A human absorbs moral or legal responsibility for an automated system's failure despite limited control.
  - Safety drivers must passively monitor for long periods and then intervene in a split second. Humans are bad at this: attention drifts and complacency sets in.
  - After a crash, "the human should have intervened" hides system-level questions.
  - Questions about a human in the loop: What exactly must they do? Can they understand the output? Can they tell when it's wrong? Do they have time and a chance to act? Can they override? Could they be punished for overriding?
  - Depending on the answers, the human may be "**less a safeguard and more a liability sponge**."
- **Where should responsibility land?** There is no single answer, and different regimes choose differently:
  - **Product focus:** defective design, inadequate testing, insufficient warnings.
  - **Operator or deployer focus:** who put the system in use and controlled the conditions.
  - **Professional standards:** competent practice in the field.
  - **Stricter responsibility:** when an actor introduces serious risk that others cannot realistically understand or control.

  Liability is not just finding someone to blame. It is a **governance choice** about where responsibility attaches and what remedies follow.
- **Module wrap-up.** It is never simply "the AI is responsible." Responsibility is spread across actors, and harms are shaped by design, business incentives, organizational decisions, and human practices. Ask who had power, who was most at risk, who has a realistic path to remedy, and what must change to prevent recurrence.

**Scholars and papers cited**
- Helen Nissenbaum, "Accountability in a Computerized Society" (1996).
- NTSB findings on the Uber crash.
- The Moral Machine experiment.
- "Why the Moral Machine Is a Monster" (philosopher; likely Abby Everett Jaques, 2019) *(attribution added; not stated in lecture)*.
- Mark Lemley and Bryan Casey, "Remedies for Robots."
- Bryan Choi, "Crashworthy Code."
- Madeleine Clare Elish, "Moral Crumple Zones" (reading).

*(The final lab notebook prompt is assigned here. Not addressed in these notes.)*

---

## 3. Reading Notes

### Reading 1: Barocas, Hardt & Narayanan, "When Is Automated Decision Making Legitimate?"

**Citation:** Barocas, S., Hardt, M., & Narayanan, A. *Fairness and Machine Learning: Limitations and Opportunities*, Chapter 2, "When is automated decision making legitimate?" (fairmlbook.org; MIT Press, 2023).

**Central thesis.** Some unfairness is not about how groups are treated relative to each other but about **legitimacy**: whether it is morally justifiable to deploy machine learning or automation *at all* in a given scenario. That question should **come before** distributive fairness questions. Machine learning should be compared to **bureaucratic** decision-making, not individual human judgment, and in high-stakes domains it can undermine the procedural protections bureaucracies use to prevent arbitrary decisions.

**Structure**
1. Three opening vignettes:
   - a perfect-scored essay that turns out to have been graded by a computer;
   - a defendant labeled high flight risk based on people "like him";
   - a social-media lockout with no explanation or appeal.
2. Why institutions, including private firms, need legitimacy.
3. "Machine learning is not a replacement for human decision making."
4. Bureaucracy as a bulwark against arbitrary decisions (two kinds of arbitrariness).
5. The three forms of automation, with a section on each.
6. A deep dive on predictive optimization:
   - mismatch between target and goal;
   - failing to consider relevant information;
   - the limits of induction;
   - a right to accurate predictions?;
   - agency, recourse, and culpability (including gaming).
7. Concluding thoughts.

**Key arguments**
- **Why legitimacy matters, even for private firms.** The more power a firm has over individuals, the more that power must be seen as legitimate. Otherwise people resist, notably through law, and the firm may lose ground competitively. Examples:
  - ride-sharing firms facing activism, litigation, and regulation;
  - Apple making Facebook tracking harder on iOS, which had public support arguably because Facebook's business model had lost legitimacy.
- **Legitimacy comes first.** Debating distributive justice inside a fundamentally unjust institution is at best a waste of time and at worst props it up.
  - Reducing racial error-rate gaps in facial analysis does not answer concerns about using it for oppressive purposes.
  - Firms have **co-opted fairness discourse**, ensuring parity between groups without addressing legitimacy.
- **Reject the "humans are black boxes too" analogy.** High-stakes decisions such as hiring, credit, and admissions are traditionally made by **bureaucracies** with formal rules and procedural protections, not by one person's judgment. Strandburg: reason-giving is required *because* humans are inscrutable and biased, not because they can accurately describe their thought processes.
- **Two kinds of arbitrariness** (Creel & Hellman):
  1. **Inconsistency or ad hoc decisions.** This is about procedural regularity. It violates "treat like cases alike" and harms **autonomy**, because people cannot make effective life plans.
  2. **Decisions that lack reasoning** even when consistent. Example: a coach consistently choosing runners by sneaker color.
  - Governments face a legal **rational basis** requirement (due process) because they monopolize certain decisions. Private actors have no such legal duty, but for high-stakes decisions we still expect good reasons out of **respect for the people affected**.
- **Form 1: automating pre-existing rules.** This addresses inconsistency but carries risks:
  - translation errors;
  - programmers filling ambiguity and so "usurping the authority to define policy" (Citron);
  - plain bugs, as in the **British Post Office scandal**, where hundreds of postmasters were convicted of theft or fraud over twenty years based on flawed software ("the biggest miscarriage of justice in British history");
  - no room for **discretion** and **brittle** decisions. A caregiver-eligibility assessment marked "no foot problems" for an amputee;
  - no chance to correct errors or add mitigating information;
  - **diffused accountability** (decisions "made by no one") and dehumanization.

  The authors stress that none of these problems come specifically from ML.
- **Form 2: learning to replicate past human decisions** (for example, essay grading). This can smooth inconsistency, but:
  1. it lends a **veneer of objectivity** to subjective judgment and can amplify human bias. Many "objective" targets are really human judgment in disguise (David Hand);
  2. models may reach similar decisions through different reasoning and with different error patterns. Rewarding sophisticated vocabulary in essays is no substitute for judging coherence.

  Result: "both too much like human decision makers and too different from them."
- **Form 3: predictive optimization** (learning a rule from data to predict a target). It seems to promise reasoned decisions, but it is a radical departure from deliberative decision-making.
  - **Table 1** compares traditional and predictive-optimization approaches to college admissions. Traditional: holistic, multiple implicit goals, debate about criteria, easier to include values such as need. Predictive: explicit target such as GPA, debate centers on the choice of target, accuracy can be quantified, harder to include multiple values, and reasons become explicit in the target.
  - Johnson & Zhang found that deliberative housing-assistance rules ranked veterans above heavily rent-burdened households, against the policy's basic goal. An explicit target can force intent into the open (Abebe, Barocas, Kleinberg et al.).
  - The danger is a narrow focus on **accuracy**, when "good" decisions also mean the right target, relevant and complete factors, other values (need, desert), and the ability to understand and contest.
- **Mismatch between target and goal:**
  - Goals are multiple and hard to measure, so decision makers pick **targets of convenience**. Example: arrests as a proxy for crime.
  - Predicting crime is not the same as reducing it.
  - **Obermeyer et al.**: using healthcare cost as the target underestimated Black patients' need. The authors add that cost may have reflected the system's **true goal** (cutting costs). Don't confuse objecting to the **goal** with objecting to the **target**.
  - Gandy: bias can be inherent in the choice of objective.
- **Failing to consider relevant information:**
  - Induction always groups people. A skilled driver of a red sports car is charged like other red-sports-car drivers. Schauer calls this "**statistically sound but nonuniversal generalizations**."
  - The real issue is failing to use **additional relevant criteria**. Telematics "black boxes" in cars still compare a driver to other drivers.
  - Cost-benefit limits on gathering information have three gaps: automation blocks cheap volunteered information; distributional effects are ignored; and the decision maker's view of costs may differ from the subject's.
- **The limits of induction:**
  - **Overfitting** (spurious sneaker-color correlation) is manageable through larger samples, penalizing complexity, and train/test splits.
  - **Distribution shift** is a foundational problem. Even a stable non-causal correlation (sneaker color tied to shoe size, which predicts speed) may fail when conditions change.
  - This leads to demands for **causal** relationships (Pasquale's "facially invalid" ML; Kim & Hanson).
- **A right to accurate predictions?** Some outcomes, such as spur-of-the-moment recidivism, may be inherently unpredictable. Typical deployed models have an **AUC of about 0.7 to 0.8**, which still means many false positives and negatives (for example, in child-protection screening). How much accuracy is needed for legitimacy, and to justify the gap between the target and the real goals?
- **Agency, recourse, culpability:**
  - **Immutable** traits deny agency.
  - **Recourse** is unequal: one person can move neighborhoods to improve a credit score, another can't. Explanations should point to actions people can actually take.
  - **Culpability**: people shouldn't be judged on factors outside their control. Kiviat notes state laws barring car insurers from using "extraordinary life circumstances" such as a death in the family.
  - The flip side is **gaming**: changing features without changing the underlying outcome, as in teaching to the test or meaningless credentials. Preventing gaming requires causal modeling.
- **Conclusion:**
  - No blanket claims. Low-stakes uses such as credit-card fraud detection (US consumer liability capped at $50, so banks bear the cost) raise few legitimacy concerns.
  - In **consequential** uses, decision makers must **affirmatively justify** the scheme: tie the target to goals all stakeholders accept, validate accuracy, and allow recourse.
  - Procedural protections are often possible, but decision makers resist them because they **undercut the cost savings** automation promises.

**Key terms**
- **Legitimacy**: whether it is morally justifiable to deploy an automated system at all in a given setting.
- **Arbitrariness (two senses)**: inconsistent or ad hoc decisions; or decisions lacking a valid reasoned basis.
- **Procedural regularity**: rules fixed in advance and applied consistently and correctly.
- **Procedural protections**: mechanisms ensuring decisions are transparent, based on relevant information, and open to challenge and correction.
- **Predictive optimization**: learning a decision rule from data by predicting a target that stands in for the decision maker's goal.
- **Target of convenience**: a prediction target chosen because data is easy to get, not because it matches the goal.
- **Statistically sound but nonuniversal generalization** (Schauer): an individual meets a group's criteria but lacks the trait the criteria are meant to predict.
- **Distribution shift**: differences between training/test data and the future population where the model is applied.
- **Recourse**: a person's ability to change features to get a different decision.
- **Gaming**: changing features to change the decision without changing the outcome the features predict.

**Ties to lectures.** This is the core of L23: the three forms of automation, Citron, a veneer of objectivity, "too much like / too different," affirmative justification, and the low-stakes fraud-detection example. It also backs L22 (Obermeyer, target choice), and its points about diffused accountability (citing Nissenbaum) prefigure L26.

---

### Reading 2: AI Now Institute, Algorithmic Management and Workplace Surveillance

**Citation:** AI Now Institute (2023). Section on algorithmic management and workplace surveillance ("Restraining Workplace Surveillance"), from AI Now's 2023 landscape report. Web version; footnotes cite sources through mid-2023.

**Central thesis.** Workplace surveillance and algorithmic management are about **control and power**, not productivity, efficiency, or safety. Policy must confront why surveillance harms workers:
- it justifies unfair decisions about pay, safety, and resources;
- it invades private lives;
- it inhibits organizing.

The authors argue for **bright-line rules** that restrain these tools and create **no-go zones**, rebalancing power among workers, employers, and the vendors who sell the tools.

**Structure**
1. Opening claim and the rise of algorithmic management and surveillance since the pandemic.
2. "Labor Technology Policy: Principles of the Emerging Framework."
3. "Worker Organizing and Tech Policy."
4. "Transparency and data-access measures are necessary but insufficient."
5. Red lines.
6. Critique of "human in the loop" proposals.
7. Critique of audits.
8. "Data protection regulations offer inroads... but don't go far enough."
9. "Building Worker Power through Tech Policy."

**Key arguments**
- **The rise.** Surveillance expanded with remote work, blurred work and home boundaries, and work tech on personal devices. **Low-wage workers** have led the fight. Organizing has exposed algorithmic benchmarks and pay setting, productivity quotas, and hiring, promotion, demotion, and firing recommendations.
  - Claimed benefits (curbing discrimination, compliance metrics, efficiency in resume review) are "weakly supported."
  - The harms: devaluing work, unequally distributing risks and privileges, threatening collective action, and destroying privacy.
- **Information as power.** Algorithmic management, surveillance, and Big Tech should all be read through **the ability to leverage information as a source of power**. This applies to employer and employee as much as to tech firms and users.
- **The emerging policy framework:**
  - **Stop Spying Bosses Act**: disclosures, prohibitions on some data collection, and a Privacy and Technology Division at the Department of Labor.
  - Proposed **EU Platform Work Directive**: worker data access, algorithmic transparency, contestability.
  - Proposed **California Workplace Technology Accountability Act (A.B. 1651)**: bright-line rules, impact assessments, transparency.
  - The **Blueprint for an AI Bill of Rights** extends to employment systems.
  - **NLRB General Counsel Memo GC 23-02**: concern that monitoring interferes with protected activity.
  - Frameworks must strengthen **collective organizing and bargaining** and **protected concerted activity**; protect all workers, union or not, across sectors including managers; include **whistleblower protections**; apply existing law (workplace safety, wage-and-hour law against just-in-time scheduling); and provide **collective rights**.
- **Worker organizing as tech accountability.** Tech worker organizing is "one of the most effective and direct means" of curbing harms before they occur: whistleblowing, dropping military contracts, calling out human rights abuses. Organizers face retaliation, and Amazon reportedly hired **Pinkerton** operatives to surveil workers and organizers. Recommended curbs: stronger whistleblower protections, limits on NDAs and non-disparagement clauses, and bans on non-competes.
- **Transparency is necessary but insufficient**, and the burden should fall on developers and employers.
  - "Worker data rights" proposals aim to know what is collected and how it's used, and to access, correct, and contest.
  - The strongest require disclosure in phases, including **before deployment**, and recognize that **consent is not meaningful at work** because refusal risks retaliation. Under Illinois's **AI Video Interview Act** and NYC's **Local Law 144**, candidates may fear seeming "difficult" if they ask for an alternative.
  - Shortfalls:
    1. They ignore the power relations among workers, employers, and **vendors**. Telling workers about wage-lowering is no substitute for fair-wage rules, and trade secrecy and contracts lead firms to resist.
    2. Data access assumes outside actors have the capacity to analyze it, but workers, journalists, and civil society have few resources. Knowledge is only a first step.
  - Bright lines put the onus on beneficiaries rather than the harmed.
- **Red lines:**
  - no monitoring of private areas (bathrooms, employees' cars);
  - limits on monitoring off-duty time;
  - bans on **emotion recognition** at work (pseudoscientific, and employers shouldn't probe inner states);
  - bans on **algorithmic wage discrimination** (Dubal);
  - **purpose limitations** and bans on secondary use and sale of worker data.

  These counter **surveillance interoperability** (Karen Levy): government, corporate, and third-party surveillance reinforcing each other. Examples: Argyle brokering employment data for insurers' "risk assessments" of rideshare drivers; Appriss Retail combining point-of-sale and criminal-background data to score employee fraud risk. Competition law could limit data combination. Defining the work/home boundary remains hard.
- **"Human in the loop" proposals are flawed:**
  - Decisions sit on a continuum rather than being fully automated or fully human.
  - Humans may **rubber-stamp** and legitimize flawed decisions (Green & Kak).
  - There is no definition of "meaningful" oversight.
  - **Automation bias** means deference to automated tools.
  - Responsibility blurs, so the overseer is blamed for systemic failures. Bright lines should decide whether algorithms belong in a decision at all.
- **Audits:**
  - They let firms mischaracterize their practices.
  - Skewed incentives limit auditor access, and trade secrecy may hide results. **HireVue** selectively released an audit and mischaracterized its breadth, excluding the facial analysis and performance predictions it had been criticized for.
  - It is unclear who has the expertise without standards.
  - Audits presume systems are contestable, which misreads employer-worker power. Referrals to the DOL, OSHA, or EEOC could rest on other evidence.
- **Data protection:**
  - US privacy law largely **exempts workplaces**, because consent frameworks break down at work. CCPA amendments from January 2023 cover workers at large firms.
  - In the EU, unions use the **GDPR** effectively. The App Drivers and Couriers Union sued Uber over pay-setting data and algorithms.
  - Notice is required under GDPR Arts. 13 and 14, and a **DPIA** under Art. 35 likely applies before deployment and periodically after.
  - Still, the burden stays on the harmed, and courts read GDPR transparency narrowly. "**Data minimization**" measures (for example, limits on biometrics in workplaces) are more promising.
- **Building worker power:**
  1. Focus on **inferences and outcomes**, not just collection, given first-party profiling, anonymization, differential privacy, and synthetic data. Anonymized data can still harm workers collectively, for example by predicting which stores will unionize.
  2. Adopt an **impact-oriented definition of data** that covers **collective harm**. "The issues at hand are not about data, but about the relationships and structural inequities between workers and employers."

**Key terms**
- **Algorithmic management**: using algorithmic systems to direct, evaluate, and discipline workers (scheduling, quotas, pay, hiring and firing recommendations).
- **Bossware / workplace surveillance**: monitoring tools such as keystroke tracking and productivity scores.
- **Bright-line rules / red lines**: categorical limits or bans rather than case-by-case disclosure.
- **Worker data rights**: proposals for notice, access, correction, and contestation of workplace data.
- **Protected concerted activity**: legally protected collective action by workers (NLRB).
- **Algorithmic wage discrimination**: personalized, algorithmically set pay (Dubal), which the authors say should be banned outright.
- **Surveillance interoperability** (Levy): mutually reinforcing surveillance regimes.
- **Purpose limitation / secondary use bans**: data may be used only for the stated purpose and not sold or ported elsewhere.
- **Data minimization**: limiting collection of certain data types or uses in certain contexts.
- **DPIA**: Data Protection Impact Assessment (GDPR Art. 35).

**Ties to lectures.** L24 (algorithmic management as a power issue, transparency insufficient, bright lines, collective rights, worker voice as a governance mechanism). The human-in-the-loop critique links to L23 and L26 (Elish), and the audit critique links to L22's audit mandates.

---

### Reading 3: Brookings, "As energy demands for AI increase, so should company transparency"

**Citation:** Stewart, J., Tanner, B., & Turner Lee, N. (2025, July 14). "As energy demands for AI increase, so should company transparency." Brookings Institution, TechTank commentary (Center for Technology Innovation, Governance Studies). Disclosure: Google, Microsoft, and Meta are general unrestricted donors to Brookings. The authors state their findings are not influenced by donations.

**Central thesis.** AI and data centers use large amounts of energy and water, but **few requirements exist to accurately record or disclose** that use. Demand may outpace efficiency gains and increase emissions. **More transparency** from tech companies, electric utilities, and data centers would give decision makers the data to understand AI's environmental impact and to craft policies that protect communities from strain on their resources.

**Structure**
1. Key takeaways.
2. Opening on viral comparisons (each ChatGPT email like dumping a bottle of water; each prompt like a light bulb on for about 20 minutes). Policy tracking lags because data is missing.
3. "What are AI energy costs? And where do they come from?"
4. "Lack of data makes AI energy consumption less transparent."
5. "Growing efficiencies in AI energy consumption."
6. Unequal impacts.
7. "What will power AI in the future?" (policy).
8. Conclusion.

**Key arguments and figures**
- **Sources of energy cost:**
  - Impact spans months or years of training and deployment.
  - GPUs often run 24 hours a day during training, usually on non-renewable power.
  - Google and UC Berkeley researchers estimated that training the model the article calls "ChatGPT-3" used electricity for about **120 US homes for a year**. GPT-4 likely took about **50 times more**.
  - One IEA-based estimate: ChatGPT uses nearly **10 times** the electricity of a Google search. 9 billion AI searches per day could need **23 to 30 times** the energy of normal searches.
  - **Sasha Luccioni's "AI Energy Score"** dashboard (Hugging Face) shows roughly a **62,000-fold** spread between the highest and lowest energy use.
  - Video is the most energy-intensive: MIT Technology Review found about **3.4 million joules** for a 5-second video, more than an hour of microwave use.
- **Data centers:**
  - **4.4% of US electricity demand in 2023**, possibly **6% by 2026**.
  - 1 to 2% of world energy needs, with some expecting up to **21% by 2030**.
  - UK researchers estimate global water use for data processing could reach **half of the UK's water usage by 2027**.
  - Indirect costs come from building infrastructure. GPUs typically last about **four years** before disposal or repurposing, and how they are disposed of is unknown.
- **The transparency gap:**
  - Companies don't typically release energy or water data and have no obligation to.
  - Google, Microsoft, and Meta declined to share per-prompt energy figures.
  - Sam Altman said an average query uses **0.34 watt-hours** and **0.000085 gallons of water**, but this excludes training and is per-query only.
- **Efficiency and its limits:**
  - Efficiency gains have recently **plateaued**.
  - Sources of gains: hyperscale centers; **power capping** (up to 15% less energy with minimal user impact); smaller models; pruning and quantization; renewables; collaboration; using AI to optimize AI (DeepMind cut data-center cooling energy by **30%**).
  - These still require more AI use, and lower costs can drive a **rebound effect**, or **Jevons paradox** (named from steam-engine efficiency).
- **Unequal impacts:**
  - **Virginia's "Data Center Alley"** has 300+ data centers, the most in the US. Residents face rising energy bills, water demand, and worse air quality from **backup diesel generators**.
  - The **NAACP sued xAI** for allegedly running turbines at a South Memphis data center without proper permits, with toxic emissions directed at predominantly Black neighborhoods, which it framed as **environmental racism**.
- **Policy landscape:**
  - MIT scientists found companies using **independent auditors for assurance** cut total emissions by **7.5% annually**.
  - Estimates lack AI-specific detail (IEA covers all data center activity), so companies need to disclose the **AI share** of their energy use.
  - Sen. Ed Markey's **Artificial Intelligence Environmental Impacts Act of 2024**: an EPA study, a NIST stakeholder consortium, a **voluntary reporting system**, and an interagency report to Congress.
  - The **GAO** report on generative AI (April 2025) lists six policy options, including encouraging developers to share infrastructure details and offering incentives for resource-efficient models and training.
  - **60+ state bills** on data centers, with little meaningful change.
  - Harvard researchers found data-center carbon intensity **48% higher** than the national average, partly because data centers sit on dirtier grids.
  - Meta and Microsoft are turning to **nuclear**, but nuclear is only about 20% of US electricity, and intermittent wind and solar cannot fully power always-on data centers.
- **Conclusion.** The US should support research on lowering AI's environmental impact while improving transparency and setting standards. Failing to do so could accelerate the climate crisis and also **slow AI adoption** and delay its benefits.

**Key terms**
- **Training versus inference (per-query) energy**: one-time model building versus ongoing use. Per-query figures leave out training.
- **Data center / hyperscale center**: facilities for computation; very large ones can be more efficient.
- **Power capping**: limiting power supplied to processors to save energy.
- **Pruning / quantization**: techniques to shrink models and their computational cost.
- **Rebound effect / Jevons paradox**: efficiency lowers cost, which raises demand and total consumption.
- **Assurance (independent auditing)** of emissions reporting.
- **Carbon intensity**: emissions per unit of electricity, which depends on the grid.
- **Environmental racism**: environmental burdens falling disproportionately on communities of color.

**Ties to lectures.** L25's core claim that we lack the information to govern AI's footprint, plus Jevons paradox, uneven local impacts, end-of-life e-waste, and "make impacts visible" tools (reporting, disclosure). The Markey bill's voluntary reporting is a soft-law tool, connecting to the earlier policy-tools lecture. Brookings focuses on energy, water, and emissions, while L25 widens to the full life cycle and the Global South.

---

### Reading 4: Elish, "Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction"

**Citation:** Elish, M. C. (2019). "Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction." *Engaging Science, Technology, and Society*, 5, 40-60. DOI: 10.17351/ests2019.260. (Elish was at Data & Society Research Institute. An earlier version was presented at WeRobot in 2015. It builds on Elish & Hwang 2015, "Praise the Machine! Punish the Human!")

**Central thesis.** In complex automated systems where control is spread across actors, time, and space, **responsibility can be misattributed to the nearest human operator, who had limited control**. That person becomes a **moral crumple zone**. A car's crumple zone protects the human driver. A moral crumple zone **protects the integrity of the technological system at the expense of the nearest human operator**. Structural features of systems and **media portrayals** of accidents exploit humans' tendency to become "**liability sponges**," filling accountability gaps.

**Structure**
1. Introduction: the Uber crash, the concept, related literatures (law, human factors, systems design, ethics, sociology of risk).
2. Case 1: Three Mile Island (1979).
3. Case 2: Air France Flight 447 (2009).
4. Discussion: Nissenbaum, the Therac-25 counterexample, conditions for moral crumple zones, culture and law.
5. "Robots on the Road": Uber, Tesla, Google.
6. Conclusion.

**Key arguments and cases**
- **Automation as a spectrum** (Parasuraman, Sheridan & Wickens 2000): ten levels, from no computer assistance to full computer control. Autonomy is a matter of degree.
- **Three Mile Island** (March 28, 1979, Unit 2; partial core meltdown, the first US nuclear disaster):
  - Maintenance workers fixing a clogged filter choked off feedwater, triggering shutdown.
  - A relief valve opened as designed but **jammed open**, so coolant drained.
  - Valves accidentally left closed after testing two days earlier had **no control-room indicator**. This is a **common-mode failure**.
  - Amid many alarms, operators misread the situation and **shut off auxiliary pumps**, overriding the automatic safety system. More than a third of the core melted over 16+ hours.
  - Media (the LA Times, AP) and official sources blamed "**human error**." The Kemeny (President's Commission) report noted systemic issues but stressed human failure.
  - Elish's systemic reading:
    - the control room did not show coolant level directly, so operators inferred it from a misleading auxiliary tank ("incorrect decisions because they had incorrect information");
    - management ignored recurring filter problems and directed corner-cutting tests;
    - regulators under-regulated valve maintenance;
    - the management climate treated rules as bureaucratic hoops.
  - Perrow calls this a "**normal accident**" in a tightly coupled complex system.
  - The operators became the moral crumple zone, showing a mismatch between **actual and perceived control**.
- **Air France 447** (Rio to Paris, 2009, 228 killed):
  - The Airbus A330 is **fly-by-wire**. Under **Normal Law** the computer overrides pilot inputs to protect the flight envelope. Under **Alternate Law** pilots have primary control without those protections.
  - Ice crystals froze the **Pitot tubes** (airspeed sensors), the autopilot disengaged, and the plane reverted to Alternate Law.
  - A junior pilot pulled back to climb, causing a stall. The angle of attack reached 23° and then 41°, so extreme the stall warning stopped (the reading counted as invalid). Correct nose-down inputs then triggered the "STALL" alarm.
  - Controls allow only one pilot in control at a time, with no haptic feedback about the other pilot's inputs.
  - The French BEA report cited multiple factors (feedback design, crew response, communication, training). US media headlined the pilots' "loss of cognitive control." Buried in the coverage: Airbus knew of Pitot icing and was replacing those parts, but not yet on this plane.
  - Contrast with 1986 marketing of the A320, which claimed computers would protect the plane from "any dumb moves by the pilot."
  - **14 CFR 91.3**: the pilot in command is directly responsible and the final authority. Courts uphold this. "While control has been effectively distributed, responsibility has not scaled accordingly."
  - Human factors research shows **handoffs** to humans at the last minute go badly. Automation reduces awareness, and skills atrophy (**deskilling**; Bainbridge's "Ironies of Automation").
  - **Certification** covers the autopilot as software only, not human-automation interaction. Because the autopilot "didn't malfunction," the human is the only possible point of malfunction.
  - "Human error" usually means **operator** error, not the error of designers or system architects. Lederer argued pilot-error categories don't explain why accidents happen.
  - Elish notes she is **not against automation**: aviation automation has made flying much safer overall.
- **Nissenbaum's four barriers** (many hands, bugs, blaming the computer, ownership without liability) explain *why* accountability gaps occur. The moral crumple zone explains *how* humans **absorb** responsibility when those gaps arise.
- **The Therac-25 counterexample** (a radiation therapy machine in the mid-1980s; six known overdose accidents):
  - The failure was proven to be **software**, and the press said "Computer Mistake," so no moral crumple zone formed.
  - Conditions this case reveals about when moral crumple zones form:
    1. **Timing and publicity**: they form in the immediate aftermath of highly publicized accidents. Therac-25 became public about two years after the first overdose, after fault had been assigned to the manufacturer. Media shapes perceptions.
    2. **The operator's position**: the Therac operator couldn't know of the malfunction; TMI operators knew but lacked information and authority; AF447 pilots had information but were systemically disempowered.
    3. **Design versus malfunction**: Therac failed to perform as designed. TMI and AF447 **performed as designed**, and the design itself was the problem.
  - So a moral crumple zone is "more than just the articulation of a scapegoat." It is a **structural** deflection in which "the technology is maintained as faultless, while the human operator becomes the faulty feature."
- **Culture and law.** The paper focuses on cultural perceptions of blame in the US, not legal theories of liability. These perceptions **permeate formal accountability** through media and official reports. Metaphors shape legal interpretation (Froomkin, Calo). People may not use their legal rights if they believe they are at fault.
- **Robots on the road:**
  - **Uber 2018**:
    - Coverage moved quickly to the safety driver. The Tempe police chief said Uber "would likely not be at fault."
    - The NTSB preliminary report found the object classifier misrecognized the pedestrian, and the Volvo XC90's built-in safety features (automatic braking) were **disabled** in autonomous mode.
    - There were reports the driver may have been streaming TV. Given the known handoff problem, the role itself is questionable. Yet the driver faced possible vehicular manslaughter charges.
  - **Tesla Autosteer**: a proposal to have humans "sign off" on lane changes. Musk said this is "not a case of abdicating responsibility." The human backup is "at once superfluous and essential."
  - **Google**: abandoned supervised automation because it couldn't solve the handoff problem. Its accident reports (2015-2017) blamed other human drivers, but there was a pattern of rear-end crashes, perhaps because the car drove contrary to human expectations. Other drivers then become the moral crumple zone despite shared control.
  - Certifications ignore interaction, and certifying unbounded deep-learning systems is an open question.
- **Conclusion.** The concept is a provocation to rethink how responsibility is assigned when control is distributed. It challenges the "human in the loop" rhetoric of fluid cooperation. It is both a **challenge and an opportunity** for designing and regulating human-robot systems, including how human value and potential develop in human-machine teams.

**Key terms**
- **Moral crumple zone**: a human operator who absorbs moral or legal responsibility for failures of an automated system they had limited control over, protecting the system's perceived integrity.
- **Liability sponge**: the human tendency, exploited by systems and media, to soak up blame.
- **Normal accident** (Perrow): an inevitable failure in complex, tightly coupled systems.
- **Common-mode failure**: simultaneous failure of safety systems, thought too improbable to plan for.
- **Fly-by-wire; Normal Law / Alternate Law**: computer-mediated flight control; protected versus unprotected pilot-control modes.
- **Handoff problem**: the poor human performance when automation abruptly hands over control.
- **Deskilling / skill atrophy**: loss of manual proficiency under automation.
- **Certification boundary**: certifying automation as a closed component, which ignores interaction failures.

**Ties to lectures.** Central to L26 (Uber Tempe, Nissenbaum, the human in the loop as liability sponge, the questions to ask about any human in the loop). It also supports L23's MABA-MABA and autonomous-vehicle handoff critique and AI Now's point that oversight humans get "blamed for systemic failures."

---

## 4. Glossary

| Term | Definition (as used in Module 4) | Source |
|---|---|---|
| Algorithmic discrimination | Automated systems contributing to unjustified different treatment or impacts that disfavor people based on protected classifications | Blueprint for an AI Bill of Rights (L22) |
| Algorithmic management | Algorithms that direct, evaluate, and discipline workers; often "becoming management" | L24; AI Now |
| Algorithmic wage discrimination | Personalized, algorithmically set pay; AI Now urges a ban | AI Now (citing Dubal) |
| Arbitrariness (two senses) | (1) inconsistent or ad hoc decisions; (2) decisions without a valid reasoned basis | Barocas et al. (Creel & Hellman) |
| Automation bias | Deferring to automated outputs without scrutiny | L23; AI Now |
| Binary governance | Pairing individual rights (contestation) with systemic accountability (oversight) | Kaminski (L23) |
| Bright-line rules / red lines | Categorical limits or bans on practices, not just disclosure | AI Now; L24 |
| Circular economy | Strategies to eliminate waste by decoupling growth from consumption of finite resources | L25 (Wang et al.) |
| Contestability | Ability of affected people to challenge a decision and have it reconsidered | L23 (Right to Contest AI) |
| Crashworthy code | Designing software systems to fail safely, since failures are statistically inevitable | Choi (L26) |
| Deactivation | A platform locking a gig worker out; functions like firing | L24 |
| Disparate impact (big data) | Data mining inheriting prior prejudice and producing emergent discrimination | Barocas & Selbst (L22) |
| Distribution shift | Gap between training/test data and the population a model is later applied to | Barocas et al. |
| Efficiency vs. sufficiency | Doing the same with fewer resources vs. asking how much computation is actually needed | L25 |
| Ex ante vs. ex post governance | Prevention before harm (risk assessments, red teaming) vs. remedies after harm (liability) | L26 |
| Externality | Usually unintended cost or benefit imposed on people not involved in the decision | L24/L25 |
| Ghost work | Hidden human labor making AI seem autonomous (labeling, moderation, RLHF) | Gray & Suri (L24) |
| Human alternatives, consideration, and fallback | Blueprint principle: opt out where appropriate; quick access to a trained human who can fix problems | L23 |
| Jevons paradox / rebound effect | Efficiency lowers cost, which raises demand and total consumption | L25; Brookings |
| Legitimacy | Whether it is morally justifiable to use automation at all for a decision | Barocas et al.; L23 |
| Liability vs. responsibility | Legal answerability vs. causal or moral connection to harm | L26 |
| MABA-MABA trap | Assuming "men are better at / machines are better at" means human + machine = best of both | L23 |
| Moral crumple zone | Human who absorbs blame for an automated system's failure despite limited control | Elish; L26 |
| Nissenbaum's four barriers | Many hands; bugs; blaming the computer; ownership without liability | L26; Elish |
| Normal accident | Inevitable failure in complex, tightly coupled systems | Perrow (in Elish) |
| Predictive optimization | Learning decision rules from data by predicting a target that stands in for a goal | Barocas et al.; L23 |
| Procedural justice | Fairness of process (clear rules, relevant info, notice, challenge, accountable decision maker) | L23 |
| Proxy | Variable that stands in for a protected attribute or for the true outcome of interest | L22 |
| Recourse | A person's practical ability to change inputs and get a different decision | Barocas et al. |
| Remedies for robots | Legal remedies must be translated into design and code, because AI cannot obey orders | Lemley & Casey (L26) |
| Six Rs | Restricting, recommending (direct); recording, rating (evaluate); replacing, rewarding (discipline) | 2020 paper (L24) |
| Surveillance interoperability | Mutually reinforcing government, corporate, and third-party worker surveillance | Levy (in AI Now) |
| Target of convenience | Prediction target chosen for data availability rather than fit with goals | Barocas et al. |
| Technological due process | Automated government systems merge rulemaking and adjudication, hiding policy choices in code | Citron (L23) |
| Veneer of objectivity | Automation making subjective judgment appear objective | Barocas et al.; L23 |

---

## 5. Practice Questions (original, for self-study)

**Q1 (MC).** A model trained to predict which employees will "stay long-term" learns to favor applicants resembling past long-tenured staff in a historically inhospitable workplace. Which bias mechanism does this primarily illustrate?
A) Proxy discrimination via names
B) Choosing the wrong target variable
C) Overfitting
D) Automation bias

**Answer: B.** The lecture's example: tenure may measure who survived the organization, not who is a good employee. *Source: L22.*

---

**Q2 (MC).** According to Barocas, Hardt & Narayanan, machine learning in high-stakes decisions is best compared to:
A) an individual human's intuitive judgment
B) bureaucratic decision-making with procedural protections
C) a coin toss
D) market competition

**Answer: B.** The authors reject the "humans are black boxes too" analogy. High-stakes decisions like hiring and credit have traditionally been made by bureaucracies with rules and procedural protections, which ML can undermine. *Source: Barocas et al.*

---

**Q3 (Short answer).** Distinguish the two senses of arbitrariness (Creel & Hellman) and give the reading's example of the second.

**Answer:** (1) Inconsistency: decisions made ad hoc or applied unevenly, violating "treat like cases alike" and undermining people's life planning. (2) Lack of reasoning: decisions made consistently but on a basis with no valid connection to the decision maker's goals. Example: a coach consistently selecting runners by sneaker color. Automating pre-existing rules addresses (1) but not (2). *Source: Barocas et al.*

---

**Q4 (MC).** In the Obermeyer healthcare example, what additional point do Barocas et al. make beyond "the target was a poor proxy"?
A) The data was simply inaccurate
B) Cost may have reflected the health system's true goal, so the objection may be to the goal itself
C) Race was an explicit input
D) The model overfit

**Answer: B.** They warn against confusing objections to the target with objections to the goal: the system may really have aimed to cut costs. *Source: Barocas et al.*

---

**Q5 (Short answer).** Why does Citron argue that automating government rules raises due-process concerns?

**Answer:** Automated systems merge rulemaking (setting general rules) and adjudication (applying them to individuals). Programmers inevitably change or interpret rules when coding them, effectively making policy, in ways officials, courts, and the public cannot review. *Source: L23; Barocas et al.*

---

**Q6 (MC).** Margot Kaminski's "binary governance" combines:
A) federal and state law
B) individual rights and systemic accountability
C) ex-ante and ex-post liability
D) hard law and soft law

**Answer: B.** Individual contestation catches concrete errors and gives people a voice. Systemic oversight catches aggregate patterns no single case reveals. *Source: L23.*

---

**Q7 (Short answer).** What is the MABA-MABA trap, and how does the autonomous-vehicle handoff illustrate it?

**Answer:** The assumption that because "men are better at" some tasks and "machines are better at" others, adding a human to a machine system automatically yields the best of both. Human-machine systems can instead combine the worst of both and add handoff, interface, organizational, and accountability problems. A human handed control in a split-second emergency is in the loop but may be set up to fail. *Source: L23.*

---

**Q8 (MC).** Which of the following is NOT one of the "six Rs" of algorithmic control mentioned in Lecture 24?
A) Recording
B) Rewarding
C) Regulating
D) Restricting

**Answer: C.** The six Rs are restricting, recommending, recording, rating, replacing, and rewarding. *Source: L24.*

---

**Q9 (Short answer).** Give AI Now's two main reasons why transparency and data-access regimes are "necessary but insufficient."

**Answer:** (1) They ignore the power relations among workers, employers, and vendors. Knowing your wages are being lowered algorithmically is no substitute for rules that set fair wages, and trade secrecy and contracts let firms resist access. (2) They assume outside actors (workers, unions, journalists, researchers) have the resources to analyze large amounts of data, which they often lack. Knowledge is only a first step. So burdens fall on the harmed rather than on the beneficiaries, which is why AI Now prefers bright lines. *Source: AI Now.*

---

**Q10 (MC).** AI Now cites HireVue as an example of:
A) a successful bright-line ban
B) audits being used to feign accountability by mischaracterizing their scope
C) GDPR litigation by drivers
D) emotion recognition being approved

**Answer: B.** HireVue selectively released results from an audit it commissioned, leaving out the facial analysis and performance predictions it had been criticized for. *Source: AI Now.*

---

**Q11 (Short answer).** Explain the Jevons paradox and why L25 says efficiency is not the same as sustainability. What complementary concept does the lecture offer?

**Answer:** Efficiency gains lower the cost of using a resource, which can increase demand and total consumption (rebound). Cheaper AI queries could put generative AI into every search box and workflow, so total resource use rises. The lecture pairs efficiency with **sufficiency**: how much computation is actually needed, which uses are worth the cost, and where to avoid unnecessary AI. *Source: L25 (Luccioni et al.); Brookings.*

---

**Q12 (MC).** Which of the following does the Brookings piece cite as evidence that AI environmental burdens fall unevenly?
A) The NAACP's suit against xAI over turbines at a South Memphis data center
B) The Therac-25 lawsuits
C) The IB grading controversy
D) Washington State deactivation law

**Answer: A.** Also Virginia's "Data Center Alley" (rising bills, water demand, diesel-generator air pollution). *Source: Brookings.*

---

**Q13 (Short answer).** Why is the Santiago, Chile data-center case useful for thinking about governance?

**Answer:** It shows several forms of governance interacting. **Formal law**: an environmental tribunal ruled that Chile's Environmental Evaluation Agency mishandled the approval. **Corporate governance**: Google agreed to reduce water consumption. **Community governance**: residents in a drought-stricken region hired an environmental lawyer, protested, organized, and engaged Google directly. *Source: L25.*

---

**Q14 (MC).** In Elish's analysis, why did NO moral crumple zone form around the Therac-25 operators?
A) The operators were fully trained
B) The failure was proven to be software, it surfaced slowly (about two years later) after fault was assigned to the manufacturer, and the press framed it as a "computer mistake"
C) No one was harmed
D) The FAA certified the machine

**Answer: B.** Elish draws out three contrasts: timing and publicity, the operator's position (Therac operators couldn't know of the malfunction), and the fact that Therac failed to perform as designed, whereas TMI and AF447 performed as designed. *Source: Elish.*

---

**Q15 (Short answer).** Using Bryan Choi's "crashworthy code" and Lemley & Casey's "Remedies for Robots," explain why the disabled emergency braking in the 2018 Uber crash matters to liability and remedy debates.

**Answer:** Choi argues that code failures in complex cyber-physical systems are statistically inevitable, so the question is whether a developer designed the system to **fail safely** (redundancies, fallbacks, warnings, containment). Disabling the Volvo's factory collision warning and automatic emergency braking removed a safety layer; the NTSB found Uber removed redundancy and failed to manage anticipated risks. Lemley & Casey note that AI can't obey court orders, so remedies must be **translated into design**, changing the technical and organizational conditions behind the harm rather than only paying compensation. Together they point to restoring redundancy and fail-safe design, not just blaming the safety driver (which Elish would call a moral crumple zone). *Source: L26; Elish.*

---

### Bonus quick-check (one line each)
- Nissenbaum's four barriers? Many hands; bugs; blaming the computer; ownership without liability. *(L26)*
- Typical AUC of deployed risk models per Barocas et al.? About 0.7 to 0.8. *(Reading)*
- US data centers' share of electricity, 2023? 4.4%, possibly 6% by 2026. *(Brookings)*
- E-waste estimate for generative AI, 2020 to 2030? 1.2 to 5 million tons. *(L25, Wang et al.)*
- FairShare's documentation-time reduction? More than 95% in some workflow parts. *(L24)*
- Regulation making the pilot the "final authority"? 14 CFR 91.3. *(Elish)*
