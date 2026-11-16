# Module 5 Study Notes: Designing AI Governance

*AI Ethics and Policy (CU Boulder on Coursera), instructor Casey Fiesler*

These notes are for self-study. They summarize the lectures and readings and explain the concepts, and they end with practice questions I wrote myself. They do **not** answer the lab notebook prompts or the quiz questions, and they do not choose quotes for the reading activities. Where a lecture asks you to stop and write in your lab notebook, the notes only say that a prompt comes up there. The prompts themselves are left for you.

**About names:** the lecture files are auto-generated transcripts, so some names are misspelled. When a name in this file comes from a transcript, it is shown as written and, where the correct spelling is clear, followed by it in brackets. Examples: "Virgil Alameda" [Virgilio Almeida], "Margot Kaminsky" [Margot Kaminski], "Witter and Nafis" [Widder and Nafus]. If the lecture did not name a paper or author, these notes leave it unnamed too.

---

## 1. How this course is assessed (from Module 1, Lectures 01–02)

- **What the course is for:** it is about what happens *after* an ethical concern has been identified: how institutions turn concerns into laws, standards, and organizational practices, and why those efforts sometimes work and sometimes fail. It is not a list of laws to memorize. The lectures were recorded around summer 2026, and Fiesler expects specific details to go out of date. Her goal is to give you **frameworks for interpreting whatever happens next** and a sense of what questions to ask.
- **Three assessment components:**
  1. **Lab notebooks (the core assignment).** There is one notebook document per module. It has prompts tied to the readings (for each reading you give a quote you found insightful) and to the lectures (discussion-style questions). You submit it as a PDF and it is **peer reviewed**. It is graded on **completion and coherence, not correctness**. It is optional for learners who are not taking the course for credit.
  2. **Module quizzes.** These are required for all learners. They are open book and can be retaken as many times as needed. They are meant to draw your attention to important ideas rather than test recall. Each quiz ends with a few open-ended reflection questions, graded on completion, that help prepare you for the final.
  3. **Final exam (for credit learners only).** It is peer reviewed and builds on the thinking you already did in the notebooks and quiz reflections.
- **On generative AI:** Fiesler does not ban it, partly because she does not think a ban could reasonably be enforced. She asks students to think carefully about what they use it for. Because grading is essentially based on completion, there is no real incentive to hand off your thinking, and the aim of the course is to develop your own perspective.
- **On learning:** many questions in the course have no single right answer. Disagreeing with the instructor's interpretations is welcome and is a sign of engagement.

---

## 2. Module overview

Module 5 brings the course together. It moves from analyzing governance to **designing** it. Module 1 separated ethics (what ought to be done) from governance (the mechanisms that shape what actually happens). Earlier modules surveyed many such mechanisms: law, standards, audits, professional norms, markets, and technical design. Module 5 asks how to put those mechanisms together so that they actually change outcomes.

**How the lectures connect:**
- **Lecture 27** starts *inside an organization*. It covers how a principle becomes a policy, then a standard, then procedures and tools, and finally decision rights. It argues that power and incentives decide whether any of those layers matter.
- **Lecture 28** *widens the view to the whole governance environment around a problem*. It gives a step-by-step design method: harm, then mechanism, then actors and power, then sites of intervention, then a menu of tools, then a check of the policy mix. It works the method through an AI hiring example.
- **Lecture 29** *stress-tests* the designed strategy. It asks how the strategy could fail even when everyone appears to comply, and how governance can be built to detect failure, trigger action, and adapt.
- **Lecture 30** is a short closing about *you*. Governance is made of small human choices, and most people have some influence over some part of it.

The readings correspond to the first two steps. **Rakova et al.** is the empirical basis for Lecture 27 (organizational practice). **Gasser & Almeida** is the layered model that Lecture 28 uses to locate sites of intervention.

---

## 3. Lecture notes

### Lecture 27: From AI Principles to Organizational Practice

**Key points**
- **Organizational AI governance** means the rules, structures, and processes through which institutions govern their *own* development and use of AI, for example companies, universities, hospitals, and agencies. Fiesler singles this out as the area where students are most likely to have some power.
- **Principles converge but their meanings do not.** Jobin and colleagues studied 84 sets of AI ethics guidelines and found broad agreement on five principles: transparency, justice and fairness, non-maleficence, responsibility, and privacy. They also found substantial disagreement about what those principles mean, why they matter, whom they apply to, and how to implement them.
- **Mittelstadt** (recalled from an earlier module) argues that principles alone cannot guarantee ethical AI. Compared with medicine, AI development lacks common professional aims, established norms, proven methods for turning principles into requirements, and strong accountability and sanction mechanisms. Concepts like fairness are also genuinely contested.
- The hard part is usually not *which* principle to adopt but *what it requires in context* and *who decides*. Lecture examples: what fairness requires in a hiring tool, what level of risk is acceptable, whether "human oversight" means someone clicks a button or someone has real authority, and what happens when principles collide with deadlines or revenue.
- **Definition from a 2022 paper (author not named in the lecture):** organizational AI governance is a *system* of rules, practices, processes, and technological tools that makes sure an organization's use of AI fits its strategies, objectives, and values, meets legal requirements, and follows its chosen ethical principles. Governance is a system, not a single document or committee, and technical tools (such as access controls, or making a use technically impossible) govern behavior too.
- **A means can exist without its end.** An ethics review can be completed by every team and still change nothing. The review may come right before launch, descriptions may be vague, reviewers may lack data, risk thresholds may be undefined, or no one may have authority to require action. Evaluation should ask whether a process *can alter decisions and outcomes*, not only whether people comply with it.
- **Power and incentives (a 2023 interview study of AI ethics workers in tech companies, not named in the lecture):** ethics goals had broad support *in principle*, but not when an intervention would cost time or money or delay a launch. Power sat largely with product teams and product managers, who controlled resources and timelines. Interventions that arrived late were especially vulnerable. The problem is **structural, not attitudinal**. People are rewarded for launches, engagement, and revenue. A harm that was prevented leaves nothing visible to count, while a delay is immediate and measurable. So governance cannot rely only on telling people to care more.
- **Persuasion work is skilled but fragile.** Without formal authority, ethics workers build relationships, find allies, frame interventions as product quality, reputation, or liability, and choose their timing carefully. A system that depends on one person's relationship with the right product manager is fragile and puts the risk on that individual, including career risk. The study notes that these burdens can fall disproportionately on people from marginalized backgrounds.
- **The organizational moral crumple zone.** This concept from Module 4 is applied to a whole organization. Picture a responsible AI officer who is held up publicly as evidence of ethics but has no budget, cannot require review, cannot delay a launch, lacks information, and can be ignored. That person carries responsibility without authority and can absorb the blame for a structural failure. Responsibility must come with **authority, resources, information, and protection**.
- **Worker voice and collective action.** "Luca and Tan" (as transcribed) describe harm reporting in three stages: (1) a harm is identified, (2) a governance decision is made about whether and how to respond, and (3) the organization responds or does not. Knowledge of harms is spread across the organization, so governance needs channels for broader worker voice. When formal channels fail, workers may turn to whistleblowing, petitions, open letters, refusal, and other collective action, which is **governance from below**.

