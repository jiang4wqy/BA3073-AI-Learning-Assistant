# BA3073 Assignment Report Instructions

Approved by the user on 2026-11-01.

## Scope

Revise the instructions in `backend/pipelines/essay_html.py` for the BA3073
take-home assignment, "From AI Agent to Cloud Service". Keep the existing
provider interface, HTML output contract, PDF conversion, and generic essay
capability.

## Report Requirements

- Explain objectives and the deployed architecture.
- Cover local Docker deployment, verification, and persistent storage.
- Cover the local image, ACR push/pull, Linux architecture, ECS container,
  port mapping, and source-IP-restricted security group.
- Cover domain DNS, Nginx, HTTPS, independent proxy authentication, and
  removal of public port 14242 after the proxy works.
- Reference supplied screenshots, URLs, and logs as evidence.
- Distinguish completed checks, observed failures, missing evidence, and
  proposed improvements. Never fabricate results, screenshots, or costs.
- Explain the actual configured model provider, including the user's
  requested DeepSeek substitution for the assignment's Qwen instructions.
- Discuss security, cloud cost, and practical improvements.
- Produce a concise report of no more than 20 A4 pages, including evidence.
- Exclude credentials, tokens, passwords, and private keys from the report.

## Implementation and Verification

1. Add assignment-specific guidance to the existing system prompt.
2. Run the existing essay and HTML/PDF tests; baseline: 14 passing tests.
3. Rebuild the image and deploy through the user's private ACR repository.
4. Generate the report with the deployed application and real evidence.
5. Inspect the resulting PDF page count, evidence, and unfinished items.

## Self-Review

The scope is limited to report instructions. Runtime credentials stay in
ignored files. Real screenshots and successful Task 3 deployment remain
required before the assignment can be described as fully complete.
