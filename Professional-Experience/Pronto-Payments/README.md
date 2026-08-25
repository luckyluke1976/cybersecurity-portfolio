# Pronto Payments, Inc. — Retrospective GRC Case Study

> **Real professional experience · Miami, Florida · 2008–2013**
> Payments operations, third-party dependencies, merchant due diligence and security controls — revisited through a modern Governance, Risk & Compliance lens.

[← Back to Cybersecurity Portfolio](../../README.md) · [📕 Case Study PDF](Pronto_Payments_Retrospective_GRC_Case_Study.pdf)

---

## About this case study

**Pronto Payments, Inc.** was an online payment platform that I co-founded in Miami in 2008.

The service allowed residents and property owners to pay rent, condominium fees, HOA fees and other property-related charges online using **credit cards, debit cards and electronic checks**.

I was a **Co-founder & Director**, with day-to-day operational involvement across the external payment-provider ecosystem, merchant onboarding, transaction-security configuration and integrations with property-management systems.

This case study looks back at that work using the GRC methods I use today.

> **Scope note**
>
> DORA, NIS2 and ISO/IEC 27001:2022 did **not** apply to Pronto Payments during its operating period.
>
> References to current frameworks in this document are retrospective. They show how I would analyse the same risks, controls and dependencies today; they are not claims of historical compliance.

---

## Business model

Pronto Payments provided an online payment channel for property managers, condominium associations, homeowners associations and their residents.

Residents could use the platform to pay:

* rent;
* condominium and HOA fees;
* assessments;
* security deposits;
* application and screening fees;
* parking and other property-related charges.

Supported payment methods included:

* credit cards;
* debit cards;
* ACH / electronic checks.

The platform depended on external financial and technology providers rather than owning the full payment infrastructure internally.

---

## Payment ecosystem

```mermaid
flowchart LR
    A[Resident] --> B[Pronto Payments]
    B --> C[Plug'n Pay<br/>Payment Gateway]
    C --> D[Card / ACH / e-check<br/>Processors]
    D --> E[BAC Florida Bank<br/>Acquirer / Settlement]
    E --> F[Card & ACH Networks]
```

The operating model included several external dependencies:

| Provider / component            | Role                                         |
| ------------------------------- | -------------------------------------------- |
| **BAC Florida Bank**            | Acquiring bank / settlement                  |
| **Plug'n Pay**                  | Payment gateway                              |
| **Credomatic of Florida**       | Card processing                              |
| **Smart Payment Solutions**     | ACH processing                               |
| **Solveras / ECHO**             | Electronic check services                    |
| **Skyline**                     | Property-management-system integration       |
| **DNSEE**                       | Outsourced IT support / account provisioning |
| **Merchant reporting platform** | Reconciliation and reporting                 |

This provider chain is one of the main reasons the Pronto Payments experience remains directly relevant to my current work in **ICT third-party risk**.

---

## My role

My responsibilities were operational rather than a formally defined GRC role.

Looking back, however, several activities correspond closely to areas that are now part of Governance, Risk & Compliance practice.

| What I did at Pronto Payments                                                                    | How I analyse it today                              |
| ------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| Managed relationships across the acquiring bank, gateway, processors and outsourced IT providers | ICT third-party risk and dependency management      |
| Performed merchant onboarding and due diligence                                                  | Pre-contractual due diligence and risk assessment   |
| Standardised transaction-security settings                                                       | Control design and implementation                   |
| Worked with payment and property-management data flows                                           | Data-flow and interface risk                        |
| Operated under security obligations imposed through the acquiring relationship                   | Contractual and payment-industry compliance         |
| Managed operational dependencies across several external providers                               | Resilience, concentration risk and substitutability |

The point of this comparison is not to rename historical activities after the fact. It is to show how operational experience translates into the structured risk methodology I use today.

---

## Merchant due diligence

Before a merchant could be activated, onboarding involved collecting and reviewing documentation covering several risk areas.

### Corporate and ownership information

Examples included:

* Articles of Incorporation;
* Federal Tax ID;
* state of incorporation;
* ownership and officer information;
* operating bank-account information.

### Financial and adverse-history review

The onboarding process also considered information such as:

* previous bankruptcies;
* outstanding judgments;
* tax liens;
* recent bank statements.

### Security review

For web-based merchants, the process required information about their:

* online security procedures;
* fraud-detection procedures;
* operational website and business information.