**Named frameworks and methods**
- **The governance stack (from principle to decision rights):**
  1. *Principles* (for example, privacy)
  2. *Policies* that turn values into expectations (for example, "don't put customers' confidential information at risk"; disclose AI use; no final employment decisions by AI without review)
  3. *Standards*, which are more specific (for example, a documented privacy risk assessment, testing across demographic groups, approval before deployment)
  4. *Procedures and tools* (exactly what counts as confidential and what not to do with it; how a team requests a review, what it submits, which office reviews, and how long it takes)
  5. *Decision rights and accountability* (who approves, who can require changes, who grants exceptions, who monitors after deployment, and who can "pull the plug")
- **The failure rule for the stack:** "a principle without a policy can become ethics theater; a policy without a process is probably difficult or impossible to follow; and a process without clear decision makers and resources just becomes a formality."
- **Rakova et al.'s four organizational questions** (see Section 4).

**Examples:** confidential data entered into commercial generative AI; ethics reviews held just before launch; the responsible AI officer as moral crumple zone; **Project Maven**. In that case Google workers objected to a U.S. Department of Defense contract that used machine learning to analyze drone footage. After thousands signed a letter saying Google should not be "in the business of war," the company did not renew the contract and then published AI principles. Fiesler's caveat: requiring workers to take extraordinary personal risks is *not* evidence of a healthy governance system.

**Scholars and papers cited:** Jobin et al. (84 guideline sets); Mittelstadt (principles alone cannot guarantee ethical AI); a 2022 paper defining organizational AI governance (unnamed); a 2023 interview study of ethics workers (unnamed); Rakova et al. (the reading); "Luca and Tan" (as transcribed) on worker voice and collective action; the moral crumple zone concept (from Module 4).

**Lab notebook:** Lecture prompt 1 comes up in this lecture. Answer it in your notebook. It is not answered here.

---

### Lecture 28: Designing a Governance Strategy

**Key points**
- **No single actor controls the governance system.** Legislatures, regulators, developers and vendors, deploying organizations, professional bodies, courts, workers, and affected communities all act at different times, for different reasons, and usually without coordination. "Designing a strategy" here means an *analytic* view: what the environment as a whole needs, who controls which levers, how interventions depend on each other, and what one actor could realistically do to strengthen the whole. The same kind of analysis can apply inside a single complex organization.
- **Start with the problem, then find its mechanism.** "The system is discriminatory" is not specific enough to design a response. Possible causes include biased historical data, proxy variables, recruiters treating recommendations as final, vendor opacity, and organizations that reward speed over fairness. Often several act together. **Each diagnosis points to a different intervention.** For example, vendor opacity points to procurement requirements for documentation.
- **The many hands problem:** systems are rarely developed, bought, deployed, and experienced by the same people. In hiring, the actors include the developer, the vendor, the purchasing company, data providers, managers who set targets, workers, investors, regulators, and applicants. Each has different knowledge and leverage, and none controls everything.
- **Gasser & Almeida's layered model** (the reading) has three layers: *technical*, *ethical*, and *social and legal*. They sit between AI systems and society and are **sites of governance controlled by different actors, not three parts of one organization**.
  - *Technical layer:* testing for disparate outcomes, evaluating training data, limiting variables, and interface design so recommendations do not look like unquestionable facts. This is necessary but **rarely sufficient**. A fairness metric does not settle whether using AI in hiring is legitimate at all, and a more accurate model does not stop discriminatory institutional practices.
  - *Ethical layer:* what counts as fair, which disparities are unacceptable, whether applicants have a right to know AI was used, whether the use is legitimate at all, and how to balance competing values.
  - *Social and legal layer:* anti-discrimination law, regulatory guidance, contestation rights, industry standards, professional norms, which regulator has authority, and what liability applies.
- **The layered model shows where to intervene but not which tool to use.** For the menu of tools, go back to **Lessig's four modalities**: law, markets, norms, and architecture (code).
- **Law design choices** come from the closing "designing AI law" section of a forthcoming AI law casebook by Margot Kaminsky [Kaminski], Paul Ohm, and Andrew Selbst. These are mostly **continua, not either/or choices**, and the trade-offs apply to non-legal policy as well.
- **Policy mixes (a 2007 paper on policy mixes and new governance arrangements, authors not named in the lecture):** tools should not be judged in isolation. Their effect depends on how they interact with the existing mix of policies, institutions, procedures, and incentives, and that mix is often an unplanned build-up of old and new rules. Design is less like building a machine from scratch and more like **coordinating within an existing system**.
- **Coherence of goals and consistency of instruments.** Goals are *coherent* when they fit a reasonably unified logic and the trade-offs are acknowledged and justified. For example, reducing bias may require collecting demographic data that privacy principles discourage, and meaningful human review costs time that efficiency goals resist. Instruments are *consistent* when they support rather than undermine each other. A counterexample is an impact assessment mandate with no procurement rule forcing the vendor to share information, or an audit with no one authorized to require changes. A further failure mode is **layering new goals or instruments on top of old ones without resolving contradictions**.
- **Documentation is infrastructure.** It looks like an administrative burden, but it feeds impact assessments, audits, and later litigation.

