# Repository guidelines

- This is the public template and archive repository for That Week in AI. Keep credentials, generated candidates, caches, and unpublished draft Markdown out of commits.
- The publication name is **That Week in AI**, its Substack URL is `https://thatweekinai.substack.com/`, and the repository slug is `this-week-in-ai`.
- `templates/` contains the issue template; `scripts/newsletter.sh` creates and archives local drafts; `archive/YYYY/` contains reviewed, published editions only.
- Tuesday is an initial configurable workflow default. Do not describe it as a confirmed publication commitment. Keep explicit issue dates aligned with the generator.
- Keep tracked documentation and newsletter content in English.
- Run `bash -n scripts/newsletter.sh` and `python3 -B -m unittest discover -s tests -v` after changing maintenance tools or templates.
- Publishing to Substack is manual. Do not publish a newsletter or archive an unpublished edition unless directly requested.