A physical **Merchant Site Survey** was also part of the documented onboarding process.

### Modern GRC interpretation

Today I would treat this as an evidence-based pre-contractual assessment process:

**information request → review → risk assessment → acceptance / remediation decision → onboarding**

That same logic appears in modern third-party risk programmes even though the regulatory and technical requirements are now considerably more formalised.

---

## Transaction security controls

Merchant accounts were configured using repeatable transaction-security settings.

Documented controls included:

| Control                      | Historical configuration    | Current GRC interpretation         |
| ---------------------------- | --------------------------- | ---------------------------------- |
| Address Verification Service | AVS fraud screening         | Preventive fraud control           |
| Card security code           | CVV2 / CVC2 required        | Transaction authentication control |
| Administrative access        | IP-based access restriction | Access-control restriction         |
| Transaction limits           | Daily limit by property     | Fraud / financial exposure control |
| Settlement processing        | Automated batching          | Operational processing control     |

The important lesson for my current GRC work is the distinction between having a security requirement and turning that requirement into a **repeatable control configuration**.

---

## Data flows and integrations

Pronto Payments exchanged information with external property-management systems.

A documented field mapping covered information including:

* property identifiers and addresses;
* unit information;
* tenant identifiers and names;
* email addresses;
* charge descriptions and amounts;
* payment-related banking information.

The platform supported integrations and data exchanges using formats including CSV, Excel, QuickBooks and Skyline.

### Modern GRC interpretation

Today I would approach this through:

* information and asset identification;
* data-flow mapping;
* interface and dependency analysis;
* data classification;
* access requirements;
* retention requirements;
* third-party processing risk.

Understanding **where information originates, where it moves and which provider processes it** is essential before meaningful controls can be selected or tested.

---

# Key retrospective finding — concentration risk

The most interesting risk I see in the historical architecture today is not primarily technical.

The payment gateway was relatively substitutable: **Plug'n Pay was bank-agnostic and could connect to different processors**.

The acquiring relationship was different.

Pronto Payments relied on **BAC Florida Bank** for acquiring and settlement, and there was no equivalent alternative acquiring relationship documented. In addition, BAC Florida Bank and card processor Credomatic were part of the same corporate group.

That created a concentration point in the provider ecosystem.

```text
Technical layer
Gateway → relatively substitutable

Contractual / financial layer
Acquirer → significantly harder to replace
                  +
Acquirer and processor → same corporate group
```

### How I would analyse this today

The questions I would ask now are:

* Is the provider supporting a critical or important function?
* How substitutable is the service?
* How long would migration realistically take?
* Are multiple services concentrated within the same provider or corporate group?
* What contractual dependencies could prevent an exit?
* Is there an executable exit strategy?
* Has continuity been tested under provider-loss scenarios?

For an EU financial entity today, these issues are central to **DORA (Digital Operational Resilience Act) Chapter V**, particularly the management of ICT third-party risk and concentration risk under Articles 28–30.

Relevant ISO/IEC 27001:2022 areas include supplier-relationship controls such as **A.5.19–A.5.22**, together with continuity and resilience considerations.

---

## Retrospective control findings

Reviewing surviving historical records also identifies weaknesses that I would treat differently today.

| Finding                                                                           | Why it matters today                                                       |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Shared portal credentials were stored in clear text                               | Authentication information should be protected throughout its lifecycle    |
| Credentials were transmitted to an external IT provider by email                  | Sensitive authentication information requires secure transfer and handling |
| Third-party personal information was retained without a documented retention rule | Retention should have a defined purpose, period and disposal process       |
| The acquiring relationship had no documented exit strategy                        | Critical provider dependency requires contingency and exit planning        |
| Acquirer and processor were concentrated within the same corporate group          | Concentration needs to be assessed beyond individual supplier risk         |

These are not presented as historical compliance failures against frameworks that did not apply.

They are **retrospective findings**: examples of issues that I would expect a GRC review to identify, document, assess and track today.

---

## Modern control mapping

The mapping below is intentionally high-level. It shows areas of current relevance rather than claiming one-to-one equivalence.