**The step-by-step design method (as given in the lecture)**
1. **Define the harm or problem** precisely.
2. **Identify the mechanisms** that produce it (usually several).
3. **Map the actors and their power**: who has what knowledge and which levers.
4. **Locate the sites of intervention** using the layered model (technical, ethical, social and legal).
5. **Choose forms of regulation** from a menu (Lessig's law, markets, norms, and code). For law, work through the design trade-offs below.
6. **Assess the policy mix**: are the goals coherent, are the instruments consistent, what does each tool depend on, and what might it conflict with?
7. **Assemble concrete, interlocking interventions**, each giving authority to someone who can act on it.

**Law design trade-offs (from Kaminski, Ohm, and Selbst)**

| Choice | Option A | Option B | Trade-off |
|---|---|---|---|
| **Rules vs. standards** | *Rule:* clearly specifies what must or must not happen (for example, no AI hiring tool unless it passes a specified test) | *Standard:* flexible (for example, "reasonable steps to prevent discriminatory outcomes") | Rules give clarity, consistency, and easy compliance checks, but can go obsolete or encourage doing the bare minimum. Standards adapt and allow judgment in context, but create uncertainty and can be sidestepped. This is especially hard for AI because the technology changes fast and fairness resists one fixed definition. |
| **Technology-specific vs. technology-neutral** | Targets a kind of system (for example, automated employment decision tools) | Targets the behavior or harm whatever the technology (for example, discriminatory hiring by a human, an algorithm, or both) | Specific laws respond directly to new risks, but go out of date and invite "our system is outside the definition" arguments. Neutral laws last longer and don't favor one technology, but can fit AI's structure and scale poorly. This links to the earlier "law of the horse" debate. |
| **Ex ante vs. ex post** | *Ex ante:* before deployment or harm (licensing, impact assessments, pre-deployment testing, red teaming requirements) | *Ex post:* after harm (lawsuits, penalties, corrective orders, product liability) | Ex ante can prevent widespread or irreversible harm, but is costly, slow, hard to administer, and vulnerable to regulatory capture. Ex post responds to real harm and vindicates rights, but depends on people spotting the harm and seeking redress. That is hard with AI because evidence is proprietary, decisions are spread across actors, and harms are diffuse. **Use a mix: review and later liability support each other.** |

**Worked example: AI hiring**
- **Problem:** a hiring system produces significant disparities, and applicants cannot understand or challenge its recommendations.
- **Mechanisms:** vendor opacity, pressure to process applications quickly, over-reliance on recommendations, no applicant notice or appeal, and weak access to evidence after harm.
- **Actors and power:** the vendor controls technical information; the employer controls procurement and deployment; recruiters know how the tool is actually used; applicants experience the effects; regulators have authority but lack information unless something else in the system requires it to be produced.
- **How the interventions interlock:**
  - Anti-discrimination law keeps the **employer responsible** even though the vendor supplies the tool, which gives the employer a reason to act.
  - **Procurement and contract** terms require vendor documentation of training data and performance across groups, plus continued access for testing and auditing.
  - **Internal policies**: a pre-deployment impact assessment, auditing after a set period, and real authority for whoever is responsible.
  - **Limits on automation** to address over-reliance: the tool supports recruiters but cannot auto-reject. Recruiters are trained on its limits, and audits check whether they always defer to it, with a pathway to act if they do.
  - **Notice to applicants** about automated decision-making (by law or as good practice), plus a real way to request human review or challenge inaccurate information. This requires **retaining logs and documentation**, which ties back to the documentation requirement.
  - **Ongoing monitoring and periodic independent review**, with reviewers who have authority to act, all reconciled with efficiency goals.
- **Summary of how the pieces fit:** law sets minimum rights and duties; procurement reduces vendor opacity; documentation makes assessment and auditing possible; limits on automation reduce over-reliance; notice and appeal let applicants find errors and seek remedy; monitoring provides feedback for revision; authority creates a real pathway to change. "No single tool solves the problem." A website principle such as "we don't discriminate," or a single "there must be an audit" rule, would let much of this fall through the cracks.

**Bottom line:** a governance strategy is not a checklist. It is a set of connected interventions, usually spread across actors, that makes gaps, dependencies, and limits visible.

**Scholars and papers cited:** Urs Gasser and "Virgil Alameda" [Virgilio Almeida] (the reading); Lawrence Lessig (four modalities); Kaminsky [Kaminski], Ohm, and Selbst (AI law casebook, forthcoming at time of recording); a 2007 paper on policy mixes and new governance arrangements (authors not named); "law of the horse" (from an earlier module).

**Lab notebook:** Lecture prompt 2 comes up in this lecture. Answer it in your notebook. It is not answered here.

---

### Lecture 29: Testing and Adapting Governance

**Key points**
- **Stress-test governance the way you red-team a system.** Use an adversarial, threat-modeling mindset. How could an organization evade the policy, game its metrics, exploit ambiguity, or comply on paper without meeting its purpose? Failure can also come from missing information, lack of enforcement capacity, or unintended consequences, not only from deliberate evasion.
- **Running example: mandated algorithmic impact assessments.** Precedents include the U.S. **National Environmental Policy Act** (federal agencies must assess the environmental impact of proposed actions) and the **GDPR**'s data protection impact assessments for high-risk processing. Open questions include: what counts as an impact, who defines the harms, how much evidence is needed, who reviews the assessment, and whether the mitigations have to be implemented.
- **Andrew Selbst** argues that impact assessments depend on information and expertise held by the organizations being assessed. That gives those organizations a lot of discretion and opens the door to **hollow compliance**: the process is completed while behavior stays the same. The assessment may be given to a junior employee, done after key design decisions, written vaguely, or left with aspirational mitigations that no one must act on, and it can still be pointed to as evidence of responsibility. Selbst explains this with **legal managerialism**: organizations reinterpret broad legal or ethical requirements through their existing priorities (for example, profit over safety), and they need not be malicious to do so. Fiesler connects this to ethics washing, means–ends decoupling, and ethics being absorbed into corporate logics.
- **Hollow versions of common tools:** human oversight that rubber-stamps (and may be incentivized to); transparency that is accurate but impossible to understand or act on; an audit by an auditor the organization picks and pays; and participation where a workshop is held and the plan proceeds unchanged. The point is that **you should judge a tool's effectiveness under worst-case implementation, not only ideal implementation**.
- **Participation is not the same as power.** Corbett and colleagues used the **ladder of citizen participation** to analyze participatory AI projects and found that most operated at the level of *informing or consultation* rather than *partnership, delegated power, or community control*. Consultation can be useful, but "a meeting isn't automatically power sharing and a survey isn't democratic control." This links to the **paradox of participation** from early in the course.
- **Dislocated accountability.** "Witter and Nafis" [Widder and Nafus] studied the AI supply chain. Developers recognized harms but saw them as outside their responsibility. Upstream actors said harms were the deployer's problem, deployers blamed the model or data, and developers treated business decisions as outside their role. **Modularity**, breaking systems into separate components, reinforces this by encouraging people to set aside the social context of their work. A policy aimed at one actor can therefore miss the mechanism. Instead of expecting any one actor to have a "view from nowhere," governance should create **opportunities for actors with different situated knowledge to meet across organizational boundaries**.
- **Regulation's own alignment problem.** Guha and colleagues ask whether the behavior a regulation requires will actually reduce the harm it targets.
  - **Regulatory mismatch:** the policy targets the wrong actor, object, or mechanism. Example: restricting one kind of large language model to prevent bioweapons help does little if the information is available elsewhere or smaller systems can do the same thing. Governance should start from the mechanism of harm, "not with a favorite tool."
  - **Value conflict:** goals that are each desirable can be hard to achieve together, for example demographic data for discrimination testing versus privacy and data minimization. This calls for explicit trade-offs, not a list of universally good values.
- **Practical tests:** *capacity* (does the overseer have the expertise and resources?) and *distribution* (who bears the costs: money, time, labor, career risk?). When structures are weak, burdens fall on individuals: the worker who must delay a launch, communities repeatedly asked to explain harms, and frontline workers who correct flawed recommendations while being evaluated on speed.
- **Remedies.** What happens to people already harmed? Monitoring and organizational learning **do not replace** remedies such as appeal, compensation, reinstatement, and injunctive relief. Selbst notes that **documentation from an ex ante impact assessment can make ex post accountability possible**, because records of design alternatives, testing, and reasoning help regulators and courts work out later what went wrong.
- **Changing technology.** The lecture contrasts **future-proof** regulation (broad enough to stay effective as things change) with **future-responsive** regulation (accepts that revision may be needed). The transcript is garbled at the point where the source is introduced, and the author is not named. Example: the **EU AI Act**'s risk structure was organized around systems built for particular purposes. General-purpose foundation models challenged its *whole organizing logic*, because one model can be adapted to many uses and risk levels. But adaptability must not mean rules change whenever regulated actors find them inconvenient. Unconstrained revision undermines the rule of law, so **adaptation needs its own governance**.
- **The Collingridge dilemma and the pacing problem** (from Module 1): early on, a technology's consequences are hard to predict; later, it is too embedded to change easily. Waiting for certainty doesn't work, and neither does one perfect policy. The goal is governance that can **act under uncertainty while keeping the ability to learn and correct**.

**Named frameworks and methods**

*Stress-test questions* (from the lecture, paraphrased):
1. How might an organization **meet the formal requirement without achieving its purpose**? (hollow compliance)
2. Did participation **merely gather input, or give participants power to change the outcome**? Who chose the participants, what information did they get, what could they ask, what options did they have, and what accountability exists if their recommendations are ignored?
3. Where do **information, responsibility, or authority fall between actors**? Do the people assigned responsibility have the **knowledge and power** to act?
4. Does the intervention address the **actual mechanism** producing the harm (mismatch)? What other **values or goals might it undermine** (value conflict)?
5. **Capacity:** does the overseer have the expertise and resources?
6. **Distribution:** who does the labor of making governance work, and who bears the consequences when it fails?
7. **Remedies:** what happens to people who have already been harmed?

*Designing for adaptation, in three parts:*
1. **Identify failure (observation).** Monitoring continues beyond pre-deployment testing. The **NIST AI Risk Management Framework** treats risk management as a lifecycle process in which mapping, measuring, and managing recur as the system and its context change, and it puts "people and planet" at the center of its lifecycle diagram, recognizing civil society, end users, and affected communities as sources of knowledge. Different sources catch different things: technical monitoring may catch rising error rates but miss chilling effects, while complaints show individual harms but not statistical patterns. Feedback must be **treated as legitimate evidence**, not merely collected.
2. **Triggers.** These connect evidence to a decision: a performance threshold, a pattern of complaints, a new use context, or a scheduled review date. Examples: a safety incident leads to immediate suspension and investigation; a sustained rise in error rates leads to model revalidation; a review every two years checks whether the regulation still fits the technology and market. Triggers keep monitoring from becoming theater.
3. **Revision.** Know *who can revise what, through what procedure*. Small items such as reporting templates or lists of covered applications can change easily. Fundamental changes may properly require serious authority, even legislative review.

**Examples:** NEPA; GDPR data protection impact assessments; human oversight that rubber-stamps; auditor capture; token participation; bioweapons and LLM restrictions; the EU AI Act and foundation models; a law school banning AI in first-year classes (from the news, mentioned as an example).

**Scholars and papers cited:** Andrew Selbst (impact assessments, legal managerialism, documentation enabling ex post accountability); Corbett et al. (ladder of citizen participation applied to participatory AI); "Witter and Nafis" [Widder and Nafus] (dislocated accountability in the AI supply chain); Guha et al. (AI regulation's own alignment problem); an unnamed author on future-proof vs. future-responsive regulation; the NIST AI RMF; the Collingridge dilemma and pacing problem (from Module 1).

**Lab notebook:** the final lecture prompt (prompt 3) comes up in this lecture. Answer it in your notebook. It is not answered here.

---

### Lecture 30: You Have the Power

**Key points**
- AI governance is not only done by legislators, regulators, and executives. **You are probably already part of it.**
- **Builders** make choices about data, evaluation, documentation, interface design, and whether to raise a problem before launch.
- **People in organizations that buy or use AI** can evaluate vendors, write procurement requirements, decide which uses are acceptable, create review processes, or notice when a policy isn't working.
- **Managers** decide whether an automated recommendation is advice or a final answer, and can make it safe for workers to question a system.
- **People in law, policy, compliance, education, and public service** can turn broad obligations into practice, preserve information that makes accountability possible, and recognize when new policies are needed.
- **Everyone** (as worker, consumer, student, community member, or citizen) can ask questions, organize, challenge decisions, support different products or institutions, and help make harms visible.
- **Governance is made up of small decisions.** One important thing you can do is notice *when a choice is being made*, because "this is just how the system works" tends to hide decisions about authority and acceptable risk.
- You may have information others lack, be able to connect people working in isolation, document a problem, or ask whether a policy is accomplishing its purpose or just producing filled-out forms.
- **Governance is built through human choices, so human choices can change it**, and even limited influence can shape its future.

**Frameworks and examples:** no new framework. This lecture applies the module's themes (decision rights, documentation, worker voice, hollow compliance) to the individual. No scholars are cited.

---

## 4. Reading notes

### Reading 1: Rakova, Yang, Cramer & Chowdhury (2021), "Where Responsible AI meets Reality"

**Citation:** Rakova, B., Yang, J., Cramer, H., & Chowdhury, R. (2021). Where Responsible AI meets Reality: Practitioner Perspectives on Enablers for Shifting Organizational Practices. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 7, 23 pages. https://doi.org/10.1145/3449081. The authors were affiliated with Partnership on AI, Accenture, and Spotify.

**Central thesis:** responsible AI efforts succeed or fail mostly because of **organizational culture and structure**, not technical methods alone. In current practice, the work of identifying and fixing responsible AI problems falls on **individuals**, who must do their own job, do the responsible AI work (often unpaid), redesign the structures around them, and manage the change. To scale responsible AI, organizations have to build structures and processes that **support and amplify individual efforts**, moving from reactive to anticipatory practice.

**Structure**
1. *Introduction:* the field's "practical turn" and the gap between what academic research prioritizes and what practitioners need (organizational tactics and stakeholder management, not only technical tools). It introduces Meyerson's "tempered radicals." The paper's text spells the name "Myerson"; the reference list has Debra Meyerson.
2. *Literature review:* (a) algorithmic responsibility in practice (Mittelstadt; Zeng et al.'s 74 sets of principles; Jobin et al.'s 84) and the difficulty of translating principles; (b) organizational change, comparing responsible AI to legal compliance, diversity and inclusion, and corporate privacy (Bamberger & Mulligan); Gender Shades as an external audit that created internal momentum; Raji et al.'s internal auditing framework; organizational theory (Orlikowski's duality of technology and "structurational" model; Dawson's "process turn"; Scott's rational, natural, and open systems); and multi-stakeholder meta-organizations (Berkowitz's six capabilities).
3. *Study and methods:* **26 semi-structured interviews** with practitioners at **19 organizations** on **4 continents** (21 of 26 in the US), recruited by convenience and snowball sampling. Interviews took place in late 2019. Roles included AI strategy, engineering, HR, legal, marketing and sales, ML research, policy, and product management. Data were analyzed with contextual design interpretation sessions and **affinity diagramming**. The authors also ran a workshop at an ML conference with 13 small groups.
4. *Interview results:* organized as a 4 x 3 grid (Table 2).
5. *Workshop results:* four themes or recommendations.
6. *Discussion and conclusion,* plus an appendix with the interview questionnaire.

**Key arguments and findings**
- *Overview statistics:* more than half (14 of 26) worked on their initiatives alone rather than in a team. About 40% (11 of 26) volunteered time outside their official job. 15 had official responsible AI roles. Some showed stress, and some had left their organizations by the time of submission.
- **The analytical framework (Table 2):** three states (**prevalent**, **emerging**, and **aspirational future**) crossed with **four questions every organization needs processes to answer**:

| Question | Prevalent | Emerging | Aspirational |
|---|---|---|---|
| **When and how do we act?** | *Reactive:* act only when pushed by external forces (media, regulators) | *Proactive:* act to address potential issues | *Anticipatory:* frameworks for anticipating risks |
| **How do we measure success?** | *Performance trade-offs:* conversations dominated by ill-informed performance trade-offs | *Provenance:* organization-level metrics frameworks and processes | *Concrete results:* success redefined to include societal impact |
| **What internal structures do we rely on?** | *Lack of accountability:* work falls through the cracks due to role uncertainty | *Structural support:* scaffolding built on existing structures | *Integrated:* responsible AI built into all product-related processes |
| **How do we resolve tensions?** | *Fragmented:* misalignment between individual, team, and organizational incentives and mission | *Rigid:* overly rigid incentives discourage addressing tensions | *Aligned:* tensions resolved according to the organization's mission and values |

- **Acting:** the main triggers were catastrophic media attention and legal compliance. Practitioners used reputational risk as leverage ("What if ProPublica found out about...?"). Responsible AI could be a "taboo topic," and people hit the question "whose job is this?" Full-time teams were sometimes formed only after volunteer-led bias investigations. The reactive stance **moves labor and cost onto the individual**.
- **Measuring success:** the biggest challenge was a lack of metrics that capture real impact. Inappropriate or misleading metrics were seen as an even bigger threat than missing ones. Practitioners had to squeeze their work into clicks, churn, or revenue, or argue that fixing problems before launch is cheaper. The paper lists seven challenges, including short timelines, neglect of qualitative work, leadership expecting "magic," and performance reviews that ignore responsible AI work. Emerging enablers: rewarding internal education, rewarding risk-taking for the public good, following up with internal investigations, and cross-functional mechanisms.
- **Internal structures:** concerns were heard because of seniority, not because of a system, which is fragile. Emerging structures include distributed accountability, escalation paths, internal review boards, release norms, and cross-functional roles. The aspiration is required responsible AI reviews before release, responsible AI or ML operations roles for continuous assessment after deployment, and structures that allow external scrutiny and shared industry benchmarks.
- **Resolving tensions:** individuals settle tensions ad hoc based on their own values and relationships. In the *emerging* "rigid" state, organizational processes take over but are not aligned with responsible AI goals, so this transition can **move the organization away from** the aspirational future. Not all emerging practices lead to the aspirational one. Limiting factors include rewarding unnecessary technical complexity, unclear expectations, impact that seems diffuse, reliance on high-trust relationships, and **lack of data on sensitive attributes**.
- **Workshop recommendations:** (1) **veto power** at many levels, from whistleblower protections to internal oversight committees to investors and boards, with the most important design feature being that a decision to stop **cannot be overruled**. This includes asking whether AI is appropriate at all. (2) **Balance internal and external pressure**: internal processes have more information, while external groups have more freedom and can build coalitions. (3) **Communication channels** between employees and leadership, leadership and board, and users and companies (for example, town halls). (4) **Interdependence**: the enablers work best together, so sequencing them is hard. For example, people need whistleblower protection before they will speak candidly at town halls.
- **Conclusion:** the transitions are not linear. They involve "persistent steps and coalition building." The research community should treat this less visible organizational work as a core field of study and education. In the aspirational state, change management becomes a full-time role and individuals can focus on their actual jobs.

**Key terms**
- **Responsible AI / fair-ML:** fairness-aware ML, used here broadly to cover accountability and responsibility work.
- **Prevalent / emerging / aspirational practices:** the most common current practices, shared but less common practices, and the ideal future that practitioners describe.
- **Tempered radicals (Meyerson):** employees who change their organizations through persistent small steps while relying on their own legitimacy and networks.
- **Duality of technology / structurational model (Orlikowski):** people's actions are enabled and constrained by organizational structures that are themselves products of earlier human action.
- **Open systems (Scott):** organizations are incomplete and depend on exchanges with their environment, like an ecology.
- **Meta-organizations:** standards bodies, partnerships, and multi-stakeholder initiatives through which organizations interact.
- **Ethics washing:** the appearance of ethics without substance, which emerging practices try to move beyond.
- **Veto power:** a stop decision available at many levels that cannot be overruled.

**Ties to lectures**
- Lecture 27 summarizes the four questions and the shift from reactive and fragmented to anticipatory practice.
- The paper's evidence that action depends on **seniority and individual relationships** supports Fiesler's point that persuasion-based ethics work is skilled but fragile.
- The **veto** recommendation matches Lecture 27's "who can pull the plug?" and the authority requirement for avoiding an organizational moral crumple zone.
- The finding that emerging "rigid" processes can lead away from the goal shows Lecture 27's **means without ends** and Lecture 29's **hollow compliance**.
- The **interdependence** recommendation anticipates Lecture 28's **policy mix and instrument consistency**.
- The metric problems echo the lecture point that **a prevented harm is invisible while a delay is measurable**.

---

### Reading 2: Gasser & Almeida (2017), "A Layered Model for AI Governance"

**Citation:** Gasser, U., & Almeida, V. A. F. (2017). A Layered Model for AI Governance. *IEEE Internet Computing, 21*(6), 58–62. https://doi.org/10.1109/MIC.2017.4180835. Both authors were at Harvard's Berkman Klein Center; Almeida was also at the Federal University of Minas Gerais in Brazil.

**Central thesis:** AI systems are "black boxes" that create large **information asymmetries** between developers and consumers and policymakers. Lists of substantive issues are not enough to design governance. A better approach takes inspiration from **Internet governance** and uses **modularity in the form of layering**: a three-layer model (**social and legal; ethical; technical foundations**) that sits between AI applications and society. Governance instruments can be combined *within and across* the layers, making governance a **shared responsibility among all relevant actors**.

**Structure**
1. *Introduction:* AI is quietly built into private and public decision-making (filtering algorithms on platforms, self-driving cars, face recognition, and a Stanford study claiming to infer sexuality from dating-site photos). Governments, civil society, the private sector, and academia all need to be involved. The authors explain why designing AI governance is hard: regulating separately could wrongly treat challenges as unrelated, regulating ahead of time is difficult, and a global system must handle cultural and legal differences.
2. *The nature of AI:* there is no universally accepted definition, AI is a set of techniques rather than one technology, and it is often used as an umbrella term for some degree of autonomy. The authors distinguish **weak (narrow) AI** from **strong (general) AI** and argue that weak AI already raises real governance issues today.
3. *AI governance challenges:* stakeholders usually present issue *lists*. The authors cite Calo's roadmap: justice and equality; use of force; safety and certification; privacy; displacement of labor and taxation. They add IP and liability, plus cross-cutting themes such as transparency, accountability, and explainability; inclusion and fairness; and global governance.
4. *Models for AI governance:* three **structural challenges** that become design requirements (below). Together they point **away from state-centric command-and-control regulation** toward more complex approaches used for the Internet, nanotechnology, and gene drives. They mention active matrix theory, polycentric governance, hybrid regulation, and mesh regulation. Any model must fit with existing law, especially **human rights**.
5. *The layered model:* modularity and layering (the OSI reference model; David Clark's four-layer model of cyberspace), then the three layers.
6. *Closing section:* implementation can be multi-layered and blended. Some layers would come into play only when risks are "substantial and concrete." Approaches range from market-based to government-based, and from national to international. GDPR is a regional example with its (limited) "right to explanation." Without an AI-specific international legal framework, a **global multistakeholder oversight body** could curate global principles and norms.

**Key arguments**
- **Three structural challenges, which are also design requirements:**
  1. **Information asymmetries:** few people understand the techniques, and systems are inscrutable. Governance needs mechanisms that improve **collective understanding** of AI across contexts.
  2. **Finding normative consensus:** debate focuses on risks, but AI also has benefits (for example, the Sustainable Development Goals). Governance must open space for **cost-benefit analysis and consensus-building**, especially around trade-offs, handle normative differences across contexts and regions, and allow **interoperability** among frameworks.
  3. **Government mismatches** (the text's wording): even with shared understanding and consensus, designing effective, efficient, and legitimate means is hard under uncertainty and complexity, and broader trends limit traditional lawmaking in the digital age.
- **Why layering:** modularity reduces the number of interdependencies that have to be analyzed. Layering arranges parts of a system into parallel hierarchies.
- **The three layers (from the top down):**
  - **Social and legal:** creating institutions and allocating responsibilities for regulating AI. Example: Matthew Scherer's proposed policymaking body that could define AI, create research exceptions from strict liability, and set up an AI certification process. Norms here can grow out of principles from the ethical and technical layers plus existing national and international law, including human rights.
  - **Ethical:** high-level ethical concerns that apply to all AI. Sources include human rights principles and the IEEE general principles for AI and autonomous systems. Example: an insurance algorithm that charges a group higher premiums based on gender or age violates the principle of equal or fair treatment.
  - **Technical (the foundation):** algorithms and data. It includes principles for accountable algorithms from a Dagstuhl seminar ("Data, Responsibly"): **responsibility, explainability, accuracy, auditability, fairness**, along with a suggested social impact statement. It also covers **data governance** that guards against discrimination based on race, color, national origin, religion, sex, gender, sexual orientation, disability, or family status.
- **Timing:** instruments can be developed at different times. In the near term, standards and principles for algorithms; in the mid to long term, legislation for mature AI applications from nation-states.
- **The model is a heuristic.** It shows how principles, policies, norms, and laws can be combined and work together.

**Key terms**
- **Information asymmetry:** the knowledge gap between AI developers and other stakeholders.
- **Normative consensus:** agreement among stakeholders about what is desirable, including trade-offs.
- **Interoperability:** compatibility among different governance frameworks across contexts and regions.
- **Modularity / layering:** managing a complex system by dividing it into components, and the specific form that arranges them in parallel hierarchies.
- **Command-and-control regulation:** traditional state-centric rule-setting and enforcement, which the authors argue is insufficient on its own.
- **Polycentric, hybrid, and mesh regulation; active matrix theory:** advanced governance models named as sources of inspiration.
- **Weak (narrow) vs. strong (general) AI:** task-specific systems vs. machines with general intelligence and self-awareness.
- **Data governance:** principles for collecting, using, and managing data that promote fairness and guard against discrimination.
- **Right to explanation (GDPR, "limited"):** an obligation to explain the purpose of an algorithm and the kinds of data used in automated decisions.

**Ties to lectures**
- Lecture 28 uses this model as **Step 4 (sites of intervention)**. Fiesler stresses that the layers are **sites controlled by different actors, not parts of one organization**, and that the model tells you *where* to intervene but not *which tool* to use, which is why she pairs it with Lessig.
- Fiesler's hiring example fills each layer: disparity testing and interface design (technical); what counts as fair (ethical); anti-discrimination law and contestation rights (social and legal). Her point that the technical layer is "rarely sufficient" matches the authors' view that the layers interact.
- The **information asymmetry** challenge returns in Lecture 28 (vendor opacity, regulators without information) and Lecture 29 (Selbst on assessments relying on information held by the organization being assessed).
- The authors' call to combine instruments as a **shared responsibility** connects to Lecture 28's **policy mix**. Fiesler adds that combined instruments must also be *consistent*.
- Interesting contrast: Gasser & Almeida treat **modularity** as a strength for managing complexity, while in Lecture 29 Widder & Nafus show that modularity in *development* can spread out accountability. That is a good discussion point.

---

## 5. Glossary

- **Ex ante / ex post regulation:** intervention before deployment or harm (assessments, licensing, testing) vs. after harm (lawsuits, penalties, liability).
- **Adaptation governance:** rules about *who can revise what, through what procedure*, so that adaptation is neither impossible nor unconstrained.
- **Algorithmic impact assessment:** a required process for identifying harms, affected groups, testing, documentation, and mitigation before deployment (modeled partly on NEPA and GDPR DPIAs).
- **Coherence of goals:** goals fit within a reasonably unified logic, with trade-offs acknowledged and justified.
- **Collingridge dilemma:** early on, consequences are hard to predict; later, the technology is too embedded to change easily.
- **Consistency of instruments:** policy tools support rather than undermine each other; for example, a documentation rule makes an assessment mandate workable.
- **Decision rights:** who approves, requires changes, grants exceptions, monitors, and can stop a system.
- **Dislocated accountability (Widder & Nafus):** each actor in the AI supply chain sees harms as someone else's responsibility.
- **Ethics theater / ethics washing:** visible ethics commitments without real effect on decisions.
- **Future-proof vs. future-responsive regulation:** broad rules meant to last vs. frameworks that expect and allow revision.
- **Governance from below:** worker collective action (petitions, open letters, refusal, whistleblowing) that challenges management's authority over governance decisions.
- **Hollow compliance:** completing a required process in a way that leaves behavior largely unchanged.
- **Ladder of citizen participation:** a range from informing and consultation up to partnership, delegated power, and community control.
- **Layered model (Gasser & Almeida):** technical, ethical, and social/legal layers between AI applications and society.
- **Legal managerialism (Selbst):** organizations reinterpret broad legal or ethical requirements through their existing priorities.
- **Lessig's four modalities:** law, markets, norms, and architecture (code) as ways behavior is regulated.
- **Many hands problem:** responsibility is spread across many actors, so no one controls the whole.
- **Means without ends:** a process that is completed without achieving its purpose.
- **Organizational AI governance:** the system of rules, practices, processes, and technological tools that aligns an organization's AI use with its goals, legal duties, and chosen ethics.
- **Organizational moral crumple zone:** a person given responsibility without authority, who absorbs blame for structural failure.
- **Paradox of participation:** formal inclusion alongside structures that still limit whose knowledge and interests count.
- **Policy mix:** the set of interacting policies, institutions, procedures, and incentives into which any new tool enters.
- **Prevalent / emerging / aspirational practices (Rakova et al.):** the three states of responsible AI organizational practice.
- **Regulatory mismatch (Guha et al.):** regulation that targets the wrong actor, object, or mechanism.
- **Rules vs. standards:** precise requirements vs. flexible ones (for example, "reasonable steps").
- **Stress testing governance:** an adversarial review of how a policy could be evaded, gamed, or fail in practice.
- **Technology-specific vs. technology-neutral law:** regulating a kind of system vs. regulating a behavior or harm whatever the technology.
- **Tempered radicals (Meyerson):** insiders who push for change through small, persistent steps.
- **Trigger:** a predefined condition (a threshold, complaints, a new context, a review date) that links monitoring evidence to a required decision.
- **Value conflict (Guha et al.):** desirable goals that are hard to achieve together, such as fairness testing vs. data minimization.
- **Veto power (Rakova et al. workshop):** a stop decision, available at many levels, that cannot be overruled.

---

## 6. Practice questions (original, for self-study)

*These are my own questions, written to check understanding. They are not taken from the course quizzes or notebooks.*

**Q1 (MC).** Jobin and colleagues' study of 84 AI ethics guideline sets found:
A) No overlap among principles
B) Convergence on five principles but substantial disagreement about their meaning and implementation
C) That most guidelines were legally binding
D) That fairness was absent from most guidelines

