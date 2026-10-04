# BROSPP: Python Project Collection

BROSPP (Big Repository of Small Python Projects) is a collection of independent Python exercises, command-line utilities, and small experiments. Projects are kept in separate directories so each can be explored and run on its own.

## Project Catalog

- [Bullet Adder](projects/bullet-adder/README.md): turn clipboard lines into a Markdown list.
- [Calculator](projects/calculator/README.md): command-line arithmetic operations.
- [Chess Simulator](projects/chess-simulator/README.md): an educational chess simulation.
- [Coin Flip Streaks](projects/coin-flip-streaks/README.md): explore streaks in random coin flips.
- [Desktop Folder Finder](projects/desktop-folder-finder/README.md): inspect folders beneath the user's Desktop directory.
- [Email Extractor](projects/email-extractor/README.md): extract email-like strings from clipboard text.
- [Fantasy Game](projects/fantasy-game/README.md): an early object-oriented fantasy game experiment.
- [Food Day Questionnaire](projects/food-day-questionnaire/README.md): planning notes for a food and health questionnaire.
- [Matrix Screen](projects/matrix-screen/README.md): a terminal matrix-style animation.
- [Mini Search Engine](projects/mini-search-engine/README.md): a small document-search experiment.
- [OpenStreetMap Launcher](projects/openstreetmap-launcher/README.md): open a street address in OpenStreetMap.
- [OpenWeather Geocoder](projects/openweather-geocoder/README.md): retrieve coordinates and weather from OpenWeather.
- [Random Quiz Generator](projects/random-quiz-generator/README.md): generate randomized geography quiz material.
- [Regex Search](projects/regex-search/README.md): search files using a regular expression.
- [Regex Strip](projects/regex-strip/README.md): trim matching characters from string edges.
- [Snowstorm](projects/snowstorm/README.md): a terminal snow animation with a shell launcher.
- [Testing Sandbox](projects/testing-sandbox/README.md): a placeholder for small tests and experiments.
- [Traffic Light Simulator](projects/traffic-light-simulator/README.md): cycle through traffic light states in the terminal.

## Getting Started

Use Python 3 for the projects. Most are standalone scripts and use only the Python standard library; projects that need third-party packages or credentials document them in their own README. For example:

```bash
python projects/calculator/acalc.py --help
```

Run commands from the project directory when a program reads or writes relative paths. Check that project's README first, especially for scripts that access the clipboard, inspect local files, create output, or call an online service.

## Repository Layout

```text
projects/
	<project-name>/
		README.md
		<source files>
```

The projects are intentionally independent; there is no shared dependency set or single application entry point. Local virtual environments, API keys, private credentials, logs, and generated files are excluded by the root `.gitignore`.

## Contributing

Keep each project self-contained, add or update its README when behavior or setup changes, and avoid committing credentials or generated local data. Small, focused improvements and tests are welcome.

## License

This repository is distributed under the MIT License. See [LICENSE](LICENSE).
