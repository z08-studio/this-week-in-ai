# That Week in AI

Public project scaffold for **That Week in AI**, maintained by **z08 Studio**.

[Subscribe on Substack](https://thatweekinai.substack.com/).

The repository is named `this-week-in-ai` and follows the repository organization of [This Week in Obsidian](https://github.com/z08-studio/this-week-in-obsidian). It contains a blank draft starter, local draft and archive tools, and a content suggestion form. No published editions have been imported.

Publish every Monday, covering the preceding Monday through Sunday in `Asia/Shanghai`. The half-open collection window is `[previous Monday 00:00, issue Monday 00:00)`.

## Issue structure

The private generator's Formatted template owns the reader-facing layout. Picks opens the edition; the remaining content is grouped into Models & APIs; AI Tools & Agents; AI & Video; Images, Audio & Multimodal; FDE & Production Delivery; Research & Evaluation; Workflows & Learning. Keep `templates/newsletter-template.md` empty here.

Use one descriptive Markdown link per bullet, normally 10–18 words. Put the useful information, attribution and any essential condition inside the link text; do not append explanations or supporting links. Each event has one primary section. Reddit and YouTube content is categorized by subject. AI & Video covers AI applied to video, while a video about FDE belongs in FDE. Remove empty sections before publication. The initial generator target is about 80 distinct items, including 8 Picks; each item appears once and quantities remain configurable in the private generator.

The private workflow is source-grouped `generate`, then topic-grouped `format`, followed by the editor's manual edits and copying approved content here. Content collection and generation are not implemented in this public repository.

## Drafts and archives

Requirements: Bash and the system `date` command on macOS or Linux. No API key is required.

Create a local draft with an explicit intended publication date:

```sh
bash scripts/newsletter.sh new 2026-11-02
```

The first issue starts at `01`. The script checks existing drafts and archives before assigning the next number, then creates an empty file named with the date and issue number. Choose the intended publication Monday explicitly. The helper currently validates calendar dates without enforcing a weekday. The example date does not announce an actual issue.

Draft Markdown is ignored by Git. Copy the reviewed Formatted output from the private generator into the empty file, then edit it manually. The generator's `output/templates/formatted_template.md` is the sole content template. After publishing, archive the matching draft:

```sh
bash scripts/newsletter.sh archive 2026-11-02-issue-01.md
```

The file moves into `archive/2026/`. Its date should match the actual publication date. Archive contents become public when committed and pushed; only reviewed, published editions belong there. Existing archive files are protected from replacement.

## Checks

Run the checks without modifying real issues:

```sh
bash -n scripts/newsletter.sh
python3 -B -m unittest discover -s tests -v
```

GitHub CI runs these checks on Linux and macOS.

## Suggest content

[Submit a suggestion](https://github.com/z08-studio/this-week-in-ai/issues/new?template=content-suggestion.yml) with a primary link and a short explanation. Suggestions are reviewed manually. Contributions to published material can be proposed through pull requests.

## License

Code, templates, and original repository material are available under the [MIT License](LICENSE). Linked third-party material retains its original ownership and license.