**Answer: B.** The study found broad agreement on transparency, justice and fairness, non-maleficence, responsibility, and privacy, but disagreement over what they mean, why they matter, whom they apply to, and how to implement them. This is why the hard part is translating principles, not choosing them. *Source: Lecture 27; also cited in Rakova et al. §2.1.*

**Q2 (MC).** In Lecture 27's governance stack, which item is a *procedure* rather than a *policy*?
A) "Employees must not put customers' confidential data at risk."
B) "We value privacy."
C) A document listing exactly which data types are confidential and the steps for requesting a review
D) "High-risk AI uses require review."

**Answer: C.** A and D are policies (expectations), and B is a principle. Procedures spell out exactly what to do, how, and through which office. *Source: Lecture 27.*

**Q3 (Short answer).** Explain why, according to the 2023 interview study discussed in Lecture 27, ethics interventions are vulnerable even when colleagues agree with ethical principles.

**Answer:** Support in principle does not become support for interventions that cost time or money or delay a launch. Power over resources and timelines sits with product teams and product managers, and people are rewarded for launches, engagement, and revenue. A harm that was prevented is invisible and hard to count, while a delay is immediate and measurable. The problem is structural, not that people don't care. *Source: Lecture 27.*

**Q4 (MC).** In Rakova et al.'s framework, the *emerging* answer to "How do we resolve tensions?" is labeled "Rigid." Why is this notable?
A) Rigid incentives always lead to the aspirational future
B) It shows that a move from individual to organizational processes can lead *away* from the aspirational future if the processes are misaligned with responsible AI goals
C) Rigid means tensions are resolved according to the mission
D) It refers to rigid technical metrics only

