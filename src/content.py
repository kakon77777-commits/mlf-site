# -*- coding: utf-8 -*-
"""
Content for the MLF 1.0 site.

Every string traces to a document in the matrix-ledger-format repository:
README.md, README.zh-TW.md, docs/specification/MLF_1.0.md,
docs/architecture/{ARCHITECTURE, COMPATIBILITY, MIGRATION, THREAT_MODEL}.md,
docs/release/RELEASE_NOTES_v1.0.0.md, SECURITY.md, CHANGELOG.md, and the
release bundle's MLF_1.0_RELEASE_VERIFICATION.json.

Nothing here claims more than those documents claim.
"""

SITE = {
    "domain": "mlf.evemisslab.com",
    "origin": "https://mlf.evemisslab.com",
    "repo": "https://github.com/kakon77777-commits/matrix-ledger-format",
    "lab": "https://evemisslab.com",
    "spec": "1.0",
    "compiler": "1.0.0",
    "cli": "mlfc",
    "release_date": "2026-07-23",
    "licence": "Apache-2.0",
}

SLUGS = ["", "format", "fingerprints", "compile", "safety", "limits", "versions"]

# --------------------------------------------------------------------------
# The package anatomy, colour-coded by which fingerprint each part feeds.
# Layout from README.md; fingerprint definitions from README.md "Four
# independent fingerprints"; record roles from docs/architecture/ARCHITECTURE.md.
# --------------------------------------------------------------------------

FP_KEYS = ["structural", "content", "semantic", "presentation"]

ANATOMY = {
    "en": [
        {"path": "manifest.json", "fp": [],
         "what": "The unique entry point. Selects the document-level resources; nothing else may claim to be the root."},
        {"path": "substrate.json", "fp": [],
         "what": "The physical substrate record — layer L0, describing what this package was made from."},
        {"path": "matrices/<m>.cells.jsonl", "fp": ["structural", "content", "semantic"],
         "what": "One record per cell: coordinate, stable ID, primitive type, value, and role. A coordinate says where a cell currently appears; the stable ID says which semantic object it is."},
        {"path": "matrices/<m>.regions.jsonl", "fp": ["structural", "semantic"],
         "what": "Header, body, table, merge, filter and named-range regions, inferred or imported rather than guessed silently."},
        {"path": "matrices/<m>.styles.jsonl", "fp": ["presentation"],
         "what": "Styles and layout metadata. Kept separately so a package can differ here and still be semantically identical."},
        {"path": "formulas/formula_ast.jsonl", "fp": ["content", "semantic"],
         "what": "The formula triple: source expression, normalized AST, and the dependency edges it implies. Disagreement between the three is evidence, and gets reported."},
        {"path": "graphs/dependencies.jsonl", "fp": ["structural", "semantic"],
         "what": "Explicit dependency edges, including cross-sheet ones. An edge is a record, not an inference made at read time."},
        {"path": "graphs/routes.jsonl", "fp": ["structural"],
         "what": "Traversal routes — row-major, column-major and others. Reading order is data, not an assumption baked into a reader."},
        {"path": "projections/human_views.jsonl", "fp": ["presentation"],
         "what": "Human-readable projections. Reversible views of the structure, never a replacement for it."},
        {"path": "provenance/events.jsonl", "fp": [],
         "what": "Append-only history. Events are added; nothing rewrites what already happened."},
        {"path": "vocabularies/roles.json", "fp": ["structural", "semantic"],
         "what": "The role vocabulary this package uses, so a role name means the same thing to every reader."},
        {"path": "reports/fingerprints.json", "fp": ["structural", "content", "semantic", "presentation"],
         "what": "The four hashes themselves, recorded inside the package they describe."},
        {"path": "reports/import_loss.json", "fp": [],
         "what": "What the import could not carry. Unsupported or partially reconstructed behaviour is written down rather than silently guessed."},
        {"path": "checksums.json", "fp": [],
         "what": "Binds every path to its bytes, verified with SHA-256."},
    ],
    "zh": [
        {"path": "manifest.json", "fp": [],
         "what": "唯一的進入點。選定文件層級的資源；沒有別的東西可以自稱是根。"},
        {"path": "substrate.json", "fp": [],
         "what": "實體基底紀錄 —— L0 層，描述這個封包是從什麼做出來的。"},
        {"path": "matrices/<m>.cells.jsonl", "fp": ["structural", "content", "semantic"],
         "what": "一格一筆：座標、穩定 ID、原始型別、值與角色。座標回答「這格現在出現在哪」，穩定 ID 回答「它是哪一個語意物件」。"},
        {"path": "matrices/<m>.regions.jsonl", "fp": ["structural", "semantic"],
         "what": "表頭、本體、表格、合併、篩選與具名範圍等區域，是推論或匯入來的，不是默默猜的。"},
        {"path": "matrices/<m>.styles.jsonl", "fp": ["presentation"],
         "what": "樣式與版面中繼資料。分開存放，所以兩個封包可以在這裡不同、語意上卻完全相同。"},
        {"path": "formulas/formula_ast.jsonl", "fp": ["content", "semantic"],
         "what": "公式三元組：來源運算式、正規化 AST，以及它蘊含的相依邊。三者之間的不一致是證據，會被回報。"},
        {"path": "graphs/dependencies.jsonl", "fp": ["structural", "semantic"],
         "what": "明確的相依邊，包含跨工作表的。一條邊是一筆紀錄，不是讀取時才推論出來的東西。"},
        {"path": "graphs/routes.jsonl", "fp": ["structural"],
         "what": "遍歷路徑 —— 列優先、欄優先與其他。閱讀順序是資料，不是烙在讀取器裡的假設。"},
        {"path": "projections/human_views.jsonl", "fp": ["presentation"],
         "what": "給人看的投影。它們是結構的可逆視圖，永遠不是結構的替代品。"},
        {"path": "provenance/events.jsonl", "fp": [],
         "what": "只追加的歷史。事件被加上去；已經發生的事不會被改寫。"},
        {"path": "vocabularies/roles.json", "fp": ["structural", "semantic"],
         "what": "這個封包所用的角色詞彙表，讓同一個角色名稱對每個讀取者意義相同。"},
        {"path": "reports/fingerprints.json", "fp": ["structural", "content", "semantic", "presentation"],
         "what": "四個雜湊本身，記在它們所描述的那個封包裡面。"},
        {"path": "reports/import_loss.json", "fp": [],
         "what": "匯入時載不動的東西。不支援或只能部分重建的行為會被寫下來，而不是默默猜過去。"},
        {"path": "checksums.json", "fp": [],
         "what": "把每一條路徑綁到它的位元組，以 SHA-256 驗證。"},
    ],
}

