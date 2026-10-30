# Maintenance

This repository holds the publication assets, local draft tools, and reviewed archive for **This Week in AI**. Collection, scoring, and generation belong in the private `gen-newsletter-ai` workspace.

## Editorial handoff

Publish every Monday, covering the preceding Monday through Sunday in `Asia/Shanghai`. The collection window is `[previous Monday 00:00, issue Monday 00:00)`.

The generator owns the sole content template at `output/templates/formatted_template.md`. Its workflow is source-grouped `generate`, then topic-grouped `format`, followed by manual review and copying approved Formatted output here. Picks opens the edition. The initial target is about 80 distinct items, including 8 Picks; quantities remain configurable in the generator.

Use one descriptive Markdown link per bullet, normally 10–18 words. Keep useful information and essential qualifications inside the link text. Each event appears once. Categorize Reddit and YouTube material by subject, and remove empty sections before publication.

Review content suggestions through the existing GitHub issue form. Contributions to published material can be proposed through pull requests.

## Drafts and archives

Requirements: Bash and the system `date` command on macOS or Linux. No API key is required.

Create an empty draft with an explicit intended publication date:

```sh
bash scripts/newsletter.sh new 2026-11-02
```

The first issue starts at `01`. The helper checks existing drafts and archives before assigning the next number, then creates an empty file named with the date and issue number. It validates calendar dates without enforcing a weekday; choose the intended Monday explicitly. The example does not announce an issue.

Drafts and their attachments are ignored by Git. Copy reviewed Formatted output into the empty file and edit it manually. After publishing, archive the matching draft:

```sh
bash scripts/newsletter.sh archive 2026-11-02-issue-01.md
```

The file moves into `archive/2026/`. The filename date should match the actual publication date. Only reviewed, published editions belong in the archive. Existing archive files are protected from replacement.

## Assets

- `assets/avatar.png`: the approved A1b refined blue folded A logo, copied from the fixed brand master.
- `assets/banner.png`: the blue README masthead, matching the Obsidian banner's editorial style.

The publication is named **This Week in AI**; its subscription address remains `https://thatweekinai.substack.com/`.

## Checks

```sh
bash -n scripts/newsletter.sh
python3 -B -m unittest discover -s tests -v
```

These checks use temporary fixtures and do not modify real issues. GitHub CI runs them on Linux and macOS.

Code and original repository material are available under the [MIT License](../LICENSE). Linked third-party material retains its original ownership and license.
