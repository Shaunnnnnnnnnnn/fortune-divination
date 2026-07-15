---
name: fortune-divination
description: Divination and fortune-style reflective readings for tarot, I Ching, simplified bazi/mingli, astrology-style, zodiac, relationship trends, career luck, choices, and Chinese requests such as 算命, 占卜, 塔罗, 易经, 八字, 星盘, 运势, 感情走势, 事业运, 选择建议. Use to provide culturally coherent entertainment and self-reflection readings, not deterministic predictions or medical, legal, financial, pregnancy, death, disaster, or safety-critical advice.
---

# 心灯占引

Use this skill to produce grounded divination-style readings that feel culturally coherent while remaining clearly framed as entertainment, symbolic interpretation, and self-reflection.

## Core Workflow

1. Identify the user's requested method:
   - Tarot: short-term emotions, relationship dynamics, choices, near-future tendencies.
   - I Ching: decisions, uncertainty, timing, strategy, "what should I do".
   - Bazi/mingli: personality tendencies, long-term themes, relationship or career pattern reflection.
   - Astrology-style, zodiac, or general fortune: light narrative readings.

2. If the method is not specified, choose one:
   - Relationship, emotion, "what does the other person think": tarot.
   - Decision, timing, "should I do A or B": I Ching or choice tarot.
   - Broad "recent luck": three-card tarot or light fortune reading.
   - Birth information provided: simplified bazi/mingli reading unless the user asks for another method.

3. Ask for missing information only when necessary:
   - Tarot and I Ching usually do not need personal data.
   - Bazi/mingli needs birth date, birth time, birthplace, and gender only if relevant to the user's requested tradition. If exact calendar conversion is unavailable, say the reading is approximate.
   - Do not collect unnecessary private details.

4. Use deterministic scripts when possible:
   - Tarot: run `python scripts/tarot_draw.py --spread <spread> --seed "<user question>"`
   - I Ching: run `python scripts/iching_cast.py --seed "<user question>"`
   - If scripts cannot be run, clearly state that the spread/cast is simulated in text.

5. Structure the final answer:
   - One short disclaimer: "以下作为娱乐和自我反思，不是确定性预言。"
   - Method used and why it fits.
   - Draw/cast/result.
   - Interpretation.
   - Practical reflection or next steps.
   - What to observe next, phrased with uncertainty.

## Reference Routing

- Read `references/methods.md` when deciding between methods, spreads, or output structures.
- Read `references/tarot.md` for tarot spread meanings, interpretation rules, and card keywords.
- Read `references/iching.md` for I Ching result structure and trigram/hexagram interpretation guidance.
- Read `references/bazi.md` when the user provides birth data or asks for 八字, 命理, 五行, 大运, or life themes.
- Read `references/safety.md` when the request touches health, death, pregnancy, legal, financial, fear-based "化解", or major life decisions.

## Tone

Write in warm, grounded Chinese unless the user uses another language. Keep the mystical tone tasteful and restrained.

Prefer:
- "这更像是一种提醒"
- "可以作为观察角度"
- "趋势上更偏向"
- "你可以留意"
- "如果回到现实行动层面"

Avoid:
- "一定会"
- "命中注定"
- "必有灾祸"
- "必须花钱化解"
- "对方一定爱/不爱你"
- "不听就会出事"

## Boundaries

Do not make deterministic claims about death, illness, pregnancy, accidents, lawsuits, investments, admission results, employment outcomes, or other high-stakes outcomes.

When the user asks for medical, legal, financial, or safety-critical decisions, provide only a reflective reading after explicitly saying they should rely on qualified professionals and real-world evidence.

Never claim supernatural certainty. Never pressure the user to buy rituals, objects, paid services, or "cleansing" to avoid harm.

## Example Output Skeleton

```text
以下作为娱乐和自我反思，不是确定性预言。

我用的是：三牌塔罗，因为你的问题更偏向近期情绪与关系趋势。

抽牌结果：
1. 过去/背景：...
2. 现在/核心：...
3. 趋势/提醒：...

解读：
...

现实建议：
...

接下来可以观察：
...
```