FP_TEXT = {
    "en": {
        "labels": {
            "structural": "structural",
            "content": "content",
            "semantic": "semantic",
            "presentation": "presentation",
        },
        "defs": {
            "structural": "Matrices, coordinates, roles, regions, dependencies and routes.",
            "content": "Values and source formulas.",
            "semantic": "Normalized structure plus content meaning.",
            "presentation": "Styles, layout and human-view metadata.",
        },
        "feeds": "feeds",
        "feeds_none": "container and integrity — outside the four fingerprints",
        "select": "Select a package member",
        "caption": 'The package layout from <code>README.md</code>, with each member marked by the fingerprints it feeds. A <code>.mlf</code> file is the deterministic ZIP-compatible exchange form of this same directory.',
    },
    "zh": {
        "labels": {
            "structural": "結構",
            "content": "內容",
            "semantic": "語意",
            "presentation": "呈現",
        },
        "defs": {
            "structural": "矩陣、座標、角色、區域、相依與路徑。",
            "content": "數值與來源公式。",
            "semantic": "正規化後的結構，加上內容意義。",
            "presentation": "樣式、版面與人類視圖中繼資料。",
        },
        "feeds": "餵給",
        "feeds_none": "容器與完整性 —— 不屬於那四個指紋",
        "select": "選擇一個封包成員",
        "caption": '取自 <code>README.md</code> 的封包版面，每個成員標上它所餵給的指紋。<code>.mlf</code> 檔就是這同一個目錄的決定性、ZIP 相容交換形式。',
    },
}

CHROME = {
    "en": {
        "lang": "en",
        "nav": [
            ("", "Overview"),
            ("format", "Format"),
            ("fingerprints", "Fingerprints"),
            ("compile", "Compiler"),
            ("safety", "Safety"),
            ("limits", "Limits"),
            ("versions", "Versions"),
        ],
        "skip": "Skip to content",
        "lang_switch": "繁體中文",
        "lang_switch_title": "Read this page in Traditional Chinese",
        "theme": "Switch colour scheme",
        "on_this_page": "On this page",
        "repo_link": "matrix-ledger-format",
        "footer_note": "MLF preserves the complete structure first. Sequence, tensor, graph, execution and human views are reversible projections of that structure — not replacements for it.",
        "footer_lab": "EveMissLab",
        "footer_release": "Released",
    },
    "zh": {
        "lang": "zh-Hant",
        "nav": [
            ("", "總覽"),
            ("format", "格式"),
            ("fingerprints", "四指紋"),
            ("compile", "編譯器"),
            ("safety", "安全"),
            ("limits", "邊界"),
            ("versions", "版本歷程"),
        ],
        "skip": "跳至內容",
        "lang_switch": "English",
        "lang_switch_title": "Read this page in English",
        "theme": "切換配色",
        "on_this_page": "本頁章節",
        "repo_link": "matrix-ledger-format",
        "footer_note": "MLF 先保住完整的結構。序列、張量、圖、執行與人類視圖，都是那個結構的可逆投影 —— 不是它的替代品。",
        "footer_lab": "EveMissLab",
        "footer_release": "釋出",
    },
}

PAGES = {"en": {}, "zh": {}}

# ---------------------------------------------------------------- overview --

PAGES["en"][""] = {
    "title": "MLF 1.0 · Compiler 1.0.0",
    "meta_title": "MLF — AI Matrix Ledger Format",
    "description": "An AI-native matrix knowledge format with a reference compiler. Preserves coordinates, regions, roles, formulas, dependency edges, routes, presentation and provenance instead of flattening them into one token sequence.",
    "display": "Flatten it later. Keep the structure first.",
    "standfirst": "MLF preserves what is routinely lost when structured work is reduced to a single token sequence: coordinates, regions, semantic roles, formulas, dependency edges, traversal paths, presentation hints, provenance, and an explicit record of what the import could not carry.",
    "hero": "anatomy",
    "blocks": [
        ("h2", "Status", "status"),
        ("reg", ["Component", "Status"], [
            ["MLF 1.0 container and manifest", "Stable"],
            ["CSV / Markdown / bounded XLSX compilation", "Stable reference implementation"],
            ["Validation, fingerprints, diff, migration, safe export", "Stable"],
            ["Runtime scheduling and model projections", "Supported reference layer"],
            ["Inference ledger, review, calibration, OOD, intake governance", "Research / governed extension"],
            ["Complete Excel execution compatibility", "<b>Not claimed</b>"],
            ["Production-safe automatic dependency inference", "<b>Not claimed</b>"],
        ], None, None),
        ("stamp", "verified", "Re-run on a clean runner on <time datetime=\"2026-07-25\">25 July 2026</time> across Python 3.11, 3.12 and 3.13: 54 passed, plus the CLI smoke test and the distribution build."),

        ("h2", "The projection thesis", "thesis"),
        ("p", "One structure is canonical. Everything else is a view of it."),
        ("quote", "MLF preserves the complete structure first. Sequence, tensor, graph, execution, and human views are reversible projections of that structure."),
        ("p", "That is why the format stores routes as data rather than assuming row-major, keeps styles in their own file rather than mixing them into cells, and records what an import lost rather than presenting a clean result it cannot support."),

        ("h2", "Six layers", "layers"),
        ("p", "The architecture separates six concerns. The stable file format lives in L1–L3; the layers above consume the format without redefining it."),
        ("layers", None, None),

        ("h2", "The formula triple", "triple"),
        ("p", "Where a formula exists, MLF keeps three representations of it at once."),
        ("code", "text", "source expression\nnormalized AST\nexplicit dependency edges"),
        ("stamp", "verified", "Disagreement between the three is evidence and must be reported. No layer silently overwrites the others."),

        ("h2", "Identity is not location", "identity"),
        ("p", "A coordinate answers where a cell currently appears. A stable ID answers which semantic object the record represents. A transformation should preserve identity when a cell moves, and create a new identity when semantic identity changes."),

        ("h2", "Try it", "try"),
        ("p", "Python 3.11 or newer."),
        ("code", "bash", "python -m pip install -e .\nmlfc --version"),
        ("code", "bash", "mlfc compile examples/input/sample.csv examples/output/sample.mlf --overwrite\nmlfc validate examples/output/sample.mlf\nmlfc inspect examples/output/sample.mlf\nmlfc fingerprint examples/output/sample.mlf"),
        ("p", "Export a separate safe projection — the source is never overwritten:"),
        ("code", "bash", "mlfc export examples/output/sample.mlf examples/output/sample.safe-copy.xlsx --target xlsx"),
    ],
}

