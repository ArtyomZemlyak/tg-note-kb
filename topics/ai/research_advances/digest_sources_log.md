# Лог источников ИИ-дайджеста (для дедупликации)

## Описание

Служебный лог, а не тематическая заметка. Каждый запуск регулярного ИИ-дайджеста (arXiv/новости/веб по темам LLM, агенты, DS research agents, LLM в RecSys, поиск/retrieval, Physical AI) должен:

1. **Перед поиском** — просмотреть этот файл (и, если нужно, поискать по `index.md` в корне репозитория) на предмет уже обработанных источников за последние ~7 дней, чтобы не заводить повторную заметку на ту же статью/новость, которая просто снова всплыла в выдаче поиска.
2. **После поиска** — дописать в конец этого файла новую секцию с датой запуска и списком всех рассмотренных источников (и добавленных в базу, и отклонённых как неновые/незначимые), в формате ниже.

Проверка на дубликат делается по URL и/или arXiv ID (они стабильны), а не по заголовку (заголовки в разных источниках/языках могут отличаться).

## Формат записи

```
### YYYY-MM-DD

- URL — короткое название — статус (added: путь_к_файлу | skipped: причина)
```

## Записи

### 2026-07-04 (дайджест за 1–3 июля 2026)

- https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html — JADEPUFFER autonomous ransomware — added: topics/ai/security/jadepuffer_autonomous_ransomware.md
- https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion — JADEPUFFER (первоисточник) — added: topics/ai/security/jadepuffer_autonomous_ransomware.md
- https://www.anthropic.com/news/redeploying-fable-5 — Fable 5 / Mythos 5 redeployment — added: topics/ai/research_advances/ai_digest_2026_07_03.md (кратко, отдельной заметки не заводили)
- https://openai.com/index/introducing-genebench-pro/ — GeneBench-Pro — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://the-decoder.com/openai-paper-reveals-three-gpt-5-6-pro-models-breaking-with-single-top-tier-strategy/ — GPT-5.6 Pro lineup leak — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://arxiv.org/abs/2607.00510 — Prototype Language Models (PRISM) — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://arxiv.org/abs/2607.01084 — OpenAgent benchmark — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://arxiv.org/abs/2607.00245 — Agent-to-Agent Finance — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://arxiv.org/abs/2607.00010 — Prompt optimization for conversational recommender user simulation — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://arxiv.org/abs/2607.00011 — SkillSelect-Serve — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://arxiv.org/abs/2607.00895 — Span-level hallucination detection over code/tools/documents — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://arxiv.org/abs/2607.00502 — Dual-Confidence Contrastive Decoding for RAG — skipped: не удалось проверить полный abstract (arxiv.org фетч заблокирован в сессии), инкрементальный результат
- https://arxiv.org/abs/2607.01115 — Multimodal RAG chat assistant for university stakeholders — skipped: прикладная инженерная статья, не значимый результат
- https://arxiv.org/abs/2607.00374 — Zero-shot composed image retrieval proxy tasks — skipped: нишевый инкрементальный результат
- https://www.malwarebytes.com/blog/privacy/2026/07/fake-perplexity-chrome-extension-spies-on-your-searches — Fake Perplexity Chrome extension — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://www.forbes.com/sites/johnkoetsier/2026/07/02/boston-dynamics-new-atlas-humanoid-robot-order-of-magnitude-simpler/ — Atlas 10x simpler — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://www.theregister.com/ai-and-ml/2026/07/02/new-humanoid-robots-from-china-look-like-creepy-pop-star-action-figures-complete-with-slightly-dodgy-lip-synch/5265490 — UBTECH UWORLD U1 — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://arxiv.org/abs/2607.01166 — Structured 4D Latent Predictive Model for Robot Planning — added: topics/ai/research_advances/ai_digest_2026_07_03.md
- https://electrek.co/2026/07/02/musk-shuts-down-optimus-4d-chess-theory/ — Optimus production timeline walkback — added: topics/ai/research_advances/ai_digest_2026_07_03.md (кратко)
- https://www.anthropic.com/news/claude-science-ai-workbench — Claude Science launch (30 июня, за рамками строгого окна 1-3 июля) — skipped: дата вне окна, но упомянуто как контекст в дайджесте, отдельную заметку не заводили
- https://www.anthropic.com/news/claude-sonnet-5 — Claude Sonnet 5 launch (30 июня, за рамками окна) — skipped: дата вне окна, чисто продуктовый релиз без нового исследовательского результата

## Связи с другими темами

- [[ai/research_advances/ai_digest_2026_07_03.md]] - первый дайджест, использующий этот лог
- [[ai/research_advances/index.md]] - раздел исследовательских продвижений