| Historical area                        | ISO/IEC 27001:2022    | DORA                                     |
| -------------------------------------- | --------------------- | ---------------------------------------- |
| External provider management           | A.5.19–A.5.22         | Chapter V / Art. 28                      |
| Provider concentration                 | Supplier-risk context | Art. 29                                  |
| Contractual controls                   | A.5.20                | Art. 30                                  |
| Authentication information             | A.5.17                | ICT protection framework                 |
| Secure information transfer            | A.5.14                | ICT protection framework                 |
| Operational continuity / provider loss | A.5.29, A.5.30        | ICT continuity / third-party risk        |
| Data and dependency identification     | A.5.9                 | ICT-supported functions and dependencies |

> A mapping means that a control or historical activity **may support** a current requirement. It does not establish regulatory compliance or equivalence.

---

## What I would do differently today

If I were assessing the same environment now, I would formalise several activities that were handled operationally at the time.

### 1. Build a structured third-party register

For each provider:

* service delivered;
* data processed;
* criticality;
* business functions supported;
* subcontractors;
* contractual requirements;
* concentration dependencies;
* exit options.

### 2. Formalise provider risk assessments

Before onboarding and periodically thereafter:

```text
Criticality
    ↓
Due diligence
    ↓
Security assessment
    ↓
Contract review
    ↓
Risk decision
    ↓
Ongoing monitoring
```

### 3. Document an acquiring-provider exit strategy

This would include:

* alternative-provider analysis;
* migration dependencies;
* contractual termination requirements;
* data portability;
* technical changes;
* estimated transition time;
* testing.

### 4. Introduce formal credential-management requirements

Shared credentials would be eliminated where possible, privileged access individually attributable, and authentication information stored and transferred using approved secure methods.

### 5. Define information-retention rules

Personal and financial information collected during merchant onboarding would have explicit:

* purpose;
* owner;
* retention period;
* access restrictions;
* disposal requirements.

---

## From operational experience to GRC methodology

My formal cybersecurity GRC specialisation came later.

The underlying risk problems did not.

At Pronto Payments I was already dealing operationally with:

**external providers → sensitive data → transaction controls → fraud → dependencies → continuity**

My current work with ISO/IEC 27001, DORA, NIS2, risk assessment and control testing gives me a structured method for analysing those same problems.

That connection is the reason I include Pronto Payments in this portfolio.

It is not presented as a historical GRC implementation.

It is the **real operational experience behind my current GRC work**.

---

## Historical material

The following marketing material comes from the operating period of Pronto Payments and is included to provide business context.

It demonstrates the customer-facing service: online payment of rent and property-maintenance charges using cards or electronic checks.

<p align="center">
  <img src="assets/pronto_mail_flyer_FRONT.jpg" width="48%" alt="Pronto Payments original marketing flyer front">
  <img src="assets/pronto_mail_flyer_BACK.jpg" width="48%" alt="Pronto Payments original marketing flyer back">
</p>

**Original Pronto Payments marketing material — operating period.**

[Front image](assets/pronto_mail_flyer_FRONT.jpg) · [Back image](assets/pronto_mail_flyer_BACK.jpg)

---

## Evidence basis & limitations

This case study was reconstructed from surviving material including:

* corporate registration information;
* company agreements and operating documents;
* merchant onboarding material;
* payment-provider documentation;
* internal procedures and configuration notes;
* data-integration documentation;
* original marketing material.

I distinguish documented facts from retrospective interpretation.

Some original source documents contain third-party personal or confidential information and are **not published in this repository**.

No transaction volumes, merchant counts, regulatory licence status or other facts for which sufficient evidence has not been located are asserted here.

---

## Related portfolio work

The modern GRC areas discussed here are developed in more detail in the fictional **VindobonaPay GmbH** case study:

* [Risk Assessment & Risk Register](../../GRC/01-risk-assessment-risk-register/README.md)
* [Statement of Applicability](../../GRC/02-statement-of-applicability/README.md)
* [Control Mapping Matrix](../../GRC/03-control-mapping/README.md)
* [DORA Compliance Mapping](../../GRC/05-dora-compliance-mapping/README.md)
* [Control Testing & Evidence Automation](../../GRC/06-control-testing-evidence/README.md)

---

## Supporting document

📕 **[Download / view the Pronto Payments Retrospective GRC Case Study PDF](Pronto_Payments_Retrospective_GRC_Case_Study.pdf)**

The PDF provides a shorter visual version of this case study, including the payment-provider architecture, key retrospective findings and historical marketing material.

---

<sub>Pronto Payments, Inc. is inactive. This portfolio section is a retrospective professional case study based on historical records and personal professional experience. Current regulatory references are provided solely as a modern analytical comparison.</sub>
