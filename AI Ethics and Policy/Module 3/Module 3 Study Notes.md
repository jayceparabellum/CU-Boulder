# Module 3 Study Notes: Data Ownership, Privacy, and Authenticity

*CU Boulder / Coursera, AI Ethics and Policy (Casey Fiesler)*
*These are self-study notes: summaries, explanations, and original practice questions. They do not contain answers to any lab notebook prompt or quiz.*

---

## 1. Module Overview

Module 3's main claim is that **much AI governance is really data governance**: "before there's a model, there's data." The module follows data through three areas where governance problems show up most clearly. **Privacy** (Lectures 15-16) covers collecting, reusing, inferring from, and predicting with data about people. **Copyright** (Lectures 17-19) covers creative works used as training inputs and AI outputs that may be unowned or infringing. **Synthetic media** (Lectures 20-21) covers faces, voices, and identities turned into data and then into digital replicas and deepfakes. Lecture 14 introduces three concepts from Longpre et al. that run through every lesson: **authenticity** (is the data what it claims to be?), **consent** (did the people or creators involved have a meaningful say?), and **provenance** (can we trace where data came from, how it moved, and what obligations attach to it?). It also introduces the idea of **data cascades**: an upstream data problem turns into a downstream legal or social one. A consent problem becomes a privacy problem, a provenance gap becomes a copyright dispute, and an authenticity failure becomes a disinformation problem. Two themes keep returning. First, **existing legal tools are imperfect proxies** for deeper concerns. Copyright stands in for consent, credit, compensation, and labor, and copyright takedowns even stand in for intimate-privacy protection. Second, **Lessig's four modalities** (law, markets, norms, architecture) all matter: platform guardrails, consent toggles, provenance metadata, and labor contracts govern alongside statutes and court cases.

**How the lectures connect**

| # | Lecture | Builds on / leads to |
|---|---|---|
| 14 | It's All About Data | Sets up authenticity / consent / provenance, data cascades, and the supply chain |
| 15 | Data Protection | Privacy as governance of the whole data lifecycle (FIPPs); consent's limits; deletion and unlearning |
| 16 | Surveillance and Prediction | Privacy harms *after* collection: aggregation, inference, prediction; due process |
| 17 | Copyright and Input | Creative works as training data; the 3 Cs; copyright as an imperfect proxy |
| 18 | Copyright and the AI Supply Chain | Where in the pipeline copying happens; fair use; international approaches; policy tools |
| 19 | Copyright and Output | Who owns AI output (human authorship); infringing outputs; platform guardrails as architecture |
| 20 | Identity and Likeness | Digital replicas; voice and face as data; trademark, publicity, labor contracts |
| 21 | Governing Deepfakes | Societal harms: liar's dividend, NCII, political disinformation; detection, watermarking, provenance |

---

## 2. Lecture Notes

### Lecture 14: It's All About Data

**Key points**
- Talk about regulating AI usually focuses on the *model* (power, benchmarks, safety, bias, explainability), but before there's a model there's data. The module's guiding claim is that **a lot of AI governance is actually data governance**. This holds across systems that predict, classify, recommend, rank, identify, and generate.
- Datasets are not neutral inputs. They shape model development, benchmarking, research agendas, and the field's values. Ask where a dataset came from, who created it, what assumptions shaped it, who was included or left out, and what context was stripped away.
- **"Data is the new oil" is a misleading metaphor.** Oil is finite, rivalrous, and tangible. Data can be copied, reused, and combined; it can be valuable in one context and harmful in another; and it is increasingly *endogenously produced*, because AI outputs become future training data. *(Note: the transcript says "Oil is infinite," which is almost certainly a transcription slip for "finite," given the contrast being drawn.)*
- Data comes from human activity but is often **detached from its original context**. A photo, a forum post, a song, a medical record, a face, or a voice is still connected to people, communities, and expectations.
- **The "Great Scrape"** (Solove & Hartzog): AI has changed the *scale and stakes* of scraping. Scraping itself is not new and not always bad (search engines, journalists, researchers do it). Scraping can be a form of surveillance: information shared in one context, for one imagined audience, gets aggregated and reused in another.
- **Three core concepts** (Longpre et al.):
  - *Authenticity*: is data or content what it claims to be? This covers deepfakes and also the training-data ecosystem: can developers tell human-made content from machine-made content once synthetic content floods the web?
  - *Consent*: did the people involved have meaningful control? It is hard because of **scale**, **reuse** (data collected in one context becomes valuable in another), and **inference** (AI generates new information). Data is also **relational**: a legal scholar argues data's purpose in the digital economy is to place people into population-based relations, which creates "supra-individual" interests. That makes individual consent "something of a legal fiction."
  - *Provenance*: the chain of custody for data. Was it scraped, licensed, donated, or curated? What permissions apply? Does it include personal or copyrighted material? Can any of this be verified? Without provenance you can't evaluate consent, copyright, or authenticity, so these become **governance prerequisites**.
- **Data cascades** (from the paper titled "Everyone wants to do the model work, not the data work"): in high-stakes domains such as health and conservation, data work is undervalued, so problems compound downstream. They can be technical, legal, ethical, or social.
- **Supply chain view** (Lee et al.): data moves through collection, dataset creation, training, fine-tuning, deployment, prompting, and generation, and different actors control different stages. Responsibility is hard to locate, so policy can't look at only one moment.
- **Transparency is infrastructure, not accountability.** Narayanan & Kapoor say harms debates happen in a "data vacuum." Longpre et al. call for standardized, interoperable provenance infrastructure. Transparency *enables* accountability but doesn't replace substantive rights, limits, and enforcement.

**Scholars / works cited:** Paullada et al., *Data and Its Discontents* (transcribed "Paldal"); a scholar critiquing the data-as-oil metaphor (transcribed "Renato"); Fiesler's own research on public data and on traceability in computer-vision datasets; Solove & Hartzog, *The Great Scrape*; Longpre et al. (reading); Solove, *AI and Privacy* (reading); Viljoen-style relational data argument (scholar unnamed in lecture; Solove's reading attributes this idea to Salomé Viljoen); Sambasivan et al. on *data cascades*; Lee et al. supply chain (reading); Narayanan & Kapoor.

---

### Lecture 15: Data Protection

**Key points**
- **AI intensifies and remixes old privacy problems** (Solove): collection, consent, secondary use, surveillance, identification, automation, accountability. AI didn't break a working system; it *exposed existing weaknesses*.
- **Privacy is not just secrecy.** Modern data protection governs the *entire lifecycle* of personal data: collection, use, sharing, retention, security, access, deletion, transfer. Small pieces of data become revealing and powerful once aggregated.
- **Fair Information Practice Principles (FIPPs)** provide a common language across privacy regimes. Typical questions: Why is data collected? Is it necessary? Was the purpose specified? Is it being reused for an incompatible purpose? Retained too long? Can people access, correct, or delete it? Is it secure? Who is accountable?
- **Issue-spotting questions for organizations:** Is personal data being processed, and at what stages (training data, prompts, outputs, logs, feedback, monitoring)? Who is responsible? Is the new AI use compatible with the original purpose? What were users told? What happens when they ask for access or deletion? With third-party vendors: what data is sent, where is it stored, and can the vendor train on it?
- **Global variety.** GDPR is influential but not universal. A comparison of **Brazil, India, and Nigeria** shows all three have data protection frameworks: Brazil has been more proactive with AI and automated-decision guidance, while India and Nigeria rely on general principles shaped by different institutional and socioeconomic constraints. Governance takes many forms: hard law, soft law, standards, markets/contracts (e.g., procurement), and architecture (Lessig).
- **Recurring tensions:**
  - *Data minimization vs. data hunger*: "what data is necessary?" vs. "what might become useful someday?"
  - *Purpose limitation vs. future reuse*: data provided for one purpose later gets used for training, ads, risk scoring, or moderation.
  - *Notice and consent stretched thin*: Zoom, Google, and X faced scrutiny for privacy-notice language about AI training. Solove's critique of **privacy self-management**: a formal disclosure doesn't produce real understanding or control.
  - *Rights vs. pipeline complexity*: deleting a database record is easy. "Deleting" data that was scraped, filtered, and absorbed into model weights is not. You might delete the file, delete the training example, retrain, modify the model, or suppress outputs.
