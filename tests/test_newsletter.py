from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]


class NewsletterScriptTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ("scripts", "templates", "drafts", "archive/2026"):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        for filename in ("scripts/newsletter.sh", "templates/newsletter-template.md"):
            shutil.copy2(REPO_ROOT / filename, self.root / filename)
        (self.root / "archive/2026/2026-10-13-issue-43.md").write_text(
            "# That Week in AI #43\n"
        )

    def run_script(self, *args, env=None):
        return subprocess.run(
            ["bash", str(self.root / "scripts/newsletter.sh"), *args],
            cwd=self.root,
            env=env,
            capture_output=True,
            text=True,
        )

    def test_explicit_publication_date_and_issue_heading(self):
        result = self.run_script("new", "2026-10-20")
        self.assertEqual(result.returncode, 0, result.stderr)
        draft = self.root / "drafts/2026-10-20-issue-44.md"
        self.assertTrue(draft.exists())
        self.assertEqual(draft.read_text().splitlines()[0], "# That Week in AI #44")

    def test_first_issue_starts_at_one(self):
        (self.root / "archive/2026/2026-10-13-issue-43.md").unlink()
        result = self.run_script("new", "2026-10-20")
        self.assertEqual(result.returncode, 0, result.stderr)
        draft = self.root / "drafts/2026-10-20-issue-01.md"
        self.assertIn("# That Week in AI #01", draft.read_text())
        self.assertIn("**Publication date**: 2026-10-20", draft.read_text())

    def test_publication_date_is_not_restricted_to_a_weekday(self):
        result = self.run_script("new", "2026-10-21")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.root / "drafts/2026-10-21-issue-44.md").exists())

    def test_archive_does_not_overwrite_published_issue(self):
        draft = self.root / "drafts/2026-10-20-issue-44.md"
        archive = self.root / "archive/2026/2026-10-20-issue-44.md"
        draft.write_text("Draft\n")
        archive.write_text("Published\n")
        result = self.run_script("archive", draft.name)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(draft.read_text(), "Draft\n")
        self.assertEqual(archive.read_text(), "Published\n")

    def test_archive_rejects_files_outside_drafts(self):
        external = self.root / "2026-10-20-issue-44.md"
        external.write_text("Outside drafts\n")
        result = self.run_script("archive", str(external))
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(external.exists())

    def test_new_requires_an_explicit_publication_date(self):
        result = self.run_script("new")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("explicit publication date", result.stderr)
        self.assertEqual(list((self.root / "drafts").iterdir()), [])

    def test_create_and_archive_round_trip(self):
        created = self.run_script("new", "2026-10-20")
        self.assertEqual(created.returncode, 0, created.stderr)
        draft = self.root / "drafts/2026-10-20-issue-44.md"
        content = draft.read_text()

        archived = self.run_script("archive", draft.name)
        self.assertEqual(archived.returncode, 0, archived.stderr)
        self.assertFalse(draft.exists())
        self.assertEqual(
            (self.root / "archive/2026/2026-10-20-issue-44.md").read_text(),
            content,
        )

    def test_existing_draft_or_archive_prevents_duplicate_date(self):
        for directory in ("drafts", "archive/2026"):
            with self.subTest(directory=directory):
                existing = self.root / directory / "2026-10-20-issue-44.md"
                existing.write_text("Existing issue\n")
                result = self.run_script("new", "2026-10-20")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("already exists", result.stderr)
                self.assertEqual(existing.read_text(), "Existing issue\n")
                self.assertFalse((self.root / "drafts/2026-10-20-issue-45.md").exists())
                existing.unlink()

    def test_invalid_dates_leave_drafts_empty(self):
        for publication_date in ("2026-02-30", "2026-1-6", "tomorrow"):
            with self.subTest(publication_date=publication_date):
                result = self.run_script("new", publication_date)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(list((self.root / "drafts").iterdir()), [])

    def test_future_draft_still_blocks_earlier_publication_date(self):
        existing = self.root / "drafts/2026-10-27-issue-44.md"
        existing.write_text("Future draft\n")
        result = self.run_script("new", "2026-10-20")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dated after 2026-10-20", result.stdout)
        self.assertEqual(existing.read_text(), "Future draft\n")
        self.assertEqual(list((self.root / "drafts").iterdir()), [existing])


if __name__ == "__main__":
    unittest.main()