**Answer: B.** The authors note that not every emerging practice leads to the aspirational state. Overly rigid incentives, sustained by organizational inertia, can discourage addressing ethical tensions. *Source: Rakova et al. §4.5.2 and Discussion.*

**Q5 (Short answer).** Name the four recommendations from Rakova et al.'s workshop, and explain why the authors say sequencing them is difficult.

**Answer:** (1) Veto power at many levels that cannot be overruled; (2) balancing and coordinating internal and external pressure; (3) communication channels between and within levels (employees and leadership, leadership and board, users and companies); (4) designing for interdependence. Sequencing is hard because the enablers work best together. For example, whistleblower protections and a supportive culture are needed before people will speak candidly at town halls. *Source: Rakova et al. §5.*

**Q6 (MC).** Gasser & Almeida identify three structural challenges for AI governance. Which is NOT one of them?
A) Information asymmetries
B) Finding normative consensus
C) Government mismatches
D) Insufficient computing power for regulators

**Answer: D.** The three are information asymmetries, finding normative consensus, and government mismatches. Together they point away from purely state-centric command-and-control regulation. *Source: Gasser & Almeida, "Models for AI Governance."*

**Q7 (Short answer).** Fiesler says the layered model tells you *where* to intervene but not *which tool* to use. What does she pair it with, and what point does she make about what the layers *are*?

