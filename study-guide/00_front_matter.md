# CCNA Automation 200-901 v1.1 — Complete Study Guide

This is the primary textbook-style study document for **Automating Networks Using Cisco Platforms (200-901 CCNAAUTO) v1.1**. Passing that exam earns the **CCNA Automation** certification.

It is organized by the official Cisco exam blueprint in `200-901-CCNAAUTO_v.1.1.pdf`. Objective numbers, domain names, weights, and command verbs are copied from that document. Do not study a homemade curriculum in place of those objectives.

The Learning Matrix (`Automation-v2.0-Learning-Matrix.xlsx`) was used only as a **secondary** map of books, Cisco U. training, Cisco Live sessions, and online references. Where the matrix still uses older verbs (*Identify*) or older product names (*DNA Center*, *Umbrella*, *Webex Teams*), this guide follows the **PDF**.

This material does **not** guarantee that you will pass. Cisco can include related topics beyond the printed bullets. The goal is exam-aligned understanding plus enough hands-on practice that the blueprint verbs (especially *construct*, *interpret*, *troubleshoot*, and *utilize*) are realistic.

---

## How to use this guide

1. Build the lab in `CCNAAUTO_LAB_SETUP.md`.
2. Follow `CCNAAUTO_STUDY_PLAN.md` (about eight weeks, adjustable).
3. Study each objective in this file. Every objective has five parts:
   - **What Cisco expects me to know** — depth implied by the verb
   - **Detailed explanation** — how the technology works
   - **Syntax and examples** — code, APIs, configs, commands
   - **Exam-style understanding** — original practice ideas, not real exam items
   - **Hands-on exercise** — free labs first
4. Track status in `CCNAAUTO_Study_Tracker.xlsx` (a copy of the matrix; the original file was not modified).
5. Drill `CCNAAUTO_PRACTICE_QUESTIONS.md` with the answer section folded away.
6. In the final days, use `CCNAAUTO_FINAL_REVIEW.md`.

The same chapters also live as smaller files under `study-guide/` if you prefer to open one domain pair at a time.

---

## Exam snapshot

| Item | Official fact |
| --- | --- |
| Exam | 200-901 CCNAAUTO v1.1 |
| Title | Automating Networks Using Cisco Platforms |
| Certification | CCNA Automation |
| Duration | 120 minutes |
| Typical item types | Multiple choice, drag-and-drop, performance-based |
| Languages | English, Japanese |
| Associated course | Developing Applications and Automating Workflows using Cisco Core Platforms (now titled Automating Networks Using Cisco Platforms) |

This exam is the rebranded **DevNet Associate (200-901 DEVASC)** content with updated product names. Treat older DEVASC books as useful, then overlay v1.1 names: Catalyst Center, Catalyst SD-WAN, Secure Connect, Terraform (not Puppet/Chef), CML (not VIRL).

