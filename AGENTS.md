# Repository guidelines

- This is the public publication and archive repository for This Week in AI. Keep credentials, generated candidates, caches, and unpublished draft Markdown out of commits.
- The publication name is **This Week in AI**, its Substack URL is `https://thatweekinai.substack.com/`, and the repository slug is `this-week-in-ai`.
- The approved schedule is Monday, covering the previous Monday through Sunday in Asia/Shanghai. Do not inherit Obsidian's Tuesday schedule.
- The private generator's Formatted template owns the issue layout: Picks, then Models & APIs; AI Tools & Agents; AI & Video; Images, Audio & Multimodal; FDE & Production Delivery; Research & Evaluation; Workflows & Learning.
- Reddit and YouTube are discovery channels, not reader-facing sections. Categorize their items by subject; AI & Video means AI applied to video. Use one primary placement per event, including Picks, preserve useful original links and keep bullets concise.
- Each reader item is one descriptive Markdown link, normally 10–18 words. Put the useful information and essential qualifications inside its text; do not append body copy, annotations or supporting links.
- Maintain the content template only in the private generator's `output/templates/formatted_template.md`; do not add a local `templates/` directory. `scripts/newsletter.sh` creates empty local drafts and archives reviewed editions; `archive/YYYY/` is for reviewed, published editions only. Collectors, scoring and generation code remain separate work.
- Draft creation requires an explicit date and currently validates calendar dates without enforcing a weekday. Choose the intended publication Monday explicitly. The date and issue number appear only in the new filename; copy reviewed Formatted output into the empty file. The script does not generate or publish content.
- Keep tracked documentation and newsletter content in English.
- Keep the README focused on readers: banner, short introduction, subscription, and suggestions. Maintenance instructions live in `docs/maintenance.md`. Use `assets/avatar.png` for the approved blue folded A identity and `assets/banner.png` for the README masthead.
- Run `bash -n scripts/newsletter.sh` and `python3 -B -m unittest discover -s tests -v` after changing maintenance tools.
- Publishing to Substack is manual. Do not publish or archive an unpublished edition unless directly requested.
- This repository belongs to **This Week In Newsletters**. Commit directly to `main` by default; create a pull request only when the user explicitly requests one.