**Answer:** She pairs it with Lessig's four modalities (law, markets, norms, architecture/code) as the menu of tools. She stresses that the layers are sites of governance controlled by *different actors*, not three parts of one organization. *Source: Lecture 28.*

**Q8 (MC).** A city passes a law requiring "reasonable measures to prevent discriminatory outcomes" from any hiring process, whether it is run by people or software. On Kaminski, Ohm, and Selbst's continua, this law is best described as:
A) Rule; technology-specific
B) Standard; technology-neutral
C) Rule; technology-neutral
D) Standard; technology-specific

**Answer: B.** "Reasonable measures" is a flexible standard, and it applies regardless of technology. Trade-offs: it adapts and lasts, but creates uncertainty and can be sidestepped, and may fit AI's scale poorly. *Source: Lecture 28.*

**Q9 (Short answer).** Give an example of *inconsistent instruments* (from the lecture or your own), and explain what would make the instruments consistent.

**Answer (sample):** A law requires employers to carry out impact assessments of AI hiring tools, but nothing requires vendors to share training-data or performance information. The assessment then cannot really be done. Consistency would come from a procurement or contract requirement (or a legal duty) that vendors provide documentation, so that one tool produces the information another needs. Documentation then also supports audits and later litigation. *Source: Lecture 28.*

