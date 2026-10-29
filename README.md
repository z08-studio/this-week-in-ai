# That Week in AI

**That Week in AI** is a weekly newsletter about AI developments, research, tools, and practical ideas, maintained by **z08 Studio**.

[Subscribe on Substack](https://thatweekinai.substack.com/).

This public repository is named `this-week-in-ai`. It follows the template and archive workflow of [This Week in Obsidian](https://github.com/z08-studio/this-week-in-obsidian). It starts with a template and maintenance tools; no AI newsletter issues have been imported or marked as published.

## Editorial sections

- Models & announcements
- Pick of the week, selected and written manually
- Research
- Tools & releases
- Workflows & learning

Prefer original announcements, repositories, papers, and hands-on resources. Attribute claims to their sources, distinguish preprints from reviewed findings, and verify access, availability, and benchmarks before publication.

## Drafts and archives

Requirements: Bash and the system `date` command on macOS or Linux. No API key is required.

Create a draft with its intended publication date:

```sh
bash scripts/newsletter.sh new 2026-11-03
```

The first issue starts at `01`. The script checks drafts and archives before assigning the next number. It fills the issue number and publication date and rejects duplicate dates. Draft Markdown is ignored by Git; only reviewed, published issues should be archived and committed.

The initial workflow defaults to Tuesday for parity with the Obsidian project. This is an editable workflow default, rather than an announced publication schedule. Without a date, `new` selects the next configured weekday, including a full week ahead when run on that weekday. Override it with `NEWSLETTER_WEEKDAY` (`1` = Monday through `7` = Sunday):

```sh
NEWSLETTER_WEEKDAY=5 bash scripts/newsletter.sh new 2026-11-06
```

Keep that weekday aligned with the private generator's `config.toml`. Pass an explicit issue date to both tools when preparing a particular edition.

Review generated material privately, then copy the approved content into the local draft. Publishing to Substack remains manual. After publication, archive the matching draft:

```sh
bash scripts/newsletter.sh archive 2026-11-03-issue-01.md
```

This moves the file into `archive/2026/`. The filename date must match the actual publication date. Archive contents become public when committed and pushed. Existing archive files are protected from replacement.

Run deterministic checks without touching real issues:

```sh
bash -n scripts/newsletter.sh
python3 -B -m unittest discover -s tests -v
```

## Suggest content

[Submit a suggestion](https://github.com/z08-studio/this-week-in-ai/issues/new?template=content-suggestion.yml) with a primary source and a short explanation. Suggestions are reviewed manually; submission does not guarantee inclusion. Contributions to published archives can be proposed through pull requests.

## License

Code, templates, and original repository material are available under the [MIT License](LICENSE). Linked third-party material retains its original ownership and license.