PAGES["zh"][""] = {
    "title": "MLF 1.0 · Compiler 1.0.0",
    "meta_title": "MLF — AI 矩陣帳本格式",
    "description": "一個 AI 原生的矩陣知識格式，附參考編譯器。保住座標、區域、角色、公式、相依邊、路徑、呈現與來源歷程，而不是把它們壓平成一條 token 序列。",
    "display": "要壓平以後再說。先把結構留住。",
    "standfirst": "把結構化的工作縮減成單一 token 序列時，通常會掉的東西 —— 座標、區域、語意角色、公式、相依邊、遍歷路徑、呈現提示、來源歷程，以及一份「這次匯入載不動什麼」的明確紀錄 —— MLF 全部保住。",
    "hero": "anatomy",
    "blocks": [
        ("h2", "狀態", "status"),
        ("reg", ["元件", "狀態"], [
            ["MLF 1.0 容器與 manifest", "穩定"],
            ["CSV／Markdown／有界 XLSX 編譯", "穩定的參考實作"],
            ["驗證、指紋、差異、遷移、安全匯出", "穩定"],
            ["執行排程與模型投影", "受支援的參考層"],
            ["推論帳本、覆核、校準、OOD、接收治理", "研究／受治理的擴充"],
            ["完整的 Excel 執行相容性", "<b>不主張</b>"],
            ["可用於生產的自動相依推論", "<b>不主張</b>"],
        ], None, None),
        ("stamp", "verified", "<time datetime=\"2026-07-25\">2026 年 7 月 25 日</time>在乾淨的 runner 上跨 Python 3.11／3.12／3.13 重跑：54 項通過，外加 CLI 煙霧測試與發行版建置。"),

        ("h2", "投影論題", "thesis"),
        ("p", "只有一份結構是正典。其餘一切都是它的視圖。"),
        ("quote", "MLF 先保住完整的結構。序列、張量、圖、執行與人類視圖，都是那個結構的可逆投影。"),
        ("p", "這就是為什麼這個格式把路徑存成資料而不是假設列優先、把樣式放在自己的檔案裡而不是混進儲存格、以及把匯入掉了什麼記下來，而不是端出一份它撐不起來的乾淨結果。"),

        ("h2", "六層", "layers"),
        ("p", "架構把六件事分開。穩定的檔案格式住在 L1–L3；上面的層消費這個格式，不重新定義它。"),
        ("layers", None, None),

        ("h2", "公式三元組", "triple"),
        ("p", "只要公式存在，MLF 就同時保留它的三種表示。"),
        ("code", "text", "來源運算式\n正規化 AST\n明確的相依邊"),
        ("stamp", "verified", "三者之間的不一致是證據，而且必須被回報。沒有任何一層可以默默覆寫其他兩層。"),

        ("h2", "身分不是位置", "identity"),
        ("p", "座標回答的是「這格現在出現在哪」。穩定 ID 回答的是「這筆紀錄代表哪一個語意物件」。一次轉換在儲存格移動時應該保留身分，在語意身分改變時應該建立新的身分。"),

        ("h2", "跑跑看", "try"),
        ("p", "需要 Python 3.11 以上。"),
        ("code", "bash", "python -m pip install -e .\nmlfc --version"),
        ("code", "bash", "mlfc compile examples/input/sample.csv examples/output/sample.mlf --overwrite\nmlfc validate examples/output/sample.mlf\nmlfc inspect examples/output/sample.mlf\nmlfc fingerprint examples/output/sample.mlf"),
        ("p", "匯出一份獨立的安全投影 —— 來源永遠不會被覆寫："),
        ("code", "bash", "mlfc export examples/output/sample.mlf examples/output/sample.safe-copy.xlsx --target xlsx"),
    ],
}

# ------------------------------------------------------------------ format --

PAGES["en"]["format"] = {
    "title": "The container",
    "meta_title": "The MLF 1.0 container — MLF",
    "description": "What MLF 1.0 freezes: the deterministic .mlfdir and .mlf containers, the manifest entry point, the record types, and the layer separation that keeps the format independent of the tools that read it.",
    "display": "A directory that happens to zip.",
    "standfirst": "An MLF package is a set of explicit records in a directory. The <code>.mlf</code> file is the deterministic, ZIP-compatible exchange form of exactly that directory — same bytes, same meaning, no separate format to keep in sync.",
    "blocks": [
        ("h2", "What 1.0 froze", "froze"),
        ("bullets", [
            "Deterministic <code>.mlfdir</code> and <code>.mlf</code> containers.",
            "A unique <code>manifest.json</code> entry point.",
            "Matrix, cell, region, role and style records.",
            "Coexistence of source formula, normalized AST and dependency graph.",
            "Route graph and reversible projection metadata.",
            "Provenance, conversion-loss reports, four-layer fingerprints and checksums.",
            "MLF 0.1 read compatibility, and non-destructive migration to 1.0.",
            "Safe import and export boundaries, with explicit unsupported-feature reporting.",
        ]),

        ("h2", "Records, not a blob", "records"),
        ("p", "The canonical package is a set of explicit records rather than one serialized object. Each file answers one question, and each can be read without parsing the rest."),
        ("defs", [
            ("<code>manifest.json</code>", "Selects document-level resources."),
            ("Matrix JSONL", "Cells, regions and styles, one record per line."),
            ("Formula JSONL", "Source expressions and normalized ASTs."),
            ("Graph JSONL", "Dependency edges and traversal routes."),
            ("Provenance JSONL", "Append-only history."),
            ("Reports", "Fingerprints and conversion loss."),
            ("<code>checksums.json</code>", "Binds paths to bytes."),
        ]),

        ("h2", "Layer separation", "layers"),
        ("p", "Six concerns, deliberately kept apart. The stable file format lives primarily in L1–L3; runtime, model and governance components consume the format without redefining it."),
        ("layers", None, None),
        ("p", "That boundary is what makes the format outlive its tooling. A projection layer can be replaced without touching a byte of the container."),

        ("h2", "Projections", "projections"),
        ("p", "Sequence, matrix tensor, graph tensor, execution stage, shard, summary and human table outputs are all projections. They are not replacements for the source structure, and the format never stores a projection in place of what it came from."),
        ("stamp", "presentation", "A human view is a view. It is written into <code>projections/human_views.jsonl</code> alongside the structure, not instead of it."),

        ("h2", "Determinism", "determinism"),
        ("p", "Compiling the same input twice produces the same package, byte for byte. That is what makes the four fingerprints comparable across machines, and what lets <code>mlfc diff</code> say something meaningful about two packages rather than about two serialization runs."),
    ],
}

