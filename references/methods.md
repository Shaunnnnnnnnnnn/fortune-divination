# Method Selection

Use the least intrusive method that fits the question. Avoid asking for birth data unless the user explicitly wants bazi/mingli or long-term life themes.

## Default Choices

- Relationship, emotions, ambiguity: tarot.
- "What should I choose", "should I wait", timing, strategic uncertainty: I Ching.
- Personality, recurring patterns, long-term career/relationship themes: bazi/mingli if birth data is available; otherwise use a light reflective reading.
- Daily/weekly/monthly luck: single-card or three-card tarot.
- User asks "随便帮我算": three-card tarot unless the question is clearly decision-oriented.

## Tarot Spreads

- Single card: today, quick advice, emotional snapshot.
- Three-card: past/background, present/core, trend/reminder.
- Relationship spread: self, other, relationship field, obstacle, advice.
- Choice spread: option A, option B, hidden factor, advice.

Run `scripts/tarot_draw.py` with:

```bash
python scripts/tarot_draw.py --spread three-card --seed "用户问题"
python scripts/tarot_draw.py --spread relationship --seed "用户问题"
python scripts/tarot_draw.py --spread choice --seed "用户问题"
```

## I Ching Casts

Use I Ching when the user wants direction rather than emotion. Run:

```bash
python scripts/iching_cast.py --seed "用户问题"
```

Interpret the result as:

- 本卦: current situation pattern.
- 动爻: active pressure points or changing factors.
- 变卦: likely direction if the situation keeps moving.
- 行动建议: grounded next action.

## Bazi/Mingli

If the user gives only a Gregorian birthday and no reliable calendar conversion tool is available, do not invent exact four pillars. Say the reading is approximate and focus on symbolic tendencies from season, time period, and self-described context.

If the user provides four pillars directly, interpret them. Keep claims probabilistic and reflective.
