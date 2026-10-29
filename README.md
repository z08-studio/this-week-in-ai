# That Week in AI

Public project scaffold for **That Week in AI**, maintained by **z08 Studio**.

[Subscribe on Substack](https://thatweekinai.substack.com/).

The repository is named `this-week-in-ai` and follows the repository organization of [This Week in Obsidian](https://github.com/z08-studio/this-week-in-obsidian). It contains a neutral issue template, local draft and archive tools, and a content suggestion form. The AI newsletter's content strategy, editorial sections, and publication schedule will be designed separately. No published editions have been imported.

## Drafts and archives

Requirements: Bash and the system `date` command on macOS or Linux. No API key is required.

Create a local draft with an explicit intended publication date:

```sh
bash scripts/newsletter.sh new 2026-11-03
```

The first issue starts at `01`. The script checks existing drafts and archives before assigning the next number and fills the issue heading and date. Any valid calendar date is accepted; there is no preset publication weekday. An explicit date is required until the schedule is decided. The example date does not announce a publication date.

Draft Markdown is ignored by Git. Add and review the content manually. After publishing, archive the matching draft:

```sh
bash scripts/newsletter.sh archive 2026-11-03-issue-01.md
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
