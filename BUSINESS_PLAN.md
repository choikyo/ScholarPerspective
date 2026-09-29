# Business & Logistics Brainstorm
## Scholar Perspective — Getting Recognized as a Real Journal

This file is for the non-technical side of the project: legal/business setup, ISSN registration, and getting indexed in the search systems that make a journal discoverable and citable. No code lives here — just decisions, research notes, and open questions.

---

## 1. Why This Matters

A website with PDFs is not yet "a journal" in the eyes of libraries, researchers, or citation databases. What makes it one:
- A registered **ISSN** (proves it's a recognized serial publication)
- **Discoverability** in the places scholars actually search (Google Scholar, DOAJ, library catalogs, aggregators)
- **Citability** — other papers can reference an article in a stable, permanent way (ideally a DOI)
- Documented **editorial/peer-review policies** — most indexes require these before they'll even consider listing you

These four things are interlinked: you generally need the ISSN and the editorial policies *before* you can apply to most indexing services.

---

## 2. ISSN Registration (Library of Congress / U.S. ISSN Center)

**What it is:** An ISSN (International Standard Serial Number) is an 8-digit identifier for a serial publication (journal, magazine, newsletter — anything published in ongoing issues). The U.S. ISSN Center, housed at the Library of Congress, issues them for U.S.-based publications. It's free.

**Key facts to confirm/research:**
- Apply here: https://www.loc.gov/issn/ (request form is online)
- One ISSN per **format** — since Scholar Perspective is online-only (PDF/web), you'd request an "online ISSN," not a separate print one (unless a print edition is ever planned)
- Typical requirements:
  - Title of the publication (must be exact wording as it appears in issues) — this is the journal's own title (e.g., "Scholar Perspective"), not article titles. Tied permanently to that exact string; a future title change needs a *new* ISSN.
  - Confirmation it publishes on an ongoing/serial basis (not a one-off) — satisfied just by being structured as a numbered, continuing series rather than a standalone publication.
  - At least one published issue, sometimes evidence of intent to continue — already satisfied (Issue 1 live, Issue 2 in progress).
  - Publisher name/contact info — administrative only, for LOC's own records; doesn't require a registered business entity.
  - URL where issues are accessible — just the live publications URL, so they can confirm it's real and public.
- Processing time: historically a few weeks to a few months
- **Open question:** Do we need a full issue already live, or can we apply with issue #1 published (April 2026 issue) and reference that?
- **Open question:** Does the ISSN Center require any particular metadata to appear on the site/PDF itself (e.g., the ISSN printed on the cover/each issue once assigned)? Standard practice is to print the ISSN on the front cover or masthead of each issue once granted.

**Action items:**
- [ ] Read current U.S. ISSN Center application requirements in full (they update wording periodically)
- [ ] Decide the exact, final title wording before applying (title changes require a NEW ISSN, so lock this in first)
- [ ] Apply for online ISSN once issue #1 is stable/public
- [ ] Once granted, add ISSN to site footer, PDF cover/masthead, and `articles.csv`/metadata

---

## 3. ISSN vs. DOAJ — Two Different Gatekeepers

Easy to conflate these since both come up together, but they check completely different things. Keeping the split clear avoids over- or under-building for either one.

| | **ISSN (Library of Congress)** | **DOAJ** |
|---|---|---|
| **What it actually is** | A bibliographic identifier — a catalog number for a serial publication | A curated directory that vets journals for legitimacy/quality |
| **What it checks** | Nothing about content. Just: is this a real, ongoing, identifiable serial? | Editorial rigor: peer review, ethics policy, licensing, editorial board, minimum output |
| **Article count required** | None | ~5 published articles (historically) |
| **Contributor nationality/diversity** | Not checked | Not explicitly required, but international/varied authorship strengthens credibility |
| **Issues-per-year frequency** | Declared as metadata only, not enforced | Not a hard rule, but needs to show it's an active, ongoing publication |
| **Peer review** | Not required at all | Required — must be real and publicly described |
| **Cost** | Free | Free |
| **Think of it as** | "This publication exists and has a library-catalog ID" | "This publication meets quality/legitimacy standards for open-access scholarship" |

**The practical takeaway:** ISSN is a low bar, purely administrative, and can be secured almost immediately with what already exists (Issue 1 + a locked title). DOAJ is the actual vetting gate, and it's the one that requires building real editorial infrastructure (peer review process, ethics policy, license, ~5 articles) before applying. Getting the ISSN does not move the needle on DOAJ readiness at all — they're sequential but unrelated checks.

---

## 4. Getting Indexed / Discoverable

Different systems, different requirements, roughly ordered from "easiest / automatic" to "hardest / most prestigious":

### 4a. Google Scholar (free, no application — just crawlability)
- No formal submission process. Google Scholar crawls sites automatically if:
  - PDFs have **real, selectable text** (not scanned images) — worth double-checking since the site disables copy/right-click; that's fine for *users*, but the crawler still needs to read the text layer underneath
  - Pages use proper scholarly metadata tags (Highwire Press tags or Dublin Core `<meta>` tags: title, author, publication date, PDF URL)
  - Site isn't blocked by `robots.txt` for the article pages
  - There's a clear, crawlable path to every article (sitemap.xml helps)
- **Open question:** Does `/publications/view/<filepath>` (the PDF.js canvas viewer) expose a real, crawlable link to the underlying PDF, or does everything render client-side in a way Google can't see? Worth checking — this is a website/metadata concern to flag for later, not something to fix today.

### 4b. DOAJ — Directory of Open Access Journals (free application, real vetting)
- The most respected free index for open-access scholarly journals. (See Section 3 above for how this differs from ISSN.)
- Requirements typically include:
  - ISSN
  - Published editorial board with real names/affiliations (already have 12 members — good)
  - A clearly stated peer-review process
  - A publication ethics / plagiarism policy
  - An open-access license (e.g., Creative Commons) stated per article
  - A minimum number of published articles (historically ~5) before applying
- **Open question:** Is Scholar Perspective peer-reviewed, and if so, is that process written down anywhere? DOAJ will ask for specifics (blind/double-blind, number of reviewers, etc.)

**High-level flow to get listed:**

**Phase 1 — Prerequisites (must have before applying)**
1. ISSN issued (online ISSN)
2. At least ~5 articles published with real editorial/research content
3. Editorial board listed publicly on the site with names + affiliations (have 12 — done)
4. Peer review process described publicly on the site, and actually practiced
5. Publication ethics / plagiarism policy stated publicly
6. Open license stated per article (e.g., CC BY)
7. Immediate free full-text access to every article, no paywall/embargo
8. Author guidelines page (how to submit a manuscript)

**Phase 2 — Application**
9. Create a publisher account at doaj.org
10. Complete DOAJ's online application (~50-60 questions: journal identity, editorial process, licensing, business model, archiving) — mostly points back to policies already on the site

**Phase 3 — Review**
11. DOAJ's volunteer editors review the application AND independently check the live site against the claims
12. They may follow up asking for clarification/more documentation
13. Review can take weeks to months (anti-predatory-journal screening + application backlog)

**Phase 4 — Outcome**
14. Accepted → listed in the directory, appears in DOAJ search/metadata feeds
15. Rejected → reasons given; fix gaps and reapply (sometimes after a required wait)

**Phase 5 — Ongoing**
16. Periodic re-verification of metadata/policies to stay listed

**Current gating items for Scholar Perspective:** #4 (peer review must be a real, described process) and #6 (need a stated license) — both policy decisions, not code changes.

### 4c. CrossRef (DOI registration — paid membership)
- Assigns each article a permanent DOI (e.g., `10.xxxx/...`), the standard way papers get cited and linked across the web.
- Requires organizational membership (fee scales with size — smallest tier is relatively low-cost annually) plus a small per-DOI fee.
- Needed for: citation tracking, appearing in reference managers (Zotero, EndNote), looking credible to other publishers/authors.
- **Open question:** Worth the membership cost at this stage, or wait until there's a steady publishing cadence (e.g., 3-4 issues in)?

### 4d. WorldCat / OCLC (library catalog visibility)
- Lets libraries find and catalog the journal. Usually requires a library to catalog it, or going through OCLC directly.
- Lower priority — typically follows *after* ISSN + a track record.

### 4e. EBSCOhost / ProQuest / JSTOR (subscription aggregators)
- These are the big "list your journal here" databases many academics search first.
- Generally require an established publication history, ISSN, and sometimes an application/review process — hardest tier to get into, usually not realistic in year one.
- Worth bookmarking their "publisher submission" pages for later, not urgent now.

### 4f. BASE / CORE (Bielefeld Academic Search Engine / CORE)
- Free, open-access aggregators, generally friendlier/faster to get listed in than DOAJ, and a reasonable stepping stone.

**Action items:**
- [ ] Decide/document the peer-review process (even a lightweight one) — this single decision unlocks DOAJ, credibility, and is asked about everywhere
- [ ] Decide the content license per article (e.g., CC BY-NC) and state it on each article page/PDF
- [ ] After issue #1 is public, verify Google Scholar can actually see the PDFs (search `site:scholarperspective.com` after a few weeks to check indexing)
- [ ] Once ~5 articles are published and ISSN is granted, apply to DOAJ
- [ ] Revisit CrossRef membership once there's a steady issue cadence

---

## 5. International / Regional Discoverability (China, India, Singapore, etc.)

Important distinction: **DOAJ's requirements don't change by target country.** It's one global directory with one uniform vetting process — there's no regional version of the application. What *does* vary by country is whether readers there can actually reach the standard discovery channels at all. That's an access problem, separate from anything DOAJ or ISSN require.

### 5a. India & Singapore — no special barrier
Standard channels work normally: Google Scholar, DOAJ, and direct site access are all reachable. Whatever discoverability work is already planned (crawlable PDFs, metadata tags, DOAJ listing) covers these audiences with no extra effort.

### 5b. Mainland China — the real wrinkle
- **Google (including Google Scholar) is blocked** inside mainland China by the Great Firewall. Being perfectly indexed on Google Scholar does nothing for a reader physically in mainland China on a standard connection.
- **DOAJ's own site (doaj.org) is typically reachable** from China, so a DOAJ listing itself isn't blocked — but Google-based discovery is a dead end for that audience.
- Reaching mainland Chinese researchers in practice requires a **separate set of China-specific academic databases** — not a stricter version of DOAJ, an entirely additional track:
  - **CNKI** (China National Knowledge Infrastructure) — the dominant Chinese academic database
  - **Wanfang Data**
  - **Baidu Scholar (百度学术)** — China's Google Scholar equivalent, unaffected by the firewall
  - **VIP/CQVIP**
- These typically involve their own partnership/submission processes, and content may need Chinese-language metadata or abstracts. This is a distinct future effort, not something a DOAJ listing unlocks automatically.

**Open questions:**
- Is mainland China reach a near-term goal, or a "someday" consideration? (Affects whether this is worth pursuing before or after DOAJ/CrossRef.)
- Would Chinese-language abstracts or metadata be added per article if pursuing this track?

**Action items:**
- [ ] Treat China-specific database outreach (CNKI, Wanfang, Baidu Scholar) as a separate, later initiative — not a substitute for or dependency of the DOAJ/ISSN path
- [ ] No action needed for India/Singapore beyond the discoverability work already planned for Google Scholar/DOAJ

---

## 6. Peer Review & Publication Ethics — Documenting & Preserving Evidence

Articles have in fact been reviewed by Advisory Board members, but this hasn't been stated publicly or recorded anywhere, and there's no written ethics/plagiarism policy yet. These are two related but distinct gaps — DOAJ asks for both separately.

### 6a. Public-facing: a peer review policy statement
Add a short, honest description of the actual process to the site (e.g., an "Editorial Policies" page) — something like: *"Each submission to Scholar Perspective is reviewed by one or more members of our Advisory Board prior to acceptance. Reviewers assess scholarly merit, originality, and fit with the journal's scope; articles may be returned to authors for revision before publication."*
- Describe the real model (board review), not a formal double-blind process that isn't actually practiced — DOAJ accepts multiple review models, it just needs to be real and stated.
- Include a conflict-of-interest line: board members should not review submissions they authored.

### 6b. Internal: a review log (the evidence trail)
No special software needed — a simple shared spreadsheet, logging per article:
- Title, author(s), submission date
- Reviewer(s) assigned
- Decision (accept / accept with revisions / reject) + date
- Brief reviewer comments/notes

This is the internal record that backs up the public policy statement if ever questioned.

### 6c. Retroactively covering Issue 1
Since Issue 1's reviews happened informally with no written trail, ask whichever board member(s) reviewed each article for a short written confirmation now (even a one-line email: *"Confirming I reviewed [Article Title] prior to publication and approved it."*). Imperfect, but far better than no record at all, and cheap to collect while still fresh.

### 6d. Publication Ethics / Plagiarism Policy (separate written policy DOAJ explicitly asks for)
This is its own document from the peer-review policy — DOAJ (and general good practice) expects a stated position on research integrity, not just "we review submissions." A workable policy for a journal this size typically covers:
- **Originality:** submissions must be the author's own original work, not previously published or under review elsewhere (no duplicate/redundant publication)
- **Plagiarism screening:** how it's checked — even a lightweight manual check, or a free/low-cost plagiarism checker (e.g., Quetext, Grammarly's checker), is enough to state at this stage; paid tools like iThenticate/Turnitin (often bundled cheaply through CrossRef's Similarity Check once a CrossRef member) are a later upgrade, not a starting requirement
- **Authorship criteria:** who qualifies as an author (meaningful contribution to the work), avoiding "guest" or "ghost" authorship
- **Conflicts of interest:** disclosure expectations for both authors and reviewers
- **Data/quote integrity:** no fabricated data or misrepresented sources; proper permission/citation for quoted or reproduced material
- **Handling misconduct concerns:** a simple stated process for investigating a suspected issue after publication, and how corrections or retractions would be handled
- Many journals simply state they **follow COPE (Committee on Publication Ethics) core practices** as a recognized external standard, without needing to invent every detail from scratch

**Open questions:**
- Manual/free plagiarism checking for now, or budget for a paid tool from the start?
- Who owns ethics complaints if one ever comes up — the full board collectively, or a designated editor?
- Given the humanities/liberal-arts focus (vs. empirical human-subjects research), is IRB/ethical-approval language even relevant, or should the policy stay scoped to originality/authorship/plagiarism only?

**Action items:**
- [ ] Draft and publish an Editorial Policies page (peer review + ethics/plagiarism policy + author guidelines, can be one combined page)
- [ ] Decide on a plagiarism-checking approach (manual review vs. a free tool vs. a paid tool) and state it in the policy
- [ ] State the journal's position on COPE core practices (adopt as a reference standard)
- [ ] Set up the review log (spreadsheet) and start using it for Issue 2 submissions
- [ ] Collect retroactive written review confirmations from Issue 1 reviewers
- [ ] Decide and document the conflict-of-interest rule for board-member authors

---

## 7. Legal / Business Entity Questions

- [ ] Sole proprietorship vs. LLC vs. nonprofit (501(c)(3))? Nonprofit status is common for scholarly journals and can matter for grant eligibility and perceived legitimacy, but adds paperwork/cost.
- [ ] Does "Scholar Perspective" need a registered trademark, or is the domain + branding enough for now?
- [ ] Copyright: register the journal/issues with the U.S. Copyright Office, or rely on the open-access license per article to define rights?
- [ ] Business bank account / EIN if handling any payments (submission fees, donations, etc.)?

---

## 8. Open Decisions Summary (things only the owner can decide)

1. Final, locked title wording (blocks ISSN application)
2. Peer-review process — real, lightweight, or none for now (blocks DOAJ + credibility)
3. Content license (CC BY? All rights reserved? blocks DOAJ + author expectations)
4. Plagiarism-checking approach — manual, free tool, or paid tool (blocks the ethics policy from being fully concrete)
5. Legal entity type (nonprofit vs. LLC vs. sole prop)
6. Budget/timeline appetite for paid steps (CrossRef membership, trademark, legal entity filing)
7. Whether mainland China discoverability (CNKI/Wanfang/Baidu Scholar) is a near-term or someday goal

---

## 9. Rough Sequencing

1. Lock title → apply for ISSN
2. Write down peer-review + ethics/plagiarism + licensing policies (can be simple, just needs to exist)
3. Start the review log with Issue 2, collect retroactive confirmations for Issue 1
4. Confirm PDFs/pages are crawlable for Google Scholar
5. Publish enough issues/articles to meet minimums (~5 articles)
6. Apply to DOAJ
7. Evaluate CrossRef DOI membership
8. Longer-term: WorldCat, EBSCO/ProQuest/JSTOR outreach, and (if desired) mainland China database outreach (CNKI/Wanfang/Baidu Scholar)

---

## 10. Master Action Checklist (keep updating as the process matures)

A single running list, pulled from every section above, so progress on "becoming a recognized journal" can be tracked in one place. Check items off as they're done; add new ones as new questions come up.

**Now (before Issue 2 goes out):**
- [ ] Lock final title wording, exactly as it will appear everywhere
- [ ] Decide the peer-review model (who reviews, conflict-of-interest rule for board-author submissions)
- [ ] Decide the content license (e.g., CC BY, CC BY-NC, all rights reserved)
- [ ] Decide the plagiarism-checking approach (manual / free tool / paid tool)
- [ ] Draft and publish an Editorial Policies page (peer review + ethics/plagiarism policy + author guidelines)
- [ ] Set up the review log (spreadsheet) and start using it for Issue 2 submissions
- [ ] Collect retroactive written review confirmations from Issue 1 reviewers

**Near-term (around/after Issue 2):**
- [ ] Apply for the online ISSN (referencing Issue 1 as the published-issue evidence)
- [ ] Once granted, add the ISSN to site footer, PDF cover/masthead, and `articles.csv` metadata
- [ ] State the chosen license on every article page/PDF going forward
- [ ] Verify Google Scholar is actually indexing Issue 1 (`site:scholarperspective.com` search after a few weeks)
- [ ] Check whether the PDF.js viewer route exposes a crawlable PDF link for search engines (flag for the website side of things)

**Mid-term (once ~5 articles are published):**
- [ ] Apply to DOAJ
- [ ] Apply to BASE / CORE as an easier open-access aggregator stepping stone

**Longer-term (as the journal matures):**
- [ ] Evaluate CrossRef DOI membership once there's a steady issue cadence
- [ ] Decide legal entity type (nonprofit vs. LLC vs. sole proprietorship)
- [ ] Decide on trademark registration for "Scholar Perspective"
- [ ] Decide on copyright registration approach (Copyright Office vs. relying on the stated license)
- [ ] Pursue WorldCat/OCLC cataloging
- [ ] Reach out to EBSCOhost / ProQuest / JSTOR once there's an established track record
- [ ] If mainland China reach becomes a goal: pursue CNKI / Wanfang Data / Baidu Scholar partnerships (separate track from DOAJ/ISSN)

---

## 11. Suggested Action Order — Work Through One at a Time

Same items as Section 10, but flattened into a single suggested sequence rather than grouped by timeframe — pick them off in order.

- [ ] 1. Lock the final title wording, exactly as it will appear everywhere
- [ ] 2. Decide the content license (e.g., CC BY, CC BY-NC, all rights reserved)
- [ ] 3. Decide the peer-review model (who reviews, conflict-of-interest rule for board-author submissions)
- [ ] 4. Decide the plagiarism-checking approach (manual / free tool / paid tool)
- [ ] 5. Draft and publish an Editorial Policies page (peer review + ethics/plagiarism policy + author guidelines)
- [ ] 6. Set up the review log (spreadsheet) and start using it for Issue 2 submissions
- [ ] 7. Collect retroactive written review confirmations from Issue 1 reviewers
- [ ] 8. Apply for the online ISSN (referencing Issue 1 as the published-issue evidence)
- [ ] 9. Once granted, add the ISSN to site footer, PDF cover/masthead, and `articles.csv` metadata
- [ ] 10. State the chosen license on every article page/PDF going forward
- [ ] 11. Verify Google Scholar is actually indexing Issue 1 (`site:scholarperspective.com` search after a few weeks)
- [ ] 12. Check whether the PDF.js viewer route exposes a crawlable PDF link for search engines
- [ ] 13. Keep publishing until ~5 articles total are live
- [ ] 14. Apply to DOAJ
- [ ] 15. Apply to BASE / CORE
- [ ] 16. Evaluate CrossRef DOI membership
- [ ] 17. Decide legal entity type (nonprofit vs. LLC vs. sole proprietorship)
- [ ] 18. Decide on trademark registration for "Scholar Perspective"
- [ ] 19. Decide on copyright registration approach
- [ ] 20. Pursue WorldCat/OCLC cataloging
- [ ] 21. Reach out to EBSCOhost / ProQuest / JSTOR
- [ ] 22. If mainland China reach becomes a goal: pursue CNKI / Wanfang Data / Baidu Scholar partnerships
