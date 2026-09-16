# Deposit preparation (not a release)

Intended repository name: **closed-schur-channel-compression**. This is the
renamed identity of the existing unpublished project, not a new scientific work.
No live repository URL, version DOI, concept DOI, publication date, or release
version is assigned here.

After the owner approves an external audit and publication, use the clean
allowlisted export, set the actual repository URL and release version, enable
the intended Zenodo integration, and only then create the authorized release.
Check the minted record before adding its DOI to CITATION.cff and the paper.

Before any authorized release:

1. Select the freshly verified export, not an earlier candidate. Check its
   manifest and build the PDF outside the frozen directory.
2. Initialize or reconcile the public repository using only the allowlisted
   files; inspect the staged file list and initial commit before pushing.
3. Set the real repository URL, version, and date. Do not invent a DOI in advance.
4. Enable Zenodo for that exact repository before creating the release.
5. Recheck the deposited PDF, author, citations, licenses, and archived files.
   Replace the provisional README status only after publication is confirmed.

The export ZIP contains only files named by the manifest and the manifest
itself. Build output, private research notes, and superseded PDFs are excluded.

Author: Seth Douglas, seth.douglas@gmail.com. No affiliation or ORCID supplied.
Resource type: publication / preprint. Manuscript license CC BY 4.0; original
software license MIT, with the file scopes in LICENSE.md. Automatic ingestion
of two license scopes is not assumed: inspect the resulting Zenodo record and
ensure its description and license metadata accurately distinguish the files.
A root .zenodo.json declares the aggregate Other (Open) category and states the two file-specific licenses in its description, as in the companion releases, because the GitHub integration accepts one license field.

Suggested description: A finite closed mixed-apparatus construction approximates
Schur channels in half diamond distance using physical dimension of order
epsilon^-2 times (square root of Gram rank plus log input dimension). An extreme
ququart tensor family exhibits a matched leading exact-versus-vanishing-error
memory separation. A separately scoped scheduled-delivery theorem compares
sublogarithmic and superlogarithmic delay. No gate-efficiency or arbitrary-channel
upper bound is claimed.