- **Machine unlearning** (A. Feder Cooper et al., *Machine Unlearning Doesn't Do What You Think*): models don't hold separable per-person records. Two goals get conflated: **removal** (removing a datum's influence from the model) and **suppression** (preventing certain outputs). Neither guarantees the other. Unlearning can help but isn't a "magical technical fix" for compliance.
- **Privacy by design / "Design is Law."** Interface choices such as data controls, disclosures, opt-out settings, consent flows, defaults, and toggle placement can create *legal commitments*, sometimes without the design team realizing it. Rights have to be operationalized into requirements, technical constraints, and organizational responsibilities.

**Laws / cases:** GDPR (EU); Brazil, India, and Nigeria data protection frameworks; Zoom, Google, and X privacy-notice controversies.
**Scholars / works:** Solove (reading; privacy self-management); Solove & Hartzog (*The Great Scrape*, FIPPs); A. Feder Cooper et al. (machine unlearning); Lessig (architecture); *Design is Law*; an article on AI, privacy, and freedom in the Global South.

---

### Lecture 16: Surveillance and Prediction

**Key points**
- Privacy problems don't stop at collection. AI turns data into **inferences and predictions** that institutions use to classify, exclude, or act on people.
- **Bruce Schneier (2023): surveillance vs. spying.** *Surveillance* is gathering data. *Spying* is analyzing and making sense of it. Both used to be limited by human labor. The internet made surveillance cheap in bulk, and **AI makes spying cheap in bulk**: it makes surveillance data "searchable and understandable." So the governance question is what becomes possible once data exists, and not just who collected it.
- Legal frameworks traditionally focus on the **moment of collection** (consent, notice, warrant). AI gives retained data a **"second life"** through later analysis.
- **Public isn't the same as harmless.** One post or one walk down the street reveals little, but persistent tracking and aggregation reveal where someone sleeps, works, worships, gets healthcare, or seeks help. Harm comes from the *pattern*.
- **Inference** is information generated from other information: a guess or classification. AI systems are "inference machines." They can infer health conditions, pregnancy, religion, sexual orientation, or financial vulnerability from seemingly unrelated data. Examples: a 2018 paper claiming deep neural nets detect sexual orientation from faces more accurately than humans; **Cambridge Analytica**, which built on public research showing Facebook likes predict personality and political views.
- **Wachter & Mittelstadt: inferences are the "economy class" of personal data.** They often don't qualify as protected personal data, so people have rights over what they *provide* but weak rights over what is *concluded* about them. "We didn't collect it, we inferred it" opens a governance gap. Ask also whether a given inference is a *legitimate way to evaluate people*.
- **Prediction** is an inference about the future. **Matsumi & Solove's "prediction society"**: the law is better at arguing about the past than about things that haven't happened. Predictions trained on past data carry forward past discrimination, and they can be **self-fulfilling**. In predictive policing, more police go to a neighborhood, record more crime, and that record becomes new data confirming the prediction. People become risk scores and are treated as the expected outcome of their data instead of as agents capable of change.
- **Governance responses:**
  - **Procedural data due process** (Crawford & Schultz): for *predictive privacy harms*, people need notice that a prediction is being used, an opportunity to be heard, a way to challenge or correct profiles, and institutional accountability.
  - **Limits on use** of certain predictions in high-stakes contexts (ties to risk-based governance from Module 2).
  - Institutional accountability, soft law, and architecture.
- **Privacy-preserving isn't the same as non-surveillant.** A technically privacy-preserving system can still be part of a surveillance infrastructure.

**Cases / examples:** Cambridge Analytica; predictive policing; hiring algorithms; the 2018 sexual-orientation-from-faces study.
**Scholars / works:** Solove (reading); Bruce Schneier (2023); Wachter & Mittelstadt; Matsumi & Solove (*The Prediction Society*); Crawford & Schultz (*Big Data and Due Process*).

---

### Lecture 17: Copyright and Input

**Key points**
- When the data is a novel, song, photo, article, program, fan work, or voice recording, we're dealing with **human creative labor**. The **U.S. Copyright Office's 2025 report on generative AI training** uses "data" as shorthand but stresses these materials "embody creative expression." Calling them "training data" is technically accurate but **politically misleading**.
- **Copyright basics:** a hard-law system giving authors exclusive rights in original works. It protects **expression, not ideas**. The rights are reproduction, distribution, derivative works, public performance and display, and authorizing others to do these. Limits include the public domain, **fair use / fair dealing**, and **text and data mining (TDM) exceptions** in some countries. Its purpose is largely to incentivize creation.
- **Copyright as proxy battleground.** It gives creators one of the clearest *existing* legal handles on generative AI, but their concerns are broader: no consent, no credit, no compensation, not knowing what their work helped build, and competition from systems trained on their own labor. **Grimmelmann (Axios interview):** copyright isn't the right tool for AI's big societal impacts. It shouldn't serve as labor policy, privacy protection, or dangerous-content control, but that's where the fights are happening.
- **The 3 Cs: consent, credit, compensation.** The framework originates with the **Cultural Intellectual Property Rights Initiative**, a soft-law framework for respectful relationships with Indigenous / traditional-knowledge custodians. Fiesler uses it carefully, without collapsing the contexts. None of the three is a simple checkbox:
  - *Consent* is hard at scraping scale, when creators don't know their work is in a dataset, or when training rights are buried in contracts creators can't negotiate.
  - *Credit*: some creators want attribution, others don't want their names tied to bad AI outputs. And what would credit mean across billions of works encoded in weights?
  - *Compensation*: licensing money may go to publishers, labels, or platforms instead of individual creators.
- **HCI research on creators (2025 papers):** creative workers use *copyright infringement* as the formal legal language for broader grievances (dignitary harm, loss of control, lack of attribution, power imbalances) because there's no direct legal handle for those. Interviewed **writers** don't reject influence or remix in principle; they see themselves in a "creative chain." LLM training changes that chain: the "reader" becomes a dataset, company, or unknown future user, and writers lose control over what project their work builds.
- **Fandom norms (Fiesler's dissertation):** remix communities run on social norms that don't track the law. In a non-commercial gift economy, *attribution* matters a lot even though copyright doesn't require it.
- **IP as labor policy** (Xiyin Tang, transcribed "C. N. Tang"): IP law has focused on *creation* rather than *creators*. Generative AI threatens creators' bargaining power and livelihoods, so training objections are partly labor claims.
- **Copyright distorts the problem if asked to do too much** (scholar transcribed "Michaela Montagna"). It narrows "what would fair AI development look like?" into "was there infringement / fair use?" Enforcement isn't a level playing field, since those with lawyers and money benefit most, and licensing deals may *reinforce* power imbalances.
- Takeaway: creative works stay creative works when they become training data. The question is **"what happens when culture becomes infrastructure."**

**Scholars / works:** U.S. Copyright Office (2025 training report); James Grimmelmann; Cultural Intellectual Property Rights Initiative (3 Cs); 2025 HCI papers on creative workers and writers; Fiesler (fandom); Tang (IP as labor policy); Montagna(?) (copyright not the right tool).

---

### Lecture 18: Copyright and the AI Supply Chain

**Key points**
- From Lee et al.: **generative AI is not one thing** but a supply chain. Copyright concerns can't all be located in one moment called "training."
- **Stages discussed:**
  - *Data acquisition*: scraped vs. licensed vs. taken from existing datasets. **Publicly accessible doesn't mean free to use**: Instagram photos and blog posts are copyrighted just like novels.
  - *Curation*: cleaning, labeling, combining datasets; deciding whether to keep provenance metadata. A **2024 audit of dataset licensing and attribution** (Longpre et al.'s Data Provenance work) found widespread missing or inaccurate licenses and poor provenance documentation. Fiesler's research shows people can't trace their own faces into facial-recognition datasets, so they can't ask for removal.
  - *Training*: pre-training, fine-tuning, alignment (e.g., RLHF). This creates a **"many hands" problem**: a deployer may not know what's in the upstream dataset, and a developer may rely on someone else's dataset.
- **Reproduction right** is the key right at the input stage, because training pipelines make copies. The Copyright Office report flags copying at data collection and curation, training, **retrieval-augmented generation (RAG)**, and outputs. The **human-learning analogy breaks down here**: humans learn from works without making copies.
- **Fair use (U.S.)** weighs four factors: purpose and character of the use (including transformativeness and commerciality); nature of the work; amount used; and market effect. It is **fact-specific**, decided case by case with no bright lines. Relevant facts: factual vs. expressive work, lawful acquisition, whole work copied, commercial use, broad vs. competing purpose, whether outputs substitute, whether a licensing market exists, public benefit.
- **Arguments:**
  - *For*: **"Fair Learning" (2021)** argues ML training is *non-expressive use*. Works are used as raw data to extract unprotectable statistical patterns, producing a tool with a different function, which is transformative.
  - *Against*: generative AI trains on expressive works *to produce expressive outputs* that compete in the same markets.
  - *U.S. Copyright Office (2025)*: more cautious. Some training may be transformative, but it depends on the system, data, purpose, outputs, and market effects.
- **Early cases (as of summer 2026):**
  - ***Bartz v. Anthropic*** (transcribed "Bards"): training Claude on books was fair use ("exceedingly transformative"), but **building a library from pirated books** was treated differently. The **$1.5 billion settlement** with a class of authors was about pirated acquisition, not AI training as such.
  - ***Thomson Reuters v. Ross***: fair use rejected where Westlaw headnotes were used to build a *competing* legal research tool. The court noted the bypassed market for AI training data.
  - Don't over-extrapolate from either; fair use is fact-specific.
- **Other jurisdictions:**
  - **EU**: TDM exceptions. One is for scientific research by certain institutions. A broader one lets rights holders **reserve rights (opt out), including by machine-readable means**. The **EU AI Act** adds obligations for general-purpose AI providers: a copyright-compliance policy and a **summary of training content**. This model combines exceptions, opt-outs, and transparency instead of case-by-case judicial analysis.
  - **Japan**: relatively permissive toward ML uses not aimed at *enjoying* the expressive content, though less clear where systems imitate specific works or creators.
- **Policy toolbox and tradeoffs:** infringement law with exceptions; opt-outs; licensing; transparency requirements; statutory or collective licensing (as in music). **Licensing can entrench concentration** if only the biggest developers can pay and only the biggest rights aggregators can negotiate.
- **Lessig's modalities applied:** law (copyright, fair use), markets (licensing deals), norms (attribution, disclosure), architecture (metadata, technical opt-outs, provenance standards).

**Cases / laws:** *Bartz v. Anthropic*; *Thomson Reuters v. Ross*; EU TDM exceptions; EU AI Act (GPAI obligations); Japan's approach; U.S. Copyright Office 2025 report.
**Scholars / works:** Lee, Cooper & Grimmelmann (reading); Longpre et al. dataset licensing audit; *Fair Learning* (2021; widely attributed to Lemley & Casey); Fiesler's dataset traceability research.

---

### Lecture 19: Copyright and Output

**Key points**
- Two output questions: (1) **Who owns** AI-generated output? (2) Can output **infringe** someone else's rights?
- "Author" means different things: credit (ethical), payment (economic), control (practical). *Legally* it means who, if anyone, holds copyright.
- **U.S. rule: copyright requires human authorship.** The **monkey selfie** case: Naruto, a crested macaque (transcribed "Macaw"), took selfies in 2011. PETA sued on the monkey's behalf and lost, because animals can't hold copyright. The photographer also didn't own it because he didn't take the photo. The images are public domain.
- The question isn't whether a machine was involved (cameras and Photoshop are machines). It's **whether a human made the expressive choices** in the final work. Fiesler's "Knowledge Girl" demo shows that even detailed, iterated prompts may leave most expressive choices to the model.
- **U.S. Copyright Office approach:** AI-generated material alone is not protected. Human-authored elements are: text, the *selection and arrangement* of a whole work, and sufficiently original human edits. Prompts alone, where the system determines the expressive content, are viewed skeptically.
- **Jason Allen, *Théâtre D'opéra Spatial* (2022):** a Midjourney image that won the Colorado State Fair digital art competition. Despite hundreds of prompts, revisions, and edits, the Copyright Office **refused registration of the image as a whole** because too much expression came from Midjourney. *(Transcript says "Allard"/"Allen.")*
- **Other jurisdictions:**
  - **UK**: for computer-generated literary, dramatic, musical, or artistic works, the author is the **person who made "the arrangements necessary for the creation of the work."** How this applies to modern generative AI is still debated.
  - **China (Beijing Internet Court)**: recognized copyright in an AI-generated image where the user's prompting, parameter selection, and final-image selection reflected their intellectual input. The AI was not treated as the author.
  - Copyrightability is a **policy choice** about which creative labor to reward. Denying protection preserves incentives for humans and avoids flooding the system with new exclusive rights, but it creates uncertainty for people who use AI in their creative process.
- **Infringing outputs:**
  - **Memorization**: a 2025 preprint (A. Feder Cooper et al.) found most models don't memorize most books, with striking exceptions. A Llama model memorized *Harry Potter and the Sorcerer's Stone* so thoroughly that a near-complete copy could be extracted deterministically from a seed prompt of the first five words. Memorization matters for outputs *and* inputs (the weights encode a copy).
  - Infringement needs only **substantial similarity**, not an exact copy (changing character names doesn't save a copied novel). Copyright **doesn't protect ideas or styles** (wizard school, whimsical comic style) but does protect specific expression, including **characters** such as Batman.
  - ***Warner Bros. Discovery v. Midjourney* (2025)**: alleges Midjourney lets users generate Batman, Bugs Bunny, and others, even from *generic* prompts ("classic comic book superhero battle"), and could block this the way it blocks violence or nudity. Litigation so far targets the **AI company**, not the user.
- **Platform guardrails as architecture (Lessig):** ChatGPT refused Batman, even when Batman was described without being named. Gemini complied and produced Superman with a Metropolis reference. Platforms don't run a fair use analysis per prompt; they make design choices, often to reduce legal risk, which **can block legitimate uses** (parody, education, fan art). Governance is shaped by **who sues whom**.
- **Beyond copyright:** cheap substitutes for creative labor at scale; audience demand for disclosure. **Mel Stanfill's survey of fans** found them overwhelmingly negative about AI-generated fanfic and fan art, which violates fandom norms of *credit* and *non-commerciality* and the value placed on doing your own creative labor. Fans were more open to *access-oriented* uses (translation, captioning). The issue there is disclosure, authenticity, effort, and trust, not legal infringement.
- **China's labeling rules** for AI-generated or synthetic content are output governance aimed at audience knowledge, misinformation, and authenticity, not copyright.

**Cases / laws:** *Naruto v. Slater* (monkey selfie); Allen / *Théâtre D'opéra Spatial* registration refusal; UK computer-generated works provision (CDPA s. 9(3)); Beijing Internet Court AI-image case; *Warner Bros. v. Midjourney*; China's AI labeling regulations.
**Scholars / works:** U.S. Copyright Office; A. Feder Cooper et al. (memorization); Mel Stanfill (fan survey); Fiesler (fandom norms); Lessig.

---

### Lecture 20: Identity and Likeness

**Key points**
- The shift is from **expression as data to identity as data**: faces, voices, performances. These issues are usually governed by privacy, publicity rights, labor contracts, consumer protection, platform policy, and provenance systems more than by copyright.
- **Jennifer Rothman, "Copywriting People":** people aren't copyrightable ("born, not authored"), but the line is unstable because copyright already covers photos, films, and recordings of people, and digital replicas make reusable, controllable versions of a person. Copyright-like approaches could let others *own* a person's attributes or silence them. Copyright allows nearly unrestricted **transferability**, which is risky here.
- **Digital replicas** (U.S. Copyright Office 2024 report): "video, image, or audio recordings that have been digitally created or manipulated to realistically but falsely depict an individual." Examples include soundalike songs, fake endorsements, fabricated statements, and reused background-actor scans. Some are authorized, some exploitative, some deceptive.
- **"Heart on My Sleeve" (fake Drake / The Weeknd)**: copyright protects a sound recording or composition but **not the sound of a voice** as such. A voice isn't a work of authorship.
- **Trademark experiments:** Taylor Swift filed trademark applications in spring 2026 for two audio clips and an image of herself. Matthew McConaughey registered clips including "all right, all right, all right" in early 2026. Trademark concerns **source, endorsement, and consumer confusion**, so it can reach **false endorsement** and soundalike / lookalike ads (e.g., you can't use a Cher impersonator in a radio ad). But it's essentially limited to **commercial** use and won't reach political deepfakes or NCII.
- **Virtual impressment** (Lee, Cooper & Grimmelmann): a person conscripted into a performance they never gave. This is a *labor* issue, not copying.
- **SAG-AFTRA 2023 strike**: governance through *labor contract*. Mechanisms: consent; a reasonably specific description of intended use; compensation; residuals where appropriate; and additional consent for further projects or uses.
- **U.S. patchwork**: **Tennessee's ELVIS Act** extends publicity rights to voice and AI likeness; **California** has performer digital-replica protections; the proposed federal **NO FAKES Act** would create digital-replica rights.
- **Other jurisdictions:** a 2026 gov.uk report notes the **UK has no general personal image right**, only a patchwork (data protection, online safety, defamation, trademark). Some European countries have stronger personality rights. **Denmark** prepared copyright amendments giving people control over their voice and image in deepfakes.
- **Licensing vs. assignment:** the U.S. Copyright Office recommends people be able to *license* but **not fully assign** rights in their likeness, for reasons of autonomy and dignity.
- **Property claims get faster responses than dignity claims**, which previews the NCII audit in Lecture 21. Other tools: platform policies blocking voice-cloning uses, contracts requiring consent before scan reuse, provenance metadata, new licensing markets. **Bargaining power differs**: a star, a background performer, a voice actor, and an ordinary person are in very different positions.
- Core theme: "A person's voice or face doesn't stop being part of their identity when it becomes data."

**Cases / laws:** "Heart on My Sleeve"; Taylor Swift and Matthew McConaughey trademark filings; SAG-AFTRA 2023 agreement; Tennessee ELVIS Act; California digital-replica laws; NO FAKES Act (proposed); UK patchwork; Denmark's proposed amendments.
**Scholars / works:** Jennifer Rothman; U.S. Copyright Office 2024 Digital Replicas report; Lee, Cooper & Grimmelmann (virtual impressment).

---

### Lecture 21: Governing Deepfakes

**Key points**
- Moves from individual control over likeness to **societal** problems: evidence, trust, deception, and institutional response.
- **Definition** (Chesney & Citron): deepfakes are realistic digital falsifications of images, video, and audio. Luca Perriello adds that synthetic media blur the line between reality and fabrication. Lecture working definition: synthetic or manipulated media that **appears to make a claim about reality**.
- **Two problems at once:** fake evidence may be believed, and real evidence may be dismissed. The second is the **liar's dividend** (Chesney & Citron): as awareness of deepfakes grows, people caught on real recordings can more plausibly claim they're fake. Governance therefore also has to **preserve trust in real media**.
- **Not all synthetic media is harmful:** historical simulation, restoring speech, dubbing and accessibility, satire, film. SAG-AFTRA chose consent procedures, not bans.
- **NCII** (non-consensual intimate imagery). Perriello cites 2023 estimates that up to **98% of deepfake videos online are pornographic**, **99% of those depicted are women**, and about **one-third of deepfake tools** let users generate pornographic content for free. The harm persists **even when viewers know it's fake**, so labels don't fix it.
- **Lee et al. (2026 ICML position paper):** ML research focuses on **viewer-centered epistemic harms** (truth, authenticity, fraud, misinformation), while NCII causes **subject-centered dignity harms**. Policy must **match the harm**. Disclosure and watermarking fit deception, not sexual exploitation. **"Authentic doesn't mean safe"** (and synthetic doesn't mean harmful). What matters is often **consent**.
- **Audit of X's reporting pathways:** AI-generated nude images (not of real people) were reported. **All 25 reported via copyright were removed within ~25 hours; none of the 25 reported via non-consensual nudity were removed** during the three-week window. Lesson: platforms respond to **property claims** over dignity claims. Copyright again works as a proxy that victims are pushed toward. What victims actually need is fast removal, accountability, and trauma-informed processes.
- **TAKE IT DOWN Act (U.S.)** (Grimmelmann 2025 article): creates federal crimes for publishing NCII of an identifiable person without consent, covering real images and "digital forgeries," plus a **notice-and-takedown** system like copyright's. Grimmelmann warns takedown systems without safeguards can be **abused** to suppress lawful speech (sex education, consensual adult content, LGBTQ+ expression, journalism, criticism). The tension: under-regulation leaves victims without help; overbroad regulation enables censorship.
- **Political disinformation.** Brennan Center (2024) techniques: **face swaps, lip sync, "puppet master"** deepfakes, and increasingly **audio-only**. **Slovakia 2023**: fake audio of a politician and a journalist discussing election rigging spread two days before the vote. A 2024 paper argues against reading this as "one deepfake swung an election": context mattered, including low institutional trust, long-running disinformation, political amplification, encrypted channels, and a primed population. The broader problem is **epistemic instability**, which feeds the liar's dividend.
- **Policy toolbox:**
  - **Detection**: useful but fragile (evasion by new techniques, adversarial edits, false positives).
  - **Watermarking**: visible (easily removed) or imperceptible. Biden's 2023 AI Executive Order called for robust watermarking. An ICML position paper, *Watermarking without standards is not AI governance*, says watermarks must be **robust, auditable, interoperable, and enforceable**, or they become symbolic compliance or "compliance theater."
  - **Provenance**: shifts the question from "can we prove it's fake?" to "can we prove where it came from?" **C2PA** (Coalition for Content Provenance and Authenticity) content credentials help against the liar's dividend. Longpre et al. call C2PA-type tools **necessary but insufficient**: they track file origin but not copyright, consent, or privacy.
- **"Maria Pollock's"** (name as transcribed; verify spelling on the course bibliography) interviews with professional deepfake developers: they're attentive to political misinformation and trust decay but pay **less attention to NCII**, even though it's the most prevalent harm. What developers see as the problem shapes what they build. Ethical developers are constrained by deadlines, market pressure, and division of labor ("another team handles safety"), so **ethics must be built into organizational structure**.
- **All four Lessig modalities** apply. Practice reading law: **Colorado Candidate Elections Deepfake Disclosure Act (2024)**.
- Closing point: evidence has always depended on systems of trust and verification. Deepfakes make that dependence visible.

**Cases / laws:** TAKE IT DOWN Act; Colorado Candidate Elections Deepfake Disclosure Act (2024); Biden 2023 AI EO (watermarking); Slovak 2023 election audio; C2PA; X reporting-pathway audit.
**Scholars / works:** Chesney & Citron (reading); Luca Perriello; Lee et al. (2026 ICML NCII position paper); Grimmelmann (2025, TAKE IT DOWN); Brennan Center (2024);  ICML watermarking position paper; "Maria Pollock" (as transcribed); Longpre et al.; Lessig.

---

## 3. Reading Notes

### Reading 1: Longpre et al., "Data Authenticity, Consent, & Provenance for AI Are All Broken"

**Citation:** Shayne Longpre, Robert Mahari, Naana Obeng-Marnu, William Brannon, Tobin South, Katy Gero, Sandy Pentland & Jad Kabbara, "Position: Data Authenticity, Consent, & Provenance for AI are all broken: what will it take to fix them?", *Proceedings of the 41st International Conference on Machine Learning (ICML)*, PMLR 235, Vienna, 2024. (MIT Media Lab / MIT Center for Constructive Communication / Harvard.)

**Scope:** Explicitly limited to **foundation models** that are (a) *generative*, so they can produce potentially inauthentic content, and (b) *general-purpose*, so they tend to scrape vast, diverse, under-documented web data.

**Central thesis:** Foundation-model capabilities depend on massive, widely sourced, **under-documented** training data. That has produced failures in tracing authenticity, verifying consent, preserving privacy, addressing bias, and respecting copyright. **No complete data provenance system exists**, only a patchwork of partial tools that neglect key issues, aren't interoperable, or lack adoption. The authors call for a **unified, standardized data provenance framework** built through multi-stakeholder action. They argue for **unifying existing standards, not proposing a new one.**

**Structure**
1. *The Need for Data Provenance*: motivating failures.
2. *Who Needs Data Provenance?*: creators, developers, science and scholarship, broader society.
3. *Growing Interest*: documentation deficits and regulator interest.
4. *The Legal Dimension*: copyright, AI regulation, the role of lawmakers.
5. *Existing Solutions*: four categories and their tradeoffs (Table 1).
6. *Elements of a Data Provenance Standard*: five properties, plus Table 2 of metadata.
7. *Key Lessons*: recommendations per stakeholder.
8. *Conclusion*, plus an *Impact Statement* on risks of a badly designed standard.

**Key arguments and evidence**
- **Motivating failures:** **LAION-5B**, among the most widely used text-to-image datasets on Hugging Face, was removed after thousands of **CSAM** images were reported. IP lawsuits include *Tremblay v. OpenAI* and *New York Times v. Microsoft* (also *Sancton v. OpenAI*), with suits against Stability AI and Midjourney. Models can **leak PII**, generate **NCII**, produce misinformation and deepfakes, and spread bias (Buolamwini & Gebru). **Machine unlearning is of limited reliability** (it often fails to remove the information or harms the model), so *early data choices have long-term consequences*.
- **Stakeholder interests (Section 2):**
  - *Creators* pursue the **"three C's of creative rights: compensation, control, and credit"** (citing Chayka). *Note: Longpre's three C's include **control**, while the lecture's 3 Cs (from the Cultural IP Rights Initiative) are **consent**, credit, compensation.* Past computational uses of creative work, as in research and transformative works, followed social norms developed over years (citing Fiesler & Bruckman; Klassen & Fiesler). Current AI **sidesteps those norms**. Transparency would let creators consent, verify credit, and seek compensation. It also helps creators pick tools (e.g., knowing a model's coverage of a language, genre, or art style).
  - *Developers* need provenance for performance, behavior, and risk. Model behavior mirrors data composition. Documentation tools help (Hugging Face cards, the Data Provenance Initiative) and help avoid **synthetic data leaking into training sets** (model collapse risk, citing Shumailov et al.).
  - *Science* needs it for reproducibility, studying AI's economic and labor effects, and understanding increasingly opaque model-generated data (AI annotation, crowdworkers covertly using LLMs, LLM agents).
  - *Society* needs it because bias and other risks are tied to data, and social pressure can only be applied to data choices that are *visible*. Post-hoc debiasing is reactive. Communities may wish *not* to be represented (e.g., in facial-recognition surveillance). Cites data feminism (D'Ignazio & Klein) and data humanism.
- **Documentation deficits (Section 3):** popular systems (ChatGPT, Bard, Llama 2) don't disclose basic training-data information. Calls for documentation (datasheets, data statements, model cards) have seen **uneven adoption**. The problem is acute for **"datasets-of-datasets,"** huge compilations where original provenance gets lost. Regulators are interested: the EU AI Act, Biden's EO, U.S. congressional bills, Canada's voluntary code of conduct, UN recommendations.
- **Legal dimension (Section 4):**
  - Two copyright risks: **(1) training** may infringe rights in the works (and in the dataset compilations, since creating datasets involves copying), and **(2) specific outputs** may infringe. Even if pretraining is fair use, **outputs can still infringe**.
  - **Instruction-tuning, fine-tuning, and alignment datasets** are often used in ways their licenses don't permit. Because they contain expressive elements *created solely for training ML models*, using them for that purpose is **unlikely to be fair use** (Mahari et al.).
  - Infringement turns on **access**, so knowing what was in the training data is critical. Data mixing and repackaging obscure this.
  - **EU AI Act**: disclosure of training, validation, and testing data info for high-risk systems, plus a **summary of copyrighted training data** for foundation models. **GDPR** is less relevant to fine-tuning data, which generally isn't personal data under Art. 4(1).
  - **Perverse incentives**: disclosing datasets increases litigation risk, so the authors suggest **safe harbor** for organizations that disclose to regulators and the public.
- **Existing solutions (Section 5), four categories:**
  1. *Content authenticity techniques*: **C2PA** (Adobe, Microsoft, and others; cryptographically embedded, tamper-evident provenance) and **digital watermarks** (vulnerable to removal, especially for text).
  2. *Opt-in / opt-out*: **robots.txt** (no enforcement but historically respected by search engines) and extensions like learners.txt, ai.txt, DeviantArt's "noai" tag, Google's and OpenAI's crawler user agents (GPTBot). **None widely adopted.** Binary signals can't express nuanced preferences (e.g., "only non-commercial open-source models may train on my data"). **Consent registration** (Spawning AI's "consent layer," the Do Not Train Registry, haveibeentrained.com) gets consent from creators instead of web hosts, but granularity makes it burdensome.
  3. *Dataset provenance standards*: **Datasheets** (Gebru et al.), **data statements** (Bender & Friedman), **data cards** (Pushkarna et al.), **Data Nutrition Labels** (modeled on FDA labels; 55 mostly free-text questions), and the **Data & Trust Alliance Data Provenance Standard** (19 corporations including IBM, Nike, Mastercard, Walmart, Pfizer, UPS; includes lineage tracing).
  4. *Data provenance libraries*: **Common Crawl** (60% of GPT-3 training data; accurate, wide coverage, follows robots.txt, honors removal requests such as the NYT's, but limited metadata); **Hugging Face Datasets** (vast coverage but crowdsourced documentation that is uneven and often wrong); **Data Provenance Initiative** (accurate and detailed, but expert labor limits its scale).
- **Tradeoffs (Section 5.5):** authenticity tools are built-in and verifiable but cover only source and veracity, not copyright, privacy, or bias. They also apply to *atomic* units, not compilations. Opt-out tools need custom scraper code and can be ignored. Rich documentation standards trade off accuracy and adoption incentives. Libraries trade off **coverage vs. depth vs. accuracy**.
- **A unified framework should be (Section 6):** (1) **modality- and source-agnostic**; (2) **verifiable** (e.g., Wikipedia-style editing, creator confirmations); (3) **structured** (searchable, filterable, composable, so combined licenses can be inferred); (4) **extensible and adaptable** (new metadata, jurisdiction-specific requirements); (5) **symbolically attributable** (lineage traceable through data "ancestors").
- **Stakeholder recommendations:** *creators* adopt standardized annotation, tagging, and licensing. *Developers* publish structured provenance or at least aggregate statistics. *Regulators* set and enforce minimum standards, fund data libraries, and create disclosure incentives (as the DSA does for platforms). *Researchers* make provenance disclosure a publication norm. Overall: a **multi-stakeholder consortium** modeled on **W3C** or the **Data & Trust Alliance**.
- **Impact statement caveats:** a poorly designed standard could **entrench problems**. An onerous one could burden under-resourced researchers and favor big companies, and one missing bias information could create a false sense of security. A standard **can't directly address most AI harms** and is "not a substitute for well-informed AI policies."

**Key terms**
- **Data provenance**: documentation of data's origin, lineage, licenses, creators, and properties as it moves and gets repackaged.
- **Data authenticity**: whether data is genuine and from its claimed source (watermarks, embedded credentials).
- **Consent (data)**: what uses or audiences creators agree to.
- **Datasets-of-datasets**: large compilations of many datasets where provenance is often lost.
- **C2PA**: industry standard for cryptographically certifying the source and edit history of media.
- **robots.txt / Robots Exclusion Standard**: website file telling crawlers what to exclude. Voluntary.
- **Consent layer**: infrastructure (e.g., Spawning AI) for collecting creators' opt-in and opt-out preferences.
- **Symbolic attribution**: tracing sources through dataset ancestry.
- **Perverse incentives**: disclosure raises legal risk, which discourages transparency.

**Ties to lectures:** Lecture 14 adopts this paper's three concepts as the module's framework. Lecture 18's dataset-licensing audit is this group's Data Provenance work. Lecture 21 cites the paper's view that C2PA is necessary but insufficient. The idea that transparency is infrastructure, not accountability, matches the paper's own impact statement.

---

### Reading 2: Solove, "Artificial Intelligence and Privacy"

**Citation:** Daniel J. Solove, *Artificial Intelligence and Privacy*, 77 Fla. L. Rev. 1 (2025). (George Washington University Law School.)

**Central thesis:** Some say privacy law isn't the right tool for AI (Eric Goldman warns of privacy experts working "outside their swimlanes"). Solove argues that **existing privacy law falls far short, but privacy law "properly conceptualized and constituted" would go a long way** toward addressing AI's privacy problems. Privacy problems arise with **AI's inputs and outputs**. They are mostly **not new**: AI **remixes** them, blends them in ways that challenge regulatory frameworks, and amplifies them "to unprecedented levels." **"AI is not an unexpected upheaval for privacy; it is, in many ways, the future that has long been predicted,"** but it starkly exposes privacy law's long-standing flaws. He offers a *roadmap*, not a model law.

**Structure**
- **Part I, "AI: What Is Old Is New Again"**: the rise of AI; what AI is (ML, neural networks, generative AI); AI as **rebranded old technology**; **misleading metaphors**; and **against AI exceptionalism**.
- **Part II, "A Regulatory Roadmap"**:
  - A. Legal architecture (beyond individual control; harm and risk analysis)
  - B. Data collection (scraping; "consensual" collection)
  - C. Data generation (inference; malevolent material; simulation)
  - D. Decision-making (prediction; bias; automation)
  - E. Data analysis (surveillance; identification; interpretation; oversight)
  - F. Oversight, participation, accountability (transparency; due process; stakeholders; accountability; enforcement and remedies)

**Key arguments**

*Part I*
- Today's "AI" is mostly **machine learning** rebranded by "corporate consultants and marketers" (Wiggins & Jones; Eric Siegel calls AI "a big fat lie"). The history runs from McCulloch & Pitts (1943), Hebb (1949), and Rosenblatt's perceptron (1957), through "machine learning" coined in 1959 and the Minsky/Papert-induced "AI winter," to 2000s breakthroughs driven by data, cheap computing, and new deep-learning algorithms. Calo: nearly every technique was developed decades ago. What's new is compute plus data.
- **AI is "math plus data."** It is neither intelligent nor artificial. "Learning" is pattern recognition. Metaphors both anthropomorphize AI and **hide its human labor** (data labeling, curation). He compares AI to the **Mechanical Turk** hoax.
- **Against AI exceptionalism:** don't treat AI privacy issues as so unique that you miss their continuity with existing problems. A general AI law layered on top risks "adding a story to a building with an unstable and poorly designed foundation." Easterbrook's "Law of the Horse" point is partly right.

*Part II.A: Legal architecture*
- **Individual control / privacy self-management is "doomed."** U.S. **notice-and-choice** makes people read unreadable notices; opting out is the only "choice" (Hartzog & Richards; McDonald & Cranor estimate over 200 hours a year to read all privacy policies). The **GDPR requires opt-in consent** and grants rights (access, rectify, erase, portability, object, contest automated decisions) and duties (DPIAs, data minimization, records, data protection by design and default). Solove says it still puts too much weight on the individual, and duties often get performed "symbolically" (Waldman). Data is **collective and relational** (Solow-Niederman's "inference economy"; Viljoen's relational theory). The FCRA lets you correct your record but not challenge the scoring methodology. The fix: **"bring the collection and use of data under control"** with structural duties and accountability instead of individual rights.
- **Harm and risk analysis** (as in the EU AI Act's risk tiers) is a step in the right direction, but there are open problems. Kaminski notes risk frameworks fit poorly with unquantifiable, contested individual harms. Who assesses the risk? (Self-assessment is the fox guarding the henhouse; the CCPA is an exception requiring submission to regulators.) General-purpose AI is nearly impossible to risk-assess, and purpose limitation and minimization barely work for it. Timing: pre-deployment review starts to look like licensing, while post-deployment review may come too late.

*Part II.B: Data collection*
- **Scraping** (e.g., **Clearview AI** harvesting billions of photos for facial recognition used by law enforcement) violates nearly every FIPP: transparency, purpose specification, consent, minimization, retention, individual rights, and more. AI escalates scraping.
- **The secrecy paradigm** is privacy law's simplistic binary, where data is private only if concealed. In reality people share within social boundaries, there is privacy in public, and **practical obscurity** protects scattered, hard-to-find data. Law is **inconsistent**. The GDPR doesn't exempt public data (except data "manifestly made public" by the data subject in the special-category context). The **CCPA** exempts "publicly available information" broadly, as do Utah and Virginia; **Colorado** and **Connecticut** define it narrowly. The **FCRA** and **HIPAA** protect data even when it's public. Platform **terms of service** (e.g., LinkedIn's) restrict scraping. **Carpenter v. United States** (geolocation reveals an "intimate window"; warrant required) and **DOJ v. Reporters Committee** (a compiled FBI "rap sheet" of public records still carries a privacy interest) both reject the idea that public means unprotected. Recommendations: protect obscurity, **require organizations to protect against scraping** (letting data be taken is functionally sharing it), and require governments to place conditions on public-records access (supported by **LAPD v. United Reporting**).
- **"Consensual" collection is a fiction.** In 2023 **Zoom** changed its notice to allow AI training "for any purpose" with a perpetual license, then backtracked. **Google** and **X** also updated policies to train on public information. Opt-in barely improves readership (clicking "I agree" increased reading by about 1%). With generative AI, uses are unknowable, so consent becomes "a blank check," or in Bietti's words a "free pass."
- **The flip side:** strict consent rules could starve AI and benefit incumbents. The GDPR has **six lawful bases** (consent, contract, legal obligation, vital interests, public interest, legitimate interests), and legitimate interests is the most plausible but uncertain one. Small firms can't get consent at scale. *hiQ v. LinkedIn* raised the competition angle (Solove thinks the court was wrong to put competition above privacy). Excluding EU data could **skew models** toward the cultures of places where data flows more freely.

*Part II.C: Data generation*
- **Inference via the "aggregation effect":** small bits combine to reveal much more. The **Target pregnancy prediction** case: unscented products, vitamins, and cotton balls signaled pregnancy, and a father learned of his teen daughter's pregnancy through baby ads. Inferences harm when **accurate** (exposure) *and* when **wrong** (bad decisions). Laws regulate *collection*, not *generation*, so **inference is an end-run around collection limits**. Wachter & Mittelstadt propose a **"right to reasonable inferences"** (ex-ante justification for high-risk inferences). Solove calls this good but "far from enough" and says inference demands a "complete overhaul." Inference can also evade **confidentiality protections** (privileges, GINA's ban on employers acquiring genetic information) and **defeat de-identification** (re-identification undermines HIPAA and CCPA carve-outs). The law should treat inferred data on par with collected data.
- **Malevolent material:** hallucinated defamation (ChatGPT falsely named a law professor as a sexual harasser), deepfake porn (Taylor Swift images), voice-clone **kidnapping scams**, and security threats (malware help, **prompt injection**, **data poisoning**). **Section 230** has been read broadly to wipe out distributor liability (*Zeran v. AOL*). Citron notes more than 9,500 sites host NCII. Breach notification "isn't a vaccine or a cure." The law should place responsibilities on **AI tool creators**.
- **Simulation:** AI posing as human is deception (Pasquale: chatbot programmers act as "counterfeiters"). The Turing test assumes reality doesn't matter if the simulation convinces. Even with transparency, simulations manipulate emotionally (the film *Her*). People should know when they're interacting with AI, and law must recognize the special power of human simulation.

*Part II.D: Decision-making*
- **Prediction** (Matsumi & Solove) rests on two assumptions: history repeats, and similar people behave similarly. Its problems:
  - (a) **Threat to human agency**: judging people for acts not yet done. Véliz: forecasting people like weather treats them "like things." ***Wisconsin v. Loomis***: **COMPAS** risk score used in sentencing; the court rejected the due process challenge because the judge wasn't bound by it, despite trade-secret opacity and later ProPublica findings of bias against Black defendants. Automation bias (Ben Green). *Minority Report*. Geddes: punishment for "membership of a statistical group."
  - (b) **Fossilizing the past**: biased history projected forward. Taleb's **black swans**.
  - (c) **Self-fulfilling prophecies**: more policing leads to more arrests.
  - (d) **Beyond accuracy**: a right to correct doesn't work for predictions, which are neither true nor false yet. Process fixes like Loomis's are superficial, an "appearance of legality." The law should ensure **fair** decisions.
- **Bias:** Lobel and Sunstein argue algorithms can debias, but AI **systematizes** bias under a neutral veneer and can snuff out the gradual social change that comes from individuals deviating. "All data is dirty" (Broussard). Mayson: "bias in, bias out." **Amazon's hiring algorithm** favored men. Eaglin and O'Neil: data choices are moral. Gillis's **"input fallacy"**: removing protected attributes doesn't help because proxies encode them. **Novel discrimination** can arise from arbitrary correlations (e.g., eye color, height, baldness). Substance, not just process, has to be examined.
- **Automation:** **quantification and depersonalization** (Burk: radical decontextualization; Quetelet; Cohen: people aren't "the sum of their transactions"). **GDPR Art. 22** gives a right not to be subject to *solely* automated decisions with legal or similarly significant effects, plus human intervention, the right to express a view, and the right to contest. Its limit is the word "solely," since most decisions are hybrid; Solove suggests a "material role" threshold instead. The CCPA gives some automated-decision rights (opt out, logic, likely outcome). **Humans in the loop aren't a cure**: hybrids can produce the "worst of both worlds" (Crootof, Kaminski & Price), automation bias (Kaminski & Urban), "oil and water" (Green). The goal is **fair decisions**.

*Part II.E: Data analysis*
- **Surveillance:** Bentham's **Panopticon** and Foucault. Cohen: surveillance constrains free thought and democracy. **Schneier**: AI makes surveillance data "searchable, and understandable, in bulk." Surveillance (gathering) vs. spying (analysis) is limited by human labor, which AI removes.
- **Identification** by face, gait, or voice has a history of oppression: slave passes, Nazi ID cards, Rwanda, and **1940 census data used for Japanese American internment**. Facial recognition is "the perfect tool for oppression" (Hartzog & Selinger). AI is "the perfection of the surveillance society."
- **Interpretation and deciphering:** Kerr argues the Fourth Amendment regulates *access*, not understanding (decryption, translation). AI's capacity to decipher, re-identify, and infer creates a **paradox of the heap**: a line must be drawn, though it's hard to draw.
- **Limitation and oversight:** the **third-party doctrine** (*United States v. Miller*, bank records; *Smith v. Maryland*, pen registers), only partly curtailed by Carpenter. The government can buy data, and the Fourth Amendment says little about post-collection analysis or retention. Law enforcement are "like kids in a toy store." He calls for independent oversight, use rules, and accountability.

*Part II.F: Oversight and accountability*
- **Transparency** (Pasquale's "black box society"): what should be disclosed, existence, logic, or training data? GDPR Arts. 13-15 require "meaningful information about the logic involved." But ML isn't explainable (Suleyman), training data can't be disclosed without violating others' privacy, systems are dynamic, and **trade secrets** block scrutiny (Loomis; Wexler). Don't over-rely on transparency, but don't abandon it either: details *about* training data can be disclosed and experts can vet algorithms.
- **Due process:** Citron's *Technological Due Process*; Citron & Pasquale's *Scored Society* (procedural protections for scoring "rulemaking" and "adjudication"). Kaminski & Urban: U.S. proposals favor system-wide risk mitigation over individual due process. Crawford & Schultz: a neutral party should examine complaints. Individuals need a voice, but protection shouldn't rest mostly on individual challenges.
- **Stakeholder involvement:** Okidegbe on the exclusion of affected communities from pretrial-algorithm governance. Solow-Niederman: AI lacks an active public voice.
- **Accountability:** privacy officers, PIAs, documentation, and audits (Pauline Kim: bias lies in social processes, not just code). Gillis & Simons: accountability should be central, since having to justify conduct changes it. Waldman criticizes compliance models and wants regulator and academic audits for adherence to social values. He calls for a mix of internal and external mechanisms with meaningful consequences.
- **Enforcement and remedies:** deleting data doesn't touch the **"algorithmic shadow"** (Tiffany Li), so unlawful collection still pays. **Algorithmic destruction** (FTC, *In re Everalbum* (2021), deletion of models built on improperly collected data) may be too harsh for startups, implausible for giants like OpenAI, and overkill if only some data was tainted, though it can fit where most data was improper or the harm is serious. Huge AI rewards dwarf fines: "better to ask for forgiveness than permission"; "move fast and break things."

**Key terms**
- **Privacy self-management**: the model where individuals manage their own privacy via notices and choices.
- **Notice-and-choice**: the U.S. approach where organizations may do what they disclose if users proceed.
- **AI exceptionalism**: treating AI privacy problems as wholly new and separate.
- **Secrecy paradigm**: the view that information is private only if hidden.
- **Practical obscurity**: privacy interest in data that is technically public but hard to find or scattered.
- **Aggregation effect**: combining small data points reveals far more than each alone.
- **Inference economy** (Solow-Niederman): organizations generate new information about people from collected data.
- **Right to reasonable inferences** (Wachter & Mittelstadt): ex-ante justification for high-risk inferences.
- **Input fallacy** (Gillis): removing protected attributes from inputs doesn't yield unbiased outputs.
- **Algorithmic shadow** (Li): the persistent imprint of training data in a model after deletion.
- **Algorithmic destruction / disgorgement**: ordering deletion of models trained on improperly obtained data.
- **Third-party doctrine**: no reasonable expectation of privacy in data given to third parties.
- **Automation bias**: overconfidence in and deference to machine outputs.

**Ties to lectures:** Lecture 15 is built on Solove's "remix" thesis, privacy self-management, and the Zoom/Google/X notice changes. Lecture 16 draws on the inputs/outputs framing, Schneier's surveillance vs. spying, Wachter & Mittelstadt, the prediction society, self-fulfilling predictions, and Crawford & Schultz due process. Lecture 14 draws on relational data and consent as fiction. Lecture 21 connects through malevolent material and deepfakes (Solove cites Chesney & Citron).

---
### Reading 3: Chesney & Citron, "Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security"

**Citation:** Bobby Chesney & Danielle Keats Citron, *Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security*, 107 Cal. L. Rev. 1753 (2019). (Chesney: University of Texas School of Law, co-founder of Lawfare. Citron: then Boston University School of Law, VP of the Cyber Civil Rights Initiative.)

**Central thesis:** Harmful lies aren't new, but **machine-learning-driven deep fakes**, defined as "hyper-realistic digital falsification of images, video, and audio," take the ability to distort reality to a new level. They are increasingly realistic, resist detection, and **diffuse rapidly** to sophisticated and unsophisticated actors alike. Today's networked information environment and our **cognitive biases** amplify them. The authors offer what they call the first in-depth assessment of deep fakes' causes, costs, and benefits and survey possible responses: technology, civil and criminal law, agencies, coercive state tools, and markets. They conclude that **"there are no silver-bullet solutions."** They also warn that deep fakes create incentives for **privacy-destructive** countermeasures.

**Structure**
- **Introduction**: the **Emma González** case. After Parkland, a real image of her ripping up a shooting target was faked to show her ripping up the U.S. Constitution, and it went viral (amplified by actor Adam Baldwin). Harm was limited because the original was easy to find, journalists debunked it, and the fake was poor quality. Many believed it anyway.
- **Part I, Technological foundations**: (A) emergent technology; (B) diffusion; (C) "fueling the fire."
- **Part II, Costs and benefits**: (A) beneficial uses (education, art, autonomy); (B) harmful uses: (1) to individuals and organizations (exploitation, sabotage); (2) to society (nine categories, ending with the **liar's dividend**).
- **Part III, What can be done?**: (A) technological solutions; (B) legal solutions (problems with a ban, civil liability, criminal liability); (C) administrative agencies (FTC, FCC, FEC); (D) coercive responses (military, covert action, sanctions); (E) market solutions (immutable life logs, platform speech policies).
- **Conclusion**: credible fake audio and video have magnified impact, and legal and policy architecture isn't designed to respond. "A great deal of further creative thinking is needed."

**Key arguments**

*Part I: Technology and diffusion*
- **Neural networks** learn from examples. University of Washington researchers produced the "Synthesizing Obama" lip-sync video. **Generative adversarial networks (GANs)**, invented by Ian Goodfellow, pair a **generator** that produces samples mimicking a dataset with a **discriminator** that judges them, iterating until the fakes are convincing. Audio: DeepMind's WaveNet, Baidu's DeepVoice, Lyrebird (whose "ethics" statement invokes technological determinism). Government research includes DARPA's **MediFor** program.
- **Diffusion is inevitable** (Wittes & Blum): there's no scarce tangible chokepoint like plutonium, only knowledge, which academics and companies want to spread. A Reddit user's celebrity face-swap porn tool started the "deep fake" wave, then **FakeApp** spread it to the public. A NYT reporter made a face-swap with 1,861 images of himself and 1,023 of Chris Pratt.
- **Fueling the fire**: the media model shifted from few-to-many to many-to-many, with less gatekeeping (though platforms still control infrastructure and terms of service). Three cognitive dynamics: **(1) information cascades**, where people pass along what others seem to believe instead of their own information; **(2) attraction to negative and novel information** (Vosoughi et al.'s Twitter study: falsehoods reached people about 10 times faster and were 70% more likely to be retweeted, driven by humans, not bots); **(3) filter bubbles**, where those who consume fake news rarely see the fact-checks. Together these produce "information tribalism."

*Part II.A: Benefits*
- **Education**: historical figures "speaking" to students; altered film scenes to illustrate hypotheticals; the BuzzFeed Obama video warning about deep fakes.
- **Art**: Peter Cushing "resurrected" in *Rogue One*; Carrie Fisher's dialogue in *The Last Jedi*; satire, parody, activism.
- **Autonomy**: restoring speech to people with ALS in their own voice; avatar experiences, including for people with disabilities.

*Part II.B.1: Harms to individuals and organizations*
- **Exploitation**: extortion and **sextortion**; fake kidnapping evidence; sexual exploitation, as in a now-closed subreddit of deep-fake celebrity porn with more than 100,000 users, and a user who made a video of a former classmate from about 380 scraped Instagram and Facebook photos. **Gendered**: most victims will be women. Mary Anne Franks: "If you were the worst misogynist in the world, this technology would allow you to accomplish whatever you wanted." Robin West: sexual threats "literally, albeit not physically, penetrate the body." Victims suffer humiliation, fear, and job-market consequences (journalist **Rana Ayyub**). Also false endorsements.
- **Sabotage**: reputational attacks in work, romance, sports, business, and politics. A fake released at a draft (modeled on **Laremy Tunsil**'s real 2016 video, which may have cost him about $16 million) shows that **debunking can come too late**. More than 90% of employers use search results (2009 Microsoft study). Fakes can derail mergers and contract bids.

*Part II.B.2: Harms to society*
- (a) **Distortion of democratic discourse**: erodes the shared factual foundation and lets people "live in their own subjective realities."
- (b) **Manipulation of elections**: **decisional chokepoints** are narrow windows where irrevocable decisions get made, such as a fake released right before a vote. Example: Russia's 2017 operation against **Macron** (hacked and altered documents) fizzled because of poor tradecraft, Macron's decoy documents, and bad timing, but it was "a bullet dodged."
- (c) **Eroding trust in institutions**: FBI, ICE, judges, religious groups, Planned Parenthood, the NRA.
- (d) **Exacerbating social divisions**: the Russian IRA's 2016 operations (Jade Helm conspiracies, staged Houston protests, Texas secession). Video's emotional punch can mobilize people to act (cf. Pizzagate).
- (e) **Undermining public safety**: Holmes's "fire in a crowded theater"; the Hawaii false missile alert; IRA hoaxes about a Louisiana chemical disaster and Ebola in Atlanta.
- (f) **Undermining diplomacy**: the Qatar crisis possibly sparked by fake quotes on a hacked news site; fakes timed to summits to box in governments.
- (g) **Jeopardizing national security**: wartime deception (Operation Bodyguard); battles for "hearts and minds" in Iraq and Afghanistan; fakes of U.S. soldiers provoking attacks; post-Snowden-style pressure on intelligence agencies; mixing real leaked documents with forgeries (Belfer Center).
- (h) **Undermining journalism**: newsrooms chilled from reporting real events and vulnerable to sting operations (cf. the Roy Moore sting attempt on the Washington Post).
- (i) **The liar's dividend**: the most important concept for the course. Deep fakes make it easier to deny the truth. As the public learns about deep fakes, liars can more credibly dismiss **authentic** evidence as fake, so the dividend "flows, perversely, in proportion to success in educating the public." This fits broader "fake news" truth skepticism. **Truth decay plus trust decay creates space for authoritarianism.**

*Part III.A: Technology*
- Detection must keep pace with generation, wouldn't stop narrowly distributed fakes, and won't sway people in the grip of cognitive bias. Provenance and authentication systems are product-specific and only useful once ubiquitous. **Hany Farid** (creator of PhotoDNA): "We're decades away" from conclusively telling real from fake. DARPA's GAN-vs-detector contest drew skepticism from its own program manager. **"The defense... is currently faring poorly"** in the arms race.

*Part III.B: Law*
- **No outright ban**: undesirable, because manipulation isn't inherently harmful and a ban would chill art, education, and parody and invite politicized enforcement. Probably **unconstitutional**: *New York Times v. Sullivan* (false speech is protected when banning it would chill truth) and ***United States v. Alvarez*** ("falsity alone" doesn't remove First Amendment protection, and false statements on matters of public concern get strict scrutiny). But **narrowly tailored** bans on unprotected categories are possible: defamation, fraud, true threats, incitement, speech integral to crime (extortion), and **impersonation of government officials** (Helen Norton).
- **Civil liability, threshold obstacles**: **attribution** (anonymity, Tor), **jurisdiction** (foreign creators), **cost** and judgment-proof defendants, and the **Streisand Effect** (suing publicizes the fake).
- **Suing creators**:
  - *Copyright*: only if the victim took the source photo herself, and fair use is uncertain.
  - *Defamation*: negligence for private figures (*Gertz*), **actual malice** for public figures.
  - *False light*.
  - *Intentional infliction of emotional distress* ("extreme and outrageous" conduct, which deep-fake sex videos would likely meet).
  - *Right of publicity*: requires commercial gain, so it's limited to fake-endorsement cases, with newsworthiness defenses.
  - *Public disclosure of private facts* and *intrusion on seclusion* fit poorly because the source images are often public and there's no intrusion into a private space.
  - Strongest options: defamation, false light, and IIED.
- **Suing platforms, Section 230**: (c)(1) bars treating platforms as publisher or speaker of user content. (c)(2) protects good-faith filtering (a response to *Stratton Oakmont v. Prodigy*). Courts have stretched it into a **"super-immunity"** (*Herrick v. Grindr*, among others): "power without responsibility" (Tushnet). FOSTA (2018) carved out sex trafficking. **Proposal (Citron & Wittes): make (c)(1) immunity conditional** on taking **"reasonable steps"** to prevent illegal uses of the platform, with safeguards such as a sunset clause plus data gathering, damages caps, a federal anti-SLAPP provision, and notice/exhaustion before suit.
- **Criminal liability**: it gets around judgment-proof defendants and has better investigative tools, but law enforcement's record on online abuse is poor. Relevant laws: **federal cyberstalking (18 U.S.C. § 2261A)**, state **online impersonation** laws (e.g., Cal. Penal Code § 528.5; the Texas statute upheld in *Ex parte Bradshaw*), criminal defamation, and incitement to riot (18 U.S.C. § 2101, limited by *Brandenburg*'s imminence requirement). **Election-lie laws** are often struck down (*Susan B. Anthony List v. Driehaus*; *281 Care Committee v. Arneson*; *Brown v. Hartlage*). Foreign state actors are beyond reach.

*Part III.C: Agencies*
- **FTC**: deceptive advertising and fake endorsements, plus UDAP authority. But fake news "induce[s] someone to believe an idea," not buy a product (Vladeck), and Section 230 and the First Amendment get in the way.
- **FCC**: lacks jurisdiction over social media "edge providers" (after the 2017 reversal of the 2015 ISP reclassification), so its role is limited to broadcast.
- **FEC**: regulates financing and sponsorship disclosure, not truth. It could require disclosure that campaign content is fake, but platforms resist disclosure rules and issue ads fall outside them.

*Part III.D: Coercive responses (foreign actors)*
- **Military**: information operations, network disruption, even kinetic strikes, subject to the law of armed conflict's distinction principle. **Covert action** (50 U.S.C. § 3093): degrade a foreign actor's ability to make fakes, or impose costs. **Sanctions** under **IEEPA**: Obama's EO 13694 (2015) and its 2016 amendment (EO 13757) covering election interference, and the Trump administration's 2018 sanctions on the IRA. The authors **recommend a new national emergency declaration** aimed specifically at foreign injection of false information into U.S. political debate.

*Part III.E: Markets*
- **Immutable life logs as an alibi service**: wearables, encryption, and blockchain records that let a victim prove where they were. The authors **urge caution** because of the **"unraveling of privacy"** (Peppet: holdouts look like they're hiding something), a **"database of ruin"** (Ohm), Cambridge-Analytica-scale exploitation, and government access (*Carpenter* suggests a warrant would be needed). Their point is that **deep-fake defenses can themselves be privacy-destructive.**
- **Platform speech policies (terms of service)** are "the single most important documents governing digital speech." Twitter bans impersonation, and Google's non-consensual pornography policy covers deep fakes. Platforms should adopt **technological due process**: transparent rules, exemptions for satire, parody, art, and education, notice and appeal for removals, and **no exclusive reliance on automated filtering** (false positives and negatives), except for re-uploads of content already found fake with due care. Facebook was starting to track fake videos and favor verified sources.

**Key terms**
- **Deep fake**: hyper-realistic digital falsification of images, video, or audio, usually made without the subject's consent.
- **GAN (generative adversarial network)**: generator and discriminator networks trained against each other.
- **Information cascade**: people relay what others seem to believe, which snowballs credibility.
- **Filter bubble**: algorithmic and social sorting into belief-confirming information.
- **Decisional chokepoint**: a narrow window when irrevocable decisions are made (election day, a draft, a summit), so a well-timed fake does damage before debunking.
- **Liar's dividend**: the benefit liars get from public awareness of deep fakes, which lets them dismiss real evidence as fake.
- **Sextortion**: coercing sexual images or acts by threatening to release (real or fake) intimate content.
- **Section 230 (CDA)**: immunity for platforms from liability for user content ((c)(1)) and for good-faith filtering ((c)(2)).
- **Technological due process** (Citron): transparency, notice, and a chance to contest automated or platform decisions.
- **Immutable life log / authentication trail**: a continuous, tamper-proof record of one's life used as an alibi.
- **Truth decay / trust decay**: erosion of shared facts and of trust in institutions.

**Ties to lectures:** Lecture 21 takes its definition of deep fakes and the **liar's dividend** from this reading, plus its point that deep fakes have benefits (accessibility, education, art) and its emphasis on the **gendered** nature of sexual deep fakes. The paper's finding that copyright helps only if the victim took the photo, and that privacy torts fit poorly, anticipates Lecture 21's X audit showing victims pushed toward copyright takedowns. Its Section 230 discussion connects to Solove's critique of Section 230 under "malevolent material." The paper predates the TAKE IT DOWN Act and state election-deepfake disclosure laws such as Colorado's, which can be read as later, narrower responses to the problems it describes (its skepticism of election-lie bans versus its openness to disclosure requirements).

---


### Reading 4: Lee, Cooper & Grimmelmann, "Talkin' 'Bout AI Generation: Copyright and the Generative-AI Supply Chain"

**Citation:** Katherine Lee, A. Feder Cooper & James Grimmelmann, "Talkin' 'Bout AI Generation: Copyright and the Generative-AI Supply Chain," *Journal of the Copyright Society of the U.S.A.* (forthcoming 2024). The copy assigned is the draft of March 1, 2024.

**Central thesis:** "Does generative AI infringe copyright?" has no yes-or-no answer. "Generative AI" is not one product. It is an ecosystem of systems with different architectures, data, training methods, and deployment modes. Copyright law is also complicated, and generative AI touches many corners of it: authorship, similarity, direct and indirect liability, fair use, licensing, remedies, and more. The authors propose the **generative-AI supply chain** as the framework for reasoning about these questions. Copyright touches *every* stage of that chain. Liability at one stage often depends on choices made by actors at other stages.

**Structure**
- **Part I (technical background):** what generative AI is (models embedded in larger systems; transformers, diffusion, scale), followed by the eight-stage supply chain.
- **Part II (doctrine), Sections A-N:** authorship; the exclusive rights; substantial similarity; proving copying; direct infringement; indirect infringement; Section 512; fair use; express licenses; implied licenses; remedies; copyright management information (CMI); right of publicity; hot news misappropriation.
- **Part III, "Which Way from Here?":** (A) four possible liability regimes courts might settle into and (B) six lessons for courts and policymakers.
- **Part IV:** a short conclusion.

**The eight supply-chain stages (Part I.C)**
1. **Creation of expressive works:** people write, photograph, draw, record, and code. These works mostly were not made to be training data.
2. **Data creation:** works are converted into data, for example by digitizing them or posting them online. The authors distinguish an expressive work from its "datafied" counterpart.
3. **Training-dataset collection and curation:** curators assemble, filter, deduplicate, and label datasets such as web crawls, LAION, and Books3. Some datasets are created specifically for training.
4. **Model (pre-)training:** a base model is trained on the dataset, often at enormous cost.
5. **Fine-tuning:** the base model is adapted with additional, often more specialized data. Some services offer fine-tuning APIs to users.
6. **Model release and system deployment:** the model's parameters may be released openly for download (open or semi-closed models such as Llama), or the model may be embedded in a hosted application or API with filters and system prompts.
7. **Generation:** users prompt the system. Prompts can contain copyrighted material, long-context inputs can hold whole books, and plugins or retrieval-augmented generation (RAG) can pull in outside content at generation time.
8. **Model alignment:** techniques such as RLHF and constitutional AI shape model behavior and can feed generations and user feedback back into training.

The chain is **not linear**. Generations become training data, synthetic data blurs the line between outputs and data, and alignment loops back into models. Many different actors may each control a different stage.

**Copyright analysis by doctrine and stage (Part II)**
- **A. Authorship.** Copyright requires originality and fixation. Everything in the chain is fixed.
  - *Datasets* are **compilations**, so any copyright covers only selection and arrangement.
  - *Models* might be compilations or derivative works. Fine-tuned and aligned models are derivatives of base models.
  - *Generations* could be owned by (1) the authors of training works, (2) a supply-chain entity such as the trainer or app developer, (3) the user, or (4) no one. There is no one-size-fits-all answer.
  - The **collage metaphor is misleading**: models don't splice works together.
  - Short prompts like "Scary lighthouse" lack enough originality, and they don't constrain the output enough to make it human authorship. This tracks *Thaler v. Perlmutter* and the Copyright Office's *Zarya of the Dawn* letter.
  - The authors leave the question open for users who gain real control over outputs. If a sponge flung at a wall can yield copyrightable spatter (*Alfred Bell*), why not a carefully crafted prompt?
- **B. Exclusive rights.**
  - *Reproduction*: **every stage involves a potentially infringing reproduction**, because datasets, models, and generations are stored in material objects. The RAM-copy doctrine (*MAI v. Peak*) and the transience threshold (*Cartoon Network*, 2.4-second buffer) matter mainly for inputs and intermediate computations.
  - *Adaptation*: a dataset is probably a compilation, not a derivative. A model is more clearly "based on" its data. A broad reading of *Micro Star v. Formgen* could make a model a derivative just because it "references" its training works.
  - *Distribution*: triggered when parties *interact*, for example by sharing datasets, releasing downloadable models, serving generations, or plugin retrieval. Internal copying by one entity is not distribution.
  - *Display and performance*: mostly relevant to generations, such as Midjourney showing intermediate denoising stages or a live-streamed audio generation.
- **C. Substantial similarity.** A qualitative, fact-intensive jury question.
  - Datasets hold complete literal copies, the paradigm case of similarity.
  - Models are not human-intelligible, but a copy only needs to be perceivable "with the aid of a machine." Memorization evidence includes Carlini et al. on Stable Diffusion's memorized photo of Ann Graham Lotz and Chang et al. on GPT-4 filling in character names. A *sufficient* condition for a model to be a copy of a work is that it **can generate that work**. That would be *direct* infringement by the model itself.
  - Fine-tuning and alignment don't remove memorized content.
  - Generations fall on a spectrum: memorized, in between, or very dissimilar. The middle case is the hard one.
  - The **"Snoopy effect"** (from Matthew Sag's "Snoopy problem"): common characters, works, and styles are easily elicited, even without naming them. Examples are an "adventurous archaeologist with a whip and a fedora" that looks like Indiana Jones, an "ice princess" that looks like Elsa, and "a golden robot which is not c3po."
  - Limits on infringement: *scènes à faire*, de minimis copying (*Gottlieb*), and **filtration** of unprotected elements.
- **D. Proving copying.** Copying in fact is shown through access plus probative similarity. Finding an exact copy in a dataset is easy in theory, but near-duplicates are hard to find. The burden is asymmetric: a plaintiff needs to point to just one work, while a defendant must disprove all of them. For generations, presence in the training set is strong evidence of access. Near-access-freeness (Vyas, Kakade & Barak) doesn't map onto copyright doctrine.
- **E. Direct infringement.** Direct infringement is **strict liability**, but it has a **volitional-conduct** element that asks "who made this copy?"
  - Dataset curators, trainers, fine-tuners, and aligners are volitional direct infringers. Deployers who only use someone else's model are not.
  - For generation, **subconscious copying** (*ABKCO v. Harrisongs*, "My Sweet Lord") is a good fit.
  - Hosted services yield three scenarios. The *user* is the direct infringer ("elsa and anna from frozen"). The *service* is the direct infringer (an innocent prompt that yields Elsa). Or *both* are (a "frozen 3 screenplay" request to a sequel-tuned model, or tricking ChatGPT into producing Calvin and Hobbes).
- **F. Indirect infringement.**
  - The three forms are vicarious (*Fonovisa*), contributory (*Napster*), and inducement (*Grokster*), with the *Sony* staple-article rule.
  - Hosted services have control, so they face Napster-style liability after **specific notice**. The authors argue a notice shouldn't be limited to one exact prompt or output, though suppressing a concept can degrade the model. Sony doesn't protect services with ongoing control.
  - Trainers that license to blatant infringers can be liable.
  - Openly released models aren't like VCRs, because they *embed* expression. If a model is an infringing copy, liability is direct and Sony doesn't apply.
  - Dataset creators and content creators are rarely indirectly liable, but they might be when data is made for an infringing model or when there are funding ties. An example is Stability AI's support for academic and nonprofit groups, which Baio calls "**data laundering**."
- **G. Section 512 (DMCA safe harbors).** These mostly **don't apply**:
  - 512(a) transmission and 512(b) caching require user direction, transience, and no modification.
  - 512(c) user-directed storage might cover only prompts or user fine-tuning data.
  - 512(d) information-location tools might cover only plugins that link to content.
  - Still, **notice-and-takedown** is an influential model.
- **H. Fair use.** The analysis runs backward through the chain.
  - *Generations*: factors one, three, and four can cut either way, and factor two is neutral. Five Bojack Horseman hypotheticals show market substitution: a pirated copy, a near copy, a new episode competing in the licensing market, a broad-style output (no factor-four issue because nothing is substantially similar), and an unknowing regurgitation.
  - *Models*: Sag's **non-expressive use** argument and *Google Books* work for non-generative AI. The argument **breaks down once outputs can infringe**. Models are highly transformative, but they may capture a work's "heart," and the licensing market is circular and now open again (Getty, NYT).
  - *Datasets*: the purpose may be transformative, but the content is not. Datasets copy whole works. A dataset that gives public access to pirated books (**Books3**) is likely unfair, and **bad faith** may matter.
  - Bottom line: **fair use is not a silver bullet.**
- **I. Express licenses.**
  - A license is a complete defense, but only if granted by someone authorized. There is no good-faith-reliance defense.
  - Specific licenses (e.g., Adobe Firefly / Adobe Stock) cover a small fraction of training data.
  - **Creative Commons** terms play out differently:
    - **BY** requires attribution, which current models can't provide.
    - **NC** allows only fully noncommercial chains.
    - **ND** effectively bars models and generations, because they are derivatives.
    - **SA** is feasible but raises compatibility problems.
  - Because **BY** appears in all six standard licenses, "CC licensing is a dead-end for generative AI" for now.
- **J. Implied licenses.**
  - Posting online implies a license for search indexing and archiving (*Field v. Google*), especially absent robots.txt. That might extend to datasets, but less clearly to training, and even less to generation.
  - Voluntary online posting can still support fair use (the *Sony* analogy).
  - Trespass and the CFAA bind only the scraper. Only copyright "runs with the data."
- **K. Remedies.**
  - *Actual damages / lost licensing fees* are hard to prove without a market (*On Davis v. Gap*, $50).
  - *Infringer's profits* use apportionment: a generation is like an anthology, and a model is like a whole catalog.
  - *Statutory damages* run $750-$30,000 per work, up to $150,000 if willful, and require registration. Across billions of works this is an existential threat ("Chicxulub asteroid"), which explains the **class actions**.
  - *Attorney's fees* create settlement pressure on small defendants, which explains vendors' **indemnification** offers.
  - *Injunctions* follow *eBay*'s four factors, plus First Amendment concerns and tailored filtering orders.
  - *Destruction* (§ 503(b)) could reach models as "articles by means of which" copies may be reproduced (Elizabeth Joh).
- **L. CMI (§ 1202).** Stripping credits through decontextualization (LAION downloads) or generating distorted Getty watermarks may count as removal or falsification of CMI. The obstacle is the intent nexus to infringement. Statutory damages are **per violation**.
- **M. Right of publicity.** This is state law that varies by state. It covers commercial uses: **endorsement**, **merchandising**, and **virtual impressment** (Eric Johnson's term).
  - Cases: *Midler*, *White v. Samsung*, *Motschenbacher*.
  - Defenses: transformative use (*Comedy III*), news and public-interest exceptions, and copyright preemption (*Laws v. Sony*, compared with *Facenda*).
  - The George Carlin "Dudesy" suit was a near-miss: the episode turned out to be human-written, and California's postmortem right excludes entertainment.
  - Fake Taylor Swift and Tom Hanks ads raise the issue in endorsement form.
  - Section 230 applicability is split (*Perfect 10 v. CCBill* vs. *Hepp v. Facebook*).
- **N. Hot news.** *INS v. AP* protects time-sensitive facts against free-riding competitors. The NYT's misappropriation claims are unlikely to succeed: "Hot news is ice cold six months later," and preemption applies.

**Part III, possible outcomes:**
1. **No liability.** Simple but unstable, because generative layers could be used to launder works.
2. **Liability for generations only.** Systems are treated as tools like Photoshop, with a Grokster-style limit for systems designed to infringe.
3. **Notice and removal.** A Napster-like regime gravitating toward § 512 norms. This is technically hard, because removing data from a model is unsolved and retraining is costly. It could split the field into closed models with guardrails and open models trained on licensed or public-domain data. Datasets are easier removal targets.
4. **Infringing models.** Every model would need a fully licensed training dataset.

**Part III, six lessons:**
1. Copyright touches every stage.
2. Concerns can't be localized to one link.
3. Design choices matter.
4. Fair use is not a silver bullet.
5. The ordinary retail work of copyright still matters.
6. Analogies can mislead.

**Key terms**
- **Supply chain:** the multi-stage, multi-actor pipeline from works to generations.
- **Datafied counterpart:** a data example derived from an expressive work.
- **Volitional conduct:** the "who made this copy?" test that sorts direct from indirect infringers.
- **Subconscious copying:** liability for copying one doesn't remember.
- **Snoopy effect:** easy elicitation of common characters and styles.
- **Filtration:** removing unprotectable elements before comparison.
- **Scènes à faire:** stock elements of a genre that can't ground infringement.
- **Non-expressive use:** bulk use that doesn't consume expression.
- **Virtual impressment:** digitally conscripting a person into a performance.
- **CMI:** copyright management information.
- **Data laundering:** using academic or nonprofit intermediaries to shield commercial firms.
- **Near-access-freeness:** a technical guarantee that a model's outputs are indistinguishable from those of a model never trained on a given work.

**Ties to lectures:** This reading is the backbone of **Lecture 18**: the supply chain, the many-hands problem, reproduction at every stage, and fair use for non-generative versus generative AI. It also underlies **Lecture 19** (authorship, memorization, substantial similarity, and characters and style, cf. *Warner Bros. v. Midjourney*), **Lecture 20** (virtual impressment and the right of publicity), and **Lecture 14** (supply chain as a data-governance frame). Its discussion of how hard it is to remove works from trained models parallels Cooper et al. on **machine unlearning** in Lecture 15. Its point that design choices allocate liability matches Fiesler's "guardrails as architecture" theme. Note the date: the draft predates *Bartz v. Anthropic* and *Thomson Reuters v. Ross*, so its fair-use discussion is predictive, not a report of those holdings.

---

## 4. Key Laws and Cases Across the Module

| Name | Jurisdiction | What it does / holds (as presented in the module) |
|---|---|---|
| GDPR (incl. Art. 22) | EU | Comprehensive data-protection law built on FIPP-style principles and lawful bases. Art. 22 gives a right not to be subject to solely automated decisions with legal or similarly significant effects. |
| EU AI Act (GPAI obligations) | EU | Requires general-purpose AI providers to adopt a copyright-compliance policy and publish a summary of training content. |
| EU text-and-data-mining (TDM) exceptions | EU | One exception for scientific research by certain institutions. A broader exception lets rights holders reserve rights (opt out), including by machine-readable means. |
| Japan's ML copyright approach | Japan | Relatively permissive for uses not aimed at "enjoying" expressive content. Less clear for imitation of specific works or creators. |
| CCPA and state privacy laws | California / U.S. states | Consumer privacy rights. Solove notes many state laws exempt "publicly available" data and that re-identification undermines de-identification carve-outs. |
| FCRA, HIPAA, GINA | U.S. federal | Sectoral protections. FCRA and HIPAA protect data even when public. GINA bars employers from acquiring genetic info, which inference can evade. |
| *Carpenter v. United States* | U.S. Supreme Court | Historical cell-site location data gives an "intimate window" into a person's life. Its acquisition generally requires a warrant. |
| *DOJ v. Reporters Committee* | U.S. Supreme Court | A compiled FBI "rap sheet" of public records still carries a privacy interest. Aggregation matters. |
| *LAPD v. United Reporting* | U.S. Supreme Court | Cited by Solove as support for conditioning access to public records. |
| *United States v. Miller*; *Smith v. Maryland* | U.S. Supreme Court | Third-party doctrine: no Fourth Amendment protection for bank records or dialed numbers given to third parties. Carpenter only partly curtails it. |
| *hiQ Labs v. LinkedIn* | U.S. 9th Cir. | Scraping of public profiles. Solove criticizes its prioritizing of competition over privacy. Lee et al. cite it for limits on anti-scraping claims. |
| *Wisconsin v. Loomis* | Wisconsin Sup. Ct. | Upheld use of the COMPAS risk score in sentencing despite trade-secret opacity, because the judge wasn't bound by it. |
| *In re Everalbum* (FTC, 2021) | U.S. (FTC) | An example of "algorithmic destruction": deletion of models built on improperly obtained data. |
| Section 230 (CDA) | U.S. federal | (c)(1) says platforms aren't treated as publisher or speaker of user content. (c)(2) protects good-faith filtering. Read broadly in *Zeran v. AOL* and *Herrick v. Grindr*. FOSTA (2018) carved out sex trafficking. |
| *NYT v. Sullivan*; *United States v. Alvarez* | U.S. Supreme Court | First Amendment limits on banning false speech. Chesney & Citron conclude a general deepfake ban is likely unconstitutional. |
| *Brandenburg v. Ohio* | U.S. Supreme Court | Imminence requirement limits incitement-based prosecutions of harmful deep fakes. |
| 18 U.S.C. § 2261A | U.S. federal | Federal cyberstalking statute, one possible criminal tool against deepfake harassment. |
| IEEPA / EO 13694 (and EO 13757) | U.S. federal | Sanctions authority for malicious cyber activity and election interference. Chesney & Citron discuss it for foreign deep-fake campaigns. |
| U.S. Copyright Act § 107 (fair use) | U.S. federal | Four factors: purpose and character, nature of the work, amount used, market effect. Fact-specific. |
| *Bartz v. Anthropic* | U.S. N.D. Cal. | Training on books was fair use ("exceedingly transformative"). Building a library of pirated books was treated differently. A $1.5B class settlement covered the piracy issue. |
| *Thomson Reuters v. Ross* | U.S. D. Del. | Fair use rejected where Westlaw headnotes were used to build a competing legal-research tool. |
| *Naruto v. Slater* | U.S. 9th Cir. | Monkey selfie: animals can't hold copyright, so the images are public domain. |
| *Thaler v. Perlmutter*; *Zarya of the Dawn*; Allen *Théâtre D'opéra Spatial* refusal | U.S. (D.D.C.; Copyright Office) | Human authorship is required. Purely AI-generated material is not registrable. Human selection, arrangement, and edits can be. |
| UK CDPA s. 9(3) | UK | For computer-generated works, the author is the person who made "the arrangements necessary for the creation of the work." |
| Beijing Internet Court AI-image case | China | Recognized copyright in an AI-generated image based on the user's prompting, parameter choices, and selection. |
| China AI-content labeling rules | China | Require labeling of AI-generated or synthetic content (output governance for audience knowledge). |
| *Warner Bros. Discovery v. Midjourney* (2025) | U.S. | Alleges Midjourney generates copyrighted characters (Batman, Bugs Bunny) even from generic prompts. Targets the company, not users. |
| *Tremblay v. OpenAI*; *Kadrey v. Meta*; *Doe v. GitHub*; *Anderson v. Stability AI* | U.S. N.D. Cal. | Putative class actions over training on books, code, and images (cited by Longpre and Lee et al.). |
| *NYT v. Microsoft & OpenAI* | U.S. | Copyright, CMI, and hot-news misappropriation claims. Lee et al. think the hot-news claims are weak. |
| *Getty Images v. Stability AI* | U.S. D. Del. | Copyright, trademark, and § 1202 CMI claims, including distorted Getty watermarks in generations. |
| DMCA § 512 / § 1202 | U.S. federal | Safe harbors with notice-and-takedown (mostly inapplicable to generative AI per Lee et al.). CMI anti-removal and anti-falsification rules with per-violation damages. |
| *Sony v. Universal*; *Napster*; *Grokster* | U.S. | Secondary-liability framework: the substantial-noninfringing-use defense, liability on specific knowledge, and inducement. |
| Right of publicity (*Midler*, *White v. Samsung*, Cal. Civ. Code § 3344) | U.S. states | Protects name, voice, and likeness against commercial appropriation. Varies by state. |
| Tennessee ELVIS Act | Tennessee | Extends publicity rights to voice and AI-generated likeness. |
| California digital-replica laws | California | Protections for performers against unauthorized digital replicas. |
| NO FAKES Act (proposed) | U.S. federal | Would create a federal digital-replica right. |
| SAG-AFTRA 2023 agreement | U.S. (labor contract) | Consent, specific description of use, compensation, and additional consent for new uses of digital replicas. |
| TAKE IT DOWN Act | U.S. federal | Criminalizes publishing NCII (real or "digital forgeries") of identifiable people without consent. Creates a notice-and-takedown system. Grimmelmann warns of abuse. |
| Colorado Candidate Elections Deepfake Disclosure Act (2024) | Colorado | Disclosure requirements for candidate deepfakes in election communications (practice law-reading example). |
| Biden 2023 AI Executive Order | U.S. federal | Called for robust watermarking or labeling of AI-generated content. |
| Denmark's proposed copyright amendments | Denmark | Would give people control over deepfakes of their voice and image. |
| *INS v. AP* (1918) | U.S. Supreme Court | Hot-news misappropriation: quasi-property in fresh news against free-riding competitors. |

---

## 5. Glossary

- **Aggregation:** combining individually trivial data points into revealing profiles (Solove; *Reporters Committee*).
- **Alignment:** post-training methods such as RLHF that shape model behavior. Stage 8 of Lee et al.'s supply chain.
- **Algorithmic destruction / disgorgement:** ordering deletion of models trained on improperly obtained data (*Everalbum*).
- **Authenticity:** whether data or content is what it claims to be (Longpre et al.).
- **C2PA / content credentials:** an industry standard attaching cryptographically verifiable provenance metadata to media.
- **CMI (copyright management information):** title, author, owner, and license info attached to a work. Protected by 17 U.S.C. § 1202.
- **Compilation:** a work formed by selecting and arranging preexisting materials. Datasets are compilations.
- **Consent:** meaningful control by the people and creators whose data is used. Strained by scale, reuse, inference, and the relational nature of data.
- **Data cascades:** compounding downstream harms caused by undervalued upstream data work (Sambasivan et al.).
- **Data minimization / purpose limitation:** FIPPs: collect only what's needed, and don't reuse it for incompatible purposes.
- **Deep fake:** realistic digital falsification of images, video, or audio (Chesney & Citron).
- **Digital replica:** a digitally created or manipulated recording that realistically but falsely depicts an individual (U.S. Copyright Office, 2024).
- **Fair use:** U.S. defense weighing four statutory factors. "Not a silver bullet" for generative AI (Lee et al.).
- **FIPPs:** Fair Information Practice Principles, the shared vocabulary of data-protection law.
- **Great Scrape:** Solove & Hartzog's term for mass AI-era scraping as a form of surveillance.
- **Human authorship requirement:** U.S. rule that copyright protects only human-made expressive choices.
- **Inference:** new information derived from other data. The "economy class" of personal data (Wachter & Mittelstadt).
- **Liar's dividend:** the ability of people caught on real recordings to dismiss them as fakes (Chesney & Citron).
- **Machine unlearning:** attempts to remove a datum's influence (*removal*) or block outputs (*suppression*). Neither guarantees the other (Cooper et al.).
- **Memorization:** a model's ability to reproduce training examples near-verbatim.
- **NCII:** non-consensual intimate imagery, including sexual deep fakes.
- **Non-expressive use:** bulk use of works that doesn't consume their expression (Sag). Basis of the "Fair Learning" argument.
- **Notice-and-takedown:** a system where a rights holder's notice obliges a platform to remove material (DMCA § 512; TAKE IT DOWN Act).
- **Prediction society:** Matsumi & Solove's term for governance by forecasts about people's future behavior.
- **Privacy self-management:** placing the burden on individuals to manage privacy through notice and consent (Solove's critique).
- **Procedural data due process:** notice, hearing, and correction rights for predictive privacy harms (Crawford & Schultz).
- **Provenance:** chain of custody for data: origin, transformations, licenses, and obligations.
- **Right of publicity:** state-law right against commercial use of one's identity (name, voice, likeness).
- **Scènes à faire:** stock elements of a genre that copyright doesn't protect.
- **Section 230:** U.S. platform immunity for third-party content.
- **Snoopy effect:** easy elicitation of famous characters and styles from models (Lee et al., after Sag).
- **Substantial similarity:** the test for whether copying amounts to infringement ("total concept and feel").
- **Surveillance vs. spying:** gathering data vs. analyzing it. AI makes spying cheap at scale (Schneier).
- **TDM exception:** text-and-data-mining exception to copyright (EU, with opt-out).
- **Third-party doctrine:** no Fourth Amendment protection for information shared with third parties (*Miller*, *Smith*).
- **3 Cs:** consent, credit, compensation (from the Cultural Intellectual Property Rights Initiative).
- **Virtual impressment:** digitally conscripting someone into a performance they never gave (Eric Johnson; Lee et al.).
- **Volitional conduct:** the "who made the copy?" test for direct infringement.
- **Watermarking:** embedding visible or imperceptible signals in AI output. Must be robust, auditable, interoperable, and enforceable to be meaningful.

---

## 6. Practice Questions (original, for self-study)

**Q1 (MC).** According to Schneier as presented in Lecture 16, what does AI change most?
A) The cost of gathering data
B) The cost of analyzing gathered data
C) The legality of data collection
D) The accuracy of consent notices

**Answer: B.** The internet made *surveillance* (gathering) cheap. AI makes *spying* (analysis, making data "searchable and understandable") cheap at scale. *Source: Lecture 16.*

**Q2 (Short answer).** Distinguish "removal" from "suppression" in machine unlearning and explain why the distinction matters for deletion rights.

**Answer:** Removal eliminates a datum's influence on the model's parameters. Suppression prevents certain outputs. Neither guarantees the other: a model can be blocked from saying something while still encoding it, and removing one example doesn't ensure outputs never resemble it. So "we unlearned it" may not satisfy what a deletion right is meant to achieve. *Source: Lecture 15 (Cooper et al.).*

**Q3 (MC).** Which best describes Wachter & Mittelstadt's claim that inferences are the "economy class" of personal data?
A) Inferences are cheaper to compute than collected data
B) Inferences receive weaker legal protection than data people provide
C) Inferences are less accurate than collected data
D) Inferences are exempt from GDPR entirely

**Answer: B.** People have rights over what they *provide* but weak rights over what is *concluded* about them. D overstates the point. *Source: Lecture 16; Solove reading.*

**Q4 (Short answer).** Give two reasons Solove argues that scraping should not be excused just because data is "publicly available."

**Answer (any two):** Scraping violates nearly every FIPP (transparency, purpose specification, consent, minimization). Aggregating public data creates new privacy harms, as recognized in *Reporters Committee* and *Carpenter*. Laws like FCRA and HIPAA already protect some public data. Letting data be scraped is functionally sharing it, so organizations should have duties to protect against scraping. *Source: Solove reading.*

**Q5 (MC).** In Lee, Cooper & Grimmelmann's analysis, which supply-chain activity does NOT generally implicate the distribution right?
A) Releasing model weights for public download
B) Sharing a dataset with an outside model trainer
C) A single company training a model on its own servers for internal use
D) Serving downloadable generations to users

**Answer: C.** Internal copying by one entity can be reproduction, but distribution requires transfer to the public. That happens when parties interact. *Source: Lee et al., Part II.B.*

**Q6 (Short answer).** Why do Lee et al. say the "non-expressive use" fair-use argument works for non-generative AI but "breaks down" for generative AI?

**Answer:** For non-generative uses (search, stylometry, plagiarism detection), outputs don't deliver copyrighted expression to humans, so the intermediate copying doesn't compete with authors. Generative models can produce outputs that reproduce or substitute for expression, and some will infringe. Once outputs can infringe, the claim that the system never implicates copyright's purposes fails, and the fair-use analysis of models and datasets is "up for grabs again." *Source: Lee et al., Part II.H.*

**Q7 (MC).** Why do Lee et al. conclude that Creative Commons licensing is currently "a dead-end for generative AI"?
A) CC licenses forbid machine reading
B) All standard CC licenses require attribution, which current models can't provide in models or generations
C) CC licenses expired in 2023
D) CC licenses don't cover reproduction

