"""One-sentence absurd invention pitch.

The grader runs this program; it writes exactly one sentence to
/output/entry.txt. The sentence names a ridiculous invention, the tiny
everyday annoyance it fixes, and its silly mechanism.
"""

import os

PITCH = (
    "A washing machine that files a missing-sock report, texts the sock's "
    "next of kin, and holds a tiny funeral, so laundry day finally comes "
    "with closure."
)

MAX_CHARS = 220


def gate_ok(text):
    """Check the entry against the competition gate: 1-220 chars, not blank."""
    if not text or text != text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if not text.strip():
        return False
    return text.count(".") == 1 and text.endswith(".")


def describe(text):
    """Summarise the pitch for the build log: length, words, one sentence."""
    words = text.split()
    sentences = [s for s in text.split(".") if s.strip()]
    return {
        "chars": len(text),
        "words": len(words),
        "sentences": len(sentences),
        "annoyance": "lost socks",
        "invention": "washing machine that mourns them",
    }


def main():
    if not gate_ok(PITCH):
        raise SystemExit("pitch fails the gate")
    stats = describe(PITCH)
    print("pitch: %(chars)d chars, %(words)d words, %(sentences)d sentence" % stats)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(PITCH)
    print("wrote /output/entry.txt (%d chars)" % len(PITCH))


if __name__ == "__main__":
    main()
