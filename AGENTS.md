# Repository guidelines

- This is the public project scaffold for That Week in AI. Keep credentials, generated candidates, caches, and unpublished draft Markdown out of commits.
- The publication name is **That Week in AI**, its Substack URL is `https://thatweekinai.substack.com/`, and the repository slug is `this-week-in-ai`.
- The user explicitly deferred AI content generation strategy. Do not prescribe sources, scoring, editorial sections, or a publication schedule until directly requested. Do not inherit Obsidian's content strategy or Tuesday schedule.
- `templates/` contains a neutral issue placeholder; `scripts/newsletter.sh` creates and archives local drafts; `archive/YYYY/` is for reviewed, published editions only.
- Draft creation requires an explicit date and accepts any valid calendar date. The script does not generate or publish content.
- Keep tracked documentation and newsletter content in English.
- Run `bash -n scripts/newsletter.sh` and `python3 -B -m unittest discover -s tests -v` after changing maintenance tools or templates.
- Publishing to Substack is manual. Do not publish or archive an unpublished edition unless directly requested.