**Answer: B.** BY is common to all six standard licenses. Models don't retain attribution, so models and generations fall outside the license. *Source: Lee et al., Part II.I.*

**Q8 (Short answer).** Explain the "liar's dividend" and name one governance tool from Lecture 21 aimed at it.

**Answer:** As public awareness of deepfakes grows, people caught on authentic recordings can more plausibly claim they are fake, which erodes trust in real evidence. Provenance systems such as C2PA content credentials help, because they shift the question from "can we prove it's fake?" to "can we prove where it came from?" *Source: Chesney & Citron; Lecture 21.*

**Q9 (MC).** In the X reporting-pathway audit described in Lecture 21, which result was observed?
A) Both copyright and NCII reports were removed within a day
B) Copyright reports were removed; non-consensual nudity reports were not removed in the study window
C) Neither type was removed
D) NCII reports were removed faster than copyright reports

**Answer: B.** All 25 copyright reports were removed in about 25 hours, and none of the 25 NCII reports were removed in three weeks. This shows platforms respond to property claims over dignity claims. *Source: Lecture 21.*

**Q10 (Short answer).** Chesney & Citron consider a flat ban on deep fakes. Give their two main objections.

**Answer:** It is undesirable, because manipulation isn't inherently harmful and a ban would chill art, education, satire, and parody and invite politicized enforcement. It is likely unconstitutional, because under *NYT v. Sullivan* and *United States v. Alvarez*, falsity alone doesn't strip speech of First Amendment protection. *Source: Chesney & Citron reading.*