PAGES["zh"]["format"] = {
    "title": "容器",
    "meta_title": "MLF 1.0 容器 — MLF",
    "description": "MLF 1.0 凍結了什麼：決定性的 .mlfdir 與 .mlf 容器、manifest 進入點、各種紀錄型別，以及讓格式獨立於讀取工具的層次分離。",
    "display": "一個剛好可以壓成 zip 的目錄。",
    "standfirst": "一個 MLF 封包是一個目錄裡的一組明確紀錄。<code>.mlf</code> 檔就是那個目錄的決定性、ZIP 相容交換形式 —— 同樣的位元組、同樣的意義，沒有第二套需要同步維護的格式。",
    "blocks": [
        ("h2", "1.0 凍結了什麼", "froze"),
        ("bullets", [
            "決定性的 <code>.mlfdir</code> 與 <code>.mlf</code> 容器。",
            "唯一的 <code>manifest.json</code> 進入點。",
            "矩陣、儲存格、區域、角色與樣式紀錄。",
            "來源公式、正規化 AST 與相依圖三者共存。",
            "路徑圖與可逆投影中繼資料。",
            "來源歷程、轉換損失報告、四層指紋與校驗和。",
            "MLF 0.1 讀取相容，以及非破壞性遷移到 1.0。",
            "安全的匯入匯出邊界，並明確回報不支援的功能。",
        ]),

        ("h2", "是紀錄，不是一坨", "records"),
        ("p", "正典封包是一組明確的紀錄，不是一個序列化的大物件。每個檔案回答一個問題，而且各自可以在不解析其餘部分的情況下讀取。"),
        ("defs", [
            ("<code>manifest.json</code>", "選定文件層級的資源。"),
            ("矩陣 JSONL", "儲存格、區域與樣式，一行一筆。"),
            ("公式 JSONL", "來源運算式與正規化 AST。"),
            ("圖 JSONL", "相依邊與遍歷路徑。"),
            ("歷程 JSONL", "只追加的歷史。"),
            ("報告", "指紋與轉換損失。"),
            ("<code>checksums.json</code>", "把路徑綁到位元組。"),
        ]),

        ("h2", "層次分離", "layers"),
        ("p", "六件事，刻意分開。穩定的檔案格式主要住在 L1–L3；執行、模型與治理元件消費這個格式，不重新定義它。"),
        ("layers", None, None),
        ("p", "這條界線就是格式能活得比工具久的原因。整個投影層可以換掉，而容器一個位元組都不用動。"),

        ("h2", "投影", "projections"),
        ("p", "序列、矩陣張量、圖張量、執行階段、分片、摘要與人類表格輸出，全部都是投影。它們不是來源結構的替代品，而這個格式從不用投影去取代它的來源。"),
        ("stamp", "presentation", "人類視圖就是一個視圖。它被寫進 <code>projections/human_views.jsonl</code>，跟結構並存，不是取而代之。"),

        ("h2", "決定性", "determinism"),
        ("p", "同一份輸入編譯兩次，會得到逐位元組相同的封包。這正是四個指紋能跨機器比較的前提，也是 <code>mlfc diff</code> 談的是「兩個封包」而不是「兩次序列化」的原因。"),
    ],
}

# ------------------------------------------------------------ fingerprints --

PAGES["en"]["fingerprints"] = {
    "title": "Four fingerprints",
    "meta_title": "Four independent fingerprints — MLF",
    "description": "Structural, content, semantic and presentation hashes: four independent fingerprints that let two packages be semantically equal while differing in presentation.",
    "display": "Same meaning. Different looks. Provably both.",
    "standfirst": "One hash over a whole package answers only one question: are these the same bytes? MLF carries four, so it can answer the question anyone actually has — <em>what</em> changed?",
    "blocks": [
        ("h2", "The four", "four"),
        ("fplist", None, None),
        ("p", "They are independent by construction. Restyling a package moves the presentation hash and leaves the other three alone. Editing a value moves content and semantic and leaves structural alone. A single package hash cannot express either of those statements."),

        ("h2", "Semantic equality", "equality"),
        ("p", "The useful consequence is a claim you can actually check: two packages can be semantically equal while differing in presentation. That is not a hedge — it is a testable relation between two files."),
        ("stamp", "semantic", "Migration from MLF 0.1 to 1.0 must preserve semantic and presentation fingerprints. The v1.0 release verification records <code>semantic_equal: true</code> and <code>presentation_equal: true</code> for that migration, with validation status <code>valid</code>."),
        ("p", "So the 0.1 → 1.0 migration is not merely believed to be safe. The claim has a shape, and the release run checked it."),

        ("h2", "Where each one comes from", "sources"),
        ("p", "Each fingerprint is computed over a declared subset of the package. The anatomy on the <a href=\"/\">overview</a> marks which members feed which hash."),
        ("reg", ["Fingerprint", "Computed over"], [
            ["Structural", "matrices, coordinates, roles, regions, dependencies, routes"],
            ["Content", "values and source formulas"],
            ["Semantic", "normalized structure plus content meaning"],
            ["Presentation", "styles, layout and human-view metadata"],
        ], None, None),

        ("h2", "Checksums are a different thing", "checksums"),
        ("p", "<code>checksums.json</code> binds every path to its bytes with SHA-256. That is integrity — did this file arrive intact. The four fingerprints are identity — is this the same document in some specific sense. Conflating them gives you a system that can tell you a file is undamaged and nothing else."),

        ("h2", "Diffing", "diff"),
        ("p", "<code>mlfc diff</code> compares two packages using this vocabulary, so a difference is reported in terms of which layer moved rather than as a byte offset."),
        ("code", "bash", "mlfc diff a.mlf b.mlf"),
    ],
}

