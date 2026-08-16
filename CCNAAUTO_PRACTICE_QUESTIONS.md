# CCNA Automation 200-901 v1.1 — Practice Questions

Original items aligned to the official blueprint. These are **not** Cisco exam questions and are not reconstructed from dumps.

How to use: answer Domain by Domain on paper or in a hidden-answer editor. Check yourself in [Answer key](#answer-key). Then read the explanation even when you were right.

Legend: **MC** = single answer, **2** = choose two, **INT** = interpretation.

---

## Domain 1 — Software Development and Design (15%)

**Q1 (MC).** A colleague pastes this snippet. Which format is it, and why would Ansible prefer it over JSON?

```yaml
interfaces:
  - name: GigabitEthernet1
    enabled: true   # management
```

- A. XML, because it supports attributes
- B. JSON, because booleans are lowercase
- C. YAML, because it allows comments and indentation-based structure
- D. YANG, because `enabled` is a leaf

**Q2 (MC).** Which statement about JSON is true?

- A. Keys may be unquoted if they contain no spaces
- B. Comments start with `#`
- C. `true`, `false`, and `null` are valid literals
- D. A trailing comma after the last object property is required

**Q3 (INT).** After `data = json.loads('{"vlans":[10,20]}')`, what is `type(data["vlans"])` in Python?

- A. `tuple`
- B. `list`
- C. `str`
- D. `set`

**Q4 (MC).** You parse XML with `xml.etree.ElementTree` and `find("interface")` returns `None` even though the file contains `<interface>` tags. The root has `xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"`. What is the most likely cause?

- A. ElementTree cannot parse YANG XML
- B. The default namespace is not included in the search
- C. You must use `yaml.safe_load` on XML
- D. The file is actually JSON

**Q5 (MC).** In test-driven development, what happens first?

- A. Refactor production code for style
- B. Write a test that fails because the feature does not exist yet
- C. Deploy to production, then write tests from bugs
- D. Generate tests automatically from YANG

**Q6 (MC).** A 18-month router OS rewrite is fully specified up front, coded, then tested. Which method is this?

- A. Agile
- B. Lean
- C. Waterfall
- D. Observer

**Q7 (2).** Which two are advantages of putting code in functions and modules? (Choose two.)

- A. The interpreter skips syntax errors
- B. Units can be tested in isolation
- C. The same logic can be reused without copy-paste
- D. JSON parsers run faster

**Q8 (MC).** A monitoring dashboard updates automatically when a device object changes state, without the device code knowing about the dashboard. Which pattern is this closest to?

- A. Waterfall
- B. MVC View only
- C. Observer
- D. Bare metal

**Q9 (MC).** In MVC applied to a REST automation app, the HTTP handler that validates input and calls the Meraki client is best described as the:

- A. Model
- B. View
- C. Controller
- D. Observer subject

**Q10 (MC).** Which is an advantage of version control?

- A. It encrypts REST payloads by default
- B. It provides history, branching, and the ability to revert
- C. It replaces unit tests
- D. It converts XML to JSON

**Q11 (MC).** `git clone https://github.com/org/lab.git` primarily:

- A. Creates a branch named clone
- B. Copies the repository and its history to a new local directory
- C. Stages all remote files
- D. Opens a pull request

**Q12 (MC).** You modified `playbook.yml` but `git commit -m "update"` creates a commit with no file changes. What did you forget?

- A. `git push`
- B. `git add playbook.yml`
- C. `git branch`
- D. `git diff --staged` after the commit

**Q13 (MC).** `git pull` on a tracking branch typically:

- A. Deletes local commits
- B. Fetches remote commits and integrates them into the current branch
- C. Sends commits without fetching
- D. Creates a bare repository

**Q14 (INT).** A merge conflict shows:

```text
<<<<<<< HEAD
hostname: edge-01
=======
hostname: edge-02
>>>>>>> feature
```

What must you do before the merge is complete?

- A. Run `git clone` again
- B. Edit to one correct result, `git add`, then commit the merge
- C. Delete the repository
- D. Only run `git push --force`

**Q15 (INT).** In this unified diff, what happened to line `url = "https://router/restconf/..."`?

```text
--- a/hostname.py
+++ b/hostname.py
@@ -1,6 +1,7 @@
 import requests
-url = "https://router/restconf/data/Cisco-IOS-XE-native:native/hostname"
+HOST = "https://router"
+url = f"{HOST}/restconf/data/Cisco-IOS-XE-native:native/hostname"
```

- A. The URL line was added only
- B. The URL line was removed and replaced by a HOST variable plus a new URL line
- C. The file was deleted
- D. YAML indentation changed

---

## Domain 2 — Understanding and Using APIs (20%)

**Q16 (MC).** Docs say: `GET /organizations/{orgId}/devices` Header `X-Cisco-Meraki-API-Key` required. Which request is correctly constructed?

- A. POST with a JSON body and no headers
- B. GET to that path with the API key header and no body
- C. PUT replacing the organization
- D. GET with Basic auth only and a `/netconf` path

**Q17 (MC).** A ChatOps bot needs near-real-time room messages without asking Webex every 2 seconds. Which pattern fits?

- A. SNMP polling
- B. Webhook subscription
- C. Git clone
- D. DHCP snooping

**Q18 (2).** Which two are common constraints when consuming APIs? (Choose two.)

- A. Rate limiting
- B. OSPF hello timers
- C. Pagination of large collections
- D. Spanning Tree root priority

**Q19 (MC).** HTTP 401 vs 403:

- A. 401 means the server does not exist; 403 means JSON is invalid
- B. 401 means authentication failed or is missing; 403 means the identity is known but not allowed
- C. They are interchangeable
- D. 403 only applies to SOAP

**Q20 (MC).** You send `Content-Type: text/plain` with a JSON body to an API that requires `application/json`. Which status is most typical?

- A. 201
- B. 204
- C. 415
- D. 301

**Q21 (MC).** Response includes `429` and `Retry-After: 30`. What should a client do?

- A. Immediately retry in a tight loop
- B. Wait at least 30 seconds, then retry; consider backoff
- C. Switch the method from GET to DELETE
- D. Disable TLS

**Q22 (INT).** Given:

```text
HTTP/1.1 201 Created
Location: /networks/N_123
Content-Type: application/json

{"id":"N_123","name":"Branch"}
```

Which statement is true?

- A. The call failed authentication
- B. A resource was created; the body and Location identify it
- C. This is a NETCONF hello
- D. The client must use port 830

**Q23 (MC).** Meraki Dashboard API key is sent as:

- A. `Authorization: Basic <key>`
- B. A cookie named `JSESSIONID` only
- C. Header `X-Cisco-Meraki-API-Key`
- D. YANG namespace

**Q24 (MC).** Catalyst Center token workflow is:

- A. SSH to port 22, then SNMP
- B. POST `/dna/system/api/v1/auth/token` then send `X-Auth-Token` on later calls
- C. Only API keys in query strings
- D. NETCONF hello on 443

**Q25 (MC).** Which pair is most accurate?

- A. REST uses resource URLs and HTTP verbs; RPC emphasizes calling a named procedure
- B. REST always uses XML; RPC always uses YAML
- C. Asynchronous APIs never return HTTP 202
- D. Webhooks are a form of SNMP trap over UDP 161

**Q26 (INT).** What does this script do?

```python
import requests
r = requests.get(
    "https://httpbin.org/get",
    params={"device": "r1"},
    headers={"Accept": "application/json"},
    timeout=10,
)
print(r.status_code, r.json()["args"])
```

- A. NETCONF `<edit-config>`
- B. REST GET with a query parameter, then prints status and echoed args
- C. Docker build
- D. Ansible gather_facts

**Q27 (MC).** `requests.post(url, json={"hostname": "r1"})` sets:

- A. Form-urlencoded body and no Content-Type
- B. A JSON body and Content-Type application/json
- C. A YAML playbook
- D. An XML RPC

**Q28 (MC).** A job API returns `202 Accepted` and a URL `/tasks/88`. The client later GETs that URL. This is:

- A. Synchronous RPC completing in one round trip
- B. An asynchronous pattern
- C. A Git merge conflict
- D. CSRF

---

## Domain 3 — Cisco Platforms and Development (15%)

**Q29 (MC).** You must list wireless APs in a cloud-managed small-branch org with a Dashboard API key. Which platform?

- A. UCS Manager
- B. Meraki
- C. CUCM AXL
- D. Firepower Management Center only

**Q30 (MC).** `/dna/intent/api/v1/network-device` after a token fetch is characteristic of:

- A. Meraki
- B. Cisco Catalyst Center
- C. Webex Meetings
- D. NTP

**Q31 (MC).** Cisco ACI programmatic access is primarily through:

- A. The APIC object model / REST
- B. Meraki organization inventory
- C. Webex `/rooms`
- D. Docker Hub

**Q32 (MC).** Overlay WAN policies, device templates, and vManage REST are capabilities of:

- A. UCS Manager
- B. Cisco Catalyst SD-WAN
- C. ISE pxGrid only
- D. GitHub Actions

**Q33 (MC).** NSO is best described as:

- A. A wireless LAN controller CLI
- B. A service orchestrator that maps service models to device models
- C. A Python unit-test runner
- D. An OWASP scanner

**Q34 (2).** Which two are compute management platforms on the blueprint? (Choose two.)

- A. UCS Manager
- B. Intersight
- C. Webex
- D. Secure Malware Analytics

**Q35 (MC).** CUCM **AXL** vs **UDS**:

- A. AXL is user-facing REST; UDS is SOAP admin
- B. AXL is administrative SOAP/XML; UDS is user-oriented data services
- C. Both are NETCONF on port 830
- D. Both are Meraki API keys

**Q36 (MC).** You want to create a Webex space, add a person, and post a message. Which resources?

- A. `/rooms`, `/memberships`, `/messages`
- B. `/dna/intent/api/v1/network-device`
- C. `<get-config>`
- D. `docker exec`

**Q37 (MC).** Identity-based network access policy and session directory APIs point to:

- A. Terraform Cloud
- B. Cisco ISE
- C. NTP
- D. CML

**Q38 (MC).** You need a live IOS XE box for RESTCONF practice. Which DevNet resource?

- A. Code Exchange only
- B. Sandbox
- C. A unified diff
- D. OWASP Top 10

**Q39 (MC).** You need sample Python for SD-WAN device lists, not live gear. Which resource?

- A. Sandbox reservation of a 40-node fabric
- B. Code Exchange (or GitHub samples)
- C. TAC severity 1
- D. SNMP trap receiver

**Q40 (MC).** NETCONF on IOS XE commonly uses:

- A. TCP 830 over SSH, XML RPCs
- B. UDP 161
- C. TCP 23
- D. YAML over Telnet

**Q41 (MC).** RESTCONF GET for hostname often looks like:

- A. `ssh router show run | json`
- B. `GET /restconf/data/Cisco-IOS-XE-native:native/hostname` with `Accept: application/yang-data+json`
- C. `POST /webhooks`
- D. `git pull`

**Q42 (INT).** A YANG `list interface { key "name"; leaf name { type string; } leaf enabled { type boolean; } }` means:

- A. Interfaces are identified by `name`; `enabled` is a boolean leaf
- B. Only XML comments are allowed
- C. The list cannot be queried by RESTCONF
- D. Port 80 is required

**Q43 (MC).** NX-OS **NX-API CLI** is typically:

- A. JSON-RPC style posting of CLI commands over HTTP(S)
- B. Only SNMP
- C. Only Webex
- D. Only Terraform HCL

---

## Domain 4 — Application Deployment and Security (15%)

**Q44 (MC).** A benefit of edge computing is:

- A. Higher WAN round-trip for every sensor reading
- B. Processing closer to users or devices to cut latency and backhaul
- C. Replacing DNS
- D. Disabling TLS

**Q45 (MC).** An app runs in a customer-owned data center on OpenStack, with burst VMs in AWS. This is:

- A. Public cloud only
- B. Private cloud only
- C. Hybrid cloud
- D. Bare metal exclusive

**Q46 (2).** Which two are container attributes vs VMs? (Choose two.)

- A. Share the host kernel
- B. Each container must include a full guest OS kernel
- C. Images are typically thinner than VM images
- D. They cannot run in public cloud

**Q47 (MC).** In a CI/CD pipeline, unit tests that run on every commit belong mainly to:

- A. Manual change-advisory meetings only
- B. Continuous integration
- C. Spanning Tree
- D. NAT overload

**Q48 (INT).** Which test is correctly constructed?

```python
import unittest
from net import mask_to_prefix
class T(unittest.TestCase):
    def test_24(self):
        self.assertEqual(mask_to_prefix("255.255.255.0"), 24)
```

- A. It is invalid because unittest cannot test functions
- B. It compares expected 24 to the function result
- C. It starts a Docker daemon
- D. It sends NETCONF

**Q49 (INT).** In a Dockerfile, `CMD ["python", "app.py"]` runs:

- A. At image **build** time
- B. As the default process when a container **starts**
- C. Only on Windows hosts
- D. Instead of FROM

**Q50 (MC).** `EXPOSE 8080` in a Dockerfile:

- A. Publishes the port to the host by itself
- B. Documents the intended port; publishing still needs `-p` (or compose)
- C. Opens 8080 on the corporate firewall
- D. Enables NETCONF

**Q51 (MC).** Storing `MERAKI_API_KEY` in a public GitHub repo is primarily a failure of:

- A. Secret protection
- B. VLAN pruning
- C. NTP stratum
- D. MVC View

**Q52 (MC).** TLS for HTTPS API calls is:

- A. Encryption at rest
- B. Encryption in transit
- C. CSRF
- D. A YANG list key

**Q53 (MC).** A reverse proxy in front of microservices typically:

- A. Replaces MAC learning in a switch ASIC
- B. Terminates TLS and routes by path or hostname to backends
- C. Assigns DHCP leases
- D. Runs OSPF

**Q54 (MC).** SQL injection is best described as:

- A. Injecting script into HTML rendered for other users
- B. Inserting attacker-controlled SQL via unsanitized input
- C. Forging a request from a victim's browser to another site
- D. Rate limiting

**Q55 (MC).** XSS is:

- A. Cross-site scripting in the browser
- B. XML Site Security
- C. A NETCONF capability
- D. A Docker layer

**Q56 (MC).** CSRF:

- A. Is the same as SSH brute force
- B. Tricks an authenticated browser into sending an unwanted state-changing request
- C. Is a YAML indent error
- D. Is encryption at rest

**Q57 (INT).** What does this Bash fragment do?

```bash
mkdir -p /opt/lab && cd /opt/lab
export APP_ENV=prod
cp /tmp/app.env .env
```

- A. Creates a directory, changes into it, sets an environment variable, copies a file
- B. Starts nginx
- C. Commits to Git
- D. Builds a Docker image

**Q58 (MC).** DevOps principles emphasize:

- A. Isolated teams throwing releases over a wall with no telemetry
- B. Collaboration, automation, measurement, and sharing
- C. Telnet as the only management plane
- D. Disabling version control

---

## Domain 5 — Infrastructure and Automation (20%)

**Q59 (MC).** Model-driven programmability adds value because:

- A. Operators scrape always-changing CLI text with no schema
- B. YANG models define structured, validatable data that NETCONF/RESTCONF can read and write
- C. It eliminates the need for authentication
- D. It only works with Telnet

**Q60 (MC).** Configuring one switch via RESTCONF is **device-level**. Pushing campus intent to hundreds of devices via Catalyst Center is:

- A. Also device-level only
- B. Controller-level management
- C. CSRF
- D. Bare metal

**Q61 (2).** Which two tool roles match the blueprint? (Choose two.)

- A. Cisco Modeling Labs simulates network topologies
- B. pyATS tests and parses operational state
- C. OWASP is a routing protocol
- D. NTP forwards Ethernet frames

**Q62 (MC).** Infrastructure as code means:

- A. Clicking uniquely in GUIs so no two devices match
- B. Desired state stored in versioned files and applied repeatably
- C. Disabling Git
- D. Using only Telnet macros

**Q63 (MC).** Terraform is distinctive among the three blueprint tools because it:

- A. Has no state file
- B. Uses declarative HCL and a state file to plan/apply resources
- C. Is a YANG compiler
- D. Replaces DNS

**Q64 (INT).** Identify the workflow:

```python
token = requests.post(f"https://{host}/dna/system/api/v1/auth/token", auth=(u, p), verify=False).json()["Token"]
devs = requests.get(
    f"https://{host}/dna/intent/api/v1/network-device",
    headers={"X-Auth-Token": token},
    verify=False,
).json()
```

- A. Meraki client listing
- B. Catalyst Center authentication then device inventory
- C. Webex message send
- D. Docker image pull

**Q65 (INT).** Identify the workflow:

```python
requests.get(
    "https://api.meraki.com/api/v1/organizations",
    headers={"X-Cisco-Meraki-API-Key": key},
)
```

- A. List Meraki organizations
- B. APIC aaaLogin
- C. NETCONF commit
- D. Terraform destroy

**Q66 (INT).** Identify the workflow:

```python
requests.get(
    f"https://{host}/restconf/data/ietf-interfaces:interfaces",
    auth=(u, p),
    headers={"Accept": "application/yang-data+json"},
    verify=False,
)
```

- A. RESTCONF read of IETF interfaces
- B. Git merge
- C. CSRF attack
- D. DHCP discover

**Q67 (INT).** This playbook task:

```yaml
- name: Ensure nginx is installed
  ansible.builtin.package:
    name: nginx
    state: present
```

- A. Deletes nginx
- B. Installs/ensures the nginx package is present (idempotent package management)
- C. Creates a VLAN
- D. Opens port 830

**Q68 (INT).** Combined with `user: { name: app, state: present }` and `service: { name: nginx, state: started, enabled: true }`, the playbook is automating:

- A. Package install, user management, and service start/enable
- B. Only BGP
- C. Only Docker layer caching
- D. Only Webex rooms

**Q69 (INT).** Bash:

```bash
sudo apt-get update
sudo apt-get install -y python3-pip
sudo useradd -m cicd
cd /opt && tar xzf app.tgz
```

- A. File extract plus package and user creation on a Linux host
- B. NETCONF edit-config
- C. A Terraform provider
- D. MVC View rendering

**Q70 (INT).** RESTCONF body:

```json
{ "Cisco-IOS-XE-native:hostname": "Cat8K" }
```

Status 200. What did you learn?

- A. The device hostname is Cat8K
- B. Authentication failed
- C. The path was a webhook
- D. YAML comments were required

**Q71 (INT).** NETCONF reply contains `<rpc-error>` and `invalid-value`. This means:

- A. Success `ok`
- B. The RPC failed validation or content was rejected
- C. Git conflict
- D. HTTP 201

**Q72 (INT).** `container interfaces-state { config false; ... leaf oper-status ... }` means:

- A. `oper-status` is writable running-config
- B. Operational (read-only) state, not configuration
- C. A Docker CMD
- D. A VLAN ID

**Q73 (MC).** A code review process primarily:

- A. Replaces unit tests and monitoring
- B. Lets peers catch bugs, secret leaks, and design issues before merge
- C. Compiles YANG into OSPF
- D. Assigns MAC addresses

**Q74 (INT).** Sequence: Client → POST `/token` → Controller → 200 token → Client → GET `/devices` → Controller → 200 list. This diagram shows:

- A. Token auth then a synchronous inventory GET
- B. A webhook from device to client first
- C. A merge conflict
- D. DHCP only

---

## Domain 6 — Network Fundamentals (15%)

**Q75 (MC).** A VLAN's primary purpose is:

- A. Encrypting Git repos
- B. Segmenting a LAN into separate L2 broadcast domains
- C. Replacing DNS
- D. Storing Terraform state

**Q76 (MC).** A host `192.168.10.10/24` with gateway `192.168.10.1` sends to `8.8.8.8`. The first hop is:

- A. Direct L2 to 8.8.8.8
- B. The default gateway 192.168.10.1
- C. TCP port 830
- D. The host's MAC as destination IP

**Q77 (MC).** `/30` IPv4 prefix typically provides how many usable host addresses on a point-to-point link (classic usable-host counting)?

- A. 254
- B. 2
- C. 16
- D. 1

**Q78 (MC).** A load balancer's job in a topology is to:

- A. Learn MAC tables only
- B. Distribute client connections across a pool and health-check members
- C. Assign VLANs to Git branches
- D. Run YANG compilers

**Q79 (INT).** Diagram: Client:443 → firewall:443 → LB:443 → app:8080. Which statement is correct?

- A. The client must open NETCONF 830 to the app
- B. HTTPS is permitted to the LB; the app listens on 8080 internally
- C. Telnet is required
- D. The firewall is a hypervisor

**Q80 (MC).** OSPF adjacency formation is primarily which plane?

- A. Management plane
- B. Control plane
- C. Data plane only
- D. CI/CD plane

**Q81 (MC).** SSH to the device CLI uses which plane?

- A. Data plane
- B. Management plane
- C. Spanning Tree plane
- D. Overlay only

**Q82 (MC).** DHCP provides:

- A. Time sync
- B. Dynamic IPv4/IPv6 address and typically mask, gateway, DNS
- C. Git tags
- D. Dockerfile layers

**Q83 (MC).** DNS failure with a hardcoded-name API client typically causes:

- A. Faster RESTCONF
- B. Inability to resolve the API hostname to an IP
- C. Automatic YANG compile
- D. VLAN 1 deletion

**Q84 (2).** Which two port mappings are correct? (Choose two.)

- A. SSH 22/tcp
- B. NETCONF 830/tcp
- C. HTTPS 23/tcp
- D. Telnet 443/tcp

**Q85 (MC).** RESTCONF on IOS XE is most often reached on:

- A. UDP 123
- B. TCP 443
- C. UDP 67
- D. TCP 23

**Q86 (MC).** Packet capture shows SYN to `api.corp:443` with no SYN-ACK. Inside users can ping the API host. Most likely:

- A. DNS is wrong (ping used the name successfully)
- B. Transport port 443 is blocked
- C. The client lacks a MAC address
- D. YAML indent

**Q87 (MC).** The app logs client IP `10.0.255.2` for all users behind a VIP. Users actually sit in `203.0.113.0/24`. Likely:

- A. Source NAT on the firewall or load balancer
- B. A Git rebase
- C. TDD
- D. Observer pattern

**Q88 (MC).** An HTTPS client works at home but fails on corporate Wi-Fi unless `HTTPS_PROXY` is set. Likely:

- A. Missing proxy configuration (and possibly TLS intercept trust)
- B. NETCONF port closed
- C. Docker EXPOSE
- D. MVC Model

**Q89 (MC).** Site-to-site VPN is up but traffic to `10.10.20.0/24` never encrypts. Both sides use `10.10.20.0/24` locally. Likely:

- A. Overlapping encryption domains / VPN overlap
- B. JSON trailing comma only
- C. Python GIL
- D. Unit test discovery

**Q90 (MC).** An API client times out after 2s on a 250 ms RTT satellite link, but curl with a 30s timeout works. This illustrates:

- A. Application sensitivity to latency/timeouts as a network constraint
- B. That 401 is always wrong
- C. That VLANs replace TCP
- D. That YANG is a transport

---

## Answer key

Do not read this section until you have answered.

**Q1 C.** YAML: indentation, `-` lists, `#` comments. Ansible playbooks are YAML. YANG is a model, not this snippet's encoding.

**Q2 C.** JSON literals are lowercase `true`/`false`/`null`. Keys must be double-quoted. No comments. Trailing commas are illegal.

**Q3 B.** JSON arrays become Python `list`.

**Q4 B.** Default xmlns means unprefixed `find("interface")` misses nodes; use a namespace map.

**Q5 B.** Red-green-refactor starts with a failing test.

**Q6 C.** Big-bang specify-then-build is waterfall.

**Q7 B and C.** Testability and reuse. Functions do not skip syntax errors or speed JSON parsing by themselves.

**Q8 C.** Observer: dependents are notified of state changes.

**Q9 C.** Controller maps input to model operations.

**Q10 B.** History, branches, revert/collaboration.

**Q11 B.** Clone copies the repo locally.

**Q12 B.** Commit records the index; you must `git add` first.

**Q13 B.** Pull fetches and integrates.

**Q14 B.** Resolve markers, stage, commit.

**Q15 B.** Minus line removed; two plus lines added (`HOST` and new `url`).

**Q16 B.** Docs specify GET + API key header.

**Q17 B.** Webhooks push events; polling is the inefficient alternative.

**Q18 A and C.** Rate limits and pagination are API consumer constraints. OSPF/STP are not.

**Q19 B.** 401 authentication; 403 authorization.

**Q20 C.** 415 unsupported media type.

**Q21 B.** Honor Retry-After / backoff. Tight loops worsen 429.

**Q22 B.** 201 + Location + JSON body = created resource.

**Q23 C.** Meraki uses `X-Cisco-Meraki-API-Key`.

**Q24 B.** Token endpoint then `X-Auth-Token`. Paths still say `/dna/`.

**Q25 A.** REST vs RPC is about resources vs procedures.

**Q26 B.** `requests.get` with `params` is a REST GET.

**Q27 B.** `json=` serializes and sets Content-Type.

**Q28 B.** 202 + later GET is async job pattern.

**Q29 B.** Meraki cloud dashboard API.

**Q30 B.** Catalyst Center intent API.

**Q31 A.** APIC object model.

**Q32 B.** Catalyst SD-WAN / vManage.

**Q33 B.** NSO service orchestration.

**Q34 A and B.** UCS Manager and Intersight.

**Q35 B.** AXL admin SOAP; UDS user services.

**Q36 A.** Webex rooms, memberships, messages.

**Q37 B.** ISE.

**Q38 B.** Sandbox for live gear.

**Q39 B.** Code Exchange for samples.

**Q40 A.** NETCONF 830/ssh XML.

**Q41 B.** RESTCONF yang-data+json path.

**Q42 A.** list + key + boolean leaf.

**Q43 A.** NX-API CLI JSON-RPC.

**Q44 B.** Edge: locality, latency, backhaul.

**Q45 C.** Hybrid = private + public.

**Q46 A and C.** Shared kernel, smaller images. B is a VM trait.

**Q47 B.** CI runs tests on integrate/commit.

**Q48 B.** Standard TestCase assertion.

**Q49 B.** CMD is runtime, not build (that's RUN).

**Q50 B.** EXPOSE is documentation; `-p` publishes.

**Q51 A.** Secrets in Git.

**Q52 B.** TLS = in transit.

**Q53 B.** Reverse proxy TLS/path routing.

**Q54 B.** SQLi.

**Q55 A.** XSS.

**Q56 B.** CSRF.

**Q57 A.** mkdir/cd/export/cp.

**Q58 B.** CALMS-style DevOps.

**Q59 B.** Structured YANG vs CLI scraping.

**Q60 B.** Controller-level.

**Q61 A and B.** CML simulates; pyATS tests.

**Q62 B.** Versioned desired state.

**Q63 B.** HCL + state + plan/apply.

**Q64 B.** Catalyst Center token + devices.

**Q65 A.** Meraki orgs GET.

**Q66 A.** RESTCONF interfaces.

**Q67 B.** package state present.

**Q68 A.** Matches 5.8 verbs: packages, users, service start.

**Q69 A.** apt, useradd, tar — 5.9.

**Q70 A.** Hostname native container value.

**Q71 B.** rpc-error is failure.

**Q72 B.** config false = operational.

**Q73 B.** Peer review before merge.

**Q74 A.** Sync token then GET.

**Q75 B.** VLAN = L2 segment.

**Q76 B.** Off-subnet → gateway.

**Q77 B.** /30 → 2 usable (classic).

**Q78 B.** LB distribution + health.

**Q79 B.** 443 to LB, 8080 backend.

**Q80 B.** Routing protocols = control plane.

**Q81 B.** SSH = management plane.

**Q82 B.** DHCP addressing options.

**Q83 B.** Name resolution failure.

**Q84 A and B.** 22 and 830. HTTPS is 443, Telnet 23.

**Q85 B.** RESTCONF HTTPS 443.

**Q86 B.** Ping ≠ TCP 443 allowed.

**Q87 A.** SNAT hides real clients.

**Q88 A.** Explicit proxy requirement.

**Q89 A.** Overlapping VPN subnets.

**Q90 A.** Timeouts vs RTT — 6.9.

---

If you missed more than a couple in a domain, reopen that domain in the complete study guide and re-do the lab before taking a commercial practice exam.