**Q10 (MC).** A company commissions an audit of its AI system, choosing and paying an auditor who hopes to win future contracts. Which concept from Lecture 29 does this risk illustrating?
A) Future-responsive regulation
B) Hollow compliance
C) Regulatory mismatch
D) The Collingridge dilemma

**Answer: B.** The formal requirement (an audit) is met in a way that may not achieve its purpose, because the auditor has incentives to keep the business relationship. Fiesler's point is to judge tools under worst-case, not ideal, implementation. *Source: Lecture 29 (Selbst; legal managerialism).*

**Q11 (Short answer).** Distinguish Guha et al.'s two forms of regulatory misalignment, with one example of each.

**Answer:** *Regulatory mismatch* means the rule targets the wrong actor, object, or mechanism. Example: restricting one kind of LLM to prevent help with bioweapons when the information is available elsewhere or smaller systems can do the same. *Value conflict* means desirable goals are hard to achieve together. Example: testing for discrimination needs demographic data, while privacy and data minimization discourage collecting it. The first calls for starting from the mechanism of harm, and the second calls for explicit trade-offs. *Source: Lecture 29.*

**Q12 (Short answer).** Lecture 29 describes three things governance needs in order to adapt. Name them, and explain why adaptation itself needs governance.

**Answer:** (1) A way to **identify failure**: ongoing, lifecycle monitoring drawing on several kinds of knowledge (as in the NIST AI RMF), with feedback treated as legitimate evidence. (2) **Triggers** that link evidence to decisions (thresholds, complaint patterns, new contexts, scheduled reviews). (3) A **revision** process that specifies who can change what and how. Adaptation needs governance because unconstrained revision, where rules change whenever regulated actors find them inconvenient, would undermine the rule of law. The EU AI Act's struggle with foundation models shows why revision is sometimes necessary. *Source: Lecture 29.*