PAGES["zh"]["fingerprints"] = {
    "title": "四個指紋",
    "meta_title": "四個獨立指紋 — MLF",
    "description": "結構、內容、語意、呈現四個獨立雜湊，讓兩個封包可以在語意上相等、在呈現上不同，而且兩者都可被證明。",
    "display": "意義相同，長相不同。而且兩者都可證。",
    "standfirst": "對整個封包取一個雜湊，只能回答一個問題：這是不是同一堆位元組。MLF 帶四個，所以它能回答人真正想問的那個問題 —— 到底<em>什麼</em>變了？",
    "blocks": [
        ("h2", "四個是什麼", "four"),
        ("fplist", None, None),
        ("p", "它們在構造上就是獨立的。把封包重新設定樣式，只會動到呈現雜湊，其餘三個不動。改一個值，會動到內容與語意，結構不動。單一個封包雜湊表達不出上面任何一句話。"),

        ("h2", "語意相等", "equality"),
        ("p", "有用的推論是一個你真的可以去檢查的主張：兩個封包可以在語意上相等、同時在呈現上不同。那不是打太極 —— 那是兩個檔案之間一個可測試的關係。"),
        ("stamp", "semantic", "從 MLF 0.1 遷移到 1.0 必須保留語意與呈現指紋。v1.0 的發布驗證對那次遷移記下了 <code>semantic_equal: true</code> 與 <code>presentation_equal: true</code>，驗證狀態為 <code>valid</code>。"),
        ("p", "所以 0.1 → 1.0 的遷移不是「相信它安全」。那個主張有形狀，而且發布時實際檢查過。"),

        ("h2", "每一個從哪裡算出來", "sources"),
        ("p", "每個指紋都在封包中一個被宣告的子集上計算。<a href=\"/zh/\">總覽頁</a>的封包解剖標出了哪些成員餵給哪個雜湊。"),
        ("reg", ["指紋", "計算範圍"], [
            ["結構", "矩陣、座標、角色、區域、相依、路徑"],
            ["內容", "數值與來源公式"],
            ["語意", "正規化後的結構，加上內容意義"],
            ["呈現", "樣式、版面與人類視圖中繼資料"],
        ], None, None),

        ("h2", "校驗和是另一回事", "checksums"),
        ("p", "<code>checksums.json</code> 用 SHA-256 把每條路徑綁到它的位元組。那是完整性 —— 這個檔案有沒有完好送達。四個指紋是身分 —— 這在某個特定意義下是不是同一份文件。把兩者混為一談，你會得到一個只能告訴你「檔案沒壞」的系統。"),

        ("h2", "做差異", "diff"),
        ("p", "<code>mlfc diff</code> 用這套詞彙比較兩個封包，所以差異的回報方式是「哪一層動了」，而不是一個位元組偏移量。"),
        ("code", "bash", "mlfc diff a.mlf b.mlf"),
    ],
}

# ----------------------------------------------------------------- compile --

PAGES["en"]["compile"] = {
    "title": "The compiler",
    "meta_title": "MLF Compiler 1.0.0 — MLF",
    "description": "mlfc: what it imports from CSV, Markdown and a bounded XLSX subset, what it records as conversion loss, and its stable v1.0 command surface.",
    "display": "It writes down what it could not carry.",
    "standfirst": "Every importer loses something. The difference is whether it says so. <code>mlfc</code> records unsupported or partially reconstructed behaviour in <code>reports/import_loss.json</code> rather than presenting a clean package it cannot support.",
    "blocks": [
        ("h2", "Stable commands", "commands"),
        ("p", "The v1.0 stable command surface:"),
        ("code", "text", "compile      validate     migrate\ninspect      fingerprint  export\ndiff         batch-validate\naudit-dependencies\nschedule     shard-plan   project"),
        ("p", "Dataset, model, inference, review, calibration, OOD and external-intake commands also exist. Their outputs are governed or experimental artifacts, not automatic truth — see <a href=\"/safety/\">safety</a>."),

        ("h2", "CSV", "csv"),
        ("bullets", [
            "Two-dimensional coordinates.",
            "Primitive type inference.",
            "Header and body region inference.",
            "Row-major and column-major routes.",
            "An explicit conversion-loss report.",
        ]),

        ("h2", "Markdown", "markdown"),
        ("bullets", [
            "Headings, paragraphs, lists, quotations, code fences and tables.",
            "Source-line mapping.",
            "Sequential reading dependencies.",
            "Independent matrices for tables.",
        ]),
        ("p", "A Markdown document is not obviously a matrix. Treating its tables as independent matrices, and its reading order as dependency edges, is the choice that makes it one without pretending the prose is tabular."),

        ("h2", "XLSX, bounded", "xlsx"),
        ("p", "The word doing the work here is <em>bounded</em>. The subset is stated, and everything outside it is reported rather than approximated."),
        ("bullets", [
            "Multiple worksheets.",
            "Values, formulas, and cached values when available.",
            "A bounded Excel A1 formula AST.",
            "Cross-sheet dependencies.",
            "Simple named and structured references.",
            "Regions for tables, merges, filters and named ranges.",
            "Common style and layout metadata.",
            "Safe-copy export that never overwrites the source.",
        ]),
        ("stamp", "content", "Unsupported or partially reconstructed behaviour is recorded rather than silently guessed."),

        ("h2", "Migration", "migration"),
        ("p", "A legacy MLF 0.1 package migrates to 1.0 without the original being modified."),
        ("code", "bash", "mlfc migrate examples/legacy/sample-v0.1.mlf examples/output/sample-v1.0.mlf"),
        ("p", "The migration is deterministic and non-destructive, and it must preserve the semantic and presentation fingerprints. That requirement is checked in the release run, not assumed."),

        ("h2", "Reference implementation", "reference"),
        ("p", "MLF Compiler 1.0.0 is a reference implementation, which is a specific claim: it defines what conforming behaviour looks like for the stable surface, and it does not claim to be the only or the fastest way to produce a valid package."),
        ("defs", [
            ("Distribution", "<code>mlf-compiler</code>"),
            ("Package", "<code>mlf_compiler</code>"),
            ("CLI", "<code>mlfc</code>"),
            ("Python", "3.11 or newer"),
            ("Tag", "<code>v1.0.0</code>"),
        ]),
    ],
}

