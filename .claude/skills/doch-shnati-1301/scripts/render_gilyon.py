#!/usr/bin/env python3
"""מייצר את גיליון ההזנה לטופס 1301 מתוך netunim.json.

הסקריפט קיים כדי שהסכימה, הבדיקות והפורמט יהיו דטרמיניסטיים — לא תלויים
בקריאה חוזרת של טבלה ארוכה בשיחה.

שימוש:
    python3 render_gilyon.py doch-1301-2025/netunim.json

פלט: gilyon_hazana.md ו-gilyon_hazana.csv לצד קובץ הקלט.
יציאה בקוד 1 אם נמצאה בעיה חוסמת (סכום בלי מקור, סכום לא מספרי).
"""

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

SHEMOT_SHLAVIM = {
    0: "פתיחה ומיפוי התא המשפחתי",
    1: "מסמכים",
    2: "נספח א' — הכנסה מהעסק",
    3: "משכורת בן/בת הזוג",
    4: "ניכויים אישיים",
    5: "זיכויים",
    6: "מס ששולם ונוכה",
    7: "אומדן התוצאה",
    8: "גיליון ההזנה",
}

AMUDOT = {
    "ben_zug_rashum": "בן זוג רשום",
    "ben_zug": "בן/בת הזוג",
}


def shekel(n):
    return f"{n:,.0f}"


def bdok(netunim):
    """בדיקות תקינות. מחזיר (chosmim, azharot)."""
    chosmim, azharot = [], []

    for i, s in enumerate(netunim.get("sechumim", [])):
        tiur = s.get("prit") or f"שורה {i + 1}"

        if not str(s.get("makor") or "").strip():
            chosmim.append(f"«{tiur}» — אין מסמך מקור. סכום בלי מקור לא נכנס לדוח.")

        if not isinstance(s.get("sechum"), (int, float)) or isinstance(s.get("sechum"), bool):
            chosmim.append(f"«{tiur}» — הסכום אינו מספר: {s.get('sechum')!r}")

        if s.get("amuda") not in AMUDOT:
            azharot.append(f"«{tiur}» — לא צוין לאיזו עמודה הסכום שייך (בן זוג רשום / בן-בת הזוג).")

        if not s.get("kod"):
            azharot.append(f"«{tiur}» — קוד השדה לא ידוע. יש להקריא אותו מהמסך לפני ההקלדה.")
        elif not s.get("kod_meumat"):
            azharot.append(f"«{tiur}» — קוד {s['kod']} לא אומת מול הטופס לשנת המס.")

    for mispar, shalav in sorted(netunim.get("shlavim", {}).items()):
        if not shalav.get("ishur"):
            shem = SHEMOT_SHLAVIM.get(int(mispar), "")
            hearot = shalav.get("hearot") or "לא אושר"
            azharot.append(f"שלב {mispar} ({shem}) — {hearot}")

    return chosmim, azharot


def bnei_shurot(netunim):
    lefi_shalav = defaultdict(list)
    for s in netunim.get("sechumim", []):
        lefi_shalav[s.get("shalav", 99)].append(s)
    return dict(sorted(lefi_shalav.items()))


def kod_letzuga(s):
    if not s.get("kod"):
        return "לאמת מול הטופס"
    return s["kod"] if s.get("kod_meumat") else f"{s['kod']} ⚠"