Official topics: [https://learningnetwork.cisco.com/s/ccnaauto-exam-topics](https://learningnetwork.cisco.com/s/ccnaauto-exam-topics)

---

## Domain weights

| Domain | Weight | Why it matters |
| --- | --- | --- |
| 1.0 Software Development and Design | 15% | Data formats, Python structure, TDD, Git |
| 2.0 Understanding and Using APIs | **20%** | Heaviest skill domain with Domain 5 |
| 3.0 Cisco Platforms and Development | 15% | What each Cisco API is *for*, plus construct-from-docs |
| 4.0 Application Deployment and Security | 15% | Docker, CI/CD, secrets, OWASP, Bash, DevOps |
| 5.0 Infrastructure and Automation | **20%** | YANG/NETCONF/RESTCONF, Ansible, Terraform, IaC |
| 6.0 Network Fundamentals | 15% | Enough networking to automate and troubleshoot apps |

Prioritize Domains **2** and **5**, but do not skip 6. Connectivity diagnosis and port numbers are easy points if you know them and easy misses if you assume “this is not CCNA.”

---

## Command verbs (study depth)

| Verb | What you must be able to do |
| --- | --- |
| **Describe** | Explain purpose, attributes, and typical use |
| **Compare** | Differences, trade-offs, and when to use each option |
| **Explain** | Cause/effect and why a design exists |
| **Interpret** | Read code, output, a playbook, a diff, a YANG model, or a diagram |
| **Identify** | Name the workflow or resource from a given artifact |
| **Construct** | Build a request or script from documentation and requirements |
| **Utilize** | Perform the operation (Git, Docker, Bash, auth, `requests`) |
| **Troubleshoot / Diagnose** | Given symptoms, find the fault and a fix |
| **Apply** | Use the concept in a Cisco setting (especially YANG/NETCONF/RESTCONF) |
| **Recognize** | Recall facts such as port numbers |

---

## Product names used in v1.1

| Blueprint name | You may still see | Exam-relevant idea |
| --- | --- | --- |
| Cisco Catalyst Center | DNA Center, DNAC | Intent APIs under `/dna/` |
| Cisco Catalyst SD-WAN | vManage, Viptela | Overlay WAN manager API |
| Cisco NSO | Tail-f NSO | Service orchestration |
| Webex | Webex Teams | Rooms, messages, memberships |
| Secure Connect | Umbrella / Secure Access | Cloud security / SASE APIs |
| Secure Endpoint | AMP for Endpoints | Endpoint event APIs |
| Secure Malware Analytics | Threat Grid | File/URL detonation API |
| Cisco Modeling Labs | VIRL | Network simulation |
| Terraform | Puppet/Chef (removed) | Declarative IaC |

---

## Lab map

Full install steps: `CCNAAUTO_LAB_SETUP.md`.

| Folder | Primary objectives |
| --- | --- |
| `labs/01_python_basics` | 1.5, 1.3, 4.5 |
| `labs/02_data_formats` | 1.1, 1.2 |
| `labs/03_rest_api` | 2.1, 2.4–2.9 |
| `labs/04_git` | 1.7, 1.8, 5.12 |
| `labs/05_cisco_apis` | 3.1–3.5, 3.9 |
| `labs/06_yang_netconf_restconf` | 3.6, 3.8, 5.1, 5.10, 5.11 |
| `labs/07_docker` | 4.6, 4.7 |
| `labs/08_ansible` | 5.6, 5.8 |
| `labs/09_terraform` | 5.5, 5.6 |
| `labs/10_network_troubleshooting` | 6.8, 6.9, 4.9 |

---

## Free primary resources

| Resource | URL | Why |
| --- | --- | --- |
| Official exam topics | https://learningnetwork.cisco.com/s/ccnaauto-exam-topics | Blueprint on Cisco Learning Network |
| Cisco DevNet | https://developer.cisco.com/ | API docs, SDKs, Learning Labs |
| DevNet Sandbox | https://devnetsandbox.cisco.com/ | Free IOS XE, NSO, and other labs |
| Code Exchange | https://developer.cisco.com/codeexchange/ | Sample automation projects |
| Meraki Dashboard API | https://developer.cisco.com/meraki/api-v1/getting-started/ | Org/network/device/client calls |
| Catalyst Center API | https://developer.cisco.com/docs/catalyst-center/getting-started/ | Token + inventory |
| ACI programmability | https://developer.cisco.com/docs/aci/ | APIC object model |
| NSO docs | https://developer.cisco.com/docs/nso/ | Service orchestration |
| Webex APIs | https://developer.webex.com/docs/getting-started | Spaces, people, messages |
| IOS XE RESTCONF | https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/1717/b_1717_programmability_cg/restconf-protocol.html | Official RESTCONF behavior |
| IOS XE NETCONF | https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/26x/26x-programmability-cg/netconf_protocol.html | Port 830, datastores |
| NETCONF RFC 6241 | https://datatracker.ietf.org/doc/html/rfc6241 | Protocol standard |
| RESTCONF RFC 8040 | https://datatracker.ietf.org/doc/html/rfc8040 | HTTP mapping of YANG |
| YANG RFC 7950 | https://datatracker.ietf.org/doc/html/rfc7950 | Modeling language |
| Python `json` | https://docs.python.org/3/library/json.html | Parsing JSON |
| Python `unittest` | https://docs.python.org/3/library/unittest.html | Unit tests (4.5) |
| `requests` | https://requests.readthedocs.io/ | Exam Python HTTP library |
| Git documentation | https://git-scm.com/docs | Clone through diff |
| MDN HTTP status | https://developer.mozilla.org/en-US/docs/Web/HTTP/Status | Response codes |
| Dockerfile reference | https://docs.docker.com/reference/dockerfile/ | Interpret images |
| Ansible docs | https://docs.ansible.com/ | Playbook modules |
| Terraform docs | https://developer.hashicorp.com/terraform/docs | Plan/apply/state |
| OWASP Top 10 | https://owasp.org/www-project-top-ten/ | XSS, SQLi, CSRF |
| pyATS | https://developer.cisco.com/pyats/ | Network testing (5.3) |
| CML | https://developer.cisco.com/modeling-labs/ | Simulation (5.3) |
| CiscoDevNet netprog_basics | https://github.com/CiscoDevNet/netprog_basics | RESTCONF/NETCONF samples |

Paid-but-official (optional, not required to start): *Cisco Certified DevNet Associate DEVASC 200-901 Official Cert Guide* and the Cisco U. CCNAAUTO / CCNAAUTO course. The Learning Matrix lists these against almost every objective.

---

## Source-material gaps and how this guide filled them

The local PDF lists **what** is tested but not **how** the technologies work. The Learning Matrix points mostly at the Official Cert Guide and Cisco U., which are not in this folder. For those gaps, this guide teaches from Cisco DevNet, Cisco IOS XE programmability guides, IETF RFCs, and vendor docs for Python, Git, Docker, Ansible, and Terraform.

Notable matrix vs blueprint mismatches you should ignore in the spreadsheet:

- 1.6 matrix *Identify* vs blueprint **Explain**
- 2.3 / 2.6 / 3.7 / 4.x several *Identify* vs blueprint **Describe** / **Interpret**
- 3.2 matrix *DNA Center* / *Cisco SD-WAN* vs **Catalyst Center** / **Catalyst SD-WAN**
- 3.5 matrix *Umbrella* vs **Secure Connect**
- 5.6 Puppet/Chef in older DEVASC notes vs **Ansible, Terraform, and Cisco NSO**

---

## Table of contents

- [1.0 Software Development and Design — 15%](#10-software-development-and-design--15)
- [2.0 Understanding and Using APIs — 20%](#20-understanding-and-using-apis--20)
- [3.0 Cisco Platforms and Development — 15%](#30-cisco-platforms-and-development--15)
- [4.0 Application Deployment and Security — 15%](#40-application-deployment-and-security--15)
- [5.0 Infrastructure and Automation — 20%](#50-infrastructure-and-automation--20)
- [6.0 Network Fundamentals — 15%](#60-network-fundamentals--15)

A one-page objective-to-section map is in `CCNAAUTO_OBJECTIVE_CHECKLIST.md`.

---

