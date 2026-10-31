# Raw data

Kuro's original records, untouched. Everything in this folder is gitignored except this README and `embark/` (Kuro's DNA results are public).

```
data/raw/
├── whatsapp/        WhatsApp chat export: _chat.txt + media (IMG-*.jpg, DOC-*.pdf, …)
└── embark/          Embark DNA export: results CSV + raw genotype (.tped/.tfam)
```

To add a WhatsApp export: in the chat, **More → Export chat → Include media**, then unzip into `whatsapp/`. Keep filenames as exported; `_chat.txt` maps each file to the date it was sent.

Never edit files here. Derived outputs (page images, OCR, extractions) go elsewhere.