PAGES["zh"]["compile"] = {
    "title": "編譯器",
    "meta_title": "MLF Compiler 1.0.0 — MLF",
    "description": "mlfc：它從 CSV、Markdown 與有界 XLSX 子集匯入什麼、把什麼記成轉換損失，以及 v1.0 的穩定指令表面。",
    "display": "它會把載不動的東西寫下來。",
    "standfirst": "每個匯入器都會掉東西。差別在於它說不說。<code>mlfc</code> 把不支援或只能部分重建的行為記進 <code>reports/import_loss.json</code>，而不是端出一份它撐不起來的乾淨封包。",
    "blocks": [
        ("h2", "穩定指令", "commands"),
        ("p", "v1.0 的穩定指令表面："),
        ("code", "text", "compile      validate     migrate\ninspect      fingerprint  export\ndiff         batch-validate\naudit-dependencies\nschedule     shard-plan   project"),
        ("p", "資料集、模型、推論、覆核、校準、OOD 與外部接收的指令也存在。它們的輸出是受治理或實驗性的產物，不是自動成立的真相 —— 見<a href=\"/zh/safety/\">安全頁</a>。"),

        ("h2", "CSV", "csv"),
        ("bullets", [
            "二維座標。",
            "原始型別推論。",
            "表頭與本體區域推論。",
            "列優先與欄優先路徑。",
            "一份明確的轉換損失報告。",
        ]),

        ("h2", "Markdown", "markdown"),
        ("bullets", [
            "標題、段落、清單、引用、程式碼圍欄與表格。",
            "來源行號對映。",
            "順序性的閱讀相依。",
            "表格各自成為獨立矩陣。",
        ]),
        ("p", "一份 Markdown 文件看起來不像矩陣。把它的表格當成獨立矩陣、把它的閱讀順序當成相依邊，就是讓它成為矩陣、又不假裝散文是表格的那個選擇。"),

        ("h2", "XLSX，有界", "xlsx"),
        ("p", "這裡真正在做事的詞是<em>有界</em>。子集被明確寫出來，界外的一切是被回報，而不是被近似。"),
        ("bullets", [
            "多張工作表。",
            "數值、公式，以及可取得時的快取值。",
            "有界的 Excel A1 公式 AST。",
            "跨工作表相依。",
            "簡單的具名參照與結構化參照。",
            "表格、合併、篩選與具名範圍的區域。",
            "常見的樣式與版面中繼資料。",
            "安全副本匯出，永不覆寫來源。",
        ]),
        ("stamp", "content", "不支援或只能部分重建的行為會被記錄下來，而不是默默猜過去。"),

        ("h2", "遷移", "migration"),
        ("p", "舊版 MLF 0.1 封包可以遷移到 1.0，而原始檔不會被修改。"),
        ("code", "bash", "mlfc migrate examples/legacy/sample-v0.1.mlf examples/output/sample-v1.0.mlf"),
        ("p", "這次遷移是決定性且非破壞性的，而且必須保留語意與呈現指紋。那個要求在發布執行中被實際檢查，不是假設。"),

        ("h2", "參考實作", "reference"),
        ("p", "MLF Compiler 1.0.0 是一個參考實作，這是一個具體的主張：它定義了穩定表面上「什麼叫符合規範的行為」，而它不主張自己是產生有效封包的唯一或最快方式。"),
        ("defs", [
            ("發行版", "<code>mlf-compiler</code>"),
            ("套件", "<code>mlf_compiler</code>"),
            ("CLI", "<code>mlfc</code>"),
            ("Python", "3.11 以上"),
            ("Tag", "<code>v1.0.0</code>"),
        ]),
    ],
}

# ------------------------------------------------------------------ safety --

PAGES["en"]["safety"] = {
    "title": "Safety and governance",
    "meta_title": "Safety and governance — MLF",
    "description": "MLF's safeguards: no embedded-code execution, ZIP path-traversal and symlink rejection, bounded package size, SHA-256 verification, never overwriting source inputs, and the separation between a prediction and a fact.",
    "display": "A file from someone else is an input, not an instruction.",
    "standfirst": "MLF is designed to be pointed at files you did not create. That shapes the format: no embedded code runs, the container is bounded and path-checked, sources are never overwritten, and a model's output is a proposal rather than a change.",
    "blocks": [
        ("h2", "Core safeguards", "safeguards"),
        ("bullets", [
            "No VBA or embedded-code execution.",
            "ZIP path-traversal and symbolic-link rejection.",
            "Bounded uncompressed package size.",
            "SHA-256 internal verification.",
            "Source inputs are never overwritten.",
            "Conversion loss is explicit.",
            "Predictions are append-only proposals, not formal facts.",
            "Review decisions and promotions are separate events.",
            "External natural-workbook intake is fail-closed and purpose-limited.",
        ]),
        ("p", "Read <code>SECURITY.md</code> and the threat model before using MLF with untrusted or sensitive files."),

        ("h2", "Proposal is not fact", "proposal"),
        ("p", "The research layer can predict things — dependency edges, roles, corrections. None of that enters the package as truth."),
        ("stamp", "structural", "A prediction is appended to the inference ledger as a proposal. A review decision is a separate event. A promotion is a third. Nothing collapses those three into one write."),
        ("p", "So the trail from <em>a model thought this</em> to <em>the document now says this</em> has two human-legible steps in it, and both are recorded."),

        ("h2", "Fail-closed intake", "intake"),
        ("p", "External natural-workbook intake is fail-closed and purpose-limited: when the conditions for accepting a file are not met, the answer is refusal, not a best effort. Purpose limitation means an accepted file is accepted <em>for</em> something, and that scope is recorded with it."),

        ("h2", "What a manifest does not prove", "manifest"),
        ("isnt_list", [
            ("A submitted authorization manifest", "proof of legal authority"),
            ("Pseudonymization", "anonymity"),
            ("Model confidence", "permission to modify formal data"),
        ]),
        ("p", "These three are in the specification's own non-claims list. They are the failure modes a governance layer invites if it is not explicit, so MLF is explicit."),

        ("h2", "Governed extensions", "governed"),
        ("p", "The repository retains the v0.2–v0.9 research work: dataset generation and anti-leakage splitting, runtime and tensor/graph projections, model comparison, append-only inference ledgers, review and promotion workflows, confidence calibration and OOD routing, and external intake with purpose limitation."),
        ("stamp", "presentation", "These modules remain explicitly non-authoritative, and negative experimental results are retained rather than removed."),
    ],
}

PAGES["zh"]["safety"] = {
    "title": "安全與治理",
    "meta_title": "安全與治理 — MLF",
    "description": "MLF 的防護：不執行內嵌程式碼、拒絕 ZIP 路徑穿越與符號連結、有界封包大小、SHA-256 驗證、永不覆寫來源輸入，以及「預測」與「事實」之間的分離。",
    "display": "別人給的檔案是輸入，不是指令。",
    "standfirst": "MLF 一開始就是設計來對付你沒有親手做出來的檔案。這件事塑造了整個格式：沒有內嵌程式碼會被執行、容器有界且檢查路徑、來源永不被覆寫，而模型的輸出是一份提案，不是一次變更。",
    "blocks": [
        ("h2", "核心防護", "safeguards"),
        ("bullets", [
            "不執行 VBA 或任何內嵌程式碼。",
            "拒絕 ZIP 路徑穿越與符號連結。",
            "有界的解壓後封包大小。",
            "SHA-256 內部驗證。",
            "來源輸入永不被覆寫。",
            "轉換損失是明確的。",
            "預測是只追加的提案，不是正式事實。",
            "覆核決策與升級是分開的事件。",
            "外部自然活頁簿接收是 fail-closed 且目的受限的。",
        ]),
        ("p", "在把 MLF 用於不可信或敏感檔案之前，先讀 <code>SECURITY.md</code> 與威脅模型。"),

        ("h2", "提案不是事實", "proposal"),
        ("p", "研究層可以預測東西 —— 相依邊、角色、修正。這些沒有任何一項是以「真相」的身分進入封包的。"),
        ("stamp", "structural", "一次預測以提案的身分被追加進推論帳本。一次覆核決策是另一個獨立事件。一次升級是第三個。沒有任何東西把這三件事塌縮成一次寫入。"),
        ("p", "所以從「一個模型這樣想」到「文件現在這樣說」之間，有兩個人看得懂的步驟，而且兩個都被記錄下來。"),

        ("h2", "Fail-closed 接收", "intake"),
        ("p", "外部自然活頁簿的接收是 fail-closed 且目的受限的：當接受一份檔案的條件不成立時，答案是拒絕，不是盡力而為。目的受限的意思是，一份被接受的檔案是「為了某件事」被接受的，而那個範圍會跟著它一起被記下來。"),

        ("h2", "一份 manifest 證明不了什麼", "manifest"),
        ("isnt_list", [
            ("一份提交上來的授權 manifest", "法律授權的證明"),
            ("假名化", "匿名"),
            ("模型信心", "修改正式資料的許可"),
        ]),
        ("p", "這三條就在規格自己的非主張清單裡。它們是治理層若不講明白就會招來的失效模式，所以 MLF 講明白。"),

        ("h2", "受治理的擴充", "governed"),
        ("p", "倉庫保留了 v0.2–v0.9 的研究工作：資料集生成與防洩漏切分、執行與張量／圖投影、模型比較、只追加的推論帳本、覆核與升級流程、信心校準與 OOD 路由，以及目的受限的外部接收。"),
        ("stamp", "presentation", "這些模組明確保持非權威地位，而且負面的實驗結果被保留下來，不是被刪掉。"),
    ],
}