def bne_markdown(netunim, chosmim, azharot):
    shana = netunim.get("shnat_mas", "—")
    out = [f"# גיליון הזנה — טופס 1301, שנת המס {shana}", ""]

    rashum = netunim.get("ben_zug_rashum", {})
    zug = netunim.get("ben_zug", {})
    out += [
        f"**בן זוג רשום:** {rashum.get('shem', '—')} ({rashum.get('tz', '—')})  ",
        f"**בן/בת הזוג:** {zug.get('shem', '—')} ({zug.get('tz', '—')})  ",
        f"**תיק במס הכנסה:** {netunim.get('tik_mas_hachnasa', '—')}",
        "",
        "> הגיליון נועד להקלדה ידנית בדוח המקוון. ⚠ ליד קוד = הקוד לא אומת מול "
        "הטופס לשנת המס; יש לאמת אותו על המסך לפני ההקלדה.",
        "",
    ]

    if chosmim:
        out += ["## ⛔ חוסם — לא להקליד לפני שנפתר", ""]
        out += [f"- {c}" for c in chosmim] + [""]

    sach_lefi_amuda = defaultdict(float)

    for mispar, shurot in bnei_shurot(netunim).items():
        out += [f"## שלב {mispar} — {SHEMOT_SHLAVIM.get(mispar, '')}", ""]
        out += ["| פריט | סכום (₪) | קוד שדה | עמודה | מסמך מקור |",
                "|------|----------|---------|--------|-----------|"]
        for s in shurot:
            sechum = s.get("sechum")
            tzuga = shekel(sechum) if isinstance(sechum, (int, float)) else str(sechum)
            amuda = AMUDOT.get(s.get("amuda"), "—")
            out.append(
                f"| {s.get('prit', '—')} | {tzuga} | {kod_letzuga(s)} | {amuda} | {s.get('makor', '—')} |"
            )
            if isinstance(sechum, (int, float)) and s.get("amuda") in AMUDOT:
                sach_lefi_amuda[s["amuda"]] += sechum
        out.append("")

    if sach_lefi_amuda:
        out += ["## סיכום סכומים לפי עמודה", "",
                "| עמודה | סך הסכומים בגיליון (₪) |", "|--------|------------------------|"]
        for mafteach, sach in sach_lefi_amuda.items():
            out.append(f"| {AMUDOT[mafteach]} | {shekel(sach)} |")
        out += ["",
                "> הסכום כאן הוא סכום אריתמטי של כל השורות בגיליון, לא ההכנסה החייבת. "
                "ניכויים וזיכויים מקטינים את החבות ולכן אינם מתחברים לאותו סך.", ""]

    if azharot:
        out += ["## ⚠️ לבדוק לפני ההגשה", ""]
        out += [f"- {a}" for a in azharot] + [""]

    chaserim = netunim.get("chaserim", [])
    if chaserim:
        out += ["## מסמכים חסרים", "",
                "| מסמך | מאיפה משיגים | שלב |", "|-------|---------------|------|"]
        for c in chaserim:
            out.append(f"| {c.get('mismach', '—')} | {c.get('mekor', '—')} | {c.get('shalav', '—')} |")
        out.append("")

    dgalim = [d for d in netunim.get("dgalim", []) if d.get("status") != "nisgar"]
    if dgalim:
        out += ["## דגלים שנותרו פתוחים", ""]
        out += [f"- שלב {d.get('shalav', '—')}: {d.get('noseh', '—')}" for d in dgalim] + [""]

    out += [
        "---",
        "",
        "הגיליון הוא כלי עזר להקלדה ואינו ייעוץ מס. האחריות על תוכן הדוח המוגש היא "
        "על הנישום. במצבים חריגים — הפסד עסקי, הכנסות מחו״ל, רווח הון, בת זוג "
        "המועסקת בעסק של בן הזוג — יש לפנות לרואה חשבון לפני ההגשה.",
    ]
    return "\n".join(out)


def ktov_csv(netunim, nativ):
    with open(nativ, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["שלב", "פריט", "סכום", "קוד שדה", "קוד אומת", "עמודה", "מסמך מקור"])
        for mispar, shurot in bnei_shurot(netunim).items():
            for s in shurot:
                w.writerow([
                    mispar,
                    s.get("prit", ""),
                    s.get("sechum", ""),
                    s.get("kod") or "לאמת",
                    "כן" if s.get("kod_meumat") else "לא",
                    AMUDOT.get(s.get("amuda"), ""),
                    s.get("makor", ""),
                ])


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    nativ = Path(sys.argv[1])
    if not nativ.exists():
        print(f"לא נמצא קובץ: {nativ}", file=sys.stderr)
        return 2

    try:
        netunim = json.loads(nativ.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"netunim.json לא תקין: {e}", file=sys.stderr)
        return 2

    chosmim, azharot = bdok(netunim)

    md = nativ.parent / "gilyon_hazana.md"
    csv_path = nativ.parent / "gilyon_hazana.csv"
    md.write_text(bne_markdown(netunim, chosmim, azharot), encoding="utf-8")
    ktov_csv(netunim, csv_path)

    print(f"נכתב: {md}")
    print(f"נכתב: {csv_path}")
    print(f"שורות סכום: {len(netunim.get('sechumim', []))} | חוסמים: {len(chosmim)} | אזהרות: {len(azharot)}")

    for c in chosmim:
        print(f"  ⛔ {c}")
    for a in azharot:
        print(f"  ⚠  {a}")

    return 1 if chosmim else 0


if __name__ == "__main__":
    sys.exit(main())
