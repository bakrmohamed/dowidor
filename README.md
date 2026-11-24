# Legacy numbered-image downloader

This repository is retained as an early learning script. It is not a recommended downloader or a proof that a server has an IDOR vulnerability. Predictable image names alone do not establish missing authorization.

## Important limits

The current script attempts up to one million sequential image requests and writes successful responses to a local folder. It has no request timeout, rate control, authorization check, content-type validation, response-size limit or reliable error handling. It may create heavy server traffic, consume storage, overwrite existing filenames and stop on network errors. Do not run it against third-party services.

Only inspect or test systems and data you own or have explicit permission to access. Publicly reachable content is not automatic permission to enumerate or save it. Use synthetic local examples for learning rather than collecting other people's images.

## Review status

The code was read but not executed during the portfolio review. No images were requested or downloaded. This documentation update does not add enumeration, evasion or download capabilities, and does not claim past use was authorized.