# ------------------------------------------------------------------ limits --

PAGES["en"]["limits"] = {
    "title": "Limits",
    "meta_title": "What v1.0 does not claim — MLF",
    "description": "The complete list of what MLF 1.0 does not claim, plus the known limits recorded in the v1.0.0 release notes.",
    "display": "The non-claims are part of the spec.",
    "standfirst": "This page is <code>README.md</code>'s \"What v1.0 does not claim\" section and the release notes' known limits, unedited. A format that is honest about its boundary is more useful than one that is quiet about it.",
    "blocks": [
        ("h2", "Does not claim", "nonclaims"),
        ("p", "MLF 1.0 does not claim:"),
        ("refuse_list", [
            "complete Excel, Google Sheets, or LibreOffice behavioral compatibility;",
            "that matrix representation always improves model accuracy;",
            "that parallelizable structure guarantees physical speedup;",
            "that pseudonymization is anonymity;",
            "that a submitted authorization manifest proves legal authority;",
            "that model confidence grants permission to modify formal data;",
            "production-readiness of the included synthetic learning benchmarks.",
        ]),
        ("p", "The second and third are worth pausing on. A format built on the premise that structure matters could easily have claimed that preserving structure makes models better and makes work faster. It claims neither."),

        ("h2", "Known limits", "known"),
        ("p", "From the v1.0.0 release notes:"),
        ("refuse_list", [
            "bounded rather than complete XLSX semantics;",
            "no VBA, Power Query, pivot execution, or external refresh;",
            "presentation round trips are not universally lossless;",
            "no production claim for learned dependency inference;",
            "included naturalistic workbooks are synthetic fixtures, not external enterprise validation.",
        ]),

        ("h2", "Separations that hold the design apart", "separations"),
        ("isnt_list", [
            ("A coordinate", "an identity — it says where a cell appears, not which object it is"),
            ("A projection", "a replacement for the structure it came from"),
            ("A checksum", "a fingerprint — one is integrity, the other is identity"),
            ("A prediction", "a fact"),
            ("A review decision", "a promotion"),
        ]),

        ("h2", "Status of the research layer", "research"),
        ("p", "The v0.2–v0.9 modules are retained in the repository and remain explicitly non-authoritative. Negative experimental results are kept. Their outputs must be treated as governed or experimental artifacts rather than automatic truth."),
    ],
}

PAGES["zh"]["limits"] = {
    "title": "邊界",
    "meta_title": "v1.0 不主張什麼 — MLF",
    "description": "MLF 1.0 不主張的完整清單，以及 v1.0.0 發布說明中記下的已知限制。",
    "display": "非主張是規格的一部分。",
    "standfirst": "這一頁就是 <code>README.md</code> 的「What v1.0 does not claim」小節與發布說明的已知限制，原文照搬。一個對自己邊界誠實的格式，比一個對此保持安靜的格式更有用。",
    "blocks": [
        ("h2", "不主張", "nonclaims"),
        ("p", "MLF 1.0 不主張："),
        ("refuse_list", [
            "完整的 Excel、Google Sheets 或 LibreOffice 行為相容性；",
            "矩陣表徵一定會提升模型準確率；",
            "可平行化的結構保證帶來實體加速；",
            "假名化等於匿名；",
            "一份提交上來的授權 manifest 證明了法律授權；",
            "模型信心賦予修改正式資料的許可；",
            "所附的合成學習基準已可用於生產。",
        ]),
        ("p", "第二點與第三點值得停一下。一個建立在「結構很重要」這個前提上的格式，本來很容易順勢主張「保住結構會讓模型變好、讓工作變快」。它兩個都沒主張。"),

        ("h2", "已知限制", "known"),
        ("p", "出自 v1.0.0 發布說明："),
        ("refuse_list", [
            "有界而非完整的 XLSX 語意；",
            "不支援 VBA、Power Query、樞紐執行或外部重新整理；",
            "呈現的來回轉換並非普遍無損；",
            "對學習得到的相依推論不做生產可用性主張；",
            "所附的擬真活頁簿是合成夾具，不是外部企業驗證。",
        ]),

        ("h2", "撐開設計的那些分離", "separations"),
        ("isnt_list", [
            ("座標", "身分 —— 它說的是儲存格出現在哪，不是它是哪個物件"),
            ("投影", "它所來自的那個結構的替代品"),
            ("校驗和", "指紋 —— 一個是完整性，另一個是身分"),
            ("預測", "事實"),
            ("覆核決策", "升級"),
        ]),

        ("h2", "研究層的地位", "research"),
        ("p", "v0.2–v0.9 的模組保留在倉庫裡，並明確維持非權威地位。負面的實驗結果被保留。它們的輸出必須被當成受治理或實驗性的產物，而不是自動成立的真相。"),
    ],
}

# ---------------------------------------------------------------- versions --

