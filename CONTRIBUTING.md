# Contributing to sovern-cli 🛠️

Hey, thanks for being here! Whether you're fixing a typo, squashing a bug, or adding a whole new command, we're glad you showed up.

This project is small and friendly. You don't need to be an expert to contribute.

## Ways to help

- **Report a bug.** Something broke? Tell us.
- **Suggest a feature.** Got an idea that would make your life easier? Pitch it.
- **Improve the docs.** If something confused you, it probably confused someone else too.
- **Write code.** Pick up an issue, especially one tagged [`good first issue`](../../issues?q=label%3A%22good+first+issue%22).

## Getting set up

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/<your-username>/sovern-cli.git
cd sovern-cli

# 2. Make a virtual environment (future you will thank you)
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# 3. Install in editable mode so your changes show up right away
pip install -e .

# 4. Check it works
sovern --help
```

To try out commands against the real service you'll need a SovernStack API key:

```bash
sovern login --token <your-api-key>
```

Please don't commit your API key. Seriously. Not even "just for a second."

## Making a change

1. **Make a branch** off `main` with a name that says what you're doing:
   ```bash
   git checkout -b fix/gpu-list-crash
   ```
2. **Make your changes.** Keep them focused. One PR, one idea.
3. **Test it.** Run the commands you touched and make sure they behave. If the project has tests, run those too, and add one if you're fixing a bug.
4. **Commit** with a message that makes sense to a human:
   ```
   Fix crash when gpu list returns an empty response
   ```
5. **Push** and open a pull request.

## What we're focused on right now

The CLI currently does two things, and we want those to be great before we add more:

- **`gpu list`**: listing available GPU capacity
- **`deploy`**: deploying models as live endpoints (**ONNX only** for now)

PRs that improve these are very welcome. If you want to add something big, like a new command or support for another model format, please [open an issue](../../issues) first so we can chat before you spend a weekend on it.

## Pull request tips

- Say **what** you changed and **why** in the description.
- Link the issue it fixes (e.g. `Fixes #42`).
- Screenshots or terminal output are great for anything that changes how the CLI looks or behaves.
- Don't stress about perfection. We'll review it together.

## Reporting bugs

Open an [issue](../../issues) and include:

- What you ran (the exact command)
- What you expected to happen
- What actually happened (error messages, please!)
- Your OS and Python version
- Your `sovern` version

Just remove your API key from anything you paste.

## Code style

Keep it readable. Clear names beat clever tricks. Add a comment when something isn't obvious, and match the style of the code around you.

## Be nice

We want this to be a place where everyone feels welcome. Be kind, be patient, assume good intent, and help each other out. Harassment or being a jerk isn't okay and will get you booted.

## Questions?

Not sure about something? Open an issue and ask. There are no dumb questions here.

Thanks for helping make sovern-cli better. 💜
