# mlf.evemisslab.com

The public site for
[MLF](https://github.com/kakon77777-commits/matrix-ledger-format) — the AI
Matrix Ledger Format 1.0 and its reference compiler, `mlfc` 1.0.0.

An EveMissLab sub-site, and the third of the 3M set alongside
[mmr.evemisslab.com](https://mmr.evemisslab.com) and
[mmlc.evemisslab.com](https://mmlc.evemisslab.com). Static HTML from a single
Python script, served by an assets-only Cloudflare Worker.

## Build

```bash
python build.py
```

Writes fourteen pages plus `sitemap.xml`, `robots.txt`, `404.html` and the
favicon into `dist/`. Standard library only.

## Deploy

```bash
npx wrangler deploy
```

## Local preview

```bash
python -m http.server 8794 --directory dist
```

## Shape

```
build.py             renderers, page shell, sitemap, 404
src/content.py       every string, EN and zh-Hant, one block list per page
src/assets/          styles.css, app.js — copied verbatim into dist/assets/
dist/                build output, not committed
```

English at the root, Traditional Chinese under `/zh/`. The build fails if a
page is missing from either language.

## Where the content comes from

Every claim traces to a document in the matrix-ledger-format repository —
`README.md`, `docs/specification/MLF_1.0.md`, the `docs/architecture/` set,
`docs/release/RELEASE_NOTES_v1.0.0.md`, `SECURITY.md` — or to
`MLF_1.0_RELEASE_VERIFICATION.json` from the v1.0 release bundle.

The two lists of non-claims are reproduced unedited, because in this project
they are part of the specification rather than a disclaimer attached to it.

## Design notes

**The container.** MLF is a file format, so the site is built like one: dark
field by default, monospace paths, and colour used as a typed field marker
rather than as decoration. Dark-first is deliberate — its two siblings are
light-first, and a binary container reads as a field of records, not as paper.

**The organising system is MLF's own four fingerprints.** Every accent on the
site is one of them, and nothing is tinted that does not feed one:

| Token               | Computed over                                              |
| ------------------- | ---------------------------------------------------------- |
| `--fp-structural`   | matrices, coordinates, roles, regions, dependencies, routes |
| `--fp-content`      | values and source formulas                                  |
| `--fp-semantic`     | normalized structure plus content meaning                   |
| `--fp-presentation` | styles, layout, human-view metadata                         |

The hero is the package anatomy: the `.mlfdir` layout with every member marked
by the fingerprints it feeds. That mapping is derived from the README's layout
and fingerprint definitions, so the colour coding is a fact about the format
rather than a mood.

**Type.** Archivo for display, Zilla Slab for prose, Azeret Mono for paths,
hashes and data. Disjoint from both sibling sites; the three 3M sites share a
family and a build system, not a template.

**No side rail.** MMR puts its section index on the left, MMLC on the right;
this one runs it as an inline strip under the standfirst, which gives the
widest measure of the three and suits a reference document.

## Licence

MLF and MLF Compiler are Apache-2.0.