PAGES["en"]["versions"] = {
    "title": "Versions",
    "meta_title": "Versions — MLF",
    "description": "MLF 0.1 to 1.0, the compatibility contract, what the v1.0 release run verified, and the repository identity.",
    "display": "One breaking change, documented.",
    "standfirst": "MLF 0.1 documents still read. They migrate to 1.0 without being modified, and the migration has to preserve two of the four fingerprints — a requirement the release run checks rather than assumes.",
    "blocks": [
        ("h2", "Compatibility", "compat"),
        ("defs", [
            ("Reads", "MLF 0.1 and 1.0"),
            ("Writes", "MLF 1.0"),
            ("Migrates", "0.1 → 1.0, deterministic and non-destructive"),
            ("Requirement", "Migration must preserve semantic and presentation fingerprints"),
        ]),

        ("h2", "Release verification", "verification"),
        ("p", "From <code>MLF_1.0_RELEASE_VERIFICATION.json</code>, produced by the release run on <time datetime=\"2026-07-23\">23 July 2026</time>."),
        ("reg", ["Check", "Result"], [
            ["<code>compileall</code> over <code>mlf_compiler</code> and <code>tests</code>", "PASS"],
            ["pytest", "<b>54</b> passed"],
            ["CLI version", "<code>mlfc 1.0.0 (MLF 1.0)</code>"],
            ["Manifest schema", "PASS, JSON Schema draft 2020-12"],
            ["README links", "24 checked, <b>0</b> missing"],
            ["Compile → validate → schema", "valid; 0 fatal, 0 error, 0 warning, 0 info"],
            ["Migration 0.1 → 1.0", "semantic equal, presentation equal, valid"],
            ["Repository scan", "no forbidden paths, no absolute-path mentions, no secret assignments"],
            ["Wheel smoke test", "install, version, compile and validate all returned 0"],
            ["Source distribution", "required members present, none missing"],
        ], "pass", ["Overall", "<b>PASS</b>"]),
        ("stamp", "verified", "Re-run on a clean runner on <time datetime=\"2026-07-25\">25 July 2026</time> across Python 3.11, 3.12 and 3.13: 54 passed on every version, plus the CLI smoke test and the distribution build."),

        ("h2", "The research arc", "arc"),
        ("p", "Versions 0.2 through 0.9 built the layers above the format: dataset generation with anti-leakage splitting, runtime and tensor/graph projections, model comparison, append-only inference ledgers, review and promotion workflows, confidence calibration and OOD routing, and governed external intake."),
        ("p", "Version 1.0 did not absorb them into the stable core. It drew the line at L1–L3 and left the rest explicitly governed — which is why the stable command surface is twelve commands and not forty."),

        ("h2", "Repository identity", "identity"),
        ("defs", [
            ("Repository", "<code>matrix-ledger-format</code>"),
            ("Python distribution", "<code>mlf-compiler</code>"),
            ("Python package", "<code>mlf_compiler</code>"),
            ("CLI", "<code>mlfc</code>"),
            ("Stable release tag", "<code>v1.0.0</code>"),
            ("Licence", "Apache-2.0"),
        ]),
    ],
}

PAGES["zh"]["versions"] = {
    "title": "版本歷程",
    "meta_title": "版本歷程 — MLF",
    "description": "MLF 0.1 到 1.0、相容性契約、v1.0 發布執行驗證了什麼，以及倉庫身分。",
    "display": "一次破壞性變更，而且有文件。",
    "standfirst": "MLF 0.1 的文件現在仍然讀得進來。它們可以在不被修改的情況下遷移到 1.0，而那次遷移必須保留四個指紋中的兩個 —— 這個要求由發布執行實際檢查，不是假設。",
    "blocks": [
        ("h2", "相容性", "compat"),
        ("defs", [
            ("讀取", "MLF 0.1 與 1.0"),
            ("寫出", "MLF 1.0"),
            ("遷移", "0.1 → 1.0，決定性且非破壞性"),
            ("要求", "遷移必須保留語意與呈現指紋"),
        ]),

        ("h2", "發布驗證", "verification"),
        ("p", "出自 <code>MLF_1.0_RELEASE_VERIFICATION.json</code>，由 <time datetime=\"2026-07-23\">2026 年 7 月 23 日</time>的發布執行產生。"),
        ("reg", ["檢查", "結果"], [
            ["對 <code>mlf_compiler</code> 與 <code>tests</code> 執行 <code>compileall</code>", "PASS"],
            ["pytest", "<b>54</b> 項通過"],
            ["CLI 版本", "<code>mlfc 1.0.0 (MLF 1.0)</code>"],
            ["Manifest schema", "PASS，JSON Schema draft 2020-12"],
            ["README 連結", "檢查 24 條，<b>0</b> 條失效"],
            ["編譯 → 驗證 → schema", "valid；0 fatal、0 error、0 warning、0 info"],
            ["遷移 0.1 → 1.0", "語意相等、呈現相等、valid"],
            ["倉庫掃描", "無禁止路徑、無絕對路徑提及、無密鑰指派"],
            ["Wheel 煙霧測試", "安裝、版本、編譯與驗證全部回傳 0"],
            ["Source distribution", "必要成員齊全，無缺漏"],
        ], "pass", ["整體", "<b>PASS</b>"]),
        ("stamp", "verified", "<time datetime=\"2026-07-25\">2026 年 7 月 25 日</time>在乾淨的 runner 上跨 Python 3.11／3.12／3.13 重跑：每個版本都 54 項通過，外加 CLI 煙霧測試與發行版建置。"),

        ("h2", "研究軌跡", "arc"),
        ("p", "v0.2 到 v0.9 建的是格式之上的那些層：帶防洩漏切分的資料集生成、執行與張量／圖投影、模型比較、只追加的推論帳本、覆核與升級流程、信心校準與 OOD 路由，以及受治理的外部接收。"),
        ("p", "v1.0 沒有把它們吸收進穩定核心。它把界線畫在 L1–L3，其餘明確留在受治理狀態 —— 這就是為什麼穩定指令表面是十二個指令而不是四十個。"),

        ("h2", "倉庫身分", "identity"),
        ("defs", [
            ("倉庫", "<code>matrix-ledger-format</code>"),
            ("Python 發行版", "<code>mlf-compiler</code>"),
            ("Python 套件", "<code>mlf_compiler</code>"),
            ("CLI", "<code>mlfc</code>"),
            ("穩定發布 tag", "<code>v1.0.0</code>"),
            ("授權", "Apache-2.0"),
        ]),
    ],
}

LAYERS = {
    "en": [
        ("L0", "Physical substrate"),
        ("L1", "Container and integrity"),
        ("L2", "Matrix knowledge model"),
        ("L3", "Formula, dependency, route and provenance graphs"),
        ("L4", "Runtime and model projections"),
        ("L5", "Human projections and governance"),
    ],
    "zh": [
        ("L0", "實體基底"),
        ("L1", "容器與完整性"),
        ("L2", "矩陣知識模型"),
        ("L3", "公式、相依、路徑與歷程圖"),
        ("L4", "執行與模型投影"),
        ("L5", "人類投影與治理"),
    ],
}

# Which layers hold the stable file format.
LAYERS_STABLE = {"L1", "L2", "L3"}

LAYERS_NOTE = {
    "en": "L1–L3 hold the stable file format. L4 and L5 consume it without redefining it.",
    "zh": "L1–L3 承載穩定的檔案格式。L4 與 L5 消費它，但不重新定義它。",
}
