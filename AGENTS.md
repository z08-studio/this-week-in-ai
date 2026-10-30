# Repository guidelines

- This is the public project scaffold for That Week in AI. Keep credentials, generated candidates, caches, and unpublished draft Markdown out of commits.
- The publication name is **That Week in AI**, its Substack URL is `https://thatweekinai.substack.com/`, and the repository slug is `this-week-in-ai`.
- The approved schedule is Monday, covering the previous Monday through Sunday in Asia/Shanghai. Do not inherit Obsidian's Tuesday schedule.
- The issue template groups content into seven topics: Models & APIs; AI Tools & Agents; AI & Video; Images, Audio & Multimodal; FDE & Production Delivery; Research & Evaluation; Workflows & Learning. Keep headings and order aligned with the private generator's formatted template.
- Reddit and YouTube are discovery channels, not reader-facing sections. Categorize their items by subject; AI & Video means AI applied to video. Use one primary section per event, preserve useful original links and keep bullets concise.
- `templates/` contains the issue template; `scripts/newsletter.sh` creates and archives local drafts; `archive/YYYY/` is for reviewed, published editions only. Collectors, scoring and generation code remain separate work.
- Draft creation requires an explicit date and currently validates calendar dates without enforcing a weekday. Choose the intended publication Monday explicitly. The script does not generate or publish content.
- Keep tracked documentation and newsletter content in English.
- Run `bash -n scripts/newsletter.sh` and `python3 -B -m unittest discover -s tests -v` after changing maintenance tools or templates.
- Publishing to Substack is manual. Do not publish or archive an unpublished edition unless directly requested.
- This repository belongs to **This Week In Newsletters**. Commit directly to `main` by default; create a pull request only when the user explicitly requests one.