**Q11 (MC).** Under the U.S. approach described in Lecture 19, which element of an AI-assisted work is MOST likely to be protected?
A) An image generated from a single detailed prompt
B) The prompt-generated image after hundreds of prompt iterations
C) A human's original selection and arrangement of AI-generated images into a comic
D) The AI model as author

**Answer: C.** Human selection and arrangement and sufficiently original human edits are protectable. AI-determined expression is not, even after many prompts (cf. the Allen refusal and *Zarya of the Dawn*). *Source: Lecture 19; Lee et al., Part II.A.*

**Q12 (Short answer).** What do the 3 Cs stand for, where does the framework originate, and why does Lecture 17 say copyright is an imperfect proxy for them?

**Answer:** Consent, credit, compensation. The framework comes from the Cultural Intellectual Property Rights Initiative, which concerns Indigenous and traditional-knowledge custodians. Copyright asks about infringement and fair use, not whether creators agreed, were credited, or were paid. It narrows broader dignitary, labor, and control concerns into legal questions that favor well-resourced parties. *Source: Lecture 17.*

**Q13 (MC).** Longpre et al. call for which response to broken data provenance?
A) A brand-new proprietary standard owned by one developer
B) Unifying existing tools into a standardized, interoperable provenance framework through multi-stakeholder action
C) Banning web scraping entirely
D) Relying only on watermarking

**Answer: B.** They argue for unifying existing standards, not proposing a new one, and they call watermark-style authenticity tools necessary but insufficient. *Source: Longpre et al. reading.*

**Q14 (Short answer).** Explain why Lee et al. (2026 ICML position paper, Lecture 21) say policy for NCII must differ from policy for political deepfakes.

**Answer:** Political deepfakes mainly cause *viewer-centered* epistemic harms (deception, misinformation), which disclosure, labeling, and watermarking can address. NCII causes *subject-centered* dignity harms that persist even when viewers know the image is fake, so labels don't help. NCII policy needs consent-based rules, fast removal, and accountability. "Authentic doesn't mean safe." *Source: Lecture 21.*

**Q15 (MC).** In Lee, Cooper & Grimmelmann's discussion of remedies, why are statutory damages especially threatening to large generative-AI models?
A) They are awarded per work infringed, regardless of how much each work was used, and models train on millions or billions of works
B) They have no maximum
C) They don't require copyright registration
D) They apply only to open-source models

**Answer: A.** At $750-$30,000 per work (up to $150,000 if willful), multiplied across huge registered corpora such as books, totals become existential. That is why many suits are class actions. C is wrong: registration before infringement is required. *Source: Lee et al., Part II.K.*
