# Security

## Secrets

- Never commit credentials.
- Approved secret-loading path: none for the initial benchmark; model inference is local and no runtime provider key is required.
- Local-first operation is the default; any future external provider requires an explicit decision record.

## Untrusted input

- Treat indexed documents and retrieved text as untrusted input.
- Preserve source provenance and isolate retrieved content from control instructions.
- Query rewrites and generated answers must be logged as separate artifacts.
- Prompt-injection handling must be tested before production use.

## External actions

- External or destructive actions require explicit approval.
- The research MVP declares no external actions.

## Data

- The initial corpus is synthetic English Markdown under `data/corpus/`; PDF ingestion is deferred.
- Do not use private enterprise data without an explicit retention, access, deletion, and provider policy.
- Tenant isolation and document-level permissions are deferred until the corpus and use case are defined.
