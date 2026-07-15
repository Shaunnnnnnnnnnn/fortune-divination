# 心灯占引

一个给 Codex 用的玄学小摊：会抽塔罗、起易经、聊命理，但坚持不装大师。

`fortune-divination` 是一个面向 Codex 的占卜式自我反思 Skill。它支持塔罗、易经、简化命理和轻量运势解读，适合用来做娱乐、文化解读和自我观察，不用于确定性预测，也不替代医疗、法律、财务等专业建议。

## 支持能力

- 塔罗：单牌、三牌、关系牌阵、选择牌阵
- 易经：本卦、动爻、变卦、行动建议
- 简化命理：性格倾向、事业偏好、关系模式、人生主题
- 轻量运势：近期状态、感情走势、事业运、选择建议

## 安装

把仓库放到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Shaunnnnnnnnnnn/fortune-divination.git ~/.codex/skills/fortune-divination
```

如果已经下载到本地，也可以直接复制：

```bash
cp -R fortune-divination ~/.codex/skills/
```

## 使用示例

```text
使用 $fortune-divination，帮我用三牌塔罗看看我最近事业运如何。
```

```text
使用 $fortune-divination，帮我用易经看看我是否应该换工作。
```

```text
使用 $fortune-divination，帮我做一个简化命理倾向分析。
```

## 脚本测试

塔罗抽牌：

```bash
python3 scripts/tarot_draw.py --spread three-card --seed "我最近事业运如何"
```

易经起卦：

```bash
python3 scripts/iching_cast.py --seed "我是否应该换工作"
```

## 边界

这个 Skill 会把结果明确限定为娱乐和自我反思。它不会做死亡、疾病、灾祸、投资、诉讼、怀孕等高风险事项的确定性预测，也不会鼓励花钱化解、购买符咒或制造恐惧。
